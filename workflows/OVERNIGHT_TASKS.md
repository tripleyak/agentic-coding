# Overnight Autonomous UI/UX + QA/QC Review

**Duration:** 7 hours
**Mode:** Fully autonomous, zero tolerance for errors
**Goal:** Complete visual UI/UX review + comprehensive code QA/QC

---

## Priority 1: Complete Visual UI/UX Audit (Critical)

- [ ] Run VisualQA on entire application
  - Capture screenshots of every route/page
  - Test all viewports (desktop 1920x1080, tablet 768x1024, mobile 375x812)
  - Interactive mode: click every button, open every modal, interact with every form
  - Document all visual issues in VISUAL_QA_REPORT.md
  - Fix any layout breaks, color inconsistencies, typography issues
  - Verify fixes with new screenshots

- [ ] Run DesignAudit on entire codebase
  - Scan all UI components, styles, themes
  - 8-agent parallel analysis (colors, typography, spacing, components, layout, animations, icons, effects)
  - Flag all inconsistencies (🔴 Critical, 🟠 Warning, 🟡 Info)
  - Fix all Critical and Warning issues
  - Update DESIGN_AUDIT_REPORT.md

---

## Priority 2: Comprehensive Code QA/QC (Critical)

- [ ] Run CodeReview on entire codebase
  - Multi-agent review: Security, Performance, Patterns, Quality, A11y/UX
  - Check every file for OWASP vulnerabilities, performance issues, pattern violations
  - Fix all 🔴 Critical and 🟠 Warning issues
  - Document in CODE_REVIEW_REPORT.md

- [ ] Run SecurityAudit
  - Scan for OWASP Top 10 vulnerabilities
  - Check dependencies with npm audit
  - Scan for exposed secrets
  - Fix all Critical and High severity issues

- [ ] Run TestGen for missing coverage
  - Generate E2E tests for all user interactions
  - Generate integration tests for all components
  - Ensure 80%+ coverage on statements, branches, functions
  - All tests must pass

---

## Priority 3: End-to-End Verification (Critical)

- [ ] Run full verification suite
  - `tsc --noEmit` → 0 errors
  - `npm run lint` → 0 errors
  - `npm run test:run` → all pass
  - `npm run build` → success
  - Re-run VisualQA to verify all fixes

- [ ] Generate final reports
  - OVERNIGHT_LOG.md with complete summary
  - SESSION_HANDOFF.md with current state
  - List of all issues found + fixed
  - Screenshots before/after for visual issues

---

## Instructions

**Execution Mode:**
- Use SkillComposer to orchestrate: DesignAudit → VisualQA (interactive) → CodeReview → SecurityAudit → TestGen → MAKER (fix loop) → Verification
- Each skill runs with model: claude-opus-4-5-20251101 for maximum accuracy
- Fix issues immediately after detection (don't batch)
- Commit after each major fix with descriptive message
- If any verification fails, enter MAKER decomposition to fix
- Stop only when: ALL checks pass with 0 errors + all visual issues resolved + all screenshots captured

**Zero Tolerance:**
- TypeScript errors: 0
- Lint errors: 0
- Test failures: 0
- Build errors: 0
- Critical/Warning issues: 0

**Do NOT:**
- Skip any issues (fix everything)
- Make assumptions (verify all fixes)
- Stop early (run full 7 hours or until complete)
- Deploy to production
- Modify .env files with real secrets

**DO:**
- Capture screenshots of EVERY unique view
- Click EVERY interactive element
- Test EVERY user flow
- Fix EVERY issue found
- Verify EVERY fix
- Commit frequently with clear messages
- Update all reports continuously

---

## Success Criteria

✅ Every page/route has screenshots (desktop, tablet, mobile)
✅ Every interactive element tested and working
✅ All visual inconsistencies fixed
✅ All code quality issues resolved
✅ All security vulnerabilities patched
✅ tsc + lint + tests + build all pass with 0 errors
✅ Before/after documentation complete
✅ Git history shows all fixes committed

**DONE = 100% verified complete, not "good enough"**
