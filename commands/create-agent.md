# Create Custom Subagent

You are helping the user create customized subagents from templates. Follow this interactive workflow:

## Step 0: Choose Mode

Ask the user using AskUserQuestion:

**How many agents do you want to create?**
- **Single agent** - Create one agent now
- **Batch mode** - Collect specs for multiple agents, then generate all at once

If **Single agent**: Proceed to Step 1 and follow the standard flow.

If **Batch mode**: Follow the batch workflow described in the "Batch Mode Workflow" section below.

---

## Single Agent Workflow

### Step 1: Choose Template Type

Ask the user which type of agent they need using AskUserQuestion. Present the 9 available templates organized by category:

### Core Templates
| Type | Use When |
|------|----------|
| **Feature Enhancer** | Adding new capabilities, UI improvements, new options |
| **Flow Fixer** | Broken workflows, unexpected redirects, state resets |
| **State Connector** | UI not reacting to selections, disconnected previews |

### Development Templates
| Type | Use When |
|------|----------|
| **Wizard Builder** | Creating new multi-step guided workflows (3+ steps) |
| **AI Feature Integrator** | Adding new Gemini/AI capabilities |
| **Hook Creator** | Creating new custom React hooks |

### Quality Assurance Templates
| Type | Use When |
|------|----------|
| **E2E Test Writer** | Adding Playwright end-to-end tests |
| **Unit Test Writer** | Adding Vitest unit tests for hooks/services |
| **Performance Auditor** | Auditing and fixing performance issues |

### Step 2: Gather Information

Based on their selection, ask follow-up questions to fill in the template. Use AskUserQuestion for structured choices, or ask in natural conversation for free-form answers.

### For Feature Enhancer, ask:
1. Agent name (kebab-case, e.g., `user-profile-enhancer`)
2. What component/area are you enhancing?
3. What's missing or needs to be added? (list the features)
4. What search terms should the agent use to find relevant code?
5. Any specific implementation details or constraints?

### For Flow Fixer, ask:
1. Agent name (kebab-case, e.g., `checkout-flow-fixer`)
2. What flow/workflow is broken?
3. What happens now (the bug)?
4. What SHOULD happen instead?
5. What actions trigger the broken behavior?
6. What search terms should the agent use?

### For State Connector, ask:
1. Agent name (kebab-case, e.g., `theme-selector-connector`)
2. What input/control isn't working?
3. What output/display should it update?
4. What options/variants should be supported?
5. What search terms should the agent use?

### For Wizard Builder, ask:
1. Agent name (kebab-case, e.g., `competitor-analysis-wizard-builder`)
2. What is the wizard for? (purpose)
3. How many steps? List each step name and brief description
4. What's the final output? (PDF, CSV, etc.)
5. What search terms should the agent use to find similar patterns?

### For AI Feature Integrator, ask:
1. Agent name (kebab-case, e.g., `price-optimizer-ai-integrator`)
2. What AI capability are you adding?
3. What inputs does it need?
4. What output format should it produce?
5. What search terms for finding existing AI patterns?

### For Hook Creator, ask:
1. Agent name (kebab-case, e.g., `pricing-handlers-hook-creator`)
2. Hook name (e.g., `usePricingHandlers`)
3. What is the hook's purpose?
4. What handlers/actions should it expose?
5. What state should it manage?

### For E2E Test Writer, ask:
1. Agent name (kebab-case, e.g., `sell-sheet-e2e-tests`)
2. What feature/flow are you testing?
3. List the test scenarios (3-5 scenarios)
4. What's the entry point to the feature?
5. What assertions are critical?

### For Unit Test Writer, ask:
1. Agent name (kebab-case, e.g., `pricing-service-unit-tests`)
2. What file are you testing? (hook, service, or utility)
3. What functions/methods need tests?
4. What needs to be mocked? (localStorage, fetch, etc.)
5. Any edge cases to cover?

### For Performance Auditor, ask:
1. Agent name (kebab-case, e.g., `export-modal-performance-audit`)
2. What area has performance issues?
3. What symptoms are you seeing? (slow load, janky scroll, large bundle)
4. What are your performance targets?
5. Any known problem areas?

