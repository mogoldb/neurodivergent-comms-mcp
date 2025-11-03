# Neurodivergent Communications MCP Server

**Communication assistance tools for neurodivergent professionals in technical workplaces.**

Works with Claude Desktop, Amazon Q CLI, and any MCP-compatible AI system.

---

## What This Does

Helps with communication challenges common in neurodivergent professionals:

- ✅ **Check messages** before sending (tone, clarity, completeness)
- ✅ **Decode vague messages** from others (implicit asks, real deadlines)
- ✅ **Prep for meetings** (talking points, questions, what to expect)
- ✅ **Scaffold complex documents** (structure before reading)
- ✅ **Organize scattered thoughts** into clear messages
- ✅ **Catch up on long email threads** (extract what you need to know)
- ✅ **Decide call vs text** (based on complexity and urgency)
- ✅ **Get unstuck on reading** (strategy to start overwhelming docs)
- ...and more!

**You shouldn't spend 45 minutes editing a 3-line email.**

---

## Quick Start

### 1. Install

See **[INSTALL.md](INSTALL.md)** for detailed instructions.

**TL;DR:**
```bash
# Install FastMCP
python3 -m pip install --user fastmcp

# Clone this repo
git clone https://github.com/mogoldb/neurodivergent-comms-mcp.git

# Configure Claude Desktop or Q CLI (see INSTALL.md)
```

### 2. Try It

See **[EXAMPLES.md](EXAMPLES.md)** for real-world usage examples.

**Quick test:**
```
Can you check this message: Hey team, thoughts on approach B?
```

Your AI assistant should analyze it for clarity, tone, and effectiveness!

---

## How to Use

Once installed, just talk naturally to your AI assistant:

**Examples:**

```
"Check this email before I send it: [paste]"
→ Calls check_message tool

"I got this confusing message from my manager: [paste]
What do they actually want?"
→ Calls decode_message tool

"Help me prep for tomorrow's architecture review"
→ Calls prep_meeting tool

"I need to read this 50-page design doc but I'm overwhelmed"
→ Calls scaffold_document or unstuck_reading tool
```

The AI automatically picks the right tool based on what you need.

---

## What's Included

### 11 Communication Tools

Your AI assistant can call these functions to help you:

1. **check_message** - Analyze message drafts for clarity, tone, structure
2. **decode_message** - Extract explicit and implicit meaning from confusing messages
3. **prep_meeting** - Generate talking points and preparation for meetings
4. **scaffold_document** - Preview document structure before deep reading
5. **check_tone** - Validate tone and flag potential misinterpretations
6. **call_or_text** - Recommend communication method (call/text/video)
7. **synthesize_thoughts** - Organize scattered thoughts into clear message
8. **catch_up_thread** - Summarize long email/Slack threads
9. **summarize_meeting** - Extract decisions and action items from notes
10. **ask_clarity** - Draft polite messages asking for clarity
11. **unstuck_reading** - Get unstuck when unable to start reading a document

### 5 Communication Resources

Background knowledge automatically loaded for the AI:

- **Message clarity patterns** - How to structure clear messages
- **Context interpretation** - Decoding vague phrases and implicit meaning
- **Tone calibration** - Professional levels and tone markers
- **Meeting structure** - How to prep, participate, and follow up
- **Document scaffolding** - Strategies for approaching complex documents

---

## Design Philosophy

This toolkit treats neurodivergent communication patterns as **different, not deficient**.

**Core principles:**

- **Bottom-up processing** - Start with details, build to summary
- **Explicit over implicit** - Make assumptions visible
- **Structure first** - Scaffolding before content
- **External working memory** - Toolkit holds context for you
- **Decision reduction** - Clear paths, fewer choices

**Designed for:** ADHD, autism, dyslexia, and executive function differences.

---

## Why MCP?

**Model Context Protocol (MCP)** is an open standard that makes these tools available across multiple AI systems:

