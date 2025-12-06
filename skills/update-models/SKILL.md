# Update Models Skill

Automatically update all model references across skills, commands, plugins, and configuration files to use the latest model identifiers from the centralized model configuration.

**Triggers:** `update models`, `UpdateModels`, `update-models`, `sync models`

---
model: claude-opus-4-5-20251101
subagent_model: claude-opus-4-5-20251101
---

## Purpose

When Anthropic releases new model versions (e.g., Opus 4.6, Sonnet 5.0), you need to update all references across:
- Skills (`~/.claude/skills/**/*.md`)
- Plugins (`~/.claude/plugins/**/*.md`)
- Workflows (`~/.claude/workflows/**/*.md`)
- Commands (`~/.claude/commands/**/*.md`)
- Global config (`~/.claude/CLAUDE.md`)
- Project-specific configs (`.claude/**/*.md`)

This skill automates the entire process by reading the centralized model config and updating all references.

## How It Works

### Phase 1: Load Model Configuration

1. Read `~/.claude/config/models.yaml`
2. Extract current model identifiers:
   - `models.best` (Opus)
   - `models.balanced` (Sonnet)
   - `models.fast` (Haiku)
3. Determine what needs to be updated (old → new mappings)

### Phase 2: Scan for Model References

Search all markdown files in:
- `~/.claude/skills/`
- `~/.claude/plugins/`
- `~/.claude/workflows/`
- `~/.claude/commands/`
- `~/.claude/CLAUDE.md`
- Project directories (if specified)

Look for patterns:
- `model: claude-opus-*`
- `model: claude-sonnet-*`
- `model: claude-haiku-*`
- `subagent_model: claude-*`
- Text references like "use opus (claude-opus-4-5-20251101)"

### Phase 3: Create Update Plan

Generate a plan showing:
- **Files to update:** List of all files with model references
- **Changes per file:** Old model → New model mappings
- **Total changes:** Count of updates needed

Present plan to user for approval (unless `--auto` flag is used).

### Phase 4: Execute Updates

For each file:
1. Read current content
2. Replace old model identifiers with new ones
3. Preserve formatting and context
4. Write updated content
5. Log the change

### Phase 5: Verify & Report

1. Re-scan all files to confirm updates
2. Generate summary report:
   - ✅ Files updated (count)
   - 📝 Changes made (old → new)
   - ⏭️ Files skipped (already current)
   - ❌ Errors (if any)
3. Suggest adding version history entry to `models.yaml`

## Input Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `--dry-run` | flag | Show what would be updated without making changes | false |
| `--auto` | flag | Skip confirmation prompts | false |
| `--project <path>` | string | Also update project-specific files | none |
| `--backup` | flag | Create backup before updating | true |
| `--model <type>` | string | Only update specific model type (opus/sonnet/haiku) | all |

## Example Usage

### Standard Update (with confirmation)
```
User: "update models"

Agent:
1. Reads ~/.claude/config/models.yaml
2. Scans all files for model references
3. Shows update plan:

   📋 Update Plan

   Found 47 files with model references:
   - ~/.claude/skills/design-audit/SKILL.md: 2 updates
   - ~/.claude/skills/maker-framework/SKILL.md: 2 updates
   - ~/.claude/plugins/.../code-reviewer.md: 1 update
   - ... (44 more files)

   Changes to make:
   - claude-opus-4-5-20251101 → claude-opus-4-6-20260115 (47 occurrences)

   Proceed with updates? [Y/n]

User: "Y"

Agent: Updates all files and reports:
   ✅ 47 files updated
   📝 47 model references changed
   ⏭️ 12 files skipped (already current)
```

### Dry Run (preview only)
```
User: "update models --dry-run"

Agent: Shows what would be updated but makes no changes
```

### Auto Mode (no confirmation)
```
User: "update models --auto"

Agent: Automatically updates all files without asking for confirmation
```

### Update Specific Project
```
User: "update models --project /Users/jackatlasov/ShelfWins-Studio"

Agent: Updates global files + project-specific .claude/ directory
```

### Update Only Opus
```
User: "update models --model opus"

Agent: Only updates Opus model references, leaves Sonnet/Haiku unchanged
```

## Implementation Details

