---
name: claude-authoring-guide
description: Best practices for authoring skills, hooks, commands, and agents in Claude Code
license: MIT
model: claude-opus-4-5-20251101
version: 1.0.0
---

# Claude Authoring Guide

Comprehensive framework for creating high-quality Claude Code extensions.

## Triggers

- `how to create skill`, `create a skill`, `new skill`
- `authoring guide`, `authoring best practices`
- `meta-prompting guide`, `separation of concerns`
- `context handoff`, `handoff document`
- `thinking models`, `mental frameworks`
- `claude extension`, `claude code patterns`

---

## Quick Reference

### Performance Formula

```
Performance = Correctness² × Completeness / Size
```

- **Correctness** has exponential impact (squared)
- Optimize: correctness first → completeness → minimize size

### Hierarchy of Leverage

| Level | Error Multiplier | Impact |
|-------|------------------|--------|
| CLAUDE.md | 100,000× | Affects every conversation |
| Spec/Plan | 10,000× | Affects entire implementation |
| Skill | 1,000× | Affects all skill invocations |
| Single task | 1× | Affects one response |

**Implication:** Invest more time in higher-leverage artifacts.

### Meta-Prompting Principle

> **"PLAN.md IS the prompt."**

Separate ANALYSIS from EXECUTION for complex tasks:
1. Analysis phase → generates specification
2. Execution phase → implements specification (fresh context)

### When to Create What

| Need | Create | Location |
|------|--------|----------|
| Always-on principles | CLAUDE.md | `~/.claude/` or `.claude/` |
| Reusable procedures | Skill | `~/.claude/skills/` |
| User-initiated actions | Command | `~/.claude/commands/` |
| Automatic processing | Hook | `~/.claude/hooks/` |
| Project-specific work | Agent | `.claude/agents/` |

[Full decision tree → references/decision-trees.md]

---

## Part 1: Skills

Skills are packaged procedural knowledge activated by trigger phrases.

### Structure

```
skill-name/
├── SKILL.md           # Main entry (required)
├── assets/
│   ├── templates/     # Starter files
│   └── checklists/    # Quality checks
├── references/        # Deep documentation
└── scripts/           # Validation tools
```

### Required Elements

| Element | Purpose |
|---------|---------|
| Frontmatter | `name`, `description`, `model` |
| Triggers | 3-5 activation phrases |
| Process | Clear steps or phases |
| Verification | How to confirm success |

### Skill Patterns

| Pattern | Use When |
|---------|----------|
| Single-Phase | Simple linear tasks |
| Checklist | Quality/compliance audits |
| Generator | Creating artifacts from templates |
| Multi-Phase | Complex ordered workflows |
| Multi-Agent | Independent parallel tasks |
| Orchestrator | Coordinating multiple skills |

[Templates → assets/templates/skill-template.md]
[Full patterns → references/skill-patterns.md]
[Quality checklist → assets/checklists/skill-quality.md]

---

## Part 2: Commands

Slash commands for user-initiated actions.

### Structure

```markdown
# Command Name

Brief description of what this does.

## Usage
/command-name [arguments]

## Arguments
| Arg | Required | Description |
|-----|----------|-------------|

## Examples
/command-name foo
```

### Best Practices

- Filename: kebab-case (e.g., `create-agent.md`)
- Keep under 100 lines
- Include examples
- Document all arguments

[Template → assets/templates/command-template.md]
[Quality checklist → assets/checklists/command-quality.md]

---

## Part 3: Hooks

Automatic processing triggered by system events.

### Event Types

| Event | Trigger | Use Case |
|-------|---------|----------|
| SessionStart | New session | Load context, memories |
| UserPromptSubmit | User sends message | Inject context |
| PreToolUse | Before tool runs | Validation, blocking |
| PostToolUse | After tool completes | Transform output |
| SessionEnd | Session closes | Save state |
| PreCompact | Before summarization | Preserve critical info |

### Critical Rules

1. **Never crash** - graceful degradation only
2. **Return valid JSON** - even on errors
3. **Fast execution** - <100ms target
4. **No side effects** - unless intentional

[Template → assets/templates/hook-template.py]
[Quality checklist → assets/checklists/hook-quality.md]

