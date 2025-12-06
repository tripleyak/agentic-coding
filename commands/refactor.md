# Analyze File for Refactoring

Analyze a specific file and suggest refactoring opportunities.

## Arguments
$ARGUMENTS = file path (e.g., "App.tsx" or "components/MyModal.tsx")

## Instructions

Read the specified file and analyze:

### 1. Size Analysis
- Count total lines
- If >300 lines, suggest how to split it

### 2. State Analysis (for components)
- Count useState hooks
- Identify related states that could be consolidated
- Identify states that could be extracted to custom hooks

### 3. Handler Analysis
- Find handlers without useCallback
- Find inline handlers in JSX

### 4. Duplication Analysis
- Look for repeated patterns that could be extracted

### 5. Dependency Analysis
- What does this file import?
- What imports this file?
- Are there circular dependencies?

## Output Format

```
## Refactoring Analysis: ${filename}

**Size**: X lines (target: <300)
**useState hooks**: X (target: <10 per component)
**Handlers without useCallback**: X

### Suggested Splits
1. Extract ${SectionName} to ${NewFileName} (~X lines)
2. ...

### State Consolidation
- Combine [state1, state2, state3] into single object state

### Extract to Hooks
- ${logicDescription} → use${HookName}

### Missing Memoization
- Line X: ${handlerName} needs useCallback
- Line Y: inline handler should be extracted

### Priority Actions
1. [HIGH] ...
2. [MEDIUM] ...
```

File to analyze: $ARGUMENTS
