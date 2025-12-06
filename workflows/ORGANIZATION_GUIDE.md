# Global Claude Code Organization Guide

**Purpose:** Build a reusable, project-agnostic system for any codebase

---

## Philosophy: Global vs Project-Specific

### ✅ Global (~/.claude/)
**Belongs here if:**
- Works for ANY project/codebase
- Reusable workflow templates
- Generic skills and commands
- Universal hooks and configurations

**Examples:**
- Workflow templates (overnight, maker)
- Skills (design-audit, code-review, test-gen)
- Generic commands (build, check, debug)
- Auto-formatting hooks

### ❌ Project-Specific (project/.claude/)
**Belongs here if:**
- Specific to one project's domain
- Uses project-specific terminology
- Hardcoded file paths or structure
- Project-specific context

**Examples:**
- Commands like "add-product", "add-retailer"
- Project-specific MAKER task files
- Project documentation (CLAUDE.md, APP_MAP.md)

---

## Complete Directory Structure

```
~/.claude/
│
├── CLAUDE.md                          # Global instructions (22KB)
├── IMPROVEMENT_BACKLOG.md             # Global improvement tracking
├── settings.json                      # Hooks config (11 hooks)
│
├── workflows/                         # 🎯 Workflow templates & docs
│   ├── README.md                      # Workflows overview
│   ├── OVERNIGHT_CONFIG.md            # 7-hour autonomous config
│   ├── OVERNIGHT_TASKS.md             # Overnight task template
│   ├── SKILLS_INVENTORY.md            # 237+ skills catalog
│   ├── HOOKS_INVENTORY.md             # 11 hooks documentation
│   └── ORGANIZATION_GUIDE.md          # This file
│
├── skills/                            # 🎨 Custom skills (40)
│   ├── skill-composer/                # Meta-orchestrator
│   ├── maker-framework/               # Systematic decomposition
│   ├── design-audit/                  # 8-agent design analysis
│   ├── visual-qa/                     # Screenshot testing
│   ├── codereview/                    # Multi-agent review
│   ├── architectplan/                 # System design
│   ├── appmap/                        # Sitemap generation
│   ├── securityaudit/                 # OWASP scanning
│   ├── testgen/                       # Test generation
│   ├── deploymentguide/               # Deployment automation
│   └── ... (30 more)
│
├── commands/                          # 🎮 Global slash commands (21)
│   ├── brainstorm.md                  # Interactive design
│   ├── execute-plan.md                # Execute with checkpoints
│   ├── write-plan.md                  # Create implementation plan
│   ├── build.md                       # Build project
│   ├── check.md                       # Run checks
│   ├── debug.md                       # Debug mode
│   ├── deps.md                        # Dependency audit
│   ├── todo.md                        # Todo management
│   └── ... (13 more)
│
└── plugins/
    ├── cache/
    │   └── superpowers/
    │       ├── skills/                # 🦸 Superpowers skills (29)
    │       │   ├── brainstorming/
    │       │   ├── systematic-debugging/
    │       │   ├── test-driven-development/
    │       │   ├── using-git-worktrees/
    │       │   └── ... (25 more)
    │       └── hooks/
    │
    └── marketplaces/
        ├── claude-code-workflows/
        │   └── plugins/               # 🌐 Workflow plugins (168+ skills)
        │       ├── backend-development/
        │       ├── frontend-mobile-development/
        │       ├── kubernetes-operations/
        │       ├── security-compliance/
        │       └── ... (62 more)
        │
        └── claude-code-plugins/
            ├── frontend-design/
            ├── hookify/
            ├── plugin-dev/
            └── ...
```

---

## Project Structure Example

```
~/ShelfWins-Studio/                    # Example project
│
├── .claude/                           # Project-specific only
│   └── commands/                      # Project commands
│       ├── add-product.md             # ❌ Project-specific
│       ├── add-retailer.md            # ❌ Project-specific
│       ├── component.md               # ❌ Project-specific
│       └── modal.md                   # ❌ Project-specific
│
├── CLAUDE.md                          # Project documentation
├── APP_MAP.md                         # Project sitemap
├── MASTER_PLAN.md                     # Project roadmap
├── SESSION_KICKOFF.md                 # Project session state
├── *.maker.json                       # Project MAKER tasks
│
└── [project source code...]
```

---

## How Global System Works Across Projects