### Step 3: Generate the Agent

Read the appropriate template from `~/.claude/agent-templates/`:
- `feature-enhancer.md`
- `flow-fixer.md`
- `state-connector.md`
- `wizard-builder.md`
- `ai-feature-integrator.md`
- `hook-creator.md`
- `e2e-test-writer.md`
- `unit-test-writer.md`
- `performance-auditor.md`

Replace all `{{PLACEHOLDER}}` values with the user's answers. Remove the "TEMPLATE USAGE INSTRUCTIONS" section at the bottom.

### Step 4: Write the File

1. First, ensure the project has a `.claude/agents/` directory (create if needed)
2. Write the customized agent to: `./.claude/agents/{agent-name}.md`
3. Confirm success and show the user how to use the new agent

### Step 5: Offer Next Steps

Ask if they want to:
- Create another agent
- Review/edit the generated agent
- Start using the agent immediately

### Important Guidelines

- Be conversational but efficient
- Provide helpful examples when asking questions
- If the user's answer is unclear, ask for clarification
- Make reasonable inferences where possible (e.g., derive agent title from agent name)
- Always confirm the final agent name and location before writing
- For complex templates (wizard-builder, ai-feature-integrator), take extra care to gather detailed specifications

---

## Batch Mode Workflow

Use this workflow when the user selects "Batch mode" in Step 0.

### Batch Step 1: Initialize Collection

Tell the user: "I'll collect specs for all your agents first, then generate them all at once. Let's start with Agent #1."

Create an internal list to track agent specs:
```
agents_to_create = []
```

### Batch Step 2: Collect Agent Spec

For each agent, gather:
1. **Template type** - Ask which of the 9 templates they need (same as Single Agent Step 1)
2. **Template-specific info** - Ask the questions for that template type (same as Single Agent Step 2)

Store the collected spec in the list.

### Batch Step 3: Continue or Finish

After collecting each agent spec, ask using AskUserQuestion:

**Agent #{n} spec collected. What next?**
- **Add another agent** - Collect specs for another agent
- **Done - Generate all** - Generate all {n} agents now

If "Add another": Return to Batch Step 2 for the next agent.

If "Done - Generate all": Proceed to Batch Step 4.

### Batch Step 4: Review Before Generation

Present a summary table of all agents to be created:

```
## Agents to Create ({n} total)

| # | Agent Name | Template | Target |
|---|------------|----------|--------|
| 1 | user-profile-enhancer | Feature Enhancer | UserProfile component |
| 2 | checkout-flow-fixer | Flow Fixer | Checkout wizard |
| 3 | pricing-service-tests | Unit Test Writer | usePricing hook |
```

Ask: "Ready to generate all {n} agents? Or would you like to modify any specs?"

### Batch Step 5: Generate All Agents

1. Ensure `.claude/agents/` directory exists
2. For each agent spec in the list:
   - Read the appropriate template from `~/.claude/agent-templates/`
   - Replace all `{{PLACEHOLDER}}` values
   - Remove the "TEMPLATE USAGE INSTRUCTIONS" section
   - Write to `./.claude/agents/{agent-name}.md`
3. Report progress as you generate each agent

### Batch Step 6: Summary

After all agents are generated, show:

```
## Created {n} Agents

| Agent | File | Status |
|-------|------|--------|
| user-profile-enhancer | .claude/agents/user-profile-enhancer.md | Created |
| checkout-flow-fixer | .claude/agents/checkout-flow-fixer.md | Created |
| pricing-service-tests | .claude/agents/pricing-service-tests.md | Created |

All agents are ready to use!
```

### Batch Mode Tips

- If the user wants similar agents (e.g., multiple unit test writers), ask if they want to reuse common settings
- For large batches (5+), periodically confirm specs to avoid losing context
- If any agent fails to generate, continue with the others and report failures at the end
- Offer to run agents in parallel after generation if the user wants to execute them immediately
