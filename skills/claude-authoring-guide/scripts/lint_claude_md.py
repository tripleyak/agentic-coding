#!/usr/bin/env python3
"""
CLAUDE.md Quality Checker

Lints CLAUDE.md files for best practices based on the claude-authoring-guide.
Uses standard library only.

Usage:
    python lint_claude_md.py                           # Check ~/.claude/CLAUDE.md
    python lint_claude_md.py path/to/CLAUDE.md         # Check specific file
    python lint_claude_md.py --global --project ./     # Check both global and project
"""

import sys
import os
import re
from pathlib import Path
from typing import List, Optional


class LintResult:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        self.passed: List[str] = []

    def error(self, msg: str):
        self.errors.append(f"❌ {msg}")

    def warning(self, msg: str):
        self.warnings.append(f"⚠️  {msg}")

    def info_msg(self, msg: str):
        self.info.append(f"ℹ️  {msg}")

    def passed_check(self, msg: str):
        self.passed.append(f"✅ {msg}")

    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def print_report(self):
        print(f"\n{'=' * 60}")
        print(f"CLAUDE.md LINT REPORT: {self.filepath}")
        print("=" * 60)

        if self.passed:
            print("\nPassed:")
            for item in self.passed:
                print(f"  {item}")

        if self.info:
            print("\nInfo:")
            for item in self.info:
                print(f"  {item}")

        if self.warnings:
            print("\nWarnings:")
            for item in self.warnings:
                print(f"  {item}")

        if self.errors:
            print("\nErrors:")
            for item in self.errors:
                print(f"  {item}")

        print("\n" + "-" * 60)
        if self.is_valid():
            print("✅ LINT PASSED")
        else:
            print(f"❌ LINT FAILED ({len(self.errors)} errors)")
        print("-" * 60)


def check_line_count(content: str, result: LintResult, is_global: bool):
    """Check that CLAUDE.md isn't too long."""
    lines = content.count("\n") + 1

    # Global CLAUDE.md should be concise
    if is_global:
        if lines <= 70:
            result.passed_check(f"Concise ({lines} lines)")
        elif lines <= 100:
            result.warning(f"Getting long ({lines} lines) - consider moving to skills")
        else:
            result.error(f"Too long ({lines} lines) - move procedures to skills")
    else:
        # Project CLAUDE.md can be longer
        if lines <= 150:
            result.passed_check(f"Reasonable length ({lines} lines)")
        elif lines <= 250:
            result.warning(f"Consider splitting ({lines} lines)")
        else:
            result.warning(f"Very long ({lines} lines) - consider skill extraction")


def check_structure(content: str, result: LintResult):
    """Check for proper heading structure."""
    # Should have main title
    if re.match(r"^#\s+", content):
        result.passed_check("Has main title")
    else:
        result.error("Missing main title (# Title)")

    # Check for sections
    sections = re.findall(r"^##\s+(.+)$", content, re.MULTILINE)
    if len(sections) >= 2:
        result.passed_check(f"Has {len(sections)} sections")
        result.info_msg(f"Sections: {', '.join(sections[:5])}" + ("..." if len(sections) > 5 else ""))
    else:
        result.warning("Consider adding more sections (##)")


def check_principles_vs_procedures(content: str, result: LintResult):
    """Check balance of principles vs procedures."""
    # Procedures are typically in code blocks or numbered lists
    code_blocks = len(re.findall(r"```", content)) // 2
    numbered_steps = len(re.findall(r"^\d+\.\s+", content, re.MULTILINE))

    # Principles are typically bullets or short statements
    bullets = len(re.findall(r"^[-*]\s+", content, re.MULTILINE))

    # CLAUDE.md should favor principles
    procedure_indicators = code_blocks + numbered_steps
    principle_indicators = bullets

    if procedure_indicators > principle_indicators and procedure_indicators > 5:
        result.warning("Heavy on procedures - consider moving to skills")
        result.info_msg(f"Found {procedure_indicators} procedure indicators, {principle_indicators} principle indicators")
    else:
        result.passed_check("Good balance of principles vs procedures")


def check_error_sensitivity(content: str, result: LintResult):
    """Remind about CLAUDE.md error impact."""
    # Always add this reminder
    result.info_msg("Remember: CLAUDE.md errors have 100,000x impact")


def check_skill_references(content: str, result: LintResult):
    """Check for skill references and progressive disclosure."""
    skill_patterns = [
        r"skill",
        r"trigger",
        r"--scan",
        r"progressive",
    ]

    found = False
    for pattern in skill_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            found = True
            break

    if found:
        result.passed_check("References skills/progressive disclosure")
    else:
        result.warning("Consider adding skill references for complex procedures")


