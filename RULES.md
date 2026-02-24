# Project Overview & Agent Guidelines

**CRITICAL INSTRUCTION**: ALL AGENTS MUST READ THIS FILE (`RULES.md`) IN ITS ENTIRETY BEFORE PERFORMING ANY ACTIONS IN THIS REPOSITORY.

This document outlines the high-level architecture, development standards, and strict operational protocols for the project.

## 1. Documentation Integrity

**CRITICAL**: Any changes to code, features, or architecture must be simultaneously reflected in the project documentation. An agent's task is not complete until the documentation is consistent with the code.

When making *any* change, you must review and update the following files if they are affected by or relevant to the change:

1.  **`./README.md`** (Root): High-level design/project specs, roadmap, and submodule integration guidance.
2.  **`./RULES.md`**: Canonical organizational structure, policy, indexes, and operational protocols.
3.  **Root LLM shim files** (e.g., `./AGENTS.md`, `./GEMINI.md`, `./CLAUDE.md`, `./CODEX.md`, `./OPENCODE.md`) when bootstrap instructions change.
4.  **`./playbooks/*.md`**: Any standard operating procedures or workflows that may be altered by the change.
5.  **`./references/*.md`**: Reusable guidance patterns shared across multiple playbooks or prompts.
6.  **`./templates/*.md`**: Reusable output formats used to standardize agent results.
7.  **`./downtime/*.md`**, **`./downtime/reports/*`**, and **`./docs/assimilations/*`**: Maintenance task definitions, downtime reports, and the assimilation trail (when affected).

## 2. Operational Constraints (The Edge Protocol)

**Assume you are running on a resource-constrained device.**

Design decisions may have been made by larger models or humans with more context. Default to established patterns and incremental changes.

### The Reality
*   **Capacity**: Avoid deep architectural improvisation. Follow established procedures, interpret errors, and apply known patterns.
*   **Risk**: Attempts to improvise complex solutions without guidance will likely result in hallucinations, broken code, or "over-estimated capabilities."
*   **Role**: Your role is that of a precise, obedient operator, not a lead architect, unless explicitly asked.

### The Protocol
1.  **Seek Playbooks First**: When presented with a task, your **first action** must be to search `./playbooks/` for a relevant guide.
2.  **Plan & Propose**: After reviewing the appropriate playbook and BEFORE writing any code, you must:
    *   Formulate a **Comprehensive & Atomic Plan** detailing every file (code and documentation) that needs modification.
    *   Identify any missing information and ask **Clarifying Questions**.
    *   Present this plan to the user and **Explicitly Request Approval** to proceed.
3.  **Execute After Approval**: Once the user approves the plan, carry it out strictly according to the playbook. Do not deviate.
4.  **Wait for Long Operations (Synchronous Execution)**: When running build scripts, compilations, or deployments, execute synchronously and wait for completion before responding.
5.  **Stop on Ambiguity**: If you cannot find a playbook describing exactly what you are trying to do:
    *   **STOP**.
    *   Do not guess.
    *   Do not try to "figure it out."
    *   **Report**: Inform the user: *"I do not have a playbook for [Task Name]. Please create a playbook for this task so I can execute it reliably."*

### Downtime Task Rule (Report-Only)

Downtime tasks are analysis-only. When executing any task in `./downtime/`:
* Do **not** change framework files directly.
* Produce one report artifact in `./downtime/reports/pending/` that contains a comprehensive set of suggested changes.
* Name the report using the downtime task filename with `.report` inserted before `.md` (for example, `./downtime/x.md` -> `./downtime/reports/pending/x.report.md`).
* Wait for user review/approval before implementing any suggested changes from the report.

## 3. Self-Evolving Workflow (Required)

This repository treats documentation and plans as executable policy. The system prompt lives in these files.

### Required Cycle
Prompt -> Plan (based on a known playbook) -> Request approval -> Execute -> Plan/playbook update -> Docs update -> Verification

If the work happens inside a git repo, extend the cycle with:
* Check `git status` and staged/untracked changes.
* Review the diff (staged or unstaged as appropriate).
* Suggest a commit message that summarizes the completed task.
* **First law of vibe coding**: commit after every change is completed.

Note: "Commit after completion" is an execution requirement, not a documentation requirement. Agents do not need to update `./README.md`, `./RULES.md`, or framework artifacts merely to record that a commit was performed, unless the workflow/policy itself changed.

