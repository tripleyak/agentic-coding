---
name: maker-framework
license: MIT
model: claude-opus-4-5-20251101
subagent_model: claude-opus-4-5-20251101
---

# MAKER Framework

A systematic approach to solving complex multi-step tasks with high reliability through Maximal Agentic Decomposition, zero-error verification, and red-flag detection.

## Overview

Complex tasks fail because errors compound: a 99% success rate per step yields only 37% success over 100 steps. MAKER solves this through four principles:

1. **Zero Error Standard** - Error tolerance is 0%. There is no "good enough" — only correct or not yet correct
2. **Maximal Decomposition (MAD)** - Break tasks into the smallest possible atomic steps
3. **Step Verification** - Each step verified with zero errors before proceeding
4. **Red-Flagging** - Detect and fix unreliable outputs immediately

The framework transforms unreliable multi-step execution into a reliable process where every step is verified correct with zero errors.

## Zero Error Standard

**Error tolerance: 0%**

| Rule | Meaning |
|------|---------|
| Zero errors | 0 type errors, 0 lint errors, 0 test failures, 0 build errors |
| Correctness over speed | Take the time needed to be correct; never rush to "done" |
| Verify with evidence | Run checks, see passing output, confirm with your own eyes |
| Fix, never skip | Errors are fixed, not tolerated, not worked around, not ignored |
| Done = verified correct | A step is complete only when 100% verified with zero errors |

**There is no "good enough." There is only correct or not yet correct.**

## The MAKER Process

### Phase 1: Decomposition

Before executing, decompose the entire task into a tree structure:

```
Project Goal
├── Milestone 1
│   ├── Task 1.1
│   │   ├── Step 1.1.1 (atomic)
│   │   └── Step 1.1.2 (atomic)
│   └── Task 1.2
│       └── Step 1.2.1 (atomic)
└── Milestone 2
    └── ...
```

**Decomposition rules:**
- Each step must be independently verifiable
- Steps should take <5 minutes to execute
- Output format must be predictable
- No step should contain hidden sub-decisions

Initialize tracking:
```bash
python ~/.claude/skills/maker-framework/scripts/maker_tracker.py init "Project Name" "Description"
```

Add steps to the tree:
```bash
python ~/.claude/skills/maker-framework/scripts/maker_tracker.py add-step "Step description" --parent <parent_id>
```

### Phase 2: Execute-Verify Loop

For each pending step:

1. **Propose** - Present the step and intended approach
2. **Execute** - Perform the step
3. **Verify** - User validates result with VERIFIED / UNCERTAIN / FAILED
4. **Record** - Update tracking with result

```bash
python ~/.claude/skills/maker-framework/scripts/maker_tracker.py update <step_id> --status verified
```

If UNCERTAIN or FAILED:
- Fix the issue — never skip or work around
- Re-run verification until zero errors
- If repeated failures, decompose further and fix each sub-step
- Escalate to user only after exhausting fix attempts

### Phase 3: Red-Flag Monitoring

Throughout execution, watch for reliability signals. When detected:

1. Stop immediately
2. Diagnose root cause
3. Fix the issue — skipping is never an option
4. Re-verify with zero errors before proceeding

```bash
python ~/.claude/skills/maker-framework/scripts/maker_tracker.py flag <step_id> "Red flag description"
```

## Decomposition Methodology

### Granularity Decision

Ask: "Can the user verify this step's correctness in under 30 seconds?"

- **Yes** → Step is atomic enough
- **No** → Decompose further

### Task-Type Patterns

**Coding tasks:**
- Decompose by function/component, not by file
- Each step: implement one function OR write tests for one function OR fix one bug
- Interface definitions are separate steps from implementations

**Data/Analysis tasks:**
- Decompose into: load → validate → transform → analyze → output
- Each transformation is a separate step
- Validation checkpoints between phases

**Workflow/Automation:**
- Model as state machine: each state transition is a step
- Error handling paths are explicit steps
- Rollback procedures are documented steps

**General problem-solving:**
- Goal → subgoal hierarchy
- Each decision point is a step
- Research/discovery separated from implementation

See `references/decomposition-strategies.md` for detailed patterns.

### Anti-Patterns to Avoid

- **Over-decomposition**: Steps so small they lose context
- **Under-decomposition**: Steps with hidden complexity
- **Circular dependencies**: Step A needs B which needs A
- **Implicit ordering**: Dependencies not explicitly tracked

## Verification Framework

### Zero Error Verification Chain

**Every step must pass the full verification chain before being marked complete:**

```bash
tsc --noEmit       # 0 type errors
npm run lint       # 0 lint errors
npm run test:run   # 0 test failures
npm run build      # Build succeeds
```

**If any check fails:** Fix → Re-run all checks → Repeat until zero errors

### Auto-Verify Mode (Default)

