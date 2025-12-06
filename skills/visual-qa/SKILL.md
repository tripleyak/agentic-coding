---
name: visual-qa
description: Comprehensive visual QA and UI testing skill that captures screenshots from localhost, analyzes them with Claude's multimodal vision, and coordinates with DesignAudit for unified code-to-visual design verification. Supports both Puppeteer and Playwright with intelligent tool selection. Supports interactive browser testing, visual regression, and real-world UI/UX validation.
license: MIT
model: claude-opus-4-5-20251101
subagent_model: claude-opus-4-5-20251101
---

# VisualQA Skill

End-to-end visual quality assurance that bridges code analysis with real-world UI rendering. This skill launches a browser against your localhost, captures screenshots, and uses Claude's multimodal capabilities to analyze the actual rendered UI.

**Supports both Puppeteer and Playwright** - Intelligently selects the best tool based on task requirements.

## Triggers

- `VisualQA` - Full visual QA workflow
- `visual QA` - Analyze rendered UI
- `screenshot audit` - Capture and analyze screenshots
- `UI testing` - Test UI in browser
- `visual regression` - Compare visual changes
- `browser testing` - Interact with localhost

## What This Skill Does

```
┌─────────────────────────────────────────────────────────────────┐
│                        VisualQA Workflow                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  0. TOOL SELECT      1. CAPTURE          2. ANALYZE            │
│  ┌──────────┐       ┌──────────┐       ┌──────────┐           │
│  │Puppeteer │       │ Browser  │       │ Claude   │           │
│  │    or    │  ───► │Screenshot│  ───► │ Vision   │           │
│  │Playwright│       │ Capture  │       │ Analysis │           │
│  └──────────┘       └──────────┘       └──────────┘           │
│       │                  │                    │                 │
│       ▼                  ▼                    ▼                 │
│  ┌──────────────────────────────────────────────────┐          │
│  │            3. CORRELATE & REPORT                 │          │
│  │  ┌──────────────┐                                │          │
│  │  │DesignAudit  │ ───► Unified Visual QA Report  │          │
│  │  │  Findings   │      • Visual issues            │          │
│  │  └──────────────┘      • Code-level issues       │          │
│  │                        • Correlation mapping     │          │
│  └──────────────────────────────────────────────────┘          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Tool Selection: Puppeteer vs Playwright

This skill intelligently selects between Puppeteer and Playwright based on task requirements.

### Decision Matrix

| Scenario | Use | Reason |
|----------|-----|--------|
| **Chrome-only testing** | Puppeteer | Lighter, faster, simpler API |
| **Multi-browser testing** | Playwright | Supports Chrome, Firefox, Safari |
| **Simple screenshot capture** | Puppeteer | Less overhead, faster startup |
| **Complex interactions** | Playwright | Better selectors, auto-wait |
| **Network interception** | Puppeteer | Simpler API for network mocking |
| **Mobile device emulation** | Playwright | Better device presets |
| **Trace/debugging** | Playwright | Built-in trace viewer |
| **Parallel execution** | Playwright | Better context isolation |
| **Cross-browser compatibility** | Playwright | Test Firefox/Safari/Edge |
| **PDF generation** | Puppeteer | Native PDF support |
| **Performance testing** | Puppeteer | Lower resource usage |
| **Accessibility testing** | Playwright | Built-in accessibility tools |

### Selection Logic

**Use Puppeteer when:**
- Single browser (Chrome/Chromium) is sufficient
- Performance/speed is critical
- Simple screenshot/scraping tasks
- PDF generation needed
- Minimal dependencies preferred
- Chrome DevTools Protocol features needed

**Use Playwright when:**
- Multi-browser testing required
- Complex user interactions needed
- Accessibility testing important
- Better debugging/tracing needed
- Auto-waiting for elements preferred
- Testing across different browser engines

**Default:** Puppeteer for simple tasks, Playwright for complex/multi-browser scenarios

## Prerequisites

**Option 1: Puppeteer (Lightweight)**
```bash
npm install -D puppeteer
# Chromium auto-downloads
```

**Option 2: Playwright (Full-featured)**
```bash
npm install -D playwright @playwright/test
npx playwright install chromium
```

**Option 3: Both (Recommended)**
```bash
npm install -D puppeteer playwright @playwright/test
npx playwright install chromium
```

## Process

### Phase 0: Tool Selection

Analyze the task and select the appropriate tool:

```javascript
function selectTool(requirements) {
  // Multi-browser requirement → Playwright
  if (requirements.browsers?.length > 1) return 'playwright';

  // Accessibility testing → Playwright
  if (requirements.includeA11y) return 'playwright';

  // Simple screenshots → Puppeteer
  if (requirements.simpleScreenshots) return 'puppeteer';

  // Complex interactions → Playwright
  if (requirements.complexInteractions) return 'playwright';

  // PDF generation → Puppeteer
  if (requirements.generatePDF) return 'puppeteer';

  // Default: Puppeteer (faster for basic tasks)
  return 'puppeteer';
}
```

### Phase 1: Setup & Discovery

1. **Verify localhost is running** (check port)
2. **Identify routes to test** (from router config or APP_MAP.md)
3. **Determine viewport sizes** (desktop, tablet, mobile)
4. **Load design spec** (if available)

### Phase 2: Screenshot Capture

The skill will use either Puppeteer or Playwright based on Phase 0 selection.

#### Option A: Using Puppeteer (Node.js)

```javascript
const puppeteer = require('puppeteer');

