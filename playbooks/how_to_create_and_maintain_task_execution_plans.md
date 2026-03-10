# Playbook: Create and Maintain Task Execution Plans

*Status: Draft*

## Objective

Define a repeatable workflow for creating, selecting, executing, revising, and archiving plan files so all implementation remains bound to approved atomic checklist items.

## Prerequisites

* Read `README.md` and `RULES.md`.
* Plans directories exist:
  * `./plans/future/`
  * `./plans/current/`
  * `./plans/past/`
* Per-folder indexes exist:
  * `./plans/future/index.md`
  * `./plans/current/index.md`
  * `./plans/past/index.md`
* Plan format requirements:
  * YAML front matter with `plan_id`, `title`, `summary`, `status`, `created_at`
  * Key line must be: Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task
  * Decomposition from abstract goals to atomic executable tasks
  * Template: `./templates/task_execution_plan.md`

## Step-by-Step Instructions

1. **Find or Confirm Active Plan**
   * Check `./plans/current/index.md` for an existing active plan.
   * If multiple candidates exist, ask the user which plan governs this checkpoint.
   * If no suitable active plan exists, continue to Step 2.

2. **Create or Select the Governing Plan**
    * If work is new:
       * Create a new plan in `./plans/future/` using `YYYY-MM-DD-HH-mm-ss_slug.md`.
       * Keep slug lowercase and hyphenated (letters, numbers, hyphens only).
       * Keep `plan_id` exactly equal to the filename stem.
       * Decompose tasks down to atomic checklist items before requesting implementation approval.
       * Use a minimum quick-start scaffold:
         * top-level objective checklist item,
         * decomposed implementation workstream items,
         * decomposed verification workstream items.
    * If work is already in-flight:
       * Move/promote the plan to `./plans/current/` immediately before the first non-trivial implementation edit.

3. **Bind the Task Run to Plan Items**
   * Identify exact checklist items that will be worked in this checkpoint.
   * Include the active plan path and targeted checklist item IDs in the change plan summary.
   * Treat `./templates/change_plan.md` output as proposal-only context; it does not authorize execution by itself.
   * Do not execute work that is not explicitly represented by approved checklist items.

4. **Request Approval Before Execution**
   * Present:
     * active plan path,
     * checklist items to execute,
     * files expected to change,
     * verification approach.
   * Ask for explicit approval before making non-trivial file edits.

5. **Execute Only Approved Atomic Plan Tasks**
    * Implement exactly the approved checklist scope.
    * Mark completed items as `[x]`.
    * Mark uncertain outcomes as `[?]` with follow-up validation items.
    * Mark intentionally de-scoped work as `[-]` (closed).

6. **Handle Mid-Run Divergence**
   * If new required work appears or assumptions fail:
     * Stop implementation.
     * Propose a plan revision with atomic checklist updates.
     * Request explicit approval for the revised plan scope before continuing.

7. **Maintain Plan Lifecycle State**
   * `future -> current` immediately before the first non-trivial implementation edit.
   * `current -> past` when no further work is planned and all remaining items are either complete or intentionally closed.
   * Keep only actively executed plans in `./plans/current/`.
   * It is valid for `./plans/current/` to be empty when no plan is active.

8. **Refresh Plan Indexes**
   * Ensure each affected status index includes current entries in one-line format:
     * `last_modified | path | title | summary`
   * Order:
     * `future/current`: filesystem last-write time descending.
     * `past`: `created_at` descending.
   * Run `python scripts/regenerate_plan_indexes.py` after plan create/update/move/archive.
   * If this framework is mounted as `./agents` in a host repo using host-owned `./plans/`, run:
     * `python agents/scripts/regenerate_plan_indexes.py --repo-root .`

9. **Checkpoint Summary Requirements**
   * Before commit/push flow, summarize:
     * active plan path,
     * checklist items changed,
     * lifecycle moves (`future/current/past`) if any,
     * index files refreshed.
   * Ensure journal checkpoint details reference the same plan path and checklist deltas.

10. **Verification**
   * Confirm all implemented changes map to checklist items in the active plan.
   * Confirm plan front matter and key line remain valid.
   * Confirm plan indexes match filesystem state for affected plan directories.
   * Confirm no work was executed outside approved plan scope.

## Anti-Patterns

* Executing work without an active approved plan.
* Treating playbooks as direct execution authority without plan binding.
* Expanding scope silently instead of proposing plan revisions.
* Marking plan items complete without corresponding implementation evidence.
* Leaving stale plans in `./plans/current/` after work has ended.

## Lifecycle Compliance

Prompt -> Select/Create Plan (using relevant playbook guidance) -> Request approval -> Execute approved plan atoms -> Plan update -> Docs update -> Verification.

If this occurs inside a git repo:
* Review `git status` and relevant diffs.
* Ensure checkpoint summary includes active plan path and checklist item changes.
* Suggest a commit message that summarizes the completed checkpoint.
* Commit after approved checkpoint completion.
