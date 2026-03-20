---
created: 2026-03-19
author: Christopher Allen
brief_summary: "IFP-11's Library platform spans personal knowledge management, group knowledge, and public encyclopedia under a single name. This inquiry asks whether the Library collapses distinct knowledge management paradigms — living documents that grow through tending vs static archives that are curated and preserved — and whether these require different protocol behaviors."
tagline: "Does the Library platform collapse living knowledge and static archives into a single paradigm?"
---

← [Garden Patch Home](../) · [Inquiries](index.html)


- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Living Knowledge vs Static Archive in Agent Library Design

## The Question

IFP-11 describes the Library platform as spanning a spectrum from personal knowledge management to group knowledge to public encyclopedia — "a continuum from private notes to shared wisdom." The default temperature is cool. The analogue is "personal wikis, shared knowledge bases, Wikipedia."

This framing treats knowledge storage as a single activity that varies by sharing scope. But there are at least two distinct paradigms hiding inside "Library":

**Living knowledge** — documents that grow, split, merge, and evolve through active tending. A garden node, a wiki page under active editing, a research note accumulating findings. These are never "done." Their value increases through ongoing maintenance. They need version awareness, merge semantics, and conflict resolution.

**Static archives** — curated captures preserved for reference. A cited paper, a clipped article, a meeting transcript. These are append-only or immutable. Their value is in faithful preservation, not evolution. They need provenance tracking, retrieval optimization, and format stability.

These two paradigms require different protocol behaviors from an agent:

| Dimension | Living Knowledge | Static Archive |
|-----------|-----------------|----------------|
| **Mutability** | Evolves continuously | Append-only or immutable |
| **Agent role** | Tend, update, connect | Retrieve, cite, preserve |
| **Sharing semantics** | Version-aware collaboration | Faithful reproduction |
| **Conflict model** | Merge and resolve | No conflicts (immutable) |
| **Temperature** | Warm when active, cool when resting | Always cool |
| **Quality signal** | Freshness, connection density | Provenance, citation count |

## What Makes This Worth Investigating

**The March 5, 2026 conversation.** Christopher Allen and Peter Kaminski identified this collision directly. Christopher's Deep Context Architecture distinguishes living garden nodes (typed forms that grow through tending stages: Seed → Growing → Evergreen → Pruned) from static captures (clippings, citations, transcripts that are curated but not rewritten). Peter's Library platform collapses both into a single sharing-scope spectrum.

**Agent behavior differs.** An agent tending a living knowledge base needs to recognize staleness, propose updates, merge contributions, and resolve conflicts. An agent managing a static archive needs to preserve provenance, optimize retrieval, and resist modification. Using the same protocol behaviors for both risks either over-maintaining archives (wasting agent effort on immutable content) or under-maintaining living documents (treating evolving knowledge as static).

**The Wikipedia analogy is misleading.** Wikipedia articles look like static reference pages but are actually living documents under continuous collaborative editing with sophisticated governance (talk pages, edit wars, protection levels, featured article review). A "Library" that treats Wikipedia as the same kind of thing as a personal bookmark collection misses the governance complexity that makes Wikipedia work.

## Possible Directions

- The Library platform could split into two platforms: one for living knowledge (closer to Workshop or a new "Garden" platform) and one for static archives (closer to a pure retrieval service)
- Living and static could remain within Library but as distinct modes with different agent behaviors and protocol features
- The status lifecycle concept from Deep Context Architecture (Seed → Growing → Evergreen → Pruned for living; uncurated → curated → annotated for static) could inform Library's internal organization
- The distinction might not matter at the protocol level — agents can infer the paradigm from content metadata without explicit protocol support

## Sources

- [IFP-11: Application Platforms](../../ifp-11-application-platforms.md), Library platform
- 2026-03-05 Peter Kaminski - AI and Garden — conversation identifying the collision
- [\[\[Living Documents Over Static Publications\]\]](../principles/Living%20Documents%20Over%20Static%20Publications.html) — the principle that grounds the living-knowledge paradigm
- [\[\[Status Lifecycle Tracks\]\]](../models/Status%20Lifecycle%20Tracks.html) — three status tracks for three kinds of knowledge work

## Relations

- relates_to::[\[\[Convergence and Divergence Across Agent Application Platforms\]\]](Convergence%20and%20Divergence%20Across%20Agent%20Application%20Platforms.html)
  - The Library collision is a specific instance of the broader platform convergence/divergence question.

- relates_to::[\[\[Living Documents Over Static Publications\]\]](../principles/Living%20Documents%20Over%20Static%20Publications.html)
  - The living-document principle is the lens that reveals the collision — without it, Library looks like a coherent spectrum.

- relates_to::[\[\[Status Lifecycle Tracks\]\]](../models/Status%20Lifecycle%20Tracks.html)
  - The three status tracks (maturity, curation, processing) map to different Library paradigms.

- relates_to::[\[\[Document Lifecycle Governance Heuristics\]\]](../models/Document%20Lifecycle%20Governance%20Heuristics.html)
  - Living knowledge requires governance heuristics (split, merge, draftify) that static archives do not.

- relates_to::[\[\[When to Specify and When to Explore in Protocol Evolution\]\]](When%20to%20Specify%20and%20When%20to%20Explore%20in%20Protocol%20Evolution.html)
  - The Library's single-paradigm design may be a tactical choice that should remain open for implementation discovery.

- relates_to::[\[\[Vocabulary Lifecycle Through Tending\]\]](../models/Vocabulary%20Lifecycle%20Through%20Tending.html)
  - Living knowledge requires vocabulary tending; static archives preserve vocabulary as-is.
