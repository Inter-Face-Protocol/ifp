---
created: 2026-03-07
author: Christopher Allen
brief_summary: "Three status tracks for three kinds of knowledge work. Maturity (Seed→Growing→Evergreen→Pruned) for living documents, curation (uncurated→curated→annotated) for static captures, processing (Captured→Transcribed→Cleaned→Summarized→Published) for meetings. The has_status:: predicate is universal; the vocabulary varies by node type."
tagline: "Three status tracks for three kinds of knowledge work — maturity, curation, and processing"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Status Lifecycle Tracks

The `has_status::` predicate appears on every classified node, but not all nodes progress the same way. A garden principle matures through tending. A clipping gets reviewed and filed. A meeting note gets processed from raw recording to shareable artifact. These are three distinct kinds of work, and the status vocabulary reflects that.

## Maturity Track

For living documents — garden nodes, research notes, references, authored documents.

**Seed** → **Growing** → **Evergreen** → **Pruned**

Progression reflects deepening understanding. A seed node has raw content and minimal links. A growing node is being shaped through use — sections refined, claims checked, new connections discovered. An evergreen node is mature, well-linked, and trustworthy. A pruned node has been superseded but preserved with a `superseded_by::` edge.

Agents retrieving knowledge should prefer evergreen over seed. The track is a promotion path: nodes start as seeds and graduate as they gain structure, links, and verification.

## Curation Track

For static captures — clippings, tool evaluations, imported content.

**Uncurated** → **Curated** → **Annotated**

Clippings are snapshots of external content at a point in time. They don't grow — they get reviewed, summarized, and connected. An uncurated clipping has no summary fields. A curated one has real `brief_summary:` and `tagline:`, filed in the right subfolder. An annotated one has enriched relations and interpretive context added above the original content.

## Processing Track

For meeting notes — records that progress through a production pipeline.

**Captured** → **Transcribed** → **Cleaned** → **Summarized** → **Published**

Progression reflects processing completeness, not content maturity. A published meeting note may still have shallow content — that's expected. The track is linear: each stage adds a layer of processing on top of the previous one.

Meeting notes also carry orthogonal fork predicates: `is_published::URL` (public meetings with a web page) and `is_shared::DATE` (private meetings shared with attendees). These are independent of the linear processing stages.

## Why Three Tracks

A single maturity track doesn't fit all node types. Calling a clipping "seed" implies it will grow — it won't. Calling a meeting note "evergreen" implies it's been refined through tending — meeting notes are processed, not tended. Each track names the kind of work that advances a node through its lifecycle.

The `has_status::` predicate is the same everywhere. What changes is the vocabulary of targets it points to. This keeps the graph infrastructure uniform while letting different precincts and node types describe their own progression.

## Sources

Status lifecycle design from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), "Growth Stages as Lifecycle Metadata" section. Processing track from [\[\[Linear Processing Stages for Meetings\]\]↑](../EXTERNAL.html#:~:text=Linear%20Processing%20Stages%20for%20Meetings). Curation track from vault enrichment workstream experience.

## Relations

- relates_to::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html) — entry point for the maturity track
- relates_to::[\[\[Growing Stage\]\]](../forms/Growing%20Stage.html)
- relates_to::[\[\[Evergreen Stage\]\]](../forms/Evergreen%20Stage.html)
- relates_to::[\[\[Pruned Stage\]\]↑](../EXTERNAL.html#:~:text=Pruned%20Stage) — exit point for the maturity track
- relates_to::[\[\[Linear Processing Stages for Meetings\]\]↑](../EXTERNAL.html#:~:text=Linear%20Processing%20Stages%20for%20Meetings) — the decision that defined the processing track
- relates_to::[\[\[Classification via Predicates Not Tags\]\]↑](../EXTERNAL.html#:~:text=Classification%20via%20Predicates%20Not%20Tags) — the decision that made has_status:: a typed relation
- relates_to::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html) — maturity track is primarily a garden precinct concept
- relates_to::[\[\[Vault Precinct\]\]](../glosses/Vault%20Precinct.html) — curation and processing tracks serve the vault precinct
- relates_to::[\[\[When to Specify and When to Explore in Protocol Evolution\]\]](../inquiries/When%20to%20Specify%20and%20When%20to%20Explore%20in%20Protocol%20Evolution.html)
  - IFP's own status lifecycle (Draft→Proposed→Active) is a maturity track — how does it compare to garden maturity stages?
