# Command Quality Checklist

Use this checklist before publishing a new slash command.

## Structure

- [ ] YAML frontmatter complete
  - [ ] `description` (short, shown in command list)
  - [ ] `model` (claude-opus-4-5-20251101)
- [ ] Process steps numbered and clear
- [ ] Output format specified
- [ ] Arguments documented (if any)

## Content Quality

- [ ] **Single purpose** - Command does one thing well
- [ ] **Clear instructions** - Steps are unambiguous
- [ ] **No placeholder text** - All {{PLACEHOLDERS}} replaced
- [ ] **Examples included** - Show typical usage

## Command Pattern

| Pattern | Characteristics | Checklist |
|---------|-----------------|-----------|
| Interactive | Asks questions, provides options | [ ] Questions clear, [ ] Options exhaustive |
| Batch | Executes steps, minimal interaction | [ ] Steps atomic, [ ] Failure handling |
| Diagnostic | Read-only, reports findings | [ ] No modifications, [ ] Clear output format |

## Naming Convention

- [ ] Lowercase with hyphens (e.g., `my-command.md`)
- [ ] Name reflects action (verb-noun pattern preferred)
- [ ] No collision with existing commands

## Arguments Handling

- [ ] `$ARGUMENTS` documented if used
- [ ] Default behavior when no arguments provided
- [ ] Error handling for invalid arguments

## Output Format

- [ ] Success output is clear
- [ ] Failure output explains what went wrong
- [ ] Follows consistent formatting

## Testing

- [ ] Tested without arguments
- [ ] Tested with various argument combinations
- [ ] Tested failure cases

## File Location

- [ ] Saved to `~/.claude/commands/{{name}}.md`
- [ ] File name matches command name

## Final Verification

```bash
# Run command validator
python ~/.claude/skills/claude-authoring-guide/scripts/validate_command.py path/to/command.md
```
