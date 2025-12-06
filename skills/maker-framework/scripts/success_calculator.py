#!/usr/bin/env python3
"""
MAKER Framework - Success Calculator

Calculates success probabilities and verification thresholds based on
formulas from the MAKER paper (Solving a Million-Step LLM Task with Zero Errors).

Key formulas:
- k_min = ⌈ln(t^(-m/s) - 1) / ln((1-p)/p)⌉
- p_full = (1 + ((1-p)/p)^k)^(-s/m)
- E[cost] = O(s × ln s)
"""

import argparse
import math
import json
import os
import sys
from typing import Tuple, Optional


def calculate_k_min(
    total_steps: int,
    target_success: float = 0.99,
    per_step_success: float = 0.9,
    milestone_size: int = 1
) -> int:
    """
    Calculate minimum verification threshold (k) needed for target success rate.

    In user-guided verification, k represents the "confidence margin" needed
    before proceeding. Higher k = more conservative verification.

    Args:
        total_steps: Total number of steps in the task (s)
        target_success: Target probability of full task success (t)
        per_step_success: Probability of success per step (p)
        milestone_size: Number of steps per milestone (m)

    Returns:
        Minimum k value needed

    Formula: k_min = ⌈ln(t^(-m/s) - 1) / ln((1-p)/p)⌉
    """
    if per_step_success <= 0 or per_step_success >= 1:
        raise ValueError("per_step_success must be between 0 and 1 (exclusive)")
    if target_success <= 0 or target_success >= 1:
        raise ValueError("target_success must be between 0 and 1 (exclusive)")
    if total_steps <= 0:
        raise ValueError("total_steps must be positive")
    if milestone_size <= 0:
        raise ValueError("milestone_size must be positive")

    # Calculate the ratio (1-p)/p
    ratio = (1 - per_step_success) / per_step_success

    # Calculate t^(-m/s) - 1
    exponent = -milestone_size / total_steps
    target_term = math.pow(target_success, exponent) - 1

    if target_term <= 0:
        # Target is already achievable with k=1
        return 1

    if ratio <= 0:
        # Perfect per-step success, k=1 suffices
        return 1

    # Calculate k_min
    k_min = math.log(target_term) / math.log(ratio)

    return max(1, math.ceil(k_min))


def calculate_full_success_probability(
    total_steps: int,
    per_step_success: float = 0.9,
    k: int = 1,
    milestone_size: int = 1
) -> float:
    """
    Calculate probability of full task success given parameters.

    Args:
        total_steps: Total number of steps (s)
        per_step_success: Probability of success per step (p)
        k: Verification threshold (ahead-by-k)
        milestone_size: Number of steps per milestone (m)

    Returns:
        Probability of completing all steps successfully

    Formula: p_full = (1 + ((1-p)/p)^k)^(-s/m)
    """
    if per_step_success <= 0 or per_step_success >= 1:
        raise ValueError("per_step_success must be between 0 and 1 (exclusive)")
    if k < 1:
        raise ValueError("k must be at least 1")

    ratio = (1 - per_step_success) / per_step_success
    base = 1 + math.pow(ratio, k)
    exponent = -total_steps / milestone_size

    return math.pow(base, exponent)


def estimate_expected_cost(
    total_steps: int,
    per_step_success: float = 0.9,
    k: int = 1
) -> Tuple[float, str]:
    """
    Estimate expected cost (number of step attempts) to complete task.

    Args:
        total_steps: Total number of steps (s)
        per_step_success: Probability of success per step (p)
        k: Verification threshold

    Returns:
        Tuple of (expected_attempts, complexity_class)

    The MAKER framework achieves O(s ln s) cost complexity.
    """
    # Expected attempts per step with verification
    # Each step may need multiple attempts; with ahead-by-k, we need margin
    attempts_per_step = 1 / per_step_success

    # k-factor adds logarithmic overhead
    k_overhead = 1 + math.log(max(1, k))

    expected_total = total_steps * attempts_per_step * k_overhead

    # Determine complexity class
    if total_steps <= 1:
        complexity = "O(1)"
    else:
        log_factor = math.log(total_steps)
        if expected_total <= total_steps * 1.5:
            complexity = "O(s)"
        elif expected_total <= total_steps * log_factor * 1.5:
            complexity = "O(s ln s)"
        else:
            complexity = "O(s ln s) or higher"

    return expected_total, complexity


