# Sync Documentation Files

Synchronize the 3 core documentation files to ensure consistency after a work session.
**Includes safe pruning of completed items to prevent file bloat.**

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
   - Count hooks: `ls -1 hooks/*.ts 2>/dev/null | wc -l`
   - Count tests: `npm run test:run 2>&1 | grep -E "Tests.*passed"`
   - Count components: `ls -1 components/*.tsx 2>/dev/null | wc -l`

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

### Step 3: Identify Items to Prune (SAFETY-CRITICAL)

**IMPORTANT: Only prune items that are DEFINITIVELY completed. When in doubt, keep the item.**

#### What Qualifies as "Completed" (ALL must be true):
1. Item has explicit completion marker:
   - `completed: true` in JSON
   - `status: "completed"` or `status: "done"`
   - `[x]` checkbox (checked)
   - `✅` or `DONE` or `COMPLETE` or `PASSED` in status field
2. Item is NOT marked as:
   - `in_progress`, `in-progress`, `active`, `current`, `pending`, `todo`, `blocked`
   - `[ ]` (unchecked checkbox)
   - `🔄` or `⏳` or `🚧` (in-progress indicators)
3. Item belongs to a phase/sprint that is fully completed (not current phase)

#### What to Prune in ROADMAP.md:
- **Backlog items** with `completed: true` that are older than 30 days
- **Completed phases** that are 2+ phases behind current (keep last completed phase for reference)
- **Sprint entries** from completed phases

#### What to Prune in SESSION_HANDOFF.md:
- **completedThisSession history** older than 5 sessions
- **Old session summaries** beyond the last 3

#### NEVER Prune:
- Current phase or sprint
- Any item without explicit completion marker
- Items marked `in_progress`, `pending`, `blocked`, or similar
- The most recent completed phase (keep for reference)
- Any item you're unsure about - ASK THE USER

### Step 4: Generate Sync Report

Output what needs updating AND what will be pruned:

```
## Documentation Sync Report - [DATE]

### Current State
- Branch: [branch]
- Last Commit: [hash] [message]
- Verification: TypeCheck [✓/✗] | Lint [✓/✗] | Tests [✓/✗]

### Changes Detected
- [ ] [Description of change 1]
- [ ] [Description of change 2]

### Items to Prune (Completed)
#### ROADMAP.md:
- [List each item to be removed with its completion date]

#### SESSION_HANDOFF.md:
- [List old session history to be removed]

### Proposed Updates
1. **ROADMAP.md**: [what will change]
2. **SESSION_HANDOFF.md**: [what will change]
3. **APP_MAP.md**: [what will change]

⚠️ Please confirm pruning before proceeding.
```

### Step 5: Update Files (After User Confirmation)

After showing the report and getting user confirmation for pruning:

#### ROADMAP.md Updates:
- Update `Last Updated` date in header
- Update `Current Phase` if phase completed
- Update `Note` with recent accomplishments
- Mark any newly completed backlog items as `completed: true`
- Add new backlog items if work created new tasks
- **PRUNE**: Remove confirmed completed items per Step 3 rules

#### SESSION_HANDOFF.md Updates:
- Update `Last Updated` timestamp
- Update `lastCommit` to current HEAD
- Update `completedThisSession` with current session's work
- Update `outstandingFromRoadmap` from ROADMAP.md backlog
- Update `environment.lastVerification` with test results
- Update `metrics` section with current counts
- **PRUNE**: Remove old session history per Step 3 rules

#### APP_MAP.md Updates:
- Update `Last Updated` date
- Update metrics (hooks count, test count, etc.)
- Add new components/hooks to reference tables if significant additions

### Step 6: Commit Changes

After updates, commit together:
```bash
git add ROADMAP.md SESSION_HANDOFF.md APP_MAP.md
git commit -m "docs: Sync documentation files $(date +%Y-%m-%d)"
```

## Rules

1. **ROADMAP.md is source of truth for backlog** - SESSION_HANDOFF.md pulls from it
2. **Preserve JSON structure** - Keep the JSON blocks intact and valid
3. **Update timestamps** - Always update "Last Updated" dates
4. **Safe pruning** - Only remove items with EXPLICIT completion markers
5. **Atomic commits** - All synced files committed together
6. **Ask before pruning** - Always show what will be removed and get confirmation
7. **When in doubt, keep it** - Never delete an item you're unsure about

## Pruning Safety Checklist

Before removing ANY item, verify:
- [ ] Item has explicit `completed: true` or equivalent marker
- [ ] Item is NOT in current phase/sprint
- [ ] Item does NOT have `in_progress`, `pending`, `blocked` status
- [ ] Item is old enough (30+ days for backlog, 5+ sessions for history)
- [ ] User has confirmed the removal

## Quick Reference

```bash
# Run sync with pruning
/sync-docs

# Manual verification before sync
npx tsc --noEmit && npm run lint && npm run test:run

# Check what changed since last sync
git diff HEAD~5 --stat -- ROADMAP.md SESSION_HANDOFF.md APP_MAP.md
```
