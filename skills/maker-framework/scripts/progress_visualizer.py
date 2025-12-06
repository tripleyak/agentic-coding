#!/usr/bin/env python3
"""
MAKER Framework - Progress Visualizer

Displays progress and tree structure for MAKER projects.
Provides ASCII visualization for terminal-friendly output.
"""

import argparse
import json
import os
import sys
from typing import Optional


def load_project(path: str) -> dict:
    """Load project from JSON file."""
    if not os.path.exists(path):
        print(f"Error: Project file not found: {path}", file=sys.stderr)
        sys.exit(1)
    with open(path, 'r') as f:
        return json.load(f)


def render_progress_bar(completed: int, total: int, width: int = 40) -> str:
    """Render an ASCII progress bar."""
    if total == 0:
        return "[" + "." * width + "] 0%"

    filled = int((completed / total) * width)
    empty = width - filled

    bar = "[" + "#" * filled + "." * empty + "]"
    percentage = (completed / total) * 100

    return f"{bar} {percentage:.0f}% ({completed}/{total} steps)"


def render_tree(project_path: str, show_ids: bool = True) -> str:
    """
    Render the decomposition tree as ASCII art.

    Args:
        project_path: Path to project file
        show_ids: Whether to show step IDs

    Returns:
        ASCII tree representation
    """
    project = load_project(project_path)
    lines = []

    stats = project["statistics"]
    completed = stats["verified"]
    total = stats["total"]

    # Progress bar
    lines.append(render_progress_bar(completed, total))
    lines.append("")
    lines.append(f"Project: {project['name']}")

    status_icons = {
        "pending": "[ ]",
        "in_progress": "[>]",
        "verified": "[x]",
        "failed": "[!]",
        "flagged": "[?]"
    }

    current_step_id = None
    # Find current step (first in_progress)
    for step_id, step in project["steps"].items():
        if step["status"] == "in_progress":
            current_step_id = step_id
            break

    def render_step(step_id: str, prefix: str = "", is_last: bool = True) -> None:
        step = project["steps"][step_id]
        icon = status_icons.get(step["status"], "[ ]")

        # Build the connector
        connector = "└── " if is_last else "├── "

        # Build the step line
        id_part = f"[{step_id}] " if show_ids else ""
        current_marker = " ← CURRENT" if step_id == current_step_id else ""
        flag_marker = f" ({len(step['red_flags'])} flags)" if step["red_flags"] else ""

        lines.append(f"{prefix}{connector}{icon} {id_part}{step['description']}{current_marker}{flag_marker}")

        # Prepare prefix for children
        child_prefix = prefix + ("    " if is_last else "│   ")

        # Render children
        children = step["children"]
        for i, child_id in enumerate(children):
            render_step(child_id, child_prefix, i == len(children) - 1)

    # Render root steps
    root_steps = project["root_steps"]
    for i, root_id in enumerate(root_steps):
        render_step(root_id, "", i == len(root_steps) - 1)

    # Add summary footer
    lines.append("")

    # Red flags summary
    total_flags = sum(len(step["red_flags"]) for step in project["steps"].values())
    if total_flags > 0:
        lines.append(f"Red flags: {total_flags} active")

    # In progress count
    in_progress = stats["in_progress"]
    if in_progress > 0:
        lines.append(f"In progress: {in_progress}")

    return "\n".join(lines)


def render_statistics(project_path: str) -> str:
    """
    Render project statistics.

    Args:
        project_path: Path to project file

    Returns:
        Statistics summary
    """
    project = load_project(project_path)
    stats = project["statistics"]
    total = stats["total"]
    lines = []

    lines.append(f"{'='*50}")
    lines.append(f"Statistics: {project['name']}")
    lines.append(f"{'='*50}")
    lines.append("")

    # Status breakdown
    lines.append("Status Breakdown:")
    lines.append(f"  Pending:      {stats['pending']:4d}  {'█' * min(stats['pending'], 20)}")
    lines.append(f"  In Progress:  {stats['in_progress']:4d}  {'█' * min(stats['in_progress'], 20)}")
    lines.append(f"  Verified:     {stats['verified']:4d}  {'█' * min(stats['verified'], 20)}")
    lines.append(f"  Failed:       {stats['failed']:4d}  {'█' * min(stats['failed'], 20)}")
    lines.append(f"  Flagged:      {stats['flagged']:4d}  {'█' * min(stats['flagged'], 20)}")
    lines.append(f"  {'─'*30}")
    lines.append(f"  Total:        {total:4d}")
    lines.append("")

    # Success rate
    if stats["verified"] + stats["failed"] > 0:
        success_rate = stats["verified"] / (stats["verified"] + stats["failed"]) * 100
        lines.append(f"Success rate: {success_rate:.1f}%")

    # Completion rate
    if total > 0:
        completion_rate = stats["verified"] / total * 100
        lines.append(f"Completion:   {completion_rate:.1f}%")

    # Red flags detail
    lines.append("")
    lines.append("Red Flags:")
    flag_count = 0
    for step_id, step in project["steps"].items():
        for flag in step["red_flags"]:
            flag_count += 1
            lines.append(f"  [{step_id}] {flag['description'][:50]}...")
            if flag_count >= 10:
                remaining = sum(len(s["red_flags"]) for s in project["steps"].values()) - 10
                if remaining > 0:
                    lines.append(f"  ... and {remaining} more")
                break
        if flag_count >= 10:
            break

    if flag_count == 0:
        lines.append("  No red flags")

    return "\n".join(lines)


