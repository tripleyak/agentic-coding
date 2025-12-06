description: Initialize session by reviewing all documentation and reporting readiness

You are starting a new working session. Take time to thoroughly review and synthesize the project context.

## Instructions

1. **Read Session Handoff** (if exists)
   - Review SESSION_HANDOFF.md for previous session state
   - Note: git branch, uncommitted changes, work completed, blockers

2. **Read Project Roadmap** (if exists)
   - Review ROADMAP.md for current priorities (P0, P1, P2)
   - Identify what's in progress vs pending

3. **Read Architecture** (if exists)
   - Review APP_MAP.md for component structure
   - Understand key files and their relationships

4. **Read Project Instructions**
   - Review CLAUDE.md for project-specific commands and patterns

5. **Check Git State**
   - Run `git status` to see current branch and changes
   - Run `git log -3 --oneline` to see recent commits

## Output Format

After reviewing, provide a concise status report:

```
## Session Ready

**Project:** [name]
**Branch:** [current branch]
**Last Session:** [summary from SESSION_HANDOFF or "No previous handoff found"]

### Current State
- [uncommitted changes or "Clean working tree"]
- [any blockers identified]

### Top Priorities
1. [P0 priority from ROADMAP]
2. [next priority]
3. [next priority]

---

Ready to work. What would you like to focus on?
```

## Important

- Use extended thinking to thoroughly process the documentation
- Be concise in your output - the user has context, just needs the summary
- If files don't exist, note that and continue with what's available
- Always end by asking what to focus on first
