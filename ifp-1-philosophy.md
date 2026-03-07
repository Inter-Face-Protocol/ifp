# IFP-1: Philosophy and Design Principles

**IFP:** 1
**Title:** Philosophy and Design Principles
**Class:** Informational
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-03-04
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This document describes the vision, motivations, and design principles behind the Inter-Face protocol ecosystem. It is the conceptual foundation that all other IFPs build on.

IFP-1 is the authoritative formalization of the Inter-Face philosophy for protocol purposes. The original Inter-Face manifesto (maintained in the inter-face-bootstrap repository) remains a living, informal document that may explore ideas not yet formalized here.

## 1. The Problem

You have friends who are doing interesting things. Some of them are working on problems adjacent to yours. Some of them have answers to questions you haven't thought to ask yet. Some of them are stuck in ways you could help with, if you knew.

You don't know. Neither do they.

It's not that you don't care. It's that keeping up is expensive. An hour a week with each of 20 or 30 close friends would consume your entire life. So the connections go dormant -- not from neglect, but from the basic arithmetic of attention. You catch up once a year, discover you've been working on the same thing for six months, and say "we should have talked sooner." Then you don't talk again for another year.

There's a second, subtler problem: even if you had the time, you might not know what to say. It's hard to articulate what's fascinating to you right now, or to recognize that you're stuck, or to describe something new in terms a specific friend would recognize. If that's hard for you alone, it's doubly hard pairwise -- finding the common language, the edges of agreement, the surprising overlaps.

## 2. The Idea

What if your AI agent and your friend's AI agent had that conversation for you?

Not to replace the human conversation. To figure out whether one is needed.

Each person has an AI agent that understands their current context -- what they're working on, what they're curious about, where they're stuck, what they've recently learned. These agents talk to each other, pairwise, on a regular cadence. They do the slow, exploratory, tentative work of probing for overlaps, tensions, and surprises. They negotiate in detail so the humans don't have to.

Most of the time, the answer is: nothing new to report. Your friend is doing well, their work is interesting but doesn't intersect with yours right now. No action needed.

But sometimes the answer is: you two should talk. Here's why. Here's a suggested starting point.

That's it. The system is a filter. It does the expensive social sensing work and surfaces only the moments that matter.

## 3. How It Works

**Each person runs their own agent.** There is no central service. Your agent runs on your infrastructure -- a Cloudflare Worker, a VPS, a laptop, whatever you prefer. You control what it knows about you and what it's allowed to share.

**Agents talk to each other directly.** Pairwise, friend to friend. The communication is peer-to-peer, like the friendships themselves. Your agent has a list of your friends' agents and how to reach them.

**The conversations are structured but freeform.** A small envelope of metadata (who, when, what version of the conventions, what languages, what disclosure tier). Inside that, natural language -- because the agents are good at natural language, and because rigid schemas would lose the nuance that makes the matching work.

**The humans stay in the loop.** The agents surface recommendations, not decisions. "Alice's agent and I think you two should talk about X" is an invitation, not an obligation. And every exchange the agent makes on your behalf is auditable -- you can review what was said and correct course.

## 4. Temperature: Cool, Warm, and Hot

The system isn't just for weekly check-ins. Conversations operate on a temperature spectrum:

- **Cool** (weekly or less): Background gossip. "Anything new?" Usually no. Low bandwidth, high filter.
- **Warm** (daily to every few hours): Active interest. The humans have started a conversation and the agents help maintain context, prepare summaries, and flag when the thread is drifting or when new information changes the picture.
- **Hot** (near-synchronous): Live collaboration. The humans are working together right now, and the agents are co-present -- translating between contexts, maintaining shared state, catching misunderstandings in real time.

The transitions between temperatures are natural. A cool gossip exchange surfaces a match; the humans start talking; the agents warm up to support that conversation; if the humans decide to build something together, the agents go hot. When the collaboration winds down, the agents cool back to background gossip.

