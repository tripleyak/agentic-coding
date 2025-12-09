# Hierarchy of Leverage

Understanding where errors have the most impact on AI agent performance.

## The Core Insight

Not all work is created equal. An error's impact is determined by where it occurs in the development pipeline. Early errors compound exponentially.

## Error Multiplier Table

| Level | Example | Error Impact |
|-------|---------|--------------|
| **CLAUDE.md** | Flawed core instructions | 1 bad line = 100,000+ bad lines of code |
| **Specification** | Solving wrong problem | 1 bad line = 10,000+ bad lines of code |
| **Research** | Misunderstanding system | 1 bad line = 1,000+ bad lines of code |
| **Plan** | Wrong solution approach | 1 bad line = 10-100 bad lines of code |
| **Code** | Implementation bug | 1 bad line = 1 bad line of code |

## Why This Matters

### Exponential Compounding

```
CLAUDE.md error
    → Affects every conversation
        → Shapes every plan
            → Influences every implementation
                → Multiplies across entire codebase
```

A single incorrect instruction in CLAUDE.md gets applied thousands of times.

### The Performance Formula

```
Performance = (Correctness² × Completeness) / Size
```

**Correctness has squared impact.** A small amount of wrong information is far more damaging than:
- Missing information
- Excessive context
- Incomplete coverage

## Practical Implications

### 1. Invest Time Where It Matters

| Level | Time Investment | Return |
|-------|-----------------|--------|
| CLAUDE.md | High | Highest |
| Specification | High | Very High |
| Research | Medium-High | High |
| Planning | Medium | Medium |
| Coding | Low-Medium | Low |

Spending extra time on CLAUDE.md pays dividends across all future work.

### 2. Review Hierarchy

Review process should match leverage:

- **CLAUDE.md changes**: Careful review, test across scenarios
- **Specification changes**: Stakeholder validation
- **Research**: Verify claims, check blind spots
- **Plans**: Validate approach before implementing
- **Code**: Standard code review

### 3. Error Recovery Strategy

| Level | When Wrong | Fix Strategy |
|-------|------------|--------------|
| CLAUDE.md | Everything feels off | Stop, audit, fix root cause |
| Spec | Solving wrong problem | Restart with correct understanding |
| Research | Implementation keeps failing | Re-research, verify claims |
| Plan | Many bugs in implementation | Revise plan before continuing |
| Code | Single bug | Fix the bug |

## Applying to Your Work

### Before Editing CLAUDE.md

Ask:
1. What's the blast radius of this change?
2. Have I tested this instruction in multiple contexts?
3. Am I teaching a principle or a procedure?
4. Does this conflict with any existing instructions?

### Before Starting a Task

Check leverage levels in order:
1. **Specification**: Do I understand what's being asked?
2. **Research**: Do I understand the system?
3. **Plan**: Do I have a sound approach?
4. **Implementation**: Am I ready to code?

Don't start lower-leverage work until higher levels are solid.

## Anti-Patterns

### Rushing to Code
❌ Immediately writing code without understanding system
✅ Research first, plan second, implement third

### Treating CLAUDE.md Like Code
❌ Quick edits without considering impact
✅ Careful changes with full testing

### Ignoring Spec Errors
❌ Building wrong thing faster
✅ Stopping to clarify requirements

## Key Takeaways

1. **Errors multiply down the hierarchy** - Fix problems at the highest level possible
2. **CLAUDE.md is the highest leverage** - Every line shapes all future work
3. **Correctness beats completeness** - Wrong information is worse than missing information
4. **Invest review time proportionally** - More scrutiny at higher leverage levels
5. **Three-phase workflow exists for a reason** - Research → Plan → Implement prevents costly errors
