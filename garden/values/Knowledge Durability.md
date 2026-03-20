---
created: 2026-03-07
author: Christopher Allen
brief_summary: "The value that knowledge should survive changes in tools, platforms, and formats. A garden's reasoning substrate must outlast the software used to tend it — plain markdown over proprietary formats, git over cloud sync, zero-tooling floors over feature-rich dependencies."
tagline: "Knowledge should outlast the tools used to capture it — plain text, open formats, zero dependencies"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Values](index.html)


- is_a::[\[\[Value Form\]\]](../forms/Value%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Knowledge Durability

## The Value

Knowledge should survive changes in tools, platforms, and formats. A person's reasoning substrate — accumulated over decades — must not be held hostage by the software used to tend it, the platform used to host it, or the encoding used to store it.

This value runs deeper than a preference for open formats. It is an assertion about the temporal relationship between knowledge and infrastructure: knowledge outlives infrastructure, always. Obsidian may disappear. Git hosting may change. Markdown conventions may evolve. The reasoning captured in a garden should survive all of these transitions because the knowledge is more valuable than any single tool used to work with it.

## Scope

Knowledge durability applies to the authoring layer of the deep context architecture — the files, formats, and conventions used to capture reasoning. It does not prohibit tooling (Obsidian plugins, shell scripts, AI agents are all used). It requires that no tooling become a single point of failure for accessing the knowledge.

The value produces specific technical constraints: plain markdown over proprietary formats, file-per-form over database records, predicates as text over plugin-dependent metadata, git for version control over platform-specific sync.

## Tensions

- **Durability vs. capability**: Rich tooling (databases, graph engines, specialized editors) enables features that plain markdown cannot match. Knowledge durability accepts this trade-off — features that require specific tools are conveniences, not infrastructure. The zero-tooling floor holds even when tools add value on top.
- **Durability vs. collaboration**: Multi-user systems often require shared infrastructure (servers, real-time sync, access control) that creates platform dependencies. The deep context architecture addresses this through the trust layer (Gordian Envelope) rather than through shared infrastructure.
- **Durability vs. performance**: Text files in folders are slower to query than databases. Shell one-liners replace indexed queries. Knowledge durability accepts slower queries in exchange for format independence.

## Sources

- [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html) — the authoring layer's zero-dependency design and the three-layer architecture both serve durability
- The zero-tooling floor principle derives directly from this value

## Relations

- generates::[\[\[Zero-Tooling Floor for Knowledge Architecture\]\]](../principles/Zero-Tooling%20Floor%20for%20Knowledge%20Architecture.html)
  - The principle that the architecture must work without any specific tool is a direct expression of knowledge durability.

- generates::[\[\[Content Over Container\]\]](../principles/Content%20Over%20Container.html)
  - Content over container follows from durability: if the container (tool, platform, format) is impermanent, then the content must be portable.

- generates::[\[\[Predicate Maintenance Recipes Over Tools\]\]↑](../NODES.html#:~:text=Predicate%20Maintenance%20Recipes%20Over%20Tools)
  - Preferring shell one-liners over dedicated graph tools keeps maintenance durable.

- relates_to::[\[\[Reasoning Fidelity\]\]](Reasoning%20Fidelity.html)
  - Reasoning captured in a format that doesn't survive tool changes loses its fidelity over time. Durability is a precondition for long-term fidelity.

- relates_to::[\[\[Captured Reasoning Exchange Pipeline\]\]↑](../NODES.html#:~:text=Captured%20Reasoning%20Exchange%20Pipeline)
  - The three-layer pipeline (markdown → semantic → trust) preserves durability at the authoring layer while adding capabilities in higher layers.
