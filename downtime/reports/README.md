# Downtime Reports

Downtime tasks are report-only. They do not directly change framework files.

## Purpose

Each downtime task produces an individual report artifact containing a comprehensive set of suggested changes for user review.

## Workflow

1. Run a task from `./downtime/`
2. Create a report in `./downtime/reports/pending/` using the task filename with `.report` inserted before `.md`
3. User reviews and approves/rejects suggestions
4. If reviewed, move or copy the report to `./downtime/reports/reviewed/` (and implement changes in a separate approved task)

## Naming

Use the same base filename as the downtime task, with `.report` inserted before `.md`.

Examples:

- `./downtime/verify_playbook_index_matches_repository.md` -> `./downtime/reports/pending/verify_playbook_index_matches_repository.report.md`
- `./downtime/review_templates_against_actual_outputs.md` -> `./downtime/reports/pending/review_templates_against_actual_outputs.report.md`

Use `./templates/downtime_report.md` as the starting template.

