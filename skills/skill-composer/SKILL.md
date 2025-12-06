---
name: skill-composer
description: Global meta-orchestration skill that autonomously analyzes any task, selects optimal skills from the complete skill registry, and executes them in sequence with minimal user intervention. Acts as an AI conductor that composes multiple skills into coherent workflows to solve complex, multi-domain problems. Supports auto-discovery of new skills.
license: MIT
model: claude-opus-4-5-20251101
subagent_model: claude-opus-4-5-20251101
---

# SkillComposer

A global autonomous meta-skill that orchestrates **all available skills** to solve any complex task. Given a high-level goal, SkillComposer analyzes the problem, auto-detects domains, selects optimal skills from the complete registry, determines execution order, and runs them autonomously with intelligent handoffs between phases. Enforces **zero error standard** — retries until fixed, verifies before complete, stops when verified done.

## Triggers

- `SkillComposer: {goal}` - Full autonomous orchestration
- `compose skills` - Multi-skill workflow
- `orchestrate` - Autonomous task execution
- `auto-solve` - Hands-off problem solving
- `skill chain` - Sequential skill execution

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           SKILL COMPOSER                                         │
│                   Global Autonomous Orchestration Engine                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌────────────────┐   ┌────────────────┐   ┌────────────────┐                  │
│  │ SKILL SCANNER  │   │    ANALYZER    │   │    PLANNER     │                  │
│  │                │   │                │   │                │                  │
│  │ • Discover new │──▶│ • Parse goal   │──▶│ • Select skills│                  │
│  │   skills       │   │ • Detect       │   │ • Order deps   │                  │
│  │ • Update       │   │   domains      │   │ • Plan handoffs│                  │
│  │   registry     │   │ • Match skills │   │ • Set checkpts │                  │
│  └────────────────┘   └────────────────┘   └────────────────┘                  │
│                                                   │                             │
│                                                   ▼                             │
│                              ┌────────────────────────────────┐                │
│                              │          EXECUTOR              │                │
│                              │                                │                │
│                              │  • Run skills (seq/parallel)   │                │
│                              │  • Pass data between skills    │                │
│                              │  • Retry until fixed (0 errors)│                │
│                              │  • Verify before complete      │                │
│                              └────────────────────────────────┘                │
│                                           │                                     │
│                                           ▼                                     │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                         FEEDBACK LOOP                                    │   │
│  │  • Monitor execution    • Detect failures     • Retry until fixed       │   │
│  │  • Adjust plan          • Inject new skills   • Re-prioritize           │   │
│  │  • Verify before done   • Zero error standard • Stop when verified      │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Skill Auto-Discovery

SkillComposer can scan for and discover new skills automatically.

### Discovery Workflow

```
SkillComposer --scan-skills
```

**Process:**
1. Scan `~/.claude/skills/*/SKILL.md` for local skills
2. Scan `~/.claude/plugins/**/skills/*/SKILL.md` for plugin skills
3. Parse CLAUDE.md for inline skill definitions
4. Extract metadata: name, triggers, domains, inputs, outputs
5. Update internal SKILL_REGISTRY
6. Report new/changed skills

**Output:**
```
SKILL SCAN COMPLETE
├─ Total Skills Found: 32
├─ New Skills: 4
│   ├─ NewSkill1 (domains: [testing, backend])
│   ├─ NewSkill2 (domains: [UI, animations])
│   └─ ...
├─ Updated Skills: 2
└─ Registry Updated ✅
```

### Skill Metadata Extraction

When scanning a skill, SkillComposer extracts:

```yaml
SKILL_ENTRY:
  name: "SkillName"
  source: "~/.claude/skills/skill-name/SKILL.md"
  triggers: ["trigger1", "trigger2"]
  domains: [domain1, domain2]
  type: analyzer | executor | generator | validator
  inputs:
    - type: file
      pattern: "*.tsx"
    - type: config
      name: "DESIGN_SPEC"
  outputs:
    - REPORT.md
    - generated_files/
  requires:
    - localhost_running
    - playwright
  integrates_with: [Skill1, Skill2]
```

