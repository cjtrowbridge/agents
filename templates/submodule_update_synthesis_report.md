# Submodule Update Synthesis Report

## Scope

- Host repository:
- Submodule path: `./agents`
- Prior submodule commit:
- New submodule commit:
- Report date:

## Managed Artifact Set

- `./AGENTS.md` and other root shims
- `./playbooks/`
- `./references/`
- `./templates/`
- `./scripts/`

## Three-Way Synthesis Inputs

1. File: `[path]`
   - Old upstream source (`./agents/...` @ old commit):
   - New upstream source (`./agents/...` @ new commit):
   - Current host-managed file (`./...`):

## Proposed Merge Decisions

1. File: `[path]`
   - Host behavior to preserve:
   - Upstream changes to integrate:
   - Proposed merged output summary:
   - Risks/tradeoffs:
   - User approval status: `[pending | approved | rejected]`

## Migration / Integration Actions

1. `[Action]`
   - Trigger type: `[path change | policy/schema change | script behavior change]`
   - Files affected:
   - Verification step:

## Verification Results

- `python agents/scripts/regenerate_plan_indexes.py --check --repo-root .`:
- Path consistency grep checks:
- Additional checks:

## Rollback Plan

- Submodule rollback command:
- Host file rollback source:
- Re-validation command(s):

## Final Summary

- Files synthesized:
- Files deferred:
- Remaining open decisions/questions:
