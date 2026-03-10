---
plan_id: 2026-03-10-15-07-43_plans-feature-consistency-and-hardening
title: Plans Feature Consistency and Hardening
summary: Resolve policy, tooling, and lifecycle inconsistencies in the plans system rollout.
status: past
created_at: 2026-03-10-15-07-43
---

# Plans Feature Consistency and Hardening

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 0. Capture approved decision set from plan review.
  - [x] 0.1 Record user decision: reject recommendation #2 (no temporary dual key-line acceptance in validator).
  - [x] 0.2 Record user decision: accept all other listed recommendations as the default execution direction.

- [x] 1. Resolve key-line specification mismatch between policy docs and index validation script.
  - [x] 1.1 Proposed solution: define one canonical key-line text and enforce it consistently.
    - [x] 1.1.1 Choose canonical syntax decision (approved).
      - [x] 1.1.1.1 Selected option: keep script format with per-token backticks.
      - [x] 1.1.1.2 Rejected option: do not allow both key-line forms during transition.
    - [x] 1.1.2 Apply decision to policy and workflow docs.
      - [x] 1.1.2.1 Update `README.md`.
      - [x] 1.1.2.2 Update `RULES.md`.
      - [x] 1.1.2.3 Update plan-related playbooks.
    - [x] 1.1.3 Align validator behavior.
      - [x] 1.1.3.1 Update `scripts/regenerate_plan_indexes.py` key-line check accordingly.
    - [x] 1.1.4 Verify.
      - [x] 1.1.4.1 Run `python scripts/regenerate_plan_indexes.py --check`.

- [x] 2. Resolve downtime workflow contradictions and stale "no scripts" guidance.
  - [x] 2.1 Proposed solution: make downtime semantics internally consistent and explicitly script-aware.
    - [x] 2.1.1 Resolve contradiction between report-only mode and completion-history edit instructions.
      - [x] 2.1.1.1 Decide whether completion history updates occur during downtime runs or only in approved implementation follow-ups.
      - [x] 2.1.1.2 Update `playbooks/how_to_use_downtime_to_improve_the_framework.md` to match the decision.
      - [x] 2.1.1.3 Update downtime task files that currently require in-run completion-history edits.
    - [x] 2.1.2 Remove or revise stale "No Scripts by Design" statement.
      - [x] 2.1.2.1 Replace with current reality: scripts may exist; downtime execution remains report-only.
    - [x] 2.1.3 Verify report-only policy alignment.
      - [x] 2.1.3.1 Confirm `RULES.md`, downtime playbook, downtime task files, and downtime report readmes agree.

- [x] 3. Fix upstream/submodule migration and indexing operational gaps.
  - [x] 3.1 Proposed solution: make index tooling repo-root configurable and document host/submodule invocation patterns.
    - [x] 3.1.1 Add repo-root override support in index script.
      - [x] 3.1.1.1 Add `--repo-root` argument to `scripts/regenerate_plan_indexes.py`.
      - [x] 3.1.1.2 Preserve current default behavior when argument is omitted.
    - [x] 3.1.2 Update migration playbook commands for both contexts.
      - [x] 3.1.2.1 Document standalone invocation.
      - [x] 3.1.2.2 Document host-root invocation when framework is mounted as `./agents`.
    - [x] 3.1.3 Update README guidance for upstream adopters.
      - [x] 3.1.3.1 Add explicit note on where plan files live and where to run index command in host repos.
    - [x] 3.1.4 Verify.
      - [x] 3.1.4.1 Run script check in local repo context.

- [x] 4. Clarify plan authority versus change-plan template authority.
  - [x] 4.1 Proposed solution: explicitly distinguish proposal artifacts from execution-authorizing plan files.
    - [x] 4.1.1 Update fallback language in `RULES.md`.
      - [x] 4.1.1.1 State that `templates/change_plan.md` output is a proposal artifact, not execution authority.
    - [x] 4.1.2 Update `templates/change_plan.md`.
      - [x] 4.1.2.1 Add explicit note that execution requires approved checklist items in an active plan file under `plans/`.
    - [x] 4.1.3 Update relevant playbooks.
      - [x] 4.1.3.1 Ensure no wording implies change-plan template alone grants execution authority.
    - [x] 4.1.4 Verify.
      - [x] 4.1.4.1 Run grep checks for stale authority wording.