const VIEWPORTS = [
  { name: 'desktop', width: 1920, height: 1080 },
  { name: 'tablet', width: 768, height: 1024 },
  { name: 'mobile', width: 375, height: 812 },
];

const ROUTES = ['/', '/dashboard', '/settings'];

async function capturePuppeteer() {
  const browser = await puppeteer.launch({ headless: true });

  for (const viewport of VIEWPORTS) {
    const page = await browser.newPage();
    await page.setViewport({
      width: viewport.width,
      height: viewport.height
    });

    for (const route of ROUTES) {
      await page.goto(`http://localhost:3000${route}`, {
        waitUntil: 'networkidle2'
      });

      // Full page screenshot
      await page.screenshot({
        path: `/tmp/screenshots/${viewport.name}${route.replace(/\//g, '_')}.png`,
        fullPage: true
      });
    }

    await page.close();
  }

  await browser.close();
}
```

#### Option B: Using Playwright (Node.js)

```javascript
const { chromium } = require('playwright');

const VIEWPORTS = [
  { name: 'desktop', width: 1920, height: 1080 },
  { name: 'tablet', width: 768, height: 1024 },
  { name: 'mobile', width: 375, height: 812 },
];

const ROUTES = ['/', '/dashboard', '/settings'];

async function capturePlaywright() {
  const browser = await chromium.launch({ headless: true });

  for (const viewport of VIEWPORTS) {
    const context = await browser.newContext({
      viewport: { width: viewport.width, height: viewport.height }
    });
    const page = await context.newPage();

    for (const route of ROUTES) {
      await page.goto(`http://localhost:3000${route}`);
      await page.waitForLoadState('networkidle');

      // Full page screenshot
      await page.screenshot({
        path: `/tmp/screenshots/${viewport.name}${route.replace(/\//g, '_')}.png`,
        fullPage: true
      });
    }

    await context.close();
  }

  await browser.close();
}
```

#### Option C: Using Playwright (Python)

```python
from playwright.sync_api import sync_playwright

VIEWPORTS = [
    {"name": "desktop", "width": 1920, "height": 1080},
    {"name": "tablet", "width": 768, "height": 1024},
    {"name": "mobile", "width": 375, "height": 812},
]

