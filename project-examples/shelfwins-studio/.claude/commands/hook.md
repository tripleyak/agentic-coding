# Create Custom Hook

Scaffold a new custom React hook following ShelfWins Studio patterns.

## Arguments
$ARGUMENTS = hook name (e.g., "useLocalStorage" or "useModalManager")

## Instructions

1. Create the hook file in `hooks/` directory
2. Use this template:

```typescript
import { useState, useCallback, useEffect, useRef } from 'react';

/**
 * ${hookName}
 *
 * Description of what this hook does.
 *
 * @example
 * const { value, setValue } = ${hookName}();
 */
export function ${hookName}() {
  // State

  // Callbacks (wrap with useCallback)

  // Effects

  // Return value
  return {
    // exposed state and functions
  };
}
```

3. Ensure all callbacks are wrapped with `useCallback`
4. Ensure all effects have proper dependency arrays
5. Add JSDoc comment explaining usage

Hook name from arguments: $ARGUMENTS