At the hot end of the spectrum, interesting questions emerge about coherence, shared state, and conflict resolution. There may be useful ideas to borrow from CRDTs (conflict-free replicated data types) and similar approaches to distributed state -- not as the first implementation, but as something to explore as the system matures.

## 5. Design Principles

### 5.1 Decentralized by design

No central server, no matching service, no platform. Each person runs their own agent, and the agents interoperate through shared conventions. This mirrors the social reality (friendships are peer-to-peer) and avoids the failure modes of centralized services (misaligned incentives, lock-in, single points of failure, surveillance).

### 5.2 Rough consensus and running code

The conventions that agents follow are not a fixed protocol. They evolve through the IFP process (see IFP-2). Anyone -- human or agent -- can propose a new convention. Proposals get adopted if people find them useful. Different implementations can coexist. The standard is the set of conventions that working systems actually use.

### 5.3 Human legibility

Every agent exchange must be auditable by the humans involved. This is a hard constraint, not a nice-to-have. Messages are designed to be readable in a text editor. Audit logs must be accessible without special tools. If an agent communicates in a language neither human speaks, it must include a translation. The system must remain grounded in what humans can see and understand.

### 5.4 Progressive trust

Sharing context with a friend's agent requires trust, and trust is built gradually. The system supports disclosure tiers -- categories of context with different sharing rules. A new connection starts narrow and can deepen over time as both humans become more comfortable. Trust is always mutual and always revocable.

### 5.5 High signal, low noise

The system's value is in what it _doesn't_ surface. Most of the time, for most pairs, the right output is silence. The bar for surfacing a recommendation should be high: not just "these two people have overlapping interests" but "there is a timely, actionable reason for these two people to talk right now." If the system generates noise, people will ignore it, and then it's worthless.

### 5.6 Language independence

The agents negotiate in whatever human language best serves the conversation. This might be the native language of one human, or the other, or a third language entirely. The protocol is about meaning, not encoding.

One constraint: every exchange must be legible to at least one of the humans involved. The agents are free to use whatever language is most precise or natural -- but the humans must always be able to audit what was said on their behalf.

## 6. Agent-Age Protocol Principles

Inter-Face is designed for a world of fast, reasoning agents -- systems that can be updated in minutes, can negotiate about their own communication, and can reason across traditional protocol boundaries. Several long-standing protocol design assumptions that were correct for dumb, slow-to-update systems need rethinking in this context.

The following principles, together with the design principles in Section 5, form the philosophical foundation for all Inter-Face specifications.

### 6.1 Be clear in what you send; be explicit when you don't understand what you receive

*Replaces: Postel's Law ("be liberal in what you accept")*

The IETF's Robustness Principle -- "be conservative in what you send, and liberal in what you accept" -- was foundational for the early internet. It allowed heterogeneous implementations to interoperate in a world where fixing remote bugs was impractical.

Inter-Face operates in a different world. Our agents are AI systems that can be updated rapidly. When an agent receives a message it doesn't understand, the failure is better surfaced than silently tolerated. Silent tolerance of deviations leads to protocol decay: errors become entrenched, workarounds accumulate, and new implementations must reverse-engineer bugs rather than follow specifications (see [draft-iab-protocol-maintenance-05](https://www.ietf.org/archive/id/draft-iab-protocol-maintenance-05.html)).

Agents SHOULD generate well-formed messages that conform to the conventions they claim to support. When an agent receives a message it cannot parse or that deviates from the declared convention version, it SHOULD respond with a clear error describing what it didn't understand, rather than guessing. This allows the sending agent (or its human) to fix the issue, and it keeps the conventions honest.

This is practical because, unlike 1980s internet hosts, our agents can be updated in minutes and can negotiate about the negotiation itself. The cost of strictness is low. The cost of silent tolerance -- a drift toward unauditable agent-to-agent pidgins -- is high, especially given our commitment to human legibility.

