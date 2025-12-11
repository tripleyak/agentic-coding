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
- ./ShelfComponent
- ./ProductCard

**Types (X)**
- ../types (Product, ShelfData, ...)

**Services (X)**
- ../services/exportService

**Hooks (X)**
- ../hooks/useHistory

### Imported By (X files)
- App.tsx
- components/SellSheetGenerator.tsx
- ...

### Dependency Chain
${filename}
├── ProductCard.tsx
│   └── (no local deps)
├── ShelfComponent.tsx
│   └── types.ts
└── ...

### Potential Issues
- [None found]
- OR: Circular dependency with X
- OR: Deep dependency chain (4+ levels)
```

File to analyze: $ARGUMENTS
