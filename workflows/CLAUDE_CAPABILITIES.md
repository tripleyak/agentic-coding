# Claude Code Capabilities

**Complete inventory of all skills, hooks, commands, and plugins**

Last Updated: 2025-12-06

---

## Quick Stats

| Category | Count |
|----------|-------|
| **Custom Skills** | 41 |
| **Superpowers Skills** | 20 |
| **Workflow Plugin Categories** | 66 |
| **Active Hooks** | 15 |
| **Global Slash Commands** | 22 |
| **Plugin Commands** | 16 |
| **Enabled Plugins** | 2 |
| **MCP Servers** | 0 (none configured) |

---

## 1. Skills (127+ total)

### Custom Skills (41)
Located in `~/.claude/skills/`

| Skill | Purpose |
|-------|---------|
| **a11yaudit** | WCAG accessibility compliance checking |
| **apidesign** | REST/GraphQL API design patterns |
| **apidocgen** | Generate API documentation (OpenAPI 3.0) |
| **appmap** | Generate architecture artifacts (APP_MAP.md) |
| **architectplan** | System architecture and ADRs |
| **authsystem** | Authentication system setup |
| **backupsnapshot** | Create restore points before risky changes |
| **changelogwriter** | Generate changelog from commits |
| **codereview** | Multi-agent code review (5 agents) |
| **compactmd** | Compress CLAUDE.md to <1000 lines |
| **componentlib** | Design system/component library setup |
| **costestimator** | Estimate hosting/service costs |
| **dbschema** | Database schema design |
| **dependencyauditor** | Audit npm packages for issues |
| **deploymentguide** | Step-by-step deployment guidance |
| **design-audit** | 8-agent design language audit |
| **devopssetup** | CI/CD pipeline configuration |
| **docsync** | Keep documentation in sync |
| **envmanager** | Environment variable management |
| **errorexplainer** | Translate stack traces to plain English |
| **errorhandler** | Error handling patterns setup |
| **featurescoper** | Scope and plan features |
| **frontend-design** | Distinctive UI design (no AI slop) |
| **gitworkflow** | Git automation (branches, commits, PRs) |
| **i18nsetup** | Internationalization setup |
| **maker-framework** | Systematic task decomposition |
| **mobilekit** | React Native/Expo setup |
| **monoreposetup** | Turborepo/Nx monorepo config |
| **overnightmode** | 5-hour autonomous work mode |
| **perfoptimize** | Performance optimization |
| **proactive-guide** | Proactive guidance for non-programmers |
| **promptgen** | Generate optimized prompts |
| **refactor** | Code refactoring patterns |
| **securityaudit** | OWASP Top 10 security analysis |
| **sessionkickoff** | Project onboarding for new sessions |
| **skill-composer** | Meta-orchestrator for multiple skills |
| **skillcreator** | Create new skills |
| **skillrecommender** | Recommend skills for tasks |
| **testgen** | Generate unit/integration/E2E tests |
| **update-models** | Update model references across config |
| **visual-qa** | Screenshot-based visual QA testing |

### Superpowers Skills (20)
Located in `~/.claude/plugins/cache/superpowers/skills/`

| Skill | Purpose |
|-------|---------|
| **brainstorming** | Refine ideas before coding |
| **condition-based-waiting** | Replace arbitrary timeouts with polling |
| **defense-in-depth** | Multi-layer validation |
| **dispatching-parallel-agents** | Run 3+ agents concurrently |
| **executing-plans** | Execute implementation plans in batches |
| **finishing-a-development-branch** | Complete and integrate work |
| **receiving-code-review** | Process code review feedback |
| **requesting-code-review** | Request reviews before merging |
| **root-cause-tracing** | Trace bugs to source |
| **sharing-skills** | Contribute skills upstream |
| **subagent-driven-development** | Fresh subagent per task |
| **systematic-debugging** | 4-phase debugging framework |
| **test-driven-development** | Write tests first, watch fail, then pass |
| **testing-anti-patterns** | Avoid testing mock behavior |
| **testing-skills-with-subagents** | Verify skills work under pressure |
| **using-git-worktrees** | Isolated feature work |
| **using-superpowers** | Mandatory workflows for skills |
| **verification-before-completion** | Verify before claiming done |
| **writing-plans** | Create detailed implementation plans |
| **writing-skills** | TDD for process documentation |

