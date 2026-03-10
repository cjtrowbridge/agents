# Downtime Task: Review Default Playbook and Plan-Governance Coverage

## Purpose

Re-evaluate whether the default playbook set and plan-governance guidance are too sparse or too heavy based on repeated agent work and failure modes.

## Suggested Interval

Every 45 days.

## Last Completed

Never

## Downtime Mode (Report-Only)

Use `task-base.YYYY-MM-DD-HH-mm-ss.report.md` for the report (for example, `x.md` -> `x.2026-03-10-15-00-00.report.md`).
If needed, append a deterministic numeric suffix (`-01`, `-02`, ...) before `.report.md`.

Do not add/remove/edit playbooks during this task run. Record recommendations and any proposed playbook specs in a downtime report artifact.

## Procedure

1.  Review recent tasks and identify recurring workflows.
2.  Look for repeated failures caused by missing playbooks or weak plan-governance boundaries.
3.  Classify candidates using the framework threshold rule:
    * common,
    * high-risk,
    * multi-step,
    * recurring failure mode.
4.  Decide:
    * add a new playbook,
    * improve an existing playbook,
    * improve plan-governance policy/reference/template guidance,
    * extract a reference/template instead of adding a playbook,
    * remove/deprecate low-value playbooks.
5.  If proposing changes, draft the proposal content (using `./templates/playbook_proposal.md`) inside the downtime report.
6.  Audit `./plans/current/` for stale active plans and record archive/reclassification candidates in the report.
7.  Sample active/future plans for decomposition quality and flag checklist items that are not yet atomic.
8.  Create a timestamped report in `./downtime/reports/pending/` using `./templates/downtime_report.md`.

## Evidence to Record

* Candidate workflows reviewed
* Decision (add/improve/extract/defer/remove)
* Proposed playbook/reference/template/plan-governance changes
* Stale `plans/current/` candidates (if any)
* Decomposition quality gaps (if any)

## Completion History

Update this section only in a separate approved implementation checkpoint, not during the report-only downtime run.

- Never



