---
plan_id: YYYY-MM-DD-HH-mm-ss_slug
title: Plan Title
summary: One-sentence summary of what this plan accomplishes.
status: future
created_at: YYYY-MM-DD-HH-mm-ss
---

# Plan Title

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [ ] 1. Abstract objective.
  - [ ] 1.1 Major workstream.
    - [ ] 1.1.1 Specific sub-workstream.
      - [ ] 1.1.1.1 Atomic executable task.

- [ ] 2. Verification objective.
  - [ ] 2.1 Validation workstream.
    - [ ] 2.1.1 Atomic validation task.

## Authoring Rules

- Use filename format: `YYYY-MM-DD-HH-mm-ss_slug.md`.
- Use lowercase, hyphenated slugs (letters, numbers, hyphens only).
- Include required front matter keys only: `plan_id`, `title`, `summary`, `status`, `created_at`.
- Do not add modification-time fields to YAML front matter.
- Decompose from abstract goals to atomic tasks that can be executed without further decomposition.
- Use `[-]` for intentionally de-scoped/closed items that are not completed implementation.
- Keep plan location aligned to status:
  - `plans/future/`: queued work
  - `plans/current/`: actively executed work
  - `plans/past/`: archived work with no planned follow-up
