# Context Handoff Document

**Generated:** {{TIMESTAMP}}
**Session ID:** {{SESSION_ID}}
**Project:** {{PROJECT_NAME}}

---

## Original Task

<task>
{{ORIGINAL_TASK_DESCRIPTION}}
</task>

## Success Criteria

- [ ] {{CRITERION_1}}
- [ ] {{CRITERION_2}}
- [ ] {{CRITERION_3}}

---

## Work Completed

<completed>
### Files Modified
| File | Changes | Lines |
|------|---------|-------|
| {{FILE_1}} | {{CHANGE_DESCRIPTION_1}} | {{LINE_NUMBERS_1}} |
| {{FILE_2}} | {{CHANGE_DESCRIPTION_2}} | {{LINE_NUMBERS_2}} |

### Key Decisions Made
1. **{{DECISION_1}}**: {{REASONING_1}}
2. **{{DECISION_2}}**: {{REASONING_2}}

### Tests/Verification Completed
- {{VERIFICATION_1}}: {{RESULT_1}}
- {{VERIFICATION_2}}: {{RESULT_2}}
</completed>

---

## Work Remaining

<remaining>
### Next Steps (in order)
1. {{NEXT_STEP_1}}
2. {{NEXT_STEP_2}}
3. {{NEXT_STEP_3}}

### Blocked Items
- {{BLOCKED_ITEM}}: {{BLOCKER_REASON}}

### Known TODOs
- [ ] {{TODO_1}}
- [ ] {{TODO_2}}
</remaining>

---

## Attempted Approaches

<attempts>
### What Didn't Work
| Approach | Why It Failed | Learning |
|----------|---------------|----------|
| {{APPROACH_1}} | {{FAILURE_REASON_1}} | {{LEARNING_1}} |
| {{APPROACH_2}} | {{FAILURE_REASON_2}} | {{LEARNING_2}} |

### Dead Ends to Avoid
- {{DEAD_END_1}}
- {{DEAD_END_2}}
</attempts>

---

## Critical Context

<context>
### Environment Details
- Node version: {{NODE_VERSION}}
- Key dependencies: {{DEPENDENCIES}}
- Environment: {{ENVIRONMENT}}

### External References Consulted
- {{REFERENCE_1}}: {{INSIGHT_1}}
- {{REFERENCE_2}}: {{INSIGHT_2}}

### Important Discoveries
- {{DISCOVERY_1}}
- {{DISCOVERY_2}}
</context>

---

## Current State

<state>
### Git Status
```
{{GIT_STATUS}}
```

### Uncommitted Changes
{{UNCOMMITTED_CHANGES_SUMMARY}}

### Test Status
- Passing: {{PASSING_COUNT}}
- Failing: {{FAILING_COUNT}}
- Skipped: {{SKIPPED_COUNT}}
</state>

---

## Resume Instructions

To continue this work:

1. Read this handoff document fully
2. Review files in "Work Completed" section
3. Start with first item in "Next Steps"
4. Avoid approaches listed in "What Didn't Work"
5. Reference "Critical Context" for environment details

**Focus only on completing the original task. Do not add scope.**

---

## Template Usage Instructions (delete when using)

### When to Generate This Document
- Context usage reaches ~10% remaining
- Before ending a long session
- When work must continue later
- When handing off to another agent

### Key Principles
1. **Prevent wasted effort**: Document failures so they aren't repeated
2. **Preserve decisions**: Capture reasoning, not just actions
3. **Maintain scope**: Focus on original task, don't add features
4. **Enable continuation**: Another agent should resume seamlessly

### XML Sections Explained
- `<task>`: Original request, unchanged
- `<completed>`: What's done (with evidence)
- `<remaining>`: What's left (prioritized)
- `<attempts>`: What didn't work (prevent repeats)
- `<context>`: Environment and discoveries
- `<state>`: Current git/test status

### File Location
Save to: `{{project}}/.claude/CONTEXT_HANDOFF.md`
Or reference via: `@context-handoff.md`
