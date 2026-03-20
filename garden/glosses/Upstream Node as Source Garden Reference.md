---
created: 2026-03-19
author: Christopher Allen
brief_summary: "An upstream node is a knowledge node that exists in the source garden but was not grafted into a garden patch. It is referenced by grafted nodes through predicate links marked with ↑, and its summary is documented on the Upstream References page. The source garden is 'upstream' — the origin from which knowledge flows into the patch."
tagline: "A node that exists in the source garden but was not grafted into this patch"
---

← [Garden Patch Home](../) · [Glosses](index.html)


- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Upstream Node as Source Garden Reference

A garden patch is a fragment of a larger garden. It cannot contain every node the source garden has — that would make it a full garden, not a patch. When a grafted node references a node that exists in the source garden but was not included in the patch, that reference is an **upstream node**.

The term borrows from version control: the source garden is "upstream" — the origin from which knowledge flows into the patch. An upstream node has known provenance (we know where it is and what it says) but is not present for direct navigation.

## How Upstream Nodes Appear

Links to upstream nodes are marked with **↑** and are clickable — they navigate to the upstream section of the [Node Directory](../NODES.html), which documents each upstream node's name, form type, and brief summary from the source garden. This gives readers enough context to understand the reference without needing access to the source garden.

The ↑ marker distinguishes upstream nodes from ghost links (plain text, not clickable — the node does not exist yet) and from grafted nodes (clickable without a marker — the node is present in the patch).

## Why Not Include Everything

A garden patch is deliberately selective. Including every referenced node would cascade indefinitely — each included node references more nodes, and so on. The patch boundary is a design decision: graft the nodes needed for the patch to be self-contained and legible, document the rest as upstream references.

## Sources

- This garden patch — first instance of garden patch terminology

## Relations

- relates_to::[\[\[Garden Patch as Composable Knowledge Fragment\]\]](Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html)
  - Upstream nodes define the boundary of what a patch includes.

- relates_to::[\[\[Grafted Node as Transplanted Knowledge in a Garden Patch\]\]](Grafted%20Node%20as%20Transplanted%20Knowledge%20in%20a%20Garden%20Patch.html)
  - The complement: grafted nodes are present, upstream nodes are referenced.

- relates_to::[\[\[Ghost Link as Unplanted Garden Stake\]\]](Ghost%20Link%20as%20Unplanted%20Garden%20Stake.html)
  - Ghost links are the third category — no node exists yet, unlike upstream nodes which exist but elsewhere.

- relates_to::[\[\[Progressive Disclosure Over Eager Loading\]\]](../principles/Progressive%20Disclosure%20Over%20Eager%20Loading.html)
  - The upstream summary page is progressive disclosure — enough context to understand the reference, with the full node available on request.
