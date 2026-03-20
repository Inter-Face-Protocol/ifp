---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Jerry Michalski's concept of neobooks — composable knowledge objects that can be assembled, disassembled, and reassembled by different people for different purposes. A successor to the book as knowledge transmission unit. Garden opuses and garden patches are partial implementations of this vision: opuses handle authored composition with renditions, patches handle portable knowledge fragments applied alongside external content."
tagline: "Books replaced by composable knowledge objects — assembled and reassembled for different purposes"
---

← [Garden Patch Home](../) · [Glosses](index.html)


- is_a::[[\[Gloss Form\]]](../forms/Gloss%20Form.html)
- has_status::[[\[Seed Stage\]]](../forms/Seed%20Stage.html)
- in_domain::[[\[Deep Context Architecture\]]](../domains/Deep%20Context%20Architecture.html)

# Neobooks as Composable Knowledge Objects

Jerry Michalski's term for a successor to the book as a knowledge transmission unit. Where books are monolithic, neobooks are **composable** — knowledge objects that can be assembled, disassembled, and reassembled by different people for different purposes. One person composes a neobook from patches of knowledge; another takes a third of those patches and combines them with their own material.

The concept has been a "wish" (Peter Kaminski's word) within the Open Global Mind community for years. Previous attempts at implementation were "impractical" in Peter's assessment. The Deep Context Architecture garden implements significant portions of this vision through two mechanisms:

- **Opuses**: Compound authored documents with platform-specific renditions (X, Bluesky, LinkedIn) that evolve as understanding deepens. Opuses of opuses (e.g., a series of musings that become a collection). Living documents rather than frozen publications.

- **Garden patches**: Portable, self-contained knowledge fragments applied alongside external content. Patches are forks that can diverge and merge back. The IFP garden patch is the first instance — 118+ files expressing Inter-Face Protocol concepts through garden forms.

Both share the composable property: content can be taken apart and reassembled. Neither requires the other's permission to evolve. The garden's predicate graph provides the structural integrity that earlier neobook visions lacked — typed edges, form contracts, and status lifecycle give each composable piece a known shape.

## Lineage

The neobooks concept descends from Ted Nelson's Xanadu project (1960s onward), which envisioned transclusion — documents that include live portions of other documents with attribution and royalty tracking. Christopher Allen worked for Xanadu in 1989. The garden approach differs from Xanadu in that it uses fork-and-merge semantics (like Git) rather than transclusion. Each garden node is a complete, standalone document that can reference but does not embed other nodes.

## Sources

- Peter Kaminski, 2026-03-19 Peter Kaminski - Garden Patch Review — "This is a dream that Jerry has had, or a wish... You've kind of got a lot of it solved."
- Jerry Michalski, Open Global Mind community discussions (oral tradition, not a published document)

## Relations

- relates_to::[[\[Opus Form\]]](../forms/Opus%20Form.html)
  - Opuses are the first-party composition mechanism — how an author assembles neobook-like collections.

- relates_to::[[\[Garden Patch as Composable Knowledge Fragment\]]](Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html)
  - Garden patches are the portable distribution mechanism — how knowledge fragments travel between contexts.

- inspired_by::Ted Nelson
  - Xanadu's transclusion vision is the ancestor; garden's fork-and-merge is the descendant.
