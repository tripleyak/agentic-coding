# SessionKickoff Skill

Fast, comprehensive project onboarding. **Triggers:** `kickoff`, `get up to speed`, `new session`, `onboard me`, `catch me up`

## Process

| Step | Action |
|------|--------|
| 1. Codebase scan | Run `codemap .` (if available) |
| 2. Git status | Branch, sync status, recent commits, stashes |
| 3. Read core docs | CLAUDE.md → SESSION_KICKOFF.md/SESSION_HANDOFF.md → BACKLOG.md → APP_MAP.md |
| 4. Check state | Uncommitted work, open PRs, failing tests |
| 5. Summarize | Project overview, current phase, priorities, blockers |

## Output Format

```
## Project: [name]
**Stack:** [tech stack]
**Current Phase:** [phase/milestone]

## State
- Branch: [branch] (synced/ahead/behind)
- Last commit: [message] ([time ago])
- Uncommitted: [yes/no]

## Top 3 Priorities
1. [priority from BACKLOG.md]
2. [priority]
3. [priority]

## Blockers/Issues
- [any blockers or none]

## Ready to Start
→ [recommended first task]
```

## Key Files to Read

| Priority | File | Purpose |
|----------|------|---------|
| 1 | CLAUDE.md | Project context, architecture, commands |
| 2 | SESSION_KICKOFF.md | Current session state |
| 3 | BACKLOG.md | Priority tasks |
| 4 | APP_MAP.md | Architecture/component map |
| 5 | MASTER_PLAN.md | Long-term roadmap (optional) |

**Fallback:** If files missing, infer from code structure + git history