ROUTES = ["/", "/dashboard", "/settings"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for viewport in VIEWPORTS:
        context = browser.new_context(
            viewport={"width": viewport["width"], "height": viewport["height"]}
        )
        page = context.new_page()

        for route in ROUTES:
            page.goto(f"http://localhost:3000{route}")
            page.wait_for_load_state("networkidle")

            page.screenshot(
                path=f"/tmp/screenshots/{viewport['name']}{route.replace('/', '_')}.png",
                full_page=True
            )

        context.close()
    browser.close()
```

### Phase 3: Visual Analysis (Claude Vision)

Each screenshot is analyzed by Claude's multimodal capabilities:

**Analysis Checklist:**
| Category | What to Check |
|----------|---------------|
| **Layout** | Alignment, spacing, overflow, z-index issues, broken grids |
| **Typography** | Font rendering, size hierarchy, line height, truncation |
| **Colors** | Brand consistency, contrast, color bleeding, transparency |
| **Components** | Button states, form elements, icons, cards, modals |
| **Responsiveness** | Content reflow, hidden elements, touch targets |
| **Visual Polish** | Shadows, borders, gradients, animations frozen state |
| **Content** | Placeholder text, missing images, Lorem ipsum |
| **Accessibility** | Focus indicators, color contrast, text size |

**Analysis Prompt Template:**
```
Analyze this screenshot of [PAGE_NAME] at [VIEWPORT] viewport.

Design Spec Reference:
- Primary color: blue-900
- Background: white/slate-50
- Typography: [font family]

Check for:
1. Layout issues (alignment, spacing, overflow)
2. Color consistency with design spec
3. Typography hierarchy and readability
4. Component rendering issues
5. Visual polish problems
6. Accessibility concerns (contrast, focus)
7. Responsive behavior issues
8. Any visual bugs or anomalies

For each issue found, provide:
- Severity (Critical/Warning/Info)
- Location (describe where on screen)
- Description of the issue
- Suggested fix
```

### Phase 4: Interactive Testing (Optional)

For dynamic UI elements, both tools support interaction testing.

#### Puppeteer Interactive Examples

```javascript
// Test modal opening
await page.click('[data-testid="open-modal"]');
await page.waitForSelector('[role="dialog"]');
await page.screenshot({ path: '/tmp/screenshots/modal-open.png' });

// Test hover states
await page.hover('button.primary');
await page.screenshot({ path: '/tmp/screenshots/button-hover.png' });

// Test form validation
await page.type('[name="email"]', 'invalid-email');
await page.click('[type="submit"]');
await page.waitForTimeout(300);
await page.screenshot({ path: '/tmp/screenshots/form-error.png' });

// Test dropdown
await page.click('[data-testid="dropdown-trigger"]');
await page.waitForSelector('[role="listbox"]');
await page.screenshot({ path: '/tmp/screenshots/dropdown-open.png' });

// Test dark mode
await page.click('[data-testid="theme-toggle"]');
await page.waitForTimeout(300);
await page.screenshot({ path: '/tmp/screenshots/dark-mode.png' });
```

#### Playwright Interactive Examples

```javascript
// Test modal opening
await page.click('[data-testid="open-modal"]');
await page.waitForSelector('[role="dialog"]');
await page.screenshot({ path: '/tmp/screenshots/modal-open.png' });

// Test hover states (auto-waits)
const button = page.locator('button.primary');
await button.hover();
await page.screenshot({ path: '/tmp/screenshots/button-hover.png' });

// Test form validation
await page.fill('[name="email"]', 'invalid-email');
await page.click('[type="submit"]');
await page.screenshot({ path: '/tmp/screenshots/form-error.png' });

// Test dropdown
await page.click('[data-testid="dropdown-trigger"]');
await page.waitForSelector('[role="listbox"]');
await page.screenshot({ path: '/tmp/screenshots/dropdown-open.png' });

// Test dark mode
await page.click('[data-testid="theme-toggle"]');
await page.waitForTimeout(300);
await page.screenshot({ path: '/tmp/screenshots/dark-mode.png' });
```

### Phase 5: Correlation with DesignAudit

Cross-reference visual findings with code-level issues:

```markdown
## Correlation Report

### Issue: Button has wrong background color
- **Visual Finding:** Screenshot shows button with slate-800 background
- **Code Finding:** `components/Button.tsx:45` uses `bg-slate-800`
- **Fix:** Change to `bg-blue-900`
- **Files to Update:** 1

### Issue: Inconsistent card shadows
- **Visual Finding:** Some cards have shadows, others don't
- **Code Finding:** Mixed usage of `shadow-md` and `shadow-lg` across 5 files
- **Fix:** Standardize to `shadow-card` token
- **Files to Update:** 5
```

## Output Format

### VISUAL_QA_REPORT.md

```markdown
# Visual QA Report

**Project:** [name]
**Date:** [date]
**Tool Used:** Puppeteer/Playwright
**Localhost:** http://localhost:[port]
**Routes Tested:** [count]
**Screenshots Captured:** [count]
**Browser:** Chrome/Chromium [version]

## Summary

| Viewport | Routes | Issues | Critical | Warning | Info |
|----------|--------|--------|----------|---------|------|
| Desktop  | 12     | 8      | 2        | 4       | 2    |
| Tablet   | 12     | 15     | 5        | 7       | 3    |
| Mobile   | 12     | 22     | 8        | 10      | 4    |

## Critical Issues

### 🔴 [Issue Title]
**Route:** /dashboard
**Viewport:** Mobile (375px)
**Screenshot:** `screenshots/mobile_dashboard.png`
**Location:** Bottom navigation bar
**Description:** Navigation bar overlaps content, cutting off last item
**Visual Evidence:** [Screenshot with annotation]
**Related Code:** `components/BottomNav.tsx:89` - missing `safe-area-inset`
**Fix:** Add `pb-safe` or `env(safe-area-inset-bottom)`

### 🔴 [Issue Title]
...

## Warnings

### 🟠 [Issue Title]
...

## By Route

### / (Homepage)
| Viewport | Status | Issues |
|----------|--------|--------|
| Desktop  | ⚠️     | 2 warnings |
| Tablet   | ✅     | Clean |
| Mobile   | 🔴     | 1 critical |

**Desktop Issues:**
- 🟠 Hero text contrast too low on gradient background
- 🟠 CTA button too close to edge

**Mobile Issues:**
- 🔴 Hamburger menu doesn't open (JS error?)

### /dashboard
...

## Responsive Breakpoint Analysis

| Breakpoint | Width | Issues Found |
|------------|-------|--------------|
| sm         | 640px | Content overflow in sidebar |
| md         | 768px | Clean |
| lg         | 1024px | Clean |
| xl         | 1280px | Excessive whitespace |

## Component State Testing

| Component | Default | Hover | Active | Disabled | Focus |
|-----------|---------|-------|--------|----------|-------|
| Button    | ✅      | ✅    | ✅     | 🟠       | 🔴    |
| Input     | ✅      | ✅    | ✅     | ✅       | ✅    |
| Card      | ✅      | 🟠    | N/A    | N/A      | N/A   |
| Modal     | ✅      | N/A   | N/A    | N/A      | 🔴    |

## Correlation with DesignAudit

| Visual Issue | Code Location | Root Cause |
|--------------|---------------|------------|
| Wrong button color | Button.tsx:45 | Uses `bg-slate-800` instead of `bg-blue-900` |
| Missing focus ring | globals.css:12 | No `:focus-visible` styles |
| Card shadow inconsistent | Card.tsx:23 | Hardcoded `shadow-lg` instead of token |

## Fix Priority

### Immediate (Critical)
- [ ] Fix mobile navigation overlap
- [ ] Add focus indicators to buttons
- [ ] Fix modal backdrop z-index

### Soon (Warning)
- [ ] Improve hero text contrast
- [ ] Standardize card shadows
- [ ] Fix disabled button opacity

### Later (Info)
- [ ] Reduce whitespace on xl screens
- [ ] Add hover states to cards

## Screenshots

All screenshots saved to: `/tmp/visual-qa-[timestamp]/`

| Route | Desktop | Tablet | Mobile |
|-------|---------|--------|--------|
| / | [link] | [link] | [link] |
| /dashboard | [link] | [link] | [link] |
| ... | ... | ... | ... |
```

## Quick Commands

| Command | Action |
|---------|--------|
| `VisualQA` | Full audit (all routes, all viewports) |
| `VisualQA /dashboard` | Single route audit |
| `VisualQA --mobile` | Mobile viewport only |
| `VisualQA --interactive` | Include interaction testing |
| `VisualQA --compare` | Compare with DesignAudit findings |
| `VisualQA --regression` | Compare with previous screenshots |

## Configuration

Provide configuration for customization:

```yaml
VISUAL_QA_CONFIG:
  localhost: http://localhost:3000
  routes:
    - /
    - /dashboard
    - /settings
    - /profile
  viewports:
    - name: desktop
      width: 1920
      height: 1080
    - name: tablet
      width: 768
      height: 1024
    - name: mobile
      width: 375
      height: 812
  interactions:
    - selector: '[data-testid="theme-toggle"]'
      action: click
      name: dark-mode
    - selector: '[data-testid="menu-button"]'
      action: click
      name: menu-open
  design_spec:
    primary: blue-900
    background: white
    font: "Inter"
  exclude_routes:
    - /admin/*
    - /api/*
```

## Integration with Other Skills

| Skill | Integration |
|-------|-------------|
| **DesignAudit** | Correlate code issues with visual bugs |
| **MAKER** | Systematic fix execution |
| **A11yAudit** | Combine with accessibility checks |
| **webapp-testing** | Leverages Playwright infrastructure |
| **ui-visual-validator** | Uses visual analysis patterns |
| **e2e-testing-patterns** | Follows E2E best practices |

## Workflow Example

```
1. Start dev server
   $ npm run dev

2. Run VisualQA
   > VisualQA

3. Review report
   → VISUAL_QA_REPORT.md generated
   → Screenshots in /tmp/visual-qa-[timestamp]/

4. Run DesignAudit for code correlation
   > DesignAudit --compare

5. Fix issues with MAKER
   > MAKER: Fix all critical visual issues from VISUAL_QA_REPORT.md
```

## Best Practices

1. **Run after major UI changes** - Catch visual regressions early
2. **Test all viewports** - Mobile issues are often missed
3. **Include interaction states** - Hover, focus, active, error states
4. **Correlate with code** - Connect visual bugs to source files
5. **Save baseline screenshots** - For future regression comparison
6. **Test both themes** - If you have light/dark mode
7. **Check edge cases** - Empty states, long content, RTL

## Limitations

- Requires localhost to be running
- Cannot test authentication-protected routes without login handling
- Screenshot timing may miss animations
- Cannot detect performance issues (use Lighthouse)
- Does not replace user testing

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Screenshots blank | Wait for `networkidle`, increase timeout |
| Missing dynamic content | Add explicit waits for selectors |
| Auth-protected routes | Add login step before capture |
| Wrong viewport | Verify context viewport settings |
| Animations mid-frame | Use `page.wait_for_timeout(500)` |
