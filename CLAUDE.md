# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Model Context Protocol (MCP) server** that provides communication assistance tools for neurodivergent professionals in technical workplaces. The server is built using FastMCP and provides 11 communication tools and 5 resource files.

**Design philosophy:** Treats neurodivergent communication patterns as different, not deficient. Supports bottom-up processing, explicit over implicit communication, and external working memory.

## Repository Structure

```
src/
├── server.py              # Main MCP server implementation
├── __init__.py
└── resources/             # Communication rule files (markdown)
    ├── message-clarity.md
    ├── context-interpretation.md
    ├── tone-calibration.md
    ├── meeting-structure.md
    └── document-scaffolding.md
```

## Testing and Running

### Run the MCP server manually

```bash
python3 src/server.py
```

The server will start and wait for MCP protocol connections. Press Ctrl+C to stop.

### Test FastMCP installation

```bash
python3 -c "import mcp.server.fastmcp; print('✓ FastMCP OK')"
```

### Verify Python version

```bash
python3 --version  # Must be 3.10+
```

## Architecture

### MCP Server Pattern

The server uses FastMCP's decorator-based pattern:

- **Resources** (`@mcp.resource()`): Background knowledge files loaded automatically by the LLM. These provide communication rules and patterns that inform how tools analyze messages.

- **Tools** (`@mcp.tool()`): Functions the LLM can execute. Each tool returns a JSON structure containing both the input data and an analysis framework that guides the LLM's response.

### Tool Design Pattern

All tools follow a consistent pattern:

1. Accept input parameters (message text, context, relationships)
2. Build structured data from inputs
3. Return JSON with:
   - Input data (what the user provided)
   - Analysis framework (questions/structure for the LLM to follow)
   - Optional reference data (common patterns, safe phrases, etc.)

**The tools don't do the analysis themselves** - they provide structure for the LLM to perform analysis using the loaded resource files.

### Resource Loading

Resources are loaded from `src/resources/` directory:
- Files are markdown format
- Loaded via `Path(__file__).parent / "resources" / "filename.md"`
- URI pattern: `comms://rules/{resource-name}`

## Making Changes

### Adding a New Tool

1. Add new `@mcp.tool()` decorated function in `src/server.py`
2. Follow existing pattern: return JSON with input + framework
3. Include comprehensive docstring (shows up in MCP protocol)
4. Parameters should have type hints and defaults where appropriate
5. Update README.md to reflect new tool count and description

### Adding a New Resource

1. Create markdown file in `src/resources/`
2. Add `@mcp.resource()` function in `src/server.py`
3. Use URI pattern: `comms://rules/{resource-name}`
4. Return contents via `Path.read_text()`
5. Update README.md to reflect new resource

### Modifying Resource Content

Resource files are **instructional guides** for the LLM. They should:
- Be concise and scannable
- Use bullet points and clear structure
- Provide specific patterns and examples
- Avoid being too prescriptive (LLM needs flexibility)

## Development Requirements

- Python 3.10+ (required by FastMCP)
- Dependencies: `mcp>=1.0.0` (see pyproject.toml)
- Optional dev dependencies: pytest, black

## Installation for Testing

Users install this by:
1. Installing FastMCP: `python3 -m pip install --user fastmcp`
2. Configuring Claude Desktop or Q CLI to point to `src/server.py`
3. Restarting their MCP client

See INSTALL.md for complete installation instructions.

## Important Notes

### This is NOT a Python Package (Yet)

The project is structured like a package but currently runs as a script. The `[project.scripts]` in pyproject.toml is for future PyPI distribution. Users currently run `src/server.py` directly.

### Path Handling

Always use `Path(__file__).parent` for resource loading since the server runs from different working directories depending on how it's launched.

### Error Handling

The server should start without errors. If resource files are missing, the server will fail at startup. Validate that all referenced resources exist.

### JSON Return Pattern

Tools return JSON strings, not dicts. This is intentional - the JSON structure serves as a prompt template for the LLM to fill in when generating responses.

## Communication Tools (11 Total)

1. **check_message** - Analyze drafts for clarity, tone, structure, completeness
2. **decode_message** - Extract explicit and implicit meaning from vague messages
3. **prep_meeting** - Generate talking points and preparation framework
4. **scaffold_document** - Preview document structure before deep reading
5. **check_tone** - Validate tone and flag potential misinterpretations
6. **call_or_text** - Recommend communication method (call/text/video)
7. **synthesize_thoughts** - Organize scattered thoughts into clear messages
8. **catch_up_thread** - Summarize long email/Slack threads
9. **summarize_meeting** - Extract decisions and action items from notes
10. **ask_clarity** - Draft polite messages requesting clarification
11. **unstuck_reading** - Strategy to overcome reading paralysis

## Future Roadmap

- Publish to PyPI (`pip install neurodivergent-comms-mcp`)
- Workplace integrations (Slack, email)
- Conversation memory for user preferences
- Additional tools based on feedback
