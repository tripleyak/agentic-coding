# Show Code TODOs

Extract and display all TODO, FIXME, and HACK comments from the codebase.

## Instructions

Search for TODO-style comments:

```bash
grep -rn "TODO\|FIXME\|HACK\|XXX" --include="*.ts" --include="*.tsx" .
```

## Output Format

Group by type and show with file locations:

```
## Code TODOs

### FIXME (High Priority) - X items
- [ ] App.tsx:234 - Fix memory leak in drag handler
- [ ] ...

### TODO (Normal Priority) - X items
- [ ] components/ShelfComponent.tsx:89 - Add animation
- [ ] ...

### HACK (Tech Debt) - X items
- [ ] services/exportService.ts:45 - Workaround for jsPDF bug
- [ ] ...

### Summary
Total: X items (Y FIXME, Z TODO, W HACK)
```

If no TODOs found, report "No TODO comments found in codebase."
