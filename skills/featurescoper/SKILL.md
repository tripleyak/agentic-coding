# FeatureScoper Skill

Before building, helps think through scope, edge cases, and phases. Prevents overbuilding and scope creep.

**Triggers:** `scope this`, `plan feature`, `before I build`, `help me think through`, `what should I consider`

**Domain:** Planning / Architecture

## Process

| Phase | Action |
|-------|--------|
| 1. Clarify | Understand the core request |
| 2. Expand | Surface edge cases and considerations |
| 3. Scope | Define in/out of scope |
| 4. Phase | Break into buildable chunks |
| 5. Document | Create scope document |

## Scoping Questions

### Core Understanding
| Question | Purpose |
|----------|---------|
| What problem does this solve? | Validate need |
| Who uses this feature? | Identify user type |
| What does success look like? | Define acceptance criteria |
| What's the simplest version? | Find MVP |

### Edge Cases
| Category | Questions |
|----------|-----------|
| Errors | What if it fails? Empty states? |
| Scale | What if 1000x users? 1000x data? |
| Security | Who can access? Data exposure? |
| Mobile | Does it need to work on mobile? |
| Offline | What happens without network? |

### Dependencies
| Question | Purpose |
|----------|---------|
| What existing code does this touch? | Impact assessment |
| Does this need new packages? | Dependency check |
| Does this need backend changes? | Full-stack awareness |
| Does this affect other features? | Side effect check |

## Output Format

```markdown
# Feature Scope: [Name]

## Problem Statement
[1-2 sentences describing the problem]

## User Story
As a [user type], I want to [action] so that [benefit].

## Success Criteria
- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]
- [ ] [Measurable criterion 3]

## Scope

### In Scope (MVP)
- [Feature 1]
- [Feature 2]
- [Feature 3]

### Out of Scope (Future)
- [Deferred feature 1]
- [Deferred feature 2]

### Explicitly Not Doing
- [Anti-feature 1] - because [reason]

## Edge Cases to Handle
| Case | Handling |
|------|----------|
| Empty state | Show placeholder |
| Error | Show error message + retry |
| Loading | Show skeleton |

## Phases

### Phase 1: MVP
- [Task 1]
- [Task 2]
**Deliverable:** [What user can do]

### Phase 2: Enhancement
- [Task 3]
- [Task 4]
**Deliverable:** [Additional capability]

## Dependencies
- [Package/service needed]
- [Existing code to modify]

## Risks
| Risk | Mitigation |
|------|------------|
| [Risk 1] | [Mitigation] |

## Time Estimate
- Phase 1: [estimate]
- Phase 2: [estimate]
```

## Anti-Patterns to Flag

| Pattern | Problem | Instead |
|---------|---------|---------|
| "And also..." | Scope creep | Defer to Phase 2 |
| "Just in case..." | Overbuilding | YAGNI - build when needed |
| "It should handle everything" | No focus | Define explicit boundaries |
| No error handling plan | Fragile | Plan error states upfront |
| No success criteria | Unclear done | Define measurable outcomes |

## Integration

| With Skill | Purpose |
|------------|---------|
| MAKER | Feed scope into decomposition |
| ArchitectPlan | For complex architectural decisions |
| CostEstimator | Estimate costs for scoped features |
| superpowers:brainstorming | Explore ideas before scoping |
