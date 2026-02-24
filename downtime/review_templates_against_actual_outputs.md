# Downtime Task: Review Templates Against Actual Outputs

## Purpose

Compare `./templates/` files against real agent outputs and tighten placeholders, section order, and required fields.

## Suggested Interval

Every 30 days.

## Last Completed

Never

## Downtime Mode (Report-Only)

Use the same base filename as this task file for the report, with `.report` inserted before `.md` (for example, `x.md` -> `x.report.md`).

Do not edit templates or dependent playbooks/references during this task run. Record template deltas and suggested follow-up edits in a downtime report artifact.

## Procedure

1.  Pick 2-3 recent outputs that should match existing templates (plans, playbook proposals, assimilation reports).
2.  Compare each output to the corresponding template.
3.  Note where templates are:
    * missing useful sections,
    * too verbose,
    * unclear about required vs optional fields,
    * using terms inconsistent with playbooks.
4.  Record suggested template improvements in the downtime report.
5.  If playbooks/references would need updates, record the affected files and suggested wording.
6.  Create a report named after this task file with `.report` inserted before `.md` in `./downtime/reports/pending/` using `./templates/downtime_report.md`.

## Evidence to Record

* Template reviewed
* Mismatches found
* Suggested changes (or "template still fits")

## Completion History

- Never



