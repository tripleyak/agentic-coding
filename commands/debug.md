# Debug Investigation

Investigate a reported issue or bug.

## Arguments
$ARGUMENTS = issue description (e.g., "button not responding" or "data not saving")

## Instructions

Based on the issue description, investigate:

### 1. Identify Related Code
Search for relevant:
- Components involved
- Event handlers
- State variables
- Service functions

### 2. Trace the Flow
For the identified feature:
- Where does user interaction start?
- What state changes should occur?
- What functions are called?

### 3. Check Common Issues
- Missing dependencies in useEffect/useCallback
- State not updating (stale closure)
- Event handlers not bound correctly
- Async operations not awaited
- Type mismatches

### 4. Suggest Debug Steps
Recommend specific console.logs or breakpoints to add

## Output Format

```
## Debug Investigation: "<issue>"

### Related Code
- Component: <ComponentName> (file:line)
- Handler: <handlerName> (file:line)
- State: <stateName> (file:line)

### Expected Flow
1. User does X
2. Handler Y is called
3. State Z should update
4. Component should re-render

### Potential Causes
1. [LIKELY] <cause description> - Check file:line
2. [POSSIBLE] <cause description>

### Debug Steps
1. Add console.log in <location>: `console.log('debug:', value)`
2. Check if <condition> is true
3. Verify <state> updates correctly

### Quick Fixes to Try
1. <suggestion>
2. <suggestion>
```

Issue to investigate: $ARGUMENTS
