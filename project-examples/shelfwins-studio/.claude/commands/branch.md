# Create Feature Branch

Create and switch to a new feature branch.

## Arguments
$ARGUMENTS = branch name (e.g., "feature/product-library" or "fix/drag-drop-bug")

## Instructions

1. Check for uncommitted changes: `git status`
   - If there are changes, warn the user and ask if they want to stash or commit first
   - Do NOT proceed if there are uncommitted changes without user confirmation

2. Fetch latest from remote: `git fetch origin`

3. Create branch from main:
   ```bash
   git checkout -b <branch-name> origin/main
   ```
   - If origin/main doesn't exist, try `main` or `master`

4. Confirm the branch was created and switched:
   ```bash
   git branch --show-current
   ```

5. Report success with the new branch name

Branch name from arguments: $ARGUMENTS
