# GitWorkflow Skill

Automates branching, commits, and PR creation with good messages. Prevents git mistakes that lose work. Lightweight wrapper around superpowers plugin skills.

**Triggers:** `create branch`, `commit changes`, `open PR`, `git help`, `save my work`

**Domain:** DevOps / Version Control

> **Note:** This skill integrates with superpowers plugin skills:
> - `using-git-worktrees` - For isolated feature work
> - `finishing-a-development-branch` - For merge/PR/cleanup

## Process

| Phase | Action |
|-------|--------|
| 1. Status | Check current git state |
| 2. Decide | Determine operation (branch/commit/PR) |
| 3. Execute | Run git commands safely |
| 4. Confirm | Verify operation succeeded |

## Operations

### Create Branch
```bash
# Check status first
git status

# Create and switch
git checkout -b feature/[name]

# Push and set upstream
git push -u origin feature/[name]
```

| Branch Type | Prefix | Example |
|-------------|--------|---------|
| Feature | `feature/` | `feature/add-auth` |
| Bugfix | `fix/` | `fix/login-error` |
| Hotfix | `hotfix/` | `hotfix/security-patch` |
| Refactor | `refactor/` | `refactor/cleanup-utils` |

### Smart Commit
```bash
# Stage changes
git add -A

# Commit with generated message
git commit -m "[type]: [description]

[body if needed]

🤖 Generated with Claude Code"
```

| Commit Type | When |
|-------------|------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Code change that neither fixes nor adds |
| `docs` | Documentation only |
| `style` | Formatting, no code change |
| `test` | Adding tests |
| `chore` | Maintenance tasks |

### Open PR
```bash
# Push current branch
git push -u origin [branch]

# Create PR
gh pr create --title "[title]" --body "[body]"
```

## Safety Rules

| Rule | Action |
|------|--------|
| Never force push to main/master | Block with warning |
| Uncommitted changes before checkout | Stash or commit first |
| Large number of files (>20) | Confirm with user |
| Sensitive files (.env, secrets) | Warn and exclude |
| Merge conflicts | Explain and guide resolution |

## Output Format

```markdown
## Git Operation: [type]

### Before
- Branch: `main`
- Status: 3 modified, 1 new

### Action Taken
- Created branch: `feature/add-auth`
- Staged: 4 files
- Committed: "feat: add user authentication"

### After
- Branch: `feature/add-auth`
- Ahead of origin by: 1 commit

### Next Steps
1. Continue working, or
2. `git push` to sync with remote, or
3. Open PR when ready
```

## Common Fixes

| Problem | Solution |
|---------|----------|
| "Changes not staged" | `git add -A` |
| "Branch already exists" | Use different name or checkout existing |
| "Merge conflicts" | Guide through resolution |
| "Detached HEAD" | `git checkout main` |
| "Push rejected" | `git pull --rebase` then push |

## Integration

| With Skill | Purpose |
|------------|---------|
| BackupSnapshot | Auto-snapshot before risky operations |
| superpowers:using-git-worktrees | Delegate worktree creation |
| superpowers:finishing-a-development-branch | Delegate PR/merge flow |
| ErrorExplainer | Explain git errors |
