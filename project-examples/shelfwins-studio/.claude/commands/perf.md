# Performance Audit

Analyze the codebase for performance issues.

## Instructions

Check for these issues and report findings with file:line references:

### 1. Large Components (>300 lines)
Search for component files and count lines. Flag any over 300 lines.

### 2. Missing useCallback
Look in App.tsx for event handler functions (functions starting with `handle` or arrow functions assigned to const) that are NOT wrapped in useCallback.

### 3. Inline Arrow Functions in JSX
Search for patterns like `onClick={() =>` in JSX that should be extracted.

### 4. Missing React.memo
Check ShelfComponent.tsx, ProductCard.tsx, and other frequently-rendered components for React.memo usage.

### 5. Heavy Imports on Critical Path
Check if html2canvas and jspdf are imported at module level (should be dynamic imports).

### 6. Code Splitting
Check if React.lazy is used for modal components.

## Output Format

```
## Performance Audit Results

### Critical Issues
- [ISSUE]: Description (file:line)

### Warnings
- [WARNING]: Description (file:line)

### Passed Checks
- ✓ Check name

### Recommendations
1. Specific action to take
2. ...
```