### Definition of Done (DoD)
* Plan updated to match reality (if it changed mid-task).
* Playbook updated if the workflow was missing or wrong.
* Documentation updated to reflect all changes.
* Verification performed and reported.
* In git repos: status/diff reviewed and a commit message suggested; commit performed after completion.

### UI Intent
Commit history is a first-class UI surface. The user should see a list of recent completed tasks, so commit messages must be clear and task-scoped.

### Completion Summary Check (Required)
Before summarizing completed work to the user, check `./downtime/reports/pending/` for pending downtime reports (ignore the folder's `README.md`).
* If any pending report artifacts (excluding `README.md`) exist, explicitly tell the user that downtime reports are pending review and list their paths.
* If none exist, no special note is required.

## 4. Agent Playbooks (Required Index)

RULES.md must always include a complete list of all playbooks with their paths and a brief description. When a playbook is added, removed, or renamed, update this list in the same change.

Current playbooks:
* `./playbooks/how_to_create_a_new_playbook.md` - How to create a new operational playbook (scope, template, and lifecycle requirements).
* `./playbooks/how_to_commit_and_push_changes.md` - How to summarize, approve, commit, and push changes safely.
* `./playbooks/debugging_changes_that_lead_to_errors.md` - Evidence-first debugging workflow for changes that cause errors.
* `./playbooks/how_to_assimilate_another_agentic_framework.md` - How to study similar frameworks, extract transferable lessons, and propose atomic grafts into this project.
* `./playbooks/how_to_review_changes_for_risk_and_regression.md` - Bug/risk-first review workflow for code and documentation changes.
* `./playbooks/how_to_add_or_modify_a_tool_wrapper_safely.md` - Safety-first workflow for adding or changing tool wrappers and tool integrations.
* `./playbooks/how_to_use_downtime_to_improve_the_framework.md` - Periodic framework maintenance workflow using a tracked downtime task catalog.

### References Index

Maintain this list when `./references/` files are added, removed, or renamed.

Current references:
* `./references/how_to_shape_agent_tone_and_timbre.md` - Reusable guidance for writing prompts/instructions with consistent tone and behavioral shaping.
* `./references/verification_patterns_for_docs_and_policy.md` - Verification patterns for confirming documentation and policy artifacts are usable, not just present.
* `./references/interaction_checkpoints_and_automation_boundaries.md` - Rules for when to ask the user vs automate vs pause at approval/checkpoint boundaries.

### Templates Index

Maintain this list when `./templates/` files are added, removed, or renamed.

Current templates:
* `./templates/change_plan.md` - Atomic implementation plan + approval request template.
* `./templates/assimilation_report.md` - Structured report template for framework assimilation reviews.
* `./templates/playbook_proposal.md` - Template for proposing a new playbook before implementation.
* `./templates/assimilation_trail_entry.md` - Template for recording adopted/rejected lessons from an external framework review.
* `./templates/downtime_report.md` - Template for downtime task reports (analysis-only suggested changes, no direct edits).

### Downtime Task Index

Maintain this list when `./downtime/` task files are added, removed, or renamed.

Current downtime tasks:
* `./downtime/verify_playbook_index_matches_repository.md` - Manual periodic check that `RULES.md` playbook index matches `./playbooks/`.
* `./downtime/review_prompt_tone_and_timbre_guidance.md` - Audit tone/timbre guidance against recent agent outputs.
* `./downtime/audit_playbook_overlap_and_extract_references.md` - Find duplicated guidance and extract shared patterns into `./references/`.
* `./downtime/review_templates_against_actual_outputs.md` - Compare templates to real outputs and tighten schemas/examples.
* `./downtime/record_assimilation_lessons.md` - Convert recent framework comparisons into durable assimilation trail entries.
* `./downtime/review_default_playbook_coverage.md` - Re-evaluate whether new default playbooks should be added or removed.
* `./downtime/audit_readme_and_rules_structure_docs.md` - Check `README.md`/`RULES.md` structure documentation against actual repo layout.

### Downtime Reports

Downtime task outputs are stored in:
* `./downtime/reports/pending/` - Reports awaiting user review
* `./downtime/reports/reviewed/` - Reports already reviewed (and optionally acted on later)

## 5. Project Organization

The README must be updated when project organization changes in a way that affects the documented structure, submodule integration usage, or user-facing workflow guidance (for example, new top-level directories/files, renamed major folders, or changes to any structure explicitly listed in the README).

## 6. Logging & Debugging Standards
*   **Requirement**: The project must include comprehensive logging and debugging capabilities.
*   **Implementation**: Any new feature or module must include appropriate logging statements to facilitate troubleshooting and performance monitoring.

