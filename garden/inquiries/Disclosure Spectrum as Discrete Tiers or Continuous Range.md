---
created: 2026-03-19
author: Christopher Allen
brief_summary: "IFP-12 defines six named disclosure tiers (public through close) as a discrete hierarchy. This inquiry asks whether discrete tiers are the right model — whether a continuous range would better capture the nuance of information sharing, whether the specific tier names impose cultural assumptions, and whether six is the right number."
tagline: "Should information sharing boundaries be discrete named tiers or a continuous spectrum?"
---

← [Garden Patch Home](../) · [Inquiries](index.html)


- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Disclosure Spectrum as Discrete Tiers or Continuous Range

## The Question

IFP-12 defines six disclosure tiers arranged in a hierarchy from narrow to broad sharing:

```
public → professional → professional-open → community-trust → personal → close
```

This raises three related questions:

1. **Discrete or continuous?** Is information sharing naturally tiered, or is it a continuous spectrum that these six labels artificially discretize?
2. **Why these six?** The specific tier names embed assumptions about how relationships are categorized — professional/personal, community/individual. Do these categories transfer across cultures and contexts?
3. **Why six?** Five might be sufficient (drop professional-open or community-trust). Seven might be needed (add a tier for family or legal obligations). What determines the right granularity?

## What Makes This Worth Investigating

**Disclosure behavior in practice is contextual, not categorical.** A person might share their health status with a professional colleague (outside the "personal" tier) when the context demands it. Rigid tiers may not accommodate context-dependent sharing.

**The tier names are culturally specific.** "Professional" and "personal" map to a work/life boundary that not all cultures draw in the same place. "Community-trust" assumes a community concept that may not apply to all relationship structures.

**IFP-12's own persona model suggests fluidity.** Personas emerge organically from observation (not enumeration), but disclosure tiers are enumerated upfront. There is a tension between emergent personas and prescribed tiers.

**The minimum viable architecture question.** Are six named tiers a load-bearing decision (the protocol needs stable names for interoperability) or a tactical choice (the names and number could change without reshaping the protocol)?

## Possible Directions

- The six tiers may be correct — they provide enough granularity for agent interoperability without overwhelming users
- A continuous score (0-100) with named ranges might be more flexible
- Tiers could be user-defined rather than protocol-defined — the protocol specifies the mechanism, not the vocabulary
- Different domains may need different tier vocabularies — healthcare disclosure differs from social disclosure

## Sources

- [IFP-12: Personas and Disclosure Tiers](../../ifp-12-personas.md), Section 3.3
- [\[\[Allen (2024) Progressive Trust\]\]](../citations/Allen%20%282024%29%20Progressive%20Trust/Allen%20%282024%29%20Progressive%20Trust.html) — progressive disclosure as a continuous model

## Relations

- relates_to::[\[\[Disclosure Tier Hierarchy for Persona-Peer Relationships\]\]](../models/Disclosure%20Tier%20Hierarchy%20for%20Persona-Peer%20Relationships.html)
  - The model this inquiry questions.

- relates_to::[\[\[Granularity of Progressive Authentication Stages\]\]](Granularity%20of%20Progressive%20Authentication%20Stages.html)
  - The same discrete-vs-continuous question applies to authentication levels.

- relates_to::[\[\[Personas Emerge from Observation Not Enumeration\]\]](../convictions/Personas%20Emerge%20from%20Observation%20Not%20Enumeration.html)
  - Emergent personas paired with prescribed tiers creates a tension worth examining.

- relates_to::[\[\[Convergence and Divergence Across Agent Application Platforms\]\]](Convergence%20and%20Divergence%20Across%20Agent%20Application%20Platforms.html)
  - Different platforms may need different disclosure vocabularies.
- relates_to::[\[\[Vocabulary Lifecycle Through Tending\]\]](../models/Vocabulary%20Lifecycle%20Through%20Tending.html)
  - Disclosure tier names are vocabulary that needs tending — weeding ambiguous names, seeding precise ones.
