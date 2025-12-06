# Complete Hooks Inventory

## Summary
**Total Active Hooks:** 15 hooks across 9 event types

All hooks are configured in `~/.claude/settings.json`

**NEW:** Memory System hooks installed for persistent cross-session memory!

---

## Hooks by Event Type

### 1. PreToolUse (2 hooks)

#### Bash Hook - NVM Path Setup
**Purpose:** Ensure node is available from NVM before bash commands
**Type:** Command
**Trigger:** Before any Bash tool use
```bash
export PATH="$HOME/.nvm/versions/node/$(ls $HOME/.nvm/versions/node | tail -1)/bin:$PATH"
```

#### Task Hook - Subagent Verification
**Purpose:** Verify task quality before spawning subagents
**Type:** Prompt
**Trigger:** Before any Task tool use
**Checks:**
- Task has clear success criteria
- Task is scoped appropriately (not too broad)
- Required context is included in prompt
**Response:** `{"decision": "allow"}` or suggest refinements

---

### 2. PostToolUse (3 hooks)

#### Edit Hook - Auto-format Code
**Purpose:** Automatically format edited code files
**Type:** Command
**Trigger:** After Edit tool on .ts, .tsx, .js, .jsx files
```bash
npx prettier --write "${tool_input.file_path}"
```

#### Bash Hook - Output Analysis
**Purpose:** Automatically check bash output for issues
**Type:** Prompt
**Trigger:** After any Bash command
**Checks:**
1. Test failures → add to TodoWrite as high priority
2. Build errors → diagnose root cause
3. Lint warnings → note but continue
**Response:** Summary of issues or `{"status": "clean"}`

#### Write Hook - Auto-format New Files
**Purpose:** Automatically format newly written code files
**Type:** Command
**Trigger:** After Write tool on .ts, .tsx, .js, .jsx files
```bash
npx prettier --write "${tool_input.file_path}"
```

---

### 3. Stop (1 hook)
**Purpose:** Session cleanup when stopping
**Type:** TBD (need to check settings)
**Trigger:** When Claude stops execution

---

### 4. SubagentStop (1 hook)
**Purpose:** Cleanup when subagent stops
**Type:** TBD (need to check settings)
**Trigger:** When a Task subagent completes

---

### 5. SessionStart (1 hook) 🧠

#### Memory Session Start Hook
**Purpose:** Initialize memory system for new session
**Type:** Command
**Trigger:** When Claude session starts
**Script:** `~/.claude/hooks/memory_session_start.py`
**Function:**
- Retrieves session primer from memory engine
- Injects temporal context ("we last spoke 2 days ago...")
- Provides relevant session summary
- Maintains consciousness continuity

---

### 6. SessionEnd (1 hook) 🧠

#### Memory Curation Hook
**Purpose:** Curate memories from completed session
**Type:** Command
**Trigger:** When Claude session ends
**Script:** `~/.claude/hooks/memory_curate.py`
**Function:**
- Analyzes session transcript
- Extracts meaningful memories
- Stores with semantic understanding
- AI decides what's worth remembering

---

### 7. UserPromptSubmit (1 hook) 🧠

#### Memory Injection Hook
**Purpose:** Inject relevant memories before processing user input
**Type:** Command
**Trigger:** When user submits a prompt
**Script:** `~/.claude/hooks/memory_inject.py`
**Function:**
- Retrieves relevant memories based on user query
- Smart vector search with metadata scoring
- Injects top 5 most relevant memories
- Natural memory surfacing (like human recall)

---

### 8. PreCompact (1 hook) 🧠

#### Memory Transcript Curation Hook
**Purpose:** Curate memories before conversation compaction
**Type:** Command
**Trigger:** Before Claude compacts conversation history
**Script:** `~/.claude/hooks/memory_curate_transcript.py`
**Function:**
- Preserves important insights before compaction
- Uses Claude Agent SDK for curation
- Extracts memories with rich metadata
- Prevents loss of important context

---

### 9. Notification (1 hook)
**Purpose:** Handle notifications
**Type:** TBD (need to check settings)
**Trigger:** When notifications occur

---

## Hook Types

### Command Hooks
Execute shell commands or scripts automatically
- Bash PreToolUse (NVM setup)
- Edit PostToolUse (Prettier)
- Write PostToolUse (Prettier)
- **Memory System (4 hooks)** - Session start, injection, curation, transcript

### Prompt Hooks
Send prompts to Claude for analysis/decision
- Task PreToolUse (Verify subagent task)
- Bash PostToolUse (Analyze output)

