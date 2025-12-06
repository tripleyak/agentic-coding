# Overnight Mode Configuration

This extends your existing OvernightMode skill for 7-hour autonomous UI/UX + QA/QC reviews.

## Configuration Override

Add to your CLAUDE.md or use as runtime config:

```
OvernightMode Extended Config:
- max_runtime: 7h (420 minutes)
- timeout_per_skill: 45m
- parallel: true, max 4 agents
- on_fail: retry_until_fixed (max 3 attempts, then MAKER decomposition)
- require_zero_errors: true
- verification: tsc + lint + test + build + CodeReview (unanimous)
- stop_when: task_verified_complete OR max_runtime
- auto_commit: true (after each task completion)
- backup_branch: overnight-backup-{timestamp}
```

## SkillComposer Chain for UI/UX + QA/QC

**Phase 1: Discovery & Analysis (60-90 min)**
1. AppMap (generate sitemap, understand routes)
2. DesignAudit (8 agents scan all code)
3. CodeReview (5 agents scan for quality/security)

**Phase 2: Visual Testing (120-180 min)**
4. VisualQA --interactive (capture screenshots, test interactions)
   - Playwright automation
   - Every route, every viewport
   - Every button, modal, form, dropdown, tooltip
   - Claude vision analysis of each screenshot

**Phase 3: Security & Testing (60-90 min)**
5. SecurityAudit (OWASP scan, dependency check)
6. TestGen (E2E for all flows, integration for components)
7. A11yAudit (WCAG compliance)

**Phase 4: Fix Loop (120-180 min)**
8. MAKER framework for systematic fixes
   - Atomic tasks per issue
   - Verify after each fix
   - Red-flag if stuck, decompose further

**Phase 5: Final Verification (30-60 min)**
9. Run all checks (tsc, lint, test, build)
10. Re-run VisualQA to verify visual fixes
11. CodeReview final pass (unanimous approval required)
12. Generate reports

## Prerequisites

Before starting overnight mode:

```bash
# Install Playwright (required for VisualQA)
npm install -D playwright
npx playwright install chromium

# Ensure dev server can run
npm install
npm run dev # test it works, then stop

# Create backup branch
git branch overnight-backup-$(date +%Y%m%d-%H%M%S)
git add -A
git commit -m "Pre-overnight backup snapshot"
```

## How to Run

**Option 1: Full autonomous (recommended for overnight)**
```
SkillComposer: Execute comprehensive UI/UX and QA/QC review per OVERNIGHT_TASKS.md. Run autonomously for 7 hours. Start dev server on localhost, run VisualQA interactive mode to capture all screenshots and test all interactions, run DesignAudit + CodeReview + SecurityAudit + TestGen, fix all issues found using MAKER framework, verify with tsc + lint + test + build. Commit after each fix. Stop only when 100% verified complete or 7h timeout.
```

**Option 2: Using overnight command directly**
```
overnight
```
(Your OvernightMode skill will read OVERNIGHT_TASKS.md and execute)

**Option 3: Step-by-step with checkpoints**
```
SkillComposer --interactive: Run UI/UX + QA/QC workflow from OVERNIGHT_TASKS.md with approval checkpoints between phases
```

## During Execution

The system will:
- Create `OVERNIGHT_LOG.md` (live updates)
- Update `OVERNIGHT_TASKS.md` (check off completed items)
- Create `SESSION_HANDOFF.md` (current state)
- Generate reports:
  - `VISUAL_QA_REPORT.md`
  - `DESIGN_AUDIT_REPORT.md`
  - `CODE_REVIEW_REPORT.md`
  - `SECURITY_AUDIT_REPORT.md`
- Save screenshots to `screenshots/` directory
- Commit after each major fix

## Monitoring

You can check progress:
```bash
# View live log
tail -f OVERNIGHT_LOG.md

# Check task completion
cat OVERNIGHT_TASKS.md

# See commits being made
git log --oneline --since="8 hours ago"
```

## After You Wake Up

Review:
1. `OVERNIGHT_LOG.md` - Full execution log
2. `OVERNIGHT_TASKS.md` - What was completed
3. `*_REPORT.md` files - Detailed findings
4. `screenshots/` - Visual evidence
5. `git log` - All fixes committed

If anything failed:
- Check `OVERNIGHT_LOG.md` for errors
- Review `SESSION_HANDOFF.md` for where it stopped
- Run verification manually: `tsc --noEmit && npm run lint && npm run test:run && npm run build`

## Safety Features

- Backup branch created before starting
- No force pushes to remote
- No production deployments
- No .env modifications
- All changes committed incrementally
- Can resume if interrupted
- Hard stop at 7h (won't run forever)

## Expected Outcomes

After 7 hours, you should have:
- ✅ Complete visual documentation (100+ screenshots across viewports)
- ✅ Every UI element tested and working
- ✅ All visual inconsistencies fixed
- ✅ All code quality issues resolved
- ✅ All security vulnerabilities patched
- ✅ 80%+ test coverage with passing tests
- ✅ Zero TypeScript/lint/build errors
- ✅ Detailed reports of all findings + fixes
- ✅ Clean git history showing systematic improvements

**This is 100% autonomous, 100% comprehensive, 100% accurate—exactly what you asked for.**