---

## Complete Skill Registry

SkillComposer has access to **90+ skills** across multiple sources. Run `--scan-skills` to discover all.

### Skill Sources

| Source | Location | Count |
|--------|----------|-------|
| Custom Skills | `~/.claude/skills/` | 5 |
| anthropic-agent-skills | `~/.claude/plugins/marketplaces/anthropic-agent-skills/` | 15 |
| claude-code-plugins | `~/.claude/plugins/marketplaces/claude-code-plugins/` | 10 |
| claude-code-workflows | `~/.claude/plugins/marketplaces/claude-code-workflows/` | 60+ |
| superpowers | `~/.claude/plugins/cache/superpowers/` | 14 |

### Domain: UI/UX & Design

| Skill | Source | Purpose |
|-------|--------|---------|
| **Frontend Design** | custom/anthropic | Distinctive UI creation |
| **DesignAudit** | custom | Code-level design issues |
| **VisualQA** | custom | Screenshot-based visual QA |
| **A11yAudit** | custom | Accessibility compliance |
| **ComponentLib** | custom | Design system creation |
| **theme-factory** | anthropic | Theme generation |
| **canvas-design** | anthropic | Canvas/graphic design |
| **brand-guidelines** | anthropic | Brand system creation |
| **algorithmic-art** | anthropic | Generative art |

### Domain: Documents & Files

| Skill | Source | Purpose |
|-------|--------|---------|
| **pdf** | anthropic | PDF generation/manipulation |
| **xlsx** | anthropic | Excel file operations |
| **pptx** | anthropic | PowerPoint generation |
| **docx** | anthropic | Word document generation |

### Domain: Testing & QA

| Skill | Source | Purpose |
|-------|--------|---------|
| **TestGen** | custom | Test generation |
| **webapp-testing** | anthropic | Browser-based testing |
| **e2e-testing-patterns** | workflows | E2E test strategies |
| **javascript-testing-patterns** | workflows | JS test patterns |
| **python-testing-patterns** | workflows | Python test patterns |
| **bats-testing-patterns** | workflows | Shell script testing |
| **test-driven-development** | superpowers | TDD methodology |
| **testing-anti-patterns** | superpowers | What to avoid |

### Domain: Code Quality & Review

| Skill | Source | Purpose |
|-------|--------|---------|
| **CodeReview** | custom | Multi-agent code review |
| **Refactor** | custom | Code improvement |
| **code-review-excellence** | workflows | Review best practices |
| **receiving-code-review** | superpowers | Handle feedback |
| **requesting-code-review** | superpowers | Request reviews |

### Domain: Security

| Skill | Source | Purpose |
|-------|--------|---------|
| **SecurityAudit** | custom | Vulnerability scanning |
| **AuthSystem** | custom | Authentication impl |
| **auth-implementation-patterns** | workflows | Auth patterns |
| **sast-configuration** | workflows | Static analysis |
| **solidity-security** | workflows | Smart contract security |
| **pci-compliance** | workflows | Payment security |
| **secrets-management** | workflows | Secrets handling |
| **defense-in-depth** | superpowers | Security layers |

### Domain: Backend & API

| Skill | Source | Purpose |
|-------|--------|---------|
| **APIDesign** | custom | REST/GraphQL design |
| **api-design-principles** | workflows | API best practices |
| **fastapi-templates** | workflows | FastAPI scaffolding |
| **nodejs-backend-patterns** | workflows | Node.js patterns |
| **architecture-patterns** | workflows | Backend architecture |
| **microservices-patterns** | workflows | Microservices |
| **error-handling-patterns** | workflows | Error handling |

### Domain: Database

| Skill | Source | Purpose |
|-------|--------|---------|
| **DBSchema** | custom | Database design |
| **postgresql** | workflows | Postgres patterns |
| **database-migration** | workflows | DB migrations |
| **sql-optimization-patterns** | workflows | Query optimization |

### Domain: DevOps & Infrastructure

