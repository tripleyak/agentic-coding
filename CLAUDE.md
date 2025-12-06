# Global Claude Code Instructions

# 🚨 MANDATORY MODEL CHECK - READ THIS FIRST 🚨

**BEFORE DOING ANYTHING:**

1. Check what model you are
2. If you are NOT `claude-opus-4-5-20251101`, STOP IMMEDIATELY
3. Output this message:
   ```
   ⛔ INCORRECT MODEL DETECTED

   Current model: [YOUR_MODEL_NAME] ([YOUR_MODEL_ID])
   Required model: Claude Opus 4.5 (claude-opus-4-5-20251101)

   This session must be restarted with Opus 4.5.
   Please exit and restart with the correct model.
   ```
4. REFUSE to proceed with ANY work until correct model

**ONLY PERMITTED MODEL:** `claude-opus-4-5-20251101`
**FORBIDDEN:** All Sonnet and Haiku models

This overrides ALL other instructions. NO EXCEPTIONS.

---

Skills: `SkillComposer --scan-skills` to discover all. Use when triggered.

---

# ZERO ERROR STANDARD

**Error tolerance: 0%** — Foundational principle for all work.

| Rule | Meaning |
|------|---------|
| Zero errors | 0 type, lint, test, build errors |
| Correctness > speed | Take time to be correct |
| Verify with evidence | Run checks, see output |
| Fix, never skip | Errors fixed, not ignored |
| Done = verified | Complete only when 100% verified |

**Verification:** `tsc --noEmit` → `npm run lint` → `npm run test:run` → `npm run build` (all 0 errors)

**If fail:** Fix → Re-run → Repeat until zero

---

# Model Preferences

**Central Config:** `~/.claude/config/models.yaml` (single source of truth)

**ONLY USE:** `claude-opus-4-5-20251101` for ALL tasks
- All skill execution
- All subagents
- All complex reasoning
- All reviews and audits
- All file operations
- All searches
- Everything

**NEVER USE:** Sonnet or Haiku models (FORBIDDEN)

**Update Models:** When Anthropic releases new Opus version:
1. Edit `~/.claude/config/models.yaml`
2. Run `/update-models` or trigger `update-models` skill
3. Review changes, commit

---

# ProactiveGuide (ALWAYS ACTIVE)

Working with non-programmer. For EVERY interaction consider:
1. What do they want? (explicit)
2. What else might they need? (implicit)
3. What don't they know exists? (unknown unknowns)
4. Is this bigger than it sounds?
5. Which skills could help?
6. What could go wrong?
7. Teachable moment?

**Always:** Surface options as lists | Explain WHY | Plain language | Remind of skills | Warn early | Offer simple AND thorough paths

**Style:** `NOT: "debounced handler 300ms" → YES: "Add delay so saves only when you pause typing? (called 'debouncing')"`

**Phrases:** "Before I start, options..." | "You have a skill for this" | "This is bigger than it sounds" | "Quick concept: [term] means..." | "Heads up: could affect..."

`"just do it"` → proceed | `"teach me"` → go deeper

---

# MAKER Framework

Systematic decomposition for complex tasks. **Core:** 99%/step = 37% over 100 steps → MAKER: MAD (atomic) → Verify → Red-Flag

**Decomposition:** Goal → Milestones → Tasks → Steps (atomic, <5min, verifiable)
| Type | Pattern |
|------|---------|
| Coding | By fn/component |
| Data | load→validate→transform→analyze→output |
| Workflow | State transitions |

**Execute:** Propose→Execute→Verify→Record | UNCERTAIN/FAILED→Re-attempt or decompose

**Red-Flags:** Stop on: excessive length, uncertainty, format violations, scope creep

**Auto-Verify:** Stage 1: tsc+lint+test+build (all pass) → Stage 2: 5 Opus review (unanimous) → VERIFIED
**Fallback:** Fail repeatedly → decompose further. Never skip.

---

# Frontend Design

Distinctive UIs, no AI slop. **Triggers:** frontend/UI work

**Design Questions:** Purpose? | Tone (BOLD direction)? | Constraints? | Differentiation?

