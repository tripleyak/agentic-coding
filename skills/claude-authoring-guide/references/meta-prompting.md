# Meta-Prompting: Separating Analysis from Execution

A pattern for improving AI output quality by separating the planning phase from the execution phase.

## Core Principle

> "PLAN.md IS the prompt."

Instead of asking Claude to analyze AND implement in one step, separate concerns:

1. **Analysis Phase**: Analyze, clarify, and generate a specification
2. **Execution Phase**: Execute the specification in a fresh context

## Why Meta-Prompting Works

### The Problem

```
Traditional approach:
User request → Claude analyzes + implements → Mixed quality output

Issues:
- Analysis pollutes execution context
- Vague requirements lead to vague implementations
- Iteration happens at the wrong level
```

### The Solution

```
Meta-prompting approach:
User request → Analysis Agent generates spec → Execution Agent implements spec

Benefits:
- Clean execution context (no analysis noise)
- Specification can be reviewed/refined
- Implementation gets pristine instructions
```

## The Two Phases

### Phase 1: Analysis (Generate the Prompt)

**Goal:** Produce a rigorous, specification-grade prompt

**Steps:**
1. Ask clarifying questions
2. Analyze the codebase
3. Identify constraints and dependencies
4. Define success criteria
5. Generate structured specification

**Output:** A detailed prompt/spec that another agent can execute

**Key Elements in Generated Spec:**
- XML organization for semantic clarity
- Explicit "why" statements
- Measurable success criteria
- Verification protocol
- "What to avoid and WHY" sections
- Trade-off analysis if applicable

### Phase 2: Execution (Run the Prompt)

**Goal:** Implement the specification

**Context:** Fresh session, no analysis noise

**Input:** The specification from Phase 1

**Advantages:**
- Clean context window
- Focused on implementation
- Clear success criteria to verify against

## When to Use Meta-Prompting

### Use For

| Task Type | Why Meta-Prompting Helps |
|-----------|--------------------------|
| Complex refactoring | Need to understand impact before changing |
| Architectural decisions | Multiple valid approaches need analysis |
| Migrations | Many moving parts, high risk |
| Optimization | Need to profile and analyze first |
| Multi-step tasks | Coordination across many files |

### Skip For

| Task Type | Why Direct Execution Is Fine |
|-----------|------------------------------|
| Simple edits | Low complexity, quick fix |
| Single-file tweaks | Contained impact |
| Straightforward additions | Clear requirements |
| Quick experiments | Iteration is expected |

## Implementation Patterns

### Pattern 1: Plan Mode

```
1. Request enters plan mode
2. Claude analyzes codebase, asks questions
3. Claude generates PLAN.md
4. User reviews and approves
5. Claude executes plan in fresh context
```

### Pattern 2: Staged Prompts

```
Stage 1: "Analyze this task and generate a detailed specification"
         → Output: SPEC.md

Stage 2: "Execute this specification exactly: @SPEC.md"
         → Output: Implementation
```

### Pattern 3: Two-Agent Pipeline

```
Analysis Agent                Execution Agent
     │                              │
     ├─ Analyze request             │
     ├─ Ask clarifying questions    │
     ├─ Generate spec ──────────────┼─► Receive spec
     │                              ├─ Execute spec
     │                              ├─ Verify against criteria
     │                              └─ Report completion
```

## Specification Structure

A well-formed meta-prompt specification includes:

```markdown
# Task Specification

## Context
<context>
- What system/component is affected
- Current state and behavior
- Relevant file paths
</context>

## Requirements
<requirements>
- What must be accomplished
- Success criteria (measurable)
- Constraints and boundaries
</requirements>

## Approach
<approach>
- Recommended implementation strategy
- Step-by-step plan
- Dependencies and ordering
</approach>

## Avoid
<avoid>
- Common pitfalls and WHY they're problems
- Anti-patterns to skip
- Known dead ends
</avoid>

## Verification
<verification>
- How to verify success
- Test commands to run
- Expected outcomes
</verification>
```

## Key Insights

### Context Quality > Context Quantity

> "With sufficient token budgets, what matters is context quality."

Separating analysis from execution improves context quality in both phases:
- Analysis phase: Free to explore and question
- Execution phase: Focused, specification-driven

### The 20+ Iteration Problem

Without meta-prompting:
```
Vague prompt → Mediocre result → Iterate → Still mediocre → 20+ iterations
```

With meta-prompting:
```
Analysis → Clear spec → Clean execution → Good result → 1-2 iterations
```

### Investment in Specification

Time spent on specification pays dividends:
- Clearer requirements = fewer implementation errors
- Explicit success criteria = easier verification
- "What to avoid" = prevents common mistakes

## Execution Flexibility

Generated prompts can be executed:

| Mode | When to Use |
|------|-------------|
| Sequential | Dependent tasks, order matters |
| Parallel | Independent tasks, optimize time |
| Hybrid | Mix based on dependency analysis |

The specification should note dependencies so execution can be optimized.

## Integration with Other Patterns

### With Three-Phase Workflow

```
Research → [Meta-Prompting] → Implement
           ↓
    Analysis + Plan = Spec
```

### With Context Handoff

If analysis consumes significant context:
```
Analysis (Phase 1) → Handoff → Execution (Phase 2, fresh context)
```

### With Skill Composition

```
Meta-prompt skill → Generates spec → SkillComposer executes spec
```

## Best Practices

1. **Be explicit about WHY** - Not just what to do, but why
2. **Include failure modes** - What could go wrong and how to avoid
3. **Define success clearly** - Measurable criteria, not vague goals
4. **Use XML structure** - Semantic organization aids parsing
5. **Review before execution** - Human checkpoint on specification
6. **Fresh context for execution** - Don't pollute with analysis artifacts
