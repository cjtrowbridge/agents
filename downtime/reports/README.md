# Downtime Reports

Downtime tasks are report-only. They do not directly change framework files.

## Purpose

Each downtime task produces an individual report artifact containing a comprehensive set of suggested changes for user review.

## Workflow

1. Run a task from `./downtime/`
2. Create a report in `./downtime/reports/pending/` using `task-base.YYYY-MM-DD-HH-mm-ss.report.md`
3. User reviews and approves/rejects suggestions
4. If reviewed, move or copy the report to `./downtime/reports/reviewed/` (and implement changes in a separate approved task)

## Naming

Use `task-base.YYYY-MM-DD-HH-mm-ss.report.md`.
If needed, append a deterministic numeric suffix (`-01`, `-02`, ...) before `.report.md`.

Examples:

- `./downtime/verify_playbook_index_matches_repository.md` -> `./downtime/reports/pending/verify_playbook_index_matches_repository.2026-03-10-15-00-00.report.md`
- `./downtime/review_templates_against_actual_outputs.md` -> `./downtime/reports/pending/review_templates_against_actual_outputs.2026-03-10-15-00-00.report.md`

Use `./templates/downtime_report.md` as the starting template.

