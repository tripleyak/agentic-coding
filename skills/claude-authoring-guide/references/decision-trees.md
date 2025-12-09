# Decision Trees: When to Build What

Structured decision guides for choosing the right Claude Code extension type.

---

## Master Decision Tree

```
START: What type of extension do I need?
│
├─ Is this behavior needed for EVERY interaction?
│  ├─ YES → Consider CLAUDE.md
│  │  └─ Is it a principle (how to think) or procedure (what to do)?
│  │     ├─ Principle → Add to CLAUDE.md (brief!)
│  │     └─ Procedure → Create a skill, reference from CLAUDE.md
│  │
│  └─ NO → Continue...
│
├─ Is this triggered automatically by system events?
│  ├─ YES → Create a HOOK
│  │  └─ Which event? → See Hook Selection below
│  │
│  └─ NO → Continue...
│
├─ Is this triggered by explicit user command (/slash)?
│  ├─ YES → Create a COMMAND
│  │  └─ Is it interactive? → See Command Patterns below
│  │
│  └─ NO → Continue...
│
├─ Is this reusable knowledge triggered by phrases?
│  ├─ YES → Create a SKILL
│  │  └─ How complex? → See Skill Patterns below
│  │
│  └─ NO → Continue...
│
├─ Is this a project-specific subagent template?
│  ├─ YES → Create an AGENT
│  │  └─ Which pattern? → See Agent Patterns below
│  │
│  └─ NO → Just do the task directly (one-off)
```

---

## CLAUDE.md Decision Tree

```
Should this go in CLAUDE.md?
│
├─ Does it apply to ALL conversations in this scope?
│  ├─ NO → Don't add to CLAUDE.md
│  └─ YES → Continue...
│
├─ Is it brief enough to include directly?
│  ├─ NO → Create skill, add trigger phrase to CLAUDE.md
│  └─ YES → Continue...
│
├─ Is it a principle or procedure?
│  ├─ PROCEDURE → Move to skill, keep reference in CLAUDE.md
│  └─ PRINCIPLE → Add to CLAUDE.md
│
└─ Final: Add to appropriate section
   ├─ Zero Error Standard → verification rules
   ├─ Context Engineering → communication, context types
   ├─ Three-Phase Workflow → research/plan/implement
   ├─ Failure Awareness → risk mitigation
   └─ Skills → trigger discovery, references
```

---

## Hook Selection Tree

```
Which hook type do I need?
│
├─ When should it trigger?
│  │
│  ├─ Session begins → SessionStart
│  │  └─ Use for: Loading memories, setting context, initialization
│  │
│  ├─ User sends message → UserPromptSubmit
│  │  └─ Use for: Injecting context, enriching prompts
│  │
│  ├─ Before tool executes → PreToolUse
│  │  └─ Use for: Validation, blocking unsafe actions
│  │
│  ├─ After tool completes → PostToolUse
│  │  └─ Use for: Transforming output, logging
│  │
│  ├─ Session ends → SessionEnd
│  │  └─ Use for: Saving state, generating handoffs
│  │
│  └─ Before compaction → PreCompact
│     └─ Use for: Preserving critical context
│
└─ Can it fail gracefully? → All hooks must never crash
```

---

## Command Pattern Tree

```
What type of command pattern?
│
├─ Does it need user input during execution?
│  ├─ YES → Interactive Command
│  │  └─ Characteristics:
│  │     • Ask clarifying questions
│  │     • Present options
│  │     • Confirm before actions
│  │
│  └─ NO → Continue...
│
├─ Does it execute predefined steps?
│  ├─ YES → Batch Command
│  │  └─ Characteristics:
│  │     • Minimal interaction
│  │     • Clear success/failure
│  │     • Idempotent operations
│  │
│  └─ NO → Continue...
│
└─ Does it only read/report (no modifications)?
   └─ YES → Diagnostic Command
      └─ Characteristics:
         • Read-only
         • Report findings
         • Safe to run anytime
```

---

## Skill Complexity Tree

```
How complex is the skill?
│
├─ Is it a simple linear workflow?
│  └─ YES → Single-Phase Executor
│     Example: ErrorExplainer
│
├─ Is it about checking/validating?
│  └─ YES → Checklist Validator
│     Example: SecurityAudit
│
├─ Does it generate artifacts from templates?
│  └─ YES → Generator with Templates
│     Example: SkillCreator
│
├─ Are phases dependent on each other?
│  └─ YES → Multi-Phase Sequential
│     Example: MAKER framework
│
├─ Can tasks run in parallel?
│  └─ YES → Multi-Agent Parallel
│     Example: CodeReview (5 agents)
│
└─ Does it coordinate other skills?
   └─ YES → Composite Orchestrator
      Example: SkillComposer
```

---

## Agent Pattern Tree

```
What is the agent doing?
│
├─ Adding new capabilities?
│  └─ Feature Enhancer
│     Use when: Adding features to existing components
│
├─ Fixing broken behavior?
│  ├─ Is it a workflow issue?
│  │  └─ YES → Flow Fixer
│  │     Use when: User journeys break unexpectedly
│  │
│  └─ Is it a reactivity/state issue?
│     └─ YES → State Connector
│        Use when: UI doesn't respond to changes
│
├─ Building something new?
│  ├─ Multi-step guided flow?
│  │  └─ YES → Wizard Builder
│  │     Use when: Creating onboarding, setup flows
│  │
│  └─ Custom hook logic?
│     └─ YES → Hook Creator
│        Use when: New React hooks needed
│
└─ Testing/quality?
   ├─ End-to-end tests?
   │  └─ E2E Test Writer
   │     Use when: Playwright tests needed
   │
   └─ Unit tests?
      └─ Unit Test Writer
         Use when: Vitest/Jest tests needed
```

---

## Quick Reference Tables

### Extension Types Summary

| Type | Location | Trigger | Best For |
|------|----------|---------|----------|
| CLAUDE.md | ~/.claude/ or .claude/ | Always loaded | Core principles |
| Skill | ~/.claude/skills/ | Phrase match | Reusable procedures |
| Command | ~/.claude/commands/ | /slash-name | User-initiated actions |
| Hook | ~/.claude/hooks/ | System events | Automatic processing |
| Agent | .claude/agents/ | Task tool | Project-specific work |

### Scope Comparison

| Extension | Scope | Persistence | Invocation |
|-----------|-------|-------------|------------|
| Global CLAUDE.md | All projects | Permanent | Automatic |
| Project CLAUDE.md | One project | Permanent | Automatic |
| Skill | All projects | Permanent | Phrase trigger |
| Command | All projects | Permanent | Explicit /command |
| Hook | All projects | Permanent | System event |
| Agent | One project | Permanent | Task tool |

### Complexity Ladder

```
Simple ─────────────────────────────────────► Complex

CLAUDE.md < Command < Hook < Simple Skill < Complex Skill < Orchestrator
   ↓           ↓        ↓         ↓              ↓              ↓
 Lines     Markdown   Python   Single      Multi-Phase    Multi-Skill
of text                       -Phase                      Composition
```
