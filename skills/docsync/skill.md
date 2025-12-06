# DocSync Skill

Comprehensive autonomous documentation synchronization with full transparency. **Triggers:** `update docs`, `sync docs`, `DocSync`

## Documentation Files (Always Scanned)

| File | Purpose | Action |
|------|---------|--------|
| **CLAUDE.md** | Technical reference for developers | Update architecture, hooks, features, phases; preserve custom content |
| **README.md** | User-facing project documentation | Sync tech stack, features, getting started, architecture |
| **APP_MAP.md** | Current state & feature inventory | Update component counts, stats, recent changes |
| **BACKLOG.md** | Task tracking & priorities | Mark completed items, add new issues, update P0-P3 sections |
| **SESSION_KICKOFF.md** | Quick reference for dev sessions | Update current sprint, stats, priorities |
| **MASTER_PLAN.md** | Long-term roadmap & milestones | Add completion notes, update milestone status |
| **CHANGELOG.md** | Version history & changes | Add new entries, format by semantic commit type |
| **docs/SESSION_LOG.md** | Session notes & progress | Add new session entries at top |
| **SESSION_HANDOFF.md** | Session handoff notes | Replace with current state |
| **DEV_PLAN*.md** | Development plans | Mark completed items, archive or delete stale plans |

## Discovery Process

1. **Scan Project Root:** Find all `.md` files in project root and `docs/` directory
2. **Auto-Detect Files:** Identify documentation files by name patterns
3. **Read Current State:** Read all discovered documentation files
4. **Analyze Code Changes:** Detect what changed since last doc update (via git diff or recent commits)

## Update Decision Matrix

For each discovered documentation file, the skill will:

| Criteria | Action |
|----------|--------|
| **File exists & matches known pattern** | Update with changes |
| **File exists but unknown pattern** | Report as "Found but skipped" with reason |
| **Known file missing** | Report as "Expected but not found" |
| **Outdated content detected** | Flag as ⚠OUTDATED and update |
| **Accurate content** | Flag as ✓ACCURATE, skip update |
| **Obsolete content** | Flag as ✗OBSOLETE, suggest cleanup |
| **Missing critical info** | Flag as ?MISSING, add content |

## Execution Strategy

**3 Parallel Opus Agents:**

### Agent 1: Architecture & Technical Docs
- **Files:** CLAUDE.md, README.md (tech sections), MASTER_PLAN.md
- **Updates:** Architecture diagrams, tech stack, hooks, components, services, utilities
- **Preserves:** Custom instructions, user preferences, special notes

### Agent 2: Features & State Tracking
- **Files:** APP_MAP.md, BACKLOG.md, SESSION_KICKOFF.md
- **Updates:** Feature status, component counts, statistics, priorities, current sprint
- **Actions:** Mark completed items, add new issues, update P0-P3 priorities

### Agent 3: History & Changes
- **Files:** CHANGELOG.md, docs/SESSION_LOG.md, SESSION_HANDOFF.md
- **Updates:** Add new entries, format by semantic commits, record session work
- **Format:** Consistent date formatting, semantic grouping (feat/fix/refactor/docs)

## Transparency Report (Always Generated)

At the end of execution, DocSync MUST provide this report:

```markdown
## DocSync Report - [Date]

### Files Updated (X)
- ✅ CLAUDE.md (updated architecture, added 2 hooks, updated Phase 10)
- ✅ README.md (updated hook count, enhanced features section)
- ✅ APP_MAP.md (updated stats, added recent changes)
- ✅ BACKLOG.md (added P0 issues, marked Phase 10 complete)
- ✅ SESSION_KICKOFF.md (updated sprint priorities)
- ✅ MASTER_PLAN.md (added completion note)
- ✅ docs/SESSION_LOG.md (added new session entry)

### Files Skipped (Y)
- ⏭️ CHANGELOG.md (reason: no version bump detected)
- ⏭️ SESSION_HANDOFF.md (reason: file doesn't exist in project)
- ⏭️ custom-doc.md (reason: unknown format, not standard doc file)

### Files Not Found (Z)
- ❌ DEV_PLAN.md (expected but missing - may have been deleted)

### Changes Summary
| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Components | 138 | 145 | +7 |
| Hooks | 34 | 36 | +2 |
| Tests | 202 | 242 | +40 |
| [other metrics] | ... | ... | ... |

### Audit Results
- ✓ACCURATE: 5 sections verified correct
- ⚠OUTDATED: 3 sections updated
- ✗OBSOLETE: 1 section removed
- ?MISSING: 2 sections added

### What Was Changed
[Brief summary of major changes made]

### Verification
- [x] All file paths verified
- [x] No broken links
- [x] Consistent formatting
- [x] Dates updated
```

## Core Principles

1. **Comprehensive by Default:** Scan and consider ALL documentation files, not just a subset
2. **Explicit Skipping:** If a file is intentionally skipped, report WHY
3. **Full Transparency:** User always knows what was updated, what was skipped, and why
4. **Preserve Custom Content:** Never delete user-written sections, notes, or custom instructions
5. **Atomic Updates:** Update all files or none (rollback on failure)
6. **Minimal & Accurate:** Match current code state exactly, no placeholders or future promises
7. **Consistent Formatting:** Maintain existing doc formatting styles
8. **Aggressive Cleanup:** Remove obsolete sections, outdated TODOs, completed plans

## Error Handling

| Error | Action |
|-------|--------|
| File read failure | Report error, continue with other files |
| Parse error | Report malformed content, skip update, notify user |
| Write failure | Rollback all changes, report error |
| Conflicting updates | Prefer code truth over doc assumptions |
| Missing dependencies | Report what's needed (e.g., git history) |

## Commands

| Command | Behavior |
|---------|----------|
| `DocSync` | Full scan and update of all documentation |
| `DocSync --dry-run` | Show what would be updated without making changes |
| `DocSync --files="CLAUDE.md,README.md"` | Update only specified files |
| `DocSync --verify` | Check docs for outdated content without updating |
| `DocSync --report` | Generate transparency report only |

## Integration with Other Skills

- **After completing major features:** Run DocSync automatically
- **Before git commits:** Suggest running DocSync if docs outdated
- **With SkillComposer:** Include as final step in workflows
- **With MAKER:** Update docs after each milestone

## Success Criteria

✅ All documentation files synchronized with codebase
✅ User has full visibility into what changed
✅ No information lost from existing docs
✅ Consistent formatting across all files
✅ Accurate reflection of current code state
✅ Clear reporting of skipped/missing files

## Example Workflow

```
User: "DocSync"

Agent:
1. Scan project for all .md files
2. Identify 10 documentation files (7 standard + 3 custom)
3. Launch 3 Opus agents to analyze and update
4. Agent 1: Updates CLAUDE.md, README.md, MASTER_PLAN.md
5. Agent 2: Updates APP_MAP.md, BACKLOG.md, SESSION_KICKOFF.md
6. Agent 3: Updates docs/SESSION_LOG.md
7. Skips CHANGELOG.md (no version bump)
8. Skips custom-notes.md (unknown format)
9. Reports DEV_PLAN.md missing but expected
10. Generates comprehensive transparency report
11. Shows user exactly what was updated and why
```

This ensures the user ALWAYS knows what DocSync did, what it didn't do, and why.
