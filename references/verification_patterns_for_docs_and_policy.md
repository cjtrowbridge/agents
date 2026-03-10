# Reference: Verification Patterns for Docs and Policy

## Purpose

Provide reusable verification patterns for documentation, playbooks, and policy artifacts so agents confirm outputs are usable, consistent, and actionable, not merely present.

## Core Principle

**Existence != Usability**

A file can exist and still fail the framework if it is:
- incomplete,
- ambiguous,
- inconsistent with related docs,
- missing verification steps,
- or impossible to execute reliably.

## Verification Levels for Docs/Policy

1. **Exists**
   - File/path exists where referenced.

2. **Structured**
   - Contains expected sections/template fields.
   - Uses consistent naming and scope.

3. **Connected**
   - References to other files/paths are valid.
   - Indexes (`RULES.md`/`README.md`) reflect added/removed artifacts.

4. **Actionable**
   - Steps can be followed in order.
   - Preconditions and outputs are clear.
   - Approval/verification gates are explicit where required.
   - Execution boundaries are tied to approved active plan checklist items.

5. **Aligned**
   - Matches current repo policy and does not contradict `RULES.md`.
   - Matches actual repo organization and current workflows.

## Practical Checks by Artifact Type

### Playbooks

Verify:
- Objective is specific
- Prerequisites are realistic
- Steps are ordered and executable
- Plan-binding rules are explicit (active plan path + checklist mapping)
- Approval gate appears before implementation (when required)
- Verification section exists
- Lifecycle compliance is addressed (unless intentionally omitted and explained)

Failure patterns:
- "Update docs" with no files listed
- "Run tests" with no scope or fallback
- Implicit approval assumptions
- Contradicting another playbook or `RULES.md`

### References

Verify:
- Guidance is reusable across multiple playbooks/prompts
- Not overly specific to one incident
- Includes examples and anti-patterns
- Does not duplicate large sections of an existing playbook

Failure patterns:
- Hidden workflow steps disguised as "reference"
- Advice without operational implications
- Tone guidance that conflicts with framework behavior

### Templates

Verify:
- Output shape is obvious
- Required vs optional fields are distinguishable
- Template aligns with the playbook that calls it
- Field names match the terms used in the workflow
- Execution templates capture active plan path and checklist deltas when applicable

Failure patterns:
- Ambiguous placeholders
- Missing approval request section in planning templates
- Missing active plan path/checklist delta fields in execution checkpoint templates
- Sections that no playbook actually uses

### Indexes / Organization Docs (`RULES.md`, `README.md`)

Verify:
- Newly added files/directories are documented if relevant
- Index entries match actual filenames
- Descriptions still match purpose after edits/renames

Failure patterns:
- Index drift
- Renamed file still listed under old path
- README structure docs stale after adding new top-level directories

## Evidence-First Reporting Pattern

When reporting verification results, separate:
- `Observed`: direct evidence from files
- `Mismatch`: inconsistency or missing requirement
- `Impact`: why it matters
- `Fix`: smallest change to restore alignment

## Minimal Verification Log Format

Use this format for quick audits:

```md
- Checked: `path/to/file.md`
- Result: pass | fail | partial
- Evidence: [specific section/path/reference]
- Next action: [none or specific fix]
```

## Anti-Patterns

- Marking docs "done" because the file exists
- Reviewing wording but not checking linked paths
- Updating a playbook without updating the relevant index
- Fixing one file while leaving contradictory policy in another
