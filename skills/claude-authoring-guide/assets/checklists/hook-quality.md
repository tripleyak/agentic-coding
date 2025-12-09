# Hook Quality Checklist

Use this checklist before deploying a new hook.

## Structure

- [ ] Shebang line: `#!/usr/bin/env python3`
- [ ] Docstring with hook type and description
- [ ] Input JSON format documented
- [ ] Output behavior documented
- [ ] `if __name__ == "__main__":` guard

## Code Quality

- [ ] **Standard library only** - No external dependencies
- [ ] **Never crashes** - All exceptions caught
- [ ] **Fast execution** - Completes in < 5 seconds
- [ ] **Idempotent** - Safe to run multiple times
- [ ] **JSON I/O** - stdin/stdout are JSON

## Hook Type Verification

| Hook Type | Input Fields | Output Behavior |
|-----------|--------------|-----------------|
| UserPromptSubmit | session_id, prompt, cwd | stdout prepended to message |
| PreToolUse | session_id, tool_name, tool_input, cwd | "block" to prevent execution |
| PostToolUse | session_id, tool_name, tool_output, cwd | stdout appended to output |
| SessionStart | session_id, cwd | stdout typically ignored |
| SessionEnd | session_id, cwd | stdout typically ignored |
| PreCompact | session_id, cwd | stdout typically ignored |

- [ ] Correct hook type specified in docstring
- [ ] Input fields match hook type
- [ ] Output behavior matches hook type

## Error Handling

- [ ] All external calls wrapped in try/except
- [ ] Timeout for network requests (5 sec max)
- [ ] Graceful degradation on failure
- [ ] No error output to stdout (breaks protocol)

## Security

- [ ] No hardcoded secrets
- [ ] Input validation for untrusted data
- [ ] Safe file path handling
- [ ] No command injection vulnerabilities

## Testing

Manual testing:
```bash
# Test with sample input
echo '{"session_id": "test", "prompt": "hello", "cwd": "/tmp"}' | python hook.py
```

- [ ] Tested with valid input
- [ ] Tested with missing fields
- [ ] Tested with malformed JSON
- [ ] Tested timeout behavior

## Permissions

- [ ] File is executable: `chmod +x hook.py`
- [ ] Correct ownership

## File Location

- [ ] Saved to `~/.claude/hooks/{{name}}.py`
- [ ] Snake_case filename

## Configuration

If hook needs configuration:
- [ ] Uses environment variables
- [ ] Documents required env vars in docstring
- [ ] Provides sensible defaults

## Final Verification

```bash
# Check executable
ls -la ~/.claude/hooks/hook_name.py

# Test execution
echo '{}' | ~/.claude/hooks/hook_name.py
```
