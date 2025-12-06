# Production Build

Run a production build and report results.

## Instructions

1. Run `npm run build`
2. Report build success or failure
3. If successful, check the output folder (dist/ or build/) and report:
   - Total bundle size (sum of all JS files)
   - Largest files
   - Any warnings from the build
4. If build fails, report the errors clearly

## Output Format

```
Build: SUCCESS/FAILED

Bundle Analysis:
- Total JS: X KB
- Main chunk: X KB
- Vendor chunk: X KB

Recommendations:
- <any suggestions based on size or warnings>
```
