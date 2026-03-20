---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Inter-Face Protocol defines six conversation phases — greeting, context, probe, recommend, close, error — that are social in nature, not mechanical. Phases are advisory, revisitable, and named in the message envelope. They model how trust-building conversations naturally progress rather than imposing request-response mechanics."
tagline: "How does a trust-building conversation progress through structured phases?"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Social Conversation Phases as Protocol Semantics

Traditional protocols use mechanical request-response patterns: client sends request, server returns response, transaction complete. Inter-Face Protocol replaces this with **social phases** that model how trust-building conversations naturally progress between people.

## The Six Phases

| Phase | Purpose | What Agents Do |
|-------|---------|---------------|
| **Greeting** | Establish identity and disclosure tier | Exchange credentials, negotiate what to share |
| **Context** | Share current situation | Exchange relevant context from each operator's world |
| **Probe** | Explore overlaps | Test whether shared context reveals actionable connections |
| **Recommend** | Surface opportunity | Propose that the humans should talk, with specific reasoning |
| **Close** | End exchange | Wrap up, note any follow-up cadence |
| **Error** | Explicit problem | Signal misunderstanding or incompatibility in natural language |

## Social, Not Mechanical

Three properties distinguish these from RPC-style phases:

**Advisory.** Phases are declared in the message envelope, not enforced by the protocol. An agent may revisit an earlier phase if new context emerges during probing.

**Progressive.** Phases build on each other — you cannot meaningfully probe without context, and you cannot meaningfully recommend without probing. But the progression is not strictly linear.

**Most exchanges end before recommend.** A successful gossip exchange that finds no actionable overlap closes after the probe phase. Silence is the normal outcome, not a failure.

## Error as Negotiation

The error phase deserves particular attention. In traditional protocols, an error is a failure code. In IFP, an error is an opportunity for natural-language negotiation — agents explain what they did not understand and attempt to resolve the incompatibility conversationally. This implements IFP-1's principle that agent-age protocols should use [\[\[Errors as Negotiation Opportunities\]\]](../patterns/Errors%20as%20Negotiation%20Opportunities.html).

## Sources

- [IFP-3: Inter-Face Message Format](../../ifp-3-message-format.md), Section 2
- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), Section 6.3

## Relations

- relates_to::[\[\[Conversation Temperature as Protocol Cadence Spectrum\]\]](Conversation%20Temperature%20as%20Protocol%20Cadence%20Spectrum.html)
  - Phases progress at the cadence the temperature sets — cool phases take days, hot phases take minutes.

- relates_to::[\[\[Gossip as Social Sensing Filter\]\]](../glosses/Gossip%20as%20Social%20Sensing%20Filter.html)
  - The phase sequence is the mechanism through which gossip filtering operates.

- relates_to::[\[\[Recommendation as Surfaced Opportunity\]\]](../glosses/Recommendation%20as%20Surfaced%20Opportunity.html)
  - The recommend phase is where filtering yields a result worth human attention.

- relates_to::[\[\[Errors as Negotiation Opportunities\]\]](../patterns/Errors%20as%20Negotiation%20Opportunities.html)
  - The error phase implements conversational error resolution rather than mechanical failure codes.

- relates_to::[\[\[Progressive Disclosure Over Eager Loading\]\]](../principles/Progressive%20Disclosure%20Over%20Eager%20Loading.html)
  - Phases progressively deepen context exchange — greeting before context, context before probe.
- relates_to::[\[\[Social Phase Decomposition in Trust-Building Protocols\]\]](../inquiries/Social%20Phase%20Decomposition%20in%20Trust-Building%20Protocols.html)
  - Do six phases capture the right decomposition of trust-building conversation?
