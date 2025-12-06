---
name: design-audit
description: Comprehensive design language audit across entire application. Use this skill to scan all components, pages, and styling files to identify inconsistencies with a design system or theme. Performs parallel analysis of colors, typography, spacing, components, layout, animations, icons, and effects.
license: MIT
model: claude-opus-4-5-20251101
subagent_model: claude-opus-4-5-20251101
---

This skill performs a comprehensive audit of design language consistency across an entire application. It scans all styling-related files and identifies deviations from the established design system.

## Triggers

Use this skill when:
- `DesignAudit` - Full audit with all agents
- `design audit` - Analyze design consistency
- `UI audit` - Check UI patterns
- `style audit` - Scan style usage
- `theme audit` - Verify theme compliance

## File Types to Scan

| Type | Patterns | Purpose |
|------|----------|---------|
| Components | `*.tsx`, `*.jsx` | React component styles |
| Stylesheets | `*.css`, `*.scss`, `*.sass`, `*.less` | CSS definitions |
| Config | `tailwind.config.*`, `theme.*`, `tokens.*` | Design system config |
| Global | `globals.css`, `app.css`, `index.css` | Global styles |
| Styled | `*.styles.ts`, `*.styled.ts` | CSS-in-JS |
| Entry | `index.html`, `_document.*` | Base HTML/meta |
| Constants | `constants.ts`, `config.ts` | Hardcoded values |

## 8-Agent Panel (Parallel Execution)

| Agent | Scans For | Flags |
|-------|-----------|-------|
| **Colors** | `bg-*`, `text-*`, `border-*`, `fill-*`, `stroke-*`, hex codes, rgb/hsl, CSS variables, opacity values | Off-brand colors, inconsistent palettes, poor contrast, hardcoded values |
| **Typography** | `font-*`, `text-*`, `leading-*`, `tracking-*`, font-family declarations, @font-face | Wrong fonts, inconsistent sizes, missing hierarchy, hardcoded px |
| **Spacing** | `p-*`, `m-*`, `gap-*`, `space-*`, width/height values, padding/margin declarations | Inconsistent spacing scale, magic numbers, density issues |
| **Components** | Component patterns, prop interfaces, className usage, variant systems | Inconsistent patterns, missing variants, style duplication |
| **Layout** | `flex`, `grid`, `container`, `columns`, responsive breakpoints, positioning | Broken layouts, inconsistent grids, z-index chaos, overflow issues |
| **Animations** | `transition-*`, `animate-*`, `duration-*`, keyframes, transform, motion | Non-GPU properties, jarring timing, missing states, perf issues |
| **Icons & Assets** | Icon imports, image sources, SVG usage, icon sizes, asset paths | Inconsistent sizing, mixed icon sets, missing alt text |
| **Effects** | `shadow-*`, `rounded-*`, `border-*`, `ring-*`, `blur-*`, `opacity-*` | Inconsistent shadows, border styles, visual hierarchy issues |

## Process

### Phase 1: Discovery

1. Glob all target file types
2. Build component tree/dependency map
3. Extract design token usage
4. Identify design system config

### Phase 2: Analysis (8 Agents Parallel)

Each agent:
1. Scan all files for their domain patterns
2. Build usage inventory (what's used, where, how often)
3. Compare against design spec/tokens
4. Flag violations with severity + location

### Phase 3: Report Generation

1. Aggregate all agent findings
2. Deduplicate cross-agent issues
3. Prioritize by severity + frequency
4. Generate actionable fix list

## Severity Levels

| Level | Symbol | Meaning | Action |
|-------|--------|---------|--------|
| Critical | 🔴 | Breaks design system | Fix immediately |
| Warning | 🟠 | Inconsistent with spec | Should fix |
| Info | 🟡 | Could be improved | Consider fixing |
| Pass | 🟢 | Matches design system | No action |

## Output Format

The audit generates `DESIGN_AUDIT_REPORT.md` with:

```markdown
# Design Audit Report
**Project:** [name]
**Date:** [date]
**Design Spec:** [reference if available]

## Summary
| Category | 🔴 | 🟠 | 🟡 | 🟢 | Score |
|----------|----|----|----|----|-------|
| Colors | X | X | X | X | XX% |
| Typography | X | X | X | X | XX% |
| Spacing | X | X | X | X | XX% |
| Components | X | X | X | X | XX% |
| Layout | X | X | X | X | XX% |
| Animations | X | X | X | X | XX% |
| Icons & Assets | X | X | X | X | XX% |
| Effects | X | X | X | X | XX% |
| **Total** | X | X | X | X | **XX%** |

## Critical Issues (Fix First)
### 🔴 [Issue Title]
- **Files:** `path/to/file.tsx:123`, `path/to/other.tsx:45`
- **Pattern:** `bg-slate-800` (off-brand dark)
- **Expected:** `bg-blue-900` (brand primary)
- **Occurrences:** 15

## Warnings
### 🟠 [Issue Title]
...

## Fix Checklist
- [ ] Replace `bg-slate-800` → `bg-blue-900` (15 files)
- [ ] Update font-family in globals.css
- [ ] Standardize button variants
...
```

## Design Spec Input (Optional)

Provide a design spec for comparison:

```
DESIGN_SPEC:
  colors:
    primary: blue-900
    secondary: blue-600
    success: emerald-600
    warning: amber-500
    error: red-600
    text: slate-800
    muted: slate-500
    background: white, slate-50
  typography:
    font_display: "Inter"
    font_body: "Inter"
    scale: [xs, sm, base, lg, xl, 2xl, 3xl]
  spacing:
    scale: [0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24]
  effects:
    shadows: [sm, md, lg]
    radius: [sm, md, lg, xl, full]
```

## Quick Commands

| Command | Action |
|---------|--------|
| `DesignAudit` | Full audit with all agents |
| `DesignAudit colors` | Colors agent only |
| `DesignAudit typography` | Typography agent only |
| `DesignAudit --fix` | Audit + auto-fix suggestions |
| `DesignAudit --spec=FILE` | Audit against specific design spec |

## Integration with Other Skills

| Combine With | Purpose |
|--------------|---------|
| **MAKER** | Systematic fix execution with verification |
| **AppMap** | Build component inventory first |
| **CodeReview** | Include design checks in PR reviews |
| **A11yAudit** | Combine with contrast + accessibility checks |

## Example Usage

### Full Audit
```
DesignAudit
```

### With Design Spec
```
DesignAudit

DESIGN_SPEC:
  colors:
    primary: blue-900
    background: white
  typography:
    font_display: "Space Grotesk"
```

### Single Category
```
DesignAudit colors
```

## Best Practices

1. **Run after major theme changes** - Catch regressions early
2. **Include in CI/CD** - Automated design consistency checks
3. **Combine with MAKER** - For systematic fixes across many files
4. **Provide design spec** - More accurate violation detection
5. **Fix critical first** - Prioritize 🔴 issues before 🟠

## What This Skill Does NOT Do

- Does not modify files (audit only)
- Does not check business logic
- Does not validate accessibility beyond contrast (use A11yAudit)
- Does not test responsiveness at runtime
