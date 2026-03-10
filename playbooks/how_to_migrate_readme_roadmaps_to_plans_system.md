# Playbook: Migrate README Roadmaps to the Plans System

*Status: Draft*

## Objective
Provide a repeatable, low-risk workflow for migrating roadmap/milestone content from README-style sections into structured plan files under `plans/future`, `plans/current`, and `plans/past`.

## Prerequisites

- Read `README.md` and `RULES.md` first.
- Ensure the plans directories exist:
  - `plans/future/`
  - `plans/current/`
  - `plans/past/`
- Ensure per-folder index files exist (or create them during migration):
  - `plans/future/index.md`
  - `plans/current/index.md`
  - `plans/past/index.md`
- Tooling:
  - `rg` for discovery
  - shell access for file operations
- Metadata policy:
  - Plan front matter includes `plan_id`, `title`, `summary`, `status`, `created_at`.
  - `plan_id` must match the filename stem.
  - Do not store modification-time fields in YAML.
  - Index ordering uses:
    - `future/current`: filesystem last-write time.
    - `past`: `created_at`.

## Step-by-Step Instructions

1. **Determine Migration Scope**
   - Identify all roadmap-like sources in the target repository:
     - `README.md`
     - `docs/*.md`
     - `ROADMAP*.md`
     - release planning docs
   - Use discovery search from repo root:
     - `rg -n "(?i)roadmap|milestone|phase|next steps|upcoming|plan" README.md docs *.md`
   - If this framework is mounted as `./agents` in a host repo, run discovery from the host root and migrate host roadmap content, not just framework docs.

2. **Build a Migration Map Before Editing**
   - Create a temporary mapping table in the active work note or change plan with columns:
     - source file
     - source heading/line
     - old roadmap item text
     - target plan file path
     - target checklist location
   - Do not delete old roadmap sections until every source item has a target mapping.

3. **Normalize and Classify Work Items**
   - Group roadmap entries into coherent initiatives (one initiative per plan file unless scope is tiny).
   - Assign each initiative to exactly one status directory:
     - `future`: planned but not actively executed.
     - `current`: actively executed now.
     - `past`: completed/retired with no planned follow-up.
   - If status is ambiguous, default to `future` and add an explicit task to reclassify later.

4. **Create Plan Files from Roadmap Clusters**
   - Create one plan file per initiative with filename:
     - `YYYY-MM-DD-HH-mm-ss_slug.md`
   - Include required front matter:
     - `plan_id`
     - `title`
     - `summary`
     - `status`
     - `created_at`
   - Add the required key line:
     - Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task
   - Convert roadmap bullets into a decomposed checklist:
     - top levels = objectives/epics
     - middle levels = phases/workstreams
     - leaf levels = atomic tasks
   - Preserve intent from original roadmap text; avoid rewording that changes scope.

5. **Migrate README Content Safely**
   - Replace roadmap sections in `README.md` with:
     - a concise migration note,
     - links to `plans/future/index.md`, `plans/current/index.md`, `plans/past/index.md`,
     - the statement that plan files are the execution source of truth.
   - Remove duplicated milestone bullets from README after verifying they exist in plan files.
   - Keep README high-level; keep execution detail in plans.

6. **Generate or Refresh Per-Folder Indexes**
   - For each status folder, include one-line entries in `index.md`:
      - `last_modified | path | title | summary`
   - Order entries:
     - `future/current`: filesystem last-write time descending.
     - `past`: `created_at` descending.
   - Run `python scripts/regenerate_plan_indexes.py` after plan create/update/move/archive.
   - Host/submodule mode (`./agents` with host-owned plans): run `python agents/scripts/regenerate_plan_indexes.py --repo-root .` from host root.
   - If script execution is unavailable, update indexes manually and record follow-up to restore script-based regeneration.

7. **Run Migration Verification**
   - Confirm every mapped source roadmap item appears in at least one plan checklist item.
   - Confirm each plan file has required front matter keys and checkbox key line.
   - Confirm no plan YAML contains modification-time fields.
   - Confirm each index contains all plans in its folder and no cross-status mismatch.
   - Confirm README roadmap section now points to plans instead of duplicating execution tasks.

8. **Checkpoint Summary and Commit Readiness**
   - Summarize:
     - roadmap sources migrated,
     - plan files created/updated,
     - index files updated,
     - README sections changed.
   - Identify which migrated plan(s) become active execution plans in `plans/current/`.
   - Prompt to update today's journal entry with migration checkpoint details.
   - Follow the applicable commit playbook for approval, commit, and push.

9. **Select Active Plan for Execution**
   - Before implementation checkpoints begin, confirm the active governing plan path in `plans/current/`.
   - Ensure upcoming repository work maps to atomic checklist items in that active plan.
   - If no checklist item covers required work, propose a plan revision and request approval before execution.

## Verification

- `rg -n "(?i)roadmap|milestone"` no longer returns actionable milestone lists in README after migration.
- Every migrated initiative exists as a plan file in exactly one status directory.
- Every plan file includes required front matter and checkbox key.
- Index entries match actual plan files and follow status-aware ordering (`future/current` by last-write time, `past` by `created_at`).
- README contains links to all three plans indexes and states plans are the source of truth.

## Lifecycle Compliance

Prompt -> Select/Create Plan (using relevant playbook guidance) -> Request approval -> Execute approved plan atoms -> Plan update -> Docs update -> Verification.

If this occurs inside a git repo:
- Review `git status` and relevant diffs.
- Suggest a commit message that summarizes the migration checkpoint.
- Commit after approved checkpoint completion.