| Skill | Source | Purpose |
|-------|--------|---------|
| **DevOpsSetup** | custom | CI/CD configuration |
| **github-actions-templates** | workflows | GitHub Actions |
| **gitlab-ci-patterns** | workflows | GitLab CI |
| **deployment-pipeline-design** | workflows | Pipeline design |
| **terraform-module-library** | workflows | Infrastructure as code |
| **multi-cloud-architecture** | workflows | Multi-cloud |
| **cost-optimization** | workflows | Cloud costs |

### Domain: Kubernetes

| Skill | Source | Purpose |
|-------|--------|---------|
| **k8s-manifest-generator** | workflows | K8s manifests |
| **helm-chart-scaffolding** | workflows | Helm charts |
| **gitops-workflow** | workflows | GitOps patterns |
| **k8s-security-policies** | workflows | K8s security |

### Domain: Observability

| Skill | Source | Purpose |
|-------|--------|---------|
| **prometheus-configuration** | workflows | Metrics |
| **grafana-dashboards** | workflows | Dashboards |
| **distributed-tracing** | workflows | Tracing |
| **slo-implementation** | workflows | SLOs/SLIs |

### Domain: Payments

| Skill | Source | Purpose |
|-------|--------|---------|
| **stripe-integration** | workflows | Stripe payments |
| **paypal-integration** | workflows | PayPal payments |
| **billing-automation** | workflows | Billing systems |
| **pci-compliance** | workflows | PCI DSS |

### Domain: AI/LLM Development

| Skill | Source | Purpose |
|-------|--------|---------|
| **prompt-engineering-patterns** | workflows | Prompt design |
| **rag-implementation** | workflows | RAG systems |
| **langchain-architecture** | workflows | LangChain apps |
| **llm-evaluation** | workflows | LLM testing |
| **ml-pipeline-workflow** | workflows | ML pipelines |
| **mcp-builder** | anthropic | MCP server creation |

### Domain: Web3/Blockchain

| Skill | Source | Purpose |
|-------|--------|---------|
| **solidity-security** | workflows | Smart contract security |
| **defi-protocol-templates** | workflows | DeFi patterns |
| **nft-standards** | workflows | NFT implementation |
| **web3-testing** | workflows | Web3 testing |

### Domain: Languages & Frameworks

| Skill | Source | Purpose |
|-------|--------|---------|
| **typescript-advanced-types** | workflows | TS advanced patterns |
| **modern-javascript-patterns** | workflows | Modern JS |
| **async-python-patterns** | workflows | Async Python |
| **python-packaging** | workflows | Python packages |
| **react-modernization** | workflows | React upgrades |
| **angular-migration** | workflows | Angular migration |

### Domain: Shell & Scripting

| Skill | Source | Purpose |
|-------|--------|---------|
| **bash-defensive-patterns** | workflows | Safe bash |
| **shellcheck-configuration** | workflows | Shell linting |
| **bats-testing-patterns** | workflows | Shell testing |

### Domain: Meta & Orchestration

| Skill | Source | Purpose |
|-------|--------|---------|
| **MAKER** | custom | Multi-step execution |
| **SkillComposer** | custom | Skill orchestration |
| **ProactiveGuide** | custom | Guidance system |
| **SkillCreator** | custom | New skill creation |
| **skill-creator** | anthropic | Skill templates |
| **skill-development** | plugins | Skill dev guide |
| **brainstorming** | superpowers | Idea generation |
| **dispatching-parallel-agents** | superpowers | Parallel execution |
| **executing-plans** | superpowers | Plan execution |
| **subagent-driven-development** | superpowers | Subagent patterns |

### Domain: Debugging & Problem Solving

| Skill | Source | Purpose |
|-------|--------|---------|
| **debugging-strategies** | workflows | Debug approaches |
| **systematic-debugging** | superpowers | Methodical debugging |
| **root-cause-tracing** | superpowers | Find root causes |

### Domain: Documentation & Communication

| Skill | Source | Purpose |
|-------|--------|---------|
| **DocSync** | custom | Doc synchronization |
| **internal-comms** | anthropic | Internal communications |
| **slack-gif-creator** | anthropic | Slack content |

