# Downtime Task: Verify Playbook Index Matches Repository

## Purpose

Manually verify that the playbook list in `RULES.md` matches the actual contents of `./playbooks/`.

## Why This Matters

Index drift breaks discoverability and causes agents to miss valid playbooks or reference deleted ones.

## Suggested Interval

Every 14 days (and after any burst of playbook additions/renames/removals).

## Last Completed

Never

## Downtime Mode (Report-Only)

Use the same base filename as this task file for the report, with `.report` inserted before `.md` (for example, `x.md` -> `x.report.md`).

Do not update `RULES.md` or `README.md` during this task run. Record all suggested fixes in a downtime report artifact instead.

## Procedure

1.  List files in `./playbooks/`.
2.  Compare the list to the "Current playbooks" section in `RULES.md`.
3.  Check for:
    * missing entries,
    * stale entries,
    * renamed files with old paths,
    * misleading descriptions.
4.  If mismatches exist, record the exact `RULES.md` changes needed in the downtime report.
5.  If the README documents playbook inventory or structure and is stale, record the exact `README.md` changes needed in the downtime report.
6.  Create a report named after this task file with `.report` inserted before `.md` in `./downtime/reports/pending/` using `./templates/downtime_report.md`.

## Evidence to Record

Record one line in the completion history with:
* date,
* result (`no drift` or `report created`),
* report path,
* notes on suggested changes (if any).

## Completion History

- Never



