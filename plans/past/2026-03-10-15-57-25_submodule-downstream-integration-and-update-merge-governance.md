---
plan_id: 2026-03-10-15-57-25_submodule-downstream-integration-and-update-merge-governance
title: Submodule Downstream Integration and Update Merge Governance
summary: Define and document how this framework is consumed as a submodule, bootstrapped into host roots, and safely merged during upstream updates.
status: past
created_at: 2026-03-10-15-57-25
---

# Submodule Downstream Integration and Update Merge Governance

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 0. Capture decisions from question review.
  - [x] 0.1 Record decision for host ownership of framework operation directories.
    - [x] 0.1.1 Selected: copy framework operational directories/files to host root when missing.
    - [x] 0.1.2 Selected: if host already has those files/directories, synthesize updates to include new upstream features while preserving host changes.
    - [-] 0.1.3 Closed alternative: submodule-first references for playbooks/templates/references/scripts by default.
  - [x] 0.2 Record decision for merge conflict handling authority.
    - [x] 0.2.1 Selected: agents provide merge recommendations.
    - [x] 0.2.2 Selected: agents must always ask the user before final merge resolution choices.
  - [x] 0.3 Record decision scope.
    - [x] 0.3.1 Selected: all other recommendations are accepted as default direction.

- [x] 1. Define the canonical downstream operating model for submodule usage.
  - [x] 1.1 Specify that this framework is intended to be included as a git submodule in host repositories.
    - [x] 1.1.1 Document expected submodule mount path convention.
      - [x] 1.1.1.1 Standardize primary example path as `./agents`.
  - [x] 1.2 Define host-root versus submodule ownership boundaries.
    - [x] 1.2.1 List artifacts that are host-owned and copied/synthesized at host root.
      - [x] 1.2.1.1 Include root shim files (for example `./AGENTS.md`) in host-owned set.
      - [x] 1.2.1.2 Include host operational directories to be copied/synthesized (for example `./playbooks/` and other selected framework directories) in host-owned set.
    - [x] 1.2.2 List artifacts that remain submodule-owned and referenced in place.
      - [x] 1.2.2.1 Include `./agents/RULES.md` as canonical submodule policy source.
      - [x] 1.2.2.2 Include submodule scripts/templates/references paths that host shims should reference.

- [x] 2. Define host bootstrap copy/sync contract.
  - [x] 2.1 Specify exact host-root files/directories that must be created on initial integration.
    - [x] 2.1.1 Define required host-root shim files.
      - [x] 2.1.1.1 Define baseline content for host `./AGENTS.md` to point at `./agents/RULES.md`.
    - [x] 2.1.2 Define required host operational directories.
      - [x] 2.1.2.1 Define minimum host `./plans/future`, `./plans/current`, `./plans/past`.
      - [x] 2.1.2.2 Define minimum host `./journal/` and `./kanban/`.
      - [x] 2.1.2.3 Define minimum host `./downtime/reports/pending` and `./downtime/reports/reviewed`.
      - [x] 2.1.2.4 Apply selected policy for `./playbooks/`, `./references/`, `./templates/`, and `./scripts/`:
        - [x] 2.1.2.4.1 Copy these to host root when absent.
        - [x] 2.1.2.4.2 When host versions exist, synthesize host+upstream updates preserving host intent.
        - [x] 2.1.2.4.3 Require explicit user approval before applying synthesis resolutions.
  - [x] 2.2 Define bootstrap sequence and idempotency rules.
    - [x] 2.2.1 Write ordered first-time setup steps.
      - [x] 2.2.1.1 Include submodule add/init/update steps.
      - [x] 2.2.1.2 Include host copy/create steps for required artifacts.
    - [x] 2.2.2 Add idempotent rerun guidance.
      - [x] 2.2.2.1 Define overwrite/merge safety expectations for reruns.

- [x] 3. Update shim/path guidance so host-root agents resolve submodule policy/tooling correctly.
  - [x] 3.1 Define canonical host shim wording.
    - [x] 3.1.1 Ensure host `./AGENTS.md` directs runtimes to `./agents/RULES.md`.
      - [x] 3.1.1.1 Include explicit host-root path language to avoid path ambiguity.
  - [x] 3.2 Define path resolution rules for tool/script/template usage.
    - [x] 3.2.1 Document when commands should call `python agents/scripts/...` from host root.
      - [x] 3.2.1.1 Include `--repo-root .` usage when host-owned `./plans/` are authoritative.
    - [x] 3.2.2 Document when host-local copies override submodule defaults.
      - [x] 3.2.2.1 Define precedence order as `host override` for playbooks/templates/references/scripts, with submodule as upstream source for synthesis.