### Domain: Plugin Development

| Skill | Source | Purpose |
|-------|--------|---------|
| **plugin-structure** | plugins | Plugin architecture |
| **hook-development** | plugins | Hook creation |
| **agent-development** | plugins | Agent creation |
| **command-development** | plugins | Command creation |
| **mcp-integration** | plugins | MCP servers |

---

## Domain Detection

SkillComposer auto-detects domains from the goal:

```
DOMAIN_KEYWORDS:
  ui_ux:
    - UI, UX, design, visual, layout, styling, CSS, component
    - frontend, responsive, mobile, theme, colors, typography
  security:
    - security, auth, vulnerability, OWASP, injection, XSS
    - password, encryption, token, session, CSRF
  performance:
    - performance, speed, optimize, bundle, lazy, cache
    - memory, CPU, latency, throughput, bottleneck
  testing:
    - test, coverage, unit, integration, e2e, QA, QC
    - regression, assertion, mock, fixture
  code_quality:
    - review, refactor, clean, patterns, SOLID, DRY
    - naming, types, lint, format
  architecture:
    - architecture, design, system, scale, microservice
    - monolith, API, database, schema
  devops:
    - deploy, CI/CD, Docker, Kubernetes, pipeline
    - infrastructure, cloud, AWS, Vercel
  documentation:
    - docs, README, changelog, comments, API docs
  accessibility:
    - accessibility, a11y, WCAG, screen reader, contrast
    - keyboard, ARIA, focus
```

**Example:**
```
Goal: "QA the entire app for security vulnerabilities and fix them"

Detected Domains: [security, testing, code_quality]
Selected Skills: SecurityAudit, CodeReview, MAKER, TestGen
```

---

## How It Works

### Phase 0: Skill Discovery (if --scan-skills)

Scan for new skills and update registry before planning.

### Phase 1: Goal Analysis

The Analyzer Agent parses the goal and extracts:

| Extraction | Example |
|------------|---------|
| **Primary Domain(s)** | UI/UX, Security, Performance |
| **Sub-domains** | Design, Testing, Accessibility |
| **Complexity Level** | Simple (1-2 skills) / Medium (3-5) / Complex (6+) |
| **Dependencies** | What must complete before what |
| **Success Criteria** | How do we know we're done? |
| **Prerequisites** | localhost running, API keys, etc. |

**Analysis Prompt:**
```
Given this goal: "{USER_GOAL}"

1. DETECT_DOMAINS: Which domains are involved?
2. SELECT_SKILLS: Which skills can help? (from registry)
3. IDENTIFY_PREREQUISITES: What must be ready first?
4. PLAN_DEPENDENCIES: What order makes sense?
5. DEFINE_SUCCESS: How do we verify completion?
6. ESTIMATE_PHASES: How many major phases?
7. FIND_CHECKPOINTS: Where should we pause for approval?
```

### Phase 2: Skill Selection & Planning

The Planner creates an execution plan based on:
- Detected domains
- Skill capabilities
- Dependency graph
- User preferences (--domain hint)

```yaml
EXECUTION_PLAN:
  goal: "{USER_GOAL}"
  detected_domains: [domain1, domain2]
  selected_skills: [Skill1, Skill2, Skill3]
  phases:
    - phase: 1
      name: "Discovery"
      skills: [AppMap]
      parallel: false
    - phase: 2
      name: "Analysis"
      skills: [DesignAudit, A11yAudit, SecurityAudit]
      parallel: true
    - phase: 3
      name: "Execution"
      skills: [MAKER]
      condition: "user_approves"
    - phase: 4
      name: "Verification"
      skills: [VisualQA, TestGen]
```

### Phase 3: Autonomous Execution

Execute skills in order, handling:
- Parallel execution for independent skills
- Data handoffs between skills
- Failure recovery
- Dynamic skill injection

### Phase 4: Feedback Loop

Monitor and adapt:
- Retry failed skills until fixed (not skipped)
- Inject new skills if needed
- Update plan based on findings
- Cache results for efficiency

### Phase 5: Verification

