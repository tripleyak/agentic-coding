---
name: codanna
license: MIT
model: claude-opus-4-5-20251101
subagent_model: claude-opus-4-5-20251101
domains: [code-analysis, search, architecture, debugging]
type: analyzer
inputs: [codebase, source files]
outputs: [search results, call graphs, symbol relationships]
requires: [cargo/rust, codanna binary]
integrates_with: [AppMap, CodeReview, Refactor, ArchitectPlan]
---

# Codanna Skill

Semantic code indexing and search. Index your codebase so Claude can search by meaning, trace call relationships, and track implementations.

## Triggers

- `codanna` - General Codanna operations
- `semantic search` - Search code by meaning
- `find callers` - What calls this function?
- `find implementations` - What implements this trait/interface?
- `trace calls` - Call graph analysis
- `index codebase` - Set up Codanna indexing
- `code relationships` - Understand code dependencies

## What Codanna Does

| Capability | Description |
|------------|-------------|
| **Semantic Search** | Find code by meaning: "authentication logic" |
| **Call Tracing** | What functions call `parse_file()`? |
| **Implementation Tracking** | What implements the `Parser` trait? |
| **Symbol Lookup** | Fast symbol resolution (<10ms) |
| **Impact Analysis** | What's affected if I change this? |

## Performance

| Metric | Value |
|--------|-------|
| Parse Speed | 75,000+ symbols/sec |
| Symbol Lookup | <10ms (memory-mapped cache) |
| Search Response | ~300ms |
| Index Size | Few MB |

## Supported Languages

Rust, Python, JavaScript, TypeScript, Java, Kotlin, Go, PHP, C, C++, C#, Swift, GDScript (12 languages)

---

## Installation

### Prerequisites

```bash
# macOS: No additional deps needed
# Linux:
sudo apt install pkg-config libssl-dev

# Rust 1.75+ required
```

### Install Codanna

```bash
cargo install codanna --all-features
```

Model storage (~150MB) auto-downloads on first use.

---

## Quick Setup

### 1. Initialize in Project

```bash
cd /path/to/your/project
codanna init
```

Creates `.codanna/` directory for config and index.

### 2. Index Your Code

```bash
# Index entire project
codanna index . --progress

# Index specific directories
codanna index src tests lib --progress

# Add directory to existing index
codanna add-dir src --progress
```

### 3. Configure File Ignores

Create `.codannaignore` (same syntax as `.gitignore`):

```
node_modules/
dist/
build/
*.min.js
```

---

## MCP Server Integration

### Claude Code Configuration

Add to `.claude/settings.json` or `.claude/settings.local.json`:

```json
{
  "mcpServers": {
    "codanna": {
      "command": "codanna",
      "args": ["serve", "--watch"]
    }
  }
}
```

The `--watch` flag enables file watching for automatic re-indexing on changes.

### Profile-Based Setup (v0.6.8+)

```bash
codanna init --force
codanna profile provider add bartolli/codanna-profiles
codanna profile install claude@codanna-profiles
npm --prefix .claude/hooks/codanna install
```

---

## CLI Commands

### Semantic Search

Search code by meaning, not just text:

```bash
# Search for concept
codanna mcp semantic_search_docs query:"authentication logic" limit:5

# Search with higher limit
codanna mcp semantic_search_docs query:"where do we handle errors" limit:10
```

Returns relevant functions with file locations and signatures.

### Find Callers

What functions call a given symbol?

```bash
codanna mcp find_callers parse_file
codanna mcp find_callers authenticate_user
```

### Find Symbol

Locate a symbol definition:

```bash
codanna mcp find_symbol UserService
codanna mcp find_symbol handle_request
```

### Get Calls

What does a function call?

```bash
codanna mcp get_calls main
codanna mcp get_calls process_data
```

### Analyze Impact

What's affected if this changes?

```bash
codanna mcp analyze_impact DatabaseConnection
codanna mcp analyze_impact parse_config
```

---

## Usage Patterns

### Pattern 1: Understand New Codebase

```bash
# 1. Index the project
codanna init && codanna index . --progress

# 2. Find entry points
codanna mcp semantic_search_docs query:"main entry point" limit:3

# 3. Trace from entry
codanna mcp get_calls main
```

### Pattern 2: Find Implementation Locations

```bash
# Where is authentication handled?
codanna mcp semantic_search_docs query:"user authentication validation" limit:5

# What implements the auth interface?
codanna mcp find_callers AuthProvider
```

### Pattern 3: Impact Analysis Before Changes

```bash
# What calls this function I'm about to modify?
codanna mcp find_callers parse_config

# What would be affected?
codanna mcp analyze_impact ConfigParser
```

### Pattern 4: Debug Investigation

```bash
# Find error handling
codanna mcp semantic_search_docs query:"error handling retry logic" limit:5

# Trace the error path
codanna mcp find_callers handle_error
```

---

## Unix Integration

Pipe output for scripting:

```bash
# List callers with file paths
codanna mcp find_callers index_file --json | \
  jq -r '.data[]?[0] | "\(.name) - \(.file_path)"'

# Find all implementations and filter
codanna mcp find_symbol Parser --json | \
  jq '.data[] | select(.type == "impl")'
```

---

## Configuration

### codanna.toml

Project-level configuration in `.codanna/codanna.toml`:

```toml
[index]
include = ["src", "lib", "tests"]
exclude = ["node_modules", "dist", "*.min.js"]

[server]
port = 3000
watch = true

[embedding]
model = "default"  # Auto-downloads on first use
```

---

## Workflow Integration

### With Claude Code

1. Set up MCP server (see above)
2. Use naturally in conversation:
   - "What calls the `handleAuth` function?"
   - "Find where we validate user input"
   - "Show me the authentication implementation"

### Agent Workflow Pattern

Best practice for AI-assisted code exploration:

1. **Semantic search** to locate relevant code area
2. **Impact analysis** to map dependencies
3. **Symbol lookup** and **call tracing** for specifics
4. Make informed changes with full context

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Slow indexing | Check `.codannaignore`, exclude build dirs |
| Missing symbols | Re-run `codanna index . --progress` |
| MCP not connecting | Verify `codanna serve` runs, check settings.json |
| Old results | Use `--watch` flag or re-index |

### Verify Installation

```bash
# Check version
codanna --version

# Test MCP commands
codanna mcp find_symbol main

# Test server
codanna serve --watch
```

---

## Resources

- **GitHub:** https://github.com/bartolli/codanna
- **Docs:** `/docs` in repository
- **License:** Apache License 2.0
- **Version:** 0.8.3 (Dec 2025)

---

## Quick Reference

| Task | Command |
|------|---------|
| Initialize | `codanna init` |
| Index all | `codanna index . --progress` |
| Search meaning | `codanna mcp semantic_search_docs query:"..." limit:N` |
| Find callers | `codanna mcp find_callers SYMBOL` |
| Find symbol | `codanna mcp find_symbol NAME` |
| Get calls | `codanna mcp get_calls FUNCTION` |
| Impact | `codanna mcp analyze_impact SYMBOL` |
| Start server | `codanna serve --watch` |
