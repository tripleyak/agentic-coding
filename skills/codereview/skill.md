# CodeReview Skill

Multi-agent code review with Zero Error Standard. **Triggers:** `CodeReview`, `review code`, `PR review`

## Zero Error Standard

**No code is approved with known issues. Fix first, then re-review.**

| Principle | Meaning |
|-----------|---------|
| Zero issues for approval | Unanimous 5/5 Opus agents must find zero issues |
| All issues require fixes | Critical AND Warning severity = must fix (not optional) |
| Fix then re-review | Any issue found → fix → run CodeReview again |
| No exceptions | "Minor" issues still block approval |

## 5-Agent Panel (Opus)

| Agent | Checks |
|-------|--------|
| Security | OWASP, injection, XSS, auth |
| Performance | O(n), memory, N+1, bundle |
| Patterns | SOLID, DRY, abstractions |
| Quality | Naming, errors, types |
| A11y/UX | ARIA, keyboard, contrast |

## Severity Levels

| Level | Symbol | Action |
|-------|--------|--------|
| Critical | 🔴 | **MUST FIX** - Blocks approval |
| Warning | 🟠 | **MUST FIX** - Blocks approval |
| Suggestion | 🟡 | Fix recommended (does not block, but consider) |
| Passed | 🟢 | No action needed |

**Note:** Both Critical and Warning block approval. The Zero Error Standard means no known issues are acceptable.

## Approval Criteria

```
APPROVED only when:
  ✓ All 5 agents report 🟢 Passed (unanimous)
  ✓ Zero 🔴 Critical issues
  ✓ Zero 🟠 Warning issues
  ✓ Pre-checks all pass
```

## Pre-checks (Must Pass First)

```bash
tsc --noEmit      # 0 type errors
npm run lint      # 0 lint errors
npm run test:run  # 0 test failures
npm audit         # No critical vulnerabilities
```

## Review Loop

```
1. Run pre-checks → any fail? → fix first
2. Run 5-agent review
3. Any 🔴 or 🟠 found? → fix all issues
4. Re-run CodeReview
5. Repeat until unanimous 5/5 approval
```

## Output

| Result | Meaning |
|--------|---------|
| ✅ APPROVED | 5/5 agents pass, zero issues |
| ❌ CHANGES REQUIRED | Issues found, fix list provided |

**Never approve with known issues. Zero tolerance.**
