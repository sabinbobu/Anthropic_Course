# Model Context Protocol (MCP)

A hands-on module covering the full MCP lifecycle — from protocol fundamentals to building a production-ready CLI chat application backed by an MCP server and client.

---

## Topics Covered

| # | Topic | Key Takeaways |
|---|-------|---------------|
| 1 | **Introducing MCP** | What MCP is, why it exists, and how it standardizes AI tool integrations |
| 2 | **MCP Clients** | Role of the client in the MCP architecture; connecting to servers over stdio/SSE |
| 3 | **Project Setup** | Bootstrapping a Python project with `uv`, configuring `.env`, and managing dependencies (`anthropic`, `mcp[cli]`, `prompt-toolkit`) |
| 4 | **Defining Tools with MCP** | Declaring tools on the server with `@mcp.tool`, JSON schema inputs, and surfacing them to Claude |
| 5 | **The Server Inspector** | Using the MCP inspector to interactively test and debug tool definitions before wiring a client |
| 6 | **Implementing a Client** | Building `MCPClient` to connect via `stdio`, list tools, and invoke `call_tool` asynchronously |
| 7 | **Defining Resources** | Exposing document content through `@mcp.resource` with custom URI schemes (`docs://documents/{id}`) |
| 8 | **Accessing Resources** | Reading resources in the client with `read_resource()` and injecting content into Claude's context via `<document>` tags |
| 9 | **Defining Prompts** | Creating reusable prompt templates on the server with `@mcp.prompt` and parameterised arguments |
| 10 | **Prompts in the Client** | Fetching prompt templates with `get_prompt()`, converting `PromptMessage` → `MessageParam`, and routing `/commands` in the CLI |
| 11 | **MCP Review** | End-to-end review of the server ↔ client ↔ Claude message loop and multi-client fan-out pattern |
| 12 | **Quiz** | Knowledge check on all MCP concepts above |

---

## Project: `cli_project`

A fully working CLI chat app that demonstrates every MCP concept in practice.

```
cli_project/
├── main.py              # Entry point — wires MCP clients, Claude service, and CLI together
├── mcp_server.py        # MCP server — exposes tools, resources, and prompt templates
├── mcp_client.py        # MCP client wrapper — list_tools, call_tool, read_resource, get_prompt
├── core/
│   ├── claude.py        # Thin Anthropic SDK wrapper (chat, message helpers)
│   ├── chat.py          # Agentic loop — sends messages, handles tool_use stop reason
│   ├── cli_chat.py      # CliChat — adds resource injection (@mentions) and /command routing
│   └── cli.py           # CliApp — prompt_toolkit UI with tab-completion and auto-suggest
└── pyproject.toml       # Dependencies: anthropic, mcp[cli], prompt-toolkit, python-dotenv
```

### Architecture Overview

```
User input (CLI)
      │
      ▼
  CliApp (prompt_toolkit)
      │  /command or @mention or plain query
      ▼
  CliChat._process_query()
      │  injects resource content / converts prompt templates
      ▼
  Chat.run()  ──── agentic loop ────────────────────────────┐
      │                                                       │
      ▼                                                       │
  Claude API  ──► stop_reason=tool_use                       │
      │                ▼                                      │
      │         ToolManager.execute_tool_requests()           │
      │                ▼                                      │
      │         MCPClient.call_tool()  (via stdio)            │
      │                ▼                                      │
      │         MCP Server (tools / resources / prompts)      │
      │                │                                      │
      └────────────────┘  (tool results fed back) ───────────┘
      │
      ▼  stop_reason=end_turn
  Final response printed to user
```

### Key MCP Features Demonstrated

- **Tools** — Claude can invoke server-side functions (e.g. search, computation) and receive structured results
- **Resources** — Documents are served under a `docs://` URI scheme; users reference them with `@doc-id` in the CLI
- **Prompts** — Reusable prompt templates are fetched from the server; users invoke them with `/command doc-id`
- **Multi-client** — Additional MCP servers can be passed as CLI arguments and their tools are merged transparently
- **Auto-completion** — `prompt_toolkit` provides tab-completion for `/commands` and `@resource` mentions

### Running the Project

```bash
# Install dependencies
uv venv && source .venv/bin/activate
uv pip install -e .

# Set environment variables
echo 'ANTHROPIC_API_KEY="sk-..."' >> .env
echo 'CLAUDE_MODEL="claude-sonnet-4-6"' >> .env

# Run
uv run main.py

# Optionally pass additional MCP server scripts
uv run main.py extra_server.py
```

### Example Interactions

```
> What is the capital of France?          # plain chat
> Tell me about @deposition.md            # resource mention
> /summarize deposition.md               # prompt command
```

---

## Key Concepts Summary

| Concept | MCP Primitive | How it's used here |
|---------|---------------|--------------------|
| Callable functions | `@mcp.tool` | Claude invokes tools autonomously in the agentic loop |
| External data | `@mcp.resource` | Documents injected into context via `@mention` |
| Reusable workflows | `@mcp.prompt` | Slash-command templates fetched and executed client-side |
| Transport | `stdio` | Server launched as subprocess; communication over stdin/stdout |
| Discovery | `list_tools` / `list_resources` / `list_prompts` | Client fetches capabilities at startup |
