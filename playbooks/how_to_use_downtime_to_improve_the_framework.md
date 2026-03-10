# Playbook: How to Use Downtime to Improve the Framework

*Status: Draft*

## Objective

Provide a repeatable workflow for using idle time to improve this framework's reliability, consistency, documentation quality, and plan-governance integrity through small maintenance tasks that are tracked in a downtime task catalog and produce report artifacts only (no direct framework changes).

## Why This Exists

This repo is designed to evolve through use. Downtime is a good time to:
* reduce drift,
* extract repeated patterns,
* tighten templates,
* and preserve lessons from external framework reviews.

These tasks should be small, low-risk, and documentation-first.

## Downtime Rules

* Downtime tasks are **report-only**. They must not directly modify framework files.
* Prefer short, reversible suggested changes.
* Do not start broad redesigns during downtime.
* If a task uncovers a larger issue, record it as a follow-up and stop.
* Produce one individual report artifact per downtime task run with a comprehensive set of suggested changes.
* Store new downtime reports in `./downtime/reports/pending/`.
* Name each report as `task-base.YYYY-MM-DD-HH-mm-ss.report.md` (example: `verify_playbook_index_matches_repository.2026-03-10-15-00-00.report.md`).
* If that filename already exists, append a deterministic numeric suffix (`-01`, `-02`, ...) before `.report.md`.
* For proposed implementation follow-ups, identify likely affected plan files/checklist items.

## How to Run a Downtime Session

1.  Read this playbook and scan the ordered downtime task list below.
2.  Pick one task that is due (or overdue) based on the suggested interval.
3.  Open the linked `downtime/*.md` task file and follow its steps.
4.  Create a report artifact in `./downtime/reports/pending/` using the timestamped naming rule and `./templates/downtime_report.md`.
5.  Verify that no framework files were changed during the downtime task run (report-only output).
6.  Report the new pending downtime report path to the user for review.

## Required Downtime Output

Each downtime task run must produce an individual report artifact in:
* `./downtime/reports/pending/`

Use:
* `./templates/downtime_report.md`

The report must contain:
* observed state/evidence,
* a comprehensive set of suggested changes,
* likely affected files,
* likely affected plan files/checklist areas,
* risks/tradeoffs,
* and a proposed order of work if the user approves.

Report filename rule:
* If the task file is `./downtime/x.md`, create reports as:
  * `./downtime/reports/pending/x.YYYY-MM-DD-HH-mm-ss.report.md`
  * if needed: `./downtime/reports/pending/x.YYYY-MM-DD-HH-mm-ss-01.report.md`

## Ordered Downtime Task List

`Last completed` fields are informational and should only be updated in a separate approved implementation checkpoint (not during report-only downtime execution).

1.  **Manual Playbook and Plan Index Verification** - [`./downtime/verify_playbook_index_matches_repository.md`](../downtime/verify_playbook_index_matches_repository.md)
    Last completed: Never
    Suggested interval: Every 14 days

2.  **Audit README and RULES Structure Docs** - [`./downtime/audit_readme_and_rules_structure_docs.md`](../downtime/audit_readme_and_rules_structure_docs.md)
    Last completed: Never
    Suggested interval: Every 14 days

3.  **Review Prompt Tone and Timbre Guidance** - [`./downtime/review_prompt_tone_and_timbre_guidance.md`](../downtime/review_prompt_tone_and_timbre_guidance.md)
    Last completed: Never
    Suggested interval: Every 30 days

4.  **Audit Playbook Overlap and Extract Plan-Governance References** - [`./downtime/audit_playbook_overlap_and_extract_references.md`](../downtime/audit_playbook_overlap_and_extract_references.md)
    Last completed: Never
    Suggested interval: Every 30 days

5.  **Review Templates Against Actual Outputs** - [`./downtime/review_templates_against_actual_outputs.md`](../downtime/review_templates_against_actual_outputs.md)
    Last completed: Never
    Suggested interval: Every 30 days

6.  **Record Assimilation Lessons** - [`./downtime/record_assimilation_lessons.md`](../downtime/record_assimilation_lessons.md)
    Last completed: Never
    Suggested interval: After each assimilation review round (or review weekly)

7.  **Review Default Playbook and Plan-Governance Coverage** - [`./downtime/review_default_playbook_coverage.md`](../downtime/review_default_playbook_coverage.md)
    Last completed: Never
    Suggested interval: Every 45 days

## Notes on Scripts and Portability

Script tooling may exist and can be referenced for verification, but downtime runs remain strictly report-only and must not directly apply framework changes.

## Verification

* Downtime work uses a linked `./downtime/` task file.
* A report artifact is created in `./downtime/reports/pending/`.
* No framework files are modified by the downtime task run itself (report-only mode).

## Lifecycle Compliance

Confirm the workflow follows the required cycle:
Prompt -> Select/Create Plan (using relevant playbook guidance) -> Request approval -> Execute approved plan atoms -> Plan update -> Docs update -> Verification.

If this occurs inside a git repo:
* Review `git status` and relevant diffs.
* Ensure today's journal repo work log is updated for the report artifact change.
* Suggest a commit message that summarizes the completed task.
* Commit after approved checkpoint completion.

