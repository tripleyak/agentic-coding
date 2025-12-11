# Ship Changes

Commit all changes and push to origin.

## Instructions

1. Check for changes:
   ```bash
   git status
   ```
   - If no changes, report "Nothing to ship" and exit

2. Stage all changes:
   ```bash
   git add -A
   ```

3. Show what will be committed:
   ```bash
   git diff --cached --stat
   ```

4. Generate a commit message based on the changes:
   - Look at what files changed
   - Create a descriptive commit message
   - Format: `<type>: <description>`
   - Types: feat, fix, refactor, docs, style, perf, chore

5. Commit with the generated message:
   ```bash
   git commit -m "<message>

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   Co-Authored-By: Claude <noreply@anthropic.com>"
   ```

6. Push to origin:
   ```bash
   git push origin HEAD
   ```
   - If push fails due to no upstream, use: `git push -u origin $(git branch --show-current)`

7. Report success with:
   - Commit hash
   - Branch name
   - Number of files changed
