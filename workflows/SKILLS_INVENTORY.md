# Complete Skills Inventory

## Summary
- **Total Skills:** 237+
- **Custom Skills:** 40
- **Superpowers Skills:** 29
- **Workflow Plugin Skills:** 168+ (across 66 plugin categories)
- **Active Hooks:** 11

---

## Custom Skills (40)
Located in `~/.claude/skills/`

### Meta Skills
- skill-composer (orchestrates multiple skills)
- skillcreator
- skillrecommender
- maker-framework (systematic task decomposition)
- overnightmode (7-hour autonomous)

### UI/UX & Design
- design-audit (8-agent design analysis)
- visual-qa (screenshot testing with Claude vision)
- frontend-design
- a11yaudit (WCAG compliance)
- componentlib

### Code Quality & Review
- codereview (multi-agent)
- refactor
- testgen (unit/integration/E2E)
- errorexplainer
- errorhandler

### Architecture & Planning
- architectplan (system design)
- appmap (sitemap, workflows, diagrams)
- dbschema (database design)
- apidesign (REST/GraphQL)
- authsystem

### DevOps & Deployment
- devopssetup (CI/CD)
- deploymentguide
- securityaudit (OWASP Top 10)
- perfoptimize (performance)
- monoreposetup

### Documentation
- docsync
- compactmd
- promptgen
- apidocgen
- changelogwriter

### Development Tools
- mobilekit (React Native/Expo)
- i18nsetup
- envmanager
- dependencyauditor
- gitworkflow

### Project Management
- sessionkickoff
- featurescoper
- costestimator
- backupsnapshot
- proactive-guide

---

## Superpowers Skills (29)
Located in `~/.claude/plugins/cache/superpowers/skills/`

### Core Workflows
- brainstorming (before coding)
- writing-plans (detailed implementation)
- executing-plans (batch execution)
- subagent-driven-development

### Development Practices
- test-driven-development (TDD)
- testing-anti-patterns
- testing-skills-with-subagents
- condition-based-waiting

### Code Review & Quality
- requesting-code-review
- receiving-code-review
- verification-before-completion
- defense-in-depth

### Debugging & Problem Solving
- systematic-debugging (4-phase framework)
- root-cause-tracing
- dispatching-parallel-agents

### Git & Collaboration
- using-git-worktrees
- finishing-a-development-branch
- sharing-skills (contribute upstream)

### Process & Skills
- using-superpowers (mandatory workflows)
- writing-skills (TDD for skills)

---

## Workflow Plugin Skills (168+)
Located in `~/.claude/plugins/marketplaces/claude-code-workflows/plugins/`

### 66 Plugin Categories:

**Infrastructure & Cloud**
- cloud-infrastructure
- kubernetes-operations
- deployment-strategies
- deployment-validation
- database-cloud-optimization

**Backend Development**
- backend-development
- backend-api-security
- api-scaffolding
- api-testing-observability
- database-design
- database-migrations

**Frontend & Mobile**
- frontend-mobile-development
- frontend-mobile-security
- multi-platform-apps

**Full Stack**
- full-stack-orchestration

**Testing & QA**
- unit-testing
- tdd-workflows
- performance-testing-review
- data-validation-suite

**Security**
- security-compliance
- security-scanning
- frontend-mobile-security
- incident-response

**DevOps & CI/CD**
- cicd-automation
- git-pr-workflows
- deployment-strategies

**Observability**
- observability-monitoring
- api-testing-observability
- distributed-debugging
- error-diagnostics

**Code Quality**
- code-review-ai
- code-refactoring
- codebase-cleanup
- comprehensive-review
- debugging-toolkit
- error-debugging

**Documentation**
- code-documentation
- documentation-generation

**Data & ML**
- data-engineering
- machine-learning-ops
- llm-application-dev
- business-analytics
- quantitative-trading

**Languages & Frameworks**
- javascript-typescript
- python-development
- jvm-languages
- julia-development
- systems-programming
- shell-scripting
- functional-programming
- framework-migration

