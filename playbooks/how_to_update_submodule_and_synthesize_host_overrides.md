# Playbook: Update Submodule and Synthesize Host Overrides

*Status: Draft*

## Objective

Provide a safe, repeatable workflow for updating the `./agents` submodule in a host repository and synthesizing host-managed framework files (`./playbooks`, `./references`, `./templates`, `./scripts`, shims) with user-approved merge decisions.

## Prerequisites

- Host repository includes this framework as `./agents`.
- Host repository contains managed framework copies and/or customizations.
- User approval available for merge resolutions.

## Step-by-Step Instructions

1. **Capture Update Baseline**
   - Record current submodule commit.
   - Inventory host-managed framework files changed since prior sync.
   - Identify high-risk artifacts (policy files, plan tooling, templates used in active workflows).

2. **Update Submodule**
   - Update submodule pointer to target upstream revision.
   - Record new submodule commit.

3. **Compute Three-Way Inputs**
   - For each managed file:
     - old upstream version from previous submodule commit,
     - new upstream version from updated submodule commit,
     - current host-managed version.

4. **Draft Synthesis Recommendations**
   - Propose merged outputs that:
     - preserve host-specific behavior,
     - integrate new upstream safety/policy/tooling improvements.
   - Use `./templates/submodule_update_synthesis_report.md` to organize proposals.

5. **Ask User Before Final Merge Decisions**
   - Present recommendations and impacted files.
   - Ask explicit approval for final resolution choices.
   - Do not silently apply unresolved merge decisions.

6. **Apply Approved Synthesis Outputs**
   - Write only approved merged content.
   - Keep file-level changes atomic and traceable.

7. **Run Migration/Integration Checks**
   - Check for path changes requiring host updates.
   - Check policy/schema changes requiring host migration.
   - Check script behavior/flags that affect host commands.
   - Run:
     - `python agents/scripts/regenerate_plan_indexes.py --check --repo-root .`

8. **Finalize and Report**
   - Summarize:
     - submodule commit delta,
     - files synthesized,
     - user-approved merge decisions,
     - migration actions and residual risks.
   - Include active plan path and checklist item deltas.

## Verification

- Host-managed framework files reflect approved synthesis outputs.
- No unresolved merge decisions remain.
- Host verification commands pass for current operational paths.
- README/docs impacted by update semantics are synchronized.

## Lifecycle Compliance

Prompt -> Select/Create Plan (using relevant playbook guidance) -> Request approval -> Execute approved plan atoms -> Plan update -> Docs update -> Verification.

If this occurs inside a git repo:
- Review `git status` and relevant diffs.
- Suggest a commit message that summarizes the completed checkpoint.
- Commit after approved checkpoint completion.
