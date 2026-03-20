---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Garden nodes are living documents that grow, split, merge, and evolve through tending. The current state matters, not a published version. Mutability varies: most nodes evolve freely, cases are immutable records with living interpretation, convictions change rarely. Provenance links to archived sources should upgrade to living targets."
tagline: "Garden nodes grow and evolve through tending — the current state matters, not the published version"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Principles](index.html)


- is_a::[\[\[Principle Form\]\]](../forms/Principle%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Living Documents Over Static Publications

**Garden nodes are living documents.** They grow through stages, absorb new connections, split when they outgrow a single file, and merge when distinctions prove unnecessary. Git preserves every prior state, but the current version is what readers and agents encounter. No garden node is "published" in the sense that an article or book is — there is no canonical snapshot that subsequent changes diminish.

This is the opposite of publication-oriented knowledge systems where value concentrates in a specific released version. A journal article's value is its DOI-identified text. A book's value is its ISBN edition. A garden node's value is its *current state* — informed by everything that came before but not subordinate to it.

## Mutability Spectrum

Not all garden nodes are equally mutable. The architecture recognizes a spectrum:

**Designed to evolve** — Pattern, Model, Gloss, Inquiry, Reference, Principle, Protocol, Boundary, Skill, Scenario, Domain. These nodes expect revision as understanding deepens, new cases emerge, or the domain shifts. A pattern at Seed Stage may look nothing like its Evergreen version. This is by design.

**Near-immutable** — Conviction ("a change represents a fundamental shift"), Value ("evolves over decades"). These change rarely, and when they do, it signals something significant about the author's worldview.

**Immutable record, living interpretation** — Case ("history doesn't change, though interpretation may"), Citation. A case records what happened; that doesn't change. But the annotations, relations, and lessons drawn from a case are living. An [\[\[Annotated Citation\]\]↑](../NODES.html#:~:text=Annotated%20Citation) differs from a basic citation precisely because the interpretation layer evolves even when the cited work is static.

## Consequences

Growth stages (Seed, Growing, Evergreen, Pruned) make sense only for living documents. A published article doesn't have a "growing" phase after release — it has editions or errata. Garden nodes have growth as a continuous property, not a discrete event.

The compound document pattern (a form graduating from a single file to a folder with siblings) is a living document behavior. Published works don't spontaneously acquire companion documents; garden nodes do, as related knowledge accumulates around a concept.

Pruning replaces deletion because living documents leave traces. A pruned node's `superseded_by::` predicate preserves the evolution chain — how understanding moved from one form to its successor.

Provenance links to archived sources become ghost links — edges pointing at nothing navigable. When a source document is fully extracted into garden nodes, the graph should point to living targets, not dead ones. Git history preserves the extraction provenance; the graph preserves navigable relationships. An `extracted_from::` predicate is a construction artifact: once the source is archived or reincarnated as a living node, upgrade to `implements::`, `relates_to::`, or another semantic predicate that connects living nodes.

A fully extracted source document doesn't have to die. When the document itself represents a significant choice or position, it can be reincarnated as a living node — a Decision recording the choice it embodies, a Reference that continues to be tended. Reincarnation turns an archived dead end into a living node that other nodes can link to. The extraction process should include a reincarnation check as its final step: does this source represent something worth keeping alive in the graph?

## Diagnostic

If you can point to a "final version" of a garden node that subsequent edits would diminish rather than improve, it's not functioning as a living document. Either the form type is wrong (it might be a Case, which records history) or the form needs to be reconceived as something that grows.

## Sources

The digital garden movement established "continuous growth" as a core principle (Appleton's six patterns, Caufield's garden-vs-stream distinction). See [\[\[Digital Garden as Growth Ethos\]\]↑](../NODES.html#:~:text=Digital%20Garden%20as%20Growth%20Ethos). The deep context architecture operationalizes this through typed growth stages and structural contracts that accommodate evolution.

## Relations

- relates_to::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html) — living documents are a defining characteristic of the garden precinct
- relates_to::[\[\[Digital Garden as Growth Ethos\]\]↑](../NODES.html#:~:text=Digital%20Garden%20as%20Growth%20Ethos) — the growth ethos provides the philosophical foundation; this principle makes it architectural
- relates_to::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html) — entry point for new living documents
- relates_to::[\[\[Evergreen Stage\]\]](../forms/Evergreen%20Stage.html) — mature but still living; stability is not finality
- relates_to::[\[\[Pruned Stage\]\]↑](../NODES.html#:~:text=Pruned%20Stage) — end-of-life for living documents; superseded, not deleted
- relates_to::[\[\[Vault Content Graduation\]\]↑](../NODES.html#:~:text=Vault%20Content%20Graduation) — vault content becomes a living document when it graduates to a garden node
- relates_to::[\[\[Opus Form\]\]](../forms/Opus%20Form.html) — opus lead files are living documents by design; analysis can be revised when the work evolves
- relates_to::[\[\[When to Specify and When to Explore in Protocol Evolution\]\]](../inquiries/When%20to%20Specify%20and%20When%20to%20Explore%20in%20Protocol%20Evolution.html)
  - Living document philosophy grounds the argument for keeping tactical protocol details open for revision through implementation experience.

- relates_to::[\[\[Neobooks as Composable Knowledge Objects\]\]](../glosses/Neobooks%20as%20Composable%20Knowledge%20Objects.html)
  - Neobooks are the composable successor to static publications — living, assemblable, disassemblable.
