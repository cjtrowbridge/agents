# Playbook: How to Commit and Push Changes

*Status: Draft*

## Objective
Provide a repeatable workflow to summarize staged changes, propose a commit message, and push to `origin` after user approval, without assuming untracked files should be added.

## Prerequisites
*   Git installed and available in your shell.
*   Changes staged (`git add ...`).
*   Access to the remote `origin`.

## Step-by-Step Instructions

1.  **Check Repository Status**
    *   Command: `git status -sb`
    *   Expected: Shows staged files under `Changes to be committed`, and any untracked files under `??`.
    *   If nothing staged: run `git add <files>` and re-check.

2.  **Confirm Plan and Docs Are Updated**
    *   Ensure the task plan, playbooks (if relevant), and docs are updated before committing.
    *   If anything is missing, update it first, then return to Step 1.

3.  **Handle Untracked Files (Never Assume They Should Be Added)**
    *   If untracked files exist, list them explicitly and ask the user to choose one of:
        *   **Add to Git Ignore** add untracked files to `.gitignore`, then re-check status.
        *   **Add** specific untracked files to staging, then re-check status.
    *   Do not add new files without explicit user instruction.

4.  **Review Staged Diff**
    *   Command: `git diff --staged`
    *   Optional summary: `git diff --staged --stat`
    *   If no staged changes appear, return to Step 1.

5.  **Summarize Changes**
    *   Read the staged diff and produce:
        *   A concise bullet list of changes since the last commit.
        *   A single-sentence commit message suggestion (imperative mood).

6.  **Request Approval**
    *   Ask the user to approve the summary and commit message.
    *   Confirm how to handle any untracked files (ignore, add specific files, or stop).
    *   Do **not** commit until explicit approval is given.

7.  **Commit After Approval**
    *   Command: `git commit -m "<approved message>"`
    *   Expected: Commit created with the approved message.
    *   If commit fails: re-check staged files and resolve any errors.

8.  **Push to Origin**
    *   Command: `git push origin HEAD`
    *   Expected: Remote updated with the new commit.
    *   If push fails: capture the error output and report it.

## Reminder
*   First law of vibe coding: commit after every completed change.

## Verification
*   `git log -1 --oneline` shows the new commit.
*   `git status -sb` is clean.
*   `git push origin HEAD` succeeds.
