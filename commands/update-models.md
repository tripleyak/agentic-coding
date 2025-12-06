---
description: Update all model references to latest versions from models.yaml config
model: claude-opus-4-5-20251101
---

Execute the `update-models` skill to automatically update all Claude model references across skills, commands, plugins, and configuration files.

This command:
1. Reads the centralized model configuration from `~/.claude/config/models.yaml`
2. Scans all markdown files for model references
3. Shows you an update plan
4. Updates all references to match the current model identifiers
5. Creates a backup before making changes
6. Generates a detailed report

**When to use this:**
- After Anthropic releases a new model version (e.g., Opus 4.6, Sonnet 5.0)
- To ensure all skills and commands use the latest model identifiers
- To standardize model references across your configuration

**Workflow:**
1. Edit `~/.claude/config/models.yaml` with new model identifiers
2. Run `/update-models`
3. Review the update plan
4. Confirm to proceed
5. Review changes with `git diff`
6. Commit changes

**Available flags:**
- `--dry-run`: Preview changes without making them
- `--auto`: Skip confirmation prompts
- `--project <path>`: Also update project-specific files
- `--model <type>`: Only update specific model (opus/sonnet/haiku)

**Examples:**
- `/update-models` - Standard update with confirmation
- `/update-models --dry-run` - Preview only
- `/update-models --auto` - No prompts
- `/update-models --project /Users/jackatlasov/ShelfWins-Studio` - Include project files
