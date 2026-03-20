---
created: 2026-03-07
author: Christopher Allen
brief_summary: "Three domains — wiki communities, digital gardens, and AI agent context systems — face the same document lifecycle problems (splitting, staleness, ownership, deletion) under different constraints. Maps the parallels and identifies where the analogy breaks down: statelessness, read frequency, token economics, and automated maintenance."
tagline: "Wiki, garden, and agent context — same lifecycle problems, different constraints"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Cross-Domain Document Lifecycle Parallels

Three communities maintain living documents and face the same structural problems under different names. Wiki communities developed explicit governance over 25 years. Digital garden practitioners inherited the gardening metaphor but shifted to individual authorship. AI agent developers rediscovered the problems in compressed form, mostly without awareness of the prior art.

## The Parallel Structure

| Problem | Wiki | Digital Garden | Agent Context |
|---|---|---|---|
| When to split | Page exceeds 50-60kB; subtopic passes notability test | Atomic note outgrows its title | CLAUDE.md section extracted to skill/guide file |
| Staleness | Page rot — structurally intact, substantively stale | Evergreen notes that aren't evergreen | Context drift — file says auth is in src/auth/ but it moved |
| Ownership | Collective authorship; gardener role | Single author; conflict with past self | Role-based write access per agent persona |
| Merge/redirect | Explicit policy with 5 criteria | Note merging with link forwarding | No equivalent yet (gap) |
| Edit conflicts | Edit wars → talk pages → arbitration | N/A (single author) | Agent overwriting another agent's additions |
| Categorization | Categories, infoboxes, portals | Tags, folders, links, maps of content | Progressive disclosure via directory structure |
| Versioning | Page history (core feature) | Git commits (no UI equivalent) | Git (sometimes); agent sees current state only |
| Deletion | Graduated: speedy → PROD → AfD debate; ~1,000-1,500 pages/day | Rarely delete; notes accumulate indefinitely | No convention; stale sections persist |
| Scale collapse | Global category tree becomes unusable | Graph view becomes noise | Context window fills with irrelevant instructions |

## Where the Analogy Breaks

**Statelessness** — Wiki editors accumulate tacit knowledge of a page's history. Agents are stateless — every session is a cold start. This makes the context file load-bearing in a way no wiki page has been. Stale content that a human wiki reader might recognize and discount will mislead an agent that has no memory of the page's evolution.

**Read frequency** — A wiki page might be read by dozens of people per day. A CLAUDE.md is read on every agent invocation, potentially hundreds of times daily. The cost/benefit calculus of what to include shifts when every line is consumed on every request.

**Token economics** — Wiki pages have soft length constraints (usability). Agent context files compete for a finite context window with the actual work content. There is a quantifiable cost to every line — progressive disclosure is not optional.

**Automated maintenance** — Agents can garden their own context files — a capability wiki pages never had. But this introduces recursive trust problems: can you trust the agent to accurately assess the staleness of its own instructions? Wiki bot policies (explicit governance for automated edits) are the closest precedent.

## What Each Domain Teaches

**Wiki → everyone**: Governance matters more than tooling. The gardener role is real work. Categorization and lifecycle are different axes. Bot/automated maintenance needs explicit policy. Redirect/alias systems are essential when documents move or merge.

**Agent systems → wiki/garden**: Token economics as a forcing function for conciseness. Progressive disclosure as an operating principle. Metadata-driven staleness detection. Role-based ownership as an alternative to collective authorship. Explicit context budgets for deciding what to include.

**Digital gardens → both**: Growth-stage metadata as a lifecycle primitive. Atomicity as a splitting heuristic. The lived experience of single-author gardening at multi-year timescales. Link rot and structure ossification as cautionary tales.

## Sources

- [\[\[The Gardening Problem Returns - Document Lifecycle in the Age of AI Agents\]\]↑](../EXTERNAL.html#:~:text=The%20Gardening%20Problem%20Returns%20-%20Document%20Lifecycle%20in%20the%20Age%20of%20AI%20Agents), Sections 2.1-2.2 and Part 4 — the structural parallel table and synthesis
- Caulfield, Mike. "The Garden and the Stream: A Technopastoral." Keynote, dLRN 2015 — the distinction between accumulative/garden-mode and sequential/stream-mode knowledge
- [\[\[Chatlatanagulchai (2025) Agent READMEs\]\]↑](../EXTERNAL.html#:~:text=Chatlatanagulchai%20%282025%29%20Agent%20READMEs) — empirical evidence of lifecycle problems in agent context files

## Relations

- relates_to::[\[\[Document Lifecycle Governance Heuristics\]\]](Document%20Lifecycle%20Governance%20Heuristics.html)
  - The governance model describes the wiki-side operations; this model maps them across domains.

- relates_to::[\[\[Digital Garden as Growth Ethos\]\]↑](../EXTERNAL.html#:~:text=Digital%20Garden%20as%20Growth%20Ethos)
  - The digital garden domain occupies the middle column of the parallel structure.

- relates_to::[\[\[Context Conservation Hierarchy\]\]↑](../EXTERNAL.html#:~:text=Context%20Conservation%20Hierarchy)
  - Token economics (the breaking point in the analogy) is what makes context conservation load-bearing.

- relates_to::[\[\[Progressive Disclosure Over Eager Loading\]\]](../principles/Progressive%20Disclosure%20Over%20Eager%20Loading.html)
  - Progressive disclosure is the agent-domain response to token economics that wiki and garden don't face at the same intensity.

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
  - The automated maintenance question (can agents garden their own instructions?) directly tests this principle.
- relates_to::[\[\[When to Specify and When to Explore in Protocol Evolution\]\]](../inquiries/When%20to%20Specify%20and%20When%20to%20Explore%20in%20Protocol%20Evolution.html)
  - IFP specifications are another instance of the cross-domain lifecycle pattern — facing the same questions about splitting, merging, and deprecating that wikis and gardens face.
