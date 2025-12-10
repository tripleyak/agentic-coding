# Create Modal Component

Scaffold a new modal component using the ModalBase component.

## Arguments
$ARGUMENTS = modal name (e.g., "ProductLibraryModal" or "ConfirmDialog")

## Instructions

1. Create the modal file in `components/` directory

2. Use this template that uses the ModalBase component:

```typescript
import React, { useState } from 'react';
import { ModalBase, ModalSize } from './ui/ModalBase';
// Import icons as needed from 'lucide-react'

interface ${ModalName}Props {
  isOpen: boolean;
  onClose: () => void;
  // Add other props as needed
}

export const ${ModalName}: React.FC<${ModalName}Props> = ({
  isOpen,
  onClose,
}) => {
  // Footer content with action buttons
  const footer = (
    <div className="flex justify-end gap-2">
      <button
        onClick={onClose}
        className="px-4 py-2 text-slate-600 hover:bg-slate-100 rounded-lg transition-colors"
      >
        Cancel
      </button>
      <button
        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
      >
        Confirm
      </button>
    </div>
  );

  return (
    <ModalBase
      isOpen={isOpen}
      onClose={onClose}
      title="${ModalTitle}"
      subtitle="Optional subtitle here" // Remove if not needed
      size="lg" // Options: sm, md, lg, xl, 2xl, 3xl, 4xl, 5xl, 6xl, full
      footer={footer}
      // Optional props:
      // headerIcon={<IconComponent size={24} />}
      // headerClassName="bg-gradient-to-r from-blue-600 to-indigo-600" // For gradient headers
      // showCloseButton={true}
      // closeOnBackdropClick={true}
      // closeOnEscape={true}
      // zIndex={50}
    >
      {/* Modal content here */}
      <div className="p-6">
        <p className="text-slate-600">
          Your modal content goes here.
        </p>
      </div>
    </ModalBase>
  );
};
```

3. ModalBase Props Reference:

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `isOpen` | boolean | required | Controls modal visibility |
| `onClose` | () => void | required | Called when modal should close |
| `title` | string | required | Modal title in header |
| `subtitle` | string | - | Optional subtitle below title |
| `size` | ModalSize | 'lg' | Max-width: sm, md, lg, xl, 2xl, 3xl, 4xl, 5xl, 6xl, full |
| `children` | ReactNode | required | Modal body content |
| `footer` | ReactNode | - | Footer content (buttons) |
| `headerIcon` | ReactNode | - | Icon next to title |
| `showCloseButton` | boolean | true | Show X button in header |
| `headerClassName` | string | - | Custom header styling (supports gradients) |
| `overlayClassName` | string | - | Custom overlay styling |
| `contentClassName` | string | - | Custom content container styling |
| `closeOnBackdropClick` | boolean | true | Close on backdrop click |
| `closeOnEscape` | boolean | true | Close on Escape key |
| `zIndex` | number | 50 | Modal z-index |

4. Common Patterns:

**Gradient Header:**
```typescript
headerClassName="bg-gradient-to-r from-blue-600 to-indigo-600"
```

**With Header Icon:**
```typescript
import { Settings } from 'lucide-react';
// ...
headerIcon={<Settings size={24} className="text-white" />}
```

**Full Width Modal:**
```typescript
size="full"
```

**No Footer:**
```typescript
// Simply omit the footer prop
<ModalBase isOpen={isOpen} onClose={onClose} title="Title">
  {/* content */}
</ModalBase>
```

5. Report what was created

Modal name from arguments: $ARGUMENTS
