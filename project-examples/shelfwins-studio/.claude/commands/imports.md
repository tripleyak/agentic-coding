# Check Import Health

Analyze imports across the codebase for issues.

## Instructions

### 1. Check for Circular Dependencies
Look for files that import each other (A imports B, B imports A).

### 2. Heavy Imports Analysis
Check these specific imports that should be dynamic:
- `html2canvas` - Should only be imported in exportService.ts, and ideally dynamically
- `jspdf` - Should only be imported in exportService.ts, and ideally dynamically
- `@google/genai` - Check where it's imported

### 3. Unused Imports
Run TypeScript compiler to find unused imports:
```bash
npx tsc --noEmit 2>&1 | grep "is declared but"
```

### 4. Duplicate Icon Imports
Check if lucide-react icons are imported in multiple places that could be consolidated.

### 5. Barrel Export Check
Look for index.ts files that re-export everything (can hurt tree-shaking).

## Output Format

```
## Import Health Report

### Circular Dependencies
- None found ✓
- OR: A.tsx <-> B.tsx

### Heavy Library Imports
- html2canvas: <where imported, static or dynamic>
- jspdf: <where imported, static or dynamic>

### Unused Imports
- X unused imports found
- <list them>

### Recommendations
1. ...
2. ...
```