---

## Part 4: Agents

Project-specific subagent templates.

### Structure

```markdown
# Agent Name

## Purpose
What this agent specializes in.

## Approach
1. Discovery - understand context
2. Analysis - identify solutions
3. Implementation - make changes
4. Verification - confirm success

## Tools Available
List specific tool permissions.

## Success Criteria
Measurable outcomes.
```

### Agent Types

| Type | Purpose |
|------|---------|
| Feature Enhancer | Adding capabilities |
| Flow Fixer | Fixing workflow issues |
| State Connector | Reactivity/state problems |
| Wizard Builder | Multi-step guided flows |
| Test Writer | E2E or unit tests |

[Template → assets/templates/agent-template.md]
[Quality checklist → assets/checklists/agent-quality.md]

---

## Part 5: CLAUDE.md Files

Configuration files that shape Claude's behavior.

### Scope

| Type | Location | Applies To |
|------|----------|------------|
| Global | `~/.claude/CLAUDE.md` | All projects |
| Project | `.claude/CLAUDE.md` | Single project |

### Content Guidelines

**Global CLAUDE.md:**
- Core principles only
- Communication style
- Model preferences
- Skill discovery references
- Target: <70 lines

**Project CLAUDE.md:**
- Project-specific workflows
- Tech stack details
- Domain conventions
- Can be longer (150-250 lines)

### Principles vs Procedures

| CLAUDE.md (Principles) | Skills (Procedures) |
|------------------------|---------------------|
| "Verify before commit" | Step-by-step verification |
| "Use TypeScript" | TS configuration guide |
| "Test coverage >80%" | Test generation workflow |

[Template → assets/templates/project-claude-md.md]
[Lint tool → scripts/lint_claude_md.py]

---

## Part 6: Context Engineering

Three types of context in Claude Code:

| Type | Example | Loading |
|------|---------|---------|
| Static | CLAUDE.md | Always present |
| Dynamic | Skills | On trigger match |
| Procedural | Hooks | On system events |

### Progressive Disclosure

Load context on need-to-know basis:
1. CLAUDE.md provides minimal principles
2. Trigger phrases activate relevant skills
3. Skills reference deeper documentation

### The 10% Rule

Trigger context handoff when ~10% context remains:
- Leaves room for handoff generation
- Prevents abrupt information loss
- Enables seamless continuation

[Full guide → references/context-engineering.md]

---

## Part 7: Meta-Prompting

Separate analysis from execution for complex tasks.

### When to Use

| Use For | Skip For |
|---------|----------|
| Complex refactoring | Simple edits |
| Architecture decisions | Single-file changes |
| Migrations | Quick experiments |
| Multi-file coordination | Clear requirements |

### Pattern

```
1. Analysis Phase
   - Ask clarifying questions
   - Analyze codebase
   - Generate specification

2. Execution Phase (fresh context)
   - Receive specification
   - Implement exactly
   - Verify against criteria
```

[Full guide → references/meta-prompting.md]

---

## Part 8: Thinking Models

11 mental frameworks for analysis:

| Model | Core Question |
|-------|---------------|
| First Principles | What's fundamentally true? |
| Pareto (80/20) | What 20% matters most? |
| Inversion | What guarantees failure? |
| Second-Order Effects | Then what happens? |
| Pre-Mortem | Why did this fail? |
| Devil's Advocate | What's the counter-argument? |
| Systems Thinking | How do parts interact? |
| Opportunity Cost | What are we giving up? |
| Constraint Analysis | What's really fixed? |
| Root Cause (5 Whys) | Why? Why? Why? |
| Comparative Analysis | How do options compare? |

**Use during Research phase:** Apply 2-3 relevant models.

[Full guide → references/thinking-models.md]

---

## Part 9: Context Handoff

Preserve work state across context boundaries.

### Trigger

When context reaches ~10% remaining capacity.

### Document Structure

```markdown
## Original Task
<task>exact original request</task>

## Work Completed
<completed>files modified, decisions made</completed>

## Work Remaining
<remaining>next steps, blockers</remaining>

## Attempted Approaches
<attempts>what didn't work and WHY</attempts>

## Current State
<state>git status, test status</state>
```

