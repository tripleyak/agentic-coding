# A11yAudit Skill

Accessibility/WCAG. **Triggers:** `A11yAudit`, `a11y check`, `WCAG check`

**Level A:** Alt text, Keyboard accessible, No traps, Skip links, Page titles, Focus visible, Language
**Level AA:** 4.5:1 contrast, 200% zoom, Focus order, Consistent nav, Error ID

**Testing:** jest-axe, Playwright AxeBuilder

| Fix | Solution |
|-----|----------|
| Missing alt | Descriptive or `alt=""` |
| Low contrast | 4.5:1 minimum |
| No focus | `:focus-visible` styles |
| Click-only | Add onKeyDown |

**ARIA:** `aria-label`, `aria-live`, `role="dialog"`, `aria-selected`
