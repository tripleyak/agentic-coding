# Agent Quality Checklist

Use this checklist before deploying a new agent or agent template.

## Structure

- [ ] YAML frontmatter complete
  - [ ] `name` (kebab-case)
  - [ ] `description` (one line)
  - [ ] `tools` (list of required tools)
  - [ ] `skills` (list of skills to load)
  - [ ] `model` (opus/sonnet/haiku)
- [ ] Clear goal statement
- [ ] Problem statement with bullets
- [ ] Expected deliverables listed
- [ ] Four-phase approach (Discovery → Analysis → Implementation → Verification)

## Content Quality

- [ ] **Clear specialization** - Agent has defined expertise
- [ ] **Specific search terms** - Not generic keywords
- [ ] **Concrete deliverables** - Measurable outcomes
- [ ] **No placeholder text** - All {{PLACEHOLDERS}} replaced
- [ ] **Reference patterns** - Points to existing code to follow

## Agent Pattern Verification

| Pattern | Use Case | Key Requirements |
|---------|----------|------------------|
| Feature Enhancer | Add capabilities | [ ] Component identified, [ ] Integration points |
| Flow Fixer | Fix workflows | [ ] Failure scenario, [ ] Expected behavior |
| State Connector | Fix reactivity | [ ] State sources, [ ] UI components |
| Wizard Builder | Multi-step flows | [ ] Steps defined, [ ] Navigation logic |
| Test Writer | Add coverage | [ ] Test scope, [ ] Assertions defined |

- [ ] Correct pattern selected for use case
- [ ] Pattern-specific requirements met

## Scope Management

- [ ] Single clear objective
- [ ] Boundaries defined (what's NOT in scope)
- [ ] Deliverables are achievable in one session
- [ ] No scope creep indicators

## Discovery Phase

- [ ] Search terms specific and relevant
- [ ] Target files/directories identified
- [ ] Related patterns referenced

## Verification Phase

- [ ] Success criteria defined
- [ ] Verification commands specified
- [ ] Rollback plan if needed

## Output Requirements

- [ ] Summary format specified
- [ ] File modifications tracked
- [ ] Evidence of completion required
- [ ] Next steps section included

## Testing

- [ ] Tested with real codebase
- [ ] Tested edge cases
- [ ] Verified output format
- [ ] Confirmed deliverables achieved

## File Location

For reusable templates:
- [ ] Saved to `~/.claude/agent-templates/{{name}}.md`

For project-specific agents:
- [ ] Saved to `.claude/agents/{{name}}.md`

## Template Instructions

If this is a template:
- [ ] Usage instructions at bottom
- [ ] All placeholders documented
- [ ] Instructions marked for deletion
