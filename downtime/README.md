# Downtime Tasks

This directory contains recurring maintenance tasks for improving the framework during idle time.

## Report-Only Rule (Critical)

Downtime tasks are analysis-only.

They must:
* inspect and evaluate the framework,
* produce an individual report artifact with suggested changes,
* and wait for user review/approval before any implementation work.

They must **not** directly modify framework files during the downtime task run.

Each file should define:
* the task purpose,
* the suggested interval,
* the procedure,
* evidence to collect,
* and any optional archival/completion-history convention to be updated only in a separate approved implementation checkpoint.

Use `./playbooks/how_to_use_downtime_to_improve_the_framework.md` to select and run a task.

Write reports to:
* `./downtime/reports/pending/` (new reports awaiting review)

Report naming:
* Use `task-base.YYYY-MM-DD-HH-mm-ss.report.md` (for example, `x.md` -> `x.2026-03-10-15-00-00.report.md`).
* If a collision occurs, append a deterministic numeric suffix (`-01`, `-02`, ...) before `.report.md`.

Use:
* `./templates/downtime_report.md`

