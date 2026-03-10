# Playbook: How to Commit and Push Changes

*Status: Draft*

## Objective
Provide a repeatable workflow to summarize staged changes, propose a commit message, commit after explicit user approval, and push to `origin` only after explicit push approval, without assuming untracked files should be added.

## Prerequisites
*   Git installed and available in your shell.
*   Changes staged (`git add ...`).
*   Access to the remote `origin`.

## Step-by-Step Instructions

1.  **Check Repository Status**
    *   Command: `git status -sb`
    *   Expected: Shows staged files under `Changes to be committed`, and any untracked files under `??`.
    *   If nothing staged: run `git add <files>` and re-check.

2.  **Confirm Active Plan and Docs Are Updated**
    *   Ensure the active plan file is updated to reflect completed checklist items and any approved revisions.
    *   Ensure summary content includes active plan path and checklist item deltas for this checkpoint.
    *   If any plan file moved/changed, run `python scripts/regenerate_plan_indexes.py` before commit.
    *   Ensure playbooks/docs (if relevant) are updated before committing.
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
        *   Active plan path + checklist items updated in this checkpoint.
        *   A single-sentence commit message suggestion (imperative mood).

6.  **Prompt Journal Create/Update**
    *   After presenting the summary, ask:
        *   whether to create today's journal entry (if missing), and/or
        *   whether to append relevant checkpoint details to today's journal entry.
    *   If approved, perform the journal create/update before commit.
    *   If non-journal repository changes are in scope and journal create/update is not approved, stop before commit.

7.  **Request Approval**
    *   Ask the user to approve:
        *   the change summary,
        *   the commit message,
        *   whether to commit now,
        *   whether to push after commit.
    *   Confirm how to handle any untracked files (ignore, add specific files, or stop).
    *   Do **not** commit or push until explicit approval is given for each action.

8.  **Commit After Approval**
    *   Command: `git commit -m "<approved message>"`
    *   Expected: Commit created with the approved message.
    *   If commit fails: re-check staged files and resolve any errors.

9.  **Push to Origin (Only If Approved)**
    *   Command: `git push origin HEAD`
    *   Expected: Remote updated with the new commit.
    *   If push fails: capture the error output and report it.

## Reminder
*   First law of vibe coding: commit after every approved completed checkpoint.
*   This playbook governs git actions and intentionally does not require separate documentation updates merely to record that a commit/push happened.
*   This playbook intentionally omits a separate "Lifecycle Compliance" section because lifecycle compliance is documented in the governing task plan and execution playbook; this file defines the git execution workflow used within that lifecycle.

## Verification
*   `git log -1 --oneline` shows the new commit.
*   `git status -sb` is clean.
*   `git push origin HEAD` succeeds.
