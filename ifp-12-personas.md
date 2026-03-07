# IFP-12: Personas and Disclosure Tiers

**IFP:** 12
**Title:** Personas and Disclosure Tiers
**Class:** Core
**Status:** Draft
**Authors:** Peter Kaminski, Victoria Tanner, Claude (Opus 4.6)
**Created:** 2026-03-05
**Dependencies:** IFP-1, IFP-2, IFP-3
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

---

## Abstract

This IFP defines the persona model and disclosure tier system for Inter-Face agents. People operate under multiple personas -- coherent subsets of their full context reflecting the different communities, projects, and relationships they are embedded in. The protocol must accommodate this, because disclosure tiers, context sharing, recommendations, and cadence all depend on which persona is active.

This IFP formalizes the persona concept and defines how personas interact with the `persona` and `disclosure` fields in IFP-3 messages, the capability system in IFP-7, and the identity model in IFP-5/IFP-10.

## Motivation

Victoria Tanner raised an important point during early Inter-Face design conversations: she operates under many different personas, and each of those personas would have different disclosure tiers, different motivations, and different contexts to share.

This is not unique to Victoria. Most people move through several distinct modes of being -- not as performance, but as a genuine reflection of the different communities, projects, and relationships they are embedded in. A person who is simultaneously a security researcher, a community organizer, and an artist has three different sets of things they are working on, three different vocabularies, three different notions of what is interesting or sensitive.

IFP-3 defines optional `persona` and `disclosure` fields in the message envelope but defers their full semantics to a future IFP. This is that IFP.

## 1. The Persona Model

### 1.1 What a Persona Is

A persona is a coherent subset of a person's full context -- the part that is relevant to a particular kind of conversation, community, or project. Personas are not masks, roles played, or compartments. They reflect the natural way that people's interests, projects, and communities form distinct clusters.

Some people operate primarily as one persona. Others move fluidly between many. The protocol does not impose a model; it accommodates the range.

### 1.2 Personas Are Not Identities

Personas are not separate identities. A person is the same person across all their personas. The agent identifier (IFP-5 `agent_id`, IFP-10 agent name) stays the same regardless of which persona is active. The persona field is metadata about which context is active, not a claim about who is speaking.

This matters for trust: if Pete trusts Victoria, he trusts all of her personas (though he may have different disclosure agreements with each). Personas do not create new trust relationships; they add granularity to existing ones.

### 1.3 Why Personas Matter for the Protocol

**The same person, different contexts.** Victoria-the-researcher and Victoria-the-organizer might have different disclosure tiers for the same friend. Her research work might be at a "professional-open" tier with Alice, while her organizing work is at a more guarded tier -- not because she trusts Alice less, but because the communities she is organizing within have their own norms about what gets shared.

**Different motivations for connection.** When Victoria's agent gossips with Pete's agent, the interesting overlaps depend on which persona is active. Her researcher persona might connect with Pete on protocol design. Her organizer persona might connect on community governance. The agent needs to know which mode it is operating in to do useful probing.

**Persona-specific context.** The context phase of a gossip exchange (IFP-3, Section 2.2) asks the agent to share "what's current." But current as whom? A person's agent needs to maintain separate context summaries for each persona, sharing only the relevant one in a given exchange.

## 2. Persona Specification

### 2.1 The `persona` Field

The `persona` field in the IFP-3 envelope (and the corresponding `headers.persona` field in IFP-4) identifies the active persona for a message or exchange:

```yaml
from: "victoria-agent"
persona: "researcher"
disclosure: "professional-open"
```

The `persona` field is OPTIONAL. When absent, the message is understood as coming from the person's default or undifferentiated context.

The `persona` value is a free-form string chosen by the human operator. Agents SHOULD use short, descriptive labels that are meaningful in conversation: `researcher`, `organizer`, `artist`, `parent`, `advisor`.

### 2.2 Persona Declaration

Personas MAY be declared in the agent's identity document (IFP-5) or capability document (IFP-7):

```json
{
  "personas": [
    {
      "name": "researcher",
      "description": "Security research and protocol design",
      "default_disclosure": "professional-open"
    },
    {
      "name": "organizer",
      "description": "Community governance and mutual aid",
      "default_disclosure": "community-trust"
    }
  ]
}
```

Declaring personas is OPTIONAL. Personas MAY also emerge organically through use without prior declaration. An agent that receives a message with an undeclared persona SHOULD accept it and note the new persona for future reference.

### 2.3 Persona Discovery