### Example: Using Overnight Mode

**In ShelfWins-Studio:**
```bash
cd ~/ShelfWins-Studio
overnight
```
→ Runs on ShelfWins-Studio files

**In Any Other Project:**
```bash
cd ~/my-other-project
overnight
```
→ Runs on my-other-project files

**Same workflow, different projects!**

---

## Skill Discovery & Usage

### Finding Skills

```bash
# Quick search
ls ~/.claude/skills/ | grep design

# Full search across all sources
find ~/.claude -name "*design*" -type d | grep skills

# Use SkillComposer to scan everything
SkillComposer --scan-skills
```

### Using Skills

```
# Direct invocation
design-audit

# Via SkillComposer
SkillComposer: Run design audit and visual QA on current project

# Via SkillRecommender
SkillRecommender: which skill for UI testing?
```

---

## Hooks: Universal Automation

Hooks in `~/.claude/settings.json` apply to ALL projects:

| Hook | Effect on ANY Project |
|------|----------------------|
| Edit/Write + Prettier | Auto-formats all JS/TS edits |
| Bash output analysis | Catches test/build failures everywhere |
| Task verification | Ensures quality subagents everywhere |
| NVM path | Node available in all projects |

---

## Creating New Global Skills

### When to Create Global Skill

✅ **Create if:**
- Applies to multiple project types
- Reusable workflow pattern
- Generic domain (testing, security, performance)
- No hardcoded paths/names

❌ **Don't create if:**
- Only for one specific project
- Hardcoded business logic
- Project-specific terminology

### Where to Create

```bash
# Custom skills
~/.claude/skills/my-new-skill/

# Or contribute to plugin
~/.claude/plugins/marketplaces/claude-code-plugins/plugins/my-plugin/skills/
```

---

## Quick Reference: Where Does X Go?

| Item | Global | Project | Reason |
|------|--------|---------|--------|
| Overnight workflow | ✅ | ❌ | Works on any project |
| Design audit skill | ✅ | ❌ | Generic UI analysis |
| "add-product" command | ❌ | ✅ | Specific to domain |
| Prettier hook | ✅ | ❌ | Applies to all code |
| MAKER task file | ❌ | ✅ | Specific to project work |
| Test-gen skill | ✅ | ❌ | Generic testing |
| API documentation | ❌ | ✅ | Project-specific |
| Code review skill | ✅ | ❌ | Universal quality check |

---

## Maintenance Commands

```bash
# View global structure
tree -L 2 ~/.claude/

# Count skills by source
echo "Custom: $(ls -1 ~/.claude/skills/ | wc -l)"
echo "Superpowers: $(find ~/.claude/plugins/cache/superpowers/skills -name "*.md" | wc -l)"
echo "Workflows: $(find ~/.claude/plugins/marketplaces/claude-code-workflows -name "*.md" -path "*/skills/*" | wc -l)"

# View hooks summary
cat ~/.claude/settings.json | jq '.hooks | keys'

# Backup entire config
tar -czf ~/claude-backup-$(date +%Y%m%d).tar.gz ~/.claude/

# Search for specific capability
grep -r "screenshot" ~/.claude/skills/*/
```

---

## Benefits of This Organization

1. **Portability** - Same tools work across all projects
2. **Consistency** - Uniform workflows everywhere
3. **Efficiency** - No duplication of generic tools
4. **Scalability** - Add projects without recreating setup
5. **Maintainability** - Update once, apply everywhere
6. **Discovery** - All tools in predictable locations

---

## Migration Guide

**Moving from Project-Specific to Global:**

1. Identify generic vs. specific files
2. Move generic files to `~/.claude/`
3. Update any hardcoded paths to be dynamic
4. Test in multiple projects
5. Document in inventories

**Example:**
```bash
# If a skill works anywhere
mv ~/project/.claude/skills/generic-skill ~/.claude/skills/

# If a command is project-specific, keep it
# ~/project/.claude/commands/add-product.md stays put
```

---

## Next Steps

1. ✅ Workflows organized in `~/.claude/workflows/`
2. ✅ Inventories created (skills, hooks, organization)
3. ✅ Documentation complete
4. 🎯 Ready to use system across ANY project!

**To use in new project:**
```bash
cd ~/new-project
overnight  # Uses global workflow
design-audit  # Uses global skill
/brainstorm  # Uses global command
# All hooks active automatically!
```
