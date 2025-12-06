# Step Verification Checklist

## Step Information

**Step ID:** [ID from tracker]

**Description:** [What this step does]

**Step Type:** [ ] Code [ ] Config [ ] Analysis [ ] Documentation [ ] Command [ ] Other

---

## Pre-Execution Checks

Before starting this step:

- [ ] Step description is clear and unambiguous
- [ ] Step is atomic (single focused action)
- [ ] All dependencies are complete and verified
- [ ] Required inputs/resources are available
- [ ] Expected output format is defined

**Issues found:** [None / List issues]

---

## Execution Record

**Action taken:**
[Describe what was actually done]

**Output/Result:**
```
[Paste or describe the output]
```

**Side effects:**
[Any changes made beyond the direct output - files modified, state changed, etc.]

**Time taken:** [Duration]

---

## Post-Execution Verification

### Universal Checks

- [ ] Output matches what was requested
- [ ] Output is complete (nothing missing)
- [ ] No unexpected side effects
- [ ] No error messages or warnings

### Type-Specific Checks

**For Code:**
- [ ] Compiles/parses without errors
- [ ] Tests pass (if applicable)
- [ ] Follows existing code style
- [ ] Edge cases handled

**For Configuration:**
- [ ] All required fields present
- [ ] Values are valid types
- [ ] Works in target environment
- [ ] Secrets protected

**For Analysis:**
- [ ] Methodology is sound
- [ ] Results are reproducible
- [ ] Sanity checks pass

**For Documentation:**
- [ ] Accurate to implementation
- [ ] Clear and complete
- [ ] Examples work

**For Commands:**
- [ ] Command completed successfully
- [ ] Expected state achieved
- [ ] Safe to run again (idempotent)

---

## Red Flag Detection

Check for these warning signs:

- [ ] Response unusually long (>3x expected)
- [ ] Contains uncertainty language ("might", "possibly", "I think")
- [ ] Scope expanded beyond original step
- [ ] Format doesn't match expectations
- [ ] Required workarounds or deviations

**Red flags detected:** [None / List flags]

---

## Verification Decision

**Status:**
- [ ] VERIFIED - Output is correct, proceed
- [ ] UNCERTAIN - Cannot fully validate, need clarification
- [ ] FAILED - Output is wrong, must retry

**Notes:**
[Explain your decision, especially if UNCERTAIN or FAILED]

---

## If UNCERTAIN or FAILED

**What's unclear/wrong:**
[Specific issue]

**Recommended action:**
- [ ] Retry with same approach
- [ ] Retry with different approach
- [ ] Decompose into smaller steps
- [ ] Escalate for guidance

**Next step:**
[What to do next]

---

## Tracker Update Command

```bash
# If VERIFIED:
python ~/.claude/skills/maker-framework/scripts/maker_tracker.py update [STEP_ID] --status verified --project [PROJECT_FILE]

# If FAILED:
python ~/.claude/skills/maker-framework/scripts/maker_tracker.py update [STEP_ID] --status failed --notes "[Reason]" --project [PROJECT_FILE]

# If flagged:
python ~/.claude/skills/maker-framework/scripts/maker_tracker.py flag [STEP_ID] "[Red flag description]" --project [PROJECT_FILE]
```
