---
created: 2026-03-07
author: Christopher Allen
brief_summary: "The decision to capture personal reasoning as typed markdown forms connected by predicates — not as fine-tuned models, retrieval-augmented documents, or tagged notes. Typed forms with structural contracts make reasoning traversable by agents; predicates make it navigable; progressive disclosure makes it fit in context windows."
tagline: "Capture reasoning as typed forms with predicates — not fine-tuning, RAG, databases, or tags"
---

← [Garden Patch Home](../) · [Decisions](index.html)


- is_a::[\[\[Decision Form\]\]](../forms/Decision%20Form.html)
- has_status::[\[\[Growing Stage\]\]](../forms/Growing%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Deep Context as an Architecture for Captured Reasoning

## Context

Personal knowledge management systems capture facts and documents but not the reasoning substrate — the web of values, principles, patterns, and cases that lets a person (or an agent acting on their behalf) make decisions consistent with how they actually think. The gap: an agent with access to someone's notes can retrieve information but cannot reason as that person would, because the connective tissue between pieces of knowledge is implicit, unwritten, or scattered across unstructured prose.

Five requirements drove the architectural choice:

1. Knowledge captured in typed forms with known internal structure
2. Forms connected via explicit, traversable typed relations
3. Operation within small context windows using progressive disclosure
4. Distinction between what an agent may decide and what requires human judgment
5. Learning and expansion through use, with appropriate approval gates

## Decision

Capture reasoning as **typed markdown forms** connected by **predicate wikilinks** into a navigable knowledge graph. Each form type answers a distinct question and carries a structural contract — required sections that make its shape predictable for both human readers and agent traversal.

The architecture operates across three layers: authoring (plain markdown files), semantic (agent traversal via predicates), and trust (Gordian Envelope for signed exchange — future phase). The authoring layer is zero-dependency: no database, no plugin, no schema enforcement. Version control is git.

Sixteen form types organized in five categories (Orientation, Structural, Action, Generative, Governance) cover the full spectrum of reasoning from values and convictions through patterns and cases to inquiries and scenarios. Two precincts — garden (curated nodes) and vault (operational capture) — coexist in the same namespace with shared infrastructure.

## Alternatives Considered

**Fine-tuning / RLHF** — Train a model on the person's writing to replicate their voice and judgment. Rejected: captures behavioral patterns, not reasoning. A fine-tuned model can sound like the person without understanding why they make specific choices. The reasoning substrate is opaque inside model weights. No auditability, no progressive disclosure, no human override at decision boundaries.

**Retrieval-augmented generation (RAG) over documents** — Index existing documents and retrieve relevant chunks at query time. Rejected: retrieves but doesn't structure. RAG finds *what* someone wrote but not *how* pieces connect or *why* one principle takes priority over another. No typed relations, no structural contracts, no traversable graph. Works for information retrieval, not reasoning capture.

**Database-backed knowledge graph** — Store forms and relations in Neo4j, PostgreSQL, or similar. Rejected: violates zero-tooling floor. The knowledge becomes hostage to a running database. Plain text files in git survive any tool change; databases require maintenance, migration, and specific query languages. The authoring experience degrades when every edit requires a database write.

**Tags-only personal knowledge management** — Classify notes with YAML tags and retrieve by tag intersection. Rejected: produces sets, not graphs. Tags create flat groupings without typed edges. "Tagged with identity AND privacy" retrieves a set of notes but says nothing about *how* identity and privacy relate — whether they're in tension, whether one constrains the other, whether a specific case validates their intersection. Predicates carry semantic meaning that tags cannot.

**Hybrid structured/unstructured** — Keep most content as unstructured notes with a small structured layer (e.g., databases for key entities). Rejected: the boundary between structured and unstructured becomes the maintenance problem. Which knowledge deserves structure? The deep context approach answers this with the standalone document test — if it produces a standalone document with a known internal structure, it's a form.

## Consequences

**Positive — observed through implementation:**

- 87+ nodes across 13 of 16 form types validate that the taxonomy covers real knowledge
- Two values, two convictions, and six principles capture reasoning that no other system could represent as navigable structure
- Hybrid bootstrapping proved viable at scale (913 files → 4,294 predicates → 50 maps of content → 87+ garden nodes)
- Progressive disclosure works in practice — agents load nodes on demand via summary fields and predicate traversal
- The zero-tooling floor holds — shell one-liners serve as the query layer, no specialized tools required

**Positive — external validation:**

- Multiple agent memory systems (ClawVault, QMD, MIE) have independently converged on plain markdown + YAML frontmatter + typed metadata as the storage format for agent knowledge — benchmarks show this outperforms purpose-built infrastructure
- [\[\[Chatlatanagulchai (2025) Agent READMEs\]\]↑](../NODES.html#:~:text=Chatlatanagulchai%20%282025%29%20Agent%20READMEs) finds that context files "behave more like dynamic configurations than static text," validating the architecture's treatment of living documents as first-class engineering artifacts

**Positive — architectural:**

- Nodes are independently valuable — each stands alone as a readable document
- The predicate grammar enables typed traversal without schema enforcement
- Growth stages (seed → growing → evergreen → pruned) signal confidence without requiring formal review
- Two precincts (garden/vault) allow curated and operational content to coexist without forcing structure on everything

**Negative — observed:**

- Authoring effort is higher than unstructured notes — writing a conviction with grounding and implications takes more work than capturing a thought
- The predicate vocabulary lacks enforcement — consistency depends on author discipline
- 3 form types remain uninstantiated (Protocol, Skill, Scenario) — either the types are premature or the garden hasn't reached the use cases that produce them
- Ghost links accumulate as nodes reference concepts not yet written — manageable but requires periodic tending

## Sources

- Allen, Christopher. "The Path to Self-Sovereign Identity," 2016 — values-to-principles chain as exemplar
- Alexander, Christopher. *A Pattern Language*. Oxford University Press, 1977 — Alexandrian pattern form as structural template
- Matuschak, Andy. "Taxonomy of note types" — note type spectrum as input to form taxonomy

## Relations

- grounded_in::[\[\[Reasoning Fidelity\]\]](../values/Reasoning%20Fidelity.html)
  - The architecture exists to serve this value — capturing how someone reasons, not just what they know.

- grounded_in::[\[\[Knowledge Durability\]\]](../values/Knowledge%20Durability.html)
  - Plain markdown, git, zero-tooling floor — all serve the value that knowledge outlasts tools.

- grounded_in::[\[\[Values Precede Technical Decisions\]\]](../convictions/Values%20Precede%20Technical%20Decisions.html)
  - The architecture derives from values; the decision to use typed forms follows from what matters, not what's technically convenient.

- implements::[\[\[Standalone Document Test for Form Candidacy\]\]↑](../NODES.html#:~:text=Standalone%20Document%20Test%20for%20Form%20Candidacy)
  - The test that determines what qualifies as a form type — the taxonomic foundation.

- extends::[\[\[Typed Relations as Simple Graphs in Plain Markdown\]\]↑](../NODES.html#:~:text=Typed%20Relations%20as%20Simple%20Graphs%20in%20Plain%20Markdown)
  - The predicate grammar uses the `predicate::[\[\[target\]\]↑](../NODES.html#:~:text=target)` convention as its graph substrate.

- validated_by::[\[\[Hybrid Bootstrapping for Garden Migration\]\]↑](../NODES.html#:~:text=Hybrid%20Bootstrapping%20for%20Garden%20Migration)
  - The first garden bootstrap proved the architecture works at vault scale.

- relates_to::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
  - This decision is the founding architectural choice for the domain.

- relates_to::[\[\[Captured Reasoning Exchange Pipeline\]\]↑](../NODES.html#:~:text=Captured%20Reasoning%20Exchange%20Pipeline)
  - The three-layer model (authoring, semantic, trust) implements this decision.

- relates_to::[\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html)
  - Decision boundaries operationalize requirement #4 (distinguishing agent vs. human authority).
