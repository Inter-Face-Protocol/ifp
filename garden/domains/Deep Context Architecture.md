---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Domain index for Deep Context Architecture — a system for capturing reasoning as typed markdown nodes connected by predicates, organized into precincts (garden and vault). Covers precincts, type system, lifecycle tracks, compound documents, naming, classification, meeting capture, personal knowledge management methods, and retrieval."
tagline: "The architecture that defines both precincts — typed nodes, predicates, and progressive disclosure"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Domains](index.html)


- is_a::[\[\[Domain Form\]\]](../forms/Domain%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)

# Deep Context Architecture

Deep context is an architecture for captured reasoning: typed markdown forms connected by predicates into a navigable knowledge graph. Each form type answers a distinct question and carries a structural contract — required sections that make the form's shape predictable. The architecture operates across three layers: authoring (markdown), structure (predicates and graph), and retrieval (agents and search).

This domain is self-referential — the garden that implements the architecture is also the primary test case for it.

## Scope

**Covers**: The type system (form types, status stages, vault types), predicate vocabulary, naming conventions, compound document patterns, retrieval hierarchy, and garden governance. Also covers personal knowledge management method analysis where it informs architectural decisions.

**Does not cover**: Specific knowledge domains indexed by the garden (self-sovereign identity, digital identity). Those are separate domains with their own pages. Also excludes Obsidian-specific tool configuration — this architecture is tool-agnostic in principle, even though Obsidian is the current implementation.

## Key Forms

### Type System and Precincts

The architecture organizes knowledge into two precincts — bounded zones with shared infrastructure but different conventions:

