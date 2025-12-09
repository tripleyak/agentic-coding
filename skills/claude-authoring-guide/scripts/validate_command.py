#!/usr/bin/env python3
"""
Command Format Validator

Validates that a slash command follows the claude-authoring-guide best practices.
Uses standard library only.

Usage:
    python validate_command.py path/to/command.md
    python validate_command.py ~/.claude/commands/
"""

import sys
import os
import re
from pathlib import Path
from typing import List


class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.passed: List[str] = []

    def error(self, msg: str):
        self.errors.append(f"❌ {msg}")

    def warning(self, msg: str):
        self.warnings.append(f"⚠️  {msg}")

    def passed_check(self, msg: str):
        self.passed.append(f"✅ {msg}")

    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def print_report(self, filename: str = ""):
        header = f" {filename} " if filename else ""
        print(f"\n{'=' * 20}{header}{'=' * 20}")

        if self.passed:
            for item in self.passed:
                print(f"  {item}")

        if self.warnings:
            for item in self.warnings:
                print(f"  {item}")

        if self.errors:
            for item in self.errors:
                print(f"  {item}")

        status = "✅ PASS" if self.is_valid() else "❌ FAIL"
        print(f"  {status}")


def check_filename(filepath: Path, result: ValidationResult):
    """Check filename conventions."""
    name = filepath.stem

    # Check for kebab-case
    if re.match(r"^[a-z][a-z0-9-]*[a-z0-9]$|^[a-z]$", name):
        result.passed_check("Filename is kebab-case")
    else:
        result.warning(f"Filename '{name}' should be kebab-case")

    # Check extension
    if filepath.suffix == ".md":
        result.passed_check("Has .md extension")
    else:
        result.error(f"Wrong extension: {filepath.suffix} (should be .md)")


def check_title(content: str, result: ValidationResult):
    """Check for proper title."""
    if re.match(r"^#\s+.+", content):
        result.passed_check("Has main title")
    else:
        result.error("Missing main title (# Title)")


def check_description(content: str, result: ValidationResult):
    """Check for description section or intro paragraph."""
    # Check for description after title
    title_match = re.match(r"^#\s+.+\n\n(.+)", content)
    if title_match:
        desc = title_match.group(1)
        if len(desc) > 20 and not desc.startswith("#"):
            result.passed_check("Has description paragraph")
            return

    # Check for explicit description section
    if re.search(r"##\s*Description", content, re.IGNORECASE):
        result.passed_check("Has description section")
        return

    result.warning("Consider adding a description")


def check_usage_section(content: str, result: ValidationResult):
    """Check for usage/invocation information."""
    patterns = [
        r"##\s*Usage",
        r"##\s*How to Use",
        r"##\s*Invocation",
        r"##\s*Examples?",
    ]

    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            result.passed_check("Has usage section")
            return

    result.warning("Consider adding ## Usage section")


def check_arguments(content: str, result: ValidationResult):
    """Check if command documents its arguments (if any)."""
    # Look for argument references
    has_args = re.search(r"\$[A-Z_]+|\{\{[^}]+\}\}|\$\d+", content)

    if has_args:
        # Check if arguments are documented
        if re.search(r"##\s*(Arguments?|Parameters?|Options?)", content, re.IGNORECASE):
            result.passed_check("Arguments are documented")
        elif re.search(r"\|.*\|.*\|", content):  # Table format
            result.passed_check("Arguments documented in table")
        else:
            result.warning("Arguments used but not documented")


def check_examples(content: str, result: ValidationResult):
    """Check for usage examples."""
    # Look for code blocks with command invocation
    example_patterns = [
        r"```.*\n.*?/\w+",  # Code block with slash command
        r"##\s*Examples?",
        r"Example:",
    ]

    for pattern in example_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            result.passed_check("Has examples")
            return

    result.warning("Consider adding examples")


def check_line_count(content: str, result: ValidationResult):
    """Check command isn't too long."""
    lines = content.count("\n") + 1

    if lines <= 100:
        result.passed_check(f"Concise ({lines} lines)")
    elif lines <= 200:
        result.warning(f"Command is lengthy ({lines} lines)")
    else:
        result.error(f"Command too long ({lines} lines) - consider splitting")


def check_prompt_quality(content: str, result: ValidationResult):
    """Check for clear instructions to Claude."""
    # Commands should have clear action directives
    action_words = [
        "analyze",
        "create",
        "generate",
        "review",
        "check",
        "list",
        "find",
        "run",
        "execute",
        "build",
        "update",
        "fix",
        "explain",
        "summarize",
    ]

    content_lower = content.lower()
    found_actions = [w for w in action_words if w in content_lower]

    if len(found_actions) >= 1:
        result.passed_check("Has clear action directives")
    else:
        result.warning("Consider adding clear action verbs")


def validate_command(filepath: Path) -> ValidationResult:
    """Validate a single command file."""
    result = ValidationResult()

    if not filepath.exists():
        result.error(f"File not found: {filepath}")
        return result

    content = filepath.read_text()

    # Run all checks
    check_filename(filepath, result)
    check_title(content, result)
    check_description(content, result)
    check_usage_section(content, result)
    check_arguments(content, result)
    check_examples(content, result)
    check_line_count(content, result)
    check_prompt_quality(content, result)

    return result


def validate_directory(dirpath: Path) -> dict:
    """Validate all commands in a directory."""
    results = {}

    for file in sorted(dirpath.glob("*.md")):
        results[file.name] = validate_command(file)

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_command.py <path/to/command.md or commands-dir>")
        print("\nExamples:")
        print("  python validate_command.py ~/.claude/commands/")
        print("  python validate_command.py ./my-command.md")
        sys.exit(1)

    path = Path(sys.argv[1]).expanduser()

    if path.is_dir():
        results = validate_directory(path)

        print("\n" + "=" * 60)
        print("COMMAND VALIDATION REPORT")
        print("=" * 60)

        total_errors = 0
        for filename, result in results.items():
            result.print_report(filename)
            total_errors += len(result.errors)

        print("\n" + "-" * 60)
        if total_errors == 0:
            print(f"✅ ALL {len(results)} COMMANDS PASSED")
        else:
            print(f"❌ {total_errors} ERRORS FOUND")
        print("-" * 60 + "\n")

        sys.exit(0 if total_errors == 0 else 1)

    else:
        result = validate_command(path)
        result.print_report(path.name)
        sys.exit(0 if result.is_valid() else 1)


if __name__ == "__main__":
    main()