def recommend_decomposition_level(
    estimated_complexity: str,
    reliability_target: float = 0.99,
    base_step_success: float = 0.9
) -> dict:
    """
    Recommend decomposition parameters based on task complexity.

    Args:
        estimated_complexity: Description of task complexity (low/medium/high/extreme)
        reliability_target: Target success probability
        base_step_success: Expected success rate per atomic step

    Returns:
        Dictionary with recommendations
    """
    complexity_map = {
        "low": (10, 1),      # ~10 steps, milestone size 1
        "medium": (50, 5),   # ~50 steps, milestone size 5
        "high": (200, 10),   # ~200 steps, milestone size 10
        "extreme": (1000, 20) # ~1000 steps, milestone size 20
    }

    complexity = estimated_complexity.lower()
    if complexity not in complexity_map:
        complexity = "medium"

    total_steps, milestone_size = complexity_map[complexity]

    k_min = calculate_k_min(total_steps, reliability_target, base_step_success, milestone_size)
    success_prob = calculate_full_success_probability(total_steps, base_step_success, k_min, milestone_size)
    expected_cost, cost_class = estimate_expected_cost(total_steps, base_step_success, k_min)

    return {
        "complexity": complexity,
        "estimated_steps": total_steps,
        "milestone_size": milestone_size,
        "recommended_k": k_min,
        "expected_success_rate": f"{success_prob * 100:.2f}%",
        "expected_cost": f"{expected_cost:.0f} step attempts",
        "cost_complexity": cost_class,
        "guidance": _get_guidance(complexity, k_min)
    }


def _get_guidance(complexity: str, k: int) -> str:
    """Generate guidance text based on complexity and k."""
    if complexity == "low":
        return f"Simple task. Verify each step once (k={k}). Brief check sufficient."
    elif complexity == "medium":
        return f"Moderate task. Use structured verification (k={k}). Document key decisions."
    elif complexity == "high":
        return f"Complex task. Rigorous verification needed (k={k}). Consider checkpoints."
    else:
        return f"Extreme task. Maximum decomposition required (k={k}). Milestone-based verification essential."


def analyze_project(project_path: str) -> dict:
    """
    Analyze a MAKER project file and calculate success metrics.

    Args:
        project_path: Path to project JSON file

    Returns:
        Analysis results
    """
    if not os.path.exists(project_path):
        raise FileNotFoundError(f"Project file not found: {project_path}")

    with open(project_path, 'r') as f:
        project = json.load(f)

    stats = project["statistics"]
    total = stats["total"]
    verified = stats["verified"]
    failed = stats["failed"]
    flagged = stats["flagged"]

    # Calculate observed success rate
    completed = verified + failed
    observed_success = verified / completed if completed > 0 else 0.9

    # Estimate remaining success probability
    remaining = total - verified
    if remaining > 0 and observed_success > 0:
        remaining_success = calculate_full_success_probability(
            remaining, observed_success, k=1
        )
    else:
        remaining_success = 1.0

    # Overall projected success
    if verified == total:
        overall_success = 1.0
    else:
        overall_success = remaining_success * (1 - flagged / total if total > 0 else 1)

    return {
        "project_name": project["name"],
        "total_steps": total,
        "completed": verified,
        "failed": failed,
        "flagged": flagged,
        "remaining": remaining,
        "observed_success_rate": f"{observed_success * 100:.1f}%",
        "projected_remaining_success": f"{remaining_success * 100:.1f}%",
        "overall_projected_success": f"{overall_success * 100:.1f}%",
        "recommendation": _get_project_recommendation(stats, observed_success)
    }


def _get_project_recommendation(stats: dict, observed_success: float) -> str:
    """Generate recommendation based on project state."""
    if observed_success < 0.7:
        return "High failure rate. Consider decomposing steps further or reviewing approach."
    elif stats["flagged"] > stats["verified"] * 0.2:
        return "Many flagged steps. Address red flags before proceeding."
    elif observed_success >= 0.95:
        return "Excellent progress. Continue current approach."
    else:
        return "Good progress. Monitor for patterns in failures."


