---
description: {{SHORT_DESCRIPTION}}
model: claude-opus-4-5-20251101
---

# {{COMMAND_NAME}}

{{DETAILED_DESCRIPTION}}

## Arguments

`$ARGUMENTS` = {{ARGUMENT_DESCRIPTION}}

## Process

1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

## Output Format

{{OUTPUT_FORMAT_DESCRIPTION}}

## Examples

### Basic Usage
```
/{{command-name}}
```

### With Arguments
```
/{{command-name}} {{example-args}}
```

## Flags (optional)

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview without executing |
| `--verbose` | Show detailed output |

---

## Template Usage Instructions (delete after customizing)

### Required Placeholders
- `{{SHORT_DESCRIPTION}}` - One line for frontmatter (shown in command list)
- `{{COMMAND_NAME}}` - Display name (e.g., "Build Project")
- `{{DETAILED_DESCRIPTION}}` - Full explanation of what the command does
- `{{ARGUMENT_DESCRIPTION}}` - What arguments the command accepts

### Command Patterns

**Interactive Commands:**
- Ask clarifying questions before execution
- Use step-by-step guidance
- Provide options for user to choose

**Batch Commands:**
- Execute predefined steps
- Minimal user interaction
- Clear success/failure output

**Diagnostic Commands:**
- Read-only operations
- Report findings
- No modifications to files

### File Location
Save to: `~/.claude/commands/{{command-name}}.md`

### Quality Checklist
- [ ] Description fits in command list display
- [ ] Arguments documented if any
- [ ] Examples show common usage
- [ ] No placeholder text remaining
