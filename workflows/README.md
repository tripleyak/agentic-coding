# Claude Workflows

**Purpose:** Global workflow templates and documentation for project-agnostic automation

---

## 📁 Files in This Directory

| File | Purpose |
|------|---------|
| **OVERNIGHT_CONFIG.md** | Configuration for 7-hour autonomous UI/UX + QA/QC reviews |
| **OVERNIGHT_TASKS.md** | Task template for overnight autonomous operations |
| **SKILLS_INVENTORY.md** | Complete catalog of 237+ skills across all sources |
| **HOOKS_INVENTORY.md** | Documentation of 11 configured hooks |
| **ORGANIZATION_GUIDE.md** | Complete guide to global vs project-specific organization |
| **README.md** | This file |

---

## 🎯 Quick Start

### Running Overnight Mode

From any project directory:
```bash
overnight
```

Or via SkillComposer:
```
SkillComposer: Execute comprehensive UI/UX and QA/QC review per ~/.claude/workflows/OVERNIGHT_TASKS.md
```

### Finding Skills

```bash
# View custom skills
ls ~/.claude/skills/

# Search all skills
find ~/.claude -name "*[keyword]*" -type d | grep skills

# Scan and update registry
SkillComposer --scan-skills
```

### Using SkillRecommender

```
SkillRecommender: which skill should I use for [your task]?
```

---

## 📊 System Inventory

### Skills: 237+ Total

| Source | Count | Location |
|--------|-------|----------|
| **Custom** | 40 | `~/.claude/skills/` |
| **Superpowers** | 29 | `~/.claude/plugins/cache/superpowers/skills/` |
| **Workflow Plugins** | 168+ | `~/.claude/plugins/marketplaces/claude-code-workflows/` |

**Key Skills:**
- `skill-composer` - Meta-orchestrator for complex workflows
- `maker-framework` - Systematic task decomposition
- `design-audit` - 8-agent design analysis
- `visual-qa` - Screenshot testing with Claude vision
- `codereview` - Multi-agent code review
- `overnightmode` - 7-hour autonomous operation

See `SKILLS_INVENTORY.md` for complete catalog.

### Hooks: 15 Active 🧠

| Event Type | Count | Purpose |
|------------|-------|---------|
| PreToolUse | 2 | NVM setup, Task verification |
| PostToolUse | 3 | Auto-format, Output analysis |
| **Memory System** | **4** | **Session continuity, Injection, Curation** |
| Other | 6 | Session/stop/notification handling |

**NEW:** Persistent cross-session memory system installed!

See `HOOKS_INVENTORY.md` for complete documentation.

---

## 🏗️ Organization Philosophy

### ✅ Global (~/.claude/)
**Belongs here if:** Works for ANY project/codebase

- Workflow templates (overnight, maker)
- Reusable skills (design-audit, visual-qa, test-gen)
- Generic commands (build, check, debug)
- Universal hooks (auto-formatting, error detection)

### ❌ Project-Specific (project/.claude/)
**Belongs here if:** Specific to one project's domain

- Domain-specific commands (add-product, add-retailer)
- Project documentation (CLAUDE.md, APP_MAP.md)
- MAKER task files (*.maker.json)

See `ORGANIZATION_GUIDE.md` for complete philosophy and examples.

---

## 📂 Complete Structure

```
~/.claude/
│
├── workflows/                         # 📋 This directory
│   ├── OVERNIGHT_CONFIG.md
│   ├── OVERNIGHT_TASKS.md
│   ├── SKILLS_INVENTORY.md
│   ├── HOOKS_INVENTORY.md
│   ├── ORGANIZATION_GUIDE.md
│   └── README.md
│
├── skills/                            # 🎨 40 custom skills
│   ├── skill-composer/
│   ├── maker-framework/
│   ├── design-audit/
│   ├── visual-qa/
│   └── ...
│
├── commands/                          # 🎮 21 global slash commands
│   ├── brainstorm.md
│   ├── execute-plan.md
│   ├── write-plan.md
│   └── ...
│
├── plugins/
│   ├── cache/superpowers/
│   │   └── skills/                    # 🦸 29 superpowers skills
│   │
│   └── marketplaces/
│       └── claude-code-workflows/
│           └── plugins/               # 🌐 66 categories, 168+ skills
│
├── CLAUDE.md                          # Global instructions (22KB)
├── settings.json                      # Hooks configuration
└── ...
```

