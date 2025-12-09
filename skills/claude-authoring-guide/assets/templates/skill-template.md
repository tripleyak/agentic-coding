---
name: {{SKILL_NAME}}
description: {{ONE_LINE_DESCRIPTION}}
license: MIT
model: claude-opus-4-5-20251101
---

# {{SKILL_TITLE}}

{{BRIEF_DESCRIPTION}}

## Triggers

- `{{TRIGGER_1}}`
- `{{TRIGGER_2}}`
- `{{TRIGGER_3}}`

## Quick Reference

| Input | Output | Complexity |
|-------|--------|------------|
| {{INPUT_TYPE}} | {{OUTPUT_TYPE}} | Simple / Medium / Complex |

## Process

### Phase 1: {{PHASE_NAME}}

1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

### Phase 2: {{PHASE_NAME}} (if needed)

1. {{STEP_1}}
2. {{STEP_2}}

## Verification

| Check | Command | Expected |
|-------|---------|----------|
| {{CHECK_NAME}} | `{{COMMAND}}` | {{EXPECTED_RESULT}} |

## Related Skills

- {{RELATED_SKILL_1}}
- {{RELATED_SKILL_2}}

---

## Template Usage Instructions (delete after customizing)

### Required Placeholders
- `{{SKILL_NAME}}` - kebab-case identifier (e.g., `my-skill`)
- `{{SKILL_TITLE}}` - Human-readable title (e.g., `My Skill`)
- `{{ONE_LINE_DESCRIPTION}}` - Brief description for frontmatter
- `{{BRIEF_DESCRIPTION}}` - 1-2 sentence overview

### Triggers
Define 3-5 natural language phrases that invoke this skill.
Examples: "analyze performance", "review security", "generate tests"

### Process Phases
- Most skills need 1-2 phases
- Each phase should have 3-5 concrete steps
- Keep steps atomic and verifiable

### Quality Checklist
Before publishing, verify:
- [ ] Distinct purpose (not overlapping with existing skills)
- [ ] Tables over prose where applicable
- [ ] No placeholder text remaining
- [ ] Verification commands included