def main():
    parser = argparse.ArgumentParser(
        description="MAKER Framework Success Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s kmin 100 --target 0.99 --step-success 0.9
  %(prog)s probability 100 --k 3 --step-success 0.9
  %(prog)s cost 100 --step-success 0.9 --k 3
  %(prog)s recommend high --target 0.99
  %(prog)s analyze my-project.maker.json
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # kmin command
    kmin_parser = subparsers.add_parser("kmin", help="Calculate minimum k value")
    kmin_parser.add_argument("total_steps", type=int, help="Total number of steps")
    kmin_parser.add_argument("--target", "-t", type=float, default=0.99,
                             help="Target success probability (default: 0.99)")
    kmin_parser.add_argument("--step-success", "-p", type=float, default=0.9,
                             help="Per-step success probability (default: 0.9)")
    kmin_parser.add_argument("--milestone", "-m", type=int, default=1,
                             help="Milestone size (default: 1)")

    # probability command
    prob_parser = subparsers.add_parser("probability", help="Calculate success probability")
    prob_parser.add_argument("total_steps", type=int, help="Total number of steps")
    prob_parser.add_argument("--k", type=int, default=1, help="Verification threshold (default: 1)")
    prob_parser.add_argument("--step-success", "-p", type=float, default=0.9,
                             help="Per-step success probability (default: 0.9)")
    prob_parser.add_argument("--milestone", "-m", type=int, default=1,
                             help="Milestone size (default: 1)")

    # cost command
    cost_parser = subparsers.add_parser("cost", help="Estimate expected cost")
    cost_parser.add_argument("total_steps", type=int, help="Total number of steps")
    cost_parser.add_argument("--k", type=int, default=1, help="Verification threshold (default: 1)")
    cost_parser.add_argument("--step-success", "-p", type=float, default=0.9,
                             help="Per-step success probability (default: 0.9)")

    # recommend command
    recommend_parser = subparsers.add_parser("recommend", help="Get decomposition recommendations")
    recommend_parser.add_argument("complexity", choices=["low", "medium", "high", "extreme"],
                                  help="Task complexity level")
    recommend_parser.add_argument("--target", "-t", type=float, default=0.99,
                                  help="Target success probability (default: 0.99)")
    recommend_parser.add_argument("--step-success", "-p", type=float, default=0.9,
                                  help="Per-step success probability (default: 0.9)")

    # analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a project file")
    analyze_parser.add_argument("project", help="Project file path")

    # table command (quick reference)
    table_parser = subparsers.add_parser("table", help="Show reference table")
    table_parser.add_argument("--step-success", "-p", type=float, default=0.9,
                              help="Per-step success probability (default: 0.9)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "kmin":
        k = calculate_k_min(args.total_steps, args.target, args.step_success, args.milestone)
        print(f"Minimum k for {args.total_steps} steps with {args.target*100}% target: {k}")

    elif args.command == "probability":
        prob = calculate_full_success_probability(
            args.total_steps, args.step_success, args.k, args.milestone
        )
        print(f"Success probability for {args.total_steps} steps with k={args.k}: {prob*100:.2f}%")

    elif args.command == "cost":
        cost, complexity = estimate_expected_cost(args.total_steps, args.step_success, args.k)
        print(f"Expected cost: {cost:.0f} step attempts")
        print(f"Complexity: {complexity}")

    elif args.command == "recommend":
        rec = recommend_decomposition_level(args.complexity, args.target, args.step_success)
        print(f"Recommendations for {args.complexity} complexity task:")
        print(f"  Estimated steps: {rec['estimated_steps']}")
        print(f"  Milestone size: {rec['milestone_size']}")
        print(f"  Recommended k: {rec['recommended_k']}")
        print(f"  Expected success: {rec['expected_success_rate']}")
        print(f"  Expected cost: {rec['expected_cost']}")
        print(f"  Complexity: {rec['cost_complexity']}")
        print(f"  Guidance: {rec['guidance']}")

    elif args.command == "analyze":
        try:
            analysis = analyze_project(args.project)
            print(f"Project: {analysis['project_name']}")
            print(f"  Total steps: {analysis['total_steps']}")
            print(f"  Completed: {analysis['completed']}")
            print(f"  Failed: {analysis['failed']}")
            print(f"  Flagged: {analysis['flagged']}")
            print(f"  Remaining: {analysis['remaining']}")
            print(f"  Observed success: {analysis['observed_success_rate']}")
            print(f"  Projected remaining: {analysis['projected_remaining_success']}")
            print(f"  Overall projected: {analysis['overall_projected_success']}")
            print(f"  Recommendation: {analysis['recommendation']}")
        except FileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "table":
        p = args.step_success
        print(f"Quick Reference (p={p}):")
        print(f"{'Steps':>8} | {'k=1':>8} | {'k=2':>8} | {'k=3':>8} | {'k_min (99%)':>12}")
        print("-" * 50)
        for s in [10, 25, 50, 100, 200, 500, 1000]:
            p1 = calculate_full_success_probability(s, p, 1) * 100
            p2 = calculate_full_success_probability(s, p, 2) * 100
            p3 = calculate_full_success_probability(s, p, 3) * 100
            k_min = calculate_k_min(s, 0.99, p)
            print(f"{s:>8} | {p1:>7.1f}% | {p2:>7.1f}% | {p3:>7.1f}% | {k_min:>12}")


if __name__ == "__main__":
    main()
