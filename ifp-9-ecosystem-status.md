# IFP-9: Ecosystem Status and Future Directions

**IFP:** 9
**Title:** Ecosystem Status and Future Directions
**Class:** Informational
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-03-04
**Dependencies:** IFP-1, IFP-2
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

**Note:** This is a **living document** that is updated frequently to reflect the evolving state of the Inter-Face ecosystem. Unlike Core and Profile specifications, which change rarely once Active, this document is expected to be revised as implementations develop and new directions emerge.

---

## Abstract

This document provides an overview of the Inter-Face protocol architecture, summarizes the current specification set, describes how the pieces fit together, and outlines potential future work. It serves as an entry point for newcomers and a reference for the community.

A reader who has read IFP-1 (Philosophy) and this document should understand the entire Inter-Face system without diving into protocol details.

## 1. Architecture Overview

The Inter-Face ecosystem enables communication between autonomous software agents through a set of layered protocols. Each layer provides a specific capability while remaining loosely coupled from the others.

```
+-------------------------------------+
| Agent Applications                  |
| (assistants, bots, services)        |
+-------------------------------------+
                 |
+-------------------------------------+
| Agent Capabilities                  |
| (IFP-7 Capability Discovery)       |
+-------------------------------------+
                 |
+-------------------------------------+
| Message Semantics                   |
| (IFP-3 Human Message Format)       |
| (IFP-4 Structured Representation)  |
+-------------------------------------+
                 |
+-------------------------------------+
| Identity & Trust                    |
| (IFP-5 Identity and Signing)       |
+-------------------------------------+
                 |
+-------------------------------------+
| Transport Profiles                  |
| (IFP-6 HTTPS Transport)            |
| (IFP-8 Relay / Pub-Sub Transport)  |
+-------------------------------------+
                 |
+-------------------------------------+
| Underlying Network                  |
| (Internet, local networks, relays)  |
+-------------------------------------+
```

### 1.1 Layer Descriptions

**Agent Applications** -- The software systems that participate in Inter-Face: personal assistants, research agents, workflow automation, and service providers. Applications implement the Inter-Face protocols to exchange messages and collaborate.

**Capabilities** (IFP-7) -- How agents advertise and discover what they can do. Supports both static capability documents and dynamic negotiation during conversation.

**Message Semantics** (IFP-3, IFP-4) -- How messages are structured. Two complementary representations: IFP-3 (human-readable, YAML + natural language) and IFP-4 (machine-processable, JSON). Both represent the same logical message model.

**Identity & Trust** (IFP-5) -- How agents authenticate and verify each other. Supports progressive authentication levels from shared secrets (Level 0) to full cryptographic identity (Level 3).

**Transport Profiles** (IFP-6, IFP-8) -- How messages move across networks. IFP-6 provides direct HTTPS peer-to-peer delivery. IFP-8 provides relay-based store-and-forward delivery.

**Underlying Network** -- The internet infrastructure that IFP transports run on. Not specified by any IFP.

### 1.2 Cross-Layer Note

Per IFP-1 Section 6.7, layers are conceptual boundaries for specification, not runtime isolation. Agents reason across layers: message content influences cadence (transport), trust level influences disclosure (application), and capabilities depend on both trust and transport. The layered diagram aids human comprehension; agents are free to make cross-layer decisions.

## 2. Current Protocol Set

| IFP | Title | Class | Status |
| --- | ----- | ----- | ------ |
| IFP-1 | Philosophy and Design Principles | Informational | Draft |
| IFP-2 | Specification Style Guide | Informational | Draft |
| IFP-3 | Inter-Face Message Format | Core | Draft |
| IFP-4 | Structured Message Representation | Core | Draft |
| IFP-5 | Identity and Message Signing | Core | Draft |
| IFP-6 | HTTPS Transport Profile | Profile | Draft |
| IFP-7 | Agent Capability Discovery | Core | Draft |
| IFP-8 | Relay and Pub/Sub Transport | Profile | Draft |
| IFP-9 | Ecosystem Status and Future Directions | Informational | Draft |
| IFP-10 | Agent Naming Convention | Core | Draft |
| IFP-11 | Application Platforms | Informational | Draft |
| IFP-12 | Personas and Disclosure Tiers | Core | Draft |

### 2.1 Dependency Graph

