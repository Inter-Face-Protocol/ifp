---
created: 2026-03-19
author: Christopher Allen
citation_slug: allen-2024-progressive-trust
publication_year: 2024
canonical: "https://developer.blockchaincommons.com/progressive-trust/"
brief_summary: "Christopher Allen's progressive trust framework: trust deepens through stages from initial contact to full collaboration, with each stage requiring verification before advancing. Not binary (trusted/untrusted) but a progression where disclosure, authentication, and commitment deepen together. Provides the conceptual foundation for IFP's progressive authentication and disclosure tier models."
tagline: "Trust deepens through verifiable stages, not binary trusted/untrusted switches"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)
- in_domain::[\[\[Self-Sovereign Identity\]\]](../../domains/Self-Sovereign%20Identity.html)
- cites_work_by::[\[\[Christopher Allen\]\]↑](../../NODES.html#:~:text=Christopher%20Allen)

# Allen (2024) Progressive Trust

## Bibliographic Entry

***Progressive Trust***, 2024, [developer reference], *Christopher Allen*, Blockchain Commons. Retrieved from https://developer.blockchaincommons.com/progressive-trust/

## Summary

Progressive trust rejects the binary trusted/untrusted model. Trust is a progression: initial contact → identity verification → context exchange → commitment → collaboration, with each stage requiring verification before advancing. The framework applies to both human relationships and technical systems — authentication, disclosure, and commitment deepen together rather than being set to maximum strength upfront.

## Key Points

**Trust is not binary.** Systems that model trust as trusted/untrusted miss the spectrum between first contact and deep collaboration. Progressive trust maps this spectrum explicitly.

**Verification before advancement.** Each stage of trust deepening requires some form of verification — not necessarily cryptographic, but appropriate to the stage. A shared introduction (Level 0 in IFP terms) is sufficient for initial contact; verified public keys (Level 2) are appropriate for sustained exchange.

**Disclosure deepens with trust.** What you share is proportional to how much trust has been established. This is not a privacy setting — it is a natural consequence of the relationship stage.

**Commitment deepens with trust.** Early-stage relationships involve low-commitment exchanges (gossip, context sharing). Deeper trust enables higher-commitment actions (recommendations, collaboration, shared projects).

**Applies to both human and technical systems.** The same progressive model governs how people build trust in face-to-face relationships and how agents build trust in protocol exchanges.

## Influence

Progressive trust is the conceptual foundation for two of IFP's core models: progressive authentication (IFP-5, four levels from shared secret to DID-bound identity) and disclosure tiers (IFP-12, six tiers from public to close). IFP operationalizes progressive trust for agent-to-agent communication.

## Sources

- https://developer.blockchaincommons.com/progressive-trust/

## Relations

- relates_to::[\[\[Progressive Authentication as Trust Deepening\]\]](../../models/Progressive%20Authentication%20as%20Trust%20Deepening.html)
  - IFP's four authentication levels implement progressive trust for agent identity verification.

- relates_to::[\[\[Disclosure Tier Hierarchy for Persona-Peer Relationships\]\]](../../models/Disclosure%20Tier%20Hierarchy%20for%20Persona-Peer%20Relationships.html)
  - IFP's disclosure tiers implement progressive trust for information sharing boundaries.

- relates_to::[\[\[Granularity of Progressive Authentication Stages\]\]](../../inquiries/Granularity%20of%20Progressive%20Authentication%20Stages.html)
  - The progressive trust framework describes a spectrum — the inquiry asks whether IFP's four discrete stages capture the right boundaries.

- relates_to::[\[\[Progressive Disclosure Over Eager Loading\]\]](../../principles/Progressive%20Disclosure%20Over%20Eager%20Loading.html)
  - Progressive disclosure is the information-sharing expression of progressive trust.

- relates_to::[\[\[Authority Flows from the Person\]\]](../../principles/Authority%20Flows%20from%20the%20Person.html)
  - Progressive trust assumes the person controls their own trust progression — no external authority decides when to deepen.

- relates_to::[\[\[Conversation Temperature as Protocol Cadence Spectrum\]\]](../../models/Conversation%20Temperature%20as%20Protocol%20Cadence%20Spectrum.html)
  - Temperature and trust deepen in parallel — cool conversations at low trust, hot collaboration at high trust.
