# Downtime Task: Audit Playbook Overlap and Extract References

## Purpose

Find duplicated guidance across playbooks and extract reusable patterns into `./references/` so playbooks stay shorter and more atomic.

## Suggested Interval

Every 30 days.

## Last Completed

Never

## Downtime Mode (Report-Only)

Use the same base filename as this task file for the report, with `.report` inserted before `.md` (for example, `x.md` -> `x.report.md`).

Do not create or modify `./references/` or playbook files during this task run. Record suggested extraction changes in a downtime report artifact.

## Procedure

1.  Scan playbooks for repeated instruction blocks (tone, verification, approval wording, anti-patterns).
2.  Identify duplication that appears in 2+ playbooks.
3.  Decide:
    * keep duplication (if task-specific), or
    * extract to `./references/` (if reusable).
4.  If extracting is recommended, record:
    * the proposed new/updated reference file,
    * the repeated text to replace,
    * the concise playbook-specific replacement wording,
    * and any needed cross-references.
5.  If a new reference file would be added, record the required `RULES.md` reference index update.
6.  Create a report named after this task file with `.report` inserted before `.md` in `./downtime/reports/pending/` using `./templates/downtime_report.md`.

## Evidence to Record

* Duplication found
* Suggested files to change
* New reference to add/update (if any)

## Completion History

- Never