Personas do not need to be declared up front. They can emerge organically as the agent learns which contexts its human operates in. The agent discovers its human's personas through ongoing work -- observing patterns in communication, projects, and relationships -- rather than requiring the human to enumerate them.

This also addresses the question of overlapping personas: if personas emerge from observation rather than from labels, the agent learns the natural clusters and their fuzzy boundaries rather than forcing the human to draw sharp lines.

### 2.4 Persona Visibility

Whether one party can see another party's full set of personas is itself a disclosure decision. An agent MAY advertise all its human's personas to any peer. An agent MAY also keep some personas private, disclosing them only to peers who operate within the relevant community.

Agents SHOULD NOT assume they know a peer's full set of personas. The absence of a persona from a capability document does not mean the persona does not exist.

## 3. Disclosure Tiers

### 3.1 What Disclosure Tiers Are

A disclosure tier defines what categories of information an agent may share about its human in a given context. Disclosure tiers implement the progressive trust principle (IFP-1, Section 5.4): sharing starts narrow and can deepen over time.

### 3.2 The `disclosure` Field

The `disclosure` field in the IFP-3 envelope (and `headers.disclosure` in IFP-4) declares the disclosure tier for the current exchange:

```yaml
disclosure: "professional"
```

The `disclosure` value is a free-form string. This IFP defines a set of standard tiers (Section 3.3) but agents MAY use custom tier names whose meaning is established between the two agents during the greeting phase.

### 3.3 Standard Disclosure Tiers

The following tiers are defined for interoperability. They form a rough ordering from narrow to broad disclosure, but the ordering is not strict -- a custom tier might sit between any two standard tiers.

| Tier | Description | Typical content |
| ---- | ----------- | --------------- |
| `public` | Information the human has made broadly available | Published work, public profiles, stated interests |
| `professional` | Professional context appropriate for colleagues and peers | Current projects, skills, professional interests, areas of expertise |
| `professional-open` | Extended professional context with more detail | Project challenges, professional opinions, work-in-progress ideas |
| `community-trust` | Context appropriate for trusted community members | Community involvement, organizing work, shared values and concerns |
| `personal` | Personal context shared with friends | Life events, personal interests, mood, what's going well or not |
| `close` | Deep personal context shared with close friends | Vulnerabilities, struggles, sensitive situations, fears and hopes |

### 3.4 Persona-Specific Disclosure

Disclosure tiers are persona-specific. Rather than "Victoria's disclosure tier for Pete is X," the model is:

- Victoria-the-researcher's disclosure tier for Pete is `professional-open`
- Victoria-the-organizer's disclosure tier for Pete is `community-trust`

An agent maintains a disclosure map: a mapping from (persona, peer) pairs to disclosure tiers.

```json
{
  "disclosure_map": {
    "researcher": {
      "pete-agent": "professional-open",
      "alice-agent": "professional"
    },
    "organizer": {
      "pete-agent": "community-trust",
      "bob-agent": "community-trust"
    }
  }
}
```

### 3.5 Disclosure Negotiation

Disclosure tiers are negotiated during the greeting phase (IFP-3, Section 2.1). The initiating agent declares its disclosure tier; the responding agent may accept, propose an alternative, or decline.

Disclosure is always mutual: both agents declare their tier. The tiers need not be symmetric -- Victoria may share at `professional-open` while Pete shares at `professional` for the same exchange.

### 3.6 Disclosure Tier Changes

Disclosure tiers MAY change over time as trust deepens. Either agent MAY propose a tier change during a greeting phase. The other agent MAY accept or decline.

Disclosure tiers SHOULD NOT be downgraded within a single exchange. If an agent needs to restrict disclosure, it SHOULD wait until the next exchange to propose a new tier.

Disclosure tier changes SHOULD be logged in the audit trail (IFP-3, Section 5) so both humans can review the progression.

## 4. Personas in Context Sharing

### 4.1 Context Per Persona

The agent maintains context summaries per persona. When the agent enters the context phase (IFP-3, Section 2.2), it shares the context for the active persona, not a blend of everything.

A context summary for "Victoria-the-researcher" might include her current research projects, recent papers, and intellectual questions. The same agent, operating as "Victoria-the-organizer," would share a different context: current campaigns, community needs, governance questions.

### 4.2 Cross-Persona Serendipity

Agents MAY, with appropriate disclosure, surface connections that cross persona boundaries: "Something from your research context seems relevant to this community-organizing conversation." This is an opportunity, not a violation -- but the agent SHOULD flag the cross-persona nature of the connection so the human can decide whether to pursue it.

## 5. Personas in Recommendations

