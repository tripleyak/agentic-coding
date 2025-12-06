# ErrorExplainer Skill

Translates cryptic stack traces and error messages into plain English with actionable fixes. Essential for non-programmers hitting errors.

**Triggers:** `explain error`, `what does this mean`, `help with error`, `fix this error`, auto-detect stack traces

**Domain:** Debugging

## Process

| Phase | Action |
|-------|--------|
| 1. Detect | Identify error type (syntax, runtime, build, dependency, network) |
| 2. Parse | Extract key info: file, line, error code, message |
| 3. Explain | Plain English explanation of what went wrong |
| 4. Fix | Suggest concrete fixes ranked by likelihood |
| 5. Prevent | Tips to avoid this error in the future |

## Error Categories

| Category | Examples | Common Fixes |
|----------|----------|--------------|
| Syntax | Unexpected token, missing bracket | Show corrected code |
| Type | Cannot read property of undefined | Add null checks, verify data shape |
| Import | Module not found, cannot resolve | Check path, install package |
| Build | TypeScript errors, webpack failures | Fix types, check config |
| Runtime | Unhandled promise rejection | Add try/catch, check async flow |
| Network | CORS, 404, timeout | Check URL, add headers, verify server |
| Dependency | Version mismatch, peer deps | Update/downgrade, check compatibility |

## Output Format

```markdown
## What Happened
[1-2 sentence plain English explanation]

## The Problem
- **File:** `path/to/file.ts:42`
- **Error:** [error message]
- **Type:** [category from table above]

## Why This Happens
[Simple explanation of the root cause]

## How to Fix

### Option 1 (Most Likely)
[Concrete fix with code example]

### Option 2
[Alternative fix if Option 1 doesn't work]

## Prevent This Next Time
- [Tip 1]
- [Tip 2]
```

## Auto-Detection Patterns

| Pattern | Triggers ErrorExplainer |
|---------|------------------------|
| `Error:` or `error:` in output | Yes |
| Stack trace (at File.js:123) | Yes |
| `npm ERR!` | Yes |
| `TypeError`, `SyntaxError`, etc. | Yes |
| Exit code non-zero | Yes |
| `ENOENT`, `EACCES`, etc. | Yes |

## Integration

| With Skill | Purpose |
|------------|---------|
| MAKER | Pause on error, explain, then resume |
| DependencyAuditor | If dependency error, run audit |
| systematic-debugging | For complex multi-step debugging |
