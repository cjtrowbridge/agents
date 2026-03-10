# Downtime Task: Record Assimilation Lessons

## Purpose

Convert recent framework comparison work into durable entries in `./docs/assimilations/` so adopted and rejected lessons are preserved.

## Suggested Interval

After each assimilation round, or review weekly if multiple rounds happened.

## Last Completed

Never

## Downtime Mode (Report-Only)

Use `task-base.YYYY-MM-DD-HH-mm-ss.report.md` for the report (for example, `x.md` -> `x.2026-03-10-15-00-00.report.md`).
If needed, append a deterministic numeric suffix (`-01`, `-02`, ...) before `.report.md`.

Do not create or modify assimilation trail entries during this task run. Record proposed entries/edits in a downtime report artifact.

## Procedure

1.  Review recent assimilation reports and notes.
2.  Check whether a corresponding `./docs/assimilations/YYYY-MM-DD-*.md` entry exists.
3.  If missing, draft the proposed entry outline using `./templates/assimilation_trail_entry.md` inside the downtime report.
4.  Record:
    * what was studied,
    * what was adopted,
    * what was rejected/deferred,
    * why.
5.  Include concrete file references for implemented grafts when possible.
6.  Create a timestamped report in `./downtime/reports/pending/` using `./templates/downtime_report.md`.

## Evidence to Record

* Proposed entry path(s)
* Framework(s) covered
* Any pending follow-up items

## Completion History

Update this section only in a separate approved implementation checkpoint, not during the report-only downtime run.

- Never



