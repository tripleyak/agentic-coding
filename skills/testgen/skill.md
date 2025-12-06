# TestGen Skill

Comprehensive tests with zero tolerance for failures. **Triggers:** `TestGen`, `generate tests`, `write tests`

**Tests are not complete until they all pass with zero failures.**

## Zero Error Standard

| Rule | Meaning |
|------|---------|
| 100% pass rate required | All generated tests MUST pass |
| Fix, never skip | If tests fail after generation, fix them (never skip or disable) |
| Coverage = minimum | Coverage targets are floors, not ceilings |
| Verified complete | Tests are done only when `npm run test:run` shows 0 failures |

**Verification chain (run after every test generation):**
```
npm run test:run   → 0 failures (REQUIRED)
npm run coverage   → meets minimums
tsc --noEmit       → 0 type errors in test files
```

**If tests fail:** Diagnose → Fix → Re-run → Repeat until 0 failures

## Coverage Minimums (Floors, Not Goals)

| Layer | Minimum Coverage | Tools |
|-------|------------------|-------|
| Unit | 80%+ | Vitest, Jest |
| Integration | Key flows | Testing Library |
| E2E | Critical paths | Playwright |

| Metric | Minimum |
|--------|---------|
| Statements | 70% |
| Branches | 65% |
| Functions | 75% |

*Exceeding these is expected. Meeting them is the bare minimum.*

## 3-Agent Panel

| Agent | Scope |
|-------|-------|
| Unit | Functions, hooks, edge cases, error paths |
| Integration | Components, API calls, state management |
| E2E | User journeys, critical paths |

## Process

| Phase | Action |
|-------|--------|
| Generate | Create tests for target code |
| Run | Execute all tests |
| Verify | Confirm 0 failures |
| Fix | If failures, diagnose and fix (loop until passing) |
| Coverage | Confirm minimums met |
| Complete | Only mark done when verified passing |

## Anti-Patterns (Never Do These)

| Anti-Pattern | Correct Approach |
|--------------|------------------|
| `.skip()` failing tests | Fix the test or the code |
| `expect(true).toBe(true)` | Write meaningful assertions |
| Commenting out tests | Delete or fix |
| Ignoring flaky tests | Fix race conditions, use proper waits |
| "Tests pass locally" | Must pass in CI too |

## Quality Checklist

```
[ ] All tests pass (0 failures)
[ ] No skipped tests
[ ] Coverage meets minimums
[ ] No type errors in test files
[ ] Tests are deterministic (not flaky)
[ ] Tests actually test behavior (not implementation)
```