### Workflow Plugin Categories (66)
Located in `~/.claude/plugins/marketplaces/claude-code-workflows/plugins/`

**Infrastructure:** cloud-infrastructure, kubernetes-operations, deployment-strategies, deployment-validation

**Backend:** backend-development, backend-api-security, api-scaffolding, api-testing-observability, database-design, database-migrations

**Frontend & Mobile:** frontend-mobile-development, frontend-mobile-security, multi-platform-apps

**Testing:** unit-testing, tdd-workflows, performance-testing-review, data-validation-suite

**Security:** security-compliance, security-scanning, incident-response

**DevOps:** cicd-automation, git-pr-workflows

**Code Quality:** code-review-ai, code-refactoring, codebase-cleanup, comprehensive-review, debugging-toolkit, error-debugging

**Documentation:** code-documentation, documentation-generation

**Data & ML:** data-engineering, machine-learning-ops, llm-application-dev, business-analytics

**Languages:** javascript-typescript, python-development, jvm-languages, julia-development, systems-programming, shell-scripting, functional-programming

*(66 total categories with 168+ individual skills)*

---

## 2. Hooks (15 active)

All hooks configured in `~/.claude/settings.json`

### PreToolUse (2)
| Matcher | Type | Purpose |
|---------|------|---------|
| Bash | Command | Export NVM node path |
| Task | Prompt | Verify subagent task has clear success criteria |

### PostToolUse (3)
| Matcher | Type | Purpose |
|---------|------|---------|
| Edit | Command | Auto-format with Prettier (.ts/.tsx/.js/.jsx) |
| Bash | Prompt | Check for test failures, build errors, lint warnings |
| Write | Command | Auto-format with Prettier (.ts/.tsx/.js/.jsx) |

### Session & Memory (4)
| Event | Script | Purpose |
|-------|--------|---------|
| SessionStart | `memory_session_start.py` | Load session primer + project docs |
| SessionEnd | `memory_curate.py` | Curate memories from session |
| SessionEnd | `session_handoff_generator.py` | Generate SESSION_HANDOFF.md |
| UserPromptSubmit | `memory_inject.py` | Inject relevant memories |
| PreCompact | `memory_curate_transcript.py` | Preserve insights before compaction |

### Other (3)
| Event | Type | Purpose |
|-------|------|---------|
| Stop | Prompt | Overnight mode task continuation check |
| SubagentStop | Prompt | Evaluate subagent completion |
| Notification | Prompt | Handle test/build failure notifications |

---

## 3. Slash Commands (38 total)

### Global Commands (22)
Located in `~/.claude/commands/`

| Command | Description |
|---------|-------------|
| `/brainstorm` | Interactive design refinement using Socratic method |
| `/branch` | Create and switch to a new feature branch |
| `/build` | Run a production build and report results |
| `/changelog` | Add a new entry to CHANGELOG.md |
| `/check` | Run TypeScript compiler and linter |
| `/checkpoint` | Create a WIP checkpoint commit |
| `/debug` | Investigate a reported issue or bug |
| `/deps` | Show file imports and what imports it |
| `/execute-plan` | Execute plan in batches with review checkpoints |
| `/find` | Smart search for components, functions, types |
| `/imports` | Analyze imports across the codebase |
| `/perf` | Analyze codebase for performance issues |
| `/pr` | Create a pull request with auto-generated summary |
| `/refactor` | Suggest refactoring opportunities for a file |
| `/ship` | Commit all changes and push to origin |
| `/shipit` | Commit all changes and push to origin/main |
| `/size` | Analyze bundle size vs targets |
| `/status` | Show overall project health |
| `/sync` | Pull latest from main and rebase |
| `/todo` | Extract all TODO/FIXME/HACK comments |
| `/update-models` | Update model references from models.yaml |
| `/write-plan` | Create detailed implementation plan |

### Plugin Commands (16)
From enabled plugins in `~/.claude/plugins/marketplaces/`

