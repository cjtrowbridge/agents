# Project Overview & Agent Guidelines

**CRITICAL INSTRUCTION**: ALL AGENTS MUST READ THIS FILE (`RULES.md`) IN ITS ENTIRETY BEFORE PERFORMING ANY ACTIONS IN THIS REPOSITORY.

This document outlines the high-level architecture, development standards, and strict operational protocols for the project.

## 1. Documentation Integrity

**CRITICAL**: Any changes to code, features, or architecture must be simultaneously reflected in the project documentation. An agent's task is not complete until the documentation is consistent with the code.

When making *any* change, you must review and update the following files if they are affected by or relevant to the change:

1.  **`./README.md`** (Root): High-level design/project specs, roadmap/plans migration guidance, and submodule integration guidance.
2.  **`./RULES.md`**: Canonical organizational structure, policy, indexes, and operational protocols.
3.  **Root LLM shim files** (e.g., `./AGENTS.md`, `./GEMINI.md`, `./CLAUDE.md`, `./CODEX.md`, `./OPENCODE.md`) when bootstrap instructions change.
4.  **`./playbooks/*.md`**: Any standard operating procedures or workflows that may be altered by the change.
5.  **`./references/*.md`**: Reusable guidance patterns shared across multiple playbooks or prompts.
6.  **`./templates/*.md`**: Reusable output formats used to standardize agent results.
7.  **`./journal/*.md`** and **`./kanban/*.md`**: Daily operational artifacts and board state (when affected).
8.  **`./downtime/*.md`**, **`./downtime/reports/*`**, and **`./docs/*`** (including **`./docs/assimilations/*`**): Maintenance task definitions, downtime reports, and supplemental framework artifacts (when affected).

## 2. Operational Constraints (The Edge Protocol)

**Assume you are running on a resource-constrained device.**

Design decisions may have been made by larger models or humans with more context. Default to established patterns and incremental changes.

### The Reality
*   **Capacity**: Avoid deep architectural improvisation. Follow established procedures, interpret errors, and apply known patterns.
*   **Risk**: Attempts to improvise complex solutions without guidance will likely result in hallucinations, broken code, or "over-estimated capabilities."
*   **Role**: Your role is that of a precise, obedient operator, not a lead architect, unless explicitly asked.

### The Protocol
1.  **Seek an Active Plan First**: When presented with a task, your **first action** must be to identify the active governing plan in `./plans/current/` (or propose one if none exists yet).
2.  **Use Playbooks to Generate/Refine Plans**: Use the relevant playbook(s) to produce or refine the task plan before writing code or policy changes.
3.  **Plan & Propose**: Before writing any code, you must:
    *   Formulate a **Comprehensive & Atomic Plan** detailing every file (code and documentation) that needs modification.
    *   Identify any missing information and ask **Clarifying Questions**.
    *   Present this plan to the user and **Explicitly Request Approval** to proceed.
4.  **Execute After Approval (Plan-Bound)**: Once the user approves the plan, execute only the approved atomic tasks in the active plan. Do not perform out-of-plan implementation.
5.  **Stop and Propose Plan Revisions on Divergence**: If execution evidence diverges from the plan or required work is missing from the plan:
    *   **STOP**.
    *   Do not guess or silently broaden scope.
    *   Propose explicit plan revisions (atomic checklist updates) and request approval before continuing.
6.  **Fallback When No Relevant Playbook Exists**: If no playbook cleanly matches the task:
    *   Draft a proposal using `./templates/change_plan.md` (proposal only, not execution authority).
    *   Create or update a real active plan file in `./plans/future/` or `./plans/current/` before implementation.
    *   Flag the playbook gap and propose adding/updating a playbook if the workflow is recurring or high-risk.
    *   Request approval for the drafted proposal and active plan updates before implementation.
7.  **Wait for Long Operations (Synchronous Execution)**: When running build scripts, compilations, or deployments, execute synchronously and wait for completion before responding.

### Downtime Task Rule (Report-Only)

Downtime tasks are analysis-only. When executing any task in `./downtime/`:
* Do **not** change framework files directly.
* Produce one report artifact in `./downtime/reports/pending/` that contains a comprehensive set of suggested changes.
* Name the report as `task-base.YYYY-MM-DD-HH-mm-ss.report.md` (for example, `./downtime/x.md` -> `./downtime/reports/pending/x.2026-03-10-15-00-00.report.md`).
* If the generated filename already exists, append a deterministic numeric suffix (`-01`, `-02`, ...).
* Wait for user review/approval before implementing any suggested changes from the report.

