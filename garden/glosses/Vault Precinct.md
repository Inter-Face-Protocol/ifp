---
created: 2026-03-06
author: Christopher Allen
brief_summary: "The vault precinct is the zone within Deep Context Architecture for operational knowledge work — capturing meetings, managing contacts, daily journaling, research intake, and organizing clippings. Uses the same predicate infrastructure as the garden precinct but with lighter conventions suited to capture-first workflows."
tagline: "Operational knowledge capture, organization, and retrieval for daily work"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Glosses](index.html)


- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Vault Precinct

The vault precinct is the zone within the deep context architecture for operational knowledge work. Meetings get captured, contacts get tracked, daily notes record what happened, research gets clipped and filed, reference material gets organized. The vault solves the problem of not losing things — capturing information at the speed of work and making it findable later.

Vault content uses the same predicate infrastructure as garden nodes (`is_a::`, `has_status::`, `attendee::`, `derived_from::`) but follows lighter conventions. A meeting note has a template and expected sections, not a structural contract with enforceable constraints. The priority is capture speed and retrieval, not compositional rigor.

## What Lives Here

- **Vault form types**: [\[\[Meeting Note\]\]↑](../NODES.html#:~:text=Meeting%20Note), [\[\[Transcript\]\]↑](../NODES.html#:~:text=Transcript), [\[\[Person Note\]\]↑](../NODES.html#:~:text=Person%20Note), [\[\[Chat Log\]\]↑](../NODES.html#:~:text=Chat%20Log), [\[\[Sidecar\]\]↑](../NODES.html#:~:text=Sidecar)
- **Growth stages** shared with the [\[\[Garden Precinct\]\]](Garden%20Precinct.html): Seed, Growing, Evergreen, Pruned
- **Processing stages** specific to meetings: Captured, Transcribed, Cleaned, Summarized, Published
- **Folder structure**: `Meetings/`, `People/`, `Daily/`, `Research/`, `Notes/`, `Clippings/`, `References/`

## Typed Edges in the Vault

The vault precinct uses typed predicates now — `is_a::[\[\[Meeting Note\]\]↑](../NODES.html#:~:text=Meeting%20Note)`, `attendee::[\[\[Person Name\]\]↑](../NODES.html#:~:text=Person%20Name)`, `derived_from::[\[\[Parent Note\]\]↑](../NODES.html#:~:text=Parent%20Note)`. The current lighter adoption is a tactical sequencing choice: learning the pattern in the garden first, then extending it vault-wide. Predicates are shared infrastructure, not a garden-only feature. The [\[\[Classification via Predicates Not Tags\]\]↑](../NODES.html#:~:text=Classification%20via%20Predicates%20Not%20Tags) decision applies across both precincts.

## Relationship to Garden Precinct

Both precincts share the deep context infrastructure and coexist as peers. The vault handles fast capture and daily operations; the garden handles slow curation and durable knowledge. Content moves between them — a meeting decision becomes a Decision Form, a research thread becomes an Inquiry — but this is lateral movement between zones with different purposes, not promotion from informal to formal.

## Sources

Term adopted from urban planning via [\[\[Precinct as Organizational Unit\]\]↑](../NODES.html#:~:text=Precinct%20as%20Organizational%20Unit).

## Relations

- defined_by::[\[\[Precinct as Organizational Unit\]\]↑](../NODES.html#:~:text=Precinct%20as%20Organizational%20Unit)
  - The decision that established this term.

- relates_to::[\[\[Garden Precinct\]\]](Garden%20Precinct.html)
  - The sibling precinct for curated knowledge forms.

- relates_to::[\[\[Vault Content Graduation\]\]↑](../NODES.html#:~:text=Vault%20Content%20Graduation)
  - The pattern by which vault content moves into garden nodes.

- relates_to::[\[\[Meeting Note\]\]↑](../NODES.html#:~:text=Meeting%20Note)
  - The most developed vault form type, with compound document conventions.