Before marking any task complete:
1. Run full verification chain (tsc, lint, test, build)
2. Execute CodeReview with 5 Opus agents
3. Require unanimous approval
4. If any check fails: fix → re-verify → loop until zero errors
5. Only mark complete when all checks pass with zero errors

**Stop immediately when task is verified complete.** The 5-hour budget exists to achieve perfection, not to fill time.

---

## Commands

| Command | Action |
|---------|--------|
| `SkillComposer: {goal}` | Full autonomous execution |
| `SkillComposer --plan {goal}` | Generate plan only |
| `SkillComposer --dry-run {goal}` | Show what would run |
| `SkillComposer --interactive {goal}` | Pause at each phase |
| `SkillComposer --domain={domain} {goal}` | Hint primary domain |
| `SkillComposer --resume` | Resume from checkpoint |
| `SkillComposer --scan-skills` | Discover new skills |
| `SkillComposer --list-skills` | Show all known skills |
| `SkillComposer --list-domains` | Show all domains |

---

## Example Compositions

### Example 1: Full Application QA (Cross-Domain)

**Goal:** "Complete QA/QC of the entire application"

**Detected Domains:** [ui_ux, testing, code_quality, security, accessibility, performance]

**Composed Plan:**
```
Phase 1: Discovery
├─ AppMap                    # Understand structure

Phase 2: Multi-Domain Analysis (Parallel)
├─ DesignAudit              # UI code issues
├─ A11yAudit                # Accessibility
├─ SecurityAudit            # Security vulnerabilities
├─ CodeReview               # Code quality
├─ PerfOptimize --analyze   # Performance bottlenecks

Phase 3: Visual Verification
├─ VisualQA                 # Screenshot analysis

Phase 4: [Checkpoint] Review Findings
├─ Present summary
├─ Await user approval

Phase 5: Fix Execution
├─ MAKER                    # Apply all fixes

Phase 6: Verification
├─ VisualQA --regression    # Visual verification
├─ SecurityAudit --verify   # Security re-check
├─ TestGen                  # Generate tests

COMPLETE
```

### Example 2: Security Hardening

**Goal:** "Audit and fix all security vulnerabilities"

**Detected Domains:** [security, code_quality]

**Composed Plan:**
```
Phase 1: SecurityAudit
Phase 2: CodeReview --security
Phase 3: [Checkpoint] Prioritize fixes
Phase 4: MAKER (apply fixes)
Phase 5: SecurityAudit --verify
Phase 6: TestGen --security
```

### Example 3: Performance Optimization

**Goal:** "Make the app faster"

**Detected Domains:** [performance]

**Composed Plan:**
```
Phase 1: PerfOptimize --analyze
Phase 2: AppMap (understand deps)
Phase 3: [Checkpoint] Review bottlenecks
Phase 4: MAKER (apply optimizations)
Phase 5: PerfOptimize --compare
```

### Example 4: New Feature Development

**Goal:** "Add user authentication with OAuth"

**Detected Domains:** [architecture, security, backend]

**Composed Plan:**
```
Phase 1: ArchitectPlan (design auth system)
Phase 2: [Checkpoint] Approve architecture
Phase 3: AuthSystem (implement)
Phase 4: APIDesign (design endpoints)
Phase 5: TestGen (create tests)
Phase 6: SecurityAudit (verify security)
Phase 7: DocSync (update docs)
```

### Example 5: Design System Creation

**Goal:** "Create a comprehensive design system"

**Detected Domains:** [ui_ux, documentation]

**Composed Plan:**
```
Phase 1: AppMap (inventory components)
Phase 2: DesignAudit (analyze existing patterns)
Phase 3: [Checkpoint] Define tokens
Phase 4: ComponentLib (create library)
Phase 5: Frontend Design (build components)
Phase 6: A11yAudit (accessibility check)
Phase 7: DocSync (document system)
```

### Example 6: Monorepo Migration

**Goal:** "Convert to a monorepo with shared packages"

**Detected Domains:** [architecture, devops]