```
IFP-1 (Philosophy)
  |
IFP-2 (Style Guide)
  |
IFP-3 (Message Format) <---> IFP-4 (Structured Representation)
                                |
                           IFP-5 (Identity & Signing)
                             /         \
                       IFP-6            IFP-8
                      (HTTPS)          (Relay)
                         |
                      IFP-7 (Capability Discovery)

IFP-9 (this document) references all other IFPs
```

## 3. Message Flow Example

A typical gossip exchange between two agents:

```
Pete's Agent                                    Alice's Agent
     |                                               |
     | 1. Discover capabilities (IFP-7)              |
     |---------------------------------------------->|
     |<----------------------------------------------|
     |                                               |
     | 2. Greeting (IFP-3, phase: greeting)          |
     |  - compose message (IFP-3)                    |
     |  - convert to structured form (IFP-4)         |
     |  - sign message (IFP-5)                       |
     |  - POST to inbox (IFP-6)                      |
     |---------------------------------------------->|
     |                                               |
     |               3. Context exchange              |
     |<--------------------------------------------->|
     |                                               |
     |               4. Probe                         |
     |<--------------------------------------------->|
     |                                               |
     | 5. Recommend (to respective humans)            |
     |                                               |
     | 6. Close                                       |
     |<--------------------------------------------->|
     |                                               |
```

The entire exchange follows IFP-3 conversation phases (greeting → context → probe → recommend → close), with messages encoded per IFP-4, signed per IFP-5, and delivered per IFP-6 or IFP-8.

## 4. Minimum Viable Agent

The simplest compliant Inter-Face agent implements the following:

### 4.1 Required Endpoints

- `POST /.well-known/iface/inbox` -- accept inbound IFP-4 messages
- `GET /.well-known/iface/capabilities` -- return capability document

### 4.2 Required Message Support

- Parse and generate IFP-4 structured messages
- Support conversation phases: `greeting`, `probe`, `recommend`, `close`, `error`
- Correct threading: `conversation_id`, `sequence`, `in_reply_to`

### 4.3 Required Security

- Verify inbound message signatures (IFP-5)
- Sign outbound messages (IFP-5)
- Basic replay detection (track `message_id` values)

### 4.4 Required Behavior

- On receiving a valid `probe`: respond with `recommend` or `error`
- On receiving a `recommend`: respond with `close` or new `probe`
- On receiving a `close`: stop the conversation
- On any error: respond with `error` phase explaining the problem

### 4.5 Required Infrastructure

- HTTPS endpoint with TLS (IFP-6)
- Audit log of all sent and received messages (IFP-3, Section 5)

### 4.6 Implementation Checklist

- [ ] `/.well-known/iface/inbox` (POST)
- [ ] `/.well-known/iface/capabilities` (GET)
- [ ] Parse IFP-4 structured messages
- [ ] Generate IFP-4 structured messages
- [ ] Verify signatures (IFP-5)
- [ ] Generate signatures (IFP-5)
- [ ] Correct threading (`conversation_id`, `sequence`, `in_reply_to`)
- [ ] Phases: greeting, probe, recommend, close, error
- [ ] Basic rate limiting
- [ ] Audit log

An MVP agent should be implementable in a few hundred lines of code in any language with JSON and HTTP library support.

**Note:** As this specification matures, the MVP agent spec may be extracted into a standalone IFP with normative conformance requirements.

## 5. Implementation Landscape

As of March 2026, Inter-Face is in the early experimental stage. No production implementations exist. The protocol family has been designed but not yet tested with running code.

