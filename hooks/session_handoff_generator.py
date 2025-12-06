#!/usr/bin/env python3
"""
Session Handoff Generator for Claude Code
Hook: SessionEnd

Generates SESSION_HANDOFF.md at the end of each session to capture:
- Current working state
- Recent changes made
- Pending tasks/blockers
- Next steps for the following session

The hook receives JSON on stdin:
{
    "session_id": "...",
    "cwd": "/current/working/directory",
    "duration_ms": 123456
}

NOTE: Uses only Python standard library (no external dependencies)
"""

import sys
import json
import os
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional


def run_command(cmd: list, cwd: str, timeout: int = 10) -> str:
    """Run a shell command and return output."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout.strip()
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, FileNotFoundError):
        return ""


def find_project_root(cwd: str) -> Optional[Path]:
    """
    Find project root by looking for CLAUDE.md or .git directory.
    Returns None if not in a project.
    """
    path = Path(cwd)

    for parent in [path] + list(path.parents):
        # Stop at home directory
        if parent == Path.home():
            return None
        # Look for project markers
        if (parent / "CLAUDE.md").exists() or (parent / ".git").exists():
            return parent

    return None


def get_git_branch(cwd: str) -> str:
    """Get current git branch name."""
    return run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd)


def get_git_status(cwd: str) -> str:
    """Get git status summary."""
    return run_command(["git", "status", "--short"], cwd)


def get_recent_commits(cwd: str, count: int = 5) -> str:
    """Get recent commit messages."""
    return run_command(
        ["git", "log", f"-{count}", "--oneline", "--no-decorate"],
        cwd
    )


def get_uncommitted_files(cwd: str) -> list:
    """Get list of uncommitted/untracked files."""
    status = run_command(["git", "status", "--porcelain"], cwd)
    if not status:
        return []

    files = []
    for line in status.split('\n'):
        if line.strip():
            # Format: "XY filename" where XY is status codes
            parts = line.split(maxsplit=1)
            if len(parts) >= 2:
                files.append(parts[1])
    return files


def get_stash_count(cwd: str) -> int:
    """Get number of stashed changes."""
    stash_list = run_command(["git", "stash", "list"], cwd)
    if not stash_list:
        return 0
    return len(stash_list.split('\n'))


def read_existing_handoff(project_root: Path) -> dict:
    """Read existing SESSION_HANDOFF.md if it exists."""
    handoff_path = project_root / "SESSION_HANDOFF.md"
    if not handoff_path.exists():
        return {}

    try:
        with open(handoff_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse basic sections (simple extraction)
        sections = {}
        current_section = None
        current_content = []

        for line in content.split('\n'):
            if line.startswith('## '):
                if current_section:
                    sections[current_section] = '\n'.join(current_content).strip()
                current_section = line[3:].strip()
                current_content = []
            elif current_section:
                current_content.append(line)

        if current_section:
            sections[current_section] = '\n'.join(current_content).strip()

        return sections
    except Exception:
        return {}


def generate_handoff(project_root: Path, session_id: str, duration_ms: int) -> str:
    """Generate SESSION_HANDOFF.md content."""
    cwd = str(project_root)
    now = datetime.now()

    # Gather git information
    branch = get_git_branch(cwd) or "unknown"
    uncommitted = get_uncommitted_files(cwd)
    recent_commits = get_recent_commits(cwd, 5)
    stash_count = get_stash_count(cwd)

    # Format duration
    duration_minutes = duration_ms // 60000 if duration_ms else 0
    duration_str = f"{duration_minutes} minutes" if duration_minutes > 0 else "< 1 minute"

    # Build handoff document
    lines = [
        f"# Session Handoff - {project_root.name}",
        "",
        f"**Last Updated:** {now.strftime('%Y-%m-%d %H:%M')}",
        f"**Session Duration:** {duration_str}",
        "",
        "---",
        "",
        "## Git State",
        "",
        f"- **Branch:** `{branch}`",
        f"- **Stashes:** {stash_count}",
    ]

    if uncommitted:
        lines.append(f"- **Uncommitted Files:** {len(uncommitted)}")
        lines.append("")
        lines.append("### Uncommitted Changes")
        lines.append("```")
        for f in uncommitted[:20]:  # Limit to 20 files
            lines.append(f)
        if len(uncommitted) > 20:
            lines.append(f"... and {len(uncommitted) - 20} more files")
        lines.append("```")
    else:
        lines.append("- **Uncommitted Files:** None (clean working tree)")

    lines.extend([
        "",
        "## Recent Commits",
        "",
    ])

    if recent_commits:
        lines.append("```")
        lines.append(recent_commits)
        lines.append("```")
    else:
        lines.append("*No recent commits found*")

    lines.extend([
        "",
        "## Session Summary",
        "",
        "*[Auto-populated section - add summary of work completed]*",
        "",
        "### Work Completed",
        "- ",
        "",
        "### In Progress",
        "- ",
        "",
        "### Blockers/Issues",
        "- None identified",
        "",
        "## Next Session Priorities",
        "",
        "1. ",
        "2. ",
        "3. ",
        "",
        "---",
        "",
        "*This file is auto-generated at session end. Update the summary sections manually or they will be preserved between sessions.*",
    ])

    return '\n'.join(lines)


def merge_with_existing(new_content: str, existing_sections: dict) -> str:
    """Preserve user-edited sections from existing handoff."""
    if not existing_sections:
        return new_content

    # Sections to preserve if user has edited them
    preserve_sections = [
        "Session Summary",
        "Next Session Priorities",
    ]

    result_lines = []
    current_section = None
    skip_until_next_section = False

    for line in new_content.split('\n'):
        if line.startswith('## '):
            section_name = line[3:].strip()
            current_section = section_name
            skip_until_next_section = False

            # Check if we should preserve existing content
            if section_name in preserve_sections and section_name in existing_sections:
                existing = existing_sections[section_name]
                # Only preserve if it's been customized (not default)
                if existing and not existing.startswith('*[Auto-populated'):
                    result_lines.append(line)
                    result_lines.append("")
                    result_lines.append(existing)
                    skip_until_next_section = True
                    continue

        if not skip_until_next_section:
            result_lines.append(line)

    return '\n'.join(result_lines)


def main():
    """Main hook entry point."""
    # Skip if called from memory curator
    if os.getenv("MEMORY_CURATOR_ACTIVE") == "1":
        return

    try:
        # Read input from stdin
        input_data = json.load(sys.stdin)

        session_id = input_data.get("session_id", "unknown")
        cwd = input_data.get("cwd", os.getcwd())
        duration_ms = input_data.get("duration_ms", 0)

        # Find project root
        project_root = find_project_root(cwd)
        if not project_root:
            # Not in a project, skip handoff generation
            return

        # Read existing handoff to preserve user edits
        existing_sections = read_existing_handoff(project_root)

        # Generate new handoff content
        new_content = generate_handoff(project_root, session_id, duration_ms)

        # Merge with existing (preserve user-edited sections)
        final_content = merge_with_existing(new_content, existing_sections)

        # Write SESSION_HANDOFF.md
        handoff_path = project_root / "SESSION_HANDOFF.md"
        with open(handoff_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        # Output confirmation (visible in session end output)
        print(f"Session handoff saved to {handoff_path}")

    except Exception as e:
        # Log error but don't crash
        print(f"Error generating session handoff: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
