# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup
uv venv && source .venv/bin/activate && uv pip install -e .

# Run MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx

# Add a dependency
uv add <package>
```

## Architecture

This is a **FastMCP server** — an MCP (Model Context Protocol) server that exposes tools to AI assistants like Claude Desktop.

- **`main.py`** — Entry point. Creates the `FastMCP` instance and registers tools via `mcp.tool()(fn)`, then calls `mcp.run()`.
- **`tools/`** — Each file defines plain Python functions that become MCP tools. Tools use `pydantic.Field` for parameter descriptions and follow a structured docstring pattern (summary, when-to-use, examples).
- **`tests/`** — pytest-based tests; `tests/fixtures/` holds DOCX and PDF files used in document conversion tests.

## Code Style

- Always apply appropriate type annotations to function arguments and return types.

## Adding a New Tool

1. Define a function in `tools/` using `pydantic.Field` for parameter metadata and a detailed docstring.
2. Register it in `main.py` with `mcp.tool()(your_function)`.

See `tools/math.py` for the canonical pattern. `tools/document.py` contains `binary_document_to_markdown` which is implemented but not yet registered.
