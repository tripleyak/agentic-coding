# Thinking Models: 11 Mental Frameworks for Analysis

Structured approaches to problem-solving that improve the quality of AI analysis.

## Overview

These mental frameworks help break down complex problems systematically. Use them during the Research and Planning phases to ensure thorough analysis.

---

## 1. First Principles

**Core Question:** What are the fundamental truths? What can we build from scratch?

**Process:**
1. Identify the core problem
2. Break down to basic components
3. Question every assumption
4. Rebuild from foundational truths

**Use When:**
- Existing solutions seem overcomplicated
- Conventional wisdom isn't working
- Need innovative approach

**Example:**
```
Problem: "Authentication is slow"
First Principles:
- What does authentication actually need to do?
- What's the minimum data required?
- Why are we checking X, Y, Z?
Result: Remove unnecessary checks, 10x speedup
```

---

## 2. Pareto Analysis (80/20 Rule)

**Core Question:** Which 20% of inputs produce 80% of results?

**Process:**
1. List all factors/causes
2. Measure impact of each
3. Rank by impact
4. Focus on top 20%

**Use When:**
- Limited time/resources
- Need to prioritize
- Optimization tasks

**Example:**
```
Problem: "App is slow"
Pareto Analysis:
- 3 API calls cause 85% of load time
- Focus: Optimize these 3 calls first
- Ignore: 47 other minor issues (for now)
```

---

## 3. Inversion

**Core Question:** What would guarantee failure? How do we avoid that?

**Process:**
1. Define success
2. List all ways to fail
3. Create anti-patterns list
4. Build solution that avoids failures

**Use When:**
- Stakes are high
- Need to identify risks
- Defensive planning

**Example:**
```
Problem: "Design authentication system"
Inversion:
- How to guarantee a security breach?
  - Store passwords in plain text
  - No rate limiting
  - No session expiration
- Solution: Explicitly avoid each failure mode
```

---

## 4. Second-Order Effects

**Core Question:** What happens after the obvious consequences?

**Process:**
1. Identify immediate effects
2. For each effect, ask "then what?"
3. Map the chain of consequences
4. Plan for downstream impacts

**Use When:**
- System changes
- Policy decisions
- Architecture choices

**Example:**
```
Change: "Add caching layer"
First Order: Faster responses ✓
Second Order:
- Stale data issues
- Cache invalidation complexity
- Memory pressure
- New failure modes to handle
```

---

## 5. Pre-Mortem

**Core Question:** Assuming this failed, why did it fail?

**Process:**
1. Imagine complete failure
2. List all reasons it could have failed
3. Prioritize by likelihood × impact
4. Mitigate top risks proactively

**Use When:**
- Before starting complex projects
- High-stakes decisions
- Team alignment on risks

**Example:**
```
Project: "Database migration"
Pre-Mortem:
- "The migration failed because..."
  - We didn't account for foreign keys
  - Downtime exceeded window
  - Rollback script wasn't tested
- Action: Address each before starting
```

---

## 6. Devil's Advocate

**Core Question:** What's the strongest argument against this approach?

**Process:**
1. State your position clearly
2. Actively argue the opposite
3. Find legitimate concerns
4. Strengthen or abandon position

**Use When:**
- Evaluating options
- Avoiding confirmation bias
- Group decisions

**Example:**
```
Position: "We should use microservices"
Devil's Advocate:
- Operational complexity increases 10x
- Team lacks distributed systems experience
- Current monolith isn't the bottleneck
- Network latency could negate benefits
Result: Hybrid approach selected
```

---

## 7. Systems Thinking

**Core Question:** How do the parts interact? What are the feedback loops?

**Process:**
1. Map system components
2. Identify relationships
3. Find feedback loops
4. Locate leverage points

**Use When:**
- Complex systems
- Unexpected behaviors
- Root cause analysis