def render_step_detail(project_path: str, step_id: str) -> str:
    """
    Render detailed information for a specific step.

    Args:
        project_path: Path to project file
        step_id: Step ID to display

    Returns:
        Detailed step information
    """
    project = load_project(project_path)

    if step_id not in project["steps"]:
        return f"Error: Step not found: {step_id}"

    step = project["steps"][step_id]
    lines = []

    lines.append(f"{'='*50}")
    lines.append(f"Step Detail: [{step_id}]")
    lines.append(f"{'='*50}")
    lines.append("")

    lines.append(f"Description: {step['description']}")
    lines.append(f"Status:      {step['status'].upper()}")
    lines.append(f"Created:     {step['created_at']}")

    if step["completed_at"]:
        lines.append(f"Completed:   {step['completed_at']}")

    if step["parent_id"]:
        parent = project["steps"][step["parent_id"]]
        lines.append(f"Parent:      [{step['parent_id']}] {parent['description'][:40]}...")

    if step["children"]:
        lines.append("")
        lines.append("Children:")
        for child_id in step["children"]:
            child = project["steps"][child_id]
            lines.append(f"  [{child_id}] {child['description'][:40]}... ({child['status']})")

    if step["notes"]:
        lines.append("")
        lines.append("Notes:")
        lines.append(f"  {step['notes']}")

    if step["red_flags"]:
        lines.append("")
        lines.append("Red Flags:")
        for flag in step["red_flags"]:
            lines.append(f"  - {flag['description']}")
            lines.append(f"    Added: {flag['created_at']}")

    return "\n".join(lines)


def render_timeline(project_path: str, limit: int = 20) -> str:
    """
    Render a timeline of recent activity.

    Args:
        project_path: Path to project file
        limit: Maximum entries to show

    Returns:
        Timeline of activity
    """
    project = load_project(project_path)
    lines = []

    # Collect all events with timestamps
    events = []

    for step_id, step in project["steps"].items():
        events.append({
            "time": step["created_at"],
            "type": "created",
            "step_id": step_id,
            "description": step["description"]
        })

        if step["completed_at"]:
            events.append({
                "time": step["completed_at"],
                "type": step["status"],
                "step_id": step_id,
                "description": step["description"]
            })

        for flag in step["red_flags"]:
            events.append({
                "time": flag["created_at"],
                "type": "flagged",
                "step_id": step_id,
                "description": flag["description"]
            })

    # Sort by time descending
    events.sort(key=lambda x: x["time"], reverse=True)

    lines.append(f"{'='*50}")
    lines.append(f"Recent Activity: {project['name']}")
    lines.append(f"{'='*50}")
    lines.append("")

    type_icons = {
        "created": "+",
        "verified": "✓",
        "failed": "✗",
        "flagged": "!",
        "in_progress": ">",
        "pending": "○"
    }

    for event in events[:limit]:
        icon = type_icons.get(event["type"], "?")
        time_short = event["time"][:16].replace("T", " ")
        lines.append(f"[{icon}] {time_short} [{event['step_id']}] {event['description'][:35]}...")

    if len(events) > limit:
        lines.append(f"... and {len(events) - limit} more events")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="MAKER Framework Progress Visualizer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s tree my-project.maker.json
  %(prog)s stats my-project.maker.json
  %(prog)s step abc123 --project my-project.maker.json
  %(prog)s timeline my-project.maker.json
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # tree command
    tree_parser = subparsers.add_parser("tree", help="Display decomposition tree")
    tree_parser.add_argument("project", help="Project file path")
    tree_parser.add_argument("--no-ids", action="store_true", help="Hide step IDs")

    # stats command
    stats_parser = subparsers.add_parser("stats", help="Display statistics")
    stats_parser.add_argument("project", help="Project file path")

    # step command
    step_parser = subparsers.add_parser("step", help="Display step detail")
    step_parser.add_argument("step_id", help="Step ID to display")
    step_parser.add_argument("--project", required=True, help="Project file path")

    # timeline command
    timeline_parser = subparsers.add_parser("timeline", help="Display activity timeline")
    timeline_parser.add_argument("project", help="Project file path")
    timeline_parser.add_argument("--limit", "-n", type=int, default=20, help="Max entries to show")

    # progress command (simple one-line progress)
    progress_parser = subparsers.add_parser("progress", help="Display progress bar only")
    progress_parser.add_argument("project", help="Project file path")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "tree":
        print(render_tree(args.project, show_ids=not args.no_ids))
    elif args.command == "stats":
        print(render_statistics(args.project))
    elif args.command == "step":
        print(render_step_detail(args.project, args.step_id))
    elif args.command == "timeline":
        print(render_timeline(args.project, args.limit))
    elif args.command == "progress":
        project = load_project(args.project)
        stats = project["statistics"]
        print(render_progress_bar(stats["verified"], stats["total"]))


if __name__ == "__main__":
    main()
