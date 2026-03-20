---
created: 2026-03-20
author: Christopher Allen
brief_summary: "A structural contract is the agreement that every instance of a form type follows the same internal structure — required sections, naming heuristics, predicate patterns, and the core question the form answers. The contract is what makes forms interoperable: a reader who knows the Model Form contract can navigate any model, and an agent can traverse any form without per-instance instruction."
tagline: "The agreement that every instance of a form type follows the same internal structure"
---

← [Garden Patch Home](../) · [Glosses](index.html)


- is_a::[\[\[Gloss Form\]\]](../forms/Gloss%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Structural Contract as Form Type Agreement

A **structural contract** is the set of requirements that every instance of a form type must satisfy. It defines what sections a form must have, what question it answers, how it should be named, and what predicates it typically carries. The contract is not a template — it specifies structure, not content.

Every form type definition page ([\[\[Model Form\]\]](../forms/Model%20Form.html), [\[\[Pattern Form\]\]](../forms/Pattern%20Form.html), [\[\[Gloss Form\]\]](../forms/Gloss%20Form.html), etc.) declares its structural contract. For example, the Pattern Form contract requires: context, forces in tension, solution, consequences, and connections. Any node with `is_a::[[Pattern Form]]` commits to providing those sections. A model requires different sections. A conviction requires different sections. But all patterns look alike, all models look alike — that is what the contract guarantees.

## Why Contracts Matter

**For humans**: A reader who has seen one pattern knows how to read any pattern. The structural contract is a promise that the form's internal organization will be familiar. You do not need to learn a new layout for each node — just the content.

**For agents**: An AI agent traversing the graph can rely on the structural contract to know where to find the relevant information in a node. The "Sources" section is always where provenance lives. The "Relations" section is always where connections are declared. This predictability is what makes gardens machine-traversable without per-node instruction.

**For interoperability**: When two gardens share nodes, the structural contract is what makes them compatible. A [\[\[Model Form\]\]](../forms/Model%20Form.html) in one garden follows the same contract as a Model Form in any other garden. This is how garden patches work — grafted nodes are readable because the contracts match.

## What a Contract Specifies

- **Core question** — The question this form type answers
- **Required sections** — What the body must contain
- **Naming heuristics** — How to title instances of this form type
- **Typical predicates** — Which predicate patterns are expected
- **Category** — Which family of forms this belongs to (orientation, structural, action, generative, governance)

## Sources

- Defined implicitly across all form type definitions in the [\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html) garden
- First articulated as a concept in [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html)

## Relations

- relates_to::[\[\[Form Type\]\]](../forms/Form%20Type.html)
  - Every form type declares a structural contract; the contract is what distinguishes one form type from another.

- relates_to::[\[\[Garden Patch as Composable Knowledge Fragment\]\]](Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html)
  - Structural contracts are what make patches composable — nodes from different gardens are compatible because they follow the same contracts.
