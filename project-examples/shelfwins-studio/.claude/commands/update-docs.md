# Update Documentation Files

Update the 3 core documentation files to ensure consistency after a work session.

## Files to Sync

| File | Role | Source of Truth For |
|------|------|---------------------|
| `ROADMAP.md` | Feature tracking | Phases, sprints, backlog items, completion status |
| `SESSION_HANDOFF.md` | Session continuity | Current state, recent work, next steps |
| `APP_MAP.md` | Architecture reference | Code structure, components, hooks, metrics |

## Sync Process

### Step 1: Gather Current State

1. **Read all 3 documentation files:**
   - `ROADMAP.md`
   - `SESSION_HANDOFF.md`
   - `APP_MAP.md`

2. **Run verification commands:**
   ```bash
   git status
   git log --oneline -3
   npx tsc --noEmit 2>&1 | tail -5
   npm run lint 2>&1 | tail -5
   npm run test:run 2>&1 | tail -10
   ```

3. **Gather codebase metrics:**
   - Count hooks: `ls -1 src/hooks/*.ts 2>/dev/null | wc -l`
   - Count tests: `grep -r "it\|test(" src/**/*.test.ts 2>/dev/null | wc -l`
   - Count lazy components in `components/lazy.tsx`
   - App.tsx line count: `wc -l src/App.tsx`

### Step 2: Detect What Changed

Compare current state against documentation:

1. **New commits since last session?**
   - Check `git log` against SESSION_HANDOFF.md's `lastCommit`

2. **Backlog items completed?**
   - Any items marked `completed: true` in ROADMAP.md not in SESSION_HANDOFF.md's `completedThisSession`

3. **Metrics changed?**
   - Hook count, test count, component count different from APP_MAP.md

4. **Stale timestamps?**
   - "Last Updated" dates older than today

### Step 3: Generate Sync Report

Output what needs updating:

```
## Documentation Sync Report - [DATE]

### Current State
- Branch: [branch]
- Last Commit: [hash] [message]
- Verification: TypeCheck [✓/✗] | Lint [✓/✗] | Tests [✓/✗]

### Changes Detected
- [ ] [Description of change 1]
- [ ] [Description of change 2]

### Proposed Updates
1. **ROADMAP.md**: [what will change]
2. **SESSION_HANDOFF.md**: [what will change]
3. **APP_MAP.md**: [what will change]
```

### Step 4: Update Files

After showing the report, update the files:

#### ROADMAP.md Updates:
- Update `Last Updated` date in header
- Update `Current Phase` if phase completed
- Update `Note` with recent accomplishments
- Mark any newly completed backlog items as `completed: true`
- Add new backlog items if work created new tasks

#### SESSION_HANDOFF.md Updates:
- Update `Last Updated` timestamp
- Update `lastCommit` to current HEAD
- Move previous session's `completedThisSession` to history
- Add current session's work to `completedThisSession`
- Update `outstandingFromRoadmap` from ROADMAP.md backlog
- Update `environment.lastVerification` with test results
- Update `metrics` section with current counts

#### APP_MAP.md Updates:
- Update `Last Updated` date
- Update metrics (hooks count, test count, etc.)
- Add new components/hooks to reference tables if significant additions

### Step 5: Commit Changes

After updates, commit together:
```bash
git add ROADMAP.md SESSION_HANDOFF.md APP_MAP.md
git commit -m "docs: Update documentation files [$(date +%Y-%m-%d)]"
```

## Rules

1. **ROADMAP.md is source of truth for backlog** - SESSION_HANDOFF.md pulls from it
2. **Preserve JSON structure** - Keep the JSON blocks intact and valid
3. **Update timestamps** - Always update "Last Updated" dates
4. **Keep histories** - Don't delete completed items, move them to history sections
5. **Atomic commits** - All synced files committed together
6. **Ask before major changes** - If removing content or changing structure, confirm first

## Quick Reference

```bash
# Run update
/update-docs

# Manual verification before sync
npx tsc --noEmit && npm run lint && npm run test:run

# Check what changed since last update
git diff HEAD~5 --stat -- ROADMAP.md SESSION_HANDOFF.md APP_MAP.md
```
