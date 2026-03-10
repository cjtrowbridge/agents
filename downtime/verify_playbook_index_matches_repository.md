# Downtime Task: Verify Playbook and Plan Indexes Match Repository

## Purpose

Manually verify that:
* the playbook list in `RULES.md` matches `./playbooks/`, and
* plan index files in `./plans/*/index.md` match actual plan files.

## Why This Matters

Index drift breaks discoverability and causes agents to miss valid playbooks/plans or reference deleted artifacts.

## Suggested Interval

Every 14 days (and after any burst of playbook/plan additions, moves, renames, or removals).

## Last Completed

Never

## Downtime Mode (Report-Only)

Use `task-base.YYYY-MM-DD-HH-mm-ss.report.md` for the report (for example, `x.md` -> `x.2026-03-10-15-00-00.report.md`).
If needed, append a deterministic numeric suffix (`-01`, `-02`, ...) before `.report.md`.

Do not update `RULES.md` or `README.md` during this task run. Record all suggested fixes in a downtime report artifact instead.

## Procedure

1.  List files in `./playbooks/`.
2.  Compare the list to the "Current playbooks" section in `RULES.md`.
3.  Check playbook index for:
    * missing entries,
    * stale entries,
    * renamed files with old paths,
    * misleading descriptions.
4.  For each plan status directory (`future`, `current`, `past`):
    * list plan files excluding `index.md`,
    * compare against corresponding `./plans/<status>/index.md` entries,
    * verify one-line format `last_modified | path | title | summary`,
    * verify ordering rules (`future/current` by filesystem last-write, `past` by `created_at`),
    * spot-check plan metadata validity (required front matter keys, status-directory alignment, well-formed `created_at`, filename format, `plan_id == filename stem`, required key line, and no modification-time fields in YAML).
5.  Record drift for `RULES.md`, `README.md`, and/or plan index files as suggested changes in the downtime report.
6.  Create a timestamped report in `./downtime/reports/pending/` using `./templates/downtime_report.md`.

## Evidence to Record

Record in the report metadata:
* date,
* result (`no drift` or `report created`),
* report path,
* notes on suggested changes (if any).

## Completion History

Update this section only in a separate approved implementation checkpoint, not during the report-only downtime run.

- Never



