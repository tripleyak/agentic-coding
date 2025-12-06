#!/usr/bin/env python3
"""
MAKER Framework - Project Tracker

Manages decomposition tree and execution state for MAKER projects.
Stores project data in JSON files for persistence across sessions.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Optional
import uuid


def generate_id() -> str:
    """Generate a short unique ID for steps."""
    return uuid.uuid4().hex[:8]


def get_timestamp() -> str:
    """Get current timestamp in ISO format."""
    return datetime.now().isoformat()


def load_project(path: str) -> dict:
    """Load project from JSON file."""
    if not os.path.exists(path):
        print(f"Error: Project file not found: {path}", file=sys.stderr)
        sys.exit(1)
    with open(path, 'r') as f:
        return json.load(f)


def save_project(path: str, project: dict) -> None:
    """Save project to JSON file."""
    with open(path, 'w') as f:
        json.dump(project, f, indent=2)


def init_project(name: str, description: str, output_path: Optional[str] = None) -> str:
    """
    Initialize a new MAKER project.

    Args:
        name: Project name
        description: Project description
        output_path: Optional path for the project file

    Returns:
        Path to the created project file
    """
    project = {
        "name": name,
        "description": description,
        "created_at": get_timestamp(),
        "updated_at": get_timestamp(),
        "steps": {},
        "root_steps": [],  # IDs of top-level steps (no parent)
        "statistics": {
            "total": 0,
            "pending": 0,
            "in_progress": 0,
            "verified": 0,
            "failed": 0,
            "flagged": 0
        }
    }

    if output_path is None:
        # Create in current directory with sanitized name
        safe_name = name.lower().replace(' ', '-').replace('/', '-')
        output_path = f"{safe_name}.maker.json"

    save_project(output_path, project)
    print(f"Created project: {output_path}")
    return output_path


def add_step(project_path: str, description: str, parent_id: Optional[str] = None) -> str:
    """
    Add a new step to the project.

    Args:
        project_path: Path to project file
        description: Step description
        parent_id: Optional parent step ID

    Returns:
        ID of the created step
    """
    project = load_project(project_path)

    step_id = generate_id()
    step = {
        "id": step_id,
        "description": description,
        "parent_id": parent_id,
        "children": [],
        "status": "pending",
        "verification_result": None,
        "red_flags": [],
        "notes": "",
        "created_at": get_timestamp(),
        "completed_at": None
    }

    project["steps"][step_id] = step
    project["statistics"]["total"] += 1
    project["statistics"]["pending"] += 1

    if parent_id:
        if parent_id not in project["steps"]:
            print(f"Error: Parent step not found: {parent_id}", file=sys.stderr)
            sys.exit(1)
        project["steps"][parent_id]["children"].append(step_id)
    else:
        project["root_steps"].append(step_id)

    project["updated_at"] = get_timestamp()
    save_project(project_path, project)

    print(f"Added step [{step_id}]: {description}")
    if parent_id:
        print(f"  Parent: {parent_id}")
    return step_id


def update_status(project_path: str, step_id: str, status: str, notes: str = "") -> None:
    """
    Update the status of a step.

    Args:
        project_path: Path to project file
        step_id: Step ID to update
        status: New status (pending, in_progress, verified, failed, flagged)
        notes: Optional notes about the update
    """
    valid_statuses = ["pending", "in_progress", "verified", "failed", "flagged"]
    if status not in valid_statuses:
        print(f"Error: Invalid status '{status}'. Must be one of: {valid_statuses}", file=sys.stderr)
        sys.exit(1)

    project = load_project(project_path)

    if step_id not in project["steps"]:
        print(f"Error: Step not found: {step_id}", file=sys.stderr)
        sys.exit(1)

    step = project["steps"][step_id]
    old_status = step["status"]

    # Update statistics
    project["statistics"][old_status] -= 1
    project["statistics"][status] += 1

    # Update step
    step["status"] = status
    if notes:
        step["notes"] = notes
    if status in ["verified", "failed"]:
        step["completed_at"] = get_timestamp()
        step["verification_result"] = status

    project["updated_at"] = get_timestamp()
    save_project(project_path, project)

    print(f"Updated [{step_id}]: {old_status} -> {status}")


def add_red_flag(project_path: str, step_id: str, flag_description: str) -> None:
    """
    Add a red flag to a step.

    Args:
        project_path: Path to project file
        step_id: Step ID to flag
        flag_description: Description of the red flag
    """
    project = load_project(project_path)

    if step_id not in project["steps"]:
        print(f"Error: Step not found: {step_id}", file=sys.stderr)
        sys.exit(1)

    step = project["steps"][step_id]
    flag = {
        "description": flag_description,
        "created_at": get_timestamp()
    }
    step["red_flags"].append(flag)

    # Update status to flagged if not already
    if step["status"] != "flagged":
        old_status = step["status"]
        project["statistics"][old_status] -= 1
        project["statistics"]["flagged"] += 1
        step["status"] = "flagged"

    project["updated_at"] = get_timestamp()
    save_project(project_path, project)

    print(f"Added red flag to [{step_id}]: {flag_description}")


def get_next_step(project_path: str) -> Optional[dict]:
    """
    Get the next step to work on.

    Returns the first pending step whose parent (if any) is verified.
    """
    project = load_project(project_path)

    def can_start(step_id: str) -> bool:
        step = project["steps"][step_id]
        if step["status"] != "pending":
            return False
        if step["parent_id"]:
            parent = project["steps"][step["parent_id"]]
            # Parent must be verified or in_progress (milestone-level)
            if parent["status"] not in ["verified", "in_progress"]:
                return False
        return True

    # BFS through the tree to find next step
    def find_next(step_ids: list) -> Optional[dict]:
        for step_id in step_ids:
            step = project["steps"][step_id]
            if can_start(step_id):
                return step
            # Check children
            if step["children"]:
                result = find_next(step["children"])
                if result:
                    return result
        return None

    return find_next(project["root_steps"])


def show_status(project_path: str) -> None:
    """Display project status summary."""
    project = load_project(project_path)

    stats = project["statistics"]
    total = stats["total"]
    completed = stats["verified"]

    print(f"\n{'='*50}")
    print(f"Project: {project['name']}")
    print(f"{'='*50}")
    print(f"\nDescription: {project['description']}")
    print(f"Created: {project['created_at']}")
    print(f"Updated: {project['updated_at']}")

    print(f"\n--- Statistics ---")
    print(f"Total steps:    {total}")
    print(f"Pending:        {stats['pending']}")
    print(f"In Progress:    {stats['in_progress']}")
    print(f"Verified:       {stats['verified']}")
    print(f"Failed:         {stats['failed']}")
    print(f"Flagged:        {stats['flagged']}")

    if total > 0:
        progress = (completed / total) * 100
        print(f"\nProgress: {progress:.1f}%")

    # Show next step
    next_step = get_next_step(project_path)
    if next_step:
        print(f"\n--- Next Step ---")
        print(f"[{next_step['id']}] {next_step['description']}")

    # Show active red flags
    flags = []
    for step_id, step in project["steps"].items():
        for flag in step["red_flags"]:
            flags.append((step_id, step["description"], flag["description"]))

    if flags:
        print(f"\n--- Active Red Flags ({len(flags)}) ---")
        for step_id, step_desc, flag_desc in flags[:5]:  # Show first 5
            print(f"[{step_id}] {step_desc[:30]}...")
            print(f"  Flag: {flag_desc}")


def list_steps(project_path: str, status_filter: Optional[str] = None) -> None:
    """List all steps, optionally filtered by status."""
    project = load_project(project_path)

    def print_step(step_id: str, indent: int = 0) -> None:
        step = project["steps"][step_id]
        if status_filter and step["status"] != status_filter:
            # Still recurse to children
            for child_id in step["children"]:
                print_step(child_id, indent)
            return

        status_icons = {
            "pending": "[ ]",
            "in_progress": "[>]",
            "verified": "[x]",
            "failed": "[!]",
            "flagged": "[?]"
        }
        icon = status_icons.get(step["status"], "[ ]")
        prefix = "  " * indent
        print(f"{prefix}{icon} [{step_id}] {step['description']}")

        for child_id in step["children"]:
            print_step(child_id, indent + 1)

    print(f"\nSteps for: {project['name']}")
    if status_filter:
        print(f"Filter: {status_filter}")
    print("-" * 40)

    for root_id in project["root_steps"]:
        print_step(root_id)


def export_tree(project_path: str, format: str = "text") -> str:
    """Export the project tree in specified format."""
    project = load_project(project_path)

    if format == "json":
        return json.dumps(project, indent=2)

    # Text format
    lines = [f"# {project['name']}", "", project['description'], ""]

    def add_step(step_id: str, indent: int = 0) -> None:
        step = project["steps"][step_id]
        status_icons = {
            "pending": "[ ]",
            "in_progress": "[>]",
            "verified": "[x]",
            "failed": "[!]",
            "flagged": "[?]"
        }
        icon = status_icons.get(step["status"], "[ ]")
        prefix = "  " * indent
        lines.append(f"{prefix}{icon} {step['description']}")

        for child_id in step["children"]:
            add_step(child_id, indent + 1)

    for root_id in project["root_steps"]:
        add_step(root_id)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="MAKER Framework Project Tracker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s init "My Project" "Description of the project"
  %(prog)s add-step "First milestone" --project my-project.maker.json
  %(prog)s add-step "Sub-task" --parent abc123 --project my-project.maker.json
  %(prog)s update abc123 --status verified --project my-project.maker.json
  %(prog)s flag abc123 "Output was too long" --project my-project.maker.json
  %(prog)s status --project my-project.maker.json
  %(prog)s list --project my-project.maker.json
  %(prog)s next --project my-project.maker.json
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize a new project")
    init_parser.add_argument("name", help="Project name")
    init_parser.add_argument("description", help="Project description")
    init_parser.add_argument("--output", "-o", help="Output file path")

    # add-step command
    add_parser = subparsers.add_parser("add-step", help="Add a step to the project")
    add_parser.add_argument("description", help="Step description")
    add_parser.add_argument("--parent", "-p", help="Parent step ID")
    add_parser.add_argument("--project", required=True, help="Project file path")

    # update command
    update_parser = subparsers.add_parser("update", help="Update step status")
    update_parser.add_argument("step_id", help="Step ID to update")
    update_parser.add_argument("--status", "-s", required=True,
                               choices=["pending", "in_progress", "verified", "failed", "flagged"],
                               help="New status")
    update_parser.add_argument("--notes", "-n", default="", help="Notes about the update")
    update_parser.add_argument("--project", required=True, help="Project file path")

    # flag command
    flag_parser = subparsers.add_parser("flag", help="Add a red flag to a step")
    flag_parser.add_argument("step_id", help="Step ID to flag")
    flag_parser.add_argument("description", help="Red flag description")
    flag_parser.add_argument("--project", required=True, help="Project file path")

    # status command
    status_parser = subparsers.add_parser("status", help="Show project status")
    status_parser.add_argument("--project", required=True, help="Project file path")

    # list command
    list_parser = subparsers.add_parser("list", help="List all steps")
    list_parser.add_argument("--status", "-s", help="Filter by status")
    list_parser.add_argument("--project", required=True, help="Project file path")

    # next command
    next_parser = subparsers.add_parser("next", help="Show next step to work on")
    next_parser.add_argument("--project", required=True, help="Project file path")

    # export command
    export_parser = subparsers.add_parser("export", help="Export project tree")
    export_parser.add_argument("--format", "-f", choices=["text", "json"], default="text",
                               help="Export format")
    export_parser.add_argument("--project", required=True, help="Project file path")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "init":
        init_project(args.name, args.description, args.output)
    elif args.command == "add-step":
        add_step(args.project, args.description, args.parent)
    elif args.command == "update":
        update_status(args.project, args.step_id, args.status, args.notes)
    elif args.command == "flag":
        add_red_flag(args.project, args.step_id, args.description)
    elif args.command == "status":
        show_status(args.project)
    elif args.command == "list":
        list_steps(args.project, args.status)
    elif args.command == "next":
        project = load_project(args.project)
        next_step = get_next_step(args.project)
        if next_step:
            print(f"Next step: [{next_step['id']}] {next_step['description']}")
        else:
            print("No pending steps available")
    elif args.command == "export":
        output = export_tree(args.project, args.format)
        print(output)


if __name__ == "__main__":
    main()
