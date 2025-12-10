# Create New Component

Scaffold a new React component following ShelfWins Studio patterns.

## Arguments
$ARGUMENTS = component name (e.g., "ProductLibraryModal" or "CartProductCard")

## Instructions

1. Determine the appropriate location:
   - If it's a modal: `components/` directory
   - If it's a layout component: `components/layout/`
   - If it's a canvas component: `components/canvas/`
   - If it's a common/shared component: `components/common/`

2. Create the component file with this template:

```typescript
import React from 'react';

interface ${ComponentName}Props {
  // Define props here
}

export const ${ComponentName}: React.FC<${ComponentName}Props> = ({
  // Destructure props
}) => {
  return (
    <div>
      {/* Component content */}
    </div>
  );
};
```

3. If it's a component that receives callbacks or is rendered in lists, wrap with `React.memo`:

```typescript
export const ${ComponentName} = React.memo<${ComponentName}Props>(({
  // props
}) => {
  // component
});
```

4. Report what was created and where

Component name from arguments: $ARGUMENTS
