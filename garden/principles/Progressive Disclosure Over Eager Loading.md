---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Operating principle for the deep context graph: start with the question, load the most relevant nodes, follow edges on demand, stop when context is sufficient. Nothing requires loading the full graph. Mirrors the quad model in Claude Code (rules always, references on demand) and extends it across all form types."
tagline: "Start with the question, follow edges on demand, stop when context suffices"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Principles](index.html)


- is_a::[\[\[Principle Form\]\]](../forms/Principle%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Progressive Disclosure Over Eager Loading

## Claim

Nothing in the deep context architecture requires loading the full graph into context. The operating principle:

1. Start with the question or task
2. Load the most relevant form(s)
3. Follow edges as needed, loading connected forms on demand
4. Stop when context is sufficient to act or to identify a boundary

## Scope

Applies to any agent traversing a deep context graph — LLMs, scripts, and human readers. The principle operates at the semantic layer (agent traversal) and is enabled by summary fields at the authoring layer.

Summary fields are the mechanism: agents assess relevance via `brief_summary` without loading full documents. Status stages signal confidence. Domain pages provide entry points for topical exploration.

## Token Economics as Forcing Function

Wiki pages and garden notes have soft length constraints — usability degrades with bloat, but there is no hard limit. Agent context files compete for a finite context window with the actual work content. Every line of context has a quantifiable cost: tokens consumed that could serve the task at hand. This makes progressive disclosure not merely a best practice but a structural necessity for agent-facing content.

The forcing function has a constructive effect: it demands that knowledge systems develop the metadata infrastructure (summary fields, status stages, typed predicates) to support cheap relevance triage. Systems without this infrastructure must either load everything (filling the window with irrelevant content) or load nothing (losing accumulated knowledge). Progressive disclosure is the middle path, and token economics is what makes it load-bearing.

## Tensions

- **Comprehensiveness vs efficiency** — eager loading guarantees nothing is missed; progressive disclosure risks stopping too early. The architecture accepts this trade-off because context windows are finite and most questions don't require the full graph.
- **Discovery vs direction** — following edges on demand assumes the agent knows which edges matter. Undirected exploration (browsing) requires a different pattern. Domain pages partially address this by providing curated entry points.

## Sources

- [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), "Progressive Disclosure" section (lines 214-256)

## Relations

- extends::[\[\[Context Conservation Hierarchy\]\]↑](../NODES.html#:~:text=Context%20Conservation%20Hierarchy)
  - Progressive disclosure is the graph-level application of context conservation.

- relates_to::[\[\[Summary Fields as Load-Bearing Infrastructure\]\]↑](../NODES.html#:~:text=Summary%20Fields%20as%20Load-Bearing%20Infrastructure)
  - Summary fields are the mechanism that enables progressive disclosure.

- relates_to::[\[\[Structural Retrieval Hierarchy\]\]↑](../NODES.html#:~:text=Structural%20Retrieval%20Hierarchy)
  - The retrieval hierarchy implements progressive disclosure for agent search.

- relates_to::[\[\[Cross-Domain Document Lifecycle Parallels\]\]↑](../NODES.html#:~:text=Cross-Domain%20Document%20Lifecycle%20Parallels)
  - Token economics is the constraint that makes progressive disclosure structural rather than optional.

- relates_to::[\[\[One Context One Concern\]\]↑](../NODES.html#:~:text=One%20Context%20One%20Concern)
  - Progressive disclosure defines how to load incrementally; One Context One Concern defines the boundary of what constitutes a complete concern.
