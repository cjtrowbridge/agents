# Playbook: How to Add or Modify a Tool Wrapper Safely

*Status: Draft*

## Objective

Provide a safety-first workflow for adding or changing a tool wrapper (command wrapper, helper integration, hook, or tool-facing adapter) while preserving approval boundaries, failure handling, and documentation integrity.

## Prerequisites

* Clear description of the tool-wrapper change (new capability, bug fix, or behavior change).
* Access to the wrapper implementation and any calling prompts/playbooks.
* Ability to verify affected workflows (manual or automated).

## Step-by-Step Instructions

1.  **Define the Wrapper Change**
    * State:
        * What capability is being added/changed
        * Who calls the wrapper (which playbooks/prompts/workflows)
        * Expected inputs/outputs
        * Any safety or permission implications
    * If the behavior is unclear, stop and ask for clarification before implementation.

2.  **Map Integration Points**
    * Identify every place the wrapper is referenced or relied on:
        * Playbooks
        * References
        * Templates
        * Agent prompts / workflow docs
        * Tests (if any)
    * Make an explicit file list before editing.

3.  **Identify Risks and Boundaries**
    * Check for:
        * Permission escalation behavior
        * Destructive commands or side effects
        * Error propagation and fallback behavior
        * Output format changes that could break downstream consumers
        * Logging/debugging visibility
    * Define the smallest safe change that preserves current callers when possible.

4.  **Plan the Change Atomically**
    * Prefer one wrapper behavior change plus its corresponding docs updates in the same patch.
    * If the change is broad, split into phases:
        * wrapper behavior
        * caller updates
        * docs/templates
        * tests/verification
    * Request approval before editing files if the workflow requires it.

5.  **Implement the Wrapper Change**
    * Keep interfaces stable unless a breaking change is explicitly approved.
    * Add concise logging/error handling where it improves diagnosis.
    * Do not silently widen permissions or side effects.

6.  **Update Dependent Documentation**
    * Update all affected:
        * Playbooks
        * References
        * Templates
        * `RULES.md` / `README.md` (if organization or workflow inventory changed)
    * If the change introduces a recurring pattern, consider extracting it into `./references/`.

7.  **Verify End-to-End Behavior**
    * Validate:
        * Expected inputs are accepted
        * Outputs remain consumable
        * Failures are understandable and non-destructive
        * Approval/safety boundaries still hold
    * If tests exist, run the smallest relevant set.
    * If tests do not exist, document manual verification steps and gaps.

8.  **Review for Regression Risk**
    * Check downstream callers for assumptions about:
        * output shape
        * timing/ordering
        * side effects
        * error strings/conditions (if parsed)
    * Note migration needs if any callers must be updated later.

## Output Requirements

When reporting completion, include:
* What changed in the wrapper
* Which files/callers were updated
* Safety/permission impact (if any)
* Verification performed
* Remaining risks or compatibility assumptions

## Anti-Patterns

* Changing output format without updating consumers
* Expanding permissions without explicit acknowledgment
* Adding hidden side effects to "helper" tools
* Updating code but not playbooks/references/templates that describe it
* Treating wrapper failures as impossible and omitting diagnostics

## Verification

* Integration points were mapped and reviewed.
* Documentation describing the wrapper behavior is aligned with the implementation.
* Safety/permission implications were explicitly evaluated and reported.

## Lifecycle Compliance

Confirm the workflow follows the required cycle:
Prompt -> Plan (based on a known playbook) -> Request approval -> Execute -> Plan/playbook update -> Docs update -> Verification.

If this occurs inside a git repo:
* Review `git status` and relevant diffs.
* Suggest a commit message that summarizes the completed task.
* Commit after completion.