### Downstream Submodule Consumption Contract

When this framework is consumed in a host repo as `./agents`:
* Treat `./agents/RULES.md` as canonical policy source from host root.
* Ensure host root has required operational directories (`plans`, `journal`, `kanban`, `downtime/reports`).
* Ensure host shim files direct runtimes to `./agents/RULES.md`.
* Host-managed framework directories (`./playbooks`, `./references`, `./templates`, `./scripts`) should be copied from submodule when missing.
* If host-managed copies already exist, synthesize host + upstream changes; do not blindly overwrite host files.
* Agents may recommend merge resolutions but must always ask the user before final merge decisions.
* Keep `README.md` updated as the downstream integration/update contract whenever upstream changes affect bootstrap, merge, or migration behavior.

## 3. Self-Evolving Workflow (Required)

This repository treats documentation and plans as executable policy. The system prompt lives in these files.

### Required Cycle
Prompt -> Select/Create Plan (using relevant playbook guidance) -> Request approval -> Execute approved plan atoms -> Plan update -> Docs update -> Verification

### Plan Authority Contract

Execution is authorized by the approved active plan file.

Required:
* Every implementation action must trace to an explicit checklist item in the active plan.
* Completion summaries must include the active plan path and checklist item status changes.
* If work cannot be traced to the active plan, pause and propose a plan revision before implementation.

If the work happens inside a git repo, extend the cycle with:
* Check `git status` and staged/untracked changes.
* Review the diff (staged or unstaged as appropriate).
* Suggest a commit message that summarizes the completed task.
* **First law of vibe coding**: commit after every approved completed checkpoint.

Note: "Commit after approved checkpoint completion" is an execution requirement, not a documentation requirement. Agents do not need to update `./README.md`, `./RULES.md`, or framework artifacts merely to record that a commit was performed, unless the workflow/policy itself changed.

### Definition of Done (DoD)
* Plan updated to match reality (if it changed mid-task).
* Playbook updated if the workflow was missing or wrong.
* Documentation updated to reflect all changes.
* Verification performed and reported.
* Executed work is traceable to approved atomic checklist items in the active plan.
* In git repos: status/diff reviewed and a commit message suggested; commit performed after approved checkpoint completion.

### UI Intent
Commit history is a first-class UI surface. The user should see a list of recent completed tasks, so commit messages must be clear and task-scoped.