- ✅ **Claude Desktop** (personal use)
- ✅ **Amazon Q CLI** (work environments)
- ✅ **Cursor** (coding with AI)
- ✅ **Any MCP-compatible system**

Write once, use everywhere. No platform lock-in.

---

## Installation

**Full guide:** [INSTALL.md](INSTALL.md)

**Requirements:**
- Python 3.10+
- Claude Desktop or Q CLI
- 5 minutes

**Quick install for Claude Desktop (macOS):**
```bash
# Install FastMCP
python3 -m pip install --user fastmcp

# Clone repo
git clone https://github.com/mogoldb/neurodivergent-comms-mcp.git
cd neurodivergent-comms-mcp

# Configure Claude Desktop
mkdir -p ~/Library/Application\ Support/Claude
cat > ~/Library/Application\ Support/Claude/claude_desktop_config.json << 'EOF'
{
  "mcpServers": {
    "neurodivergent-comms": {
      "command": "python3",
      "args": [
        "/FULL/PATH/TO/neurodivergent-comms-mcp/src/server.py"
      ]
    }
  }
}
EOF

# Update the path above, then restart Claude Desktop
```

---

## Usage Examples

**Full examples:** [EXAMPLES.md](EXAMPLES.md)

**Quick tests:**

1. **Check message:**
   ```
   Check this email: Hey team, just wanted to circle back...
   ```

2. **Decode message:**
   ```
   My manager said "when you get a chance" - what do they actually mean?
   ```

3. **Prep meeting:**
   ```
   Help me prep for Architecture Review. I'm the tech lead.
   ```

---

## Troubleshooting

### Server won't start

```bash
# Test manually
python3 /path/to/neurodivergent-comms-mcp/src/server.py

# Should start without errors (Ctrl+C to stop)
```

### Tools not showing up

1. Completely quit and restart Claude Desktop (Cmd+Q)
2. Check config file exists:
   ```bash
   cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```
3. Verify Python 3.10+: `python3 --version`

### Wrong Python version

Need 3.10+. Install from [python.org](https://www.python.org/downloads/)

**More help:** See [INSTALL.md](INSTALL.md) troubleshooting section.

---

## File Structure

```
neurodivergent-comms-mcp/
├── src/
│   ├── server.py              # Main MCP server (11 tools, 5 resources)
│   └── resources/             # Communication rule files
│       ├── message-clarity.md
│       ├── context-interpretation.md
│       ├── tone-calibration.md
│       ├── meeting-structure.md
│       └── document-scaffolding.md
├── INSTALL.md                 # Installation guide
├── EXAMPLES.md                # Real-world usage examples
├── README.md                  # This file
├── pyproject.toml            # Python package config
└── example-qcli-config.json  # Example Q CLI config
```

---

## Contributing

Found a communication pattern that would help? PRs welcome!

**Areas for contribution:**
- Additional communication scenarios
- More example prompts
- Platform-specific installation guides
- Bug fixes and improvements

---

## Roadmap

**v1.0 (Current):**
- ✅ 11 core communication tools
- ✅ 5 communication resource files
- ✅ Claude Desktop support
- ✅ Q CLI support

**Future:**
- [ ] Publish to PyPI (installable via `pip install neurodivergent-comms-mcp`)
- [ ] Add workplace-specific integrations (Slack, email, etc.)
- [ ] Conversation memory (remember your communication preferences)
- [ ] Additional tools based on user feedback
- [ ] Support for more MCP clients (Cursor, etc.)

---

## License

MIT License - Use however helps you best.

---

## Acknowledgments

Designed by and for neurodivergent professionals in technical workplaces.

Special thanks to:
- The MCP community for the protocol
- FastMCP for the Python framework
- Everyone who provided feedback on communication patterns

---

## Support

- **Installation help:** See [INSTALL.md](INSTALL.md)
- **Usage examples:** See [EXAMPLES.md](EXAMPLES.md)
- **Issues:** Open an issue on GitHub
- **Questions:** Discussions welcome!

**Remember:** You're not deficient. Your communication style is just different. This toolkit helps bridge that gap.
