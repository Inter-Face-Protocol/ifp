---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Analysis of how the minimum viable architecture principle applies to Inter-Face Protocol's design decisions — distinguishing load-bearing architectural choices from tactical decisions that could be deferred or changed."
tagline: "Which IFP decisions are load-bearing architecture and which are deferrable tactical choices?"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Analysis: Minimum Viable Architecture Applied to Inter-Face Protocol

## MVA vs MVP

Minimum viable architecture is often confused with minimum viable product, but they answer different questions. MVP asks: *what is the minimum product we can ship to learn from users?* MVA asks: *what architecture will support changes as we learn?*

MVP optimizes for speed to market — build the smallest thing, ship it, iterate based on feedback. MVA optimizes for adaptability — commit to the few decisions that are hard to reverse, and deliberately leave everything else open so implementations can explore, fail cheaply, and converge on what works.

The distinction matters for protocol design. A protocol built on MVP thinking specifies everything at once (ship the spec, see what happens). A protocol built on MVA thinking specifies the load-bearing architecture and explicitly marks the rest as open for exploration. The first approach risks premature commitment; the second risks insufficient interoperability. The right balance depends on which decisions are hard to reverse.

## Load-Bearing Decisions (Hard to Reverse)

These are the decisions that would reshape the protocol if changed. They are the minimum viable architecture:

**Gossip-as-filter framing** (IFP-1). The entire protocol exists to filter attention, not to connect people. Changing this would make IFP a different system.

**Temperature model** (IFP-1). Cool/warm/hot cadence shapes rate limiting, capability availability, and escalation patterns across every spec. Removing temperature would require redesigning the protocol stack.

**Human legibility constraint** (IFP-1). Every agent action must be auditable by a human in a text editor. This rules out binary formats, opaque compression, and any exchange that is not human-readable. Relaxing this constraint would fundamentally alter the trust model.

**Agent-age protocol principles** (IFP-1). The seven principles — especially replacing Postel's Law with clarity-over-tolerance — commit IFP to a design philosophy that shapes error handling, version negotiation, and capability discovery across every spec.

**Conversation phase model** (IFP-3). Greeting → context → probe → recommend → close → error is the social backbone of every exchange. Changing the phases would require rewriting IFP-3, IFP-9, IFP-11, and IFP-12.

**Dual representation architecture** (IFP-3/4). Human-readable YAML+NL paired with machine-processable JSON. Removing either representation would break either human legibility (losing IFP-3) or cryptographic operations (losing IFP-4).

**Progressive trust model** (IFP-5/12). Authentication and disclosure deepen together. Flattening this to binary (trusted/untrusted) would eliminate progressive authentication, disclosure tiers, and much of the persona model.

## Tactical Decisions (Easy to Change)

These are implementation choices that could be refined without reshaping the protocol:

- **Specific envelope field names** (IFP-3/4) — renaming `disclosure` to `sharing_level` changes no semantics
- **Rate limiting defaults** (IFP-6) — 10 msg/min cool, 60 msg/min hot are heuristics, not architecture
- **Message size limit** (IFP-6) — 1 MB is a reasonable default, not a design commitment
- **Endpoint paths** (IFP-6) — `/.well-known/iface/inbox` follows convention but could change
- **Retry backoff schedule** (IFP-6) — exponential backoff parameters are tuning, not design
- **Relay persistence duration** (IFP-8) — 7 days is a default, not an invariant

## Uncertain Decisions

Some decisions sit between architectural and tactical. The inquiries in this garden patch examine these:

- **Four authentication levels** — Are the boundaries between levels load-bearing or refinable? (See [\[\[Granularity of Progressive Authentication Stages\]\]](../../inquiries/Granularity%20of%20Progressive%20Authentication%20Stages.html))
- **Six disclosure tiers** — Are the tier names and count architectural or conventional? (See [\[\[Disclosure Spectrum as Discrete Tiers or Continuous Range\]\]](../../inquiries/Disclosure%20Spectrum%20as%20Discrete%20Tiers%20or%20Continuous%20Range.html))
- **Six conversation phases** — Is the phase decomposition load-bearing or refinable? (See [\[\[Social Phase Decomposition in Trust-Building Protocols\]\]](../../inquiries/Social%20Phase%20Decomposition%20in%20Trust-Building%20Protocols.html))
- **Natural language bodies** — Is NL-for-bodies a minimum viable architecture choice or a deferrable bet? (See [\[\[Structured Schema vs Natural Language for Agent Message Content\]\]](../../inquiries/Structured%20Schema%20vs%20Natural%20Language%20for%20Agent%20Message%20Content.html))
- **Eleven application platforms** — Are these architectural categories or illustrative examples? (See [\[\[Organizing Principle for Agent Application Domains\]\]](../../inquiries/Organizing%20Principle%20for%20Agent%20Application%20Domains.html))

## Sources

- [\[\[Allen (2023) Minimum Viable Architecture\]\]](Allen%20%282023%29%20Minimum%20Viable%20Architecture.html) — the source principle
- [IFP-1 through IFP-12](../../) — the decisions being analyzed