def check_verification_section(content: str, result: LintResult):
    """Check for verification/quality section."""
    patterns = [
        r"verification",
        r"quality",
        r"test",
        r"lint",
        r"check",
    ]

    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            result.passed_check("Has quality/verification guidance")
            return

    result.warning("Consider adding verification commands")


def check_model_preferences(content: str, result: LintResult):
    """Check for model preference documentation."""
    model_patterns = [
        r"model",
        r"claude-opus",
        r"claude-sonnet",
        r"opus",
        r"sonnet",
    ]

    for pattern in model_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            result.passed_check("Documents model preferences")
            return

    result.info_msg("Consider documenting model preferences")


def check_communication_style(content: str, result: LintResult):
    """Check for communication/style guidance."""
    style_patterns = [
        r"communication",
        r"style",
        r"tone",
        r"explain",
        r"plain language",
    ]

    for pattern in style_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            result.passed_check("Has communication style guidance")
            return

    result.info_msg("Consider adding communication style guidance")


def check_tables_over_prose(content: str, result: LintResult):
    """Check for efficient information presentation."""
    # Count tables
    tables = len(re.findall(r"^\|.*\|$", content, re.MULTILINE))

    # Count long paragraphs (>100 chars without structure)
    paragraphs = re.findall(r"\n\n([^#\n|`-].{100,})\n", content)
    long_prose = len(paragraphs)

    if tables > 0:
        result.passed_check(f"Uses tables ({tables} found)")

    if long_prose > 3:
        result.warning(f"Heavy prose ({long_prose} long paragraphs) - consider tables")


def check_placeholders(content: str, result: LintResult):
    """Check for unfilled template placeholders."""
    placeholders = re.findall(r"\{\{[^}]+\}\}", content)

    if placeholders:
        result.error(f"Unfilled placeholders: {', '.join(placeholders[:3])}")
    else:
        result.passed_check("No unfilled placeholders")


def lint_claude_md(filepath: Path, is_global: bool = True) -> LintResult:
    """Main linting function."""
    result = LintResult(str(filepath))

    if not filepath.exists():
        result.error(f"File not found: {filepath}")
        return result

    content = filepath.read_text()

    # Run all checks
    check_line_count(content, result, is_global)
    check_structure(content, result)
    check_principles_vs_procedures(content, result)
    check_error_sensitivity(content, result)
    check_skill_references(content, result)
    check_verification_section(content, result)
    check_model_preferences(content, result)
    check_communication_style(content, result)
    check_tables_over_prose(content, result)
    check_placeholders(content, result)

    return result


def main():
    args = sys.argv[1:]

    # Parse arguments
    check_global = "--global" in args
    check_project = "--project" in args
    args = [a for a in args if not a.startswith("--")]

    results = []

    if check_global or (not args and not check_project):
        # Check global CLAUDE.md
        global_path = Path.home() / ".claude" / "CLAUDE.md"
        if global_path.exists():
            results.append(lint_claude_md(global_path, is_global=True))
        else:
            print(f"Global CLAUDE.md not found at {global_path}")

    if check_project:
        # Check project CLAUDE.md in current directory
        project_path = Path(".claude/CLAUDE.md")
        if project_path.exists():
            results.append(lint_claude_md(project_path, is_global=False))
        else:
            print(f"Project CLAUDE.md not found at {project_path}")

    if args:
        # Check specified file(s)
        for arg in args:
            filepath = Path(arg).expanduser()
            # Guess if it's global based on path
            is_global = ".claude/CLAUDE.md" in str(filepath) and "/.claude/" not in str(filepath).replace(str(Path.home()), "~")
            results.append(lint_claude_md(filepath, is_global=is_global))

    if not results:
        print("Usage: python lint_claude_md.py [options] [path/to/CLAUDE.md]")
        print("\nOptions:")
        print("  --global   Check ~/.claude/CLAUDE.md")
        print("  --project  Check ./.claude/CLAUDE.md")
        print("\nExamples:")
        print("  python lint_claude_md.py                    # Check global")
        print("  python lint_claude_md.py --project          # Check project")
        print("  python lint_claude_md.py --global --project # Check both")
        print("  python lint_claude_md.py ./custom/CLAUDE.md # Check specific")
        sys.exit(1)

    # Print all results
    total_errors = 0
    for result in results:
        result.print_report()
        total_errors += len(result.errors)

    sys.exit(0 if total_errors == 0 else 1)


if __name__ == "__main__":
    main()