- [x] 4. Define submodule update workflow with synthesis merge of host customizations.
  - [x] 4.1 Specify update triggers and preparation steps.
    - [x] 4.1.1 Define when host maintainers should update submodule pin.
      - [x] 4.1.1.1 Include periodic cadence and change-triggered cadence guidance.
    - [x] 4.1.2 Define pre-update inventory of host-local modifications.
      - [x] 4.1.2.1 Enumerate host-customized playbooks/templates/references/shims before merge.
  - [x] 4.2 Define synthesis merge procedure.
    - [x] 4.2.1 Compare old upstream, new upstream, and host-local current versions.
      - [x] 4.2.1.1 Require three-way synthesis for customized host files.
    - [x] 4.2.2 Define merge resolution policy.
      - [x] 4.2.2.1 Preserve host-specific behavior unless it conflicts with new safety-critical upstream policy.
      - [x] 4.2.2.2 Integrate upstream improvements that close known bugs/policy gaps.
      - [x] 4.2.2.3 Always present synthesis recommendations and request explicit user approval before final merge decisions.
    - [x] 4.2.3 Define merge output quality bar.
      - [x] 4.2.3.1 Require integrated output to include both host custom intent and upstream hardening changes.
  - [x] 4.3 Define post-merge validation.
    - [x] 4.3.1 Validate path correctness for host and submodule references.
      - [x] 4.3.1.1 Run grep checks for stale/incorrect old paths.
    - [x] 4.3.2 Validate plan/index tooling against host source-of-truth paths.
      - [x] 4.3.2.1 Run `python agents/scripts/regenerate_plan_indexes.py --check --repo-root .` from host root.

- [x] 5. Define migration/integration handling for upstream framework changes.
  - [x] 5.1 Define change classes that require host migration work.
    - [x] 5.1.1 Path/structure changes.
      - [x] 5.1.1.1 Define required host refactor steps when paths move/rename.
    - [x] 5.1.2 Policy/schema changes.
      - [x] 5.1.2.1 Define host plan/template/playbook migration tasks for schema or key changes.
    - [x] 5.1.3 Script behavior changes.
      - [x] 5.1.3.1 Define host command/mode updates when script flags/semantics change.
  - [x] 5.2 Define migration execution workflow.
    - [x] 5.2.1 Require a migration checklist during submodule update.
      - [x] 5.2.1.1 Include per-change-class verification criteria.
    - [x] 5.2.2 Require rollback/fallback path for failed migrations.
      - [x] 5.2.2.1 Define minimal rollback guidance for submodule pin and synthesized host files.

- [x] 6. Update README as the canonical downstream contract.
  - [x] 6.1 Add explicit "Submodule Integration" section.
    - [x] 6.1.1 Document first-time setup in host repo.
      - [x] 6.1.1.1 Show submodule add/init/update command sequence.
      - [x] 6.1.1.2 Show required host-root copy/create steps and directories.
    - [x] 6.1.2 Document path model for host versus submodule references.
      - [x] 6.1.2.1 Include explicit examples for AGENTS/RULES/script/template resolution.
  - [x] 6.2 Add explicit "Submodule Update + Synthesis Merge" section.
    - [x] 6.2.1 Document three-way synthesis merge expectations for host-customized files.
      - [x] 6.2.1.1 Include specific note that playbooks are likely host-modified and must be synthesized, not blindly overwritten.
    - [x] 6.2.2 Document migration/integration checklist requirements.
      - [x] 6.2.2.1 Include verification commands and expected outcomes.
  - [x] 6.3 Add explicit "Downstream Compatibility Maintenance" section.
    - [x] 6.3.1 Require README updates whenever upstream changes affect downstream integration/update behavior.
      - [x] 6.3.1.1 Require durable changelog-style notes for downstream-impacting changes.
    - [x] 6.3.2 Define non-breaking upgrade expectations and known breaking-change protocol.
      - [x] 6.3.2.1 Define required migration notice content when breaking changes are unavoidable.

- [x] 7. Update supporting framework artifacts for consistency with README contract.
  - [x] 7.1 Update root shim files in this repository to reflect downstream host usage patterns.
    - [x] 7.1.1 Ensure shim language is consistent across `AGENTS.md`, `CODEX.md`, `CLAUDE.md`, `GEMINI.md`, `OPENCODE.md`.
      - [x] 7.1.1.1 Ensure host-root guidance references `./agents/RULES.md` consistently.
  - [x] 7.2 Add or update playbook(s) for downstream integration/update operations.
    - [x] 7.2.1 Add/update bootstrap playbook for first-time submodule integration and host-root setup.
      - [x] 7.2.1.1 Include host directory creation and copy/sync contract.
    - [x] 7.2.2 Add/update update playbook for submodule bump + synthesis merge + migration checks.
      - [x] 7.2.2.1 Include mandatory verification and rollback paths.
  - [x] 7.3 Update templates/references if new recurring output structures are needed.
    - [x] 7.3.1 Add/update template for submodule update merge reports/checklists if required.
      - [x] 7.3.1.1 Ensure template captures host-local diffs, upstream changes, synthesis decisions, and migration steps.

- [x] 8. Verification and rollout completion criteria.
  - [x] 8.1 Validate documentation coherence and path correctness.
    - [x] 8.1.1 Run grep checks for stale path assumptions and conflicting guidance.
      - [x] 8.1.1.1 Confirm no conflicting instructions remain about host-root vs submodule ownership.
  - [x] 8.2 Validate tooling guidance.
    - [x] 8.2.1 Confirm all script examples are executable with declared working directory assumptions.
      - [x] 8.2.1.1 Confirm host-mode examples use `agents/scripts/... --repo-root .` where applicable.
  - [x] 8.3 Validate index and policy consistency.
    - [x] 8.3.1 Run `python scripts/regenerate_plan_indexes.py --check` in framework repo.
      - [x] 8.3.1.1 Confirm no validation/index drift after doc/playbook/template updates.
  - [x] 8.4 Finalize lifecycle state.
    - [x] 8.4.1 Move plan `future -> current` before first non-trivial implementation edit.
    - [x] 8.4.2 Move plan `current -> past` when all checklist items are complete or intentionally closed.
