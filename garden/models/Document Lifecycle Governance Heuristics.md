---
created: 2026-03-07
author: Christopher Allen
brief_summary: "Maps wiki governance heuristics for document lifecycle (split, merge, redirect, delete, draftify) to garden and agent context operations. Includes failure modes: the append-only trap (growth by accretion without consolidation) and structure ossification (resistance to reorganization over time)."
tagline: "Wiki split/merge/delete heuristics applied to garden tending and agent context maintenance"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Document Lifecycle Governance Heuristics

Wiki communities spent 25 years developing explicit governance for living documents — when to split a page, when to merge two pages, when to redirect, when to delete. These heuristics transfer to garden nodes and agent context files, with adaptations for the differences in authorship, readership, and cost.

## Wiki Heuristics

Wikipedia codified five core lifecycle operations:

**Splitting** — When readable prose exceeds 50-60kB, or when a subtopic has enough substance to stand alone. The notability test applies: if the subtopic isn't notable on its own, trim it rather than split. In the garden, the equivalent is the [\[\[Standalone Document Test for Form Candidacy\]\]↑](../EXTERNAL.html#:~:text=Standalone%20Document%20Test%20for%20Form%20Candidacy) — a section that passes the test should become its own node.

**Merging** — Five conditions: duplicate content forks, topical overlap, stubs unlikely to grow, insufficient notability (merge as alternative to deletion), and short articles requiring context from a broader page. In the garden, merge when two nodes are better understood as one — the distinction they claim doesn't hold in practice.

**Redirecting** — When a page moves or merges, the old title becomes a redirect. In the garden, wikilink aliases serve this function. In agent context, skill pointers (`load: path`) serve as redirects.

**Deletion** — Not binary but graduated: speedy deletion (obvious violations), proposed deletion (7-day window), community debate. Alternatives always considered first: merge, redirect, draftify. Wikipedia deletes roughly 1,000-1,500 pages daily. The garden equivalent is pruning — `superseded_by::` preserves the chain while removing the node from active use.

**Draftification** — Moving provisional content to a staging namespace where it can improve without polluting the main corpus. Structurally analogous to [\[\[Seed Stage\]\]](../forms/Seed%20Stage.html) — seed nodes are provisional, visible but signaling low confidence.

## Failure Modes

**The append-only trap** — Documents that grow by accretion without consolidation. New content is added; nothing is revised, reorganized, or removed. The document becomes a chronological log wearing a topic's name. Detectable via commit patterns: monotonically increasing length, many edit sessions, no refactoring commits (large deletions paired with additions). The trap is worse for agent context files, where every line consumed on every invocation makes bloat actively costly.

**Structure ossification** — Note systems that calcify and resist reorganization over time. Links accumulate, dependencies form, and the cost of restructuring a well-connected node exceeds the perceived benefit. The result: nodes that everyone knows are poorly organized but no one wants to touch. This is the opposite failure from the append-only trap: where append-only fails to consolidate, ossification fails to restructure. Both are failures of gardening — one from neglect, the other from inertia.

## Garden Application

The wiki heuristics suggest operations the garden currently lacks explicit guidance for:

- **When to split a node**: When a section passes the standalone document test, or when the node's `brief_summary` can no longer capture its scope in 350 characters
- **When to merge nodes**: When two nodes share most of their relations and their distinction doesn't survive the diagnostic question "could someone confuse these?"
- **When to prune**: When a node is superseded (the architecture handles this via `superseded_by::`) or when it hasn't been referenced or tended in multiple review cycles
- **When to restructure**: When ossification is visible — a node is well-linked but poorly organized, and agents retrieving it waste tokens navigating structure that doesn't serve them

## Sources

- Wikipedia governance policies: WP:SIZESPLIT, WP:Merging, WP:Deletion policy — codified heuristics for page lifecycle
- [\[\[The Gardening Problem Returns - Document Lifecycle in the Age of AI Agents\]\]↑](../EXTERNAL.html#:~:text=The%20Gardening%20Problem%20Returns%20-%20Document%20Lifecycle%20in%20the%20Age%20of%20AI%20Agents), Sections 1.1 and 4.1 — wiki heuristics mapped to agent context
- Cunningham, Ward. WikiWikiWeb (1995) — "radical trust" as the original design: start with trust, add governance when needed
- [\[\[Chatlatanagulchai (2025) Agent READMEs\]\]↑](../EXTERNAL.html#:~:text=Chatlatanagulchai%20%282025%29%20Agent%20READMEs) — empirical evidence that context files "behave more like dynamic configurations than static text"

## Relations

- relates_to::[\[\[Living Documents Over Static Publications\]\]](../principles/Living%20Documents%20Over%20Static%20Publications.html)
  - Living documents require lifecycle governance; this model describes the operations.

- relates_to::[\[\[Standalone Document Test for Form Candidacy\]\]↑](../EXTERNAL.html#:~:text=Standalone%20Document%20Test%20for%20Form%20Candidacy)
  - The standalone test is the garden equivalent of the wiki splitting heuristic.

- relates_to::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
  - Draftification maps to seed stage as a provisional-content pattern.

- relates_to::[\[\[Pruned Stage\]\]↑](../EXTERNAL.html#:~:text=Pruned%20Stage)
  - Pruning is the garden equivalent of graduated deletion.

- relates_to::[\[\[Context Conservation Hierarchy\]\]↑](../EXTERNAL.html#:~:text=Context%20Conservation%20Hierarchy)
  - The append-only trap directly degrades context conservation by inflating node size.
- relates_to::[\[\[When to Specify and When to Explore in Protocol Evolution\]\]](../inquiries/When%20to%20Specify%20and%20When%20to%20Explore%20in%20Protocol%20Evolution.html)
  - Wiki governance heuristics for document lifecycle (split, merge, draftify) apply to how IFP specifications could evolve as implementations emerge.
