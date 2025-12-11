# Add Sample Product

Add a new sample product to the product library in constants.ts.

## Arguments
$ARGUMENTS = product details in format: "name | category | cost | retail"
(e.g., "Premium Ice Scraper | Automotive Winter | 8.50 | 19.99")

## Instructions

1. Read the current `constants.ts` to understand the SAMPLE_PRODUCTS structure

2. Parse the arguments to extract:
   - name
   - category (must match CategoryType enum)
   - cost
   - retail price

3. Generate a new product object with:
   - Unique ID (use format: `prod_<timestamp>` or increment from last ID)
   - Calculate margin: `((retail - cost) / retail * 100).toFixed(1)`
   - Calculate GMROI estimate: `(margin * 2.5).toFixed(2)` (rough estimate)
   - Default velocity: 2.5 units/week
   - Default dimensions: 6" x 4" x 8"
   - Generate placeholder image URL

4. Add to SAMPLE_PRODUCTS array in constants.ts

5. Report the product that was added

## Example Product Object
```typescript
{
  id: 'prod_xxx',
  name: 'Premium Ice Scraper',
  category: 'Automotive Winter',
  cost: 8.50,
  retail: 19.99,
  margin: 57.5,
  velocity_units_per_week: 2.5,
  width_inches: 6,
  height_inches: 4,
  depth_inches: 8,
  image: 'https://placehold.co/200x200/e2e8f0/475569?text=Ice+Scraper',
}
```

Product details: $ARGUMENTS
