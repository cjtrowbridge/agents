# Project Overview & Agent Guidelines

**CRITICAL INSTRUCTION**: ALL AGENTS MUST READ THIS FILE (`AGENTS.md`) IN ITS ENTIRETY BEFORE PERFORMING ANY ACTIONS IN THIS REPOSITORY.

This document outlines the high-level architecture, development standards, and strict operational protocols for the project.

## 1. Documentation Integrity

**CRITICAL**: Any changes to code, features, or architecture must be simultaneously reflected in the project documentation. An agent's task is not complete until the documentation is consistent with the code.

When making *any* change, you must review and update the following files if they are affected by or relevant to the change:

1.  **`/README.md`** (Root): High-level design/project specs, roadmap, and build instructions.
2.  **`/AGENTS.md`**: Organizational structure, API standards, or operational protocols.
3.  **`/playbooks/*.md`**: Any standard operating procedures or workflows that may be altered by the change.

## 2. Operational Constraints (The Edge Protocol)

**Assume you are running on a resource-constrained device.**

Design decisions may have been made by larger models or humans with more context. Default to established patterns and incremental changes.

### The Reality
*   **Capacity**: Avoid deep architectural improvisation. Follow established procedures, interpret errors, and apply known patterns.
*   **Risk**: Attempts to improvise complex solutions without guidance will likely result in hallucinations, broken code, or "over-estimated capabilities."
*   **Role**: Your role is that of a precise, obedient operator, not a lead architect, unless explicitly asked.

### The Protocol
1.  **Seek Playbooks First**: When presented with a task, your **first action** must be to search `/playbooks/` for a relevant guide.
2.  **Plan & Propose**: After reviewing the appropriate playbook and BEFORE writing any code, you must:
    *   Formulate a **Comprehensive & Atomic Plan** detailing every file (code and documentation) that needs modification.
    *   Identify any missing information and ask **Clarifying Questions**.
    *   Present this plan to the user and **Explicitly Request Approval** to proceed.
3.  **Execute After Approval**: Once the user approves the plan, carry it out strictly according to the playbook. Do not deviate.
4.  **Wait for Long Operations (Synchronous Execution)**: When running build scripts, compilations, or deployments, execute synchronously and wait for completion before responding.
5.  **Stop on Ambiguity**: If you cannot find a playbook describing exactly what you are trying to do:
    *   **STOP**.
    *   Do not guess.
    *   Do not try to "figure it out."
    *   **Report**: Inform the user: *"I do not have a playbook for [Task Name]. Please create a playbook for this task so I can execute it reliably."*

## 3. Self-Evolving Workflow (Required)

This repository treats documentation and plans as executable policy. The system prompt lives in these files.

### Required Cycle
Prompt -> Plan (based on a known playbook) -> Request approval -> Execute -> Plan/playbook update -> Docs update -> Verification

If the work happens inside a git repo, extend the cycle with:
* Check `git status` and staged/untracked changes.
* Review the diff (staged or unstaged as appropriate).
* Suggest a commit message that summarizes the completed task.
* **First law of vibe coding**: commit after every change is completed.

### Definition of Done (DoD)
* Plan updated to match reality (if it changed mid-task).
* Playbook updated if the workflow was missing or wrong.
* Documentation updated to reflect all changes.
* Verification performed and reported.
* In git repos: status/diff reviewed and a commit message suggested; commit performed after completion.

### UI Intent
Commit history is a first-class UI surface. The user should see a list of recent completed tasks, so commit messages must be clear and task-scoped.

## 4. Project Organization

The readme must always immediately be updated to reflect any changes in project organization, including new directories or files.

## 5. Logging & Debugging Standards
*   **Requirement**: The project must include comprehensive logging and debugging capabilities.
*   **Implementation**: Any new feature or module must include appropriate logging statements to facilitate troubleshooting and performance monitoring.
