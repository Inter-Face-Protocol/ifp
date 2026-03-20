---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Defines the Boundary form type: a declaration of what an agent may and may not decide. Not what the right choice is, not how to make it, but who holds authority. Amendable through deliberative process, never unilaterally. 1 instance in Garden/boundaries/."
tagline: "Where does this system's authority end? — the structural contract for boundary forms"
---

← [Garden Patch Home](../) · [Form Definitions](index.html)


- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)

# Boundary Form

**Core question**: "Where does this system's authority end?"

A declaration of what an agent (LLM, individual, group) may and may not decide. Not *what* the right choice is (principle), not *how* to make it (protocol), but *who holds authority*. Boundaries are the governance layer — the rules about who gets to play and what moves they can make. Amendable through deliberative process, never unilaterally by an LLM.

## Structural Contract

A boundary form requires:

- **Authority zones** — A table or structured list showing zones of authority with levels (autonomous, guided, escalate, prohibited) and examples for each zone.
- **Agent behavior at boundaries** — Steps for recognition and escalation when an agent encounters the boundary edge.
- **Amendment** — How the boundary can be changed and by whom. This section is mandatory because boundaries without amendment processes become brittle.
- **Sources** — Values and principles the boundary is grounded in.
- **Relations** — Connections to principles it enforces, models it constrains, and patterns it governs.

Naming heuristic: what's bounded + distinctive feature. "Delegated Decision Authority Spectrum" not "Authority Boundary."

## Typical Predicates

- `is_a::[\[\[Boundary Form\]\]](Boundary%20Form.html)`
- `has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)` or `[\[\[Growing Stage\]\]](Growing%20Stage.html)`
- `in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)`
- `grounded_in::[\[\[Value\]\]↑](../NODES.html#:~:text=Value)` — values that justify the boundary
- `embodies::[\[\[Pattern Form\]\]](Pattern%20Form.html)` — patterns that demonstrate the boundary
- `relates_to::[\[\[Principle Form\]\]](Principle%20Form.html)`, `[\[\[Model Form\]\]](Model%20Form.html)`

## Exemplars

- [\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html) — authority zone table with HAAH spectrum, amendment process, and escalation steps

## Category

Governance form — establishes *who decides* and *how rules change*.

## Sources

Definition from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), lines 117-118.

## Relations

- relates_to::[\[\[Principle Form\]\]](Principle%20Form.html) — principles inform what boundaries protect
- relates_to::[\[\[Model Form\]\]](Model%20Form.html) — models map the authority zones boundaries define
- relates_to::[\[\[Decision Form\]\]](Decision%20Form.html) — boundaries constrain what decisions an agent can make autonomously