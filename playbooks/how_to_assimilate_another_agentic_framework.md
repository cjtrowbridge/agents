# Playbook: How to Assimilate Another Agentic Framework

*Status: Draft*

## Objective
Provide a repeatable, evidence-first workflow for studying similar or adjacent agentic projects, extracting transferable lessons across multiple layers (architecture, tools, prompts, workflows, documentation, and operational discipline), and proposing a safe, atomic integration plan for this project.

## Prerequisites
* Access to this repo and the comparison repo(s) (local paths, git URLs, or exported files).
* Ability to read documentation, prompts/instructions, playbooks, and implementation code from the comparison repo(s).
* A user-provided comparison repo (or a plan to provide one next).
* Time to perform deep reflection before proposing changes (do not jump straight to implementation).

## When to Use This Playbook
Use this playbook when:
* The user provides one or more other agentic frameworks/repos and wants lessons extracted.
* You need to improve this framework's reliability, accuracy, ergonomics, or extensibility using proven patterns from elsewhere.
* You need to decide whether to remain minimal or adopt more default playbooks/workflows.
* You want to compare not just code, but also prompt engineering style, tool design, and documentation policy.

## Step-by-Step Instructions

1.  **Take a First Look at This Repo (Required, Before Asking for a Goal)**
    * Read `RULES.md`, `README.md`, and the current `./playbooks/*.md`.
    * Summarize the framework's apparent design philosophy by comparing and contrasting each of the key features to those of our framework.
    * Identify the current baseline posture:
        * Minimal-by-default vs batteries-included.
        * Strictness vs flexibility.
        * Documentation burden vs execution speed.
        * Atomicity vs expressiveness.
    * Do not begin by asking the user for an assimilation goal; present the user with a list of assimilation opportunities.

2.  **Create an Apparent Opportunity Map (Required)**
    * Based on the first look, define a set of apparent opportunities to explore and compare against other frameworks.
    * These are hypotheses, not conclusions.
    * Include opportunities across multiple layers, including:
        * Architecture and project organization.
        * Tool wrappers, tool usage, and execution/approval flow.
        * Playbook coverage (including whether more default playbooks would help or hurt).
        * Prompt engineering structure, tone, and timbre.
        * Documentation maintenance and self-evolving workflow policy.
        * Verification, debugging, and evidence collection discipline.
    * For each opportunity, state:
        * Why it appears to be a possible leverage point.
        * What outcome might improve if a better pattern exists elsewhere.

3.  **Define the Comparison Scope From the Opportunity Map**
    * Select which opportunities will be tested in this assimilation round.
    * Ask the user to confirm or reprioritize the opportunity list if needed.
    * Record explicit non-goals so the review does not sprawl.
    * Example non-goals:
        * Full architecture rewrite.
        * Blindly copying another project's prompt stack.
        * Adopting tooling patterns that conflict with this repo's safety model.

4.  **Collect Evidence From the Comparison Repo(s)**
    * Do not skim only the README.
    * Inspect the structure and the operating rules of the framework.
    * Gather evidence from the layers below:
        * Architecture and file organization.
        * Agent/system prompts, instruction style, and tone/timbre.
        * Tool wrappers and execution model.
        * Planning/approval workflow.
        * Documentation/playbook conventions.
        * Verification and debugging workflows.
        * Logging/observability guidance.
        * Git hygiene and commit practices (if present).
    * For each observed pattern, capture the source file/path and a short note on what problem it appears to solve.

5.  **Build a Multi-Layer Comparison Matrix**
    * Compare this repo and the other repo(s) across the same categories.
    * Required categories:
        * Architectural structure.
        * Agent constraints and policy design.
        * Planning and approval mechanics.
        * Tool interface design and failure handling.
        * Documentation maintenance model.
        * Playbook coverage (minimal vs default set).
        * Prompt tone/timbre and behavioral shaping.
        * Verification/debugging workflow quality.
    * For each category, explicitly state:
        * What they do better.
        * What we do better.
        * Unknowns / evidence gaps.

