# Skill Architecture Patterns

Common patterns for structuring skills based on their purpose and complexity.

## Pattern Overview

| Pattern | Complexity | Use When |
|---------|------------|----------|
| Single-Phase Executor | Low | Simple, linear tasks |
| Checklist Validator | Low | Quality assurance, audits |
| Generator with Templates | Medium | Creating artifacts |
| Multi-Phase Sequential | Medium | Complex ordered workflows |
| Multi-Agent Parallel | High | Independent concurrent tasks |
| Composite Orchestrator | High | Coordinating multiple skills |

---

## Pattern 1: Single-Phase Executor

### When to Use
- Task is straightforward and linear
- No branching logic needed
- Output format is predictable

### Structure
```markdown
## Process

1. Gather inputs
2. Execute operation
3. Produce output
4. Verify result
```

### Example Skills
- ErrorExplainer: Parse → Explain → Suggest
- CodeReview: Read → Analyze → Report

### Template
```markdown
# {{SkillName}}

## Triggers
- `{{trigger phrase}}`

## Process

### Step 1: {{Input}}
{{description}}

### Step 2: {{Execute}}
{{description}}

### Step 3: {{Output}}
{{description}}

## Verification
{{how to verify success}}
```

---

## Pattern 2: Checklist Validator

### When to Use
- Quality assurance tasks
- Compliance verification
- Audit workflows

### Structure
```markdown
## Checklist

- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

## Verification
All items must pass
```

### Example Skills
- SecurityAudit: Check OWASP top 10
- A11yAudit: Check WCAG compliance
- skill-quality checklist

### Template
```markdown
# {{SkillName}}

## Triggers
- `{{trigger phrase}}`

## Checklist

### Category 1
- [ ] {{Check 1}}
- [ ] {{Check 2}}

### Category 2
- [ ] {{Check 3}}
- [ ] {{Check 4}}

## Actions
| Check Failed | Remediation |
|--------------|-------------|
| {{Check 1}} | {{Fix}} |

## Report Format
{{output structure}}
```

---

## Pattern 3: Generator with Templates

### When to Use
- Creating new artifacts (files, docs, configs)
- Output follows consistent structure
- Customization through placeholders

### Structure
```markdown
## Templates Available
- Template A
- Template B

## Generation Process
1. Select template
2. Gather variables
3. Generate output
4. Validate structure
```

### Example Skills
- SkillCreator: Generate new skill files
- DocGen: Generate documentation

### Template
```markdown
# {{SkillName}}

## Triggers
- `{{trigger phrase}}`

## Available Templates

| Template | Use Case |
|----------|----------|
| {{Template1}} | {{UseCase1}} |
| {{Template2}} | {{UseCase2}} |

## Process

### 1. Template Selection
{{criteria for selection}}

### 2. Variable Collection
| Variable | Description | Default |
|----------|-------------|---------|
| {{VAR1}} | {{desc}} | {{default}} |

### 3. Generation
{{generation logic}}

### 4. Validation
{{validation steps}}
```

---

## Pattern 4: Multi-Phase Sequential

### When to Use
- Complex workflows with dependencies
- Each phase builds on previous
- Clear handoff points between phases

### Structure
```markdown
## Phase 1: Discovery
{{discovery work}}

## Phase 2: Analysis
{{analysis work}}

## Phase 3: Implementation
{{implementation work}}

## Phase 4: Verification
{{verification work}}
```

### Example Skills
- MAKER: Research → Plan → Implement
- FullAudit: Scan → Analyze → Fix → Verify

### Template
```markdown
# {{SkillName}}

## Triggers
- `{{trigger phrase}}`

## Phase Overview

| Phase | Input | Output |
|-------|-------|--------|
| Discovery | {{input1}} | {{output1}} |
| Analysis | {{output1}} | {{output2}} |
| Implementation | {{output2}} | {{output3}} |
| Verification | {{output3}} | Report |

## Phase 1: Discovery
{{detailed steps}}

## Phase 2: Analysis
{{detailed steps}}

## Phase 3: Implementation
{{detailed steps}}

## Phase 4: Verification
{{detailed steps}}

## Checkpoint Behavior
{{when to pause for approval}}
```

---

## Pattern 5: Multi-Agent Parallel

### When to Use
- Independent tasks that can run concurrently
- Results need aggregation
- Performance optimization through parallelism

### Structure
```markdown
## Parallel Execution

Agent A ──┐
Agent B ──┼──► Aggregator ──► Output
Agent C ──┘
```

### Example Skills
- CodeReview (5 agents): Parallel review, unanimous approval
- FullQA: Security + A11y + Performance in parallel

### Template
```markdown
# {{SkillName}}

## Triggers
- `{{trigger phrase}}`

## Parallel Agents

| Agent | Focus | Output |
|-------|-------|--------|
| Agent 1 | {{Focus1}} | {{Output1}} |
| Agent 2 | {{Focus2}} | {{Output2}} |
| Agent 3 | {{Focus3}} | {{Output3}} |

## Execution

### Launch (Parallel)
{{launch all agents simultaneously}}

### Aggregation
{{how to combine results}}

### Consensus Rules
{{how to resolve conflicts}}

## Output Format
{{combined report structure}}
```

---

## Pattern 6: Composite Orchestrator

### When to Use
- Coordinating multiple skills
- Dynamic skill selection based on task
- Meta-level orchestration

### Structure
```markdown
## Orchestration Logic

1. Analyze task
2. Select relevant skills
3. Determine execution order
4. Execute skills
5. Aggregate results
```

### Example Skills
- SkillComposer: Meta-orchestration across all skills
- TaskRouter: Routes to appropriate specialist

### Template
```markdown
# {{SkillName}}

## Triggers
- `{{trigger phrase}}`

## Skill Registry
| Skill | Domain | Triggers |
|-------|--------|----------|
| {{Skill1}} | {{Domain1}} | {{Triggers1}} |
| {{Skill2}} | {{Domain2}} | {{Triggers2}} |

## Orchestration

### 1. Task Analysis
{{how to analyze incoming task}}

### 2. Skill Selection
{{criteria for selecting skills}}

### 3. Execution Planning
{{sequential vs parallel decision}}

### 4. Execution
{{invoke selected skills}}

### 5. Aggregation
{{combine outputs}}

## Handoff Protocol
{{data passing between skills}}
```

---

## Pattern Selection Guide

```
Is the task simple and linear?
├─ YES → Single-Phase Executor
└─ NO
    ↓
Is it about checking/validating?
├─ YES → Checklist Validator
└─ NO
    ↓
Is it about creating artifacts?
├─ YES → Generator with Templates
└─ NO
    ↓
Are phases dependent on each other?
├─ YES → Multi-Phase Sequential
└─ NO
    ↓
Can tasks run in parallel?
├─ YES → Multi-Agent Parallel
└─ NO
    ↓
Does it coordinate other skills?
├─ YES → Composite Orchestrator
└─ NO → Reconsider requirements
```

## Best Practices

1. **Start simple** - Use simplest pattern that works
2. **Add phases as needed** - Don't over-engineer initially
3. **Define clear outputs** - Each phase should produce defined artifacts
4. **Include verification** - Every pattern should end with validation
5. **Document handoffs** - Be explicit about data flow between phases