### Key Principles

1. Document failures (prevent repetition)
2. Preserve reasoning (not just actions)
3. Maintain scope (prevent drift)
4. Enable seamless continuation

[Full guide → references/context-handoff.md]
[Template → assets/templates/context-handoff.md]

---

## Part 10: Quality Controls

### Research Quality

Before finalizing analysis:

**Blind Spots Review:**
- [ ] Checked opposing viewpoints
- [ ] Considered edge cases
- [ ] Identified assumptions
- [ ] Verified data sources

**Critical Claims Audit:**
- [ ] Each claim has evidence
- [ ] Sources are cited
- [ ] Uncertainty is acknowledged

[Full checklist → assets/checklists/research-quality.md]

### Extension Quality

Use appropriate checklist before publishing:
- Skills → [skill-quality.md]
- Commands → [command-quality.md]
- Hooks → [hook-quality.md]
- Agents → [agent-quality.md]

---

## Part 11: ACE Framework

Generator → Reflector → Curator cycle for quality output.

| Phase | Role | Output |
|-------|------|--------|
| Generator | Create content | Draft |
| Reflector | Critique quality | Feedback |
| Curator | Integrate delta | Final |

**Key Insight:** Curator makes delta updates (not regeneration).

[Full guide → references/ace-framework.md]

---

## Part 12: Failure Modes

| Failure | Risk | Mitigation |
|---------|------|------------|
| Hallucination | High | Verify with evidence |
| Context limits | Medium | Handoff at 10% |
| Prompt injection | Medium | Validate inputs |
| Tool misuse | Low | Permission controls |
| Incomplete work | Medium | Todo tracking |
| Scope creep | Medium | Maintain boundaries |
| Poor handoffs | Medium | Structured templates |

[Full taxonomy → references/failure-modes.md]

---

## Validation Commands

```bash
# Validate a skill
python ~/.claude/skills/claude-authoring-guide/scripts/validate_skill.py path/to/skill/

# Validate commands
python ~/.claude/skills/claude-authoring-guide/scripts/validate_command.py ~/.claude/commands/

# Lint CLAUDE.md
python ~/.claude/skills/claude-authoring-guide/scripts/lint_claude_md.py --global
```

---

## Reference Documents

| Document | Topic |
|----------|-------|
| [hierarchy-of-leverage.md](references/hierarchy-of-leverage.md) | Error multiplier analysis |
| [context-engineering.md](references/context-engineering.md) | Context types and loading |
| [failure-modes.md](references/failure-modes.md) | Risk taxonomy |
| [ace-framework.md](references/ace-framework.md) | Generator-Reflector-Curator |
| [skill-patterns.md](references/skill-patterns.md) | Architecture patterns |
| [decision-trees.md](references/decision-trees.md) | When to build what |
| [meta-prompting.md](references/meta-prompting.md) | Analysis/execution separation |
| [context-handoff.md](references/context-handoff.md) | State preservation |
| [thinking-models.md](references/thinking-models.md) | Mental frameworks |

---

## Quick Start

### Create a New Skill

1. Copy template: `assets/templates/skill-template.md`
2. Fill in frontmatter and triggers
3. Define process steps
4. Add verification section
5. Run: `python scripts/validate_skill.py ./`
6. Review: `assets/checklists/skill-quality.md`

### Create a New Command

1. Copy template: `assets/templates/command-template.md`
2. Use kebab-case filename
3. Document arguments and examples
4. Run: `python scripts/validate_command.py ./command.md`

### Create a New Hook

1. Copy template: `assets/templates/hook-template.py`
2. Implement handler for target event
3. Ensure graceful failure
4. Test with each event type
5. Review: `assets/checklists/hook-quality.md`

---

## Summary

| Principle | Application |
|-----------|-------------|
| Correctness² | Verify everything, errors compound |
| 100,000× impact | Invest in CLAUDE.md quality |
| Progressive disclosure | Load context on demand |
| Separate analysis/execution | Meta-prompting for complex tasks |
| Handoff at 10% | Preserve context proactively |
| Document failures | Prevent repeated mistakes |
| Use thinking models | Systematic analysis |
| Quality checklists | Pre-publish validation |
