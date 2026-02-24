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
* and a completion history entry format.

Use `./playbooks/how_to_use_downtime_to_improve_the_framework.md` to select and run a task.

Write reports to:
* `./downtime/reports/pending/` (new reports awaiting review)

Report naming:
* Use the same base filename as the downtime task, with `.report` inserted before `.md` (for example, `x.md` -> `x.report.md`).

Use:
* `./templates/downtime_report.md`

