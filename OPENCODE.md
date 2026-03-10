# OPENCODE Instructions

Read `RULES.md` in its entirety before doing anything in this repository. Follow all instructions in `RULES.md` as though they are written directly in this file. Do not proceed if you have not read and understood `RULES.md`.

If this repository is mounted as a submodule at `./agents` inside another project, from the host project root:
- Read `./agents/RULES.md` as canonical policy.
- Use host-managed `./playbooks/`, `./references/`, `./templates/`, and `./scripts/` when present.
- Fall back to `./agents/playbooks/`, `./agents/references/`, `./agents/templates/`, and `./agents/scripts/` when host copies are missing.
- For host-owned plans, run `python agents/scripts/regenerate_plan_indexes.py --repo-root .`.
