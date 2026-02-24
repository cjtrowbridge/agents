# Playbook: How to Use Downtime to Improve the Framework

*Status: Draft*

## Objective

Provide a repeatable workflow for using idle time to improve this framework's reliability, consistency, and documentation quality through small maintenance tasks that are tracked in a downtime task catalog and produce report artifacts only (no direct framework changes).

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
* Name each report using the downtime task filename with `.report` inserted before `.md` (for example, `verify_playbook_index_matches_repository.md` -> `verify_playbook_index_matches_repository.report.md`).
* Record when a downtime task was last completed (report generated), not when changes were implemented.

## How to Run a Downtime Session

1.  Read this playbook and scan the ordered downtime task list below.
2.  Pick one task that is due (or overdue) based on the suggested interval.
3.  Open the linked `downtime/*.md` task file and follow its steps.
4.  Create a report artifact in `./downtime/reports/pending/` using the task filename with `.report` inserted before `.md` and `./templates/downtime_report.md`.
5.  Update:
    * the task file's completion history, and
    * this playbook's "Last completed" field for that task.
6.  Verify that no framework files were changed during the downtime task run (report-only output).
7.  Report the new pending downtime report path to the user for review.

## Required Downtime Output

Each downtime task run must produce an individual report artifact in:
* `./downtime/reports/pending/`

Use:
* `./templates/downtime_report.md`

The report must contain:
* observed state/evidence,
* a comprehensive set of suggested changes,
* likely affected files,
* risks/tradeoffs,
* and a proposed order of work if the user approves.

Report filename rule:
* If the task file is `./downtime/x.md`, the report file must be `./downtime/reports/pending/x.report.md`.

## Ordered Downtime Task List

1.  **Manual Playbook Index Verification** - [`./downtime/verify_playbook_index_matches_repository.md`](../downtime/verify_playbook_index_matches_repository.md)
    Last completed: Never
    Suggested interval: Every 14 days

2.  **Audit README and RULES Structure Docs** - [`./downtime/audit_readme_and_rules_structure_docs.md`](../downtime/audit_readme_and_rules_structure_docs.md)
    Last completed: Never
    Suggested interval: Every 14 days

3.  **Review Prompt Tone and Timbre Guidance** - [`./downtime/review_prompt_tone_and_timbre_guidance.md`](../downtime/review_prompt_tone_and_timbre_guidance.md)
    Last completed: Never
    Suggested interval: Every 30 days

4.  **Audit Playbook Overlap and Extract References** - [`./downtime/audit_playbook_overlap_and_extract_references.md`](../downtime/audit_playbook_overlap_and_extract_references.md)
    Last completed: Never
    Suggested interval: Every 30 days

5.  **Review Templates Against Actual Outputs** - [`./downtime/review_templates_against_actual_outputs.md`](../downtime/review_templates_against_actual_outputs.md)
    Last completed: Never
    Suggested interval: Every 30 days

6.  **Record Assimilation Lessons** - [`./downtime/record_assimilation_lessons.md`](../downtime/record_assimilation_lessons.md)
    Last completed: Never
    Suggested interval: After each assimilation review round (or review weekly)

7.  **Review Default Playbook Coverage** - [`./downtime/review_default_playbook_coverage.md`](../downtime/review_default_playbook_coverage.md)
    Last completed: Never
    Suggested interval: Every 45 days

## Notes on Graft 3 (No Scripts by Design)

The earlier idea of a script-based playbook index verifier was intentionally not implemented in this repo because this framework will be forked into many projects and systems. The equivalent check is tracked above as a manual downtime task to preserve portability.

## Verification

* Downtime work uses a linked `./downtime/` task file.
* A report artifact is created in `./downtime/reports/pending/`.
* No framework files are modified by the downtime task run itself (report-only mode).
* Completion timestamps are updated in both the task file and this playbook.

## Lifecycle Compliance

Confirm the workflow follows the required cycle:
Prompt -> Plan (based on a known playbook) -> Request approval -> Execute -> Plan/playbook update -> Docs update -> Verification.

If this occurs inside a git repo:
* Review `git status` and relevant diffs.
* Suggest a commit message that summarizes the completed task.
* Commit after completion.

