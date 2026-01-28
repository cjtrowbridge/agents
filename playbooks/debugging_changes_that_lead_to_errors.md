# Playbook: Debugging Changes That Lead to Errors

*Status: Draft*

## Objective

Provide a repeatable, anti-hallucination workflow for debugging when a change produces an error or unexpected behavior. This playbook forces **evidence-first diagnosis**, **deep reflection**, and **documentation updates** so the same mistake is less likely to recur.

## Prerequisites

* You can reproduce the failure (or you can describe precisely when/where it happens).
* You have access to the repo and can run the relevant command/test.
* You can view:

  * `git status -sb`
  * `git diff` (and `git diff --staged` if applicable)
  * the full error output / logs

## Step-by-Step Instructions

### 0) Stabilize the Scene (No Fixing Yet)

1. **Do not start editing files.**
2. Capture and paste (or record) the **exact command** that failed and its **full output**.
3. Record the **expected outcome** in one sentence.
4. Record the **actual outcome** in one sentence.

### 1) Reflect Deeply on What Changed

> **Think deeply**: You are likely to jump to the wrong first conclusion. Your job is to ground yourself in the diff and the original intent.

1. Run `git status -sb`.
2. Run `git diff` (and `git diff --staged` if relevant).
3. Create an **Evidence List**:

   * Files changed
   * Key functions/lines affected
   * Any config/build changes
4. Restate the **original intention** of the change (what you were trying to accomplish).
5. Compare intention vs reality:

   * **Why is the actual outcome different than expected?** (Write 3-5 sentences.)

### 2) Reproduce Reliably and Minimize Variables

1. Re-run the failing command exactly.
2. If it's intermittent, run it 3 times and note differences.
3. Identify the smallest reproducible case:

   * Can you reproduce with fewer inputs, smaller data, or a single module?

### 3) Categorize the Failure

Classify the failure into one of these buckets (pick the best match):

* **Syntax / parse error** (compiler/interpreter will not run)
* **Type / API contract error** (wrong args/shape/return)
* **Logical error** (runs but wrong result)
* **State / environment issue** (paths, permissions, deps, env vars)
* **Integration mismatch** (component boundaries, version mismatch)
* **Test expectation mismatch** (test wrong vs code wrong)

### 4) Generate Multiple Hypotheses (Before Fixing)

> **Reflect deeply** and resist anchoring.

1. Produce **at least 3 plausible hypotheses**.
2. For each hypothesis, list:

   * What evidence supports it?
   * What evidence would refute it?
   * The **cheapest experiment** to test it (no big refactors).

### 5) Run the Smallest Experiments

1. Execute the cheapest experiment for hypothesis #1.
2. If refuted, move to the next hypothesis.
3. Keep a short log:

   * Experiment -> result -> conclusion

### 6) Identify the Smallest Safe Fix

1. Once you have a likely cause, propose the **minimal change** that should fix it.
2. Explicitly list:

   * Files to change
   * Lines/sections to touch
   * Any doc/playbook updates required

### 7) Plan & Request Approval (Required)

Before implementing:

1. Present:

   * Evidence summary (diff + error)
   * Hypotheses tested and outcomes
   * Proposed fix (minimal)
   * Verification plan
   * Docs/playbook updates
2. Ask for explicit approval to proceed.

### 8) Execute the Fix (After Approval)

1. Apply the minimal change.
2. Add/adjust logging if it helps future diagnosis (do not spam).
3. Keep the change atomic.

### 9) Verify

1. Re-run the failing command/test.
2. If tests exist, run the smallest relevant suite.
3. Confirm:

   * The error is gone
   * The outcome matches the stated expectation

### 10) Prevent Recurrence (Self-Evolving Loop)

> **Assume you will make the same mistake again** unless you update the repo's policy.

1. Update documentation where future-you will see it first:

   * `README.md` if behavior/usage changed
   * `AGENTS.md` if this is a new operational rule
   * Add/update a playbook note if this is a recurring pitfall
2. Update the task plan or playbook if new steps were discovered or the workflow changed.
3. Add a short **"Known Failure Mode"** note:

   * Symptom
   * Cause
   * Fix
   * How to detect early

### 11) Git Hygiene (If in a git repo)

Follow the commit playbook:

* Check status/diff
* Suggest a commit message
* Commit after completion
* First law of vibe coding: commit after every completed change

## Verification

* The original failure is no longer reproducible.
* Evidence log explains what changed and why the fix addresses it.
* Documentation/playbooks updated to prevent recurrence.

## Lifecycle Compliance

Prompt -> Plan (based on a known playbook) -> Request approval -> Execute -> Plan/playbook update -> Docs update -> Verification.

If inside a git repo:

* Review `git status` and diffs
* Suggest a commit message
* Commit after completion
* First law of vibe coding: commit after every completed change
