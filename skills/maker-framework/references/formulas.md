# Mathematical Foundations

Formulas and calculations underlying the MAKER framework.

## Contents

1. [Core Formulas](#core-formulas)
2. [Practical Interpretation](#practical-interpretation)
3. [Quick Reference Tables](#quick-reference-tables)
4. [Example Calculations](#example-calculations)

---

## Core Formulas

### Success Probability Without Verification

For a task with `s` steps, each with success probability `p`:

```
P(all steps succeed) = p^s
```

**Example:** 100 steps at 95% each = 0.95^100 = 0.6%

This is why multi-step tasks fail.

### Minimum Verification Threshold (k_min)

To achieve target success rate `t` with `s` steps, per-step success `p`, and milestone size `m`:

```
k_min = ⌈ ln(t^(-m/s) - 1) / ln((1-p)/p) ⌉
```

Where:
- `k_min` = minimum number of consecutive verifications needed
- `t` = target success probability (e.g., 0.99)
- `s` = total number of steps
- `m` = milestone size (steps per verification group)
- `p` = per-step success probability
- `⌈ ⌉` = ceiling function (round up)

### Full Success Probability with Verification

Given verification threshold `k`:

```
P_full = (1 + ((1-p)/p)^k)^(-s/m)
```

As `k` increases, `P_full` approaches 1.

### Expected Cost

```
E[cost] = O(s × ln s)
```

More precisely:
```
E[cost] ≈ s × (1 + k × (1-p))
```

The log factor comes from the k_min scaling: `k_min = O(ln s)`.

---

## Practical Interpretation

### What k Means in User-Guided Verification

In the original MAKER paper, `k` represents voting margin (ahead-by-k). In user-guided verification:

- **k=1**: Single verification pass (user marks VERIFIED once)
- **k=2**: Double-check (verify, then re-verify)
- **k=3**: Triple confirmation (for critical steps)

Higher k = more conservative = higher reliability = more effort.

### Milestone Size (m)

- **m=1**: Verify every single step (most granular)
- **m=5**: Verify every 5 steps as a batch
- **m=10**: Checkpoint verification after larger chunks

Smaller m = more overhead but catches errors earlier.

### Trade-offs

| Parameter | Increase Effect | Decrease Effect |
|-----------|-----------------|-----------------|
| k | ↑ reliability, ↑ cost | ↓ reliability, ↓ cost |
| m | ↓ overhead, ↓ granularity | ↑ overhead, ↑ granularity |
| p (step success) | ↓ k needed | ↑ k needed |

---

## Quick Reference Tables

### k_min for 99% Target Success (p=0.9)

| Steps (s) | k_min |
|-----------|-------|
| 10 | 2 |
| 25 | 2 |
| 50 | 3 |
| 100 | 3 |
| 200 | 3 |
| 500 | 4 |
| 1,000 | 4 |
| 10,000 | 5 |
| 100,000 | 6 |
| 1,000,000 | 6 |

### Success Probability by k (100 steps, p=0.9)

| k | P_full |
|---|--------|
| 1 | 37.0% |
| 2 | 84.6% |
| 3 | 97.6% |
| 4 | 99.7% |
| 5 | 99.97% |

### k_min by Per-Step Success (100 steps, 99% target)

| p | k_min |
|---|-------|
| 0.99 | 1 |
| 0.95 | 2 |
| 0.90 | 3 |
| 0.85 | 3 |
| 0.80 | 4 |
| 0.75 | 4 |
| 0.70 | 5 |

### Cost Comparison

For 100 steps at p=0.9:

| Approach | Expected Attempts | Success Rate |
|----------|------------------|--------------|
| No verification | 100 | 0.003% |
| k=1 | ~111 | 37.0% |
| k=2 | ~122 | 84.6% |
| k=3 | ~133 | 97.6% |
| k=4 | ~144 | 99.7% |

---

## Example Calculations

### Example 1: Medium Project

**Given:**
- Task: Implement API (50 steps estimated)
- Target: 99% success
- Expected per-step success: 90%
- Milestone size: 1 (verify each step)

**Calculate k_min:**
```
k_min = ⌈ ln(0.99^(-1/50) - 1) / ln(0.1/0.9) ⌉
      = ⌈ ln(0.99^(-0.02) - 1) / ln(0.111) ⌉
      = ⌈ ln(1.0002 - 1) / (-2.197) ⌉
      = ⌈ ln(0.0002) / (-2.197) ⌉
      = ⌈ -8.52 / (-2.197) ⌉
      = ⌈ 3.88 ⌉
      = 4
```

Wait, let me recalculate more carefully:
```
t^(-m/s) = 0.99^(-1/50) = 0.99^(-0.02) ≈ 1.0002
t^(-m/s) - 1 ≈ 0.0002
(1-p)/p = 0.1/0.9 ≈ 0.111
ln(0.0002) ≈ -8.52
ln(0.111) ≈ -2.197
k_min = ⌈ -8.52 / -2.197 ⌉ = ⌈ 3.88 ⌉ = 4
```

**Result:** Use k=4 verification for 99% success.

### Example 2: Simple Bug Fix

**Given:**
- Task: Fix bug (10 steps)
- Target: 95% success
- Per-step success: 85%

**Calculate:**
```
k_min = ⌈ ln(0.95^(-0.1) - 1) / ln(0.15/0.85) ⌉
      = ⌈ ln(1.0051 - 1) / ln(0.176) ⌉
      = ⌈ ln(0.0051) / (-1.737) ⌉
      = ⌈ -5.28 / -1.737 ⌉
      = ⌈ 3.04 ⌉
      = 4
```

**Result:** k=4, even for small task with lower target, because lower per-step success.

### Example 3: Verify Current Progress

**Given:**
- Project: 100 steps total
- Completed: 40 verified, 5 failed
- Remaining: 55 steps

**Calculate observed success rate:**
```
p_observed = 40 / (40 + 5) = 0.889 ≈ 89%
```

**Calculate remaining success probability (k=1):**
```
P_remaining = (1 + ((1-0.889)/0.889)^1)^(-55/1)
            = (1 + 0.125)^(-55)
            = 1.125^(-55)
            = 0.0012 ≈ 0.12%
```

**With k=3:**
```
P_remaining = (1 + 0.125^3)^(-55)
            = (1 + 0.00195)^(-55)
            = 0.898 ≈ 89.8%
```

**Result:** With observed 89% step success, need k=3 for reasonable completion probability.

---

## Using the Calculator Script

```bash
# Calculate k_min
python success_calculator.py kmin 100 --target 0.99 --step-success 0.9

# Calculate success probability
python success_calculator.py probability 100 --k 3 --step-success 0.9

# Get recommendations
python success_calculator.py recommend high --target 0.99

# Show reference table
python success_calculator.py table --step-success 0.9

# Analyze existing project
python success_calculator.py analyze my-project.maker.json
```
