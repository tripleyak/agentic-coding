#!/usr/bin/env python3
"""
MAKER Framework - Validation Utilities

Detects red flags and validates step outputs for the MAKER framework.
Implements automated quality checks based on paper findings.
"""

import argparse
import re
import sys
from typing import List, Dict, Tuple, Optional


# Expected response lengths by step type (in characters)
EXPECTED_LENGTHS = {
    "code": 500,
    "config": 200,
    "analysis": 800,
    "documentation": 600,
    "command": 100,
    "decision": 300,
    "default": 400
}

# Uncertainty signal patterns
UNCERTAINTY_PATTERNS = [
    r"\bmight\b",
    r"\bpossibly\b",
    r"\bperhaps\b",
    r"\bmaybe\b",
    r"\bprobably\b",
    r"\bI think\b",
    r"\bI believe\b",
    r"\bnot sure\b",
    r"\bnot certain\b",
    r"\bcould be\b",
    r"\bseems like\b",
    r"\bappears to\b",
    r"\bassuming\b",
    r"\bif I understand\b",
    r"\bI'm guessing\b",
    r"\bhard to say\b",
]

# Scope creep indicators
SCOPE_CREEP_PATTERNS = [
    r"\bwhile we're at it\b",
    r"\bwe should also\b",
    r"\blet's also\b",
    r"\badditionally\b.*\bwe could\b",
    r"\bfuture improvement\b",
    r"\bnice to have\b",
    r"\bout of scope but\b",
    r"\bbonus\b.*\bwe can\b",
]


def check_response_length(
    response: str,
    expected_type: str = "default",
    threshold_multiplier: float = 3.0
) -> Tuple[bool, str]:
    """
    Check if response length is within expected bounds.

    Args:
        response: The response text to check
        expected_type: Type of step (code, config, analysis, etc.)
        threshold_multiplier: How many times expected length triggers flag

    Returns:
        Tuple of (is_flagged, message)
    """
    expected = EXPECTED_LENGTHS.get(expected_type, EXPECTED_LENGTHS["default"])
    actual = len(response)
    threshold = expected * threshold_multiplier

    if actual > threshold:
        ratio = actual / expected
        return True, f"Response too long: {actual} chars ({ratio:.1f}x expected for {expected_type})"

    return False, f"Length OK: {actual} chars (expected ~{expected} for {expected_type})"


def check_uncertainty_signals(text: str) -> Tuple[bool, List[str]]:
    """
    Detect hedging and uncertainty language.

    Args:
        text: Text to analyze

    Returns:
        Tuple of (has_signals, list of matched signals)
    """
    matches = []
    text_lower = text.lower()

    for pattern in UNCERTAINTY_PATTERNS:
        if re.search(pattern, text_lower):
            # Find the actual match for context
            match = re.search(pattern, text_lower)
            if match:
                # Get surrounding context
                start = max(0, match.start() - 20)
                end = min(len(text), match.end() + 20)
                context = text[start:end].strip()
                matches.append(f"...{context}...")

    return len(matches) > 0, matches


def check_scope_creep(text: str) -> Tuple[bool, List[str]]:
    """
    Detect scope creep indicators.

    Args:
        text: Text to analyze

    Returns:
        Tuple of (has_scope_creep, list of matched indicators)
    """
    matches = []
    text_lower = text.lower()

    for pattern in SCOPE_CREEP_PATTERNS:
        if re.search(pattern, text_lower):
            match = re.search(pattern, text_lower)
            if match:
                start = max(0, match.start() - 10)
                end = min(len(text), match.end() + 30)
                context = text[start:end].strip()
                matches.append(f"...{context}...")

    return len(matches) > 0, matches


def check_format_compliance(
    output: str,
    expected_format: str
) -> Tuple[bool, str]:
    """
    Validate output matches expected format.

    Args:
        output: The output to validate
        expected_format: Expected format type (json, code, markdown, command, file_path)

    Returns:
        Tuple of (is_compliant, message)
    """
    format_checks = {
        "json": lambda x: x.strip().startswith("{") or x.strip().startswith("["),
        "code": lambda x: any(x.strip().startswith(s) for s in ["def ", "class ", "function", "import ", "from ", "#!", "const ", "let ", "var "]),
        "markdown": lambda x: any(x.strip().startswith(s) for s in ["# ", "## ", "- ", "* ", "1. "]),
        "command": lambda x: not x.strip().startswith("#") and len(x.strip().split("\n")) <= 3,
        "file_path": lambda x: "/" in x or "\\" in x or x.endswith((".py", ".js", ".ts", ".md", ".json", ".yaml", ".yml")),
    }

    if expected_format not in format_checks:
        return True, f"Unknown format '{expected_format}', skipping check"

    is_compliant = format_checks[expected_format](output)
    if is_compliant:
        return True, f"Format OK: matches {expected_format}"
    else:
        return False, f"Format mismatch: expected {expected_format}"