| Command | Plugin | Description |
|---------|--------|-------------|
| `/cancel-ralph` | ralph-wiggum | Cancel Ralph loop |
| `/clean_gone` | commit-commands | Clean gone branches |
| `/code-review` | code-review | Review code |
| `/commit` | commit-commands | Create commit |
| `/commit-push-pr` | commit-commands | Commit, push, and create PR |
| `/configure` | hookify | Configure hookify |
| `/create-plugin` | plugin-dev | Create a new plugin |
| `/dedupe` | claude-code-plugins | Deduplicate |
| `/feature-dev` | feature-dev | Feature development workflow |
| `/help` | hookify | Hookify help |
| `/hookify` | hookify | Hookify main command |
| `/list` | hookify | List hooks |
| `/new-sdk-app` | agent-sdk-dev | Create new SDK app |
| `/oncall-triage` | claude-code-plugins | Oncall triage |
| `/ralph-loop` | ralph-wiggum | Start Ralph loop |
| `/review-pr` | pr-review-toolkit | Review a pull request |

---

## 4. Enabled Plugins (2)

| Plugin | Source | Features |
|--------|--------|----------|
| **superpowers** | superpowers-marketplace | 20 skills, 3 commands |
| **frontend-design** | claude-code-plugins | Distinctive UI generation |

---

## 5. Memory System

### Components
- **Server:** `~/.claude/memory/` (localhost:8765)
- **Storage:** ChromaDB (vectors) + SQLite (metadata)
- **Hooks:** 4 Python scripts in `~/.claude/hooks/`

### Memory Flow
1. **SessionStart** → Load temporal context ("we last spoke...")
2. **UserPromptSubmit** → Inject top 5 relevant memories
3. **PreCompact** → Preserve insights before compression
4. **SessionEnd** → AI curates meaningful memories

---

## 6. Project Documentation (Auto-loaded)

At session start, these files are loaded from project root:

| File | Purpose | Max Lines |
|------|---------|-----------|
| `SESSION_HANDOFF.md` | Previous session state | 150 |
| `ROADMAP.md` | Project priorities & specs | 150 |
| `APP_MAP.md` | Architecture overview | 200 |

---

## 7. Quick Reference

### Trigger Phrases by Category

| Need | Say | Skill Activated |
|------|-----|-----------------|
| Design review | "design audit", "UI audit" | design-audit |
| Visual testing | "visual QA", "screenshot audit" | visual-qa |
| Code review | "review code", "PR review" | codereview |
| Debug issue | "systematic debugging" | systematic-debugging |
| Plan feature | "scope this", "plan feature" | featurescoper |
| Complex task | "MAKER", "decompose" | maker-framework |
| Overnight work | "overnight", "queue tasks" | overnightmode |
| Deploy | "deploy", "go live" | deploymentguide |
| Security check | "security audit", "OWASP" | securityaudit |
| Performance | "optimize", "speed up" | perfoptimize |
| Tests | "write tests", "TestGen" | testgen |
| API docs | "document API", "openapi" | apidocgen |
| Backup | "backup", "snapshot" | backupsnapshot |
| Changelog | "update changelog" | changelogwriter |
| Skill help | "recommend skill", "which skill" | skillrecommender |
| Multi-skill | "SkillComposer", "orchestrate" | skill-composer |

### Common Commands

```bash
# Project health
/status
/check
/todo

# Development
/branch feature/my-feature
/debug "error message"
/refactor src/component.tsx

# Git workflow
/checkpoint
/ship
/pr

# Planning
/brainstorm
/write-plan
/execute-plan
```

---

## File Locations

```
~/.claude/
├── CLAUDE.md                    # Global instructions
├── settings.json                # Hooks, plugins, permissions
├── commands/                    # 22 slash commands
├── hooks/                       # 5 Python hook scripts
├── skills/                      # 41 custom skills
├── workflows/                   # This file + inventories
├── plugins/
│   ├── cache/superpowers/       # Superpowers skills (20)
│   └── marketplaces/
│       ├── claude-code-plugins/ # Plugin commands (16)
│       └── claude-code-workflows/ # 66 workflow categories
└── memory/                      # Memory system server
```

---

*This document consolidates SKILLS_INVENTORY.md and HOOKS_INVENTORY.md into a single reference.*
