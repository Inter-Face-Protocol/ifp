---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Insights from Schegloff's repair research — the repair taxonomy as a model form, fifty years of convergent evidence for a protocol design choice, repair as continuous calibration rather than exception handling, and the modulation problem for inter-agent error signals."
tagline: "Repair as continuous self-monitoring, not exception handling — and why error modulation matters between agents"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Insights: Preference for Self-Correction in Repair

## Conversational Repair Organization as a Model

The repair taxonomy maps cleanly to agent protocol behaviors, and the mapping is specific enough to generate a form:

| Repair type | Conversational example | Agent protocol behavior |
|-------------|----------------------|------------------------|
| Self-initiated self-repair | "Turn left — I mean right" | Agent detects own malformed output, sends correction unprompted |
| Self-initiated other-repair | "What's that word... starts with P..." / "Paradigm?" | Agent requests help completing an operation; partner supplies missing element |
| Other-initiated self-repair | "Huh?" / "Oh, I said turn right at the light" | Receiving agent signals error; sending agent reformulates |
| Other-initiated other-repair | "You mean right, not left" | Receiving agent corrects the message unilaterally |

The model "[\[\[Conversational Repair Organization\]\]](../../models/Conversational%20Repair%20Organization.html)" captures this taxonomy, with the structural preference hierarchy as its core claim: protocols that give the error-producing agent first opportunity to self-correct produce better outcomes than protocols that skip to unilateral correction. The claim is testable and has 50 years of conversational evidence behind it.

## Fifty Years of Evidence for a Protocol Design Choice

Schegloff, Jefferson, and Sacks published in 1977. The subsequent research tradition — thousands of studies across dozens of languages, in medical consultations, courtrooms, classrooms, air traffic control, and human-computer interaction — has consistently confirmed the preference hierarchy. This is not a fragile finding from a single study. It is one of the most replicated results in the social sciences.

This gives the Inter-Face Protocol's error handling design something that most protocol specifications lack: deep theoretical grounding from an independent research tradition. The error phase was designed from first principles about agent interaction. That it converges with a well-established finding from conversation analysis strengthens both the design and the justification for it.

## Beyond Error Handling: Repair as Ongoing Calibration

The most productive insight from Schegloff for protocol design goes beyond error handling per se. In conversation, repair is not exceptional — it is constant. Speakers monitor their own output continuously, catching and fixing problems that listeners might never notice. Most self-repair happens within the same turn, invisible to casual observation.

This reframes error handling in agent protocols. If repair is treated as an exceptional state (error phase triggered by failure), the protocol misses the continuous self-monitoring that makes conversation work. A protocol that builds in self-monitoring — agents checking their own output against their intent before sending, with low-cost mechanisms to retract or amend — would be closer to how human conversation actually maintains mutual understanding.

## The Modulation Problem

Schegloff documents that when other-correction does occur, speakers modulate it heavily: delays, agreement prefaces ("yes, but..."), embedding corrections inside larger responses. This modulation is not mere politeness. It manages the social cost of publicly identifying someone else's error.

Agent protocols face an analogous problem when agents represent different principals. An error signal between agents is also a signal between the principals those agents represent. How the error is communicated — its framing, timing, and directness — carries social meaning beyond the technical content. Protocol designers who treat error messages as purely technical miss the interactional dimension that Schegloff's work makes visible.
