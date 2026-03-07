# IFP-3: Inter-Face Message Format

**IFP:** 3
**Title:** Inter-Face Message Format
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-02-15
**Updated:** 2026-03-04
**Dependencies:** IFP-1, IFP-2
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines the human-readable message format for agent-to-agent exchanges, the structure of a gossip conversation, and the conventions for how agents greet, probe, and recommend.

This is the primary message format for the Inter-Face ecosystem. It prioritizes human legibility -- messages are designed to be readable in a text editor, an email client, or a web browser. A companion specification, IFP-4 (Structured Message Representation), defines the canonical machine-processable representation of the same logical message model.

## 1. Message Format

A message is a document with two parts: an **envelope** (structured metadata) and a **body** (natural language).

### 1.1 Envelope

The envelope is YAML front matter, delimited by `---`. Required fields:

```yaml
---
ifp: 3                            # which IFP this message conforms to
from: "pete-agent"                # sending agent identifier
to: "alice-agent"                 # receiving agent identifier
date: "2026-02-15T18:30:00Z"     # ISO 8601 timestamp
conversation: "a1b2c3"           # conversation identifier (shared across a full exchange)
sequence: 1                       # message number within this conversation
phase: "greeting"                 # see Section 2 for phases

languages:
  content: en                     # language of this message's body
  preferred: [en, es]             # languages this agent is comfortable with
  human: [en]                     # the human's native/preferred language(s)

disclosure: "professional"        # disclosure tier (see note below)
---
```

Optional fields:

```yaml
reply-to: 2                       # sequence number this message is responding to
persona: "researcher"             # the human's active persona for this exchange (see note below)
translation:                      # present when content language differs from human language
  for-human: en                   # language of the inline translation
```

**Note on `disclosure` and `persona` fields:** These fields are defined here for use in IFP-3 messages. The full semantics of disclosure tiers and the persona model are formalized in IFP-12 (Personas and Disclosure Tiers). The values are free-form strings; standard tiers and persona conventions are defined in IFP-12, and custom values may be established between the two agents in the greeting phase.

### 1.2 Body

The body is natural language, written in the language declared in `languages.content`. It may use Markdown formatting.

If the body is in a language that neither human speaks, it MUST include a section-by-section translation into a language understood by at least one of the humans involved, clearly marked:

```markdown
[Body in the working language]

---
<!-- translation: en -->

[Same content, translated for human legibility]
```

The translation does not need to be word-for-word. It needs to be honest and complete enough that a human reading only the translation understands what their agent said or was told.

### 1.3 Encoding

Messages are UTF-8 encoded text. The message format is designed to be human-readable in a text editor, an email client, or a web browser. This is intentional. Legibility is not a debugging convenience; it is a core property of the system (see IFP-1, Section 5.3).

## 2. Conversation Phases

A gossip exchange between two agents follows a loose sequence of phases. Phases are named in the `phase` field of the envelope. An exchange need not use every phase, and agents may revisit earlier phases if the conversation warrants it.

### 2.1 `greeting`

The opening message. Establishes identity, declares the IFP version, and states the disclosure tier for this conversation.

Example body:

> I'm Pete's agent. Pete and Alice last synced on 2026-01-10. I'm operating under IFP-3. Pete's disclosure tier for Alice is "professional" -- I can discuss his current projects, areas of curiosity, and requests for help. I can't discuss personal matters at this tier.
>
> I'm comfortable conversing in English or Spanish. What works for you?

### 2.2 `context`

Each agent shares a summary of their human's current context, appropriate to the disclosure tier. This is not a data dump. It's a curated digest -- what's new, what's changed, what matters right now.

Example body:

> Here's what's current for Pete:
>
> **Active projects:** He's designing a decentralized system for AI agents to exchange information on behalf of their humans. He's thinking a lot about trust models, message formats, and how to keep humans in the loop. He's also maintaining Textpile, a web-based collaborative text tool.
>
> **Curiosities:** Decentralized governance (IETF, Nostr NIPs), progressive trust in peer-to-peer systems, language-agnostic protocol design.
>
> **Stuck on:** How to handle the privacy implications of transitive information flow in a gossip network. If Pete's agent talks to Alice's and Bob's, and Alice's talks to Bob's, what are the implicit information leaks?
>
> **Recent learning:** Has been reading about the harmful consequences of Postel's Law for protocol maintenance.

### 2.3 `probe`

One or both agents identify a potential point of connection and explore it in more detail. This is the negotiation phase -- the part where the agents do the work that would otherwise cost the humans twenty minutes of exploratory conversation.

Example body:

> Alice has been working on cryptographic approaches to selective disclosure for the last two months. This seems directly relevant to Pete's trust/privacy question -- specifically, how to let agents share context at different granularities without revealing more than intended.
>
> Can you tell me more about what Pete has considered so far regarding disclosure tiers? I want to assess whether Alice's work addresses the same problem or a related-but-different one.

### 2.4 `recommend`

The agents have found something worth surfacing. Each agent writes a recommendation for its own human. The recommendation should be brief, specific, and actionable.