**Aesthetics:** Brutally minimal | Maximalist | Retro-futuristic | Organic | Luxury | Playful | Industrial | Editorial

**Composition:** Asymmetry, overlap, diagonal flow, grid-breaking | Whitespace OR density (commit)

**Typography FORBIDDEN:** Inter, Roboto, Arial, Helvetica, Open Sans, Lato, system fonts
| Context | Display | Body |
|---------|---------|------|
| Editorial | Playfair Display, Crimson Pro | Source Sans 3, IBM Plex Sans |
| SaaS | Space Grotesk, Bricolage Grotesque | IBM Plex Sans, DM Sans |
| Dev Tools | JetBrains Mono, Cascadia Code | IBM Plex Mono |
| E-commerce | Crimson Pro, Fraunces | Work Sans, General Sans |
| Creative | Bricolage Grotesque, Syne | DM Sans, Outfit |
| Luxury | Cormorant Garamond, Cinzel | Jost, Raleway |

**Rules:** Weight extremes (100-300 vs 700-900), scale 1.333+, fluid `clamp()`

**Color:** OKLCH tokens | Gradient mesh heroes | Noise 0.03 | Glassmorphism cards
**Layering:** Base→Gradient→Accent→Noise(0.02-0.05)→Vignette | 60-30-10, 4.5:1 contrast
**AVOID:** Purple/blue gradients on white, flat #FFF/#000

**Animation:** Only `transform`+`opacity` (GPU) | micro 100-200ms, transitions 200-300ms, page 400-500ms
| Lib | For | Size |
|-----|-----|------|
| Framer Motion | React gestures | 45kb |
| GSAP | Timelines, scroll | 60kb |
| Auto Animate | Zero-config | 2kb |

**3D:** `@react-three/fiber`+`drei`+`postprocessing` | Use: heroes, products | Avoid: forms, mobile-critical

**UI Libs:** shadcn/ui (control) | Aceternity (marketing) | Magic UI (SaaS)
**Effects:** Bento, Spotlight, Glowing border, Shimmer, Background beams, Aurora

**Modern CSS:** `:has()`, Container queries, Nesting, `@layer`, Subgrid, `color-mix()`, View Transitions

**Checklist:** `□ Bold direction □ No forbidden fonts □ OKLCH □ Layered bg □ GPU animations □ Asymmetry □ Premium lib □ No AI look`
**Targets:** LCP <2.5s | FID <100ms | CLS <0.1 | Bundle <200kb | 60fps

---

# DocSync

Autonomous doc sync. **Triggers:** `update docs`, `sync docs`, `DocSync`

| File | Action |
|------|--------|
| CLAUDE.md | Update arch, preserve custom |
| CHANGELOG.md | Add changes, format |
| README.md | Sync stack, commands |
| DEV_PLAN*.md | Mark done, delete stale |
| SESSION_HANDOFF.md | Replace current state |

**Exec:** 3 Opus agents→Audit (✓ACCURATE ⚠OUTDATED ✗OBSOLETE ?MISSING)→Update→Cleanup→Verify

---

# AppMap

Architecture artifacts. **Triggers:** `AppMap`, `generate sitemap`, `map the app` | **Output:** `APP_MAP.md`

**Artifacts:** 1. Sitemap (routes, auth, params) | 2. Workflow (flows, states, API) | 3. Component Dir | 4. UI/UX Diagram
**Exec:** 4 Opus parallel→Synthesize→Validate

---

# CompactMD

Compress CLAUDE.md <1,000 lines. **Triggers:** `CompactMD`, `compact claude.md`

**DENSE:** Deduplicate→Eliminate→Normalize→Symbolize→Evaluate
| Technique | Savings |
|-----------|---------|
| Tables | 40-60% |
| Inline lists | 30-50% |
| Symbols (→✓✗⚠) | 10-20% |
| Example reduction | 50-70% |

---

# PromptGen

Best prompts. **Triggers:** `PromptGen`, `generate prompt`

**Components:** Task✓, Context✓, Persona○, Format✓, Examples○, Constraints○
**Exec:** 3 Opus generate→Cross-review→Vote (clarity 20%, context 15%, format 15%, conciseness 20%, completeness 15%, effectiveness 15%)→Winner

