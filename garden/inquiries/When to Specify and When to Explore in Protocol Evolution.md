---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Protocol evolution involves a tension between specifying details (creating interoperability commitments) and leaving space for implementation discovery. IFP currently specifies both load-bearing architecture and tactical details at the same level. This inquiry asks how to distinguish what should be committed in specifications from what should remain open for exploration."
tagline: "When should a protocol commit to specification details vs leave space for implementation discovery?"
---

← [Garden Patch Home](../) · [Inquiries](index.html)


- is_a::[\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# When to Specify and When to Explore in Protocol Evolution

## The Question

Protocol design involves two activities that serve different purposes:

**Specification** commits to details — field names, message formats, authentication levels, tier names. Specifications create interoperability: two independent implementations can communicate because they agree on the same details. But premature specification locks in tactical choices before enough is known to choose well.

**Exploration** leaves details open — describing the problem, the design space, and the constraints without committing to specific solutions. Exploration enables discovery: implementations can experiment with different approaches and converge on what works. But insufficient specification prevents interoperability: without shared conventions, implementations diverge.

The tension: specify too early and you lock in mistakes; specify too late and you never converge.

## Where This Tension Appears in IFP

IFP's twelve specifications mix load-bearing architectural decisions with tactical implementation details at the same level of commitment (all are "Draft" status, all use the same normative language):

**Load-bearing decisions that benefit from early specification:**
- Gossip-as-filter framing (IFP-1) — changes everything if changed
- Temperature model (IFP-1) — inherited across all specs
- Human legibility constraint (IFP-1) — non-negotiable design boundary
- Phase model (IFP-3) — social backbone of every exchange
- Agent-age protocol principles (IFP-1) — shapes error handling, versioning, capabilities

**Tactical details that might benefit from remaining open:**
- Four authentication levels (IFP-5) — why not three or five?
- Six disclosure tier names (IFP-12) — why these categories?
- Eleven application platforms (IFP-11) — illustrative or normative?
- Rate limiting defaults (IFP-6) — heuristics, not architecture
- Specific endpoint paths (IFP-6) — conventions, not constraints

IFP-2's status lifecycle (Draft → Proposed → Active) recognizes this tension in principle — Active status requires two independent implementations. But the current specifications do not distinguish between "this is load-bearing architecture we're confident about" and "this is a tactical proposal we expect to revise."

## What Makes This Worth Investigating

**The IETF lesson.** The Internet Engineering Task Force learned through decades of experience that "rough consensus and running code" works better than premature specification. IFP-1 explicitly cites this principle. But the current specifications sometimes specify details before running code exists to validate them.

**IFP-2's own standard.** IFP-2 requires two independent interoperating implementations before a specification reaches Active status. This is a strong maturity gate for the overall protocol. But within Draft status, there is no mechanism to distinguish load-bearing architecture from tactical proposals.

**The minimum viable architecture principle.** Christopher Allen's minimum viable architecture argues: commit to hard-to-reverse decisions early, defer easy-to-change decisions until you know more. Applied to IFP, this suggests the specifications could explicitly mark which decisions are architectural commitments and which are tactical defaults that implementations should feel free to vary.

## Possible Directions

- IFP specifications could adopt a convention marking sections as "Architectural" (stable, intended as commitment) vs "Exploratory" (expected to change based on implementation experience)
- The eleven application platforms (IFP-11) could be reframed as an Informational exploration rather than implied normative categories
- Tactical details (rate limits, endpoint paths, tier names) could be moved to implementation guidance rather than core specifications
- IFP-2 could define a pre-Draft status for design exploration documents that are not yet ready for specification-level commitment

## Sources

- [IFP-2: Specification Style Guide](../../ifp-2-style-guide.md), status lifecycle and normative language
- [IFP-1: Philosophy and Design Principles](../../ifp-1-philosophy.md), "rough consensus and running code"
- [\[\[Allen (2023) Minimum Viable Architecture\]\]](../citations/Allen%20%282023%29%20Minimum%20Viable%20Architecture/Allen%20%282023%29%20Minimum%20Viable%20Architecture.html) — the principle of committing to hard-to-reverse decisions early

## Relations

- relates_to::[\[\[Allen (2023) Minimum Viable Architecture\]\]](../citations/Allen%20%282023%29%20Minimum%20Viable%20Architecture/Allen%20%282023%29%20Minimum%20Viable%20Architecture.html)
  - The minimum viable architecture principle directly addresses when to commit vs defer.

- relates_to::[\[\[Granularity of Progressive Authentication Stages\]\]](Granularity%20of%20Progressive%20Authentication%20Stages.html)
  - Four authentication levels may be a tactical detail specified before implementation can validate the boundaries.

- relates_to::[\[\[Disclosure Spectrum as Discrete Tiers or Continuous Range\]\]](Disclosure%20Spectrum%20as%20Discrete%20Tiers%20or%20Continuous%20Range.html)
  - Six disclosure tier names may be exploratory conventions rather than architectural commitments.

- relates_to::[\[\[Organizing Principle for Agent Application Domains\]\]](Organizing%20Principle%20for%20Agent%20Application%20Domains.html)
  - Eleven application platforms may be design exploration rather than specification.

- relates_to::[\[\[Structured Schema vs Natural Language for Agent Message Content\]\]](Structured%20Schema%20vs%20Natural%20Language%20for%20Agent%20Message%20Content.html)
  - Natural language bodies may be a load-bearing architectural choice — or a tactical bet that should remain open for experimentation.

- relates_to::[\[\[Clarity Over Tolerance in Agent-Age Protocols\]\]](../decisions/Clarity%20Over%20Tolerance%20in%20Agent-Age%20Protocols.html)
  - Replacing Postel's Law is a load-bearing architectural decision — the kind that should be specified early.
- relates_to::[\[\[Document Lifecycle Governance Heuristics\]\]](../models/Document%20Lifecycle%20Governance%20Heuristics.html)
  - Wiki governance heuristics for splitting, merging, and deprecating documents apply to IFP specification evolution.
- relates_to::[\[\[Living Documents Over Static Publications\]\]](../principles/Living%20Documents%20Over%20Static%20Publications.html)
  - The living document principle grounds the argument for keeping tactical details revisable.
- relates_to::[\[\[Status Lifecycle Tracks\]\]](../models/Status%20Lifecycle%20Tracks.html)
  - IFP's Draft→Proposed→Active lifecycle is a maturity track comparable to garden stages.
