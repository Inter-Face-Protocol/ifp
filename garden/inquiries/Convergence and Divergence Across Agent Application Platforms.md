---
created: 2026-03-19
author: Christopher Allen
brief_summary: "IFP-11 describes eleven application platforms as distinct categories, but several share characteristics: Friend Zone and Guild Hall both manage relationship maintenance, Bazaar and Guild Hall both involve reputation-dependent matching. This inquiry asks where platforms genuinely diverge in protocol requirements and where apparent boundaries are artificial."
tagline: "Where do the eleven application platforms genuinely differ in protocol requirements?"
---

← [Garden Patch Home](../) · [Inquiries](index.html)


- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Convergence and Divergence Across Agent Application Platforms

## The Question

IFP-11 presents eleven platforms as distinct application domains. But reading the descriptions closely reveals convergence:

| Convergent Pair | Shared Characteristic |
|-----------------|----------------------|
| Friend Zone + Guild Hall | Relationship maintenance with progressive trust |
| Bazaar + Guild Hall | Reputation-dependent matching for bilateral exchange |
| Library + Agora | Knowledge management at different sharing scopes |
| Watchtower + Weatherbee | Proactive information gathering with different triggers |
| Round Table + Workshop | Multi-party coordination with different output types |

If two platforms share the same IFP features (phases, temperature, trust levels), differ only in domain vocabulary, and could be implemented by the same agent code — are they genuinely separate platforms?

## What Makes This Worth Investigating

**Convergence suggests shared abstractions.** If Friend Zone and Guild Hall both implement relationship-maintenance gossip with progressive trust, the shared abstraction (relationship-maintenance protocol) might be more useful to specify than the individual platforms.

**Divergence reveals real protocol differences.** Where platforms genuinely differ in protocol requirements — Sanctuary requires Level 3 authentication and full audit trails, Friend Zone can start at Level 0 — the differences are load-bearing and worth specifying.

**Implementation implications.** If platforms converge at the protocol level, an agent implementation can be configured for different domains rather than rebuilding per platform. If they diverge, each platform needs distinct protocol extensions.

**The Library problem.** IFP-11's Library platform spans personal knowledge management, group knowledge, and public encyclopedia. Christopher Allen's Deep Context Architecture distinguishes living documents (garden forms that grow through tending) from static archives (curated references). The Library platform may be collapsing distinct knowledge management paradigms. This tension was identified in the March 5, 2026 conversation between Christopher Allen and Peter Kaminski.

## Possible Directions

- The eleven platforms may be correctly distinct — domain-specific semantics matter even when protocol features overlap
- A smaller number of platform archetypes (relationship, exchange, knowledge, coordination, monitoring) might capture the real distinctions
- Platform convergence/divergence might be analyzed along three axes: trust requirements, temperature patterns, and disclosure models
- The Library platform specifically may need decomposition into distinct knowledge management paradigms

## Sources

- [IFP-11: Application Platforms](../../ifp-11-application-platforms.md), Sections 3-5
- [IFP-9: Ecosystem Status and Future Directions](../../ifp-9-ecosystem-status.md)

## Relations

- relates_to::[\[\[Organizing Principle for Agent Application Domains\]\]](Organizing%20Principle%20for%20Agent%20Application%20Domains.html)
  - The companion inquiry about the taxonomy's organizing principle.

- relates_to::[\[\[Cooperation vs Collaboration as Distinct Concepts\]\]](Cooperation%20vs%20Collaboration%20as%20Distinct%20Concepts.html)
  - Platform convergence/divergence may track the cooperation-collaboration spectrum — some platforms enable cooperation (independent agents, compatible goals), others enable collaboration (shared creation).

- relates_to::[\[\[Conversation Temperature as Protocol Cadence Spectrum\]\]](../models/Conversation%20Temperature%20as%20Protocol%20Cadence%20Spectrum.html)
  - Temperature differences are one genuine axis of platform divergence.

- relates_to::[\[\[Disclosure Spectrum as Discrete Tiers or Continuous Range\]\]](Disclosure%20Spectrum%20as%20Discrete%20Tiers%20or%20Continuous%20Range.html)
  - Different platforms may need different disclosure vocabularies — a genuine divergence point.

- relates_to::[\[\[Filtering Is More Valuable Than Connecting\]\]](../convictions/Filtering%20Is%20More%20Valuable%20Than%20Connecting.html)
  - If filtering is the core value, do all eleven platforms serve filtering equally? Platforms that primarily connect (Guild Hall, Bazaar) may operate under a different conviction than those that primarily filter (Friend Zone).

- relates_to::[\[\[Living Knowledge vs Static Archive in Agent Library Design\]\]](Living%20Knowledge%20vs%20Static%20Archive%20in%20Agent%20Library%20Design.html)
  - The Library platform is the sharpest convergence case — it collapses living knowledge and static archives into a single paradigm that may require distinct protocol behaviors.