### Files to Scan

**Global Configuration:**
- `~/.claude/CLAUDE.md`
- `~/.claude/config/models.yaml` (the source of truth)

**Skills:**
- `~/.claude/skills/*/SKILL.md`
- All subdirectories and markdown files

**Plugins:**
- `~/.claude/plugins/*/agents/*.md`
- `~/.claude/plugins/*/skills/*/SKILL.md`
- All plugin markdown files

**Workflows:**
- `~/.claude/workflows/*.md`

**Commands:**
- `~/.claude/commands/*.md`

**Project-specific (if --project specified):**
- `<project>/.claude/commands/*.md`
- `<project>/.claude/skills/*/SKILL.md`

### Search Patterns

Use regex to find model references:
```regex
# Frontmatter model declarations
^model:\s*(claude-opus-[\d-]+)
^model:\s*(claude-sonnet-[\d-]+)
^model:\s*(claude-haiku-[\d-]+|claude-3-5-haiku-[\d-]+)
^subagent_model:\s*(claude-[\w-]+)

# Inline text references
\(claude-opus-[\d-]+\)
\(claude-sonnet-[\d-]+\)
\(claude-haiku-[\d-]+|claude-3-5-haiku-[\d-]+\)

# Code block examples
model:\s*["']?(claude-[\w-]+)["']?
```

### Replacement Strategy

1. **Exact match replacement:** Replace old identifier with new identifier character-for-character
2. **Preserve context:** Keep surrounding text, formatting, indentation
3. **Handle edge cases:**
   - Model names in code examples
   - Model names in documentation text
   - Comments explaining model choices

### Backup Strategy

Before making any changes:
1. Create `~/.claude/backups/models-update-<timestamp>/`
2. Copy all files that will be modified
3. If updates fail, restore from backup

### Error Handling

| Error | Action |
|-------|--------|
| models.yaml not found | Create from template, ask user to fill in |
| models.yaml malformed | Show error, abort |
| File read error | Skip file, log error, continue |
| File write error | Abort all changes, restore from backup |
| No model references found | Report success (nothing to update) |

## Success Criteria

✅ All model references updated to match `models.yaml`
✅ No broken references or syntax errors
✅ Backup created before changes
✅ Clear report showing all changes made
✅ User can verify changes with git diff
✅ Process is idempotent (can run multiple times safely)

## Integration with Other Skills

- **After running:** Suggest running `DocSync` to update documentation
- **Version tracking:** Update `models.yaml` version history
- **Git workflow:** Suggest committing changes with descriptive message

## Output Format

```markdown
## Update Models Report - 2026-01-15

### Configuration
- Source: ~/.claude/config/models.yaml
- Backup: ~/.claude/backups/models-update-20260115-143022/

### Changes Made

**Opus Updates:**
- claude-opus-4-5-20251101 → claude-opus-4-6-20260115
- 47 occurrences across 47 files

**Sonnet Updates:**
- No changes (already current)

**Haiku Updates:**
- No changes (already current)

### Files Updated (47)
✅ ~/.claude/skills/design-audit/SKILL.md (2 updates)
✅ ~/.claude/skills/maker-framework/SKILL.md (2 updates)
✅ ~/.claude/skills/skill-composer/SKILL.md (2 updates)
... (44 more)

### Files Skipped (12)
⏭️ ~/.claude/commands/build.md (no model references)
⏭️ ~/.claude/commands/todo.md (no model references)
... (10 more)

### Verification
✅ All files updated successfully
✅ No syntax errors detected
✅ Backup preserved at ~/.claude/backups/models-update-20260115-143022/

### Next Steps
1. Review changes: `git diff ~/.claude/`
2. Update documentation: Run `DocSync`
3. Commit changes: `git commit -m "chore: update to Opus 4.6"`
4. Update models.yaml version history
```

## Notes

- **Safe to run multiple times:** The skill is idempotent - running it when models are already current will report "0 updates needed"
- **Git-friendly:** Changes are clean and reviewable with `git diff`
- **Rollback:** If something goes wrong, restore from `~/.claude/backups/models-update-<timestamp>/`
- **Future-proof:** When Anthropic releases new models, just update `models.yaml` and run this skill