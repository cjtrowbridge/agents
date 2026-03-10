#!/usr/bin/env python3
"""Validate plan files and regenerate per-status plan indexes."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path

STATUSES = ("future", "current", "past")
REQUIRED_KEYS = ("plan_id", "title", "summary", "status", "created_at")
FORBIDDEN_MODIFICATION_KEYS = {
    "updated_at",
    "last_updated",
    "last_modified",
    "modified_at",
    "mtime",
    "modification_time",
}
CREATED_AT_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}$")
FILENAME_PATTERN = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2})_(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)\.md$"
)
KEY_LINE = "Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task"


@dataclass(frozen=True)
class PlanEntry:
    status: str
    path: Path
    rel_path_posix: str
    title: str
    summary: str
    plan_id: str
    created_at: dt.datetime
    mtime: float

    @property
    def mtime_label(self) -> str:
        return dt.datetime.fromtimestamp(self.mtime).strftime("%Y-%m-%d-%H-%M-%S")


def parse_front_matter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        raise ValueError("missing YAML front matter delimiters")

    end_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_index = i
            break
    if end_index is None:
        raise ValueError("missing closing YAML front matter delimiter")

    front_matter_lines = lines[1:end_index]
    body_lines = lines[end_index + 1 :]
    data: dict[str, str] = {}

    for raw in front_matter_lines:
        line = raw.strip()
        if not line:
            continue
        if ":" not in line:
            raise ValueError(f"invalid front matter line: {raw}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key:
            raise ValueError(f"empty front matter key in line: {raw}")
        if key in data:
            raise ValueError(f"duplicate front matter key: {key}")
        data[key] = value

    return data, body_lines


def validate_and_collect_plans(repo_root: Path) -> tuple[list[PlanEntry], list[str]]:
    errors: list[str] = []
    entries: list[PlanEntry] = []
    seen_plan_ids: dict[str, str] = {}

    plans_root = repo_root / "plans"
    for status in STATUSES:
        status_dir = plans_root / status
        if not status_dir.exists():
            errors.append(f"missing plans directory: {status_dir}")
            continue

        for plan_path in sorted(status_dir.glob("*.md")):
            if plan_path.name == "index.md":
                continue

            rel_path = plan_path.relative_to(repo_root).as_posix()
            filename_match = FILENAME_PATTERN.match(plan_path.name)
            if not filename_match:
                errors.append(
                    f"{rel_path}: invalid filename (expected YYYY-MM-DD-HH-mm-ss_slug.md with lowercase hyphenated slug)"
                )
                continue

            try:
                metadata, body_lines = parse_front_matter(plan_path)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"{rel_path}: {exc}")
                continue

            missing = [k for k in REQUIRED_KEYS if k not in metadata]
            if missing:
                errors.append(f"{rel_path}: missing required front matter keys: {', '.join(missing)}")
                continue

            forbidden = sorted(k for k in metadata if k in FORBIDDEN_MODIFICATION_KEYS)
            if forbidden:
                errors.append(
                    f"{rel_path}: forbidden modification-time keys in front matter: {', '.join(forbidden)}"
                )

            declared_status = metadata["status"]
            if declared_status not in STATUSES:
                errors.append(f"{rel_path}: invalid status '{declared_status}' (expected one of {STATUSES})")
            if declared_status != status:
                errors.append(
                    f"{rel_path}: status-directory mismatch (status '{declared_status}' in plans/{status}/)"
                )

            created_at = metadata["created_at"]
            if not CREATED_AT_PATTERN.match(created_at):
                errors.append(
                    f"{rel_path}: malformed created_at '{created_at}' (expected YYYY-MM-DD-HH-mm-ss)"
                )
                continue

            try:
                created_at_dt = dt.datetime.strptime(created_at, "%Y-%m-%d-%H-%M-%S")
            except ValueError:
                errors.append(
                    f"{rel_path}: malformed created_at '{created_at}' (expected YYYY-MM-DD-HH-mm-ss)"
                )
                continue

            plan_id = metadata["plan_id"]
            expected_plan_id = plan_path.stem
            if plan_id != expected_plan_id:
                errors.append(
                    f"{rel_path}: plan_id '{plan_id}' must match filename stem '{expected_plan_id}'"
                )

            if plan_id in seen_plan_ids:
                errors.append(
                    f"{rel_path}: duplicate plan_id '{plan_id}' (already seen in {seen_plan_ids[plan_id]})"
                )
            else:
                seen_plan_ids[plan_id] = rel_path

            if KEY_LINE not in "\n".join(body_lines):
                errors.append(f"{rel_path}: missing required key line: {KEY_LINE}")

            entries.append(
                PlanEntry(
                    status=status,
                    path=plan_path,
                    rel_path_posix=rel_path,
                    title=metadata["title"],
                    summary=metadata["summary"],
                    plan_id=plan_id,
                    created_at=created_at_dt,
                    mtime=plan_path.stat().st_mtime,
                )
            )

    return entries, errors


def render_index(status: str, entries: list[PlanEntry]) -> str:
    lines = [
        f"# {status.capitalize()} Plans Index",
        "",
        "Format: `last_modified | path | title | summary`",
        "",
    ]
    for entry in entries:
        lines.append(
            f"{entry.mtime_label} | {entry.rel_path_posix} | {entry.title} | {entry.summary}"
        )
    return "\n".join(lines).rstrip() + "\n"


def write_atomic(path: Path, content: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8", newline="\n")
    tmp.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate plan files and regenerate per-status indexes.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate and check whether indexes are up to date without rewriting files.",
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Repository root containing plans/ (defaults to parent directory of this script).",
    )
    args = parser.parse_args()

    if args.repo_root is None:
        repo_root = Path(__file__).resolve().parents[1]
    else:
        repo_root = Path(args.repo_root).resolve()

    entries, errors = validate_and_collect_plans(repo_root)
    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    by_status: dict[str, list[PlanEntry]] = {status: [] for status in STATUSES}
    for entry in entries:
        by_status[entry.status].append(entry)
    for status in STATUSES:
        if status == "past":
            by_status[status].sort(key=lambda e: (-e.created_at.timestamp(), e.rel_path_posix))
        else:
            by_status[status].sort(key=lambda e: (-e.mtime, e.rel_path_posix))

    check_failures = 0
    for status in STATUSES:
        index_path = repo_root / "plans" / status / "index.md"
        rendered = render_index(status, by_status[status])
        if args.check:
            current = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
            if current != rendered:
                check_failures += 1
                print(f"OUTDATED: {index_path.relative_to(repo_root).as_posix()}")
        else:
            write_atomic(index_path, rendered)
            print(f"UPDATED: {index_path.relative_to(repo_root).as_posix()}")

    if args.check and check_failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
