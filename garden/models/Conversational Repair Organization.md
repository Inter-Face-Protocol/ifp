---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Schegloff's four repair types mapped to agent protocol behaviors: self-initiated self-repair, self-initiated other-repair, other-initiated self-repair, and other-initiated other-repair. Protocols giving the error-producing agent first opportunity to self-correct produce better outcomes. Continuous self-monitoring beats error-state handling."
tagline: "Four repair types from conversation analysis map directly to agent error-correction protocol design"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Conversational Repair Organization

**Protocols that give the error-producing agent first opportunity to self-correct produce better outcomes.** This is not a design preference — it is an empirical finding from 50 years of conversation analysis research. Emanuel Schegloff established in 1977 that human conversation has a systematic organization for handling errors, and that this organization has a strong structural preference for self-correction.

## The Four Repair Types

Repair in conversation is organized along two dimensions: who initiates the repair (the speaker or the hearer) and who completes it.

| Repair Type | Initiator | Repairer | Agent Protocol Example |
|---|---|---|---|
| Self-initiated self-repair | Speaker | Speaker | Agent detects own malformed output, sends correction before recipient responds |
| Self-initiated other-repair | Speaker | Hearer | Agent signals it cannot complete an operation, requests help from another agent |
| Other-initiated self-repair | Hearer | Speaker | Receiving agent signals a problem ("I don't understand field X"), sender reformulates |
| Other-initiated other-repair | Hearer | Hearer | Receiving agent corrects the error unilaterally without consulting sender |

## The Preference Hierarchy

Schegloff's central finding: self-initiated self-repair is structurally preferred over all other types. In natural conversation, speakers routinely monitor their own output and correct errors within the same turn, often before the problematic element is even complete. When self-repair does not happen, hearers provide opportunities for the speaker to self-correct before attempting correction themselves.

This hierarchy exists because self-repair preserves the speaker's competence and the collaborative relationship. Other-repair — especially other-initiated other-repair — carries social costs. The parallel in agent systems is direct: an agent that catches and corrects its own errors maintains trust with collaborating agents. An agent that must be corrected by others imposes coordination overhead on the system.

## Design Implications

Agent protocols should build in self-monitoring as a continuous process, not an exception-handling path. Every output stage should include a verification check before transmission. When verification fails, the agent should issue a correction in the same message sequence rather than waiting for the recipient to detect the problem.

The repair preference hierarchy also means that protocol error-handling should escalate through the four types in order. Give the originating agent the first chance. If it does not self-correct within a defined window, signal the error and let it try again. Only after that fails should the receiving agent attempt unilateral correction.

## Sources

Grounded in [\[\[Schegloff (1977) Preference for Self-Correction in Repair\]\]](../citations/Schegloff%20%281977%29%20Preference%20for%20Self-Correction%20in%20Repair/Schegloff%20%281977%29%20Preference%20for%20Self-Correction%20in%20Repair.html), which established the preference organization for conversational repair across languages and contexts.

## Relations

- relates_to::[\[\[Errors as Negotiation Opportunities\]\]](../patterns/Errors%20as%20Negotiation%20Opportunities.html)
  - Repair is the mechanism through which errors become productive negotiations rather than failures.

- relates_to::[\[\[Clark (1991) Grounding in Communication\]\]](../citations/Clark%20%281991%29%20Grounding%20in%20Communication/Clark%20%281991%29%20Grounding%20in%20Communication.html)
  - Clark's grounding model describes how mutual understanding is established; repair is what happens when grounding fails.
