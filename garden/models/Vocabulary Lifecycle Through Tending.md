---
created: 2026-03-09
author: Christopher Allen
brief_summary: "Model unifying the degradation mechanism common to growing vocabularies, configuration systems, and knowledge graphs. Any accumulating terminology — predicates, tags, rules, skills — degrades retrieval effectiveness without continuous tending. Three gardening activities maintain health: weeding (removing malformed entries), seeding (introducing needed specificity), and fertilizing (enriching with semantic structure)."
tagline: "Growing vocabularies degrade without tending — weed, seed, and fertilize to maintain retrieval"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Vocabulary Lifecycle Through Tending

## Structure

The model describes a lifecycle common to any system where terminology accumulates over time: folksonomies, predicate vocabularies, agent configuration (rules and skills), tag taxonomies, and ontologies.

### The Degradation Mechanism

1. **Growth phase** — New terms enter the vocabulary as needs arise. Each addition is locally rational: a new predicate captures a relationship, a new rule prevents a failure, a new tag marks a category.

2. **Accumulation without review** — Terms pile up. Synonyms appear (`relates_to::` and `connected_to::` for the same relationship). Terms drift from their original meaning. Some become orphaned (no longer used but never removed). Others contradict each other.

3. **Retrieval degradation** — The vocabulary's signal-to-noise ratio drops. Search returns false positives. Navigation produces dead ends. Agents following instructions encounter contradictions. In Peters & Weller's metaphor: the garden becomes "savaged — different types of plants all grow wildly."

4. **The entropy floor** — Without energy input (curation effort), the system moves toward maximum disorder. This is not metaphorical — it follows from the mathematical fact that disordered states vastly outnumber ordered ones. Maintaining vocabulary health requires ongoing work.

### The Tending Activities

Peters & Weller (2008) formalized three gardening activities that counteract degradation:

**Weeding** — Remove malformed, redundant, or harmful entries. Spelling errors, spam tags, deprecated rules, orphaned predicates. The simplest form: automated lint catches formatting violations. The harder form: identifying semantic weeds (terms that look valid but mislead).

**Seeding** — Introduce specific terms where only broad ones exist. When the vocabulary has `relates_to::` doing the work of five distinct relationships, seed the specific predicates (`validates::`, `extends::`, `constrains::`) and migrate existing uses.

**Fertilizing** — Enrich terms with semantic structure from external knowledge organization systems. Map informal tags to formal ontologies. Add hierarchy, synonymy, and disambiguation. In the garden context: connecting freeform predicates to the semantic predicate catalog.

### Cross-Domain Instances

| Domain | Vocabulary | Degradation | Tending |
|--------|-----------|-------------|---------|
| Knowledge graph | Predicates | Retrieval failure from synonym drift | Predicate vocabulary stabilization |
| Agent config | Rules + skills | Contradictions, context bloat | Periodic consolidation |
| Folksonomy | Tags | Search noise, false positives | Tag gardening |
| Ontology | Classes + relations | Dependent artifacts break | Ontology evolution |
| Infrastructure | Config files | State diverges from intent | Configuration management |

The mechanism is the same in each: accumulation without review degrades the system's usefulness. The countermeasure is the same: continuous tending through weeding, seeding, and fertilizing.

## Sources

- [\[\[Peters (2008) Tag Gardening for Folksonomy Enrichment\]\]↑](../EXTERNAL.html#:~:text=Peters%20%282008%29%20Tag%20Gardening%20for%20Folksonomy%20Enrichment) — formalized the seed/weed/fertilize model for folksonomies
- [\[\[systematicls (2026) World-Class Agentic Engineering\]\]↑](../EXTERNAL.html#:~:text=systematicls%20%282026%29%20World-Class%20Agentic%20Engineering) — observed the same lifecycle in agent rules and skills: "add preferences → performance improves → contradictions accumulate → consolidate → performance improves again"
- [\[\[Informal Edges Poison the Graph\]\]↑](../EXTERNAL.html#:~:text=Informal%20Edges%20Poison%20the%20Graph) — the failure mode this model explains
- [\[\[Predicate Vocabulary Stabilization\]\]↑](../EXTERNAL.html#:~:text=Predicate%20Vocabulary%20Stabilization) — the open question this model informs

## Relations

- explains::[\[\[Informal Edges Poison the Graph\]\]↑](../EXTERNAL.html#:~:text=Informal%20Edges%20Poison%20the%20Graph)
  - The anti-pattern is the degradation phase of this lifecycle. The pattern's curation layers are the tending activities.

- informs::[\[\[Predicate Vocabulary Stabilization\]\]↑](../EXTERNAL.html#:~:text=Predicate%20Vocabulary%20Stabilization)
  - The seed/weed/fertilize framework provides a concrete methodology for the open question of when and how to stabilize.

- relates_to::[\[\[Digital Garden as Growth Ethos\]\]↑](../EXTERNAL.html#:~:text=Digital%20Garden%20as%20Growth%20Ethos)
  - The gardening metaphor for vocabulary maintenance independently parallels and enriches the digital garden ethos.

- relates_to::[\[\[Document Lifecycle Governance Heuristics\]\]](Document%20Lifecycle%20Governance%20Heuristics.html)
  - Document lifecycle governance (split, merge, delete) is tending applied to documents rather than vocabulary terms.

- relates_to::[\[\[Living Documents Over Static Publications\]\]](../principles/Living%20Documents%20Over%20Static%20Publications.html)
  - Vocabularies, like garden nodes, are living systems that require ongoing tending rather than one-time construction.
- relates_to::[\[\[Disclosure Spectrum as Discrete Tiers or Continuous Range\]\]](../inquiries/Disclosure%20Spectrum%20as%20Discrete%20Tiers%20or%20Continuous%20Range.html)
  - IFP's disclosure tier names are vocabulary that needs tending — usage will reveal which names work and which create confusion.
