# Downtime Task: Review Templates Against Actual Outputs

## Purpose

Compare `./templates/` files against real agent outputs and tighten placeholders, section order, and required fields.

## Suggested Interval

Every 30 days.

## Last Completed

Never

## Downtime Mode (Report-Only)

Use `task-base.YYYY-MM-DD-HH-mm-ss.report.md` for the report (for example, `x.md` -> `x.2026-03-10-15-00-00.report.md`).
If needed, append a deterministic numeric suffix (`-01`, `-02`, ...) before `.report.md`.

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
6.  Create a timestamped report in `./downtime/reports/pending/` using `./templates/downtime_report.md`.

## Evidence to Record

* Template reviewed
* Mismatches found
* Suggested changes (or "template still fits")

## Completion History

Update this section only in a separate approved implementation checkpoint, not during the report-only downtime run.

- Never



