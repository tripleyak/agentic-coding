# Add Retailer Profile

Add a new retailer profile to types.ts.

## Arguments
$ARGUMENTS = retailer details in format: "name | color | categories"
(e.g., "Costco | #e31837 | Bulk Items, Home Goods, Electronics")

## Instructions

1. Read `types.ts` to find the RETAILER_PROFILES object

2. Parse the arguments:
   - name: Retailer display name
   - color: Primary brand color (hex)
   - categories: Comma-separated list of focus categories

3. Generate retailer key (lowercase, underscores): "Costco" → "costco"

4. Add new RetailerProfile with defaults:
   ```typescript
   costco: {
     name: 'Costco',
     primaryColor: '#e31837',
     categoryFocus: ['Bulk Items', 'Home Goods', 'Electronics'],
     preferredMarginMin: 0.25,  // 25% default
     preferredGMROIMin: 2.0,    // $2.00 default
     preferredIncoterms: ['DDP', 'DAP'],
   },
   ```

5. Add to RetailerType enum if not exists

6. Report what was added

Retailer details: $ARGUMENTS