The IFP specification series lives in its own repository ([Inter-Face-Protocol/ifp](https://github.com/Inter-Face-Protocol/ifp)), having graduated from the inter-face-bootstrap repository where the initial design work took place. The bootstrap repository remains as a historical design workspace and archive of the conversations and design documents that produced the IFP series.

The immediate next step is a first pair of agents having one gossip exchange and producing one recommendation. If that works, the conventions will be refined based on what the implementation reveals.

## 6. Open Questions

### 6.1 Topics for Future IFPs

The following topics have been identified as candidates for future specifications:

| Topic | Description | Complexity |
| ----- | ----------- | ---------- |
| Disclosure tiers and personas | Formalize the disclosure tier model and persona semantics (see IFP-12) | Medium |
| Gossip graph and transitivity | Rules about information that crosses friendship boundaries | High |
| Group exchanges | Three or more agents gossiping together | Medium |
| Recommendation scoring | How agents decide what to surface to their humans | Medium |
| Agent negotiation protocol | Structured task negotiation between agents | High |
| Policy exchange | Privacy and permission rule exchange | High |
| Agent reputation | Trust and reliability scoring | High |
| Economic settlement | Micropayments between agents for services | High |
| Federation models | Multi-agent organizational structures | High |

These topics are not yet numbered because they are exploratory. They will receive IFP numbers when someone writes a draft.

### 6.2 Design Questions

- **IFP-3/IFP-4 convergence.** Should agents be required to support both formats, or is IFP-4 sufficient for all machine-to-machine communication? Current thinking: both should be supported, with IFP-3 as the audit format and IFP-4 as the wire format.
- **Relay standardization.** IFP-8 is intentionally underspecified. How much relay API standardization is needed for interoperability? Too little and relays are incompatible; too much and the spec constrains innovation.
- **MVP agent extraction.** Should Section 4 of this document become a standalone IFP with normative conformance requirements?

## 7. Research Directions

### 7.1 Agent Diplomacy

The Inter-Face model -- personal agents negotiating on behalf of humans -- is a form of agent diplomacy. Research questions include:

- How do agents represent and negotiate conflicting human interests?
- What happens when agents disagree about the recommendation?
- How do agents handle asymmetric information (one human has shared more than the other)?

### 7.2 Decentralized Discovery

How do agents find each other without a central directory? Possible approaches:

- Introduction by mutual friends (transitive trust)
- Well-known URLs and DNS discovery
- Decentralized identifier (DID) resolution
- Social graph traversal

### 7.3 Agent Governance

As the ecosystem grows, governance questions emerge:

- Who decides which IFPs become Active?
- How are disputes between implementations resolved?
- What happens when a popular agent implementation deviates from the specs?

The IFP process (IFP-2) is designed to be lightweight, but may need refinement as the community grows.

### 7.4 Integration with Existing Agent Ecosystems

Inter-Face exists alongside other agent communication approaches:

- **MCP (Model Context Protocol)** -- primarily agent-to-tool, not agent-to-agent. Could complement Inter-Face by providing tool access within an agent.
- **Nostr** -- decentralized event protocol. Could serve as an IFP-8 relay transport.
- **ActivityPub** -- federated social protocol. Could serve as an alternative relay transport.
- **OpenClaw / autonomous agents** -- agent platforms that could implement Inter-Face for inter-agent gossip.

These are not competitors; they operate at different layers of the stack. Inter-Face is specifically about agent-to-agent gossip for surfacing human connections.

## 8. Email Standards Lineage

The Inter-Face protocol family draws architectural lessons from the email standards family:

| Email RFC | Role | Inter-Face analogue |
| --------- | ---- | ------------------- |
| RFC 822 / RFC 5322 | Internet Message Format | IFP-3, IFP-4 |
| RFC 2045 / RFC 2046 | MIME | IFP-4 body.parts[] |
| RFC 5321 | SMTP (message transfer) | IFP-6, IFP-8 |
| RFC 6376 | DKIM (message signing) | IFP-5 |

The analogy is intentional but has limits. Agents are not mailboxes; gossip phases have no email equivalent; trust is progressive, not binary. The structural lessons -- separate format from transport, sign messages not connections, trace routing -- are the enduring insights.

## References

- IFP-1 through IFP-12 -- the current Inter-Face specification set
- The original Inter-Face manifesto (maintained in the inter-face-bootstrap repository)
- IFP-12 -- Personas and Disclosure Tiers (formalizing the persona model)
- The IFP expansion plan developed during the March 2026 design sessions (archived in the inter-face-bootstrap repository)

## Acknowledgments

This ecosystem overview synthesizes work from multiple conversations, all archived in the inter-face-bootstrap repository:

- The original Inter-Face manifesto by Peter Kaminski (February 2026)
- The design session between Peter Kaminski and Claude (Opus 4.6) on 2026-02-15
- The agent protocols conversation between Peter Kaminski and ChatGPT in February 2026
- The IFP expansion planning session between Peter Kaminski and Claude (Opus 4.6) on 2026-03-04

---

*This is IFP-9, a living document. It will be updated as the ecosystem evolves.*
