# ACE Framework: Agentic Context Engineering

A framework for self-improving AI systems through structured knowledge management.

## Overview

The ACE (Agentic Context Engineering) framework, from Stanford/SambaNova research, provides a pattern for AI systems to learn and improve over time through structured reflection and knowledge curation.

## The Three Roles

### 1. Generator

**Purpose:** Execute tasks and produce output

**Responsibilities:**
- Perform requested work
- Generate code, analysis, or content
- Apply existing knowledge to new problems

**Characteristics:**
- Action-oriented
- Uses available context
- Produces concrete deliverables

### 2. Reflector

**Purpose:** Analyze successes and failures

**Responsibilities:**
- Examine what worked and why
- Identify patterns in failures
- Extract learnings from execution

**Key Questions:**
- What went well?
- What could have gone better?
- What patterns emerged?
- What assumptions were wrong?

**Output:**
- Insights about effective approaches
- Failure patterns to avoid
- Suggestions for knowledge updates

### 3. Curator

**Purpose:** Update procedural knowledge

**Responsibilities:**
- Integrate reflections into knowledge base
- Maintain consistency across documentation
- Prune outdated information

**Key Innovation: Delta Updates**

Instead of regenerating entire context:
```
Old approach: Regenerate all → Risk context collapse
New approach: Apply deltas → Preserve accumulated knowledge
```

**Benefits:**
- Prevents catastrophic forgetting
- Incremental improvements
- Maintains institutional memory

## The ACE Cycle

```
                    ┌─────────────┐
                    │  GENERATE   │
                    │   (Execute) │
                    └──────┬──────┘
                           │
                           ▼
    ┌─────────────────────────────────────────┐
    │              Task Execution              │
    │  • Apply knowledge                       │
    │  • Produce output                        │
    │  • Track what worked/didn't              │
    └──────────────────────┬──────────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   REFLECT   │
                    │  (Analyze)  │
                    └──────┬──────┘
                           │
                           ▼
    ┌─────────────────────────────────────────┐
    │              Analysis Phase              │
    │  • What succeeded?                       │
    │  • What failed?                          │
    │  • What patterns emerged?                │
    └──────────────────────┬──────────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   CURATE    │
                    │  (Update)   │
                    └──────┬──────┘
                           │
                           ▼
    ┌─────────────────────────────────────────┐
    │            Knowledge Update              │
    │  • Apply delta changes                   │
    │  • Preserve existing knowledge           │
    │  • Remove outdated info                  │
    └──────────────────────┬──────────────────┘
                           │
                           └──────► Next Cycle
```

## Delta Updates Explained

### The Problem: Context Collapse

When AI systems summarize too aggressively:
```
Rich context → Summarize → Lossy summary → Summarize → Critical loss
```

Accumulated knowledge gets compressed into oblivion.

### The Solution: Delta Updates

Instead of wholesale replacement:
```
Original: "Use npm install"
Delta: "Add: Use --legacy-peer-deps flag for React 18+"
Result: "Use npm install (add --legacy-peer-deps for React 18+)"
```

### Delta Types

| Type | Description | Example |
|------|-------------|---------|
| Addition | New knowledge | "Also check for circular imports" |
| Modification | Updated knowledge | "v2 API replaces deprecated v1" |
| Deprecation | Mark as outdated | "No longer needed after v3.0" |
| Deletion | Remove incorrect | "Remove: false claim about X" |

## Implementing ACE

### In Skills

```markdown
## After Task Completion

### Reflection
- What approach worked?
- What didn't work and why?
- What would do differently?

### Curation Candidates
- [ ] New pattern to document
- [ ] Existing doc to update
- [ ] Outdated info to remove
```

### In Sessions

**End-of-session hooks** can trigger reflection:
```python
# memory_curate.py
def curate_session():
    """Extract learnings from session and update knowledge base."""
    # Analyze session for patterns
    # Generate delta updates
    # Apply to skill/documentation
```

### In Project Memory

```
SESSION_REFLECTION.md:
- Task: Implemented OAuth flow
- Success: Token refresh worked first try
- Failure: CORS issues required 3 attempts
- Learning: Always configure CORS before testing auth
- Delta: Add CORS step to AuthSystem skill
```

## Practical Application

### For Skill Authors

After using a skill several times:

1. **Reflect**: What worked? What didn't?
2. **Identify patterns**: Common issues, successful approaches
3. **Curate**: Update skill with delta (add, modify, deprecate)

### For Session Management

At session boundaries:

1. **Generate handoff**: What was accomplished?
2. **Reflect**: What could improve?
3. **Curate memories**: Update persistent knowledge

### For CLAUDE.md

When updating global instructions:

1. **Review performance**: Are instructions working?
2. **Reflect**: What's causing issues?
3. **Apply delta**: Surgical changes, not rewrites

## Key Principles

1. **Preserve accumulated knowledge** - Never summarize away hard-won learnings
2. **Delta over replace** - Small targeted changes beat wholesale rewrites
3. **Separate roles** - Generation, reflection, and curation are distinct phases
4. **Continuous improvement** - Every execution is a learning opportunity
5. **Track what didn't work** - Failures are as valuable as successes

## Anti-Patterns

### Over-Summarization
❌ Compressing session to 3 sentences
✅ Preserving key learnings and failures

### Ignoring Failures
❌ Only documenting successes
✅ Recording what didn't work and why

### Wholesale Replacement
❌ Rewriting entire skill after one issue
✅ Applying targeted delta update

### No Reflection Phase
❌ Task → Next Task
✅ Task → Reflect → Curate → Next Task
