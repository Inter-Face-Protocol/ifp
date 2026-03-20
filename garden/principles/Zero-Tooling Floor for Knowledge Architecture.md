---
created: 2026-03-06
author: Christopher Allen
brief_summary: "The deep context architecture preserves a zero-tooling floor: plain markdown, YAML frontmatter, predicate wikilinks, and git. No database, plugin, or schema enforcement required at the authoring or semantic layers. Shell one-liners serve as the query layer. Specialized tools add value but are never prerequisites."
tagline: "Plain markdown, git, and shell one-liners — specialized tools add value but are never prerequisites"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Principles](index.html)


- is_a::[\[\[Principle Form\]\]](../forms/Principle%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Zero-Tooling Floor for Knowledge Architecture

## Claim

The authoring and semantic layers of the deep context architecture operate without specialized tooling. Forms are plain markdown with YAML frontmatter and `predicate::[\[\[target\]\]↑](../NODES.html#:~:text=target)` typed relations. Version control is git. The query layer is shell one-liners (`rg 'predicate::\[\[Target\]\]' --type md`). A dedicated graph-traversal skill could add value but is not required.

## Scope

Applies to the authoring layer (human-facing) and semantic layer (agent-facing). The trust layer (Gordian Envelope) adds tooling requirements but is explicitly separate — the architecture works without it.

The zero-tooling floor means:

- No database
- No plugin dependency for core operations
- No schema enforcement beyond file conventions
- No build step between authoring and querying

The zero-tooling floor is also a portability guarantee. If the current tool (Obsidian, Claude Code, any future replacement) disappears tomorrow, the knowledge survives intact — readable, searchable, and structurally coherent with nothing more than a text editor and `grep`. No migration, no export, no data rescue. The choice of plain markdown over richer formats is a values decision: portability over power.

## External Convergence

Multiple agent memory systems have independently converged on plain markdown files with YAML frontmatter as their storage format — validating the zero-tooling choice from a different direction:

- **ClawVault** — 8 typed memory categories as YAML `memoryType:` field, wiki-links for connections, folder hierarchy for organization. Benchmarks show this format outperforms purpose-built memory infrastructure (74% vs 68.5% on the LoCoMo long-context memory benchmark).
- **QMD** — Local markdown search engine achieving 96% token reduction by returning snippets rather than full documents. The architecture's summary-first retrieval pattern, independently discovered.
- **MIE** — Cross-agent knowledge graph with typed nodes and relationships stored in markdown. 12 MCP tools for query/store/analyze across multiple simultaneous agent connections.

The convergence suggests that plain markdown with typed metadata is not merely a viable choice but the emerging default for agent-facing knowledge systems. The zero-tooling floor is also the interoperability floor — any system that can read files can participate.

## Tensions

- **Power vs accessibility** — specialized tools (Dataview, graph databases, custom indexers) enable queries that shell one-liners cannot express. The principle doesn't reject tools; it ensures the architecture isn't hostage to them.
- **Enforcement vs convention** — without schema enforcement, structural contracts are conventions that can be violated. Path-based Claude rules provide soft enforcement during authoring, but nothing prevents manual edits from breaking contracts.

## Sources

- [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), "Authoring Layer" and "Semantic Layer" sections (lines 244-256)
- [\[\[The Gardening Problem Returns - Document Lifecycle in the Age of AI Agents\]\]↑](../NODES.html#:~:text=The%20Gardening%20Problem%20Returns%20-%20Document%20Lifecycle%20in%20the%20Age%20of%20AI%20Agents), Section 1.3 — ClawVault, QMD, and MIE as independent convergence on markdown+YAML for agent memory

## Relations

- relates_to::[\[\[Predicate Maintenance Recipes Over Tools\]\]↑](../NODES.html#:~:text=Predicate%20Maintenance%20Recipes%20Over%20Tools)
  - Maintenance recipes demonstrate the zero-tooling floor in practice.

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](Human%20Authority%20Over%20Augmentation%20Systems.html)
  - Zero-tooling preserves human authority by avoiding tool lock-in.

- relates_to::[\[\[Content Over Container\]\]](Content%20Over%20Container.html)
  - Both principles favor portable content over infrastructure dependency.