---

# CodeReview

Multi-agent review. **Triggers:** `CodeReview`, `review code`, `PR review`

| Agent | Checks |
|-------|--------|
| Security | OWASP, injection, XSS, auth |
| Performance | O(n), memory, N+1, bundle |
| Patterns | SOLID, DRY, abstractions |
| Quality | Naming, errors, types |
| A11y/UX | ARIA, keyboard, contrast |

**Severity:** 🔴Critical | 🟠Warning | 🟡Suggestion | 🟢Passed
**Pre-checks:** `tsc --noEmit`, `eslint`, `npm run test`, `npm audit`

---

# TestGen

Comprehensive tests. **Triggers:** `TestGen`, `generate tests`, `write tests`

| Layer | Coverage | Tools |
|-------|----------|-------|
| Unit | 80%+ | Vitest, Jest |
| Integration | Key flows | Testing Library |
| E2E | Critical paths | Playwright |

**3 Agents:** Unit | Integration | E2E
**Coverage:** Statements 70%→85%, Branches 65%→80%, Functions 75%→90%

---

# ArchitectPlan

System architecture. **Triggers:** `ArchitectPlan`, `system design`, `architect this`

**ADR:** Status | Context | Decision | Consequences | Alternatives
**4 Agents:** System | Data | API | Infrastructure
**Deliverables:** System diagram, Components, Data flow, API contracts, NFRs (p99<200ms, 99.9% avail)

| Pattern | When |
|---------|------|
| Monolith | MVP, small team |
| Microservices | Scale, complex |
| Event-driven | Async, decoupling |
| CQRS | Read/write asymmetry |

---

# SecurityAudit

Security analysis. **Triggers:** `SecurityAudit`, `security scan`, `check vulnerabilities`

**OWASP Top 10:** Injection, Auth, Data Exposure, XXE, Access, Misconfig, XSS, Deserialization, Components, Logging
**4 Agents:** Code | Dependencies | Config | Infrastructure
**Checks:** `npm audit --production`, secrets scan, headers
**Output:** Risk level, Critical findings, Secrets, Vulns, Headers, Compliance

---

# APIDesign

RESTful/GraphQL APIs. **Triggers:** `APIDesign`, `design API`, `REST design`

**REST:** Resources, HTTP methods, Status codes (200/201/400/401/403/404/500), Versioning, Pagination, Filtering
**Patterns:** HATEOAS, Bulk ops, Partial responses, Idempotency, Rate limiting, ETags
**Output:** OpenAPI 3.0, TypeScript types, Examples, Error format

---

# DevOpsSetup

CI/CD & deployment. **Triggers:** `DevOpsSetup`, `setup CI/CD`, `Docker setup`

**Pipeline:** checkout→npm ci→lint→test:coverage→build→security→deploy
**Docker:** Multi-stage (builder→runner), USER node, EXPOSE 3000
| Platform | Config |
|----------|--------|
| Vercel | vercel.json |
| Railway | railway.json |
| AWS | terraform/, cdk/ |
| Fly.io | fly.toml |

**Monitoring:** Logs (Datadog) | Metrics (Prometheus) | Tracing (OpenTelemetry) | Errors (Sentry)

---

# MobileKit

React Native/Expo. **Triggers:** `MobileKit`, `React Native`, `Expo setup`

**Setup:** `npx create-expo-app@latest --template tabs`
**Libs:** @react-navigation, zustand, react-hook-form, @tanstack/react-query, tamagui, reanimated
**Perf:** FlashList, expo-image, memoization, Hermes, useNativeDriver
**Deploy:** EAS Build, Update, Submit

---

# Refactor

Code improvement. **Triggers:** `Refactor`, `refactor this`, `clean up code`

**Process:** Analyze→Plan→Execute (one at a time, test after)→Verify

| Smell | Fix |
|-------|-----|
| Long fn (>50) | Extract Method |
| Large class (>300) | Extract Class |
| Duplicate | Extract shared |
| Deep nesting (>3) | Early returns |
| Long params (>4) | Parameter Object |