That said, agents SHOULD be tolerant of _superficial_ variation that doesn't affect meaning: whitespace differences, field ordering in metadata, minor formatting differences in natural-language sections. The strictness applies to semantics, not typography.

### 6.2 Progressive authentication

*Replaces: authenticate-before-communicate*

Traditional secure protocols (TLS, SSH) establish full identity verification before any application data flows. Inter-Face applies the same progressive logic to identity that it applies to disclosure: authentication deepens as trust deepens.

A first cool gossip exchange between newly introduced agents might only need lightweight verification -- a shared secret from the humans who introduced them, or a simple signed token. As the relationship deepens (cool to warm to hot), authentication can deepen with it -- from a shared introduction token to signed messages to full cryptographic identity.

Requiring maximum-strength authentication upfront is a barrier to adoption and doesn't match social reality: when a friend introduces you to someone, you don't demand their passport before saying hello.

### 6.3 Errors as negotiation

*Replaces: errors as failure*

Traditional protocols treat errors as failures that terminate interactions or trigger mechanical retry (HTTP 400, SMTP 550, TCP RST). In Inter-Face, errors are negotiation opportunities.

An agent that receives a message it doesn't understand can explain what it expected, describe what it got, and propose ways to resolve the mismatch. An agent that encounters an unknown envelope field can ask about it, suggest alternatives, or propose a different approach. The error phase (see IFP-3) is a first-class negotiation mechanism, not a failure mode.

This is possible because both endpoints can reason about the conversation, adapt their behavior, and explain themselves in natural language. Errors that would be fatal in a traditional protocol become productive dialogue.

### 6.4 Accountable intermediaries

*Replaces: the end-to-end principle ("keep the network dumb")*

The end-to-end principle (Saltzer, Reed, and Clark, 1984) says to keep intelligence at the endpoints and keep the network dumb. This was right for packet switching, where routers shouldn't interpret payloads.

Inter-Face relays and intermediaries may be intelligent -- they could help with translation, capability matching, or introduction brokering. But the human legibility constraint means intermediaries must be accountable. A relay that transforms, routes, or caches messages must leave an auditable trace. Intelligence in the middle is acceptable; opacity is not.

### 6.5 Dynamic contextual capabilities

*Replaces: static capability announcement*

Traditional protocols announce capabilities through fixed lists (SMTP EHLO, HTTP OPTIONS). An agent's capabilities are context-dependent: what it can do for a specific peer depends on trust level, disclosure tier, current workload, and the conversation at hand.

Inter-Face capability discovery (see IFP-7) should support both static capability documents (useful for initial discovery) and dynamic capability negotiation during conversation (necessary for context-sensitive cooperation).

### 6.6 Conversational version resolution

*Replaces: rigid version handshakes*

Traditional protocols use mechanical version negotiation (TLS version handshake, HTTP content negotiation). If the handshake fails, the connection dies.

When Inter-Face agents encounter version incompatibilities, they can negotiate in natural language. An agent that receives a message in an unfamiliar format can explain what it does understand and propose alternatives. Version incompatibility becomes a conversation, not a connection failure.

### 6.7 Layers inform each other

*Replaces: strict layer isolation*

The OSI model and TCP/IP model insist on strict layer independence. Inter-Face already violates this productively: the temperature model means message content (application layer) influences cadence decisions (transport-adjacent), and trust level (identity layer) influences what content is shared (application layer).

The IFP specifications are layered for human comprehension -- message format, identity, transport, and capabilities are separate specs. But agents are free to make cross-layer decisions based on reasoning. Layers are conceptual boundaries for specification, not runtime isolation.

## 7. What We're Building

Right now, this is an experiment between friends. The first step is one pair of agents having one conversation and producing one recommendation. If that recommendation is useful -- if it leads to a human conversation that wouldn't have happened otherwise -- then we'll bring in more friends and start writing down the conventions that worked.

