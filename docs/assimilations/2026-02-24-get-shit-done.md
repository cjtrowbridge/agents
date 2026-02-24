# Assimilation Trail Entry: get-shit-done

## External Framework Reviewed

- Name: get-shit-done (GSD)
- Repo/Source: `https://github.com/gsd-build/get-shit-done/` (local clone in workspace for comparison)
- Review Date: 2026-02-24

## What We Studied

- Architecture layering (agents, commands, workflows, references, templates, hooks, tooling, tests)
- Prompt/policy design and role-specific behavior shaping
- Reusable references/templates for consistency
- Verification/debugging patterns and evidence-first checks
- Tooling centralization and failure-handling posture

## Lessons Adopted

1. Reusable `./references/` layer for shared guidance patterns
   - Why adopted: reduces duplicated wording across playbooks and improves consistency
   - Where integrated: `./references/` docs + `RULES.md` references index

2. Reusable `./templates/` layer for common outputs
   - Why adopted: standardizes plans/reports/proposals across agents and tasks
   - Where integrated: `./templates/` docs + `RULES.md` templates index

3. Assimilation trail artifact
   - Why adopted: preserves adopted/rejected lessons and avoids repeated re-analysis
   - Where integrated: `./docs/assimilations/README.md`, `./templates/assimilation_trail_entry.md`, this entry

4. Default playbooks for recurring high-risk workflows
   - Why adopted: improves reliability for review and tool-wrapper changes without requiring a large framework expansion
   - Where integrated:
     - `./playbooks/how_to_review_changes_for_risk_and_regression.md`
     - `./playbooks/how_to_add_or_modify_a_tool_wrapper_safely.md`

5. Downtime maintenance workflow and task catalog
   - Why adopted: creates a portable, script-free way to run periodic framework improvements
   - Where integrated:
     - `./playbooks/how_to_use_downtime_to_improve_the_framework.md`
     - `./downtime/*.md`

## Lessons Rejected / Deferred

1. Script-based playbook index verification utility
   - Decision: rejected (for this repo)
   - Why: this framework is intended to be forked into many projects/systems; a script adds portability and environment assumptions. Replaced with a manual `.downtime` task.

2. Full GSD `.planning/` execution framework (phases, milestones, orchestration)
   - Decision: rejected (for now)
   - Why: too product-specific and heavyweight for this repo's universal policy/playbook role

3. Context-monitor/statusline hook instrumentation
   - Decision: deferred
   - Why: useful pattern, but premature until this repo adds more executable tooling

## Follow-Up Tasks

- Use the new downtime playbook to periodically tighten references/templates from real outputs
- Decide whether to add more default playbooks via the downtime coverage review task
- Consider adding test coverage only if executable tooling is introduced later

## Notes

Key transferable idea from GSD was not "copy the system," but "separate reusable guidance and templates from workflow playbooks so many agents can apply the same policy with less drift."

