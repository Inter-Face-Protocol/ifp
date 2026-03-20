---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Seed Stage, the entry point for all garden nodes: raw capture with low confidence, unprocessed structure, and minimal links. Seeds are extraction products that have enough content to stand alone but have not been tested against other nodes, verified, or refined through use."
tagline: "Raw capture, unprocessed, low confidence — where every garden node begins"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Form Definitions](index.html)


- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)
- in_precinct::[\[\[Vault Precinct\]\]](../glosses/Vault%20Precinct.html)

# Seed Stage

A seed is a garden node that has been captured but not yet developed. The content exists but lacks full structure, rich links, or editorial confidence. Every node enters the garden at seed stage.

Seed nodes are the product of extraction — pulled from source documents, meetings, conversations, or research sessions. They have enough content to stand alone (a core claim, a structural contract attempt, a definition) but have not been tested against other nodes, verified against sources, or refined through use.

## Characteristics

- Body content present but may be rough or incomplete
- Minimal outbound links beyond required predicates (`is_a::`, `has_status::`, `in_domain::`)
- No inbound links from other nodes (or very few)
- Has not been revisited since initial creation
- Low confidence for agent retrieval — an agent encountering two nodes that answer the same question should prefer a growing or evergreen node over a seed

## Transitions

**Seed → Growing**: When a node gains structure, links to related nodes, and has been revisited at least once with editorial attention. The node demonstrates its structural contract (required sections present and substantive).

**Seed → Pruned**: When a node is superseded before it develops, or when extraction produced a duplicate that a better node covers.

## Sources

Growth stage definitions from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), "Growth Stages as Lifecycle Metadata" section. Originally `status/seed` tag; migrated to `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` predicate per [\[\[Classification via Predicates Not Tags\]\]↑](../NODES.html#:~:text=Classification%20via%20Predicates%20Not%20Tags).

## Relations

- relates_to::[\[\[Growing Stage\]\]](Growing%20Stage.html) — the next stage in the growth progression
- relates_to::[\[\[Form Type\]\]](Form%20Type.html) — all form types begin at seed stage
- relates_to::[\[\[Structural Retrieval Hierarchy\]\]↑](../NODES.html#:~:text=Structural%20Retrieval%20Hierarchy) — seed nodes rank below growing and evergreen in retrieval priority
