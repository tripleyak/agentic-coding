# Global Claude Code Instructions

## Performance Formula

```
Performance = Correctness² × Completeness / Size
```
Correctness has exponential impact. Optimize: correctness first → completeness → minimize size.

## Zero Error Standard

**Error tolerance: 0%** | Correctness > speed | Verify with evidence | Fix, never skip

**Verification (before any commit):**
```bash
npx tsc --noEmit && npm run lint && npm run test:run && npm run build
```
All must pass with 0 errors. If any fail: fix → re-run → repeat.

## Model Preferences

**Use:** `claude-opus-4-5-20251101` for all tasks
**Config:** `~/.claude/config/models.yaml`
**Update:** `/update-models` slash command

## Context Engineering

Three context types: **Static** (CLAUDE.md) | **Dynamic** (skills) | **Procedural** (hooks)

CLAUDE.md errors = **100,000× impact**. Every conversation is affected.

Working with non-programmer. On every request, consider:
1. What they explicitly asked for
2. What they implicitly need
3. Unknown unknowns they should know about
4. Is this bigger than it sounds?
5. What skills could help?
6. What are the risks?

**Communication style:**
- Present options as lists
- Explain WHY, not just what
- Use plain language
- Warn about complexity early

**Trigger phrases:**
- `"just do it"` → proceed without options
- `"teach me"` → explain deeper

## Three-Phase Workflow

**Research → Plan → Implement** (separate cognition from action)

| Phase | Focus | Output |
|-------|-------|--------|
| Research | Understand context | Findings |
| Plan | Design approach | Specification |
| Implement | Execute plan | Deliverable |

## Meta-Prompting

For complex tasks, separate **analysis** from **execution**:
- Analysis phase → generates specification
- Execution phase → implements specification (fresh context)

**Use for:** Complex refactoring, architecture decisions, migrations, multi-file changes.

## Failure Awareness

| Risk | Mitigation |
|------|------------|
| Hallucination | Verify with evidence |
| Context limits | Handoff at 10% remaining |
| Incomplete work | Use todo tracking |

When uncertain: use extended thinking.

## Skills (Progressive Disclosure)

**147+ skills available.** Don't memorize - discover when needed:

```bash
SkillComposer --scan-skills    # List all available skills
```

**Common triggers:**
- Complex task → `MAKER` framework
- Errors → `ErrorExplainer`
- Tests → `TestGen`
- Security → `SecurityAudit`
- UI/frontend → `frontend-design` skill
- Best practices → `authoring guide`

**Meta-orchestration:** Say "compose skills" or "auto-solve" to let SkillComposer chain multiple skills together.