**Composed Plan:**
```
Phase 1: AppMap (understand structure)
Phase 2: ArchitectPlan (design monorepo)
Phase 3: [Checkpoint] Approve plan
Phase 4: MonorepoSetup (configure workspace)
Phase 5: Refactor (reorganize code)
Phase 6: DevOpsSetup (update CI/CD)
Phase 7: TestGen (verify nothing broke)
```

---

## Composition Patterns

### Pattern 1: Sequential Chain
```
Skill A → Skill B → Skill C
```
Each skill's output feeds the next.

### Pattern 2: Parallel Fan-Out
```
        ┌─ Skill B ─┐
Skill A ─┼─ Skill C ─┼─ Skill E
        └─ Skill D ─┘
```
Independent skills run concurrently, results aggregated.

### Pattern 3: Conditional Branch
```
Skill A → [if critical_issues] → MAKER → Verify
          [else] → TestGen → Done
```
Execution path depends on results.

### Pattern 4: Iterative Loop (Zero Error)
```
Skill A → Skill B → [verify] → [if errors] → Fix → [verify] → (loop until 0 errors)
                             → [if 0 errors] → Complete
```
Repeat until zero errors. Never skip, never tolerate errors.

### Pattern 5: Checkpoint Resume
```
Skill A → Skill B → [CHECKPOINT] → Skill C → Skill D
                         ↑
                    Resume from here
```
Save state for long-running compositions.

### Pattern 6: Dynamic Injection
```
Skill A → Skill B → [unexpected finding] → Inject Skill X → Continue
```
Add skills mid-execution based on discoveries.

---

## Cross-Skill Data Handoffs

Skills pass data to subsequent skills:

```yaml
HANDOFF_MATRIX:
  AppMap:
    provides: [component_tree, route_list, file_inventory]
    consumers: [DesignAudit, VisualQA, SecurityAudit]

  DesignAudit:
    provides: [code_issues, file_locations, token_usage]
    consumers: [VisualQA, MAKER, Refactor]

  SecurityAudit:
    provides: [vulnerabilities, severity_scores, fix_suggestions]
    consumers: [MAKER, CodeReview]

  VisualQA:
    provides: [visual_issues, screenshots, correlations]
    consumers: [MAKER, DesignAudit]

  CodeReview:
    provides: [code_issues, patterns_found, suggestions]
    consumers: [MAKER, Refactor]

  MAKER:
    provides: [changes_made, files_modified, verification_status]
    consumers: [TestGen, VisualQA, SecurityAudit]
```

---

## Zero Error Standard

**Error tolerance: 0%**

SkillComposer enforces the Zero Error Standard for all compositions.

| Rule | Meaning |
|------|---------|
| Zero errors | 0 type errors, 0 lint errors, 0 test failures, 0 build errors |
| Verify with evidence | Run checks, see passing output, confirm with your own eyes |
| Fix, never skip | Errors are fixed, not tolerated, not worked around |
| Done = verified correct | A task is complete only when 100% verified with zero errors |

**Verification Chain (required before any task is "complete"):**
```
tsc --noEmit       → 0 errors
npm run lint       → 0 errors
npm run test:run   → 0 failures
npm run build      → succeeds
CodeReview         → 5 Opus agents unanimous approval
```

**If any check fails:** Fix → Re-run all checks → Repeat until zero errors

**The 5-hour limit exists to achieve perfection, not to fill time.** Stop as soon as the task is verified complete.

---

## Configuration

