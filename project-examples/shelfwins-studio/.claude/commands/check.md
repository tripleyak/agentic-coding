# Type Check & Lint

Run TypeScript compiler and check for errors.

## Instructions

1. Run TypeScript compiler in check mode:
   ```bash
   npx tsc --noEmit
   ```

2. Report results:
   - If no errors: "TypeScript: ✓ No errors"
   - If errors: List each error with file:line and message

3. Check for any ESLint config and run if available:
   ```bash
   npx eslint . --ext .ts,.tsx 2>/dev/null || echo "No ESLint configured"
   ```

## Output Format

```
## Type Check Results

### TypeScript
✓ No errors
OR
❌ X errors found:
- file.tsx:line: error message
- ...

### ESLint
✓ No issues
OR
⚠️ X warnings, Y errors
- ...

### Summary
[PASS/FAIL] - Ready to commit: [Yes/No]
```
