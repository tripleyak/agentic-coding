# BackupSnapshot Skill

Creates restore points before big changes. Peace of mind for risky operations.

**Triggers:** `backup`, `snapshot`, `save state`, `create restore point`, `before I break something`

**Domain:** DevOps / Safety

## Process

| Phase | Action |
|-------|--------|
| 1. Check | Verify git status |
| 2. Stash | Save uncommitted changes if any |
| 3. Branch | Create timestamped backup branch |
| 4. Confirm | Report snapshot location |

## Snapshot Types

| Type | When | Command |
|------|------|---------|
| Quick | Before small changes | `git stash push -m "snapshot"` |
| Branch | Before refactors | `git branch backup/[timestamp]` |
| Full | Before major changes | Branch + stash + remote push |

## Commands

### Quick Snapshot (Stash)
```bash
# Save current work
git stash push -m "snapshot-$(date +%Y%m%d-%H%M%S)"

# List snapshots
git stash list

# Restore
git stash pop
```

### Branch Snapshot
```bash
# Create backup branch from current state
git branch backup/$(date +%Y%m%d-%H%M%S)

# Verify
git branch | grep backup/

# Restore
git checkout backup/[timestamp]
```

### Full Snapshot
```bash
# Stash any uncommitted work
git stash push -m "pre-snapshot-$(date +%Y%m%d-%H%M%S)"

# Create backup branch
git branch backup/$(date +%Y%m%d-%H%M%S)

# Push to remote for extra safety
git push origin backup/$(date +%Y%m%d-%H%M%S)

# Return to work
git stash pop
```

## Auto-Trigger Conditions

| Operation | Auto-Snapshot |
|-----------|---------------|
| Large refactor (>10 files) | Yes |
| Dependency major update | Yes |
| Database migration | Yes |
| Before `git rebase` | Yes |
| Before `git reset` | Yes |

## Output Format

```markdown
## Snapshot Created

| Detail | Value |
|--------|-------|
| Type | [Quick/Branch/Full] |
| Timestamp | [YYYY-MM-DD HH:MM:SS] |
| Branch | `backup/20241204-143022` |
| Stash | `stash@{0}: snapshot-20241204-143022` |
| Remote | [Pushed/Local only] |

### Current State
- Files modified: [count]
- Files staged: [count]
- Commits ahead: [count]

### To Restore
```bash
# Option 1: Checkout backup branch
git checkout backup/20241204-143022

# Option 2: Cherry-pick from backup
git cherry-pick [commit-hash]

# Option 3: Pop stash
git stash pop
```

### To Delete (when no longer needed)
```bash
git branch -d backup/20241204-143022
git stash drop stash@{0}
```
```

## Cleanup

| Age | Action |
|-----|--------|
| < 1 day | Keep |
| 1-7 days | Keep if uncommitted work |
| > 7 days | Safe to delete |

```bash
# List old backup branches
git branch | grep backup/

# Delete old backups
git branch -d backup/[old-timestamp]

# Clean old stashes
git stash list
git stash drop stash@{n}
```

## Integration

| With Skill | Purpose |
|------------|---------|
| GitWorkflow | Snapshot before risky git ops |
| MAKER | Snapshot before multi-step tasks |
| Refactor | Snapshot before refactoring |
| DeploymentGuide | Snapshot before deploy |
