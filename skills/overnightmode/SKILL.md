# OvernightMode Skill

Enables 5-hour autonomous operation with task queuing and zero error verification.

**Triggers:** `overnight`, `run overnight`, `queue tasks`, `work while I sleep`

**Domain:** Automation / Meta

---

## Zero Error Standard

**Error tolerance: 0%**

OvernightMode runs autonomously but maintains the same quality standards as interactive work:

| Principle | Implementation |
|-----------|----------------|
| Zero errors | Every task verified with 0 type/lint/test/build errors |
| Correctness over speed | Take time needed; don't rush overnight |
| Fix, never skip | Errors are fixed, not skipped or worked around |
| Done = verified | Task complete only when 100% verified correct |

**The 5-hour limit exists to give Claude enough time to achieve perfection — not to fill time with work.**

---

## How to Use

1. Create `OVERNIGHT_TASKS.md` in your project root
2. Run `overnight` or start Claude with the task file present
3. Go to sleep
4. Review `OVERNIGHT_LOG.md` in the morning

---

## Task File Format (OVERNIGHT_TASKS.md)

```markdown
# Overnight Tasks

## Priority 1 (Critical)
- [ ] Fix all TypeScript errors in src/
- [ ] Run full test suite and fix failures

## Priority 2 (Important)
- [ ] SecurityAudit on authentication flow
- [ ] PerfOptimize the dashboard page

## Priority 3 (Nice to Have)
- [ ] Update all dependencies
- [ ] Generate API documentation

## Instructions
- Commit after each major task
- Stop if tests fail after 3 retry attempts
- Skip UI changes (need visual review)
```

---

## Configuration

| Setting | Value | Purpose |
|---------|-------|---------|
| `checkpoints.require_approval` | `[]` | No pauses |
| `timeout_per_skill` | `30m` | Long-running tasks |
| `max_total_runtime` | `5h` | Hard cap (but stops early when done) |
| `on_skill_failure` | `retry_until_fixed` | Keep fixing until zero errors |
| `require_zero_errors` | `true` | Never mark complete with errors |
| `stop_when` | `task_verified_complete` | Stop immediately when done |

---

## Behavior

| Situation | Action |
|-----------|--------|
| Task implemented | Run full verification chain |
| Verification passes | Log, commit, next task |
| Verification fails | Fix issues, re-run verification (loop until zero errors) |
| All tasks verified complete | Write summary, **stop immediately** |
| 5 hours elapsed | Hard stop, checkpoint remaining work |

---

## Verification Chain

Every task runs through this before being marked complete:

```
1. tsc --noEmit       → 0 errors
2. npm run lint       → 0 errors
3. npm run test:run   → 0 failures
4. npm run build      → succeeds
5. CodeReview         → 5 Opus agents, unanimous approval
```

**If any check fails:** Fix → Re-run all checks → Repeat until zero errors

---

## Output Files

| File | Purpose |
|------|---------|
| `OVERNIGHT_LOG.md` | Detailed log of all actions, decisions, errors |
| `OVERNIGHT_TASKS.md` | Updated with [x] for completed, notes for skipped |
| `SESSION_HANDOFF.md` | State for next session |
| Git commits | One per major task completed |

---

## Safety Guardrails

| Guardrail | Reason |
|-----------|--------|
| No force pushes | Protect git history |
| No destructive DB ops | Prevent data loss |
| No production deploys | Require human approval |
| No secret/env changes | Security sensitive |
| Backup branch created | Can always rollback |

---

## Example Run

```
22:00 - Session starts, reads OVERNIGHT_TASKS.md
22:01 - Creates backup branch: backup/overnight-2024-01-15
22:02 - Task 1: Fix TypeScript errors (SkillComposer → MAKER)
22:45 - Task 1 complete (0 errors verified), committed
22:46 - Task 2: Run tests, fix failures
01:30 - Task 2 complete after 3 test-fix cycles (0 failures)
01:31 - Task 3: SecurityAudit
02:15 - Task 3 complete, 2 issues fixed and verified
02:16 - Task 4: PerfOptimize
03:00 - Task 4 complete
03:01 - All tasks verified complete
03:02 - Writing summary, session ends

Duration: 5h 02m
Commits: 4
Files changed: 127
Verification: All passed with 0 errors
```

---

## Integration

Combines with:
- **SkillComposer** for complex multi-skill tasks
- **MAKER** for systematic execution with verification
- **BackupSnapshot** for safety
- **GitWorkflow** for commits
- **ErrorExplainer** for auto-diagnosing failures
- **CodeReview** for unanimous 5-agent verification

---

## Key Principle

**There is no "good enough." There is only correct or not yet correct.**

OvernightMode doesn't work for working's sake. It works until every task is verified 100% correct with zero errors, then it stops.