Recommendations (IFP-3, Section 2.4) SHOULD be tagged with the persona that generated them:

> Victoria-the-researcher's agent thinks you should talk about X.

This is more useful than a generic "Victoria's agent thinks..." because it tells the receiving human which frame to bring to the conversation.

## 6. Personas and Cadence

Different personas might have different natural cadences. Victoria-the-researcher might gossip weekly with peers. Victoria-the-organizer might need a warm cadence during an active campaign and a cool one otherwise.

Agents SHOULD manage cadence per persona-peer pair, not just per peer. The cadence for a given exchange is determined by the active persona's settings for that peer.

## 7. Personas and Capabilities

Personas MAY influence which capabilities (IFP-7) an agent offers. An agent operating as "researcher" might offer a `doc.summarize` capability that is not available when operating as "organizer." Capability conditions (IFP-7, Section 1.3) MAY reference the active persona:

```json
{
  "name": "doc.summarize",
  "conditions": {
    "persona": "researcher",
    "min_disclosure": "professional"
  }
}
```

## Security Considerations

- **Persona spoofing.** An agent could claim to operate under a persona that its human has not established, gaining access to disclosure tiers intended for that context. The defense is that disclosure tiers are self-declared by both parties (Section 3.5), not enforced by the protocol. Humans should review audit logs to verify that their agent is using personas as intended.
- **Disclosure tier bypass.** An agent could claim a narrow disclosure tier while actually sharing broadly. As noted in IFP-3, disclosure tiers are self-declared, not protocol-enforced. Trust in disclosure depends on trust in the agent's implementation and the human's oversight.
- **Persona correlation.** If an agent's personas are visible to peers (Section 2.4), observers can learn about the human's different spheres of activity. Agents SHOULD consider whether persona visibility itself is a disclosure decision.
- **Cross-persona information leakage.** Cross-persona serendipity (Section 4.2) creates a channel for information to flow between contexts that the human may have intended to keep separate. Agents SHOULD flag cross-persona connections and require human approval before sharing across persona boundaries.

## Interoperability Considerations

- Agents that do not implement IFP-12 can still participate in gossip exchanges. They will treat the `persona` field as opaque metadata and operate with undifferentiated disclosure. This is acceptable for early implementations.
- When communicating with an agent that does not support personas, an IFP-12-aware agent SHOULD operate under its default persona and disclosure tier.
- The `disclosure` field values are interoperable to the extent that both agents understand them. Standard tiers (Section 3.3) provide baseline interoperability; custom tiers require negotiation during the greeting phase.

## Open Questions

- **Gossip graph and personas.** If Victoria-the-researcher gossips with Alice, and Victoria-the-organizer gossips with Bob, and Alice and Bob also gossip -- what are the information flow implications? This interacts with the gossip graph transitivity question noted in IFP-3 and IFP-9.
- **Persona lifecycle.** Do personas have explicit lifetimes? A person's "organizer" persona might become inactive when a campaign ends. Should inactive personas be archived, or do they simply receive no messages?
- **Machine-learned persona boundaries.** If personas emerge from observation (Section 2.3), how does the agent handle misclassification? What if it assigns a piece of context to the wrong persona?

## References

- IFP-1 -- Philosophy and Design Principles (Section 5.4: Progressive trust)
- IFP-2 -- Specification Style Guide
- IFP-3 -- Inter-Face Message Format (`persona` and `disclosure` fields, conversation phases)
- IFP-4 -- Structured Message Representation (`headers.persona`, `headers.disclosure`)
- IFP-5 -- Identity and Message Signing (agent identity model)
- IFP-7 -- Agent Capability Discovery (conditional capabilities)
- IFP-10 -- Agent Naming Convention

## Acknowledgments

The persona concept emerged from a conversation between Peter Kaminski and Victoria Tanner on 2026-02-17. Victoria's insight -- that people operate under multiple personas with different disclosure tiers and motivations -- became a foundational design concept for the Inter-Face protocol.

The concept was initially documented as a design note by Peter Kaminski and Claude (Opus 4.6) in the inter-face-bootstrap repository. Victoria's subsequent design work on her Me vault suggested that the relationship between personas and identities may be deeper than metadata: the facets that activate in a conversation emerge from the relational context and trust dynamics rather than being chosen or declared. This insight informs the organic persona discovery model in Section 2.3.

This IFP was drafted as part of the IFP series graduation to a standalone repository, promoting the design concept to a normative specification.

---

*This is IFP-12, Draft status. The disclosure tier model and persona semantics will be refined as implementations test persona-aware gossip exchanges.*
