# Playbook: Daily Kickoff and Snapshot Capture

*Status: Stable*

## Objective
Run a startup workflow that discovers daily artifact state, gets approval before any writes, captures daily intent, applies verbatim kanban changes, and prepares a checkpoint summary.

## Prerequisites

- Read `README.md` and `RULES.md` before making changes.
- Journal template available at `./templates/daily_journal_entry.md`.
- Kanban template available at `./templates/kanban_board.md`.

## Step-by-Step Instructions

1. **Resolve Local Date**
   - Determine current local date as `YYYY-MM-DD`.

2. **Discover Today's Journal State (Read-Only)**
   - Target path: `./journal/YYYY-MM-DD.md`.
   - Record whether it exists.

3. **Discover Baseline Board State (Read-Only)**
   - Required board files:
     - `./kanban/today.md`
     - `./kanban/this_week.md`
     - `./kanban/eventually.md`
     - `./kanban/ideas.md`
     - `./kanban/reminders.md`
   - Record which files exist and which are missing.

4. **Present Startup Status and Ask Write Approval**
   - Report:
     - what exists already,
     - what is missing,
     - what files would be created/updated.
   - Ask for explicit approval before creating or editing files.

5. **Create Missing Artifacts (After Approval)**
   - If `./journal/YYYY-MM-DD.md` is missing, create from `./templates/daily_journal_entry.md` and replace all `YYYY-MM-DD` tokens with the resolved date.
   - For each missing baseline board, create from `./templates/kanban_board.md` and replace placeholders:
     - `<Board Name>`
     - `<time_horizon_or_theme>`
     - `<why this board exists>`

6. **Startup Interaction**
   - Greet the user with:
     - what exists today,
     - what was created,
     - what information is still needed.
   - Ask the smallest set of questions required to capture:
     - `Today's Intentions` from the user (verbatim user text only),
     - immediate task flow details.

7. **Confirm Active Plan Before Non-Trivial Execution**
   - Identify the governing active plan path in `./plans/current/` for non-trivial repository changes.
   - If no suitable active plan exists, create a quick-start plan scaffold via `./playbooks/how_to_create_and_maintain_task_execution_plans.md` and request approval before implementation.
   - Quick-start scaffold minimum:
     - objective checklist item,
     - implementation checklist decomposition,
     - verification checklist decomposition.
   - Promote `future -> current` immediately before the first non-trivial implementation edit.
   - Map intended checkpoint work to explicit plan checklist items.

8. **Apply Kanban Changes**
   - If task moves are requested, follow `./playbooks/how_to_move_kanban_tasks_verbatim.md`.

9. **Prepare Journal Update Content**
   - Capture `Today's Intentions` using verbatim user-provided text only.
   - Do not author, infer, summarize, or rewrite intentions.
   - If the user does not provide intentions, keep `Today's Intentions` as an empty list item (`-`).
   - Draft kanban state summary and any moves performed.
   - Draft required repo work log entries for repository changes made during the checkpoint.

10. **Present Snapshot Summary**
   - List files changed.
   - List what was added/updated.
   - List active plan path and checklist items updated in this checkpoint.
   - List kanban moves with exact task lines.

11. **Prompt Journal Create/Update and Ask Save Approval**
   - After summary, ask whether to create or update today's journal entry with the drafted checkpoint details.
   - Ask user to approve saving the snapshot edits.
   - If approved, save files.

12. **Commit + Push Journal Checkpoint**
   - For journal checkpoint commits, follow `./playbooks/how_to_commit_and_push_journal_checkpoints.md`.

## Verification

- `./journal/YYYY-MM-DD.md` exists and has kickoff/intent/log sections filled.
- `Today's Intentions` contains user-provided text or an empty list item (`-`).
- Required baseline boards exist in `./kanban/`:
  - `today.md`
  - `this_week.md`
  - `eventually.md`
  - `ideas.md`
  - `reminders.md`
- Any moved kanban lines are unchanged verbatim in destination.
- Snapshot summary matches actual diffs.
- Active plan path and checklist deltas are captured when non-trivial repository work occurred.

## Lifecycle Compliance

Prompt -> Select/Create Plan (using relevant playbook guidance) -> Request approval -> Execute approved plan atoms -> Plan update -> Docs update -> Verification.

If this occurs inside a git repo:
- Review `git status` and relevant diffs.
- Suggest a commit message that summarizes the completed task.
- Prompt journal create/update after summary; apply approved journal edits before commit.
- Commit after approved checkpoint completion.
