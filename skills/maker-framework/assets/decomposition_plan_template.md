# MAKER Decomposition Plan

## Project Overview

**Project Name:** [Name]

**Description:** [Brief description of what this project accomplishes]

**Target Reliability:** [e.g., 99%, 95%]

**Estimated Total Steps:** [Number]

**Estimated Complexity:** [Low / Medium / High / Extreme]

---

## Success Criteria

What must be true for this project to be considered complete?

1. [ ] [Criterion 1]
2. [ ] [Criterion 2]
3. [ ] [Criterion 3]

---

## Decomposition Tree

### Milestone 1: [Name]
**Goal:** [What this milestone accomplishes]

- [ ] Task 1.1: [Description]
  - [ ] Step 1.1.1: [Atomic step]
  - [ ] Step 1.1.2: [Atomic step]
- [ ] Task 1.2: [Description]
  - [ ] Step 1.2.1: [Atomic step]

### Milestone 2: [Name]
**Goal:** [What this milestone accomplishes]

- [ ] Task 2.1: [Description]
  - [ ] Step 2.1.1: [Atomic step]
  - [ ] Step 2.1.2: [Atomic step]

### Milestone 3: [Name]
**Goal:** [What this milestone accomplishes]

- [ ] Task 3.1: [Description]
  - [ ] Step 3.1.1: [Atomic step]

---

## Dependencies

| Step | Depends On | Notes |
|------|------------|-------|
| 1.2.1 | 1.1.2 | [Why] |
| 2.1.1 | Milestone 1 | [Why] |

---

## Risk Areas / Red Flag Watchlist

Areas that may need extra attention:

1. **[Area 1]:** [Why this is risky, what to watch for]
2. **[Area 2]:** [Why this is risky, what to watch for]

---

## Verification Strategy

**Verification Level (k):** [Recommended k value]

**Milestone Checkpoints:** [How often to do major verification]

**Key Verification Points:**
- After [step/milestone]: [What to verify]
- After [step/milestone]: [What to verify]

---

## Notes

[Any additional context, constraints, or considerations]

---

## Initialization Command

```bash
python ~/.claude/skills/maker-framework/scripts/maker_tracker.py init "[Project Name]" "[Description]"
```