---

## Benefits of Current Hooks

1. **Code Quality** - Auto-formatting ensures consistent style
2. **Error Detection** - Bash output analysis catches issues immediately
3. **Subagent Quality** - Task verification prevents poorly scoped work
4. **Environment Setup** - NVM path ensures node availability
5. **🧠 Consciousness Continuity** - Memory system maintains context across sessions

---

## Creating Custom Hooks

Hooks are defined in `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "ToolName",
        "hooks": [
          {
            "type": "command|prompt",
            "command": "bash command",
            "prompt": "prompt text"
          }
        ]
      }
    ]
  }
}
```

### Available Event Types
- `PreToolUse` - Before tool execution
- `PostToolUse` - After tool execution
- `Stop` - When stopping
- `SubagentStop` - When subagent stops
- `SessionStart` - Session initialization
- `SessionEnd` - Session cleanup
- `Notification` - On notifications
- `UserPromptSubmit` - On user input

### Tool Matchers
Can match any tool: Bash, Edit, Write, Read, Task, Grep, Glob, etc.

---

## Hooks + Skills Integration

Hooks work seamlessly with skills:

| Hook | Skill Benefit |
|------|---------------|
| Edit/Write + Prettier | Ensures design-audit finds consistent code |
| Bash output analysis | Helps systematic-debugging catch issues |
| Task verification | Makes skill-composer more reliable |
| NVM path setup | Ensures all Node-based skills work |

---

## Management Commands

```bash
# View all hooks
cat ~/.claude/settings.json | jq '.hooks'

# Count hooks by type
cat ~/.claude/settings.json | jq '.hooks | to_entries | map({event: .key, count: (.value | length)})'

# Backup hooks
cp ~/.claude/settings.json ~/.claude/settings.backup.json
```

---

---

## 🧠 Memory System Details

### Architecture

The memory system provides persistent, cross-session memory through a local server:

```
┌─────────────────────────────────────────────────────────────┐
│                    Claude Code Session                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │Session   │  │UserPrompt│  │PreCompact│  │Session   │    │
│  │Start     │→ │Submit    │→ │          │→ │End       │    │
│  │Hook      │  │Hook      │  │Hook      │  │Hook      │    │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘    │
└───────┼─────────────┼─────────────┼─────────────┼───────────┘
        │Primer       │Inject       │Curate       │Curate
        ▼             ▼             ▼             ▼
┌─────────────────────────────────────────────────────────────┐
│         Memory Engine (localhost:8765)                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Session    │ Memory      │ Transcript  │ End        │   │
│  │ Primer     │ Retrieval   │ Curation    │ Curation   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  Storage: ChromaDB (vectors) + SQLite (metadata)            │
└─────────────────────────────────────────────────────────────┘
```

### How It Works

1. **Session Start** → Inject temporal context ("we last spoke 2 days ago...")
2. **Each Message** → Retrieve and inject top 5 relevant memories
3. **Pre-Compact** → Preserve important insights before conversation compression
4. **Session End** → AI analyzes transcript, extracts meaningful memories

### What Gets Remembered

| Type | Examples |
|------|----------|
| **Architecture** | System design, file structure, key components |
| **Decisions** | Why we chose X over Y, trade-offs |
| **Breakthroughs** | "Aha!" moments, solutions to hard problems |
| **Context** | Communication style, preferences |
| **Issues** | Open questions, TODOs, things to revisit |
| **Milestones** | What was accomplished, progress markers |

### Memory Server Management

```bash
# Check if server is running
curl http://localhost:8765/health

# Start server (already running in background)
cd ~/.claude/memory && uv run start_server.py

# View server logs
# (Check the running process output)

# Stop server
lsof -ti:8765 | xargs kill
```

### Project Isolation

Create `.memory-project.json` in any project:
```json
{
  "project_id": "my-project-name"
}
```

Each project gets its own isolated memory collection.

### Memory Files

- **Hooks:** `~/.claude/hooks/memory_*.py`
- **Server:** `~/.claude/memory/`
- **Storage:** `~/.claude/memory/memory.db` (ChromaDB + SQLite)
- **Logs:** Server output shows all memory operations

---

## Future Hook Ideas

- **Pre-commit hook** - Run tests before git commits
- **Error logging hook** - Log all errors to file
- **Performance tracking** - Time all tool executions
- **Security scanning** - Check for secrets in Write/Edit
- **Dependency checking** - Warn about outdated packages