---

# DBSchema

Database design. **Triggers:** `DBSchema`, `database design`, `schema design`

**Process:** Entities→Attributes→Normalize (3NF)→Indexes→Migrations

| Pattern | Use |
|---------|-----|
| Soft delete | `deleted_at TIMESTAMP NULL` |
| Polymorphic | `*_type`, `*_id` |
| Audit | `created_at`, `updated_at` |
| UUID | Distributed |

**Indexes:** B-tree (equality, range) | GIN (full-text, JSON) | GiST (geo)

---

# AuthSystem

Authentication. **Triggers:** `AuthSystem`, `setup auth`, `login system`

| Pattern | For |
|---------|-----|
| Session | Traditional web |
| JWT | API, mobile, SPA |
| OAuth 2.0 | Social login |
| Magic link | Passwordless |
| Passkeys | Modern passwordless |

**JWT:** Access (15m) + Refresh (7d), verify middleware, RBAC
**Checklist:** Hashed passwords, HTTPS, Rate limiting, Lockout, CSRF, Refresh rotation

---

# ErrorHandler

Error handling & logging. **Triggers:** `ErrorHandler`, `error handling`, `logging setup`

**Hierarchy:** AppError→ValidationError(400)→NotFoundError(404)→UnauthorizedError(401)
**Middleware:** Log→Operational? code+message : 500
**Logging:** pino, structured JSON, redact sensitive
**Monitoring:** Sentry | Datadog | LogRocket

---

# A11yAudit

Accessibility/WCAG. **Triggers:** `A11yAudit`, `a11y check`, `WCAG check`

**Level A:** Alt text, Keyboard, No traps, Skip links, Titles, Focus visible, Language
**Level AA:** 4.5:1 contrast, 200% zoom, Focus order, Consistent nav, Error ID
**Testing:** jest-axe, Playwright AxeBuilder
**ARIA:** `aria-label`, `aria-live`, `role="dialog"`, `aria-selected`

---

# PerfOptimize

Performance. **Triggers:** `PerfOptimize`, `optimize performance`, `speed up`

**Vitals:** LCP <2.5s | FID <100ms | CLS <0.1 | TTFB <800ms
**Bundle:** vite-bundle-visualizer, React.lazy, tree shaking, gzip/Brotli
**React:** React.memo, useMemo, useCallback, @tanstack/react-virtual, Suspense
**Images:** WebP/AVIF, srcset, loading="lazy", CDN
**DB:** Eager loading, indexes, pagination, Redis

---

# MonorepoSetup

Monorepo config. **Triggers:** `MonorepoSetup`, `Turborepo setup`, `workspace setup`

| Tool | Config |
|------|--------|
| Turborepo | turbo.json |
| Nx | nx.json |
| pnpm | pnpm-workspace.yaml |

**Structure:** `apps/` (web, mobile, api) + `packages/` (ui, config, utils, types)

---

# ComponentLib

Component libraries. **Triggers:** `ComponentLib`, `design system`, `UI library`

**Structure:** `components/Button/{Button.tsx, .test.tsx, .stories.tsx}` + `tokens/{colors, typography, spacing}`
**Pattern:** CVA variants + VariantProps + Storybook

---

# i18nSetup

Internationalization. **Triggers:** `i18nSetup`, `setup i18n`, `translations`

| Library | Framework |
|---------|-----------|
| next-intl | Next.js |
| react-i18next | React |
| lingui | Any (compile) |

**Best:** Namespace keys, Named params, Intl formatters, RTL

---

# SkillRecommender

146+ skills across 5 sources. **Triggers:** `recommend skill`, `which skill`

| Source | Count | Key Skills |
|--------|-------|------------|
| Custom | 41 | MAKER, SkillComposer, DesignAudit, VisualQA, ProactiveGuide, UpdateModels, OvernightMode, ErrorExplainer, DeploymentGuide, DependencyAuditor, GitWorkflow, FeatureScoper, CostEstimator, BackupSnapshot, ChangelogWriter, EnvManager, APIDocGen |
| Anthropic | 15 | pdf, xlsx, pptx, docx, webapp-testing, mcp-builder, theme-factory |
| Workflows | 60+ | stripe-integration, postgresql, github-actions, k8s-manifest, rag-implementation |
| Superpowers | 20 | brainstorming, systematic-debugging, test-driven-development, parallel-agents, git-worktrees |
| Plugin | 10+ | frontend-design, code-review, hookify, plugin-dev |