**Example:**
```
Problem: "Performance degrades over time"
Systems Analysis:
- Memory usage → GC pressure → Latency spikes
- Latency spikes → User retries → More load
- Feedback loop: Load → Degradation → More load
Solution: Break the loop at leverage point (rate limiting)
```

---

## 8. Opportunity Cost

**Core Question:** What are we giving up by choosing this?

**Process:**
1. List all options
2. For each, identify what's sacrificed
3. Quantify trade-offs
4. Make informed choice

**Use When:**
- Resource allocation
- Technology choices
- Time management

**Example:**
```
Choice: "Build custom vs buy SaaS"
Custom Build Opportunity Cost:
- 3 months developer time
- Could ship 2 other features instead
- Could reduce tech debt instead
SaaS Opportunity Cost:
- $500/month ongoing
- Vendor lock-in
- Less customization
```

---

## 9. Constraint Analysis

**Core Question:** What are the real constraints? Which are self-imposed?

**Process:**
1. List all perceived constraints
2. Classify: Hard (real) vs Soft (assumed)
3. Challenge soft constraints
4. Work within hard constraints

**Use When:**
- Feeling stuck
- "Impossible" requirements
- Creative solutions needed

**Example:**
```
Perceived Constraints:
- "Must use legacy database" → Hard (contractual)
- "Can't change API format" → Soft (just convention)
- "Must support IE11" → Check actual usage (0.1%)
Action: Challenge soft constraints, unlock new solutions
```

---

## 10. Root Cause Analysis (5 Whys)

**Core Question:** Why did this happen? (Asked 5 times)

**Process:**
1. State the problem
2. Ask "Why?"
3. For the answer, ask "Why?" again
4. Repeat until root cause emerges
5. Address root cause, not symptoms

**Use When:**
- Debugging
- Post-mortems
- Recurring issues

**Example:**
```
Problem: "Production crashed"
1. Why? → Server ran out of memory
2. Why? → Memory leak in worker process
3. Why? → Unclosed database connections
4. Why? → Missing cleanup in error handler
5. Why? → No code review caught it

Root Cause: Code review process gap
Action: Add static analysis for resource leaks
```

---

## 11. Comparative Analysis

**Core Question:** How do the options stack up against each other?

**Process:**
1. Define evaluation criteria
2. Weight criteria by importance
3. Score each option
4. Calculate weighted totals
5. Consider intangibles

**Use When:**
- Multiple viable options
- Technology selection
- Vendor evaluation

**Example:**
```
Options: Framework A vs B vs C

| Criteria       | Weight | A | B | C |
|----------------|--------|---|---|---|
| Performance    | 30%    | 8 | 9 | 7 |
| Learning curve | 25%    | 6 | 7 | 9 |
| Community      | 20%    | 9 | 8 | 6 |
| Maintenance    | 25%    | 7 | 8 | 8 |
|----------------|--------|---|---|---|
| Weighted Total |        |7.3|8.0|7.5|

Winner: B (but consider team familiarity)
```

---

## Quick Reference

| Model | Best For | Key Question |
|-------|----------|--------------|
| First Principles | Innovation | "What's fundamentally true?" |
| Pareto | Prioritization | "What's the 20% that matters?" |
| Inversion | Risk mitigation | "What guarantees failure?" |
| Second-Order | Impact analysis | "Then what happens?" |
| Pre-Mortem | Planning | "Why did this fail?" |
| Devil's Advocate | Decision validation | "What's the counter-argument?" |
| Systems Thinking | Complex problems | "How do parts interact?" |
| Opportunity Cost | Trade-offs | "What are we giving up?" |
| Constraint Analysis | Unblocking | "What's really fixed?" |
| Root Cause | Debugging | "Why? Why? Why?" |
| Comparative | Selection | "How do options compare?" |

## Usage in Research Phase

During the Research phase, apply 2-3 relevant models:

```markdown
## Analysis

### First Principles
[What are the fundamentals?]

### Inversion
[What would guarantee failure?]

### Second-Order Effects
[What happens after the obvious?]
```

This ensures thorough analysis before planning.
