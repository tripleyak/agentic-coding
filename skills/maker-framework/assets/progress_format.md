# MAKER Progress Report

## Project Summary

**Project:** [Name]

**Report Date:** [Date]

**Status:** [On Track / At Risk / Blocked]

---

## Progress Overview

```
[####################....................] 50%
```

| Metric | Count |
|--------|-------|
| Total Steps | X |
| Completed (Verified) | X |
| In Progress | X |
| Pending | X |
| Failed | X |
| Flagged | X |

---

## Current Focus

**Current Step:** [Step ID and description]

**Status:** [In progress / Blocked / Awaiting verification]

**Notes:** [Any relevant context]

---

## Recent Activity

| Time | Step | Action | Result |
|------|------|--------|--------|
| [Time] | [ID] | [What was done] | VERIFIED |
| [Time] | [ID] | [What was done] | FAILED |
| [Time] | [ID] | [What was done] | In progress |

---

## Milestone Status

### Milestone 1: [Name]
**Status:** [Complete / In Progress / Not Started]
**Progress:** X/Y steps complete

### Milestone 2: [Name]
**Status:** [Complete / In Progress / Not Started]
**Progress:** X/Y steps complete

### Milestone 3: [Name]
**Status:** [Complete / In Progress / Not Started]
**Progress:** X/Y steps complete

---

## Active Red Flags

| Step | Flag | Severity | Status |
|------|------|----------|--------|
| [ID] | [Description] | High/Medium/Low | Open/Resolved |
| [ID] | [Description] | High/Medium/Low | Open/Resolved |

**Total Active Flags:** X

---

## Success Probability

**Calculation Parameters:**
- Total remaining steps: X
- Observed success rate: Y%
- Verification level (k): Z

**Projected Success Rate:** X%

**Recommendation:** [Continue / Increase verification / Review approach]

---

## Blockers

| Blocker | Impact | Required Action | Owner |
|---------|--------|-----------------|-------|
| [Issue] | [Which steps blocked] | [What's needed] | [Who] |

---

## Next Steps

1. [ ] [Next immediate action]
2. [ ] [Following action]
3. [ ] [After that]

---

## Notes

[Any additional observations, concerns, or decisions made]

---

## Commands for This Report

```bash
# View current tree
python ~/.claude/skills/maker-framework/scripts/progress_visualizer.py tree [PROJECT_FILE]

# View statistics
python ~/.claude/skills/maker-framework/scripts/progress_visualizer.py stats [PROJECT_FILE]

# Calculate success probability
python ~/.claude/skills/maker-framework/scripts/success_calculator.py analyze [PROJECT_FILE]

# Get next step
python ~/.claude/skills/maker-framework/scripts/maker_tracker.py next --project [PROJECT_FILE]
```
