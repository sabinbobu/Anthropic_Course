# Anthropic Course — Building with the Claude API

A complete hands-on course covering everything needed to build production-grade AI applications with Claude. Each module combines theory, Jupyter notebooks with exercises, and real projects.

---

## Course Structure

```
building-with-the-claude-api/
├── Accessing_Claude_with_the_API/
├── Prompt_Engineering/
├── Prompt_Evaluation/
├── Features_of_Claude/
├── Tool_use_with_Claude/
├── Retrieval_Augmented_Generation/
└── Model_Context_Protocol/
```

---

## Modules

### 1. Accessing Claude with the API
> Foundations of communicating with Claude programmatically.

- Making basic API requests with the Anthropic SDK
- Writing effective system prompts
- Streaming responses in real time
- Controlling output format, length, and stop sequences

---

### 2. Prompt Engineering
> Writing prompts that reliably produce the results you need.

- Core prompting principles (clarity, context, constraints)
- Few-shot and chain-of-thought techniques
- Role prompting and persona assignment
- Structured output formatting
- Hands-on exercises with before/after prompt comparisons

---

### 3. Prompt Evaluation
> Measuring and improving prompt quality systematically.

- Building automated eval pipelines
- Model-graded evaluation (using Claude to grade Claude)
- Code-based graders with deterministic assertions
- Tracking prompt quality across iterations

---

### 4. Features of Claude
> Leveraging Claude's advanced built-in capabilities.

- **Extended Thinking** — enabling deeper multi-step reasoning
- **Vision** — processing images and PDFs with citations
- **Prompt Caching** — reducing latency and cost on repeated context
- **Code Execution** — running Python in a sandbox and interpreting results

---

### 5. Tool Use with Claude
> Giving Claude the ability to take actions and call external systems.

- Defining tools with JSON schema and registering them with the API
- Agentic loop — handling `tool_use` stop reasons and feeding results back
- Structured data extraction using tools as a typed schema
- Streaming tool calls in real time
- Built-in tools: Text Editor and Web Search
- End-to-end examples: unit conversion, web research

---

### 6. Retrieval-Augmented Generation (RAG)
> Building knowledge-grounded Claude applications.

- **Chunking** strategies (fixed-size, sentence, semantic)
- **Embeddings** — generating and storing vector representations
- **Vector databases** — similarity search with ChromaDB / FAISS
- **BM25** — keyword-based sparse retrieval
- **Hybrid search** — combining dense + sparse retrieval
- **Reranking** — cross-encoder reranking for precision
- **Contextual retrieval** — prepending chunk-level context before embedding

---

### 7. Model Context Protocol (MCP)
> Standardizing how Claude connects to tools, data, and workflows.

- MCP architecture — servers, clients, and the stdio transport
- Defining **tools** (`@mcp.tool`) for Claude to invoke
- Defining **resources** (`@mcp.resource`) for dynamic data access
- Defining **prompts** (`@mcp.prompt`) for reusable workflow templates
- Using the MCP Inspector to debug server implementations
- Building a full **CLI chat app** with document retrieval (`@mention`), slash-command prompts (`/command`), multi-client fan-out, and `prompt_toolkit` auto-completion

---

## Key Skills Gained

| Area | Skills |
|------|--------|
| API & SDK | Requests, streaming, system prompts, output control |
| Prompt craft | Few-shot, CoT, role prompting, structured output |
| Evaluation | Automated evals, model graders, code graders |
| Claude features | Extended thinking, vision, caching, code execution |
| Tool use | Tool definitions, agentic loops, structured extraction, streaming |
| RAG | Chunking, embeddings, vector DBs, hybrid search, reranking |
| MCP | Server/client architecture, tools, resources, prompts, CLI projects |

---

## Tech Stack

- **Language**: Python 3.10+
- **AI**: [Anthropic SDK](https://github.com/anthropics/anthropic-sdk-python) (`anthropic`)
- **MCP**: `mcp[cli]`
- **RAG**: `chromadb`, `sentence-transformers`, `rank-bm25`
- **CLI**: `prompt-toolkit`
- **Notebooks**: Jupyter
- **Package manager**: `uv`

## Setup

```bash
# Clone the repo
git clone <repo-url>
cd Anthropic_Course

# Create a virtual environment
uv venv && source .venv/bin/activate

# Install dependencies per module (see each module's pyproject.toml or notebook)

# Set your API key
export ANTHROPIC_API_KEY="sk-..."
```
