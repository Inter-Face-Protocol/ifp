---
created: 2026-03-19
author: Christopher Allen
brief_summary: "A ghost link is a wikilink reference to a node that does not exist yet — neither in this garden patch nor in the source garden. Like a stake marking where to plant, it signals that a concept has been identified as worth developing but has not yet been written. Ghost links appear as plain, non-clickable text."
tagline: "A reference to a node that does not exist yet — a stake marking where one could grow"
---

← [Garden Patch Home](../) · [Glosses](index.html)


- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Ghost Link as Unplanted Garden Stake

In wiki culture, a ghost link (sometimes called a "red link" or "zombie node") is a reference to a page that does not exist yet. It is not an error — it is an intentional signal that a concept has been identified as worth writing about.

In a Deep Context Architecture garden, ghost links serve as **planning tools**. When a node references `[[Concept Name]]` and no node by that name exists anywhere — not in the patch, not in the source garden — the ghost link marks a gap in the knowledge graph. The concept has been named and connected to other ideas through predicates, but no one has written the node yet.

## Ghost Links as Garden Stakes

The gardening metaphor: a ghost link is a **stake in the ground** marking where something should be planted. The stake shows the gardener's intention — this is where a pattern, model, or inquiry should grow — without committing to the planting yet.

Ghost links are visually distinct: they render as **plain, non-clickable text** with `[[brackets]]`. This distinguishes them from grafted nodes (clickable, no marker) and upstream nodes (clickable, with ↑ marker).

## Ghost Links in Practice

A garden can track ghost links to prioritize what to write next. Nodes with the most incoming ghost links — the most predicates pointing to something that doesn't exist yet — are candidates for early creation. The ghost link count is a measure of how much the existing graph expects a concept to be developed.

## Sources

- Wiki culture: "red links" in MediaWiki, "zombie nodes" in WikiBonsai's Caudex
- This garden patch — first formal definition in Deep Context Architecture

## Relations

- relates_to::[\[\[Grafted Node as Transplanted Knowledge in a Garden Patch\]\]](Grafted%20Node%20as%20Transplanted%20Knowledge%20in%20a%20Garden%20Patch.html)
  - Grafted nodes are present; ghost links mark where future nodes could be grafted.

- relates_to::[\[\[Upstream Node as Source Garden Reference\]\]](Upstream%20Node%20as%20Source%20Garden%20Reference.html)
  - Upstream nodes exist but elsewhere; ghost links do not exist yet at all.

- relates_to::[\[\[Garden Patch as Composable Knowledge Fragment\]\]](Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html)
  - Ghost links in a patch reveal what the patch expects but does not yet contain.
