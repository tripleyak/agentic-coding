#!/usr/bin/env python3
"""
{{HOOK_DESCRIPTION}}
Hook: {{HOOK_TYPE}}

{{DETAILED_DESCRIPTION}}

Input (JSON via stdin):
{
    "session_id": "...",
    "prompt": "...",      # For UserPromptSubmit
    "tool_input": {...},  # For PreToolUse/PostToolUse
    "cwd": "..."
}

Output (stdout):
{{OUTPUT_DESCRIPTION}}

NOTE: Uses only Python standard library (no external dependencies)
"""

import sys
import json
import os
from pathlib import Path

# Configuration
TIMEOUT_SECONDS = 5  # Keep hooks fast


def main():
    """Main hook entry point."""
    try:
        # Read input from stdin
        input_data = json.load(sys.stdin)

        # Extract common fields
        session_id = input_data.get("session_id", "unknown")
        cwd = input_data.get("cwd", os.getcwd())

        # Process based on hook type
        result = process(input_data)

        # Output result (if any)
        if result:
            print(result)

    except Exception:
        # Never crash - hooks must be resilient
        # Output nothing on error
        pass


def process(input_data: dict) -> str:
    """
    Process the hook input and return output.

    Args:
        input_data: JSON data from stdin

    Returns:
        String to output (or None/empty for no output)
    """
    # {{IMPLEMENTATION}}
    pass


if __name__ == "__main__":
    main()


# --- Template Usage Instructions (delete after customizing) ---
#
# HOOK TYPES:
#   - UserPromptSubmit: Before user message is processed
#   - PreToolUse: Before a tool runs
#   - PostToolUse: After a tool completes
#   - SessionStart: When session begins
#   - SessionEnd: When session ends
#   - PreCompact: Before context compaction
#
# REQUIRED:
#   - chmod +x this file
#   - Use only Python standard library
#   - Never crash (always catch exceptions)
#   - Complete in < 5 seconds
#
# INPUT FIELDS BY HOOK TYPE:
#   UserPromptSubmit: session_id, prompt, cwd
#   PreToolUse: session_id, tool_name, tool_input, cwd
#   PostToolUse: session_id, tool_name, tool_output, cwd
#   SessionStart: session_id, cwd
#   SessionEnd: session_id, cwd
#
# OUTPUT BEHAVIOR:
#   - UserPromptSubmit: stdout prepended to user message
#   - PreToolUse: return "block" to prevent tool execution
#   - PostToolUse: stdout appended to tool output
#   - Others: stdout typically ignored
#
# FILE LOCATION:
#   Save to: ~/.claude/hooks/{{hook-name}}.py
#
# QUALITY CHECKLIST:
#   - [ ] Executable (chmod +x)
#   - [ ] No external dependencies
#   - [ ] Handles all exceptions gracefully
#   - [ ] Completes within timeout
#   - [ ] JSON I/O only
