← [Garden Patch Home](./)

# AGENTS.md — Garden Patch for [IFP](../)

Orientation for AI agents working with this garden patch.

## What This Is

A **garden patch** — a portable, self-contained subset of Christopher Allen's Deep Context Architecture garden, applied alongside the Inter-Face Protocol specifications. See [\[\[Garden Patch as Composable Knowledge Fragment\]\]](glosses/Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html) for the concept.

This is not part of the [IFP](../) specifications. It is an alternative lens that reveals connections between [IFP](../)'s design decisions and broader patterns in identity, trust, collaboration, and protocol design.

## Before Working With This Garden

Read these files to orient yourself:

- **[README.md](./)** — What the garden patch is, how it connects to [IFP](../), reading order
- **[NODES.md](NODES.html)** — Complete node directory: grafted, patch-native⊙, and upstream↑ nodes
- **[\[\[Form Type\]\]](forms/Form%20Type.html)** — What form types are and how the type system works
- **[\[\[Deep Context Graph Vocabulary\]\]](glosses/Deep%20Context%20Graph%20Vocabulary.html)** — Definitions: node, edge, predicate, form type

## How to Read a Garden Node

Every node follows the same structure:

```markdown
---
created: 2026-03-19
author: Christopher Allen
brief_summary: "250-350 character summary"
tagline: "10-20 word tagline, often phrased as the core question"
---

- is_a::[[Form Type]]           ← what kind of node
- has_status::[[Seed Stage]]    ← lifecycle stage
- in_domain::[[Domain Name]]    ← knowledge area

# Node Title

[Body content — structure varies by form type]

## Sources
[Where this comes from]

## Relations
- predicate::[[Target]]
  - Explanation of why this relation exists
```

**Frontmatter** (YAML between `---`) is scalar metadata: dates, summaries, identifiers.

**Body predicates** (lines with `predicate::[[Target]]`) are typed relations — labeled directed edges in the knowledge graph. They connect nodes to each other with meaning.

**Relations section** at the bottom collects cross-references with explanations.

## Form Types in This Patch

| Form Type | Core Question | Node Count |
|-----------|--------------|------------|
| [\[\[Model\]\]](forms/Model%20Form.html) | "How do these elements relate?" | 8 |
| [\[\[Gloss\]\]](forms/Gloss%20Form.html) | "What does this concept mean?" | 10 |
| [\[\[Inquiry\]\]](forms/Inquiry%20Form.html) | "What should we think about X?" | 9 |
| [\[\[Pattern\]\]](forms/Pattern%20Form.html) | "What resolves this tension?" | 5 |
| [\[\[Principle\]\]](forms/Principle%20Form.html) | "What must we always/never do?" | 7 |
| [\[\[Conviction\]\]](forms/Conviction%20Form.html) | "What do we believe is true?" | 4 |
| [\[\[Decision\]\]](forms/Decision%20Form.html) | "Why did we choose this?" | 1 |
| [\[\[Boundary\]\]](forms/Boundary%20Form.html) | "Where does authority end?" | 1 |
| [\[\[Citation\]\]](forms/Citation%20Form.html) | "What do I need to know about this source?" | 4 (2 compound) |
| [\[\[Domain\]\]](forms/Domain%20Form.html) | "What knowledge area is this?" | 3 |
| [\[\[Value\]\]](forms/Value%20Form.html) | "What do we care about?" | 2 |

## How to Create New Nodes

When adding a node to this garden patch:

1. **Choose the form type** that matches the core question. See the table above.

2. **Name the node** following conventions:
   - **Models**: Descriptive noun phrases ("Authority Conferral Chain", "Memory as Operating System")
   - **Convictions**: Claims ("Authentic Collaboration Requires Agency")
   - **Decisions**: Noun phrases about the choice, often "X Over Y" ("Classification via Predicates Not Tags")
   - **Patterns**: Claims or noun phrases ("Technology Paternalism Masks Coercion")
   - **Principles**: "X Over Y" pattern ("Content Over Container")
   - **Glosses**: "X as Y" interpretive lens ("Gossip as Social Sensing Filter")
   - **Inquiries**: Descriptive noun phrases about the question ("Trust Layer Activation Criteria")
   - All names: two-word minimum, no articles, no verbs, spell out terms fully

3. **Place the file** in the form-type subfolder (e.g., [garden/models/](models/), [garden/glosses/](glosses/))

4. **Include required metadata**:
   - Frontmatter: `created`, `author`, `brief_summary` (250-350 chars), `tagline` (10-20 words)
   - Body predicates: `is_a::`, `has_status::`, `in_domain::` at minimum
   - Relations section at the bottom

5. **Connect to existing nodes** via predicate relations. Check what's already in the patch.

## Predicate Vocabulary

| Predicate | Meaning | Example |
|-----------|---------|---------|
| `is_a::` | Classification — what kind of node | `is_a::[[Model Form]]` |
| `has_status::` | Lifecycle stage | `has_status::[[Seed Stage]]` |
| `in_domain::` | Knowledge area | `in_domain::[[Deep Context Architecture]]` |
| `relates_to::` | Lateral connection | `relates_to::[[Progressive Trust]]` |
| `grounds::` | Foundational support | `grounds::[[Filtering Is More Valuable Than Connecting]]` |
| `defines_vocabulary_from::` | Term definition source | `defines_vocabulary_from::[[Inter-Face Protocol]]` |
| `cites_work_by::` | Attribution | `cites_work_by::[[Christopher Allen]]` |
| `extends::` | Builds on | `extends::[[Authority Flows from the Person]]` |
| `depends_on::` | Requires | `depends_on::[[Progressive Disclosure]]` |

## Link Types

| What You See | Term | Meaning |
|---|---|---|
| \[\[Node Name\]\] | **Grafted node** | Copied from the source garden into this patch — click to navigate |
| \[\[Node Name\]\]⊙ | **Patch-native node** | Born in this patch, not grafted from upstream — this patch is its garden home |
| \[\[Node Name\]\]↑ | **Upstream node** | Exists in source garden, not grafted here — click for summary |
| \[\[Node Name\]\] | **Ghost link** | Node does not exist yet — a stake marking where one could grow |
| \[\[Node Name\]\]↗ | **Cross-garden node** | In another published garden with navigable URL |
| [Link text](url) | **Regular link** | Standard web link to an external website or resource — no brackets |

See [NODES.md](NODES.html) for the complete node directory.

## Key Points for Agents

- Garden files live in [garden/](./) with form-type subfolders. [IFP](../) specs live at the [repository root](../). Do not mix them.
- Reference [IFP](../) specs by relative path (`../../ifp-1-philosophy.md`), not wikilink.
- Preserve the voice and intent of existing nodes. If something seems wrong, create an Inquiry node rather than silently correcting.
- Attribution matters. Use `cites_work_by::` for others' works, note the origin of ideas.
- This patch belongs to Christopher Allen. Changes should be discussed before committing.
