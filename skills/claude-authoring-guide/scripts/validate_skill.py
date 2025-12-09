#!/usr/bin/env python3
"""
Skill Structure Validator

Validates that a skill follows the claude-authoring-guide best practices.
Uses standard library only.

Usage:
    python validate_skill.py path/to/SKILL.md
    python validate_skill.py ~/.claude/skills/my-skill/
"""

import sys
import os
import re
from pathlib import Path
from typing import List, Tuple, Dict


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

    def print_report(self):
        print("\n" + "=" * 60)
        print("SKILL VALIDATION REPORT")
        print("=" * 60)

        if self.passed:
            print("\nPassed Checks:")
            for item in self.passed:
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
            print("✅ VALIDATION PASSED")
        else:
            print(f"❌ VALIDATION FAILED ({len(self.errors)} errors)")
        print("-" * 60 + "\n")


def check_frontmatter(content: str, result: ValidationResult) -> Dict:
    """Check YAML frontmatter exists and has required fields."""
    frontmatter = {}

    # Check for frontmatter delimiters
    if not content.startswith("---"):
        result.error("Missing YAML frontmatter (should start with ---)")
        return frontmatter

    # Extract frontmatter
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        result.error("Malformed frontmatter (missing closing ---)")
        return frontmatter

    fm_content = match.group(1)

    # Required fields
    required = ["name", "description"]
    for field in required:
        pattern = rf"^{field}:\s*(.+)$"
        field_match = re.search(pattern, fm_content, re.MULTILINE)
        if field_match:
            frontmatter[field] = field_match.group(1).strip()
            result.passed_check(f"Frontmatter has '{field}'")
        else:
            result.error(f"Missing required frontmatter field: {field}")

    # Optional but recommended
    optional = ["license", "model", "version"]
    for field in optional:
        pattern = rf"^{field}:\s*(.+)$"
        if re.search(pattern, fm_content, re.MULTILINE):
            result.passed_check(f"Frontmatter has '{field}'")
        else:
            result.warning(f"Consider adding frontmatter field: {field}")

    return frontmatter


def check_triggers(content: str, result: ValidationResult):
    """Check that triggers section exists and has entries."""
    if not re.search(r"##\s*Triggers?", content, re.IGNORECASE):
        result.error("Missing ## Triggers section")
        return

    result.passed_check("Has Triggers section")

    # Check for trigger phrases (backtick-wrapped or list items)
    triggers_match = re.search(
        r"##\s*Triggers?\n(.*?)(?=\n##|\Z)", content, re.DOTALL | re.IGNORECASE
    )
    if triggers_match:
        triggers_content = triggers_match.group(1)
        trigger_count = len(re.findall(r"`[^`]+`", triggers_content))
        if trigger_count >= 2:
            result.passed_check(f"Has {trigger_count} trigger phrases")
        elif trigger_count == 1:
            result.warning("Only 1 trigger phrase (recommend 3-5)")
        else:
            result.error("No trigger phrases found (use backticks)")


def check_verification(content: str, result: ValidationResult):
    """Check for verification/testing section."""
    patterns = [
        r"##\s*Verification",
        r"##\s*Testing",
        r"##\s*Validation",
        r"##\s*Quality\s*Check",
    ]

    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            result.passed_check("Has verification section")
            return

    result.warning("Consider adding ## Verification section")


def check_structure(content: str, result: ValidationResult):
    """Check overall document structure."""
    # Check for main title
    if not re.match(r"^---.*?---\s*\n#\s+", content, re.DOTALL):
        result.warning("Missing main title after frontmatter")
    else:
        result.passed_check("Has main title")

    # Count sections
    sections = re.findall(r"^##\s+.+$", content, re.MULTILINE)
    if len(sections) >= 3:
        result.passed_check(f"Has {len(sections)} sections")
    else:
        result.warning(f"Only {len(sections)} sections (recommend 3+)")

    # Check for code blocks or tables (structured content)
    has_code = "```" in content
    has_table = re.search(r"\|.*\|.*\|", content)

    if has_code or has_table:
        result.passed_check("Uses structured content (code/tables)")
    else:
        result.warning("Consider adding code blocks or tables")


def check_line_count(content: str, result: ValidationResult):
    """Check that skill isn't too long."""
    lines = content.count("\n") + 1

    if lines <= 400:
        result.passed_check(f"Line count OK ({lines} lines)")
    elif lines <= 600:
        result.warning(f"Skill is long ({lines} lines) - consider splitting")
    else:
        result.error(f"Skill too long ({lines} lines) - split into references")


def check_references(skill_dir: Path, result: ValidationResult):
    """Check for references directory if skill is complex."""
    refs_dir = skill_dir / "references"
    assets_dir = skill_dir / "assets"

    if refs_dir.exists() and any(refs_dir.iterdir()):
        result.passed_check("Has references directory")

    if assets_dir.exists():
        templates = assets_dir / "templates"
        checklists = assets_dir / "checklists"

        if templates.exists() and any(templates.iterdir()):
            result.passed_check("Has templates directory")
        if checklists.exists() and any(checklists.iterdir()):
            result.passed_check("Has checklists directory")


def validate_skill(path: str) -> ValidationResult:
    """Main validation function."""
    result = ValidationResult()
    path = Path(path).expanduser()

    # Determine if path is file or directory
    if path.is_dir():
        skill_md = path / "SKILL.md"
        if not skill_md.exists():
            result.error(f"No SKILL.md found in {path}")
            return result
        skill_dir = path
    else:
        skill_md = path
        skill_dir = path.parent

    if not skill_md.exists():
        result.error(f"File not found: {skill_md}")
        return result

    content = skill_md.read_text()

    # Run all checks
    check_frontmatter(content, result)
    check_triggers(content, result)
    check_verification(content, result)
    check_structure(content, result)
    check_line_count(content, result)

    # Directory-level checks
    if skill_dir.is_dir():
        check_references(skill_dir, result)

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_skill.py <path/to/SKILL.md or skill-directory>")
        print("\nExamples:")
        print("  python validate_skill.py ~/.claude/skills/my-skill/")
        print("  python validate_skill.py ./SKILL.md")
        sys.exit(1)

    path = sys.argv[1]
    result = validate_skill(path)
    result.print_report()

    sys.exit(0 if result.is_valid() else 1)


if __name__ == "__main__":
    main()
