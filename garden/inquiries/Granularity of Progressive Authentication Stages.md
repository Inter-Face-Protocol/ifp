---
created: 2026-03-19
author: Christopher Allen
brief_summary: "IFP defines four authentication levels (shared secret, signed, verified, DID-bound) as discrete stages in a progressive trust model. This inquiry asks whether four stages capture the right boundaries — whether the jumps between levels are too large, whether intermediate stages are missing, and whether the Level 0 shared-secret starting point is appropriate for all contexts."
tagline: "Do four discrete authentication levels capture the right trust boundaries for agent protocols?"
---

← [Garden Patch Home](../) · [Inquiries](index.html)


- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Granularity of Progressive Authentication Stages

## The Question

IFP-5 defines four authentication levels as discrete stages in a progressive trust model. Each level represents a distinct verification mechanism:

| Level | Mechanism | Jump from Previous |
|-------|-----------|-------------------|
| 0 | Shared secret (introduction token) | — |
| 1 | Public-key signature | Symmetric → asymmetric crypto |
| 2 | Key verified via identity document | Self-asserted → externally resolvable |
| 3 | Key bound to DID | Domain-specific → decentralized identity |

The jumps between levels are large. Are there trust-relevant distinctions being collapsed? Are four stages the right granularity?

## What Makes This Worth Investigating

**The Level 0 → 1 jump is the largest.** Moving from a shared secret to public-key signatures changes the entire trust model — from "someone we both know introduced us" to "I can verify your signature independently." This single jump may be doing too much work.

**Level 3 depends on DID infrastructure that does not yet exist at scale.** If Level 3 is aspirational rather than practical, IFP effectively has three usable levels. Is that enough?

**Christopher Allen's progressive trust framework** describes a richer spectrum than four discrete stages. The question is whether IFP's four-level discretization loses important trust distinctions that the continuous model preserves.

**The minimum viable architecture question applies.** Are four levels a load-bearing architectural decision (the right boundaries, worth committing to early) or a tactical choice (the specific boundaries could be refined without reshaping the protocol)?

## Possible Directions

- The four levels may be correct — each represents a genuinely distinct trust mechanism
- An intermediate level between 0 and 1 (e.g., verified introduction — the introducer's identity is confirmed) might smooth the largest jump
- The levels might be better expressed as a continuous score with threshold behaviors rather than discrete stages
- Different application platforms (IFP-11) might need different granularity — Sanctuary (healthcare) may need finer stages than Friend Zone (social)

## Sources

- [IFP-5: Identity and Message Signing](../../ifp-5-identity-signing.md), Section 2
- [\[\[Allen (2024) Progressive Trust\]\]](../citations/Allen%20%282024%29%20Progressive%20Trust/Allen%20%282024%29%20Progressive%20Trust.html) — the continuous model these levels discretize

## Relations

- relates_to::[\[\[Progressive Authentication as Trust Deepening\]\]](../models/Progressive%20Authentication%20as%20Trust%20Deepening.html)
  - The model this inquiry questions.

- relates_to::[\[\[Allen (2024) Progressive Trust\]\]](../citations/Allen%20%282024%29%20Progressive%20Trust/Allen%20%282024%29%20Progressive%20Trust.html)
  - The progressive trust framework describes a richer spectrum than four discrete stages.

- relates_to::[\[\[Allen (2023) Minimum Viable Architecture\]\]](../citations/Allen%20%282023%29%20Minimum%20Viable%20Architecture/Allen%20%282023%29%20Minimum%20Viable%20Architecture.html)
  - Are four levels a load-bearing decision or a tactical one?

- relates_to::[\[\[Disclosure Spectrum as Discrete Tiers or Continuous Range\]\]](Disclosure%20Spectrum%20as%20Discrete%20Tiers%20or%20Continuous%20Range.html)
  - The same granularity question applies to disclosure tiers — both discretize a continuous spectrum.
