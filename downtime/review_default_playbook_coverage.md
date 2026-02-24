# Downtime Task: Review Default Playbook Coverage

## Purpose

Re-evaluate whether the default playbook set is too sparse or too heavy based on repeated agent work and failure modes.

## Suggested Interval

Every 45 days.

## Last Completed

Never

## Downtime Mode (Report-Only)

Use the same base filename as this task file for the report, with `.report` inserted before `.md` (for example, `x.md` -> `x.report.md`).

Do not add/remove/edit playbooks during this task run. Record recommendations and any proposed playbook specs in a downtime report artifact.

## Procedure

1.  Review recent tasks and identify recurring workflows.
2.  Look for repeated failures caused by missing playbooks.
3.  Classify candidates using the framework threshold rule:
    * common,
    * high-risk,
    * multi-step,
    * recurring failure mode.
4.  Decide:
    * add a new playbook,
    * improve an existing playbook,
    * extract a reference/template instead of adding a playbook,
    * remove/deprecate low-value playbooks.
5.  If proposing changes, draft the proposal content (using `./templates/playbook_proposal.md`) inside the downtime report.
6.  Create a report named after this task file with `.report` inserted before `.md` in `./downtime/reports/pending/` using `./templates/downtime_report.md`.

## Evidence to Record

* Candidate workflows reviewed
* Decision (add/improve/extract/defer/remove)
* Proposed playbook/reference/template changes

## Completion History

- Never