| Stage | Check | Requirement |
|-------|-------|-------------|
| 1 | `tsc --noEmit` | 0 errors |
| 2 | `npm run lint` | 0 errors |
| 3 | `npm run test:run` | 0 failures |
| 4 | `npm run build` | Success |
| 5 | 5 Opus agents review | Unanimous approval (5/5) |

**Only when all 5 stages pass → VERIFIED**

### Manual Verification Mode

Use `"manual verification"` when automated checks aren't applicable:

```
## Step [ID]: [Description]

**Action taken:** [What was done]
**Result:** [Output/outcome]
**Side effects:** [Any changes made]
**Verification evidence:** [Command output showing zero errors]

Status: VERIFIED / UNCERTAIN / FAILED
```

### Verification Outcomes

| Status | Meaning | Action |
|--------|---------|--------|
| VERIFIED | Zero errors, all checks pass | Proceed to next step |
| UNCERTAIN | Cannot fully validate | Fix issues, re-verify |
| FAILED | Errors detected | Fix until zero errors |

**There is no "skip" option. Errors are fixed, never tolerated.**

### Verification Checklists by Domain

**Code implementation:**
- `tsc --noEmit` passes with 0 errors
- All tests pass (0 failures)
- Lint passes with 0 errors
- Build succeeds
- No regressions introduced

**Configuration/Setup:**
- Target state reached and verified
- Changes validated with tests
- No breaking changes to existing functionality

**Analysis/Data:**
- Inputs validated
- Results reproducible
- Sanity checks pass with evidence

See `references/verification-checklists.md` for complete checklists.

## Red-Flagging Criteria

### Automatic Detection

The framework flags responses exhibiting:

1. **Excessive length** - Response >3x expected length for step type
2. **Uncertainty language** - "might", "possibly", "I think", "not sure"
3. **Format violations** - Output doesn't match expected structure
4. **Scope creep** - Response addresses more than the specific step
5. **Missing outputs** - Expected artifacts not produced

Run detection:
```bash
python ~/.claude/skills/maker-framework/scripts/validation_utils.py check "<response_text>"
```

### User-Detected Flags

Flag when you observe:
- Result feels incomplete
- Something seems off but hard to articulate
- Step took much longer than expected
- Required unexpected workarounds

### Handling Flags

1. **Diagnose** - Identify root cause before attempting fix
2. **Fix** - Resolve the issue completely
3. **Decompose** - If fix is complex, break into smaller steps
4. **Re-verify** - Run full verification chain until zero errors
5. **Escalate** - Ask user only after exhausting fix attempts

**Never "document and proceed" with known errors. Fix them.**

## Progress Tracking

### Visualize Current State

```bash
python ~/.claude/skills/maker-framework/scripts/progress_visualizer.py tree <project_file>
```

Output:
```
[##########..........] 50% (15/30 steps)

Project: Migration Task
├── [x] Milestone 1: Setup
│   ├── [x] Step 1.1: Install dependencies
│   └── [x] Step 1.2: Configure environment
├── [>] Milestone 2: Implementation
│   ├── [x] Step 2.1: Create schema
│   ├── [>] Step 2.2: Implement handlers    ← CURRENT
│   └── [ ] Step 2.3: Add validation
└── [ ] Milestone 3: Testing
    └── ...

Red flags: 2 active
Success probability: 94.2%
```

### Calculate Success Probability

```bash
python ~/.claude/skills/maker-framework/scripts/success_calculator.py <total_steps> <completed> <failed>
```

See `references/formulas.md` for mathematical foundations.

### Persistence

Project state is stored in JSON files. Resume any project:
```bash
python ~/.claude/skills/maker-framework/scripts/maker_tracker.py status <project_file>
```

## Quick Reference

### Starting a New Project

1. Initialize: `maker_tracker.py init "Name" "Description"`
2. Decompose: Add all steps with `add-step`
3. Execute: Work through steps with verify loop
4. Track: Update status after each step

### Decision Matrix

| Situation | Action |
|-----------|--------|
| Step unclear | Decompose further |
| Verification fails | Fix → Re-verify → Loop until 0 errors |
| Red flag detected | Stop, diagnose, fix root cause |
| Multiple failures | Decompose smaller, use systematic-debugging |
| Step too large | Break down before executing |

**Core principle:** Errors are fixed, never skipped. There is no "good enough."

### Commands Summary

| Command | Purpose |
|---------|---------|
| `maker_tracker.py init` | Start new project |
| `maker_tracker.py add-step` | Add step to tree |
| `maker_tracker.py update` | Update step status |
| `maker_tracker.py flag` | Add red flag |
| `maker_tracker.py status` | Show project state |
| `progress_visualizer.py tree` | Visual tree display |
| `success_calculator.py` | Probability calculation |
| `validation_utils.py check` | Red flag detection |

### Templates

- `assets/decomposition_plan_template.md` - Project planning template
- `assets/step_verification_checklist.md` - Per-step validation
- `assets/progress_format.md` - Progress report format