def assess_atomicity(step_description: str) -> Tuple[bool, str]:
    """
    Assess whether a step is sufficiently atomic.

    Args:
        step_description: Description of the step

    Returns:
        Tuple of (is_atomic, feedback)
    """
    # Red flags for non-atomic steps
    non_atomic_indicators = [
        (r"\band\b.*\band\b", "Multiple 'and' conjunctions suggest compound step"),
        (r"\bthen\b", "Sequential actions ('then') suggest multiple steps"),
        (r"\bfirst\b.*\bthen\b", "Explicit sequence suggests decomposition needed"),
        (r"\bif\b.*\belse\b", "Conditional branches may need separate steps"),
        (r"\ball\b", "'All' may indicate batch operation needing breakdown"),
        (r"\bevery\b", "'Every' may indicate iteration needing breakdown"),
        (r"\bmultiple\b", "'Multiple' suggests compound operation"),
    ]

    # Length-based heuristic
    word_count = len(step_description.split())

    issues = []

    if word_count > 20:
        issues.append(f"Description too long ({word_count} words)")

    for pattern, message in non_atomic_indicators:
        if re.search(pattern, step_description.lower()):
            issues.append(message)

    if issues:
        return False, "; ".join(issues)
    else:
        return True, "Step appears atomic"


def generate_verification_questions(
    step_description: str,
    step_type: str = "general"
) -> List[str]:
    """
    Generate verification questions for a step.

    Args:
        step_description: Description of the step
        step_type: Type of step (code, config, analysis, documentation, command)

    Returns:
        List of verification questions
    """
    base_questions = [
        "Does the output match what was requested?",
        "Are there any unexpected side effects?",
        "Is the output complete?",
    ]

    type_specific = {
        "code": [
            "Does the code compile/parse without errors?",
            "Are edge cases handled?",
            "Does it follow the existing code style?",
            "Are there any security concerns?",
        ],
        "config": [
            "Are all required fields present?",
            "Are values in expected formats?",
            "Will this work in all environments?",
            "Are sensitive values protected?",
        ],
        "analysis": [
            "Is the methodology sound?",
            "Are conclusions supported by data?",
            "Are assumptions explicitly stated?",
            "Is the analysis reproducible?",
        ],
        "documentation": [
            "Is the language clear and unambiguous?",
            "Are examples provided where helpful?",
            "Is it accurate to the implementation?",
            "Is the target audience considered?",
        ],
        "command": [
            "Is the command safe to run?",
            "Are all paths/arguments correct?",
            "What happens if it fails?",
            "Is it idempotent?",
        ],
    }

    questions = base_questions.copy()
    questions.extend(type_specific.get(step_type, []))

    return questions


def run_all_checks(
    response: str,
    step_description: str = "",
    step_type: str = "default"
) -> Dict:
    """
    Run all validation checks on a response.

    Args:
        response: The response text to validate
        step_description: Description of the step (for atomicity check)
        step_type: Type of step

    Returns:
        Dictionary with all check results
    """
    results = {
        "flags": [],
        "warnings": [],
        "passed": [],
    }

    # Length check
    is_flagged, msg = check_response_length(response, step_type)
    if is_flagged:
        results["flags"].append(f"LENGTH: {msg}")
    else:
        results["passed"].append(f"LENGTH: {msg}")

    # Uncertainty check
    has_uncertainty, matches = check_uncertainty_signals(response)
    if has_uncertainty:
        results["warnings"].append(f"UNCERTAINTY: Found {len(matches)} signals")
        for match in matches[:3]:  # Show first 3
            results["warnings"].append(f"  - {match}")
    else:
        results["passed"].append("UNCERTAINTY: No hedging language detected")

    # Scope creep check
    has_creep, matches = check_scope_creep(response)
    if has_creep:
        results["warnings"].append(f"SCOPE: Potential scope creep detected")
        for match in matches[:3]:
            results["warnings"].append(f"  - {match}")
    else:
        results["passed"].append("SCOPE: No scope creep indicators")

    # Atomicity check (if step description provided)
    if step_description:
        is_atomic, msg = assess_atomicity(step_description)
        if not is_atomic:
            results["warnings"].append(f"ATOMICITY: {msg}")
        else:
            results["passed"].append(f"ATOMICITY: {msg}")

    # Summary
    results["summary"] = {
        "total_flags": len(results["flags"]),
        "total_warnings": len(results["warnings"]),
        "total_passed": len(results["passed"]),
        "recommendation": _get_recommendation(results)
    }

    return results


