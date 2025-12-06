# Find in Codebase

Smart search for components, functions, types, or patterns.

## Arguments
$ARGUMENTS = search term (e.g., "ProductCard", "handleDrop", "UserData")

## Instructions

Search for the term in the following order:

### 1. Component Search
Look for React components with this name:
```bash
grep -r "export const $TERM" --include="*.tsx" -l
grep -r "export function $TERM" --include="*.tsx" -l
```

### 2. Type/Interface Search
Look for type definitions:
```bash
grep -r "interface $TERM" --include="*.ts" --include="*.tsx"
grep -r "type $TERM" --include="*.ts" --include="*.tsx"
```

### 3. Function Search
Look for function definitions:
```bash
grep -r "function $TERM\|const $TERM.*=" --include="*.ts" --include="*.tsx"
```

### 4. Usage Search
Find where it's used:
```bash
grep -r "$TERM" --include="*.ts" --include="*.tsx" -l
```

## Output Format

```
## Search Results: "$TERM"

### Definitions
- components/SomeComponent.tsx:15 - export const SomeComponent
- types.ts:45 - interface SomeComponent

### Usage (X files)
- App.tsx
- components/OtherComponent.tsx
- ...

### Quick Navigation
The main definition is at: <file>:<line>
```

Search term: $ARGUMENTS
