# Playbook: How to Create a New Agent Playbook

*Status: Stable*

This playbook outlines the standard procedure for an AI Agent to create a new operational playbook for this project. Playbooks are essential for standardizing complex tasks, troubleshooting, and development workflows.

## 1. Prerequisites & Context Gathering

**CRITICAL STEP**: Before attempting to write a new playbook, you must establish a complete mental model of the system. Do not skip this.

1.  **Read the Root Documentation**:
    *   `README.md`: Understand the project's high-level architecture and goals.
    *   `AGENTS.md`: Understand the organizational structure, API standards, and the role of agents.
2.  **Read Component Documentation (If Present)**:
    *   Relevant module or subsystem READMEs (e.g., `/docs`, `/services`, `/modules`, `/platform`).
    *   Any architecture or integration notes that affect the task.
3.  **Verify Current State**:
    *   Check `playbooks/` to ensure a similar playbook does not already exist.

## 2. When to Create a Playbook

Create a new playbook when:
*   **Complexity**: A task involves more than 3 distinct steps or spans multiple domains (e.g., backend + frontend + documentation).
*   **Repetition**: The user asks for the same multi-step operation frequently.
*   **Troubleshooting**: You successfully solve a difficult error (e.g., "Build failed due to missing library") and want to document the fix for future agents.
*   **Workflow**: A new feature is added that requires a specific deployment or testing sequence.

## 3. Drafting the Playbook

### Filename Convention
*   Use **verbose, descriptive filenames** using snake_case.
*   The filename should be a sentence fragment that answers "What is this for?".
*   *Bad*: `deploy.md`, `fix_error.md`
*   *Good*: `how_to_run_release_builds.md`, `troubleshooting_ci_failures.md`

### File Structure
Start with the following template:

```markdown
# Playbook: [Title of the Task]

*Status: [Draft | Stable | Deprecated]*

## Objective
A 1-sentence summary of what this playbook achieves.

## Prerequisites
*   Tools required (e.g., language toolchains, package managers, SDKs).
*   Access required (e.g., network access, credentials, hardware).

## Step-by-Step Instructions
1.  **Step Name**: 
    *   Command to run.
    *   Expected output.
    *   What to do if it fails.

## Verification
How to confirm the task was successful.

## Lifecycle Compliance
Confirm the workflow follows the required cycle:
Prompt -> Plan (based on a known playbook) -> Request approval -> Execute -> Plan/playbook update -> Docs update -> Verification.

If this occurs inside a git repo:
* Review `git status` and relevant diffs.
* Suggest a commit message that summarizes the completed task.
* Commit after completion.
```

## 4. Writing Guidelines

*   **Be Specific**: Do not say "Run the script." Say "Run `<script>` from the project root."
*   **Anticipate Failure**: If a step is prone to error (like network timeouts), provide a specific remediation sub-step.
*   **Code-First**: Where possible, reference specific scripts in the repo rather than writing long manual terminal commands.
*   **Idempotency**: Playbooks should ideally be repeatable without breaking the system.
*   **Lifecycle Alignment**: Include the lifecycle compliance block so agents always follow plan/approval/update/verify and commit after completion.

## 5. Finalizing

1.  Save the file to `playbooks/`.
2.  If this is a major workflow, mention it in `AGENTS.md` under the "Agent Playbooks" section.
3.  If in a git repo, check status/diff and suggest a commit message. Commit after completion.