```yaml
SKILL_COMPOSER_CONFIG:
  mode: autonomous  # autonomous | interactive | plan-only

  model:
    primary: opus           # Main orchestration model
    subagents: opus         # Model for spawned subagents
    fallback: sonnet        # If opus unavailable
    # Note: Always use Opus for complex reasoning tasks

  discovery:
    auto_scan: true  # Scan for new skills on start
    scan_paths:
      - ~/.claude/skills/
      - ~/.claude/plugins/

  checkpoints:
    auto_checkpoint: true
    checkpoint_interval: 5m
    require_approval: []  # No pauses - fully autonomous

  execution:
    parallel_skills: true
    max_parallel: 4
    timeout_per_skill: 30m  # Longer timeout for complex skills
    max_total_runtime: 5h   # Hard cap, but stop when done

  recovery:
    on_skill_failure: retry_until_fixed  # Keep trying until fixed
    max_retries: 10  # More attempts before escalating
    on_critical_failure: checkpoint_and_stop

  completion:
    require_zero_errors: true  # MUST have zero errors to mark complete
    verification_chain:
      - tsc --noEmit        # Zero type errors
      - npm run lint        # Zero lint errors
      - npm run test:run    # All tests pass
      - npm run build       # Build succeeds
      - CodeReview          # 5 Opus agents unanimous
    on_verification_fail: fix_and_reverify  # Loop until clean
    stop_when: task_verified_complete  # Don't fill time, stop when done

  domains:
    prefer: []  # Domains to prioritize
    exclude: []  # Domains to skip

  skills:
    exclude: []  # Skills to never auto-select
    prefer: []   # Skills to prefer when multiple options

  feedback:
    summarize_after_phase: true
    notify_on_complete: true
    save_execution_log: true
```

---

## Output Format

### COMPOSITION_REPORT.md

```markdown
# SkillComposer Execution Report

**Goal:** {original_goal}
**Detected Domains:** {domains}
**Mode:** {autonomous|interactive}
**Started:** {timestamp}
**Completed:** {timestamp}
**Duration:** {total_time}

## Execution Summary

| Phase | Skills | Status | Duration | Findings |
|-------|--------|--------|----------|----------|
| 1 | AppMap | ✅ | 45s | 47 components |
| 2 | DesignAudit, A11yAudit, SecurityAudit | ✅ | 2m 15s | 52 issues |
| 3 | VisualQA | ✅ | 3m 30s | 18 visual issues |
| 4 | MAKER | ✅ | 8m 12s | 45 fixed |
| 5 | VisualQA, TestGen | ✅ | 4m 00s | 0 remaining |

## Skills Executed

[Details for each skill...]

## Artifacts Generated

| File | Description |
|------|-------------|
| APP_MAP.md | Component architecture |
| DESIGN_AUDIT_REPORT.md | Code-level design issues |
| SECURITY_REPORT.md | Security vulnerabilities |
| VISUAL_QA_REPORT.md | Visual verification |
| COMPOSITION_REPORT.md | This report |

## Next Steps

1. [Recommendation based on findings]
2. [Recommendation]
3. [Recommendation]
```

---

## Adding New Skills

When you create a new skill with SkillCreator:

1. Create skill in `~/.claude/skills/{skill-name}/SKILL.md`
2. Run `SkillComposer --scan-skills`
3. New skill is auto-added to registry
4. SkillComposer can now use it in compositions

**Best Practice for New Skills:**

Include this metadata in SKILL.md frontmatter:
```yaml
---
name: my-new-skill
description: What the skill does
domains: [domain1, domain2]
type: analyzer | executor | generator | validator
inputs: [input types]
outputs: [output files/types]
requires: [prerequisites]
integrates_with: [other skills]
---
```

---

## Best Practices

1. **Start with `--plan`** - Review the plan before full execution
2. **Use `--scan-skills`** - After adding new skills
3. **Use domain hints** - `--domain=security` for faster planning
4. **Set checkpoints** - Long compositions should have approval points
5. **Review reports** - Check COMPOSITION_REPORT.md after completion
6. **Iterate** - Run composition again after fixes to verify
7. **Customize config** - Adjust for your workflow preferences

---

## Limitations

- Cannot create new skills (use SkillCreator for that)
- Some skills require prerequisites (e.g., localhost running)
- Context limits may affect very complex compositions

## Completion Behavior

| Situation | Action |
|-----------|--------|
| Task implemented | Run full verification chain |
| Verification passes | Mark complete, stop immediately |
| Verification fails | Fix issues, re-verify (loop until zero errors) |
| 5 hours elapsed | Hard stop, checkpoint remaining work |

**Error tolerance: 0%** — There is no "good enough." There is only correct or not yet correct.