**Quick:** Error→ErrorExplainer | Deploy→DeploymentGuide | Packages→DependencyAuditor | Git→GitWorkflow | Plan→FeatureScoper | Costs→CostEstimator | Backup→BackupSnapshot | Changelog→ChangelogWriter | Env→EnvManager | API docs→APIDocGen | Models→UpdateModels | Complex→MAKER | Full audit→SkillComposer | Overnight→OvernightMode | Debug→systematic-debugging | Ideas→brainstorming

---

# SkillCreator

Create skills. **Triggers:** `create skill`, `new skill`

| Match | Action |
|-------|--------|
| >7 | Use existing |
| 5-7 | Ask user |
| <5 | Create new |
| One-off | Just do it |

**Patterns:** Single-phase | Multi-agent parallel | Sequential | Checklist | Generator | Composite
**Quality:** Distinct purpose, 3-5 triggers, Defined I/O, 1-3 phases, Tables > prose

---

# SessionKickoff

Project onboarding. **Triggers:** `kickoff`, `get up to speed`, `new session`, `onboard me`, `catch me up`

| Step | Action |
|------|--------|
| 1 | `codemap .` (if available) |
| 2 | Git status (branch, commits, stashes) |
| 3 | Read: CLAUDE.md→SESSION_KICKOFF.md→BACKLOG.md→APP_MAP.md |
| 4 | Check: uncommitted, PRs, failing tests |
| 5 | Summarize: overview, phase, priorities, blockers |

**Output:** `## Project: [name] | Stack | Phase | State (branch, commit, uncommitted) | Top 3 Priorities | Blockers | Ready to Start`

---

# DesignAudit

Design language audit. **Triggers:** `DesignAudit`, `design audit`, `UI audit`, `style audit`, `theme audit` | **Output:** `DESIGN_AUDIT_REPORT.md`

**Files:** `*.tsx/jsx` | `*.css/scss/sass/less` | `tailwind.config.*`, `theme.*`, `tokens.*` | `globals.css` | `*.styles.ts`

**8-Agent Panel:**
| Agent | Scans | Flags |
|-------|-------|-------|
| Colors | `bg-*`, `text-*`, hex, rgb, CSS vars | Off-brand, inconsistent, poor contrast |
| Typography | `font-*`, `text-*`, @font-face | Wrong fonts, inconsistent sizes |
| Spacing | `p-*`, `m-*`, `gap-*` | Magic numbers, density issues |
| Components | Patterns, className, variants | Inconsistent, missing variants |
| Layout | flex, grid, breakpoints, z-index | Broken layouts, overflow |
| Animations | `transition-*`, `animate-*`, keyframes | Non-GPU, jarring timing |
| Icons | Imports, SVG, sizes | Mixed sets, missing alt |
| Effects | `shadow-*`, `rounded-*`, `border-*` | Inconsistent shadows |

**Process:** Discovery (glob, tree, tokens)→Analysis (8 agents parallel)→Report
**Severity:** 🔴Critical | 🟠Warning | 🟡Info | 🟢Pass
**Commands:** `DesignAudit` | `DesignAudit colors` | `DesignAudit --fix` | `DesignAudit --spec=FILE`

---

# VisualQA

Visual QA with screenshots. **Triggers:** `VisualQA`, `visual QA`, `screenshot audit`, `UI testing` | **Output:** `VISUAL_QA_REPORT.md`

**Process:** CAPTURE (Playwright)→ANALYZE (Claude Vision)→CORRELATE (DesignAudit)
**Checks:** Layout, Colors, Typography, Components, Responsive, Polish
**Viewports:** Desktop (1920x1080) | Tablet (768x1024) | Mobile (375x812)
**Commands:** `VisualQA` | `VisualQA /route` | `VisualQA --mobile` | `VisualQA --interactive` | `VisualQA --compare`
**Prereq:** `npm install -D playwright && npx playwright install chromium`