- [\[\[Precinct as Organizational Unit\]\]↑](../NODES.html#:~:text=Precinct%20as%20Organizational%20Unit) — the decision adopting "precinct" from urban planning
- [\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html) — curated forms with structural contracts and growth stages
- [\[\[Vault Precinct\]\]](../glosses/Vault%20Precinct.html) — operational knowledge capture, organization, and retrieval
- [\[\[Form Type\]\]](../forms/Form%20Type.html) — meta-definition of what a form type is
- 17 garden form type definitions: [\[\[Boundary Form\]\]](../forms/Boundary%20Form.html), [\[\[Case Form\]\]↑](../NODES.html#:~:text=Case%20Form), [\[\[Citation Form\]\]](../forms/Citation%20Form.html), [\[\[Conviction Form\]\]](../forms/Conviction%20Form.html), [\[\[Decision Form\]\]](../forms/Decision%20Form.html), [\[\[Domain Form\]\]](../forms/Domain%20Form.html), [\[\[Gloss Form\]\]](../forms/Gloss%20Form.html), [\[\[Inquiry Form\]\]](../forms/Inquiry%20Form.html), [\[\[Model Form\]\]](../forms/Model%20Form.html), [\[\[Opus Form\]\]](../forms/Opus%20Form.html), [\[\[Pattern Form\]\]](../forms/Pattern%20Form.html), [\[\[Principle Form\]\]](../forms/Principle%20Form.html), [\[\[Protocol Form\]\]↑](../NODES.html#:~:text=Protocol%20Form), [\[\[Reference Form\]\]↑](../NODES.html#:~:text=Reference%20Form), [\[\[Research Form\]\]↑](../NODES.html#:~:text=Research%20Form), [\[\[Scenario Form\]\]↑](../NODES.html#:~:text=Scenario%20Form), [\[\[Skill Form\]\]↑](../NODES.html#:~:text=Skill%20Form), [\[\[Value Form\]\]](../forms/Value%20Form.html)
- 4 status stages (shared): [\[\[Seed Stage\]\]](../forms/Seed%20Stage.html), [\[\[Growing Stage\]\]](../forms/Growing%20Stage.html), [\[\[Evergreen Stage\]\]](../forms/Evergreen%20Stage.html), [\[\[Pruned Stage\]\]↑](../NODES.html#:~:text=Pruned%20Stage)
- 5 vault form types: [\[\[Meeting Note\]\]↑](../NODES.html#:~:text=Meeting%20Note), [\[\[Transcript\]\]↑](../NODES.html#:~:text=Transcript), [\[\[Person Note\]\]↑](../NODES.html#:~:text=Person%20Note), [\[\[Chat Log\]\]↑](../NODES.html#:~:text=Chat%20Log), [\[\[Sidecar\]\]↑](../NODES.html#:~:text=Sidecar)

### Founding Decision

- [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html) — the decision to capture reasoning as typed forms with predicates, not fine-tuning, RAG, databases, or tags

### Core Concept

- [\[\[Deep Context as Shared Language\]\]↑](../NODES.html#:~:text=Deep%20Context%20as%20Shared%20Language) — the origin and meaning of "deep context": making implicit understanding explicit and navigable

### Classification and Naming

How forms are identified, named, and classified in the graph:

- [\[\[Classification via Predicates Not Tags\]\]↑](../NODES.html#:~:text=Classification%20via%20Predicates%20Not%20Tags) — the founding decision: body predicates over YAML tags
- [\[\[Descriptive Noun-Phrase Names for Predicate Targets\]\]↑](../NODES.html#:~:text=Descriptive%20Noun-Phrase%20Names%20for%20Predicate%20Targets) — two-word minimum, noun-phrase wikilink targets
- [\[\[Note Titles as APIs\]\]↑](../NODES.html#:~:text=Note%20Titles%20as%20APIs) — Matuschak's insight extended: title shape varies by form type because each answers a different question
- [\[\[Vault Type Targets for Non-Garden Notes\]\]↑](../NODES.html#:~:text=Vault%20Type%20Targets%20for%20Non-Garden%20Notes) — extending `is_a::` to vault precinct forms
- [\[\[Structural Retrieval Hierarchy\]\]↑](../NODES.html#:~:text=Structural%20Retrieval%20Hierarchy) — five tiers from evergreen nodes to binary archives
- [\[\[Snake Case for Predicate Naming\]\]↑](../NODES.html#:~:text=Snake%20Case%20for%20Predicate%20Naming) — editor ergonomics drove the snake_case choice over kebab-case
- [\[\[Spelled-Out Names Over Internal Acronyms\]\]↑](../NODES.html#:~:text=Spelled-Out%20Names%20Over%20Internal%20Acronyms) — spell out names for discoverability; no DCA, SSI, PKM, MOC

### Compound Documents

How multi-file knowledge objects are structured:

- [\[\[Compound Node Anatomy\]\]↑](../NODES.html#:~:text=Compound%20Node%20Anatomy) — the model: lead file + sidecars + archives
- [\[\[Folder-Note Pattern for Compound Documents\]\]↑](../NODES.html#:~:text=Folder-Note%20Pattern%20for%20Compound%20Documents) — lead file shares folder name, no index.md
- [\[\[Display Name Preservation in Compound Documents\]\]↑](../NODES.html#:~:text=Display%20Name%20Preservation%20in%20Compound%20Documents) — human-readable names for sidecars
- [\[\[Universal Compound Form Graduation\]\]↑](../NODES.html#:~:text=Universal%20Compound%20Form%20Graduation) — when atomic forms become compound
- [\[\[Lead File to Sidecar Discovery\]\]↑](../NODES.html#:~:text=Lead%20File%20to%20Sidecar%20Discovery) — navigating from lead file to companions
- [\[\[Lead File Selection Guidance\]\]↑](../NODES.html#:~:text=Lead%20File%20Selection%20Guidance) — choosing the lead file in a compound node

### Artifacts and Archives

How binary and non-markdown artifacts participate in the graph:

- [\[\[Artifact Predicate for Binary Metadata\]\]↑](../NODES.html#:~:text=Artifact%20Predicate%20for%20Binary%20Metadata) — `artifact::` predicate for binaries
- [\[\[Sidecar Files as Metadata Envelopes\]\]↑](../NODES.html#:~:text=Sidecar%20Files%20as%20Metadata%20Envelopes) — markdown proxies for non-markdown files
- [\[\[Non-Local Artifact References in Sidecars\]\]↑](../NODES.html#:~:text=Non-Local%20Artifact%20References%20in%20Sidecars) — source repository + public URL pattern
- [\[\[Descriptive Slugs for Archive Binaries\]\]↑](../NODES.html#:~:text=Descriptive%20Slugs%20for%20Archive%20Binaries) — naming convention for archived files
- [\[\[Renditions and Archives as Distinct Artifact Types\]\]↑](../NODES.html#:~:text=Renditions%20and%20Archives%20as%20Distinct%20Artifact%20Types) — separating processed from raw
- [\[\[Renditions and Archives Replace Sources\]\]↑](../NODES.html#:~:text=Renditions%20and%20Archives%20Replace%20Sources) — new terminology over old "sources" folder
- [\[\[Knowledge Hub Not Binary Archive\]\]↑](../NODES.html#:~:text=Knowledge%20Hub%20Not%20Binary%20Archive) — the vault stores knowledge, not files

### Meeting Capture

How synchronous conversations enter the knowledge graph:

- [\[\[Body Predicates for Meeting Attendees\]\]↑](../NODES.html#:~:text=Body%20Predicates%20for%20Meeting%20Attendees) — `attendee::[\[\[Name\]\]↑](../NODES.html#:~:text=Name)` over YAML arrays
- [\[\[Linear Processing Stages for Meetings\]\]↑](../NODES.html#:~:text=Linear%20Processing%20Stages%20for%20Meetings) — Captured → Transcribed → Cleaned → Summarized → Published
- [\[\[Predicates Everywhere for Compound Nodes\]\]↑](../NODES.html#:~:text=Predicates%20Everywhere%20for%20Compound%20Nodes) — extending predicates to all compound node files
- [\[\[Compound Node Meeting Structure\]\]↑](../NODES.html#:~:text=Compound%20Node%20Meeting%20Structure) — open question on optimal meeting folder layout

### Personal Knowledge Management Method Analysis

Glosses on external personal knowledge management methods that informed architectural decisions:

- [\[\[PARA as Actionability-First Design\]\]↑](../NODES.html#:~:text=PARA%20as%20Actionability-First%20Design) — Forte's system as design input
- [\[\[IPARAG as Extended PARA\]\]↑](../NODES.html#:~:text=IPARAG%20as%20Extended%20PARA) — extending PARA with three new categories
- [\[\[ACE as Three Dimensional Personal Knowledge Management\]\]↑](../NODES.html#:~:text=ACE%20as%20Three%20Dimensional%20Personal%20Knowledge%20Management) — Linking Your Thinking's dimensional model
- [\[\[GRID as Note Type Organization\]\]↑](../NODES.html#:~:text=GRID%20as%20Note%20Type%20Organization) — note type spectrum from Groves to Distillations
- [\[\[Johnny Decimal as Permanent Addressing\]\]↑](../NODES.html#:~:text=Johnny%20Decimal%20as%20Permanent%20Addressing) — fixed numbering as addressing scheme
- [\[\[Digital Garden as Growth Ethos\]\]↑](../NODES.html#:~:text=Digital%20Garden%20as%20Growth%20Ethos) — gardening metaphor as personal knowledge management philosophy
- [\[\[Personal Knowledge Management Organizing Principle Spectrum\]\]↑](../NODES.html#:~:text=Personal%20Knowledge%20Management%20Organizing%20Principle%20Spectrum) — model comparing organizational axes
- [\[\[Personal Knowledge Management Method Adoption for Vault Architecture\]\]↑](../NODES.html#:~:text=Personal%20Knowledge%20Management%20Method%20Adoption%20for%20Vault%20Architecture) — inquiry on which methods to adopt
- [\[\[IPARAG Term Origins\]\]↑](../NODES.html#:~:text=IPARAG%20Term%20Origins) — inquiry on IPARAG acronym provenance
- [\[\[Knowledge on Three Axes\]\]↑](../NODES.html#:~:text=Knowledge%20on%20Three%20Axes) — axes of organization pattern

### Values

Orientations that direct architectural decisions:

- [\[\[Reasoning Fidelity\]\]](../values/Reasoning%20Fidelity.html) — capture how someone reasons, not just what they know
- [\[\[Knowledge Durability\]\]](../values/Knowledge%20Durability.html) — knowledge should outlast the tools used to capture it

### Convictions

- [\[\[Values Precede Technical Decisions\]\]](../convictions/Values%20Precede%20Technical%20Decisions.html) — technical architecture must be grounded in human values; when values and convenience conflict, values win

### Principles and Patterns

Standing constraints and recurring solutions:

- [\[\[Living Documents Over Static Publications\]\]](../principles/Living%20Documents%20Over%20Static%20Publications.html) — garden nodes grow and evolve; the current state matters, not a published version
- [\[\[Content Over Container\]\]](../principles/Content%20Over%20Container.html) — what matters is the knowledge, not its packaging
- [\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html) — augmentation, not autonomy
- [\[\[Standalone Document Test for Form Candidacy\]\]↑](../NODES.html#:~:text=Standalone%20Document%20Test%20for%20Form%20Candidacy) — the test that grounds the entire type taxonomy
- [\[\[Context Conservation Hierarchy\]\]↑](../NODES.html#:~:text=Context%20Conservation%20Hierarchy) — where to invest context budget
- [\[\[Progressive Summary Before Substance\]\]↑](../NODES.html#:~:text=Progressive%20Summary%20Before%20Substance) — inverted pyramid for agent retrieval
- [\[\[Summary Fields as Load-Bearing Infrastructure\]\]↑](../NODES.html#:~:text=Summary%20Fields%20as%20Load-Bearing%20Infrastructure) — 280-char summaries quantified as retrieval infrastructure
- [\[\[Still Knowledge, Moving Action\]\]↑](../NODES.html#:~:text=Still%20Knowledge%2C%20Moving%20Action) — knowledge persists, actions flow
- [\[\[Vault Content Graduation\]\]↑](../NODES.html#:~:text=Vault%20Content%20Graduation) — how vault types mature into garden nodes through tending
- [\[\[Progressive Disclosure Over Eager Loading\]\]](../principles/Progressive%20Disclosure%20Over%20Eager%20Loading.html) — start with the question, follow edges on demand, stop when context suffices
- [\[\[Zero-Tooling Floor for Knowledge Architecture\]\]](../principles/Zero-Tooling%20Floor%20for%20Knowledge%20Architecture.html) — plain markdown, git, and shell — specialized tools add value but are never prerequisites
- [\[\[Predicate Maintenance Recipes Over Tools\]\]↑](../NODES.html#:~:text=Predicate%20Maintenance%20Recipes%20Over%20Tools) — shell one-liners preserve zero-tooling floor
- [\[\[Probe Before Commit\]\]↑](../NODES.html#:~:text=Probe%20Before%20Commit) — probe external state before acting on assumptions about it
- [\[\[Source Adapter for Heterogeneous Imports\]\]↑](../NODES.html#:~:text=Source%20Adapter%20for%20Heterogeneous%20Imports) — source-specific adapters extract; common normalization maps to conventions
- [\[\[Domain Extensions on Common Frontmatter Base\]\]↑](../NODES.html#:~:text=Domain%20Extensions%20on%20Common%20Frontmatter%20Base) — common base plus content-type extensions over monolithic schema
- [\[\[Lightweight Governance for Personal Gardens\]\]↑](../NODES.html#:~:text=Lightweight%20Governance%20for%20Personal%20Gardens) — rule file plus reference file, not full quad for single-user gardens
- [\[\[Temporary Predicate Scaffolding\]\]↑](../NODES.html#:~:text=Temporary%20Predicate%20Scaffolding) — build predicates for a purpose, use them, then remove before graph pollution
- [\[\[Git Tags for Sent-Version Tracking\]\]↑](../NODES.html#:~:text=Git%20Tags%20for%20Sent-Version%20Tracking) — git tags track what recipients received of living documents
- [\[\[Cross-Project Learning Repatriation\]\]↑](../NODES.html#:~:text=Cross-Project%20Learning%20Repatriation) — learnings belong where consumed, not where produced
- [\[\[Informal Edges Poison the Graph\]\]↑](../NODES.html#:~:text=Informal%20Edges%20Poison%20the%20Graph) — uncurated predicates compound into retrieval failure (anti-pattern)
- [\[\[One Context One Concern\]\]↑](../NODES.html#:~:text=One%20Context%20One%20Concern) — separate research and implementation into distinct contexts connected by compressed handoff
- [\[\[Ghost Links as Garden Planning Tools\]\]↑](../NODES.html#:~:text=Ghost%20Links%20as%20Garden%20Planning%20Tools) — treat unresolved wikilinks as planning tools, not lint errors; prioritize writing by incoming predicate count
- [\[\[Graph Structure Validation for Garden Nodes\]\]↑](../NODES.html#:~:text=Graph%20Structure%20Validation%20for%20Garden%20Nodes) — graph-level lint complementing form-level validation: predicate presence, domain membership, orphan detection

### Inquiries

Open investigations into architectural questions:

- [\[\[Form Type Distinctiveness in Naming and Structure\]\]↑](../NODES.html#:~:text=Form%20Type%20Distinctiveness%20in%20Naming%20and%20Structure) — whether 16 form types are distinguishable in practice by naming patterns and structural contracts
- [\[\[Inquiry Lifecycle and Resolution\]\]↑](../NODES.html#:~:text=Inquiry%20Lifecycle%20and%20Resolution) — when an inquiry is "done" and what resolution means for a generative form
- [\[\[Predicate Vocabulary Stabilization\]\]↑](../NODES.html#:~:text=Predicate%20Vocabulary%20Stabilization) — freeform predicates past 200+ threshold; when to audit and stabilize
- [\[\[Cross-Domain Form Indexing\]\]↑](../NODES.html#:~:text=Cross-Domain%20Form%20Indexing) — how domain pages handle forms that belong to multiple domains
- [\[\[Domains and Pattern Languages as Organizational Concepts\]\]](../inquiries/Domains%20and%20Pattern%20Languages%20as%20Organizational%20Concepts.html) — whether pattern languages are a view of a domain or a distinct organizational concept
- [\[\[Productivity Separation from Knowledge Vault\]\]↑](../NODES.html#:~:text=Productivity%20Separation%20from%20Knowledge%20Vault) — whether garden and productivity content should separate into distinct vaults
- [\[\[Cooperation vs Collaboration as Distinct Concepts\]\]](../inquiries/Cooperation%20vs%20Collaboration%20as%20Distinct%20Concepts.html) — distinguishing cooperation and collaboration as separate research threads
- [\[\[Vault-Wide Compound Node Adoption\]\]↑](../NODES.html#:~:text=Vault-Wide%20Compound%20Node%20Adoption) — strategy for converting existing atomic notes to compound structure
- [\[\[Scenario Lifecycle and Aging\]\]↑](../NODES.html#:~:text=Scenario%20Lifecycle%20and%20Aging) — how scenarios age when validated, invalidated, or overtaken by events
- [\[\[Group Deliberation Mechanism\]\]](../inquiries/Group%20Deliberation%20Mechanism.html) — practical mechanism when an agent hits a group-deliberative boundary
- [\[\[Trust Layer Activation Criteria\]\]](../inquiries/Trust%20Layer%20Activation%20Criteria.html) — what triggers the transition from markdown-only to cryptographically-verified exchange
- [\[\[Garden Publishing Path\]\]↑](../NODES.html#:~:text=Garden%20Publishing%20Path) — how to publish the garden preserving typed relations, balancing fidelity, features, and minimalism
- [\[\[Custom Python Generator for Typed Relations\]\]↑](../NODES.html#:~:text=Custom%20Python%20Generator%20for%20Typed%20Relations) — decision: ~150-line Python generator over Quartz, Jekyll, Eleventy, and Pandoc
- [\[\[Universal Document Lifecycle State Machine\]\]↑](../NODES.html#:~:text=Universal%20Document%20Lifecycle%20State%20Machine) — is there one lifecycle model for wiki pages, garden nodes, and agent context files?
- [\[\[Automated Gardening Trust Problem\]\]↑](../NODES.html#:~:text=Automated%20Gardening%20Trust%20Problem) — can agents garden their own instructions, or does self-modification require human oversight?
- [\[\[Living Document Scale Limits\]\]↑](../NODES.html#:~:text=Living%20Document%20Scale%20Limits) — is there a practical threshold where gardening cost exceeds accumulated value?
- [\[\[Graph-Native Skill Execution\]\]↑](../NODES.html#:~:text=Graph-Native%20Skill%20Execution) — how skills can discover and load garden nodes through predicate traversal rather than hardcoded paths

### Models

Structural relationships within the architecture:

- [\[\[Captured Reasoning Exchange Pipeline\]\]↑](../NODES.html#:~:text=Captured%20Reasoning%20Exchange%20Pipeline) — how reasoning moves through the system
- [\[\[Principal-Agent Relationship in Augmented Knowledge Work\]\]](../models/Principal-Agent%20Relationship%20in%20Augmented%20Knowledge%20Work.html) — vault as delegated authority
- [\[\[Authority Conferral Chain\]\]](../models/Authority%20Conferral%20Chain.html) — three types of delegation (from Self-Sovereign Identity, bridges to Deep Context Architecture)
- [\[\[Quad Model Mapping to Forms\]\]↑](../NODES.html#:~:text=Quad%20Model%20Mapping%20to%20Forms) — how the quad maps onto form types as facets
- [\[\[Status Lifecycle Tracks\]\]↑](../NODES.html#:~:text=Status%20Lifecycle%20Tracks) — three status tracks for three kinds of knowledge work (maturity, curation, processing)
- [\[\[Document Lifecycle Governance Heuristics\]\]↑](../NODES.html#:~:text=Document%20Lifecycle%20Governance%20Heuristics) — wiki split/merge/delete heuristics applied to garden tending and agent context
- [\[\[Cross-Domain Document Lifecycle Parallels\]\]↑](../NODES.html#:~:text=Cross-Domain%20Document%20Lifecycle%20Parallels) — wiki, garden, and agent context face the same lifecycle problems under different constraints
- [\[\[Sycophantic Confidence Spiral\]\]↑](../NODES.html#:~:text=Sycophantic%20Confidence%20Spiral) — AI agreement-bias creates circular evidence that concentrates beliefs without approaching truth
- [\[\[Vocabulary Lifecycle Through Tending\]\]↑](../NODES.html#:~:text=Vocabulary%20Lifecycle%20Through%20Tending) — growing vocabularies degrade without continuous weeding, seeding, and fertilizing

### Reference

- [\[\[Structural Elements Within Forms\]\]↑](../NODES.html#:~:text=Structural%20Elements%20Within%20Forms) — where non-form knowledge types live (ADR, Narrative, Warrant, Signal, Commitment, Lexicon, Tension)

### Boundary

- [\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html) — where agent authority begins and ends

### Citations

- [\[\[Roy (2026) Words Without Consequence, from The Atlantic\]\]↑](../NODES.html#:~:text=Roy%20%282026%29%20Words%20Without%20Consequence%2C%20from%20The%20Atlantic) — speech without a speaker who bears consequence erodes the moral structure of language; grounds [\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
- [\[\[Chatlatanagulchai (2025) Agent READMEs\]\]↑](../NODES.html#:~:text=Chatlatanagulchai%20%282025%29%20Agent%20READMEs) — empirical study validating that agent context files behave as living configurations, not static documentation
- [\[\[Altshuler (2026) Nanograph On-Device GraphDB\]\]↑](../NODES.html#:~:text=Altshuler%20%282026%29%20Nanograph%20On-Device%20GraphDB) — on-device schema-enforced graph database; independent validation of typed predicates over freeform edges and local-first data sovereignty
- [\[\[systematicls (2026) World-Class Agentic Engineering\]\]↑](../NODES.html#:~:text=systematicls%20%282026%29%20World-Class%20Agentic%20Engineering) — practitioner guide on context management, rule/skill lifecycle, and task contracts; validates context conservation and progressive disclosure patterns
- [\[\[arscontexta (2026) Skill Graphs\]\]↑](../NODES.html#:~:text=arscontexta%20%282026%29%20Skill%20Graphs) — wikilink-connected skill files as traversable knowledge graphs; independent validation of predicate-linked progressive disclosure
- [\[\[Rajasekaran (2025) Effective Context Engineering for AI Agents\]\]↑](../NODES.html#:~:text=Rajasekaran%20%282025%29%20Effective%20Context%20Engineering%20for%20AI%20Agents) — Anthropic's engineering guide on attention budgets, sub-agent isolation, and progressive disclosure; validates context conservation patterns
- [\[\[Batista (2026) Rational Analysis of Sycophantic AI\]\]↑](../NODES.html#:~:text=Batista%20%282026%29%20Rational%20Analysis%20of%20Sycophantic%20AI) — Bayesian proof that sycophancy creates circular evidence inflating confidence without truth convergence; grounds human authority concerns
- [\[\[Peters (2008) Tag Gardening for Folksonomy Enrichment\]\]↑](../NODES.html#:~:text=Peters%20%282008%29%20Tag%20Gardening%20for%20Folksonomy%20Enrichment) — formalizes seed/weed/fertilize vocabulary maintenance model; grounds predicate vocabulary curation methodology

### Protocols

- [\[\[Inter-Face Protocol\]\]](../protocols/Inter-Face%20Protocol.html) — peer-to-peer AI agent communication that filters social connections to surface conversations worth having

### Scenarios

- [\[\[Knowledge Graph as Digital Twin of Principal Reasoning\]\]↑](../NODES.html#:~:text=Knowledge%20Graph%20as%20Digital%20Twin%20of%20Principal%20Reasoning) — what happens when gardens grow dense enough that agents shift from augmentation toward delegation

### Cases

- [\[\[Hybrid Bootstrapping for Garden Migration\]\]↑](../NODES.html#:~:text=Hybrid%20Bootstrapping%20for%20Garden%20Migration) — the first garden bootstrap: script-extract structure, hand-author interpretation
- [\[\[Architecture Document Extraction to Garden Forms\]\]↑](../NODES.html#:~:text=Architecture%20Document%20Extraction%20to%20Garden%20Forms) — decomposing a 450-line architecture document into 80+ typed garden nodes across 12 sessions

### Garden Migration

- [\[\[Extraction Model for Garden Migration\]\]↑](../NODES.html#:~:text=Extraction%20Model%20for%20Garden%20Migration) — migration as extraction, not relocation

## Open Questions

- How should domain pages handle cross-domain forms? (e.g., [\[\[Authority Conferral Chain\]\]](../models/Authority%20Conferral%20Chain.html) bridges Deep Context Architecture and Self-Sovereign Identity)
- What's the right governance weight for a personal garden? (Currently: lightweight rule + reference, no full quad)
- ~~Should the architecture document itself be extracted into garden nodes, or does it serve better as a monolithic reference?~~ Resolved: extraction is the right approach. All unique content extracted to 17+ garden nodes. The architecture doc itself became a Decision form; the original reference doc is archived (git tag: `archive/dca-architecture-doc/2026-03-07`).

## Sources

- [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html) — founding decision: typed forms with predicates over alternatives
- [\[\[Deep Context Garden Conventions\]\]↑](../NODES.html#:~:text=Deep%20Context%20Garden%20Conventions) — implementation conventions for this vault
- [\[\[Deep Context Content Decision Records\]\]↑](../NODES.html#:~:text=Deep%20Context%20Content%20Decision%20Records) — ADRs for content decisions
- [\[\[Deep Context Implementation Roadmap\]\]↑](../NODES.html#:~:text=Deep%20Context%20Implementation%20Roadmap) — phase-by-phase build plan

## Relations

- relates_to::[\[\[Self-Sovereign Identity\]\]](Self-Sovereign%20Identity.html) — Self-Sovereign Identity provides the first non-Deep Context Architecture domain content; agency law concepts bridge both
- relates_to::[\[\[Digital Identity\]\]↑](../NODES.html#:~:text=Digital%20Identity) — parent domain in Categories/; Deep Context Architecture forms may eventually contribute