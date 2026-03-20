---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Clark and Brennan's eight grounding constraints — copresence, visibility, audibility, contemporality, simultaneity, sequentiality, reviewability, revisability — mapped across communication channels from face-to-face to structured data APIs. As channels shift from synchronous to asynchronous, they trade repair speed for message permanence."
tagline: "Eight constraints on mutual understanding shift predictably from embodied conversation to structured data exchange"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Grounding Constraints Across Communication Media

**As communication channels move from synchronous and embodied to asynchronous and structured, they trade repair speed for message permanence.** Herbert Clark and Susan Brennan identified in 1991 that every communication medium imposes a specific set of constraints on how participants establish mutual understanding — what they called "grounding." These constraints are not arbitrary; they determine which grounding techniques are available and which are blocked.

## The Eight Constraints

| Constraint | Definition |
|---|---|
| Copresence | Participants share the same physical environment |
| Visibility | Participants can see each other |
| Audibility | Participants can hear each other |
| Contemporality | Receiver gets message roughly as sender produces it |
| Simultaneity | Both parties can send and receive at the same time |
| Sequentiality | Turns arrive in order they were sent |
| Reviewability | Receiver can re-examine previous messages |
| Revisability | Sender can revise message before it is received |

## Constraint Profiles by Channel

| Channel | Copres. | Visib. | Audib. | Contemp. | Simul. | Sequen. | Review. | Revis. |
|---|---|---|---|---|---|---|---|---|
| Face-to-face | Yes | Yes | Yes | Yes | Yes | Yes | No | No |
| Video call | No | Yes | Yes | Yes | Yes | Yes | No | No |
| Phone | No | No | Yes | Yes | Yes | Yes | No | No |
| Chat/IM | No | No | No | Near | No | Yes | Yes | Yes |
| Email | No | No | No | No | No | Yes | Yes | Yes |
| Structured API | No | No | No | No | No | Yes | Yes | Yes |

Face-to-face has the richest grounding affordances — participants share physical context, can point, can interrupt, can see confusion on each other's faces. But face-to-face has no reviewability. Once a word is spoken, it exists only in memory. Written channels lose the repair speed of real-time interaction but gain the ability to re-read, search, and quote previous messages.

## The Trade-off for Agent Systems

Agent-to-agent communication operates at the bottom of this table — structured, asynchronous, fully reviewable, fully revisable. This means agents have no access to the fast grounding techniques that humans rely on: facial expressions, tone of voice, real-time interruption. Every misunderstanding must be caught through explicit verification rather than ambient signals.

The design response is to build grounding into the protocol itself. An agent response should echo its understanding of the request before providing results — the equivalent of "So you're asking me to..." in human conversation. Shared schemas, type systems, and protocol standards function as pre-built common ground, reducing the amount of grounding that must happen per interaction.

Without these compensations, agent systems operating in low-constraint channels accumulate undetected misunderstandings. The cost surfaces later as coordination failures that are expensive to diagnose because the original misunderstanding left no visible trace.

## Sources

Grounded in [\[\[Clark (1991) Grounding in Communication\]\]](../citations/Clark%20%281991%29%20Grounding%20in%20Communication/Clark%20%281991%29%20Grounding%20in%20Communication.html), which introduced the constraint framework for analyzing how communication media shape mutual understanding.

## Relations

- relates_to::[\[\[Conversational Repair Organization\]\]](Conversational%20Repair%20Organization.html)
  - Repair is the recovery mechanism when grounding fails; the available repair types depend on the channel's constraint profile.

- relates_to::[\[\[Errors as Negotiation Opportunities\]\]](../patterns/Errors%20as%20Negotiation%20Opportunities.html)
  - Channels with high reviewability turn errors into negotiation material rather than lost information.
