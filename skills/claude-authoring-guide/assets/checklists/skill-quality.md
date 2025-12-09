# Skill Quality Checklist

Use this checklist before publishing a new skill.

## Structure

- [ ] YAML frontmatter complete
  - [ ] `name` (kebab-case)
  - [ ] `description` (one line)
  - [ ] `license` (usually MIT)
  - [ ] `model` (claude-opus-4-5-20251101)
- [ ] Triggers section with 3-5 clear phrases
- [ ] Quick reference table present
- [ ] Process broken into phases (1-3 phases max)
- [ ] Verification section with test commands

## Content Quality

- [ ] **Distinct purpose** - Not overlapping with existing skills
- [ ] **Tables over prose** - Use tables where data is structured
- [ ] **No placeholder text** - All {{PLACEHOLDERS}} replaced
- [ ] **Examples provided** - For complex operations
- [ ] **Progressive disclosure** - Deep details in references, not main file

## Performance Formula Check

| Criterion | Question | Pass? |
|-----------|----------|-------|
| Correctness | Are instructions accurate and tested? | [ ] |
| Completeness | Are edge cases covered? | [ ] |
| Size | Is verbosity minimized? (token cost) | [ ] |

## Integration

- [ ] Related skills referenced
- [ ] No conflicting triggers with existing skills
- [ ] Works with SkillComposer orchestration
- [ ] Added to skill registry (if applicable)

## Testing

- [ ] Manually tested happy path
- [ ] Tested with edge cases
- [ ] Verified in isolation
- [ ] Verified in composed workflows

## Documentation

- [ ] Brief description explains "what" and "why"
- [ ] Triggers are natural language phrases users would say
- [ ] Verification commands actually work
- [ ] Reference docs linked (not duplicated)

## Final Verification

```bash
# Run skill validator
python ~/.claude/skills/claude-authoring-guide/scripts/validate_skill.py path/to/skill
```

## Post-Publish

- [ ] Added to `~/.claude/CLAUDE.md` skill registry (if user-facing)
- [ ] Documented in IMPROVEMENT_BACKLOG.md (status: complete)
- [ ] Tested by invoking trigger phrase
