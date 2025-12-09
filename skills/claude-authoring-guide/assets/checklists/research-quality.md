# Research Quality Checklist

Use this checklist to validate research before planning or implementation.
Based on taches-cc-resources quality control patterns.

## Verification Checklist

### Sources Validated
- [ ] Primary sources consulted (not just summaries)
- [ ] Documentation version matches codebase version
- [ ] Multiple sources cross-referenced
- [ ] Recency verified (information not outdated)

### Claims Audited
| Claim | Source | Verified? | Evidence |
|-------|--------|-----------|----------|
| {{CLAIM_1}} | {{SOURCE_1}} | [ ] | {{EVIDENCE_1}} |
| {{CLAIM_2}} | {{SOURCE_2}} | [ ] | {{EVIDENCE_2}} |
| {{CLAIM_3}} | {{SOURCE_3}} | [ ] | {{EVIDENCE_3}} |

- [ ] All critical claims have supporting evidence
- [ ] No claims based on assumptions alone
- [ ] Contradictory information resolved

## Blind Spots Review

### What Might We Be Missing?

| Area | Question | Investigated? |
|------|----------|---------------|
| Edge Cases | What happens at boundaries? | [ ] |
| Scale | Does this work at production load? | [ ] |
| Security | Are there security implications? | [ ] |
| Performance | Are there performance concerns? | [ ] |
| Dependencies | What depends on this? What does this depend on? | [ ] |
| Failure Modes | What can go wrong? | [ ] |

### Assumptions Made

| Assumption | Why We Made It | Risk if Wrong |
|------------|----------------|---------------|
| {{ASSUMPTION_1}} | {{REASON_1}} | {{RISK_1}} |
| {{ASSUMPTION_2}} | {{REASON_2}} | {{RISK_2}} |

- [ ] All assumptions documented
- [ ] High-risk assumptions validated
- [ ] Alternative interpretations considered

## Critical Claims Audit

For each major claim in the research:

1. **Is the claim specific enough?**
   - [ ] Yes, it's concrete and testable
   - [ ] No → Make it more specific

2. **What's the source?**
   - [ ] Official documentation
   - [ ] Verified code inspection
   - [ ] Community consensus
   - [ ] Single blog post (higher risk)
   - [ ] AI-generated (verify independently)

3. **Is it current?**
   - [ ] Verified within last 6 months
   - [ ] Version-specific and matches our version
   - [ ] No deprecation warnings

4. **Counter-evidence?**
   - [ ] Actively searched for contradicting info
   - [ ] None found / Resolved contradictions

## Research Completeness

### Required Information
- [ ] Problem fully understood
- [ ] Existing solutions explored
- [ ] Technical constraints identified
- [ ] Success criteria defined
- [ ] Failure scenarios mapped

### Hierarchy of Leverage Applied

| Level | Question | Verified? |
|-------|----------|-----------|
| Specification | Is the problem correctly defined? | [ ] |
| Research | Do we understand the system? | [ ] |
| Plan | Is the approach sound? | [ ] |
| Implementation | Ready to code? | [ ] |

- [ ] Higher-leverage items verified before lower
- [ ] Errors at spec level caught early

## Quality Gates

Before proceeding to planning:

- [ ] All critical claims verified with evidence
- [ ] Blind spots reviewed and documented
- [ ] Assumptions explicitly stated with risk assessment
- [ ] No outstanding questions that could derail implementation
- [ ] Research summary written (compression of truth)

## Red Flags

Stop and re-research if:
- [ ] Key information comes from single unverified source
- [ ] Documentation contradicts observed behavior
- [ ] Critical assumption has no supporting evidence
- [ ] Edge cases weren't considered
- [ ] "I think" or "probably" appears in critical decisions