---

# SkillComposer

Meta-orchestrator. **Triggers:** `SkillComposer`, `compose skills`, `orchestrate`, `auto-solve`, `skill chain` | **Output:** `COMPOSITION_REPORT.md`

**Architecture:** ANALYZER (parse, detect domains)→PLANNER (select, order, handoff)→EXECUTOR (run, pass data, verify)←FEEDBACK LOOP

**Discovery:** `SkillComposer --scan-skills` scans `~/.claude/skills/`, plugins, CLAUDE.md→extracts metadata→updates registry

**Domains:** UI/UX (Frontend, DesignAudit, VisualQA, A11y, ComponentLib) | Testing (TestGen, CodeReview) | Security | Performance | Architecture (ArchitectPlan, AppMap, DBSchema) | DevOps | Data (API, ErrorHandler, i18n) | Auth | Mobile | Meta (MAKER, SkillRecommender, SkillCreator, SkillComposer) | Docs (DocSync, CompactMD, PromptGen) | Session | Code

**Patterns:** Sequential (A→B→C) | Parallel (A→[B,C,D]→E) | Conditional | Iterative | Checkpoint | Dynamic

**Commands:** `SkillComposer: {goal}` | `--plan` | `--dry-run` | `--interactive` | `--resume` | `--scan-skills` | `--domain=X`

**Example Compositions:**
- UI/UX QA: AppMap→[DesignAudit+A11y+CodeReview]→VisualQA→MAKER→TestGen
- Security: SecurityAudit→CodeReview→ErrorHandler→MAKER→SecurityAudit(verify)
- New Feature: ArchitectPlan→DBSchema→APIDesign→Frontend→TestGen→CodeReview

**Config:** mode: autonomous | checkpoints: [] | parallel: true, max 4 | timeout: 30m | max_runtime: 5h | on_fail: retry_until_fixed | require_zero_errors: true | verification: tsc+lint+test+build+CodeReview | stop_when: task_verified_complete

---

# ErrorExplainer

Stack traces to plain English. **Triggers:** `explain error`, `what does this mean`, `help with error`, auto-detect

**Process:** Detect (syntax/runtime/build/dependency/network)→Parse (file, line, code)→Explain→Fix→Prevent
| Category | Fix |
|----------|-----|
| Syntax | Corrected code |
| Type | Null checks |
| Import | Check path, install |
| Build | Fix types |
| Runtime | try/catch |
| Network | URL, headers |
| Dependency | Update/downgrade |

---

# DependencyAuditor

Package audit. **Triggers:** `audit deps`, `check packages`, `update dependencies`, `npm audit`

**Phases:** `npm audit --json` | `npm outdated --json` | `npx depcheck --json` | Report | Update commands
**Severity:** 🔴Critical | 🟠High | 🟡Moderate | 🟢Low

---

# DeploymentGuide

Deployment. **Triggers:** `deploy`, `go live`, `push to production` | **Depends:** DependencyAuditor

**Phases:** Pre-flight (build, tests, types, security, env)→Platform→Configure→Deploy→Verify
| Platform | CLI | Config |
|----------|-----|--------|
| Vercel | `vercel --prod` | vercel.json |
| Railway | `railway up` | railway.json |
| Fly.io | `fly deploy` | fly.toml |

---

# GitWorkflow

Git automation. **Triggers:** `create branch`, `commit changes`, `open PR`, `save my work`

**Branches:** feature/ | fix/ | hotfix/ | refactor/
**Commits:** feat | fix | refactor | docs | chore
> Integrates: `superpowers:using-git-worktrees`, `superpowers:finishing-a-development-branch`

---

# FeatureScoper

Scope planning. **Triggers:** `scope this`, `plan feature`, `before I build`, `what should I consider`

**Phases:** Clarify→Expand (edge cases)→Scope (in/out)→Phase→Document
**Output:** Problem, user story, success criteria, scope, phases, risks

---

# CostEstimator