**Specialized Domains**
- blockchain-web3
- game-development
- arm-cortex-microcontrollers
- payment-processing

**Performance**
- application-performance
- performance-testing-review

**Dependencies & Management**
- dependency-management
- context-management

**SEO & Marketing**
- seo-analysis-monitoring
- seo-content-creation
- seo-technical-optimization
- content-marketing

**Business & Compliance**
- hr-legal-compliance
- accessibility-compliance

**Team & Collaboration**
- team-collaboration
- agent-orchestration
- customer-sales-automation

---

## Configured Hooks (11)

Located in `~/.claude/settings.json`

### PreToolUse Hooks (2)
1. **Bash** - Export NVM node path
2. **Task** - Verify task has clear success criteria before spawning subagent

### PostToolUse Hooks (3)
1. **Edit** - Auto-format with Prettier for JS/TS files
2. **Bash** - Check output for test failures, build errors, lint warnings
3. **Write** - Auto-format with Prettier for JS/TS files

### Other Hooks (6)
4. **Stop** - Session cleanup
5. **SubagentStop** - Subagent cleanup
6. **SessionStart** - Initialize session
7. **SessionEnd** - End session cleanup
8. **Notification** - Handle notifications
9. **UserPromptSubmit** - Process user input

---

## Organization Structure

```
~/.claude/
├── CLAUDE.md                        # Global instructions (22KB)
├── IMPROVEMENT_BACKLOG.md           # Global improvement tracking
│
├── workflows/                       # Global workflow templates
│   ├── OVERNIGHT_CONFIG.md          # 7-hour autonomous config
│   ├── OVERNIGHT_TASKS.md           # Overnight task template
│   ├── SKILLS_INVENTORY.md          # This file
│   └── README.md
│
├── skills/                          # Custom skills (40)
│   ├── skill-composer/
│   ├── maker-framework/
│   ├── design-audit/
│   ├── visual-qa/
│   └── ... (36 more)
│
├── commands/                        # Global slash commands (21)
│   ├── brainstorm.md
│   ├── execute-plan.md
│   ├── write-plan.md
│   └── ... (18 more)
│
├── plugins/
│   ├── cache/superpowers/
│   │   └── skills/                  # Superpowers skills (29)
│   │
│   └── marketplaces/
│       ├── claude-code-workflows/
│       │   └── plugins/             # 66 plugin categories (168+ skills)
│       └── claude-code-plugins/
│
└── settings.json                    # Hooks configuration (11 hooks)
```

---

## Usage Guide

### Finding Skills
```bash
# List custom skills
ls -1 ~/.claude/skills/

# List superpowers skills
ls -1 ~/.claude/plugins/cache/superpowers/skills/

# List workflow plugin categories
ls -1 ~/.claude/plugins/marketplaces/claude-code-workflows/plugins/

# Search for specific skill
find ~/.claude -name "*design*" -type d | grep skills
```

### Using SkillRecommender
```
SkillRecommender: which skill should I use for [task]?
```

### Scanning All Skills
```
SkillComposer --scan-skills
```

This will update the skill registry with all available skills.

---

## Skill Categories by Use Case

| Use Case | Recommended Skills |
|----------|-------------------|
| Design Review | design-audit, visual-qa, a11yaudit |
| Code Quality | codereview, refactor, testgen |
| Architecture | architectplan, appmap, dbschema |
| Security | securityaudit, backend-api-security, security-scanning |
| Performance | perfoptimize, application-performance |
| Testing | testgen, tdd-workflows, unit-testing |
| Debugging | systematic-debugging, error-debugging, debugging-toolkit |
| Documentation | docsync, documentation-generation, apidocgen |
| Deployment | deploymentguide, cicd-automation, deployment-strategies |
| Complex Tasks | maker-framework, skill-composer |
| Overnight Work | overnightmode |
| Project Start | sessionkickoff, featurescoper |
