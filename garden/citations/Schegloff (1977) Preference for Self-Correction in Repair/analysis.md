---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Analysis of Schegloff's repair preference hierarchy as a design pattern for agent protocol error handling — why self-correction first produces better outcomes and how the four repair types map to protocol behaviors."
tagline: "The repair preference hierarchy as a design pattern for graduated agent error handling"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Analysis: Preference for Self-Correction in Repair

## Core Thesis

Schegloff, Jefferson, and Sacks argue that conversational repair is not ad hoc troubleshooting but a system with internal organization. That organization has a clear structural bias: self-initiated self-repair occupies the earliest available position (same turn as the trouble source), while other-correction occupies the latest and most structurally constrained position. The system does not merely allow self-correction — it actively promotes it through the mechanics of turn-taking.

This is an empirical finding, not a normative claim. The authors analyzed naturally occurring conversation and found the pattern holds across trouble types (mishearings, malapropisms, wrong references, ambiguities) and participant relationships. The preference is built into the turn-taking system itself, not into social rules about politeness.

## The Repair Preference Hierarchy as Design Pattern

The four repair types form a hierarchy ordered by structural preference:

1. **Self-initiated self-repair** — Speaker catches and fixes their own error within the same turn. No other participant needs to act. This is the fastest, least disruptive repair.
2. **Self-initiated other-repair** — Speaker signals trouble but another participant completes the repair (e.g., word searches where a listener supplies the target word). Initiation stays with the trouble source.
3. **Other-initiated self-repair** — A listener signals a problem ("huh?", "you mean X?"), and the original speaker produces the correction. The initiator deliberately avoids correcting directly.
4. **Other-initiated other-repair** — A listener both identifies and corrects the problem. This is structurally last, delayed, and modulated when it occurs.

This hierarchy maps directly to agent protocol error handling. In a two-agent interaction where Agent A produces a malformed message:

| Repair type | Protocol equivalent |
|-------------|-------------------|
| Self-initiated self-repair | Agent A detects its own error and sends a correction before Agent B responds |
| Other-initiated self-repair | Agent B signals the error; Agent A produces the corrected version |
| Other-initiated other-repair | Agent B detects and corrects the error unilaterally |

The Inter-Face Protocol's error phase already implements something close to other-initiated self-repair: when an agent receives a problematic message, it initiates a repair sequence rather than silently failing or unilaterally reinterpreting. Schegloff's research provides the theoretical basis for why this design works.

## Why Self-Correction First

The preference for self-correction is not just socially graceful — it is technically sound for agent protocols.

**The trouble source has the most context.** The speaker who produced the error knows what they intended. A listener can identify that something went wrong but often cannot determine the intended meaning. In protocol terms, the agent that produced a malformed message knows what it was trying to communicate. An error signal that gives that agent the opportunity to reformulate produces better corrections than one where the receiving agent guesses.

**Self-correction preserves intent.** When others correct, they substitute their interpretation of the intended meaning. This works in simple cases (obvious word substitutions) but fails for complex or ambiguous trouble sources. Agent protocols that allow receiving agents to silently "fix" malformed messages risk compounding errors — the correction may address the wrong problem.

**Escalation creates accountability.** The hierarchy is an escalation sequence. Each step up involves more disruption and more intervention from others. This natural escalation means that simple errors resolve quickly (self-repair in same turn) while serious misunderstandings get more collaborative attention (other-initiation forcing explicit repair sequences). A flat error-handling model that treats all errors identically misses this graduated response.

## Connection to Error Phase Design

The Inter-Face Protocol structures error handling as a negotiation between agents, not a unilateral rejection. This matches Schegloff's finding that other-initiation typically takes the form of an invitation to self-correct rather than a direct correction. The "huh?" of conversation and the error signal of a protocol serve the same function: they flag a problem and return the floor to the agent best positioned to fix it.

The research also explains why silent error handling fails. In conversation, when listeners silently accommodate errors (pretending to understand, guessing at the intended meaning), mutual understanding degrades. The same holds for agent protocols: silent accommodation of malformed messages produces cascading misalignment that surfaces later as harder-to-diagnose failures.
