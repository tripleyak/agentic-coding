# Context Handoff Patterns

Systematic approaches to preserving work state across context boundaries.

## Why Handoff Matters

AI agents have finite context windows. When approaching limits:
- Important details get lost
- Work gets repeated unnecessarily
- Previous failures get re-attempted

Structured handoff prevents these issues.

## The 10% Rule

**Trigger handoff when context usage reaches ~10% remaining.**

Why 10%?
- Leaves room for handoff generation
- Allows continuation instructions
- Prevents abrupt context loss

## Handoff Document Structure

Use XML sections for semantic clarity:

```markdown
# Context Handoff Document

## Original Task
<task>
The exact original request, unchanged
</task>

## Work Completed
<completed>
- Files modified (with line numbers)
- Key decisions made (with reasoning)
- Tests/verification completed
</completed>

## Work Remaining
<remaining>
- Next steps (prioritized)
- Blocked items
- Known TODOs
</remaining>

## Attempted Approaches
<attempts>
- What didn't work and WHY
- Dead ends to avoid
</attempts>

## Critical Context
<context>
- Environment details
- External references consulted
- Important discoveries
</context>

## Current State
<state>
- Git status
- Test status
- Uncommitted changes
</state>
```

## Key Principles

### 1. Prevent Wasted Effort

Document failures so they aren't repeated:

```markdown
## What Didn't Work
| Approach | Why It Failed | Learning |
|----------|---------------|----------|
| Used v2 API | Deprecated in our version | Check version first |
| Direct DOM manipulation | React hydration mismatch | Use refs instead |
```

This prevents the next session from trying the same dead ends.

### 2. Preserve Decisions

Capture reasoning, not just actions:

```markdown
## Key Decisions Made
1. **Used Context API over Redux**: Because state is local to this component tree and doesn't need global persistence.

2. **Chose synchronous validation**: Because async validation added unnecessary complexity for client-side-only checks.
```

Without reasoning, future sessions might undo good decisions.

### 3. Maintain Scope

Focus on original task, prevent scope creep:

```markdown
## Scope Boundaries
IN SCOPE:
- Fix authentication flow
- Update related tests

OUT OF SCOPE (document for later):
- Refactor user model
- Update documentation
```

### 4. Enable Seamless Continuation

Include everything needed to resume:

```markdown
## Resume Instructions
1. Read this handoff document fully
2. Review files in "Work Completed"
3. Start with first item in "Next Steps"
4. Avoid approaches in "What Didn't Work"
5. Reference "Critical Context" for environment

FOCUS: Complete original task. Do not add scope.
```

## Handoff Triggers

### Automatic Triggers

| Condition | Action |
|-----------|--------|
| 10% context remaining | Generate full handoff |
| Session timeout approaching | Generate quick summary |
| Task milestone reached | Optional checkpoint |

### Manual Triggers

| Situation | Command/Action |
|-----------|----------------|
| Stopping for the day | `/handoff` or generate manually |
| Switching contexts | Quick handoff summary |
| Complex task midpoint | Checkpoint handoff |

## Two-Tier Task Management

### Immediate (Same Day)

Use quick handoff for:
- Lunch breaks
- Quick context switches
- Short interruptions

Format:
```markdown
## Quick Handoff
**Task:** [brief description]
**Status:** [in progress/blocked/paused]
**Next:** [immediate next step]
**Blocker:** [if any]
```

### Long-Term (Days/Weeks)

Use full handoff + backlog for:
- End of work day
- Task parking
- Team handoffs

Include:
- Full handoff document
- Add to TODO backlog
- Git commit current state

## File Locations

| Type | Location | Reference |
|------|----------|-----------|
| Quick handoff | `.claude/WHATS_NEXT.md` | `@whats-next` |
| Full handoff | `.claude/CONTEXT_HANDOFF.md` | `@context-handoff` |
| Backlog | `.claude/TODOS.md` | `/todos` |

## Integration with Git

Use git as long-term memory:

```bash
# Before handoff
git add -A
git commit -m "WIP: [task description] - see CONTEXT_HANDOFF.md"
```

The commit message points to handoff details. Git history preserves state.

## Recovery from Bad Handoff

If handoff was incomplete:

1. **Check git history**: `git log --oneline -10`
2. **Review recent files**: `git diff HEAD~3`
3. **Look for TODOs**: Grep for TODO/FIXME
4. **Check test failures**: Run test suite for clues

## Template

Full template available at:
`assets/templates/context-handoff.md`

## Best Practices

1. **Generate early** - Don't wait until context is exhausted
2. **Be specific** - File paths, line numbers, exact commands
3. **Document failures** - What didn't work saves time
4. **Keep scope tight** - Original task only, note additions for later
5. **Version control** - Commit before and after handoffs
6. **Test continuation** - Verify handoff works by simulating resume

## Anti-Patterns

### Over-Compression
❌ "Made some progress on auth"
✅ "Modified auth.ts:45-78, added token refresh, tests passing"

### Missing Failures
❌ Only documenting what worked
✅ Including failed approaches with reasons

### Scope Drift
❌ "Also noticed we should refactor X, Y, Z..."
✅ "OUT OF SCOPE: X, Y, Z - add to backlog"

### No Resume Instructions
❌ Ending with current state only
✅ Explicit "Next Steps" with priorities
