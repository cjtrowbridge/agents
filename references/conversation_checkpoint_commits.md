# Conversation Checkpoint Commits

## What Is a Checkpoint

- A checkpoint is a completed conversation slice, not project completion.
- Examples:
  - Daily kickoff captured and written.
  - Kanban moves applied and recorded.
  - A focused bugfix discussion captured with resulting file edits.

## What to Include in Checkpoint Summary

- Files changed and why.
- Active plan path for the checkpoint.
- Checklist items changed (`[x]` / `[?]` / `[-]` / newly added plan items).
- Journal updates added in this checkpoint.
- Any user-only journal fields and whether user input was provided.
- Kanban moves with exact task text.
- Any unresolved items or follow-up questions.

## Approval Language Pattern

- "Here is what I captured and where it will be written."
- "This checkpoint updates plan `path/to/plan.md` items: [...]."
- "Do you want me to create or update today's journal entry with this checkpoint?"
- "Approve saving this snapshot?"
- "Approve commit + push for this journal checkpoint?"
- Journal-only exception: if staged scope is only journal updates, commit/push may proceed without a commit approval prompt after summary.
- User-only journal fields must remain verbatim user text (or an empty list item `-` if no user input was provided).

## Avoiding Commit Spam While Preserving Auditability

- Commit at meaningful checkpoint boundaries rather than every single message.
- Keep each checkpoint commit small and scoped.
- Use consistent commit messages with date + checkpoint intent.
- Treat "completed change" as "completed checkpoint" for commit cadence in this workflow.
