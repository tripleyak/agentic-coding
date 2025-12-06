# Show File Dependencies

Show what a file imports and what imports it.

## Arguments
$ARGUMENTS = file path (e.g., "components/ProductCard.tsx" or "App.tsx")

## Instructions

### 1. What This File Imports
Parse the import statements at the top of the file:
- External packages (react, lucide-react, etc.)
- Local components
- Types
- Services
- Hooks
- Utils

### 2. What Imports This File
Search for imports of this file:
```bash
grep -r "from.*${filename}" --include="*.ts" --include="*.tsx" -l
```

### 3. Dependency Depth
For each local import, note if it has further local imports (creates a dependency chain).

## Output Format

```
## Dependencies: ${filename}

### This File Imports

**External (X)**
- react
- lucide-react (X icons)
- ...

**Local Components (X)**
- ./ComponentA
- ./ComponentB

**Types (X)**
- ../types (TypeA, TypeB, ...)

**Services (X)**
- ../services/someService

**Hooks (X)**
- ../hooks/useHookName

### Imported By (X files)
- App.tsx
- components/OtherComponent.tsx
- ...

### Dependency Chain
${filename}
├── ComponentA.tsx
│   └── (no local deps)
├── ComponentB.tsx
│   └── types.ts
└── ...

### Potential Issues
- [None found]
- OR: Circular dependency with X
- OR: Deep dependency chain (4+ levels)
```

File to analyze: $ARGUMENTS
