---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Defines the Growing Stage, the active tending phase where nodes gain structure, links, and editorial attention. A growing node demonstrates its structural contract and has been revisited at least once, but remains incomplete or untested. Most nodes spend the majority of their lifecycle here. Mid-confidence for retrieval."
tagline: "Structured and linked but still developing — the active tending stage"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Form Definitions](index.html)


- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)
- in_precinct::[\[\[Vault Precinct\]\]](../glosses/Vault%20Precinct.html)

# Growing Stage

A growing node has been revisited and developed beyond its initial capture. It demonstrates its structural contract (required sections present and substantive), links to related nodes, and reflects editorial attention — but remains incomplete or untested in some dimension.

Growing is the active tending stage. A node here is being shaped through use: new links discovered, sections refined, claims checked against sources or other nodes. Most nodes spend the majority of their lifecycle at growing stage.

## Characteristics

- Structural contract satisfied (required sections present with real content)
- Multiple outbound links to related nodes, sources, and domains
- Some inbound links from other nodes
- Has been revisited at least once since creation
- Mid-confidence for retrieval — preferred over seed nodes, but an evergreen node on the same topic takes priority

## Transitions

**Growing → Evergreen**: When a node is mature, well-linked, and trustworthy. The content has been validated through use — cited by other nodes, tested against sources, stable across multiple sessions. No required sections are incomplete or placeholdered.

**Growing → Pruned**: When a node becomes obsolete or is superseded by a better treatment of the same topic.

**Growing → Seed** (demotion): When revisiting reveals the node's structure was premature — the content needs significant rework rather than incremental improvement.

## Sources

Growth stage definitions from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), "Growth Stages as Lifecycle Metadata" section. Originally `status/growing` tag; migrated to `has_status::[\[\[Growing Stage\]\]](Growing%20Stage.html)` predicate per [\[\[Classification via Predicates Not Tags\]\]↑](../NODES.html#:~:text=Classification%20via%20Predicates%20Not%20Tags).

## Relations

- relates_to::[\[\[Seed Stage\]\]](Seed%20Stage.html) — the previous stage in the growth progression
- relates_to::[\[\[Evergreen Stage\]\]](Evergreen%20Stage.html) — the next stage in the growth progression
- relates_to::[\[\[Structural Retrieval Hierarchy\]\]↑](../NODES.html#:~:text=Structural%20Retrieval%20Hierarchy) — growing nodes rank in the first retrieval tier alongside evergreen
