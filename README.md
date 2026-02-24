# agents

A set of constraints, playbooks, references, and templates for a self-evolving agentic system that can be dropped into many projects and used across different LLM runtimes.

## Purpose

This repository is the framework itself, not a target application.

Its job is to help agents:
- make plans before acting,
- keep documentation aligned with changes,
- execute work atomically,
- evolve the process based on real usage,
- and produce consistent results across many environments.

## Design Principles

- Simple core rules with strong operational discipline
- Atomic changes and clear approval gates
- Documentation and plans treated as executable policy
- Reusable guidance extracted into references and templates
- Incremental evolution instead of architecture churn

## Canonical Rules

- `RULES.md` - Canonical source of truth for policy, indexes, and operational rules
- `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `CODEX.md`, `OPENCODE.md` - Thin bootstrap shims that direct runtimes to `RULES.md`

## Project Structure

- `playbooks/` - Step-by-step workflows for recurring tasks
- `references/` - Reusable guidance patterns (tone, verification, automation boundaries)
- `templates/` - Reusable output formats for plans, reports, and proposals
- `downtime/` - Periodic maintenance task definitions for improving the framework during idle time
- `downtime/reports/pending/` - Downtime task reports awaiting user review (suggested changes only)
- `downtime/reports/reviewed/` - Reviewed downtime reports kept for history and follow-up tracking
- `docs/assimilations/` - Assimilation trail for lessons adopted/rejected from other frameworks
- `get-shit-done/` - Local comparison repo used for assimilation research in this workspace (not part of the framework core)

## Working Cycle

Prompt -> Plan (based on a playbook in `./playbooks/`) -> Request approval -> Execute -> Update docs/policy -> Verify

## Build / Runtime Notes

This repo is documentation-first and currently has no build step. If executable tools/scripts are added later, document usage and verification here.

## Known Opportunities

- Expand reusable `./references/` and `./templates/` based on real agent failures and repeated ambiguities
- Add more default playbooks only for common or high-risk workflows
- Improve long-session handoff/context guidance when the framework gains more tooling

