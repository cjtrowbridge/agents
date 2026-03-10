# Reference: Interaction Checkpoints and Automation Boundaries

## Purpose

Define reusable rules for when an agent should:
- continue autonomously,
- ask the user a question,
- request approval,
- or stop due to ambiguity.

This reference is framework-level and should be applied by playbooks and prompts in a consistent way.

## Core Principle

Automate what is safe and knowable. Ask when approval, missing information, or ambiguity would materially affect correctness.

## Boundary Types

### 1. Execution Approval Boundary

Use when a change is about to be applied.

Examples:
- Editing files after analysis/planning
- Running a risky command
- Committing or pushing (unless already approved for that action, or a journal-only auto-commit policy exception applies)

Required behavior:
- Present the plan or the atomic action
- State impacted files/areas
- Ask for explicit approval if policy or the active plan requires it

### 2. Information Gap Boundary

Use when the next step depends on information not available in the repo or prompt.

Examples:
- Missing target environment detail
- Choice between incompatible implementation paths
- Undefined user preference that affects output quality

Required behavior:
- Ask only the smallest question that unblocks progress
- Offer concrete options when possible

### 3. Ambiguity Stop Boundary

Use when the active plan is missing, insufficient, or ambiguous for the requested task and execution would require guessing.

Required behavior:
- Stop
- State what is missing from the active plan
- Propose a concrete plan revision (or plan creation) and request approval before continuing

### 4. Safety / Permission Boundary

Use when a command requires elevated permissions or introduces risk.

Required behavior:
- Explain the purpose of the command
- Request approval through the proper mechanism
- Avoid broad escalation when a narrower one works

## Default Decision Rule

Before asking the user, check:
1. Can this be discovered locally?
2. Is it already specified by policy or the active plan?
3. Is it reversible and low risk?
4. Would guessing likely reduce correctness?

If (1) or (2) is yes, do not ask.
If (4) is yes and the answer materially changes execution, ask.

## Approval Language Pattern

Good:
- "Proposed changes: X, Y, Z. Files: A, B, C. Approve this patch?"
- "I need one choice to continue: option A or B for [reason]."

Bad:
- "What do you want me to do?"
- "Should I continue?" (without scope)

## Progress Update Pattern

Use short updates while working:
- What you are doing now
- Why it matters to the task
- What you learned (if relevant)

Avoid:
- Long internal monologue
- Repeating the same status with no new information

## Anti-Patterns

- Asking for approval after the change is already made
- Asking broad open-ended questions when a narrow choice would do
- Treating every minor step as a checkpoint
- Continuing through ambiguity because "it probably means X"
- Asking users to perform automatable low-risk steps