- [x] 5. Resolve lifecycle semantics gap for intentionally closed checklist items.
  - [x] 5.1 Proposed solution: define and standardize a closure mechanism for de-scoped work.
    - [x] 5.1.1 Choose closure model.
      - [x] 5.1.1.1 Selected option: add a new checkbox state for closed/cancelled.
      - [x] 5.1.1.2 Rejected option: keep existing checkbox set and require standardized closure annotation text.
    - [x] 5.1.2 Update key semantics and lifecycle rules.
      - [x] 5.1.2.1 Update `RULES.md` plan body standards.
      - [x] 5.1.2.2 Update README plan file standard.
      - [x] 5.1.2.3 Update plan template and plan playbooks.
    - [x] 5.1.3 Update validator (if closure model affects syntax).
      - [x] 5.1.3.1 Adjust script checks as required.
    - [x] 5.1.4 Verify.
      - [x] 5.1.4.1 Validate existing plans remain compliant or are migrated.

- [x] 6. Eliminate downtime report filename collision risk.
  - [x] 6.1 Proposed solution: retain task-name traceability while adding uniqueness suffixing.
    - [x] 6.1.1 Define updated naming convention.
      - [x] 6.1.1.1 Candidate format: `task-base.YYYY-MM-DD-HH-mm-ss.report.md` or equivalent.
      - [x] 6.1.1.2 Ensure format is grep-friendly and sortable.
    - [x] 6.1.2 Update naming rules in policy and templates.
      - [x] 6.1.2.1 Update `RULES.md` downtime naming rule.
      - [x] 6.1.2.2 Update downtime readmes and task files.
      - [x] 6.1.2.3 Update `templates/downtime_report.md`.
    - [x] 6.1.3 Verify.
      - [x] 6.1.3.1 Confirm examples and rules are consistent across all downtime docs.

- [x] 7. Enforce filename and slug policy in validation tooling.
  - [x] 7.1 Proposed solution: extend script validation beyond metadata/body checks to filename invariants.
    - [x] 7.1.1 Add filename regex validation to script.
      - [x] 7.1.1.1 Enforce `YYYY-MM-DD-HH-mm-ss_slug.md`.
      - [x] 7.1.1.2 Enforce lowercase hyphenated slug character class.
    - [x] 7.1.2 Add plan-id to filename consistency check.
      - [x] 7.1.2.1 Enforce `plan_id` equals filename stem.
    - [x] 7.1.3 Update docs to mention enforced invariants.
      - [x] 7.1.3.1 Update README and RULES validator expectations.
    - [x] 7.1.4 Verify.
      - [x] 7.1.4.1 Run script check and confirm no false positives on current plans.

- [x] 8. Reduce index ordering churn from filesystem timestamp behavior.
  - [x] 8.1 Proposed solution: evaluate ordering alternatives and choose one explicit stability model.
    - [x] 8.1.1 Define candidate ordering models.
      - [x] 8.1.1.1 Keep `mtime` primary with deterministic tie-breakers.
      - [x] 8.1.1.2 Use `created_at` primary for stable historical ordering.
      - [x] 8.1.1.3 Use hybrid model (`mtime` for active status, `created_at` for past status).
    - [x] 8.1.2 Analyze tradeoffs for multi-machine/team workflows.
      - [x] 8.1.2.1 Evaluate churn risk versus recency visibility.
    - [x] 8.1.3 Apply selected model in policy and script.
      - [x] 8.1.3.1 Update `RULES.md` and README ordering statements.
      - [x] 8.1.3.2 Update index regeneration logic if needed.
    - [x] 8.1.4 Verify.
      - [x] 8.1.4.1 Regenerate indexes and confirm expected deterministic ordering behavior.

- [x] 9. Address plan-first startup friction when `plans/current` is empty.
  - [x] 9.1 Proposed solution: add a lightweight active-plan bootstrap pattern for governance tasks.
    - [x] 9.1.1 Define bootstrap guidance in plan lifecycle playbook.
      - [x] 9.1.1.1 Specify when to create/promote a plan to `plans/current/` at checkpoint start.
      - [x] 9.1.1.2 Specify when to archive after checkpoint completion.
    - [x] 9.1.2 Add explicit "no active plan" quick-start flow.
      - [x] 9.1.2.1 Include minimum required fields and checklist depth for fast startup without quality loss.
    - [x] 9.1.3 Seed one active operational hardening plan if appropriate.
      - [x] 9.1.3.1 Move or create governing plan in `plans/current/` for ongoing framework hardening.
    - [x] 9.1.4 Verify.
      - [x] 9.1.4.1 Confirm startup and execution playbooks can run without ambiguity from a clean `plans/current/`.
