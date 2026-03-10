# Playbook: How to Review Changes for Risk and Regression

*Status: Draft*

## Objective

Provide a repeatable review workflow that prioritizes bugs, behavioral regressions, missing verification, and policy/documentation drift before summaries or style feedback.

## Prerequisites

* Access to the changed files (local repo, diff, or patch).
* Ability to inspect relevant documentation (`RULES.md`, `README.md`, `./playbooks/`, `./references/`, `./templates/`) when affected.
* Enough context to understand the intended behavior of the change.

## Step-by-Step Instructions

1.  **Establish Review Scope**
    * Determine what changed (files, feature area, docs/process area).
    * Identify the intended outcome of the change.
    * If the intent is unclear, ask a targeted clarifying question before reviewing behavior.

2.  **Check for High-Risk Areas First**
    * Prioritize:
        * Behavior changes
        * Safety/permission changes
        * Tool wrapper changes
        * Workflow/playbook policy changes
        * Documentation/policy consistency requirements
    * Note any files that imply broader impact than the diff size suggests.

3.  **Review for Bugs and Regressions (Primary Focus)**
    * Look for:
        * Incorrect logic or broken edge cases
        * Contradictions with existing policy/playbooks
        * Execution performed outside approved active plan scope
        * Missing approval boundaries
        * Invalid file paths/links/references
        * Incomplete rollout (code changed, docs not updated)
    * Treat "works in one path" as insufficient if the change affects shared workflow rules.

4.  **Review Verification Quality**
    * Check whether the change has an adequate verification path.
    * For docs/playbooks/templates:
        * Confirm outputs are actionable and consistent.
        * Confirm indexes/organization docs are updated when required.
    * For code/tooling:
        * Confirm relevant tests or checks exist (or note the gap explicitly).

5.  **Classify Findings by Severity**
    * Use severity-oriented ordering:
        * High: likely breakage, policy contradiction, unsafe behavior, incorrect workflow gate, or out-of-plan execution
        * Medium: missing coverage, ambiguity, maintainability risk, incomplete docs sync
        * Low: clarity improvements, wording nits, structure polish

6.  **Produce Findings-First Review Output**
    * Present findings before overview/summary.
    * For each finding include:
        * Severity
        * File reference(s)
        * What is wrong
        * Why it matters
        * Smallest fix direction

7.  **State Assumptions and Testing Gaps**
    * If you could not run tests/verification, say so explicitly.
    * Note any assumptions that affect confidence in the review.

8.  **Add Brief Summary (Secondary)**
    * After findings, provide a short summary of what changed and residual risk.
    * If no findings, state that explicitly and list any remaining uncertainty.

## Review Output Template

1. Findings (ordered by severity)
2. Open Questions / Assumptions
3. Verification / Testing Gaps
4. Change Summary (brief)

## Anti-Patterns

* Starting with a summary and burying real risks
* Focusing on style while skipping behavioral checks
* Reporting "looks good" without checking policy/doc consistency
* Mixing speculative suggestions with concrete defects without labeling them

## Verification

* Review output lists findings first (or explicitly states no findings).
* Findings include file references and concrete impact.
* Assumptions and testing gaps are stated explicitly.

## Lifecycle Compliance

Confirm the workflow follows the required cycle:
Prompt -> Select/Create Plan (using relevant playbook guidance) -> Request approval -> Execute approved plan atoms -> Plan update -> Docs update -> Verification.

If this occurs inside a git repo:
* Review `git status` and relevant diffs.
* Suggest a commit message that summarizes the completed task.
* Commit after approved checkpoint completion.

