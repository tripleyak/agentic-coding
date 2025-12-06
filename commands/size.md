# Bundle Size Report

Analyze bundle size and compare to targets.

## Instructions

1. Check if a build exists:
   ```bash
   ls -la dist/assets/*.js 2>/dev/null || ls -la build/static/js/*.js 2>/dev/null
   ```

2. If no build exists, run one:
   ```bash
   npm run build
   ```

3. Analyze the output:
   ```bash
   # List all JS files with sizes
   ls -lh dist/assets/*.js 2>/dev/null || ls -lh build/static/js/*.js 2>/dev/null

   # Get total size
   du -sh dist/assets/ 2>/dev/null || du -sh build/static/js/ 2>/dev/null
   ```

4. Compare against common targets:
   - Initial bundle target: <500KB
   - Total target: <1MB with lazy loading

## Output Format

```
## Bundle Size Report

### Current Size
| File | Size | Status |
|------|------|--------|
| index-xxxxx.js | 450KB | ✓ OK |
| vendor-xxxxx.js | 300KB | ⚠️ Large |
| ... | ... | ... |

**Total**: X KB

### vs. Targets
- Initial bundle: X KB (target: <500KB) [✓/⚠️/❌]
- Vendor chunks: X KB
- App code: X KB

### Recommendations
- <specific recommendations based on size>
```
