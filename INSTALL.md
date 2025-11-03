# Installation Guide

Get the Neurodivergent Communications MCP server running on your computer.

---

## Prerequisites

- **Python 3.10+** (required for FastMCP)
- **Claude Desktop** OR **Q CLI** (Amazon's Q Developer CLI)
- 5 minutes

---

## Quick Install

### For Claude Desktop (Personal Computer)

#### 1. Check Python Version

```bash
python3 --version
```

Need Python 3.10+? Install from [python.org](https://www.python.org/downloads/)

Or check if you already have it:
```bash
which python3.10 python3.11 python3.12
```

#### 2. Install FastMCP

```bash
# If you have python3.10+
python3 -m pip install --user fastmcp

# Or if you found a specific version like python3.10
/usr/local/bin/python3.10 -m pip install --user fastmcp
```

#### 3. Download/Clone This Repository

```bash
cd ~/Desktop
# If you have git:
git clone https://github.com/YOUR_USERNAME/neurodivergent-comms-mcp.git

# Or download and extract the ZIP
```

#### 4. Configure Claude Desktop

Create/edit the config file:

**macOS:**
```bash
# Create directory if needed
mkdir -p ~/Library/Application\ Support/Claude

# Edit the config (use your preferred editor)
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Windows:**
```bash
# Create directory
mkdir %APPDATA%\Claude

# Edit the config
notepad %APPDATA%\Claude\claude_desktop_config.json
```

**Paste this config** (update the path to where you put the files):

```json
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
```

**Important:** Replace `/FULL/PATH/TO/` with your actual path!

Example:
- macOS: `/Users/yourname/Desktop/neurodivergent-comms-mcp/src/server.py`
- Windows: `C:\\Users\\yourname\\Desktop\\neurodivergent-comms-mcp\\src\\server.py`

If you have Python 3.10 specifically, use the full path:
```json
"command": "/usr/local/bin/python3.10",
```

#### 5. Restart Claude Desktop

**Completely quit** (not just close window):
- macOS: `Cmd+Q`
- Windows: Right-click system tray → Quit

Then reopen Claude Desktop.

#### 6. Test It!

In a new Claude chat, try:
```
Can you check this message: Hey team, thoughts on approach B?
```

Claude should call the `check_message` tool and analyze it!

See `EXAMPLES.md` for real-world usage examples.

---

### For Q CLI (Work Computer - Amazon)

#### 1. Check Python

```bash
python3 --version  # Need 3.10+
```

#### 2. Install FastMCP

```bash
python3 -m pip install --user fastmcp
```

#### 3. Download This Repository

```bash
cd ~/
git clone https://github.com/YOUR_USERNAME/neurodivergent-comms-mcp.git
```

#### 4. Configure Q CLI

Edit the example config:

```bash
cd neurodivergent-comms-mcp
cp example-qcli-config.json my-comms-agent.json

# Edit to update the path
nano my-comms-agent.json
```

Update this line to your actual path:
```json
"args": ["/Users/yourname/neurodivergent-comms-mcp/src/server.py"]
```

#### 5. Install to Q CLI

```bash
# Symlink your config
ln -sf ~/neurodivergent-comms-mcp/my-comms-agent.json ~/.aws/amazonq/cli-agents/comms.json
```

#### 6. Test It!

```bash
q chat --agent comms
```

Then try:
```
Check this email: Hey team, any thoughts on the API approach?
```

---

## Troubleshooting

### "FastMCP not found" or Import Errors

**Solution:** Make sure you installed with the Python version you're using:

```bash
# If using python3.10 specifically
/usr/local/bin/python3.10 -m pip install --user fastmcp

# Then update your config to use that exact python
"command": "/usr/local/bin/python3.10"
```

### "Server won't start" or "Connection failed"

**Test the server manually:**
```bash
python3 /path/to/neurodivergent-comms-mcp/src/server.py
```

Should start without errors. Press `Ctrl+C` to stop.

**Check for errors:**
- Wrong Python version (need 3.10+)
- Wrong path in config file
- FastMCP not installed for that Python version

### "Tools not showing up"

1. **Completely quit and restart** Claude Desktop or Q CLI
2. **Check config file exists:**
   ```bash
   # Claude Desktop (macOS)
   cat ~/Library/Application\ Support/Claude/claude_desktop_config.json

   # Q CLI
   cat ~/.aws/amazonq/cli-agents/comms.json
   ```
3. **Check paths are absolute** (not relative like `./src/server.py`)

### "Permission denied"

Make the script executable:
```bash
chmod +x /path/to/neurodivergent-comms-mcp/src/server.py
```

### Python 3.9 or older?

You need to upgrade to Python 3.10+:
- **macOS:** `brew install python@3.10` or download from python.org
- **Windows:** Download from python.org
- **Linux:** `sudo apt install python3.10` or `sudo yum install python3.10`

---

## Verify Installation

### Check Server Runs
```bash
python3 /path/to/neurodivergent-comms-mcp/src/server.py
```
Should start and wait (no errors). Press `Ctrl+C` to stop.

### Check FastMCP Installed
```bash
python3 -c "import mcp.server.fastmcp; print('✓ FastMCP OK')"
```
Should print: `✓ FastMCP OK`

### Check Config File
```bash
# Claude Desktop (macOS)
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Q CLI
cat ~/.aws/amazonq/cli-agents/comms.json
```
Should show your MCP server configuration.

---

## What's Installed?

After successful installation, you have:

**11 Communication Tools:**
1. check_message - Analyze drafts
2. decode_message - Decode vague messages
3. prep_meeting - Meeting preparation
4. scaffold_document - Preview doc structure
5. check_tone - Tone validation
6. call_or_text - Recommend communication method
7. synthesize_thoughts - Organize brain dumps
8. catch_up_thread - Summarize email threads
9. summarize_meeting - Extract decisions/actions
10. ask_clarity - Draft clarity requests
11. unstuck_reading - Get unstuck on documents

**5 Communication Resources** (loaded automatically as background knowledge):
- Message clarity patterns
- Context interpretation guidelines
- Tone calibration rules
- Meeting structure guide
- Document scaffolding framework

---

## Uninstalling

### Claude Desktop
```bash
# macOS
rm ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Windows
del %APPDATA%\Claude\claude_desktop_config.json
```

### Q CLI
```bash
rm ~/.aws/amazonq/cli-agents/comms.json
```

Then delete the repository folder if you want.

---

## Getting Help

**Issues?** Check `EXAMPLES.md` for usage examples.

**Still stuck?** Open an issue on GitHub with:
- Your OS and Python version
- Error messages
- What you tried
