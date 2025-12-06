# Refactor Skill

Code improvement. **Triggers:** `Refactor`, `refactor this`, `clean up code`

**Process:** Analyze (smells, deps, coverage) → Plan (prioritize, criteria) → Execute (one at a time, test after) → Verify

| Smell | Fix |
|-------|-----|
| Long fn (>50 lines) | Extract Method |
| Large class (>300) | Extract Class |
| Duplicate code | Extract shared fn |
| Deep nesting (>3) | Early returns |
| Long params (>4) | Parameter Object |

**Steps:** Tests exist → Smallest change → Run tests → Commit → Repeat
