# Playbook: Bootstrap Framework Submodule Into a Host Repository

*Status: Draft*

## Objective

Provide a repeatable workflow for first-time integration of this framework as `./agents` inside a host repository, including host-root bootstrap files/directories and host-managed framework copy/synthesis rules.

## Prerequisites

- Host repository access with write permissions.
- Git submodule commands available.
- User approval for any host file writes.

## Step-by-Step Instructions

1. **Confirm Host Integration Scope**
   - Confirm target host repo root and intended submodule path (`./agents`).
   - Confirm whether host already has framework-managed artifacts (`./playbooks`, `./references`, `./templates`, `./scripts`, root shim files).

2. **Add or Update Submodule**
   - Add submodule at `./agents` if missing.
   - Initialize/update submodule contents.

3. **Create Required Host Operational Directories**
   - Ensure these host directories exist:
     - `./plans/future/`, `./plans/current/`, `./plans/past/`
     - `./journal/`
     - `./kanban/`
     - `./downtime/reports/pending/`, `./downtime/reports/reviewed/`

4. **Bootstrap Host Shim Files**
   - Ensure host shim files exist (`./AGENTS.md`, and runtime-specific variants as needed).
   - Ensure host shims direct agents to `./agents/RULES.md`.
   - Ensure host shims state resolution order:
     - use host-managed `./playbooks`, `./references`, `./templates`, `./scripts` when present,
     - fall back to `./agents/...` when missing.

5. **Apply Host-Managed Framework Copy Rules**
   - If host copies are missing, copy from submodule:
     - `./agents/playbooks -> ./playbooks`
     - `./agents/references -> ./references`
     - `./agents/templates -> ./templates`
     - `./agents/scripts -> ./scripts`
   - If host copies already exist:
     - produce synthesis recommendations that preserve host intent and integrate new upstream features,
     - ask user approval before applying final merged outputs.

6. **Validate Host Commands and Paths**
   - Verify host plan-index command path:
     - `python agents/scripts/regenerate_plan_indexes.py --repo-root .`
   - Verify no unresolved `./agents/...` vs `./...` path ambiguity remains in host bootstrap artifacts.

7. **Checkpoint Summary**
   - Report:
     - created directories,
     - copied files/directories,
     - synthesized files requiring user decisions,
     - unresolved questions or follow-up migration tasks.
   - Include governing active plan path and checklist item deltas.

## Verification

- Host root has required operational directories.
- Host shim files reference `./agents/RULES.md`.
- Host-managed framework directories exist or have approved synthesis plans.
- `python agents/scripts/regenerate_plan_indexes.py --check --repo-root .` succeeds in host root context.

## Lifecycle Compliance

Prompt -> Select/Create Plan (using relevant playbook guidance) -> Request approval -> Execute approved plan atoms -> Plan update -> Docs update -> Verification.

If this occurs inside a git repo:
- Review `git status` and relevant diffs.
- Suggest a commit message that summarizes the completed checkpoint.
- Commit after approved checkpoint completion.
