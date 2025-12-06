# Check Import Health

Analyze imports across the codebase for issues.

## Instructions

### 1. Check for Circular Dependencies
Look for files that import each other (A imports B, B imports A).

### 2. Heavy Imports Analysis
Check for large libraries that should be dynamically imported:
- Heavy visualization libraries
- PDF/image processing libraries
- Large utility libraries

### 3. Unused Imports
Run TypeScript compiler to find unused imports:
```bash
npx tsc --noEmit 2>&1 | grep "is declared but"
```

### 4. Duplicate Imports
Check if the same module is imported in different ways across files.

### 5. Barrel Export Check
Look for index.ts files that re-export everything (can hurt tree-shaking).

## Output Format

```
## Import Health Report

### Circular Dependencies
- None found ✓
- OR: A.tsx <-> B.tsx

### Heavy Library Imports
- <library>: <where imported, static or dynamic>

### Unused Imports
- X unused imports found
- <list them>

### Recommendations
1. ...
2. ...
```