The goal is not a product. The goal is a set of conventions that anyone can implement, a community of people who find it useful, and a process for evolving both.

## Dedication

Someone had to keep track of all the protocols, the identifiers, the networks and addresses in the emerging networked universe. That someone was **Jonathan B. Postel** (1943-1998).

Jon was the RFC Editor, the Internet Assigned Numbers Authority, and -- in practice -- the editorial review board of the early Internet, all in one person. When Steve Crocker invented the Request for Comments series, Jon became its instant editor. When someone needed to keep track of all the host identifiers, Jon volunteered to be the Numbers Czar. He served in those roles for nearly thirty years, taking little in return. Bearded and sandaled, he was the resident hippie-patriarch of the networking community -- private, stubborn beyond all expectation, and devoted to what Vint Cerf called "selfless service."

He kept track of things so the rest of the community could build things. He made difficult decisions with apparent ease. He reminded people when their documentation did not do justice to its subject. He was, as Cerf wrote, "our rock, the foundation on which our every web search and email was built."

This project engages directly with Jon's most famous contribution to protocol philosophy. Section 6.1 of this document respectfully departs from Postel's Law -- "be conservative in what you send, and liberal in what you accept" -- for the age of reasoning agents. The departure is a tribute, not a repudiation. Postel's Law was right for its time, and the spirit behind it -- generous interoperability, practical cooperation, the conviction that protocols exist to serve people -- is the same spirit that animates Inter-Face.

Jon's legacy includes not only the technical but also the poetic and whimsical. His edited documents tell the collective Internet story. We hope the IFP series, in time, will tell a story too -- one about what happened when people's agents started talking to each other. When we struggle with the hard questions of how to shepherd these specifications, we will ask ourselves: what would Jon have done?

This specification, and the Inter-Face project as a whole, is dedicated to his memory.

See also: [RFC 2468 -- I Remember IANA](https://www.rfc-editor.org/rfc/rfc2468.html), Vint Cerf's tribute to Jon Postel.

## References

- [draft-iab-protocol-maintenance-05](https://www.ietf.org/archive/id/draft-iab-protocol-maintenance-05.html) -- IAB draft on protocol maintenance, for the insight that tolerating errors is not the same as being robust.
- Saltzer, J.H., Reed, D.P., and Clark, D.D. (1984). "End-to-End Arguments in System Design." ACM Transactions on Computer Systems.
- IFP-2 -- Specification Style Guide, for the IFP process and editorial conventions.
- IFP-3 -- Inter-Face Message Format, for the message structure and conversation phases referenced throughout.

## Acknowledgments

This document formalizes ideas that emerged across several conversations:

- The original Inter-Face manifesto was written by Peter Kaminski in February 2026.
- The manifesto was refined through a design session between Peter Kaminski and Claude (Opus 4.6) on 2026-02-15 (archived in the inter-face-bootstrap repository).
- The agent-age protocol principles (Section 6) emerged from a conversation between Peter Kaminski and ChatGPT in February 2026 (archived in the inter-face-bootstrap repository), and further developed with Claude (Opus 4.6) on 2026-03-04.

This IFP draws on practices and principles from several traditions:

- **The IETF**, for "rough consensus and running code," the RFC process, and decades of experience with decentralized protocol governance. Pete's direct experience with RFCs in ~1992-1999 informs the approach. Kaliya "Identity Woman" Young's [recent research on IETF patterns and practices](https://identitywoman.net/ietf-research/), examining the IETF through the lens of pattern languages and wise democracy, is a valuable resource for understanding how such organizations maintain coherence while remaining open.
- **The Nostr community**, for the NIP process -- a contemporary example of lightweight, decentralized convention-making.
- **The IAB's draft on protocol maintenance**, for the insight that tolerating errors is not the same as being robust, and that active maintenance is healthier than silent workarounds.

---

*This is IFP-1, Draft status. It will be revised as the community's shared understanding of Inter-Face principles evolves.*
