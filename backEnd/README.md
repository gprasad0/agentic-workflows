# Agentic Outreach Architecture

An end-to-end architecture for an **AI-powered Agentic Outreach System** that researches prospects, generates personalized outreach, and executes campaigns with a **human-in-the-loop** approval workflow.

The system combines **LangGraph**, **FastAPI**, **LLMs**, **Retrieval-Augmented Generation (RAG)**, and the **Model Context Protocol (MCP)** to build secure, scalable, and extensible AI agents.

---

## 🌟 Overview

This repository contains:

- 📐 System architecture documentation
- 🖥️ Interactive architecture visualization
- 🧠 AI agent workflow design
- 🔌 MCP-based tool integration architecture

The architecture demonstrates how an AI agent can:

- Research prospects
- Retrieve contextual information
- Generate personalized outreach
- Execute external actions
- Keep humans in control before final execution

---

# 🏗️ System Architecture

The architecture consists of seven major components.

---

## 1. Next.js Dashboard (Frontend)

**Role**

Acts as the control center for users.

**Responsibilities**

- Start outreach campaigns
- View campaign progress
- Review discovered leads
- Approve AI-generated outreach
- Monitor agent execution in real time

---

## 2. FastAPI Backend (API Gateway)

**Role**

Acts as the bridge between the frontend and the AI orchestration layer.

**Responsibilities**

- Authentication
- Request routing
- WebSocket communication
- Session management
- API endpoints
- Communication with LangGraph

---

## 3. LangGraph Orchestrator

**Role**

The central state machine controlling the AI workflow.

**Responsibilities**

- Workflow orchestration
- State persistence
- Conditional branching
- Retry logic
- Human approval checkpoints
- Agent execution flow

Example workflow:

```
Receive Request
      │
      ▼
Research Prospect
      │
      ▼
Retrieve Context
      │
      ▼
Generate Outreach
      │
      ▼
Human Approval
      │
      ▼
Send Email
```

---

## 4. LLM Engine

**Role**

The reasoning layer of the application.

Possible providers include:

- OpenAI GPT-4o
- Gemini
- Claude

**Responsibilities**

- Intent classification
- Prospect research summarization
- Email generation
- Personalization
- Decision making
- Tool selection

---

## 5. Vector Database / RAG

**Role**

Provides long-term memory and contextual grounding.

Possible databases:

- ChromaDB
- Pinecone
- Weaviate
- Qdrant

**Stores**

- Previous conversations
- Company knowledge
- Brand guidelines
- Sales documentation
- Product documentation
- Outreach history

This allows the LLM to generate grounded, context-aware responses.

---

## 6. MCP Server (Model Context Protocol)

**Role**

Secure gateway between the LLM and external tools.

Instead of giving the LLM direct access to external services, all interactions happen through the MCP Server.

This provides:

- Security
- Standardization
- Tool abstraction
- Easy extensibility

Example tools:

- Local file system
- CRM
- Databases
- Browsers
- Web search
- Internal APIs

---

## 7. External APIs

External services are accessed only through the MCP Server.

Examples include:

- Apollo
- LinkedIn research tools
- Instantly.ai
- SendGrid
- HubSpot
- Salesforce
- Google Search
- Internal company APIs

---

# 🔄 Workflow

The complete system flow is shown below.

```text
User
 │
 ▼
Next.js Dashboard
 │
 ▼
FastAPI Backend
 │
 ▼
LangGraph Orchestrator
 │
 ├─────────────► Vector Database
 │                     ▲
 │                     │
 ▼                     │
LLM Engine─────────────┘
 │
 ▼
MCP Server
 │
 ▼
External APIs
 │
 ▼
Results
 │
 ▼
Dashboard Approval
 │
 ▼
Final Execution
```

---

# 🧠 Human-in-the-Loop

A key design principle is that AI never performs irreversible actions without approval.

Examples include:

- Sending emails
- Launching campaigns
- Updating CRM records
- Triggering workflows

Users can:

- Review generated content
- Edit responses
- Reject outputs
- Approve execution

This ensures reliability and trust.

---

# 🔌 Why MCP?

The Model Context Protocol (MCP) standardizes how LLMs interact with external tools.

Benefits include:

- Tool interoperability
- Secure execution
- Easier maintenance
- Reusable integrations
- Vendor independence

Instead of writing custom integrations for every model, the LLM communicates through a common protocol.

---

# 📦 Technology Stack

| Layer            | Technology               |
| ---------------- | ------------------------ |
| Frontend         | Next.js                  |
| Backend          | FastAPI                  |
| Agent Framework  | LangGraph                |
| LLM              | GPT-4o / Gemini / Claude |
| Memory           | ChromaDB / Pinecone      |
| Tool Integration | MCP                      |
| Visualization    | Mermaid.js               |

---

# 📂 Repository Structure

```
.
├── index.html
├── README.md
├── assets/
│   ├── css/
│   ├── js/
│   └── images/
└── architecture/
```

---

# 🚀 Interactive Architecture

The repository includes an interactive architecture visualization powered by **Mermaid.js**.

Features include:

- Interactive node selection
- Component inspector
- Architecture exploration
- Expandable descriptions
- Visual workflow understanding

---

# ▶️ Running the Visualization

Simply open:

```
index.html
```

in any modern web browser.

No build process is required.

---

# 🖱️ Using the Interactive Diagram

Click on any architecture component to view additional information.

Examples:

- Next.js Dashboard
- FastAPI Backend
- LangGraph Orchestrator
- LLM Engine
- Vector Database
- MCP Server
- External APIs

The inspector panel updates dynamically with the selected component's:

- Purpose
- Responsibilities
- Relationships
- Position in the workflow

---

# 🎯 Design Goals

- Modular architecture
- Secure tool execution
- Human oversight
- Extensible integrations
- Provider-agnostic LLM support
- Scalable agent workflows
- Context-aware reasoning

---

# 🔮 Future Enhancements

Potential additions include:

- Multi-agent collaboration
- Calendar integrations
- CRM synchronization
- Slack notifications
- Agent memory persistence
- Workflow analytics
- Autonomous campaign optimization
- Multi-channel outreach (Email, LinkedIn, WhatsApp)

---

# 📜 License

This project is intended as an architectural reference and visualization for building modern AI agent systems.
