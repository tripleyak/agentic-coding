# Agent Templates

Quick-deploy subagent templates for common development tasks. Use `/create-agent` to interactively generate customized agents from these templates.

## Available Templates (9 total)

### Core Templates (General Purpose)

| Template | Use Case | Example |
|----------|----------|---------|
| `feature-enhancer.md` | Add new capabilities to existing components | Image upload, new options, UI improvements |
| `flow-fixer.md` | Fix broken user flows/workflows | Wizard redirects, form submissions failing |
| `state-connector.md` | Fix disconnected UI reactivity | Selector not updating preview, state not reflecting |

### Development Templates

| Template | Use Case | Example |
|----------|----------|---------|
| `wizard-builder.md` | Create multi-step guided workflows | New 6-step product wizard, onboarding flow |
| `ai-feature-integrator.md` | Add new AI/Gemini capabilities | Competitor analysis, price optimization AI |
| `hook-creator.md` | Create custom React hooks | usePricingHandlers, useCompetitorData |

### Quality Assurance Templates

| Template | Use Case | Example |
|----------|----------|---------|
| `e2e-test-writer.md` | Add Playwright E2E tests | Wizard flow tests, export tests |
| `unit-test-writer.md` | Add Vitest unit tests | Hook tests, service tests, utility tests |
| `performance-auditor.md` | Audit and fix performance | Bundle size, render optimization |

## Quick Start

### Option 1: Interactive (Recommended)
```bash
/create-agent
```
The command will ask which template you need and gather the required information interactively.

### Option 2: Manual
```bash
# 1. Copy template to your project
cp ~/.claude/agent-templates/wizard-builder.md \
   ./your-project/.claude/agents/my-wizard-builder.md

# 2. Edit the file and replace {{PLACEHOLDERS}}

# 3. Delete the instructions section at the bottom
```

## How to Choose

### Adding Features
| Situation | Template |
|-----------|----------|
| Adding new UI capabilities to existing component | `feature-enhancer` |
| Creating a new multi-step wizard/studio | `wizard-builder` |
| Adding AI-powered functionality | `ai-feature-integrator` |
| Creating new stateful logic | `hook-creator` |

### Fixing Issues
| Situation | Template |
|-----------|----------|
| User flow breaks unexpectedly | `flow-fixer` |
| UI doesn't react to user input | `state-connector` |
| Performance problems | `performance-auditor` |

### Testing
| Situation | Template |
|-----------|----------|
| Need E2E coverage for a feature | `e2e-test-writer` |
| Need unit tests for hook/service | `unit-test-writer` |

## Template Structure

All templates follow this structure:

```markdown
---
name: {{AGENT_NAME}}
description: {{DESCRIPTION}}
tools: Read, Write, Edit, Glob, Grep, Bash, ...
skills: skill-composer, frontend-design, ...
model: opus
---

# {{Title}}

You are a senior engineer specializing in...

## Goal
## Your Approach
1. Discovery Phase
2. Analysis Phase
3. Implementation
4. Verification

## Reference Patterns
## Skills Available
## Output Requirements

---
## TEMPLATE USAGE INSTRUCTIONS (delete after customizing)
```

## Placeholder Reference

All templates use `{{PLACEHOLDER}}` syntax:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{AGENT_NAME}}` | kebab-case identifier | `user-profile-enhancer` |
| `{{AGENT_TITLE}}` | Human-readable title | `User Profile Enhancer` |
| `{{SPECIALIZATION}}` | Technical expertise area | `React forms and validation` |
| `{{TARGET_COMPONENT}}` | What you're working on | `User Profile Editor` |
| `{{SEARCH_TERMS}}` | Code search keywords | `"UserProfile", "EditUser"` |

## Project Setup

Ensure your project has the agents directory:

```bash
mkdir -p .claude/agents
```

Then copy and customize templates as needed.

## Tips

1. **Use `/create-agent`** - It's faster than manual copying and ensures you fill in all placeholders
2. **Delete the instructions section** at the bottom of each template after customizing
3. **Be specific with search terms** - Helps the agent find relevant code faster
4. **List all scenarios in verification** - Ensures complete testing
5. **Keep problem statements focused** - One clear issue per agent works best
6. **Combine templates when needed** - Create a wizard + write E2E tests for it
