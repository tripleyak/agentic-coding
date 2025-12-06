# Project Health Status

Show overall project health and status.

## Instructions

Gather and display:

### 1. Git Status
- Current branch
- Uncommitted changes (count files)
- Last commit message and time

### 2. Dependencies
- Run `npm outdated` to check for outdated packages (just report count)

### 3. Code Metrics (quick estimates)
- Count lines in main entry file (App.tsx, index.tsx, or similar)
- Count component files: `ls components/*.tsx 2>/dev/null | wc -l`
- Count TODO/FIXME comments: `grep -r "TODO\|FIXME" --include="*.tsx" --include="*.ts" | wc -l`

### 4. Build Status
- Check if dist/ or build/ folder exists and when it was last built
- Or note if no build exists

## Output Format

```
## Project Status

### Git
Branch: <branch-name>
Changes: X files modified
Last commit: "<message>" (X hours ago)

### Code Health
Main entry: X lines (target: <500)
Components: X files
TODOs: X items

### Dependencies
Outdated packages: X

### Build
Last build: <timestamp> or "No build found"
```