6.  **Deep Reflection (Required, No Fixes Yet)**
    * Reflect deeply before proposing any changes.
    * For each strong idea from another framework, answer:
        * What exact problem does it solve there?
        * What assumptions make it work there?
        * Do those assumptions hold here?
        * What is the smallest version of this idea that would help us?
        * What complexity cost would it add?
        * What failure mode could it introduce?
    * Reject cargo-cult adoption.
    * The goal is not to mimic another framework.
    * The goal is to graft lessons that improve this framework's outcomes while preserving its core philosophy (simple, straightforward, atomic, reliable across many agents).

7.  **Extract Candidate Lessons (Transferable vs Non-Transferable)**
    * Create two lists:
        * Transferable lessons (should adopt or pilot).
        * Non-transferable lessons (good ideas elsewhere, but not a fit here).
    * Required lesson types to consider:
        * Architecture-level patterns.
        * Tooling/execution patterns.
        * Playbook/workflow patterns.
        * Prompt engineering patterns (including tone/timbre and instruction layering).
        * Documentation and self-evolution patterns.
        * Small quality-of-life details that improve outcomes (naming, templates, examples, checklists, guardrails).

8.  **Run a Graftability Test for Each Candidate**
    * Score each candidate on:
        * Expected impact (reliability/capability gain).
        * Complexity cost.
        * Operational risk.
        * Reversibility.
        * Documentation burden.
        * Fit with this repo's design principles.
    * Mark each candidate as one of:
        * Adopt now.
        * Pilot first.
        * Defer.
        * Reject.
    * Prefer small reversible grafts over large architecture rewrites unless the user explicitly requests a redesign.

9.  **Evaluate the "Minimal vs More Default Playbooks" Tradeoff Explicitly**
    * Always evaluate both options:
        * Option A: Stay minimal (fewer default playbooks, stronger general rules).
        * Option B: Add more default playbooks (more explicit workflows, less ambiguity).
    * Analyze:
        * Reliability gains.
        * Maintenance cost.
        * Onboarding clarity for new agents.
        * Risk of over-constraining agents.
        * Risk of missing guidance for common tasks.
    * Recommend a threshold rule, such as:
        * Add a default playbook only when the task is common, high-risk, or multi-step enough to benefit from standardization.
        * Keep one-off or rapidly changing workflows out of the default set unless they recur.

10.  **Produce an Assimilation Report (Required Output)**
    * Deliver a structured report to the user containing:
        * First-look baseline summary of this repo.
        * Apparent Opportunity Map (the hypotheses chosen for comparison).
        * Repos reviewed and evidence sources.
        * Comparison matrix summary.
        * Top lessons learned (with rationale).
        * Non-transferable ideas (and why not).
        * Recommended grafts (ranked).
        * A concrete integration plan (atomic steps).
        * Risks and verification plan.
        * Documentation/playbook updates required.
    * The report must distinguish:
        * Observed facts (evidence from files).
        * Inferences (your reasoning).
        * Recommendations (proposed changes).

11.  **Propose an Atomic Integration Plan (Do Not Implement Yet)**
    * Break the recommended changes into small, reviewable tasks.
    * Include every file expected to change (`RULES.md`, `README.md`, playbooks, code/tools, templates, etc.).
    * If a new playbook is required, include it explicitly.
    * If prompt/instruction tone changes are proposed, identify where that wording lives and how behavior will be validated.
    * Ask clarifying questions for anything ambiguous.
    * Request explicit user approval before implementation.

12.  **Execute Only After Approval**
    * Implement the approved subset of changes.
    * Keep the changes atomic and aligned to the integration plan.
    * Do not silently broaden scope during implementation.
    * If new insights appear mid-change, pause and update the plan before proceeding.