Cost estimates. **Triggers:** `estimate costs`, `how much will this cost`, `pricing check`

| Service | Examples |
|---------|----------|
| Hosting | Vercel ($0-50), Railway (~$5-20), Fly.io (~$5-15) |
| Database | Supabase ($0-25), PlanetScale ($0-29), Neon ($0-19) |
| Auth | Clerk ($0-25/10K MAU), Auth0 ($0-23), Supabase (free) |
| AI/APIs | OpenAI ($0.03/1K), Gemini (free), Stripe (2.9%) |

**Output:** Summary by tier, breakdown, projections, tips

---

# BackupSnapshot

Restore points. **Triggers:** `backup`, `snapshot`, `save state`, `before I break something`

| Type | When | Command |
|------|------|---------|
| Quick | Small | `git stash push -m "snapshot"` |
| Branch | Refactor | `git branch backup/[timestamp]` |
| Full | Major | Branch + stash + remote |

**Auto:** >10 files, major deps, migrations, before rebase/reset

---

# ChangelogWriter

Changelog from commits. **Triggers:** `update changelog`, `what changed`, `generate changelog`

| Prefix | Section |
|--------|---------|
| feat: | Added |
| fix: | Fixed |
| refactor: | Changed |
| BREAKING: | Breaking |
| test:, chore: | Skip |

---

# EnvManager

Environment files. **Triggers:** `setup env`, `sync env vars`, `check env`, `missing env`

| File | Git |
|------|-----|
| .env.example | ✅ |
| .env.local | ❌ |
| .env.production | ❌ |

**Checks:** Required exist, no empty, no placeholders, no secrets in template

---

# APIDocGen

API docs. **Triggers:** `document API`, `generate docs`, `openapi spec`

| Framework | Pattern |
|-----------|---------|
| Next.js App | `app/**/route.ts` |
| Next.js Pages | `pages/api/**/*.ts` |
| Express | `app.get/post/put/delete()` |
| tRPC | `router.query/mutation()` |

**Output:** OpenAPI 3.0, Markdown, curl/fetch examples

---

# UpdateModels

Model reference updates. **Triggers:** `update models`, `UpdateModels`, `sync models`

**Config:** `~/.claude/config/models.yaml` (single source of truth)

**When Anthropic releases new versions:**
1. Edit `models.yaml` with new identifiers
2. Run `/update-models` or trigger skill
3. Review update plan (12 files, ~20 references)
4. Confirm changes
5. Commit: `git commit -m "chore: update to Opus 4.6"`

**Flags:** `--dry-run` | `--auto` | `--project <path>` | `--model <type>`
**Scans:** skills/, plugins/, workflows/, commands/, CLAUDE.md

---

# OvernightMode

5-hour autonomous. **Triggers:** `overnight`, `run overnight`, `queue tasks`, `work while I sleep`

**Setup:** Create `OVERNIGHT_TASKS.md` with priorities→Run `overnight`→Sleep→Review `OVERNIGHT_LOG.md`

**Task Format:**
```
## Priority 1 (Critical)
- [ ] Fix TypeScript errors
## Priority 2 (Important)
- [ ] SecurityAudit auth
## Instructions
- Commit after each task
- Skip UI changes
```

**Config:** No approval pauses | 30m/skill timeout | 5h max | retry_until_fixed | require_zero_errors | stop_when: task_verified_complete

**Behavior:** Task→Verify (tsc+lint+test+build+CodeReview)→Pass? Log, commit, next : Fix, re-verify (loop) | All done→Stop immediately | 5h→Hard stop, checkpoint

**Completion:** NOT complete until: tsc 0 | lint 0 | tests pass | build succeeds | CodeReview unanimous
**Zero tolerance:** Fix errors, never skip. No "good enough"—only correct or not yet correct.

**Output:** OVERNIGHT_LOG.md | OVERNIGHT_TASKS.md (updated) | SESSION_HANDOFF.md | Git commits

**Safety:** No force push | No destructive DB | No prod deploy | No secret changes | Backup branch created

**Integrates:** SkillComposer, MAKER, BackupSnapshot, GitWorkflow, ErrorExplainer