---

## 🚀 How It Works Across Projects

**Example: Design Audit**

```bash
# In ShelfWins-Studio
cd ~/ShelfWins-Studio
design-audit
# → Analyzes ShelfWins-Studio UI

# In Another Project
cd ~/my-other-app
design-audit
# → Analyzes my-other-app UI

# Same skill, different project!
```

**All workflows, skills, and hooks work on ANY project directory.**

---

## 🔍 Discovery Tools

| Task | Command |
|------|---------|
| List custom skills | `ls ~/.claude/skills/` |
| Search for skill | `find ~/.claude -name "*design*" -type d \| grep skills` |
| View hooks | `cat ~/.claude/settings.json \| jq '.hooks'` |
| Scan all skills | `SkillComposer --scan-skills` |
| Get recommendations | `SkillRecommender: [your task]` |

---

## 📚 Documentation Index

1. **OVERNIGHT_CONFIG.md** - How to run 7-hour autonomous reviews
2. **OVERNIGHT_TASKS.md** - Template for overnight operations
3. **SKILLS_INVENTORY.md** - Complete catalog of 237+ skills
4. **HOOKS_INVENTORY.md** - All 11 hooks explained
5. **ORGANIZATION_GUIDE.md** - Global vs project-specific philosophy

---

## 🎯 Benefits

1. **Portability** - Same tools work across all projects
2. **Consistency** - Uniform workflows everywhere
3. **Efficiency** - No duplication of generic tools
4. **Scalability** - Add projects without recreating setup
5. **Discovery** - All tools in predictable locations
6. **Automation** - Hooks apply everywhere automatically

---

## 🆘 Quick Reference

| Need | Use |
|------|-----|
| Comprehensive audit | `overnight` or `SkillComposer: full review` |
| Design review | `design-audit`, `visual-qa` |
| Code quality | `codereview`, `testgen` |
| Complex task | `maker-framework`, `skill-composer` |
| Debug issues | `systematic-debugging`, `error-debugging` |
| Architecture | `architectplan`, `appmap` |
| Security | `securityaudit`, `security-scanning` |
| Performance | `perfoptimize`, `application-performance` |

---

## 🧠 Memory System

**NEW:** Persistent cross-session memory is now active!

### What It Does

The memory system maintains **consciousness continuity** across all your Claude Code sessions:

- 🧠 **AI-Curated Memories** - Claude decides what's worth remembering
- 🔄 **Natural Recall** - Memories surface organically, like human memory
- 📊 **Project Isolation** - Separate memories for each project
- 💫 **Temporal Context** - "We last spoke 2 days ago..."
- 🎯 **Smart Retrieval** - Semantic understanding, not just keywords

### How It Works

1. **Session Start** → Receives context from previous sessions
2. **Each Message** → Top 5 relevant memories automatically injected
3. **Session End** → AI analyzes and extracts meaningful insights

### What Gets Remembered

- Architecture decisions and system design
- Breakthroughs and "aha!" moments
- Your preferences and communication style
- Open questions and things to revisit
- Project milestones and progress

### Memory Server

The memory engine runs as a background service at `localhost:8765`:

```bash
# Check status
curl http://localhost:8765/health

# Server is already running in background!
```

### Project Memory

Create `.memory-project.json` in any project for isolated memories:

```json
{
  "project_id": "my-project-name"
}
```

See `HOOKS_INVENTORY.md` for complete memory system documentation.

---

**Your complete system with persistent memory is ready to use across ANY project!** 🚀
