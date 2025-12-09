# Context Engineering

The systematic approach to providing AI agents with the right information at the right time.

## The Three Context Types

### 1. Static Context (Always Loaded)

**What:** Information loaded at the start of every conversation
**Where:** CLAUDE.md files (global and project-level)
**When:** Every interaction

**Best for:**
- Core principles (how to think)
- Persistent standards (coding style, error handling)
- Model preferences
- Communication guidelines

**Examples:**
- "Zero Error Standard: 0 type errors, 0 lint errors..."
- "Performance = Correctness² × Completeness / Size"
- "Use claude-opus-4-5-20251101 for all tasks"

**Guidelines:**
- Every line must earn its place (high leverage)
- Teach principles, not procedures
- Keep concise (token cost matters)
- Global CLAUDE.md: ~65 lines max
- Project CLAUDE.md: project-specific additions only

### 2. Dynamic Context (Loaded on Demand)

**What:** Information loaded when triggered by keywords or explicit invocation
**Where:** Skills, plugins, expertise files
**When:** When relevant to current task

**Best for:**
- Domain expertise (testing, security, UI design)
- Complex procedures (multi-step workflows)
- Specialized knowledge (framework-specific patterns)
- Reference material (detailed documentation)

**Examples:**
- `SecurityAudit` skill loaded when "security" mentioned
- `MAKER` framework loaded for complex decomposition
- Framework-specific expertise from `~/.claude/skills/expertise/`

**Guidelines:**
- Progressive disclosure (overview first, details on demand)
- Clear triggers (natural language phrases)
- Distinct purpose (no overlapping skills)
- Link to references, don't duplicate

### 3. Procedural Context (Event-Driven)

**What:** Information injected automatically based on system events
**Where:** Hooks (Python scripts in ~/.claude/hooks/)
**When:** Specific lifecycle events trigger execution

**Best for:**
- Session initialization (loading memories, primers)
- Validation/blocking (preventing unsafe actions)
- Data transformation (enriching inputs/outputs)
- State management (tracking across sessions)

**Hook Events:**
| Event | When Triggered | Use Case |
|-------|----------------|----------|
| SessionStart | Session begins | Load memories, set context |
| UserPromptSubmit | User sends message | Inject relevant context |
| PreToolUse | Before tool executes | Validate, block if needed |
| PostToolUse | After tool completes | Transform output |
| SessionEnd | Session ends | Save state, generate handoff |
| PreCompact | Before summarization | Preserve critical info |

**Guidelines:**
- Never crash (graceful failure)
- Fast execution (< 5 seconds)
- Standard library only
- JSON stdin/stdout

## Progressive Disclosure Pattern

Load context on a need-to-know basis to optimize the performance formula.

```
Level 1: Quick Reference (always visible)
    ↓ triggers loading
Level 2: Detailed Procedures (when needed)
    ↓ links to
Level 3: Deep References (for edge cases)
```

### Example: Skill Structure

```
SKILL.md (Level 1)
├── Quick reference tables
├── Process overview
├── Triggers for detail
    ↓
references/ (Level 2)
├── skill-patterns.md
├── decision-trees.md
    ↓
External docs (Level 3)
├── Official documentation
├── API references
```

### Benefits
- **Reduced token cost**: Only load what's needed
- **Maintained completeness**: Deep info still accessible
- **Improved correctness**: Less noise = better signal

## Context Size Management

### The 10% Rule

Trigger context handoff when context usage reaches ~10% remaining.

**Why 10%?**
- Leaves room for continuation instructions
- Prevents abrupt context loss
- Enables graceful transitions

### Handoff Process

1. Detect context reaching limit
2. Generate handoff document (see templates/context-handoff.md)
3. Preserve: task, completed work, remaining work, failures, state
4. New session reads handoff to continue

### Compression Techniques

| Technique | When to Use |
|-----------|-------------|
| Summarization | Long outputs that need brief reference |
| Delta updates | Incremental changes (ACE framework) |
| External storage | Large datasets, logs |
| Git as memory | Commit history preserves state |

## Context Quality Checklist

Before loading context, verify:

- [ ] **Correctness**: Is this information accurate?
- [ ] **Relevance**: Is this needed for current task?
- [ ] **Freshness**: Is this up-to-date?
- [ ] **Uniqueness**: Is this duplicated elsewhere?
- [ ] **Conciseness**: Is this as brief as possible?

## Common Mistakes

### 1. Context Overload
❌ Loading everything "just in case"
✅ Progressive disclosure, load on demand

### 2. Static for Dynamic
❌ Putting procedures in CLAUDE.md
✅ CLAUDE.md for principles, skills for procedures

### 3. Missing Triggers
❌ Skills that never get loaded
✅ Clear, natural language trigger phrases

### 4. No Handoff Strategy
❌ Losing context mid-task
✅ Handoff at 10% remaining

## Integration Example

```
User: "Review security of the authentication system"

Context Loading:
1. Static: CLAUDE.md loads (zero error standard, model prefs)
2. Dynamic: "security" triggers SecurityAudit skill
3. Dynamic: "authentication" triggers AuthSystem expertise
4. Procedural: UserPromptSubmit hook injects relevant memories
```

All three types work together to provide optimal context for the task.