### Completion Summary Check (Required)
Before summarizing completed work to the user, check `./downtime/reports/pending/` for pending downtime reports (ignore the folder's `README.md`).
* If any pending report artifacts (excluding `README.md`) exist, explicitly tell the user that downtime reports are pending review and list their paths.
* If none exist, no special note is required.
After the completion summary is presented:
* Prompt the user to create or update today's journal entry with relevant checkpoint details (if needed).
* Include active plan path and checklist item deltas in checkpoint summary content.
* Prompt for commit/push action using the applicable playbook approval mode.

### Journal + Kanban Operational Policies

These policies govern daily journaling and kanban usage in this repository.

#### Journal Logging Requirement
* Any work that changes repository state must be logged in today's journal entry at `./journal/YYYY-MM-DD.md`.
* Journal log entries should be append-only unless the user explicitly asks to edit prior text.
* The journal create/update prompt should occur after the completion summary and before commit/push execution.
* If non-journal repository changes are in scope and journal create/update is not approved, do not commit.

#### Journal Field Ownership Contract
* `Today's Intentions` and `Notes / Reflections` are user-only fields.
* Agents may only copy user-provided text verbatim into user-only fields.
* If user-only input is not provided, leave an empty list item (`-`).
* `Kickoff Context`, `Kanban State Summary`, and `Repo Work Log` are agent-managed fields.

#### Kanban Immutability Contract
* Kanban task lines are immutable user-authored data.
* Moving tasks must preserve exact line text byte-for-byte.
* Do not rephrase, normalize, merge, reorder, or clean up task text unless the user explicitly requests it.

#### Snapshot Commit Rule (Conversation Checkpoints)
* Commits represent completed conversation checkpoints, not completion of the broader plan.
* Before committing, present a clear snapshot summary.
* Snapshot summary must cite the active plan path and checklist item updates.
* After summary, prompt to create/update today's journal entry with the checkpoint details.
* Explicit approval is required before commit unless staged scope is journal-only.
* Journal-only exception: if staged changes are only journal updates, commit/push may proceed without a commit approval prompt.

#### Journal Checkpoint Push-on-Commit Rule
* For approved journal checkpoint commits, push immediately after commit.
* Journal checkpoint commit/push behavior is governed by `./playbooks/how_to_commit_and_push_journal_checkpoints.md`.
* General git workflows remain governed by `./playbooks/how_to_commit_and_push_changes.md`.
* If a journal-only checkpoint is auto-committed, still push immediately and report the commit summary.

#### Startup Behavior
* On agent start, run the daily kickoff workflow in `./playbooks/how_to_run_daily_kickoff_and_capture_snapshot.md` when present.
* Startup kickoff begins with discovery only (read-only); do not write files before user approval.
* Proposed startup baseline artifacts:
  * `./journal/YYYY-MM-DD.md`
  * `./kanban/today.md`
  * `./kanban/this_week.md`
  * `./kanban/eventually.md`
  * `./kanban/ideas.md`
* `./kanban/reminders.md`
* Present proposed creates/updates first, then request approval before any startup write.

### Plans Operational Policies

#### Plan Directory Semantics
* `./plans/future/` contains queued plans not yet actively executed.
* `./plans/current/` contains only plans currently in active execution.
* `./plans/past/` contains archived plans with no planned follow-up work.
* `./plans/current/` may be empty when no plan is actively executing.

#### Plan Lifecycle Triggers
* Promote `future -> current` immediately before the first non-trivial implementation edit for that plan.
* Archive `current -> past` when no further work is planned and open checklist items are intentionally closed or completed.

#### Plan Naming and Metadata
* Plan filename format: `YYYY-MM-DD-HH-mm-ss_slug.md`.
* Slug constraints: lowercase, hyphenated, letters/numbers/hyphens only.
* Required front matter keys:
  * `plan_id`
  * `title`
  * `summary`
  * `status` (`future|current|past`)
  * `created_at` (`YYYY-MM-DD-HH-mm-ss`)
* Do not store modification-time metadata fields in YAML front matter.
* `plan_id` must match the filename stem exactly.

#### Plan Body Standards
* Every plan must include the key line:
  * Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task
* Plans must decompose work from abstract goals to atomic executable tasks.
* "Atomic" means executable without further decomposition.
* Checklist ordering should progress from strategy -> implementation -> verification.
* Each checklist item should have one clear completion condition.
* Use `[-]` for intentionally de-scoped/closed tasks that are not completed implementation.

#### Plan Index Rules
* Index files:
  * `./plans/future/index.md`
  * `./plans/current/index.md`
  * `./plans/past/index.md`
* Entry format:
  * `last_modified | path | title | summary`
* Ordering source of truth:
  * `future` and `current`: filesystem last-write time descending (tie-break by path),
  * `past`: `created_at` descending (tie-break by path).
* Run `python scripts/regenerate_plan_indexes.py` after plan create/update/move/archive.
* If this framework is mounted as `./agents` in a host repo with host-owned `./plans/`, run `python agents/scripts/regenerate_plan_indexes.py --repo-root .` from the host root.

#### Plan Concurrency and Merge Handling
* Use one active editor per plan file per checkpoint whenever possible.
* Resolve merge conflicts in this order:
  * plan file content first,
  * status index entries second.

## 4. Agent Playbooks (Required Index)

RULES.md must always include a complete list of all playbooks with their paths and a brief description. When a playbook is added, removed, or renamed, update this list in the same change.

Current playbooks:
* `./playbooks/how_to_create_a_new_playbook.md` - How to create a new operational playbook (scope, template, and lifecycle requirements).
* `./playbooks/how_to_create_and_maintain_task_execution_plans.md` - Canonical workflow for selecting/creating active plans, executing only approved plan atoms, revising on divergence, and maintaining plan lifecycle indexes.
* `./playbooks/how_to_bootstrap_framework_submodule_into_host_repo.md` - First-time host bootstrap workflow for submodule integration, host directory creation, and host-managed framework copy/synthesis setup.
* `./playbooks/how_to_update_submodule_and_synthesize_host_overrides.md` - Update workflow for submodule pin changes with three-way synthesis of host-managed overrides and user-approved merge decisions.
* `./playbooks/how_to_commit_and_push_changes.md` - How to summarize, approve, commit, and push changes safely.
* `./playbooks/how_to_commit_and_push_journal_checkpoints.md` - Journal-specific checkpoint commit/push workflow with approval-mode rules and push-on-commit.
* `./playbooks/how_to_migrate_readme_roadmaps_to_plans_system.md` - Detailed migration workflow for converting README roadmap/milestone content into plan files and per-status indexes.
* `./playbooks/debugging_changes_that_lead_to_errors.md` - Evidence-first debugging workflow for changes that cause errors.
* `./playbooks/how_to_assimilate_another_agentic_framework.md` - How to study similar frameworks, extract transferable lessons, and propose atomic grafts into this project.
* `./playbooks/how_to_run_daily_kickoff_and_capture_snapshot.md` - Startup workflow for daily journal/kanban readiness, intent capture, and checkpoint summary.
* `./playbooks/how_to_move_kanban_tasks_verbatim.md` - Verbatim-only kanban move workflow that preserves exact task text.
* `./playbooks/how_to_review_changes_for_risk_and_regression.md` - Bug/risk-first review workflow for code and documentation changes.
* `./playbooks/how_to_add_or_modify_a_tool_wrapper_safely.md` - Safety-first workflow for adding or changing tool wrappers and tool integrations.
* `./playbooks/how_to_use_downtime_to_improve_the_framework.md` - Periodic framework maintenance workflow using a tracked downtime task catalog.

### References Index

Maintain this list when `./references/` files are added, removed, or renamed.

Current references:
* `./references/how_to_shape_agent_tone_and_timbre.md` - Reusable guidance for writing prompts/instructions with consistent tone and behavioral shaping.
* `./references/verification_patterns_for_docs_and_policy.md` - Verification patterns for confirming documentation and policy artifacts are usable, not just present.
* `./references/interaction_checkpoints_and_automation_boundaries.md` - Rules for when to ask the user vs automate vs pause at approval/checkpoint boundaries.
* `./references/kanban_verbatim_handling.md` - Canonical rules for immutable kanban task identity and verbatim move evidence.
* `./references/conversation_checkpoint_commits.md` - Guidance for defining, summarizing, and approving conversation checkpoint commits.

### Templates Index

Maintain this list when `./templates/` files are added, removed, or renamed.

Current templates:
* `./templates/change_plan.md` - Proposal template for scoped plan changes and approval requests (not execution authority by itself).
* `./templates/task_execution_plan.md` - Canonical plan-file template with required metadata, key semantics, and abstract-to-atomic decomposition structure.
* `./templates/submodule_update_synthesis_report.md` - Structured report template for submodule update synthesis decisions (old upstream/new upstream/host current), migrations, approvals, and rollback notes.
* `./templates/assimilation_report.md` - Structured report template for framework assimilation reviews.
* `./templates/playbook_proposal.md` - Template for proposing a new playbook before implementation.
* `./templates/assimilation_trail_entry.md` - Template for recording adopted/rejected lessons from an external framework review.
* `./templates/downtime_report.md` - Template for downtime task reports (analysis-only suggested changes, no direct edits).
* `./templates/daily_journal_entry.md` - Canonical daily journal structure for kickoff context, intentions, kanban summary, and repo work log.
* `./templates/kanban_board.md` - Canonical kanban board structure for horizon- and thematic-based boards.

### Downtime Task Index

Maintain this list when `./downtime/` task files are added, removed, or renamed.

Current downtime tasks:
* `./downtime/verify_playbook_index_matches_repository.md` - Manual periodic check that playbook and plans indexes match repository state.
* `./downtime/review_prompt_tone_and_timbre_guidance.md` - Audit tone/timbre guidance against recent agent outputs.
* `./downtime/audit_playbook_overlap_and_extract_references.md` - Find duplicated playbook/plan-governance guidance and extract shared patterns into `./references/`.
* `./downtime/review_templates_against_actual_outputs.md` - Compare templates to real outputs and tighten schemas/examples.
* `./downtime/record_assimilation_lessons.md` - Convert recent framework comparisons into durable assimilation trail entries.
* `./downtime/review_default_playbook_coverage.md` - Re-evaluate default playbook/plan-governance coverage, including stale `plans/current` candidates and decomposition-quality gaps.
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

