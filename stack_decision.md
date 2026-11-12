# Stack decision

## Decision

**Primary stack: n8n.**

LangGraph is secondary for a later version, not the MVP implementation.

## Why n8n fits this problem

Competitive intelligence for mobile game product managers follows a predictable, repeatable data-gathering pattern: web search, news headlines, App Store telemetry, internal strategy retrieval, synthesis, and delivery. n8n fits that pattern because it integrates REST APIs, Pinecone retrieval, and Gmail/Slack-style delivery through visual nodes with little boilerplate code. Its node-level retries and visual routing make third-party rate limits, timeouts, and partial source failures visible and manageable. The workflow can therefore be maintained by Product Ops or Marketing teams without requiring a dedicated backend engineer for every change. LangGraph remains a good future option for branching, stateful research, or more complex agent loops, but custom Python state machines would add setup and maintenance overhead to this sequential gather-and-synthesize MVP.

## Fit with the implemented workflow

The exported workflow already provides the stack decision in executable form:

- Form input accepts a competitor name, recipient email, and optional strategy PDF.
- Three HTTP Request nodes run the Tavily, GNews, and Apple iTunes research calls in parallel.
- Set/Merge/If nodes normalize and gate the data.
- An OpenAI-backed AI Agent uses Pinecone as a strategy/KPI retrieval tool.
- Markdown is converted to HTML and delivered by Gmail.
- The three HTTP nodes have retry-on-failure enabled; an explicit no-data branch stops the run with a readable error.

This is the right level of orchestration for the MVP: observable, importable, and editable in the same environment where the target Product Ops user would maintain it.

## Boundary for a future LangGraph migration

Revisit LangGraph when the product needs multi-step source disagreement resolution, long-running research state, human approval checkpoints, provider-specific tool policies, or durable per-studio memory. None of those is required to demonstrate the current trigger → research → structured report flow.
