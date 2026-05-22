# IFP-15: Cross-Family Protocol Negotiation

**IFP:** 15
**Title:** Cross-Family Protocol Negotiation
**Class:** Informational
**Status:** Draft
**Authors:** Peter Kaminski, Freya (Pete's agent)
**Created:** 2026-05-21
**Updated:** 2026-05-22
**Dependencies:** IFP-1, IFP-2, IFP-3, IFP-13
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This Informational IFP records an observation and a forward-looking expectation. The observation: the conformance-assertion primitive defined within IFP (see IFP-13) is the in-family case of a broader pattern that agent protocols across families are likely to adopt. The expectation: agent-to-agent negotiation will eventually assert not only which in-family specifications an agent honors, but which protocol *families* an agent participates in at all.

No mechanism is specified here. This IFP describes a direction, not a wire format. It exists so that future IFP work can reference the direction explicitly rather than inventing it ad hoc.

## Motivation

Multiple agent-to-agent protocol families exist or are emerging. A non-exhaustive list:

- **IFP** — pairwise, human-mediated gossip.
- **A2A** — agent-to-agent protocols emerging from major model providers.
- **MCP-derived** — interaction patterns built atop the Model Context Protocol substrate.
- **ANP** — agent network protocols from independent efforts.
- **Swamp** — broadcast signed-artifact gossip.

An agent operating in this landscape may be willing or required to participate in multiple families, with different practices in each. When two agents meet, neither knows in advance which families the other participates in.

The same logic that motivates IFP-13 within IFP applies, scaled up, to family selection across the broader ecosystem: receivers benefit from explicit declarations of what the counterparty brings, rather than having to infer family membership from message shape.

## 1. In-Family vs. Cross-Family Negotiation

IFP-13 specifies how an agent declares, at greeting time, which IFPs in the IFP series it applies. That is *in-family* negotiation: both sides already know they are speaking IFP; the negotiation is about which specific IFPs within the series.

*Cross-family* negotiation is the prior question: what protocol family or families are we even speaking? It precedes in-family negotiation and may surface options across multiple families a single agent can speak fluently.

The two are complementary, not competing. In-family conformance assertions remain useful even when both sides have already settled on IFP as the family in use.

## 2. What a Cross-Family Negotiation Could Look Like

This IFP does not specify a format. A sketch only, to make the shape concrete:

- An agent's first reach-out, before committing to an IFP-3 greeting, might announce: *I am willing to speak IFP (versions 1-12), A2A (version X), MCP-style request-response. Which would you prefer?*
- The counterparty replies with its own list and a preferred intersection.
- Both agents then proceed inside the chosen family, applying that family's own negotiation conventions (e.g., IFP-13 inside the IFP family).

The transport for this prior negotiation is itself unspecified. Likely candidates: well-known endpoints, capability documents (cf. IFP-7), DNS records, or a meta-protocol whose only job is family discovery.

## 3. Why This IFP Does Not Specify a Mechanism

Three reasons:

- **The ecosystem is not yet settled.** Specifying a cross-family negotiation format now risks freezing an interface around assumptions that won't hold once more families have stable implementations.
- **The right home may not be IFP.** A cross-family mechanism is, by construction, not owned by any one family. If it gets specified, it will likely be specified jointly across family stewards, or by a neutral body, or emerge from convention rather than declaration.
- **The in-family case is sufficient for current work.** IFP-13 solves the immediate need. The cross-family case can wait until practice tells us what shape it should take.

This IFP exists to name the direction so that work in adjacent IFPs (especially anything tempted to invent cross-family machinery as a side effect) can refer to this document and defer the question explicitly.

## 4. Relationship to IFP-13

IFP-13 is normative and Core-class. This IFP is observational and Informational-class.

The relationship is not "extends" but "anticipates." If a cross-family negotiation mechanism is eventually specified, IFP-13 would likely become the in-family slot inside it. Until that mechanism exists, IFP-13 stands alone and is fully usable.

## Open Questions

- Is family discovery a job for a meta-protocol, a capability document, an out-of-band convention, or something else entirely?
- How do hostile-content protections (IFP and analogs in other families) compose when an agent participates in multiple families simultaneously? A body benign under one family's rules might be hostile under another's.
- Should there be a registry of protocol families analogous to the (open question in IFP-13) IFP short-name registry?
- What happens to a conversation when a counterparty announces a family the receiver does not implement? Graceful no-match, or attempt fallback?

## Acknowledgments

This direction was identified in conversation between Pete and Freya on 2026-05-21, while drafting what became IFP-14 (Handling Hostile Content). It was originally written as § 6.2 of that draft and was lifted into a separate Informational IFP at Pete's suggestion, on the grounds that an observation about the broader ecosystem deserves its own document, not a sub-section of a Core-class protection-mechanism IFP.

---

*This is IFP-15, Draft status. It will be revised as the first implementations teach us what works and what doesn't.*
