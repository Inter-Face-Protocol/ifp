---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Evergreen Stage: a mature garden node that is well-linked, trustworthy, and stable across multiple editing sessions. Highest confidence for agent retrieval. Content has been validated through citation by other nodes, tested against sources, and requires no structural revision. Borrows from Matuschak's evergreen notes concept."
tagline: "Mature, well-linked, trustworthy — the highest confidence stage for retrieval"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Form Definitions](index.html)


- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)
- in_precinct::[\[\[Vault Precinct\]\]](../glosses/Vault%20Precinct.html)

# Evergreen Stage

An evergreen node is mature, well-linked, and trustworthy. The content has been validated through use — cited by other nodes, tested against sources, stable across multiple editing sessions. An agent encountering two nodes that answer the same question should prefer the evergreen one.

The term borrows from Andy Matuschak's "evergreen notes" concept but applies it within the deep context type system. Where Matuschak's evergreen notes are atomic and concept-oriented, deep context evergreen nodes carry structural contracts specific to their form type. A principle at evergreen stage has a tested maxim, clear scope, and documented exceptions. A model at evergreen stage has components validated against real cases.

## Characteristics

- All required sections substantive (no placeholders, no stubs)
- Rich bidirectional links — both outbound to related nodes and inbound citations from other nodes
- Content stable across multiple sessions without needing structural revision
- Sources verified and properly attributed
- Highest confidence for agent retrieval — first tier in the structural retrieval hierarchy

## Transitions

**Evergreen → Pruned**: When a node's domain shifts, its claims are superseded, or the topic is better covered by a different node. Evergreen nodes are not deleted — they transition to pruned with a `superseded_by::` predicate preserving the chain.

**Evergreen → Growing** (demotion): When new information invalidates part of the node's content, requiring significant revision rather than minor updates.

## Sources

Growth stage definitions from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), "Growth Stages as Lifecycle Metadata" section. Originally `status/evergreen` tag; migrated to `has_status::[\[\[Evergreen Stage\]\]](Evergreen%20Stage.html)` predicate per [\[\[Classification via Predicates Not Tags\]\]↑](../NODES.html#:~:text=Classification%20via%20Predicates%20Not%20Tags). Term inspired by Matuschak, Andy. "Evergreen notes." https://notes.andymatuschak.org/Evergreen_notes

## Relations

- relates_to::[\[\[Growing Stage\]\]](Growing%20Stage.html) — the previous stage in the growth progression
- relates_to::[\[\[Pruned Stage\]\]↑](../NODES.html#:~:text=Pruned%20Stage) — the end-of-life transition for superseded evergreen nodes
- relates_to::[\[\[Structural Retrieval Hierarchy\]\]↑](../NODES.html#:~:text=Structural%20Retrieval%20Hierarchy) — evergreen nodes rank highest in retrieval priority
