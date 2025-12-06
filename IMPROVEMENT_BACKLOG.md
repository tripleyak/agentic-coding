# Claude Code Improvement Backlog

Tracking workflow, process, coding, and automation improvements for Claude Code CLI.

> **When completed:** Add skills to `~/.claude/CLAUDE.md` skill registry

---

## Skills to Build

### High Priority

| Skill | Purpose | Triggers | Output | Complexity | Deps | Status |
|-------|---------|----------|--------|------------|------|--------|
| **ErrorExplainer** | Translates cryptic stack traces into plain English, suggests fixes | `explain error`, `what does this mean`, auto-detect stack traces | Plain English explanation + fix suggestions + related docs | Small (1 phase) | — | ✅ Done |
| **DeploymentGuide** | Step-by-step deployment to Vercel/Railway/Fly.io with pre-flight checks | `deploy`, `go live`, `push to production` | Checklist → Pre-flight report → Deploy commands → Verification | Medium (3 phases) | DependencyAuditor | ✅ Done |
| **DependencyAuditor** | Checks package.json for outdated/vulnerable/unused packages, safely updates | `audit deps`, `check packages`, `update dependencies` | Audit report + safe update commands + breaking change warnings | Small (1 phase) | — | ✅ Done |
| **GitWorkflow** | Automates branching, commits, PR creation with good messages | `create branch`, `commit changes`, `open PR` | Branch creation → Staged commits → PR with description | Small (1 phase) | superpowers | ✅ Done |

### Medium Priority

| Skill | Purpose | Triggers | Output | Complexity | Deps | Status |
|-------|---------|----------|--------|------------|------|--------|
| **FeatureScoper** | Before building, helps think through scope, edge cases, phases | `scope this`, `plan feature`, `before I build` | Scope doc with phases, edge cases, out-of-scope items, acceptance criteria | Medium (2 phases) | — | ✅ Done |
| **CostEstimator** | Estimates monthly costs when adding services (DB, auth, APIs) | `estimate costs`, `how much will this cost`, `pricing check` | Cost breakdown table + tier recommendations + scaling projections | Small (1 phase) | — | ✅ Done |
| **BackupSnapshot** | Creates restore points before big changes | `backup`, `snapshot`, `save state`, auto before risky ops | Git stash + branch snapshot + confirmation message | Small (1 phase) | — | ✅ Done |

### Low Priority / Ideas

| Skill | Purpose | Triggers | Complexity | Status |
|-------|---------|----------|------------|--------|
| **ChangelogWriter** | Auto-generates CHANGELOG entries from commits | `update changelog`, `what changed` | Small | ✅ Done |
| **EnvManager** | Manages .env files across environments | `setup env`, `sync env vars` | Small | ✅ Done |
| **APIDocGen** | Generates API documentation from code | `document API`, `generate docs` | Medium | ✅ Done |
| **UpdateModels** | Centralized model management & auto-update across all files | `update models`, `sync models` | Medium | ✅ Done |

---

## Hooks to Add

| Hook | Trigger | Purpose | Complexity | Status |
|------|---------|---------|------------|--------|
| PreToolUse: Write | Before overwriting files | Warn user before overwriting important files (package.json, config) | Small | Idea |
| PostToolUse: Bash(npm install) | After installing packages | Explain what was installed in plain English | Small | Idea |
| PostToolUse: Bash(git *) | After git operations | Summarize what happened (commits, branch changes) | Small | Idea |
| PreToolUse: Bash(rm) | Before delete commands | Extra confirmation for destructive operations | Small | Idea |
| UserPromptSubmit | Ambiguous requests | Detect vague requests, prompt for clarification before proceeding | Medium | Idea |
| PostToolUse: Edit | After code changes | Auto-run relevant tests for changed files | Medium | Idea |

---

## Workflow Improvements

| Improvement | Description | Status |
|-------------|-------------|--------|
| Auto-backup before refactors | Run BackupSnapshot skill automatically before large refactoring operations | Ready (BackupSnapshot available) |
| Test-on-save | Run affected tests after Edit operations complete | Idea |
| Smart context loading | Load only relevant files based on task type | Idea |

---

## Completed

### Skills Built (Dec 5, 2024) - Batch 3

| Skill | Purpose | Triggers |
|-------|---------|----------|
| **UpdateModels** | Centralized model config & auto-update | `update models`, `sync models` |

### Skills Built (Dec 4, 2024) - Batch 2

| Skill | Purpose | Triggers |
|-------|---------|----------|
| **ErrorExplainer** | Translates stack traces to plain English | `explain error`, `what does this mean` |
| **DeploymentGuide** | Step-by-step deployment with pre-flight checks | `deploy`, `go live` |
| **DependencyAuditor** | Checks packages for issues, safe updates | `audit deps`, `check packages` |
| **GitWorkflow** | Automates branching, commits, PRs | `create branch`, `commit changes` |
| **FeatureScoper** | Thinks through scope before building | `scope this`, `plan feature` |
| **CostEstimator** | Estimates monthly service costs | `estimate costs`, `pricing check` |
| **BackupSnapshot** | Creates restore points | `backup`, `snapshot` |
| **ChangelogWriter** | Auto-generates CHANGELOG | `update changelog` |
| **EnvManager** | Manages .env files | `setup env`, `sync env vars` |
| **APIDocGen** | Generates API documentation | `document API`, `openapi spec` |

### Skills Built (Dec 4, 2024) - Batch 1

| Skill | Purpose |
|-------|---------|
| **SkillComposer** | Global meta-orchestrator for all 145+ skills |
| **MAKER** | Systematic decomposition for complex multi-step tasks |
| **DesignAudit** | 8-agent code-level design consistency audit |
| **VisualQA** | Screenshot-based visual QA with Claude vision |
| **ProactiveGuide** | Always-on guidance for unknown unknowns |

### Hooks Implemented (Dec 4, 2024)

| Hook | Purpose |
|------|---------|
| PreToolUse: Bash | NVM path setup |
| PreToolUse: Task | Validate subagent tasks before spawning |
| PostToolUse: Edit/Write | Auto-format with Prettier |
| PostToolUse: Bash | Detect test/build failures, add to TodoWrite |
| Stop | Continue MAKER/SkillComposer workflows |
| SubagentStop | Keep subagents running until complete |
| SessionStart | Auto-load project context |
| SessionEnd | Save SESSION_HANDOFF.md |
| Notification | Route failures to TodoWrite |
| UserPromptSubmit | ProactiveGuide activation (145+ skill awareness) |

### Configuration (Dec 5, 2024)

| Change | Detail |
|--------|--------|
| Model management | Centralized config at ~/.claude/config/models.yaml |
| Model references | All skills/commands updated to use correct identifiers |
| Update automation | /update-models command for future model updates |

### Configuration (Dec 4, 2024)

| Change | Detail |
|--------|--------|
| Model preference | All skills use Opus (claude-opus-4-5) |
| Plugins enabled | superpowers, frontend-design |
| Skill registry | Updated to 145+ skills (39 custom + plugins + workflows) |
| CLAUDE.md | ~1160 lines with all skill definitions |

---

## Stats

| Metric | Count |
|--------|-------|
| Custom skills | 41 |
| Plugin skills | 30+ |
| Workflow skills | 60+ |
| Total available | 147+ |
| Hooks implemented | 10 |

---

## Notes

- User is a non-programmer learning to build with Claude
- Priority is proactive guidance and automation
- Focus on reducing "unknown unknowns"
- All skills should use Opus model for quality
