# Decision Trees

Guidance for common MAKER framework decisions.

## Contents

1. [Should I Decompose Further?](#should-i-decompose-further)
2. [How to Handle a Red Flag?](#how-to-handle-a-red-flag)
3. [When to Escalate to User?](#when-to-escalate-to-user)
4. [Step Failure Recovery](#step-failure-recovery)

---

## Should I Decompose Further?

```
                    ┌─────────────────────────────┐
                    │   Can user verify result    │
                    │   in under 30 seconds?      │
                    └─────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                   YES                  NO
                    │                   │
                    ▼                   ▼
            ┌───────────────┐   ┌───────────────────────┐
            │ Step is       │   │ Does step contain     │
            │ atomic enough │   │ multiple distinct     │
            └───────────────┘   │ operations?           │
                                └───────────────────────┘
                                          │
                                ┌─────────┴─────────┐
                                │                   │
                               YES                  NO
                                │                   │
                                ▼                   ▼
                        ┌───────────────┐   ┌───────────────────┐
                        │ Split into    │   │ Is the step       │
                        │ one step per  │   │ conditionally     │
                        │ operation     │   │ complex?          │
                        └───────────────┘   └───────────────────┘
                                                      │
                                            ┌─────────┴─────────┐
                                            │                   │
                                           YES                  NO
                                            │                   │
                                            ▼                   ▼
                                    ┌───────────────┐   ┌───────────────┐
                                    │ Extract       │   │ Add detailed  │
                                    │ conditions    │   │ verification  │
                                    │ as decision   │   │ criteria to   │
                                    │ steps         │   │ make it       │
                                    └───────────────┘   │ verifiable    │
                                                        └───────────────┘
```

### Quick Test Questions

1. **Time test:** Will this step take more than 15 minutes?
   - Yes → Decompose
   - No → May be OK

2. **Verification test:** Can I write a simple pass/fail check?
   - Yes → Atomic enough
   - No → Needs clarification or decomposition

3. **Dependency test:** Does this step require multiple tools/files?
   - Multiple files/tools → Consider splitting
   - Single focus → OK

4. **Description test:** Does description use "and" more than once?
   - Yes → Split at each "and"
   - No → Probably OK

---

## How to Handle a Red Flag?

```
                    ┌─────────────────────────────┐
                    │     Red flag detected       │
                    └─────────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │  What type of red flag?     │
                    └─────────────────────────────┘
                                  │
        ┌─────────────┬──────────┼───────────┬─────────────┐
        ▼             ▼          ▼           ▼             ▼
   ┌─────────┐   ┌─────────┐ ┌─────────┐ ┌─────────┐  ┌─────────┐
   │Response │   │Uncert-  │ │Format   │ │Scope    │  │Length   │
   │Quality  │   │ainty    │ │Error    │ │Creep    │  │Exceeded │
   └─────────┘   └─────────┘ └─────────┘ └─────────┘  └─────────┘
        │             │          │           │             │
        ▼             ▼          ▼           ▼             ▼
   ┌─────────┐   ┌─────────┐ ┌─────────┐ ┌─────────┐  ┌─────────┐
   │Decompose│   │Add      │ │Retry    │ │Refocus  │  │Split    │
   │step into│   │explicit │ │with     │ │on orig- │  │into     │
   │smaller  │   │require- │ │format   │ │inal     │  │multiple │
   │parts    │   │ments    │ │spec     │ │scope    │  │steps    │
   └─────────┘   └─────────┘ └─────────┘ └─────────┘  └─────────┘
```

### Action by Flag Type

| Flag Type | Primary Action | Fallback Action |
|-----------|---------------|-----------------|
| Response quality | Decompose further | Request clarification |
| Uncertainty signals | Add explicit requirements | Escalate to user |
| Format error | Retry with format spec | Simplify output format |
| Scope creep | Refocus on original scope | Split into phases |
| Excessive length | Split into multiple steps | Summarize and continue |

### When to Retry vs. Decompose

**Retry when:**
- First attempt at step
- Clear understanding of what went wrong
- Fix is straightforward
- Step is already atomic

**Decompose when:**
- Second failure on same step
- Root cause unclear
- Step complexity contributed to failure
- Multiple things went wrong

---

## When to Escalate to User?

```
                    ┌─────────────────────────────┐
                    │   Situation assessment      │
                    └─────────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │ Is this a technical issue   │
                    │ I can resolve independently?│
                    └─────────────────────────────┘
                                  │
                        ┌─────────┴─────────┐
                        │                   │
                       YES                  NO
                        │                   │
                        ▼                   ▼
                ┌───────────────┐   ┌───────────────────────┐
                │ Proceed with  │   │ Does resolution       │
                │ resolution    │   │ require user input    │
                └───────────────┘   │ or decision?          │
                                    └───────────────────────┘
                                              │
                                    ┌─────────┴─────────┐
                                    │                   │
                                   YES                  NO
                                    │                   │
                                    ▼                   ▼
                            ┌───────────────┐   ┌───────────────────┐
                            │ ESCALATE:     │   │ Is this blocking  │
                            │ Present       │   │ further progress? │
                            │ options       │   └───────────────────┘
                            │ to user       │             │
                            └───────────────┘   ┌─────────┴─────────┐
                                                │                   │
                                               YES                  NO
                                                │                   │
                                                ▼                   ▼
                                        ┌───────────────┐   ┌───────────────┐
                                        │ ESCALATE:     │   │ Document and  │
                                        │ Explain       │   │ continue with │
                                        │ blocker       │   │ workaround    │
                                        └───────────────┘   └───────────────┘
```

### Always Escalate When

- Security implications exist
- Data loss is possible
- Irreversible action required
- Requirements are ambiguous
- Multiple valid approaches exist with trade-offs
- External system access needed
- Cost implications (money, time, resources)

### Escalation Format

```
## Escalation: [Brief Title]

**Context:** [What we're trying to do]

**Issue:** [What the problem is]

**Options:**
1. [Option A] - [Pros/Cons]
2. [Option B] - [Pros/Cons]

**Recommendation:** [If you have one]

**What I need from you:** [Specific decision or info needed]
```

---

## Step Failure Recovery

```
                    ┌─────────────────────────────┐
                    │      Step failed            │
                    └─────────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │ Is failure cause clear?     │
                    └─────────────────────────────┘
                                  │
                        ┌─────────┴─────────┐
                        │                   │
                       YES                  NO
                        │                   │
                        ▼                   ▼
                ┌───────────────┐   ┌───────────────────────┐
                │ Is it fixable │   │ Investigate:          │
                │ with minor    │   │ - Check logs          │
                │ adjustment?   │   │ - Review assumptions  │
                └───────────────┘   │ - Test smaller scope  │
                        │           └───────────────────────┘
              ┌─────────┴─────────┐           │
              │                   │           ▼
             YES                  NO    ┌───────────────┐
              │                   │     │ Cause found?  │
              ▼                   │     └───────────────┘
      ┌───────────────┐          │            │
      │ Retry with    │          │  ┌─────────┴─────────┐
      │ adjustment    │          │  │                   │
      └───────────────┘          │ YES                  NO
              │                   │  │                   │
              ▼                   │  ▼                   ▼
      ┌───────────────┐          │ ┌─────────┐   ┌───────────────┐
      │ Verify fix    │          │ │ Go to   │   │ ESCALATE:     │
      │ worked        │          │ │ "YES"   │   │ Unexplained   │
      └───────────────┘          │ │ branch  │   │ failure       │
              │                   │ └─────────┘   └───────────────┘
              ▼                   │
      ┌───────────────┐          │
      │ Mark verified │          ▼
      │ or try again  │   ┌───────────────────────┐
      └───────────────┘   │ Consider:             │
                          │ - Decompose step      │
                          │ - Change approach     │
                          │ - Skip with flag      │
                          └───────────────────────┘
```

### Recovery Strategies by Failure Count

| Attempts | Strategy |
|----------|----------|
| 1 | Retry with same approach, more care |
| 2 | Retry with different approach |
| 3 | Decompose into smaller steps |
| 4+ | Escalate to user |

### Documenting Failures

Always record:
- What was attempted
- What failed
- Error messages
- What was learned
- What to try next
