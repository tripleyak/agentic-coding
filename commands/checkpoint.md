# Quick Checkpoint (WIP Commit)

Create a work-in-progress checkpoint commit without pushing.

## Instructions

1. Run `git status` to see what files have changed
2. If there are changes:
   - Stage all changes with `git add -A`
   - Create a commit with message format: `wip: <brief description of changes>`
   - Auto-generate the description based on what files changed
3. If there are no changes, report "No changes to checkpoint"

Do NOT push to remote - this is just a local save point.

Example commit messages:
- `wip: component progress`
- `wip: hook implementation`
- `wip: refactoring in progress`
