# Downtime Task: Audit README and RULES Structure Docs

## Purpose

Verify that `README.md` and `RULES.md` accurately describe the current project organization and indexed framework artifacts.

## Suggested Interval

Every 14 days (and after adding/removing directories or major files).

## Last Completed

Never

## Downtime Mode (Report-Only)

Use `task-base.YYYY-MM-DD-HH-mm-ss.report.md` for the report (for example, `x.md` -> `x.2026-03-10-15-00-00.report.md`).
If needed, append a deterministic numeric suffix (`-01`, `-02`, ...) before `.report.md`.

Do not edit `README.md` or `RULES.md` during this task run. Record all suggested changes in a downtime report artifact.

## Procedure

1.  Compare actual top-level directories/files to the structure documented in `README.md`.
2.  Verify `RULES.md` indexes for:
    * playbooks,
    * references,
    * templates,
    * downtime tasks.
3.  Check descriptions still match file purpose after edits/renames.
4.  If drift exists, record the exact `README.md` and/or `RULES.md` changes needed in the downtime report.
5.  If drift is caused by a repeated workflow gap, record a suggested follow-up playbook/reference/template change in the downtime report.
6.  Create a timestamped report in `./downtime/reports/pending/` using `./templates/downtime_report.md`.

## Evidence to Record

* Drift found (yes/no)
* Suggested files to update (if any)
* Follow-up issues noted

## Completion History

Update this section only in a separate approved implementation checkpoint, not during the report-only downtime run.

- Never



