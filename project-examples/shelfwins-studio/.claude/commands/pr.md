# Create Pull Request

Create a pull request with auto-generated summary.

## Instructions

1. Check current branch: `git branch --show-current`
   - If on main/master, warn and exit

2. Check if branch has remote: `git status`
   - If not pushed, push with: `git push -u origin <branch-name>`

3. Get commit history for PR description:
   - Run: `git log main..<current-branch> --oneline`
   - If main doesn't exist, try: `git log origin/main..<current-branch> --oneline`

4. Create PR using GitHub CLI:
```bash
gh pr create --title "<branch-name-as-title>" --body "$(cat <<'EOF'
## Summary
<Generate 2-3 bullet points summarizing the commits>

## Changes
<List the commits>

## Test Plan
- [ ] Manual testing completed
- [ ] No console errors
- [ ] Build passes

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

5. Report the PR URL when done