13.  **Verify the Assimilation Outcome**
    * Verify at two levels:
        * Local correctness (files updated correctly, no broken references, docs consistent).
        * Workflow outcome quality (the new guidance actually improves clarity, reliability, or repeatability).
    * Where possible, test the new guidance with a small simulated task.
    * Report what improved, what remains uncertain, and what should be measured next.

14.  **Update Documentation and Playbooks (Self-Evolving Requirement)**
    * Update `README.md` if project organization, documented workflows, or user-facing usage changed.
    * Update `RULES.md` if operational policy, index requirements, or framework rules changed.
    * Update existing playbooks if the assimilation changed how common workflows should be executed.
    * Add a new playbook if the review exposed a recurring workflow that lacks one.
    * Document not only what changed, but why the change improves the framework.

15.  **Preserve an Assimilation Trail**
    * Record a short summary of:
        * Which external project(s) were studied.
        * Which lessons were adopted.
        * Which were rejected.
        * Why.
    * Store entries in `./docs/assimilations/` using `./templates/assimilation_trail_entry.md` and a date-first filename (`YYYY-MM-DD-framework-name.md`).
    * This prevents repeated re-analysis and helps future agents understand prior reasoning.

## Required Deliverable Template (Use in Responses)

1.  First-Look Baseline (This Repo)
2.  Apparent Opportunity Map
3.  Comparison Scope for This Round
4.  Repos Reviewed and Evidence Sources
5.  Comparison Findings by Category
6.  Transferable Lessons (Ranked)
7.  Non-Transferable Lessons (With Reasons)
8.  Minimal vs Default-Playbook Recommendation
9.  Proposed Grafts (Atomic)
10. Risks and Tradeoffs
11. Verification Plan
12. Docs/Playbooks to Update
13. Approval Request

## Reflection Prompts (Use Verbosely Internally, Summarize Externally)
* What does the other framework solve that we have not encoded yet?
* Which details look cosmetic but actually enforce reliability?
* Which details look advanced but add more complexity than value for our goals?
* Are we missing a default playbook that would reduce repeated ambiguity?
* Would more default playbooks improve outcomes here, or create maintenance drag?
* Are we overfitting to one comparison repo's assumptions?
* What is the smallest graft that captures most of the benefit?

## Example Lessons to Look For (Non-Exhaustive)
* A better approval/escalation tool flow that reduces accidental unsafe actions.
* A better review protocol that prioritizes bugs/regressions before summaries.
* A stronger prompt tone/timbre that produces more direct, less ambiguous agent behavior.
* A clearer separation of plan mode vs execution mode.
* Better default playbooks for recurring tasks (debugging, code review, dependency upgrades, release steps).
* Better tooling implementation patterns (wrappers, tool ergonomics, failure reporting).
* Better documentation rules that reduce drift between code and policy.
* Better verification patterns (evidence-first checks, explicit line references, diff review discipline).
* Small wording changes in prompts that dramatically improve consistency across many agents.

## Anti-Patterns (Do Not Do This)
* Do not copy another framework wholesale because it "looks sophisticated."
* Do not confuse verbosity with reliability.
* Do not adopt patterns without identifying the problem they solve.
* Do not propose a large refactor when a small graft achieves most of the benefit.
* Do not skip documenting rejected ideas; rejections are part of the learning system.
* Do not implement before presenting the assimilation report and getting approval.

## Verification
* The assimilation report is evidence-based and cites concrete files/paths from reviewed repos.
* The proposed grafts are atomic, prioritized, and aligned with this framework's core philosophy.
* The plan clearly separates facts, inferences, and recommendations.
* Required documentation/playbook updates are identified before implementation.
* User approval is obtained before any code or policy changes are applied.

## Lifecycle Compliance
Confirm the workflow follows the required cycle:
Prompt -> Plan (based on a known playbook) -> Request approval -> Execute -> Plan/playbook update -> Docs update -> Verification.

If this occurs inside a git repo:
* Review `git status` and relevant diffs.
* Suggest a commit message that summarizes the completed task.
* Commit after completion.