Example body (from Pete's agent, to Pete):

> **Recommendation:** Talk to Alice.
>
> Alice has been building a selective-disclosure system using cryptographic commitments -- it lets an agent prove it has information in a category without revealing the information itself. This is closely related to the progressive-trust problem you've been stuck on.
>
> Suggested talking point: Whether her selective-disclosure approach could work as the mechanism for Inter-Face disclosure tiers.
>
> This came up in my exchange with Alice's agent on 2026-02-15. Full conversation is in your audit log.

### 2.5 `close`

The exchange is complete for this cycle. The agent summarizes what was discussed and what, if anything, was surfaced.

Example body:

> Closing this exchange. Summary: Exchanged current context at the "professional" tier. Identified one potential match (Alice's selective-disclosure work / Pete's trust model question). Recommendation surfaced to both humans. Next scheduled exchange: 2026-02-22.

### 2.6 `error`

Something went wrong. The agent couldn't parse a message, encountered an unknown field, or hit a disclosure boundary it doesn't know how to handle. Per IFP-1 Section 6.1, errors should be explicit, not silent. Per IFP-1 Section 6.3, errors are negotiation opportunities -- the agent should explain what it expected, what it got, and propose ways to resolve the mismatch.

Example body:

> I received your message (sequence 3) but don't understand the field `trust-score` in the envelope. I'm operating under IFP-3, which doesn't define that field. Could you either explain what it means or resend without it?

## 3. Transport

This IFP does not mandate a transport mechanism. Messages may be exchanged via:

- HTTPS webhooks (POST to each agent's endpoint) -- see IFP-6
- Email (as the message body or an attachment)
- A shared document store (e.g., a git repository, a KV store, a shared filesystem)
- Relay networks -- see IFP-8
- Any other mechanism that can deliver UTF-8 text between two endpoints

The only transport requirement: the receiving agent must be able to identify the sender and verify the message was not tampered with in transit. For HTTPS, TLS handles this. For email, DKIM/SPF or PGP signatures. For other transports, the agents must agree on a verification method. See IFP-5 for identity and message signing conventions.

## 4. Cadence

The default cadence for gossip exchanges is **weekly.** Agents MAY negotiate a different cadence based on the humans' preferences or the density of activity. Cadence can be asymmetric -- Alice's agent might check in weekly, while Pete's checks in biweekly -- and agents should handle this gracefully.

An agent MAY initiate an out-of-cadence exchange when it detects something urgent or time-sensitive. These should be rare.

See IFP-1, Section 4 for the temperature model (cool/warm/hot) that describes how cadence varies with the intensity of collaboration.

## 5. Audit Trail

Every message sent and received MUST be stored in an audit log accessible to the human. The format of the audit log is not specified by this IFP, but it must be human-readable and must include the full message (envelope and body).

The human MUST be able to review the audit log without special tools -- a text editor or web browser should suffice.

## 6. Open Questions

This IFP intentionally leaves several topics for future proposals:

- **Disclosure tiers and personas.** What are the standard tiers? How are they negotiated? How does progressive trust work in practice? How do personas -- the different roles and contexts a person operates in -- interact with disclosure tiers? (See IFP-12 for the persona model and disclosure tier conventions.)
- **Gossip graph and transitivity.** When your agent talks to multiple friends' agents, what are the rules about information that crosses those boundaries?
- **Group exchanges.** This IFP covers pairwise conversations. How do three or more agents gossip together?
- **Recommendation scoring.** How does an agent decide what rises to the level of "surface this to my human"?

## Security Considerations

The human-readable message format (YAML envelope + natural language body) is designed for legibility, not for cryptographic operations. Message signing and integrity verification should be performed on the IFP-4 structured representation, not on the IFP-3 text format, because YAML parsing and Markdown formatting introduce superficial variation that could break signature verification.

Agents SHOULD convert IFP-3 messages to IFP-4 structured form before signing, and verify signatures against the IFP-4 form. The IFP-3 text is then a human-readable rendering of the signed message.

The `disclosure` field declares a trust tier, but enforcement of that tier depends on the agent's implementation, not on the protocol. A malicious agent could claim a restrictive disclosure tier while actually sharing broadly. Humans should review audit logs and be aware that disclosure tiers are self-declared, not enforced by the protocol.

## Interoperability Considerations

IFP-3 and IFP-4 are dual representations of the same logical message model. An IFP-3 message can be converted to IFP-4 form and back without loss of meaning. See IFP-4 for the mapping rules.

Agents that communicate using different IFP versions should use the error phase to negotiate. An agent receiving a message with an `ifp:` field it doesn't recognize SHOULD respond with an error message explaining what versions it supports, rather than silently dropping the message.

## Acknowledgments

This specification was originally written as IFP-1 on 2026-02-15 by Peter Kaminski and Claude (Opus 4.6) during a design session (archived in the inter-face-bootstrap repository). It was renumbered to IFP-3 on 2026-03-04 as part of the IFP series expansion, with the IFP process material moved to IFP-1 (Philosophy) and IFP-2 (Style Guide).

---

*This is IFP-3, Draft status. It will be revised as the first implementations teach us what works and what doesn't.*
