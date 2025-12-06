# Sync with Main Branch

Pull latest from main and rebase current branch.

## Instructions

1. Check current branch: `git branch --show-current`
   - If on main/master, just pull: `git pull origin main`
   - If on feature branch, continue below

2. Check for uncommitted changes: `git status`
   - If there are changes, stash them: `git stash`

3. Fetch and rebase:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

4. If there were stashed changes, restore them:
   ```bash
   git stash pop
   ```

5. Report:
   - How many commits were pulled
   - If rebase was successful or had conflicts
   - Current status after sync

If there are rebase conflicts:
- Report which files have conflicts
- Do NOT auto-resolve - ask user how to proceed
