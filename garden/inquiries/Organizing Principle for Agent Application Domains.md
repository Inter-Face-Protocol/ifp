---
created: 2026-03-19
author: Christopher Allen
brief_summary: "IFP-11 describes eleven application platforms (Friend Zone, Bazaar, Guild Hall, etc.) but does not articulate a clear organizing principle for why these eleven and not others. This inquiry asks what principle should govern the taxonomy — by trust requirements, by temperature, by human need, or by protocol feature usage."
tagline: "What principle should organize the taxonomy of agent application domains?"
---

← [Garden Patch Home](../) · [Inquiries](index.html)


- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Organizing Principle for Agent Application Domains

## The Question

IFP-11 describes eleven application platforms that demonstrate what Inter-Face Protocol enables:

Friend Zone, Comm Badge, Agora, Bazaar, Guild Hall, Round Table, Library, Watchtower, Weatherbee, Sanctuary, Workshop

Each platform has a stated function, characteristic temperature, and analogue to centralized systems it replaces. But the specification does not articulate **why these eleven** — what organizing principle determines the boundaries between platforms or predicts what the twelfth would be.

## What Makes This Worth Investigating

**Multiple organizing principles are implicit.** The platforms can be read as organized by:
- **Human need**: social (Friend Zone), professional (Guild Hall), commercial (Bazaar), creative (Workshop)
- **Trust requirements**: low (Agora, public), medium (Bazaar, bilateral), high (Sanctuary, healthcare)
- **Temperature**: cool (Library, Agora), warm (Guild Hall, Round Table), variable (Friend Zone, Comm Badge)
- **Protocol feature**: messaging (Comm Badge), discovery (Weatherbee), monitoring (Watchtower)

These organizing principles overlap but do not align cleanly. Friend Zone is organized by human need, Sanctuary by trust requirements, and Weatherbee by protocol feature.

**Without an explicit principle, the taxonomy resists extension.** When a new use case emerges — say, education or governance — it is unclear whether it should be a new platform, an extension of Workshop, or a combination of Round Table and Library. The lack of organizing principle makes the taxonomy descriptive rather than generative.

**The minimum viable architecture question.** Is the platform taxonomy a load-bearing architectural decision that constrains future development? Or is it an illustrative categorization that could be reorganized without affecting the protocol?

## Possible Directions

- The taxonomy may be intentionally illustrative — not meant as a formal classification
- Trust requirements might be the primary organizing principle — it is the dimension most connected to protocol features
- Temperature might serve as the organizing principle — it is already inherited from IFP-1 and shapes protocol behavior
- A two-axis taxonomy (trust level × temperature) might reveal gaps and overlaps in the current eleven platforms

## Sources

- [IFP-11: Application Platforms](../../ifp-11-application-platforms.md)
- [IFP-9: Ecosystem Status and Future Directions](../../ifp-9-ecosystem-status.md)

## Relations

- relates_to::[\[\[Convergence and Divergence Across Agent Application Platforms\]\]](Convergence%20and%20Divergence%20Across%20Agent%20Application%20Platforms.html)
  - The companion inquiry about instance-level boundaries and overlap.

- relates_to::[\[\[Allen (2023) Minimum Viable Architecture\]\]](../citations/Allen%20%282023%29%20Minimum%20Viable%20Architecture/Allen%20%282023%29%20Minimum%20Viable%20Architecture.html)
  - Is the platform taxonomy a minimum viable architecture decision or a deferrable tactical one?

- relates_to::[\[\[Conversation Temperature as Protocol Cadence Spectrum\]\]](../models/Conversation%20Temperature%20as%20Protocol%20Cadence%20Spectrum.html)
  - Temperature is one candidate organizing principle for the taxonomy.

- relates_to::[\[\[Progressive Authentication as Trust Deepening\]\]](../models/Progressive%20Authentication%20as%20Trust%20Deepening.html)
  - Trust level is another candidate organizing principle — different platforms require different authentication.

- relates_to::[\[\[Domains and Pattern Languages as Organizational Concepts\]\]](Domains%20and%20Pattern%20Languages%20as%20Organizational%20Concepts.html)
  - The eleven application platforms may function as pattern languages — each platform is a pattern language for a particular kind of human-agent interaction. If so, the organizing principle is pattern language scope, not feature taxonomy.
