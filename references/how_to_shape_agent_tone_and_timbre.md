# Reference: How to Shape Agent Tone and Timbre

## Purpose

Provide reusable guidance for writing prompts, policies, and playbooks that consistently shape agent behavior across runtimes without overfitting to one model.

## Core Principle

Tone is not cosmetic. Tone and timbre change how agents prioritize, ask questions, explain tradeoffs, and handle ambiguity.

Well-shaped tone improves:
- consistency across agents,
- decision quality under pressure,
- user trust,
- and output scanability.

## Target Qualities for This Framework

- Direct and factual
- Pragmatic and execution-oriented
- Explicit about assumptions and tradeoffs
- Respectful without cheerleading
- Clear about what is known vs inferred vs unknown
- Focused on atomic next steps

## Writing Pattern

When writing agent instructions, specify:
1. The behavioral posture (for example: "pragmatic senior engineer")
2. What to optimize for (clarity, safety, momentum, correctness)
3. What to avoid (fluff, hedging, premature implementation, overreach)
4. How to communicate progress (short updates, concrete findings)
5. How to handle uncertainty (state evidence gaps, ask targeted questions)

## Tone Controls That Matter Most

### 1. Priority Framing

Tell the agent what matters most when tradeoffs appear.

Examples:
- "Prefer reliable incremental changes over broad redesigns."
- "Findings first, summary second."
- "State risks before implementation details."

### 2. Verb Choice

Use operational verbs to reduce ambiguity:
- "verify", "compare", "patch", "measure", "cite", "ask", "defer"

Avoid vague verbs when precision matters:
- "handle", "do", "improve", "fix things"

### 3. Explicit Anti-Patterns

List what not to do, especially behaviors that look helpful but reduce reliability.

Examples:
- Do not copy patterns wholesale from another project.
- Do not treat verbosity as rigor.
- Do not ask users to perform automatable work.
- Do not present conclusions without evidence references.

### 4. Output Shape

Tone is reinforced by structure. If you need consistent behavior, define the expected output sections.

Use templates when the same output repeats (plans, reports, proposals).

## Timbre Calibration Examples

### Weak (too vague / performative)

"Be helpful, thoughtful, and do your best to solve the problem."

### Better (operational)

"Act as a pragmatic engineer. Be direct, factual, and explicit about tradeoffs. Prioritize correct, minimal changes and evidence-backed recommendations."

### Stronger (task-specific)

"Review in bug/risk-first mode. Findings must come first, ordered by severity, with file references. Keep summaries brief. State testing gaps explicitly."

## Prompt Layering Pattern

Use layered guidance instead of one giant block:
- Global posture in `RULES.md`
- Task workflow in playbooks
- Reusable tone/timbre details in `./references/`
- Output shape in `./templates/`

This reduces duplication and keeps policy edits atomic.

## Review Checklist (Tone/Timbre)

- Does the wording produce clear priorities?
- Does it discourage common failure modes?
- Does it avoid contradictions with global policy?
- Does it produce concise but sufficient outputs?
- Does it preserve user agency at approval/checkpoint boundaries?

## Anti-Patterns

- Over-prescribing personality traits that do not affect outcomes
- Mixing contradictory instructions ("be concise" + "always be exhaustive")
- Using aspirational language instead of operational rules
- Embedding repeated tone rules in many playbooks instead of one reference

