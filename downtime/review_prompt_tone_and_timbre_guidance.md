# Downtime Task: Review Prompt Tone and Timbre Guidance

## Purpose

Audit `./references/how_to_shape_agent_tone_and_timbre.md` against recent outputs and identify wording that improves consistency across agents.

## Suggested Interval

Every 30 days.

## Last Completed

Never

## Downtime Mode (Report-Only)

Use `task-base.YYYY-MM-DD-HH-mm-ss.report.md` for the report (for example, `x.md` -> `x.2026-03-10-15-00-00.report.md`).
If needed, append a deterministic numeric suffix (`-01`, `-02`, ...) before `.report.md`.

Do not edit guidance or playbooks/templates during this task run. Record recommended wording refinements in a downtime report artifact.

## Procedure

1.  Read `./references/how_to_shape_agent_tone_and_timbre.md`.
2.  Review a few recent outputs (plans, reviews, proposals, assimilation reports).
3.  Identify recurring tone issues:
    * too vague,
    * too verbose,
    * too soft/hedged,
    * missing tradeoff statements,
    * inconsistent progress updates.
4.  Propose small wording refinements and capture them in the downtime report.
5.  If related playbooks/templates would need updates, list them in the report with suggested wording changes.
6.  Create a timestamped report in `./downtime/reports/pending/` using `./templates/downtime_report.md`.

## Evidence to Record

* Example behavior observed
* Suggested guidance updates (or "no changes")
* Expected impact on consistency

## Completion History

Update this section only in a separate approved implementation checkpoint, not during the report-only downtime run.

- Never



