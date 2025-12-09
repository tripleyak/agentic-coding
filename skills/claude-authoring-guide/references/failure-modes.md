# AI Agent Failure Modes & Mitigations

Understanding how AI agents fail and how to prevent or recover from failures.

## Failure Mode Taxonomy

### 1. Hallucination

**Problem:** Agent generates plausible but factually incorrect output

**Symptoms:**
- Confident statements about non-existent features
- Made-up function names or APIs
- Incorrect documentation references

**Mitigations:**
| Strategy | Implementation |
|----------|----------------|
| Ground in verified data | Use RAG with authoritative sources |
| Require evidence | Ask for code references, file paths |
| Cross-reference | Verify against actual codebase |
| Extended thinking | Use thinking mode for complex claims |

**Detection:**
- Claims without file path references
- "I believe" or "typically" for specific facts
- API calls that don't exist in docs

### 2. Context Window Limits

**Problem:** Agent forgets critical details from earlier in conversation

**Symptoms:**
- Repeating already-discussed solutions
- Forgetting constraints mentioned earlier
- Losing track of multi-step tasks

**Mitigations:**
| Strategy | Implementation |
|----------|----------------|
| Proactive handoff | Trigger at 10% remaining context |
| External memory | Use memory hooks, git history |
| Summarization | Compress lengthy outputs |
| Task tracking | TodoWrite tool for progress |

**Detection:**
- Questions about previously answered topics
- Contradicting earlier statements
- "Starting fresh" in middle of task

### 3. Prompt Injection

**Problem:** Malicious inputs hijack agent behavior

**Attack Chain:**
```
Attacker input → Injected into prompt → Agent treats as instruction → Executes malicious action
```

**Mitigations:**
| Strategy | Implementation |
|----------|----------------|
| Input sanitization | Never inject untrusted input directly |
| Tool restrictions | Limit agent's available tools |
| Output validation | Treat AI output as untrusted |
| Architectural separation | Separate system/user input channels |

**High-Risk Scenarios:**
- Processing GitHub issues/PRs
- Analyzing user-submitted content
- Automated workflows with external input

### 4. Inadequate Training Data

**Problem:** Agent fails on edge cases or newer technologies

**Symptoms:**
- Outdated library versions
- Missing recent API changes
- Unfamiliar with new frameworks

**Mitigations:**
| Strategy | Implementation |
|----------|----------------|
| Explicit documentation | Provide up-to-date docs in context |
| Version specification | State versions explicitly |
| Web search | Use WebSearch for current info |
| Active learning | Document failures for future reference |

### 5. Poor Error Handling

**Problem:** Agent crashes or produces cryptic errors

**Symptoms:**
- Unhandled exceptions
- Generic error messages
- Silent failures

**Mitigations:**
| Strategy | Implementation |
|----------|----------------|
| Circuit breakers | Limit retry attempts |
| Graceful fallbacks | Default behaviors on failure |
| Explicit error reporting | Clear, actionable error messages |
| Hooks never crash | Always wrap in try/except |

### 6. Inconsistent Output

**Problem:** Unpredictable formatting or structure

**Symptoms:**
- Varying output formats
- Inconsistent naming conventions
- Structure changes between runs

**Mitigations:**
| Strategy | Implementation |
|----------|----------------|
| Output templates | Specify exact format expected |
| Structured generation | Use defined schemas |
| Examples in prompts | Show expected output format |
| Validation scripts | Verify output structure |

### 7. Latency Bottlenecks

**Problem:** Slow responses impact workflow

**Symptoms:**
- Long waits for responses
- Timeouts on complex tasks
- User frustration

**Mitigations:**
| Strategy | Implementation |
|----------|----------------|
| Caching | Store reusable results |
| Progressive responses | Stream output as available |
| Parallel execution | Run independent tasks concurrently |
| Model selection | Use faster models for simple tasks |

## Red Flag Detection

### Automatic Detection Criteria

Flag responses exhibiting:

| Red Flag | Detection | Action |
|----------|-----------|--------|
| Excessive length | Response >3x expected | Stop, decompose smaller |
| Uncertainty language | "might", "possibly", "I think" | Verify before proceeding |
| Format violations | Output doesn't match expected | Regenerate with clearer spec |
| Scope creep | Addresses more than asked | Refocus on original task |
| Missing outputs | Expected artifacts absent | Explicitly request missing items |

### User-Detected Flags

Flag when you observe:
- Result feels incomplete
- Something seems off (trust intuition)
- Step took much longer than expected
- Required unexpected workarounds

## Recovery Procedures

### When Hallucination Detected

```
1. Stop and acknowledge potential inaccuracy
2. Request file path and line number references
3. Verify against actual codebase
4. Correct with evidence-based information
```

### When Context Lost

```
1. Generate context handoff document
2. Save to persistent storage
3. Start fresh session
4. Load handoff at session start
```

### When Prompt Injection Suspected

```
1. Stop execution immediately
2. Review input for malicious content
3. Quarantine affected session
4. Report security concern
```

### When Stuck in Loop

```
1. Break the loop explicitly
2. Decompose into smaller steps
3. Try different approach
4. Escalate to user if repeated failures
```

## Prevention Checklist

Before deploying agents or skills:

- [ ] Hallucination: Requires evidence for claims?
- [ ] Context: Handoff strategy defined?
- [ ] Injection: Untrusted input handled safely?
- [ ] Training: Recent/relevant docs provided?
- [ ] Errors: Graceful failure implemented?
- [ ] Output: Format specified clearly?
- [ ] Latency: Timeout limits set?

## Key Principles

1. **Never trust, always verify** - Treat all AI output as requiring validation
2. **Fail gracefully** - Every component should handle errors without crashing
3. **Preserve context** - Use external storage for important state
4. **Limit blast radius** - Constrain what agents can do
5. **Monitor and detect** - Watch for red flags during execution
