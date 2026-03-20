---
created: 2026-03-19
author: Christopher Allen
citation_slug: allen-2023-minimum-viable-architecture
publication_year: 2023
canonical: "https://www.blockchaincommons.com/musings/musings-mva/"
brief_summary: "Christopher Allen's minimum viable architecture principle: make a few hard-to-reverse decisions early, defer everything else. Commit to the decisions that would be expensive to change later — the 80/20 choices that shape everything downstream — and leave tactical decisions for when you have more information."
tagline: "Make the hard-to-reverse decisions early, defer everything else"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../../domains/Deep%20Context%20Architecture.html)
- cites_work_by::[\[\[Christopher Allen\]\]↑](../../NODES.html#:~:text=Christopher%20Allen)

# Allen (2023) Minimum Viable Architecture

## Bibliographic Entry

***Musings of a Trust Architect: Minimum Viable Architecture***, 2023, [blog post], *Christopher Allen*, Blockchain Commons. Retrieved from https://www.blockchaincommons.com/musings/musings-mva/

## Summary

The minimum viable architecture principle argues that early architectural decisions should focus on the few choices that are hard to reverse later — the load-bearing decisions that shape everything downstream. Defer tactical decisions until you have more information. The 80/20 rule applies: a small number of early commitments determine the system's trajectory, and getting those wrong is expensive. Getting tactical details wrong is cheap and correctable.

## Key Points

**Hard-to-reverse vs easy-to-change.** The distinction is not between "important" and "unimportant" decisions, but between decisions that are expensive to reverse and those that are cheap to change. Focus early energy on the former.

**Defer tactical decisions.** When you do not yet know enough to make a decision well, and the decision is easy to change later, wait. Premature commitment to tactical choices creates unnecessary constraints.

**80/20 for architecture.** A small number of load-bearing decisions — data model, trust model, identity model, protocol boundaries — determine 80% of the system's character. Everything else is implementation detail.

## Influence

Directly relevant to Inter-Face Protocol's architectural choices. IFP's load-bearing decisions (gossip-as-filter, temperature model, agent-age principles, human legibility, progressive trust) are the minimum viable architecture. Many of IFP's tactical decisions (specific field names, rate limits, endpoint paths) could change without reshaping the protocol.

## Sources

- https://www.blockchaincommons.com/musings/musings-mva/

## Relations

- relates_to::[\[\[Granularity of Progressive Authentication Stages\]\]](../../inquiries/Granularity%20of%20Progressive%20Authentication%20Stages.html)
  - Are the four authentication levels a load-bearing architectural decision or a tactical choice that could be refined?

- relates_to::[\[\[Disclosure Spectrum as Discrete Tiers or Continuous Range\]\]](../../inquiries/Disclosure%20Spectrum%20as%20Discrete%20Tiers%20or%20Continuous%20Range.html)
  - Are the six disclosure tier names a minimum viable architecture decision or a deferrable tactical choice?

- relates_to::[\[\[Social Phase Decomposition in Trust-Building Protocols\]\]](../../inquiries/Social%20Phase%20Decomposition%20in%20Trust-Building%20Protocols.html)
  - Are the six conversation phases load-bearing architecture or tactical decomposition?

- relates_to::[\[\[Clarity Over Tolerance in Agent-Age Protocols\]\]](../../decisions/Clarity%20Over%20Tolerance%20in%20Agent-Age%20Protocols.html)
  - Replacing Postel's Law is a hard-to-reverse architectural decision — exactly the kind minimum viable architecture says to make early.

- relates_to::[\[\[When to Specify and When to Explore in Protocol Evolution\]\]](../../inquiries/When%20to%20Specify%20and%20When%20to%20Explore%20in%20Protocol%20Evolution.html)
  - The central application of minimum viable architecture to IFP: which decisions deserve specification commitment and which should remain open for implementation discovery?