def _get_recommendation(results: Dict) -> str:
    """Generate recommendation based on check results."""
    flags = len(results["flags"])
    warnings = len(results["warnings"])

    if flags > 0:
        return "RED FLAG - Review required before proceeding"
    elif warnings > 2:
        return "CAUTION - Multiple concerns detected, verify carefully"
    elif warnings > 0:
        return "MINOR - Some concerns, quick verification recommended"
    else:
        return "OK - No significant issues detected"


def main():
    parser = argparse.ArgumentParser(
        description="MAKER Framework Validation Utilities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s check "Response text to validate"
  %(prog)s check "Response text" --type code
  %(prog)s check "Response text" --step "Create the user model"
  %(prog)s atomicity "Create the model and write tests and update docs"
  %(prog)s questions --type code
  echo "Response text" | %(prog)s check -
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # check command
    check_parser = subparsers.add_parser("check", help="Run all validation checks")
    check_parser.add_argument("response", help="Response text to check (use '-' for stdin)")
    check_parser.add_argument("--type", "-t", default="default",
                              choices=list(EXPECTED_LENGTHS.keys()),
                              help="Step type for context-aware checks")
    check_parser.add_argument("--step", "-s", default="",
                              help="Step description for atomicity check")

    # atomicity command
    atom_parser = subparsers.add_parser("atomicity", help="Check if step is atomic")
    atom_parser.add_argument("description", help="Step description to check")

    # questions command
    q_parser = subparsers.add_parser("questions", help="Generate verification questions")
    q_parser.add_argument("--type", "-t", default="general",
                          choices=["general", "code", "config", "analysis", "documentation", "command"],
                          help="Step type")

    # length command
    len_parser = subparsers.add_parser("length", help="Check response length")
    len_parser.add_argument("response", help="Response text to check")
    len_parser.add_argument("--type", "-t", default="default", help="Step type")

    # uncertainty command
    unc_parser = subparsers.add_parser("uncertainty", help="Check for uncertainty signals")
    unc_parser.add_argument("text", help="Text to check (use '-' for stdin)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "check":
        if args.response == "-":
            response = sys.stdin.read()
        else:
            response = args.response

        results = run_all_checks(response, args.step, args.type)

        print("=" * 50)
        print("MAKER Validation Report")
        print("=" * 50)

        if results["flags"]:
            print("\nRED FLAGS:")
            for flag in results["flags"]:
                print(f"  [!] {flag}")

        if results["warnings"]:
            print("\nWARNINGS:")
            for warning in results["warnings"]:
                print(f"  [?] {warning}")

        if results["passed"]:
            print("\nPASSED:")
            for passed in results["passed"]:
                print(f"  [x] {passed}")

        print("\n" + "-" * 50)
        print(f"Summary: {results['summary']['total_flags']} flags, "
              f"{results['summary']['total_warnings']} warnings, "
              f"{results['summary']['total_passed']} passed")
        print(f"Recommendation: {results['summary']['recommendation']}")

    elif args.command == "atomicity":
        is_atomic, msg = assess_atomicity(args.description)
        status = "ATOMIC" if is_atomic else "NON-ATOMIC"
        print(f"[{status}] {msg}")

    elif args.command == "questions":
        questions = generate_verification_questions("", args.type)
        print(f"Verification questions for {args.type} step:")
        for i, q in enumerate(questions, 1):
            print(f"  {i}. {q}")

    elif args.command == "length":
        is_flagged, msg = check_response_length(args.response, args.type)
        status = "FLAGGED" if is_flagged else "OK"
        print(f"[{status}] {msg}")

    elif args.command == "uncertainty":
        if args.text == "-":
            text = sys.stdin.read()
        else:
            text = args.text

        has_signals, matches = check_uncertainty_signals(text)
        if has_signals:
            print(f"Found {len(matches)} uncertainty signals:")
            for match in matches:
                print(f"  - {match}")
        else:
            print("No uncertainty signals detected")


if __name__ == "__main__":
    main()
