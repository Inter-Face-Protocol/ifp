← [Garden Patch Home](./)

# Node Directory

Complete listing of every node referenced in this garden patch — whether it lives here, in the source garden, or nowhere yet.

| Marker | Meaning |
|---|---|
| *(none)* | **Grafted** — copied from the source garden into this patch |
| ⊙ | **Patch-native** — born in this patch; this is its garden home |
| ↑ | **Upstream** — exists in the source garden but not grafted here |

**79 grafted nodes** · **24 patch-native⊙ nodes** · **136 upstream↑ nodes documented** · 42 unlocated references (ghost links or informal references)

---

## Patch-Native Nodes⊙

These nodes were created specifically for this garden patch. This patch is their garden home.

### Glosses⊙

**[\[\[Agent as Human Proxy in Protocol Exchange\]\]⊙](glosses/Agent%20as%20Human%20Proxy%20in%20Protocol%20Exchange.html)** — In Inter-Face Protocol, an agent is autonomous software that acts on behalf of a human operator — not as an independent actor, but as a proxy whose authority derives from and returns to the person. The agent's autonomy is bounded: it may filter, exchange, and probe, but the human decides whether to act on what the agent surfaces.

**[\[\[Capability as Advertised Agent Function\]\]⊙](glosses/Capability%20as%20Advertised%20Agent%20Function.html)** — In Inter-Face Protocol, a capability is a function an agent advertises it can perform — discovered through endpoint queries or greeting-phase exchange. Capabilities are conditional: what an agent can do depends on the disclosure tier, authentication level, and conversation temperature of the current exchange.

**[\[\[Disclosure Tier as Information Sharing Boundary\]\]⊙](glosses/Disclosure%20Tier%20as%20Information%20Sharing%20Boundary.html)** — A disclosure tier defines what information an agent may share with a specific peer in a specific persona context. IFP defines six tiers from public to close, each representing a boundary the agent respects when exchanging context. Tiers are self-declared, mutual but not necessarily symmetric, and deepen over time as trust builds.

**[\[\[Gossip as Social Sensing Filter\]\]⊙](glosses/Gossip%20as%20Social%20Sensing%20Filter.html)** — In Inter-Face Protocol, 'gossip' is not chatter — it is a filtering mechanism. Agents exchange context pairwise to detect overlaps worth human attention. The value is in what gossip does not surface. Most exchanges produce silence; recommendations emerge only when the overlap is actionable, timely, and specific.

**[\[\[Persona as Emergent Context Cluster\]\]⊙](glosses/Persona%20as%20Emergent%20Context%20Cluster.html)** — In Inter-Face Protocol, a persona is a coherent subset of a person's full context — not a mask or role, but a genuine reflection of how interests naturally cluster around communities, projects, and relationships. Personas emerge from agent observation of communication patterns rather than requiring explicit enumeration by the human.

**[\[\[Recommendation as Surfaced Opportunity\]\]⊙](glosses/Recommendation%20as%20Surfaced%20Opportunity.html)** — In Inter-Face Protocol, a recommendation is what survives the gossip filter — a suggestion that two humans should talk, surfaced by agents only when an overlap is actionable, timely, and specific. Recommendations are the protocol's primary output to humans, and their quality measures the system's value.

**[\[\[Relay as Accountable Store-and-Forward Intermediary\]\]⊙](glosses/Relay%20as%20Accountable%20Store-and-Forward%20Intermediary.html)** — In Inter-Face Protocol, a relay is a store-and-forward service that accepts, stores, and delivers messages between agents that cannot reach each other directly. Unlike opaque intermediaries, IFP relays must append trace entries to every message — making their involvement visible and auditable by humans.

### Models⊙

**[\[\[Conversation Temperature as Protocol Cadence Spectrum\]\]⊙](models/Conversation%20Temperature%20as%20Protocol%20Cadence%20Spectrum.html)** — Temperature in Inter-Face Protocol describes conversation intensity as a spectrum — cool (weekly background gossip), warm (daily to hourly active interest), and hot (near-synchronous collaboration). Same protocols, same message formats, different cadences. Temperature shapes rate limiting, capability availability, and escalation thresholds.

**[\[\[Disclosure Tier Hierarchy for Persona-Peer Relationships\]\]⊙](models/Disclosure%20Tier%20Hierarchy%20for%20Persona-Peer%20Relationships.html)** — Inter-Face Protocol organizes information sharing through a six-tier hierarchy from public to close, applied per persona-peer pair. Each tier defines a boundary the agent respects. Tiers are self-declared, mutual but not symmetric, and deepen over time. The model maps how disclosure, persona, and peer identity intersect.

**[\[\[Progressive Authentication as Trust Deepening\]\]⊙](models/Progressive%20Authentication%20as%20Trust%20Deepening.html)** — Inter-Face Protocol defines four authentication levels that deepen alongside trust rather than demanding maximum-strength verification upfront. Level 0 uses a shared introduction token; Level 1 adds public-key signatures; Level 2 verifies keys through identity documents; Level 3 binds identity to a DID or external verification. No downgrading within an exchange.

**[\[\[Social Conversation Phases as Protocol Semantics\]\]⊙](models/Social%20Conversation%20Phases%20as%20Protocol%20Semantics.html)** — Inter-Face Protocol defines six conversation phases — greeting, context, probe, recommend, close, error — that are social in nature, not mechanical. Phases are advisory, revisitable, and named in the message envelope. They model how trust-building conversations naturally progress rather than imposing request-response mechanics.

### Inquiries⊙

**[\[\[Convergence and Divergence Across Agent Application Platforms\]\]⊙](inquiries/Convergence%20and%20Divergence%20Across%20Agent%20Application%20Platforms.html)** — IFP-11 describes eleven application platforms as distinct categories, but several share characteristics: Friend Zone and Guild Hall both manage relationship maintenance, Bazaar and Guild Hall both involve reputation-dependent matching. This inquiry asks where platforms genuinely diverge in protocol requirements and where apparent boundaries are artificial.

**[\[\[Disclosure Spectrum as Discrete Tiers or Continuous Range\]\]⊙](inquiries/Disclosure%20Spectrum%20as%20Discrete%20Tiers%20or%20Continuous%20Range.html)** — IFP-12 defines six named disclosure tiers (public through close) as a discrete hierarchy. This inquiry asks whether discrete tiers are the right model — whether a continuous range would better capture the nuance of information sharing, whether the specific tier names impose cultural assumptions, and whether six is the right number.

**[\[\[Granularity of Progressive Authentication Stages\]\]⊙](inquiries/Granularity%20of%20Progressive%20Authentication%20Stages.html)** — IFP defines four authentication levels (shared secret, signed, verified, DID-bound) as discrete stages in a progressive trust model. This inquiry asks whether four stages capture the right boundaries — whether the jumps between levels are too large, whether intermediate stages are missing, and whether the Level 0 shared-secret starting point is appropriate for all contexts.

**[\[\[Living Knowledge vs Static Archive in Agent Library Design\]\]⊙](inquiries/Living%20Knowledge%20vs%20Static%20Archive%20in%20Agent%20Library%20Design.html)** — IFP-11's Library platform spans personal knowledge management, group knowledge, and public encyclopedia under a single name. This inquiry asks whether the Library collapses distinct knowledge management paradigms — living documents that grow through tending vs static archives that are curated and preserved — and whether these require different protocol behaviors.

**[\[\[Organizing Principle for Agent Application Domains\]\]⊙](inquiries/Organizing%20Principle%20for%20Agent%20Application%20Domains.html)** — IFP-11 describes eleven application platforms (Friend Zone, Bazaar, Guild Hall, etc.) but does not articulate a clear organizing principle for why these eleven and not others. This inquiry asks what principle should govern the taxonomy — by trust requirements, by temperature, by human need, or by protocol feature usage.

**[\[\[Social Phase Decomposition in Trust-Building Protocols\]\]⊙](inquiries/Social%20Phase%20Decomposition%20in%20Trust-Building%20Protocols.html)** — IFP-3 defines six conversation phases — greeting, context, probe, recommend, close, error — modeled as social interactions rather than mechanical request-response. This inquiry asks whether this decomposition captures the right stages of trust-building conversation, whether phases are missing or redundant, and whether the social framing holds under adversarial conditions.

**[\[\[Structured Schema vs Natural Language for Agent Message Content\]\]⊙](inquiries/Structured%20Schema%20vs%20Natural%20Language%20for%20Agent%20Message%20Content.html)** — IFP-3 uses natural language for message bodies rather than structured schemas. This is one of IFP's most consequential architectural decisions, yet the justification is thin: 'agents are good at NLP.' This inquiry examines the trade-offs — what natural language enables, what it makes harder, and whether hybrid approaches might preserve the benefits of both.

**[\[\[When to Specify and When to Explore in Protocol Evolution\]\]⊙](inquiries/When%20to%20Specify%20and%20When%20to%20Explore%20in%20Protocol%20Evolution.html)** — Protocol evolution involves a tension between specifying details (creating interoperability commitments) and leaving space for implementation discovery. IFP currently specifies both load-bearing architecture and tactical details at the same level. This inquiry asks how to distinguish what should be committed in specifications from what should remain open for exploration.

### Patterns⊙

**[\[\[Dual Representation for Human and Machine Readability\]\]⊙](patterns/Dual%20Representation%20for%20Human%20and%20Machine%20Readability.html)** — Inter-Face Protocol maintains two equivalent representations of every message: IFP-3 (YAML envelope plus natural-language body, human-readable) and IFP-4 (JSON canonical form, machine-processable for signing and transport). Conversion between them is lossless. This resolves the tension between human legibility and cryptographic operations.

**[\[\[Errors as Negotiation Opportunities\]\]⊙](patterns/Errors%20as%20Negotiation%20Opportunities.html)** — In agent-age protocols, errors are not failures to be coded and returned — they are opportunities for natural-language negotiation. When an agent receives a message it does not understand, it describes the problem conversationally, giving the sender an opportunity to rephrase. This resolves the tension between strict semantics and graceful communication.

### Convictions⊙

**[\[\[Personas Emerge from Observation Not Enumeration\]\]⊙](convictions/Personas%20Emerge%20from%20Observation%20Not%20Enumeration.html)** — People do not experience their interests as cleanly separated categories. Systems that require explicit role enumeration force false boundaries. Inter-Face Protocol's conviction is that personas should emerge from agent observation of communication patterns — the agent notices clusters, not the human defining them.

### Decisions⊙

**[\[\[Clarity Over Tolerance in Agent-Age Protocols\]\]⊙](decisions/Clarity%20Over%20Tolerance%20in%20Agent-Age%20Protocols.html)** — Inter-Face Protocol explicitly replaces Postel's Law ('be liberal in what you accept') with a clarity-first principle for agent-age protocols. When agents can be updated in minutes, silent tolerance of deviations entrenches errors as workarounds. Strict error reporting with natural-language negotiation enables rapid correction.

### Principles⊙

**[\[\[Auditable Intermediaries Over Silent Proxies\]\]⊙](principles/Auditable%20Intermediaries%20Over%20Silent%20Proxies.html)** — Any intermediary that handles messages between agents must leave an auditable trace — recording when it received the message, from whom, and any transformations applied. Silent proxies that forward or modify messages without visible traces violate the human legibility constraint. Trace is mandatory, not optional.

---

## Grafted Nodes

These nodes were copied from the source garden into this patch.

### Forms

**[\[\[Boundary Form\]\]](forms/Boundary%20Form.html)** — Defines the Boundary form type: a declaration of what an agent may and may not decide. Not what the right choice is, not how to make it, but who holds authority. Amendable through deliberative process, never unilaterally. 1 instance in Garden/boundaries/.

**[\[\[Citation Form\]\]](forms/Citation%20Form.html)** — Defines the Citation form type: a structured dossier on a single work containing bibliographic entry, summary, key points, key quotes, influence, sources, and relations. Named as Author (Year) Abbreviated Title. Atomic at Seed stage, graduating to compound (analysis.md, insights.md, Renditions/, Archives/) as analysis deepens. Append-only.

**[\[\[Conviction Form\]\]](forms/Conviction%20Form.html)** — Defines the Conviction form type: an assertion about reality that isn't self-evident, grounding values and principles. Near-immutable — a change represents a fundamental shift. Names are declarative claims, not topics.

**[\[\[Decision Form\]\]](forms/Decision%20Form.html)** — Defines the Decision form type: a recorded choice with reasoning, alternatives considered, and consequences. Structural contract requires Context, Decision, Consequences, and Alternatives Considered sections in order. Distinguished from cases (which narrate what happened) by being forward-looking and from principles by being situation-specific.

**[\[\[Domain Form\]\]](forms/Domain%20Form.html)** — Defines the Domain form type: a navigational and structural index for a field of knowledge — its scope, key nodes, open questions, and connections to other domains. A gardener's workbench for working within a knowledge area. 3 nodes in Garden/domains/.

**[\[\[Evergreen Stage\]\]](forms/Evergreen%20Stage.html)** — Defines the Evergreen Stage: a mature garden node that is well-linked, trustworthy, and stable across multiple editing sessions. Highest confidence for agent retrieval. Content has been validated through citation by other nodes, tested against sources, and requires no structural revision. Borrows from Matuschak's evergreen notes concept.

**[\[\[Form Type\]\]](forms/Form%20Type.html)** — A form type is a knowledge object category with a known internal structure — a contract about what sections it contains and what question it answers. 17 form types are defined across five categories (Orientation, Structural, Action, Generative, Governance).

**[\[\[Gloss Form\]\]](forms/Gloss%20Form.html)** — Defines the Gloss form type: an interpretive annotation anchored to specific sources. Thesis-driven synthesis with organized citations. The atomic unit of interpretation. 12 nodes in Garden/glosses/.

**[\[\[Growing Stage\]\]](forms/Growing%20Stage.html)** — Defines the Growing Stage, the active tending phase where nodes gain structure, links, and editorial attention. A growing node demonstrates its structural contract and has been revisited at least once, but remains incomplete or untested. Most nodes spend the majority of their lifecycle here. Mid-confidence for retrieval.

**[\[\[Inquiry Form\]\]](forms/Inquiry%20Form.html)** — Defines the Inquiry form type: a thesis-driven investigation that marshals evidence, proposes hypotheses, and directs questions at specific people. The primary generative form — inquiries produce cases, patterns, and references. 11 nodes in Garden/inquiries/.

**[\[\[Model Form\]\]](forms/Model%20Form.html)** — Defines the Model form type: a structural representation showing elements, relationships, boundaries, and feedback loops. How things relate to each other. Evolving as understanding grows. Models are explanatory (how things work), distinct from patterns (what to do) and scenarios (what might happen).

**[\[\[Opus Form\]\]](forms/Opus%20Form.html)** — Defines the Opus form type: a compound garden node for the author's own substantial intellectual works. Lead file contains the work itself (living document), supported by analysis.md, insights.md, and sub-folders for Expressions (published venues), Renditions (drafts and derived versions), and Archives (binary artifacts). Opuses nest recursively. Attribution uses role-specific predicates grounded in the principal-agent framework.

**[\[\[Pattern Form\]\]](forms/Pattern%20Form.html)** — Defines the Pattern form type: a problem-solution pair in Alexandrian form with context, forces in tension, solution, consequences, and connections. Validated or invalidated by cases. 16 nodes in Garden/patterns/.

**[\[\[Principle Form\]\]](forms/Principle%20Form.html)** — Defines the Principle form type: a decision constraint derived from values that compresses patterns and experience into actionable heuristics. What must we always or never do. Stable; refined through cases but rarely overturned. 7 instances in Garden/principles/.

**[\[\[Protocol Form\]\]](forms/Protocol%20Form.html)** — Defines the Protocol form type: a specification for multi-party coordination across trust boundaries. Distinguished from a process by who must agree — a protocol works only if all parties follow it. Scope includes human coordination methods alongside technical protocols.

**[\[\[Scenario Form\]\]](forms/Scenario%20Form.html)** — Defines the Scenario form type: a plausible narrative of how the future could unfold given specific drivers and conditions. Scenarios don't predict — they prepare. Value lies in spanning the possibility space. Names state the hypothetical trajectory, not the driving forces.

**[\[\[Seed Stage\]\]](forms/Seed%20Stage.html)** — Defines the Seed Stage, the entry point for all garden nodes: raw capture with low confidence, unprocessed structure, and minimal links. Seeds are extraction products that have enough content to stand alone but have not been tested against other nodes, verified, or refined through use.

**[\[\[Value Form\]\]](forms/Value%20Form.html)** — Defines the Value form type: an orientation toward what matters. Values don't prescribe action — they orient it. Slow-changing, evolving over decades. Names are abstract noun phrases — the value itself, not a claim about it.

### Domains

**[\[\[Deep Context Architecture\]\]](domains/Deep%20Context%20Architecture.html)** — Domain index for Deep Context Architecture — a system for capturing reasoning as typed markdown nodes connected by predicates, organized into precincts (garden and vault). Covers precincts, type system, lifecycle tracks, compound documents, naming, classification, meeting capture, personal knowledge management methods, and retrieval.

**[\[\[Self-Sovereign Identity\]\]](domains/Self-Sovereign%20Identity.html)** — Domain index for Self-Sovereign Identity in the garden — 4 nodes covering the principal authority framework from agency law. Self-Sovereign Identity provides the first non-Deep Context Architecture domain content, bridging identity principles to the vault's augmented knowledge architecture.

**[\[\[Synpraxis\]\]](domains/Synpraxis.html)** — Domain index for Synpraxis — the study of how independent agents achieve outcomes together across varying degrees of integration. From Greek syn (together) + praxis (purposeful action). Covers the full spectrum from loose coordination through cooperation to deep collaboration, including anti-patterns: defection, free-riding, parasitism, coercion, and capture. Spans biology, game theory, governance, organizational theory, computer science, and the arts.

### Models

**[\[\[Authority Conferral Chain\]\]](models/Authority%20Conferral%20Chain.html)** — Model defining the formal predicate vocabulary for principal authority relationships in BCR-2026-xxx. Seven predicates encode who directed work, who asserts authority was conferred, what scope and constraints apply, and the full chain from principal to agent. Includes three conditions for meaningful authority and a Type A/B/C classification of delegation relationships.

**[\[\[Choice Architecture and Exit Rights\]\]](models/Choice%20Architecture%20and%20Exit%20Rights.html)** — Model of how initially voluntary digital choices accumulate into coercive dependencies through credential chains, platform lock-in, and exit penalties. When credentials, reputation, and relationships accumulate in one ecosystem, switching means losing recognized standing. Maps to the Exit → Erasure inversion in The Architecture of Autonomy.

**[\[\[Coercion Resistance as Meta-Lens\]\]](models/Coercion%20Resistance%20as%20Meta-Lens.html)** — Meta-lens framework showing how coercion operates across four dimensions in digital identity systems: interface (dark patterns), inference (behavioral profiling), structural (lock-in), and psychological (self-censorship). Each dimension has a specialized sub-lens. The chain Visibility → Legibility → Control → Coercion describes how identity systems escalate from observation to coercion.

**[\[\[Collaborative Meeting as Composable Knowledge Pipeline\]\]](models/Collaborative%20Meeting%20as%20Composable%20Knowledge%20Pipeline.html)** — Seven-stage pipeline for turning collaborative meetings into garden nodes, tool notes, person notes, and patch updates. Stages: pre-work (agenda from prior session output), meeting, compound capture (audio+transcript+folder), post-processing (cleanup+notes+triage), garden integration (seed+graft+repatriate), report-out (cover letter+zip+PR merge), and close. Each stage filters — a 90-minute call produced 120+ patch files, 9 tool notes, 4 person notes, 8 garden nodes, and 8 garden-foundation tasks. First exercised on the 2026-03-19 Peter Kaminski garden patch review.

**[\[\[Conversational Repair Organization\]\]](models/Conversational%20Repair%20Organization.html)** — Schegloff's four repair types mapped to agent protocol behaviors: self-initiated self-repair, self-initiated other-repair, other-initiated self-repair, and other-initiated other-repair. Protocols giving the error-producing agent first opportunity to self-correct produce better outcomes. Continuous self-monitoring beats error-state handling.

**[\[\[Cross-Domain Document Lifecycle Parallels\]\]](models/Cross-Domain%20Document%20Lifecycle%20Parallels.html)** — Three domains — wiki communities, digital gardens, and AI agent context systems — face the same document lifecycle problems (splitting, staleness, ownership, deletion) under different constraints. Maps the parallels and identifies where the analogy breaks down: statelessness, read frequency, token economics, and automated maintenance.

**[\[\[Document Lifecycle Governance Heuristics\]\]](models/Document%20Lifecycle%20Governance%20Heuristics.html)** — Maps wiki governance heuristics for document lifecycle (split, merge, redirect, delete, draftify) to garden and agent context operations. Includes failure modes: the append-only trap (growth by accretion without consolidation) and structure ossification (resistance to reorganization over time).

**[\[\[Grounding Constraints Across Communication Media\]\]](models/Grounding%20Constraints%20Across%20Communication%20Media.html)** — Clark and Brennan's eight grounding constraints — copresence, visibility, audibility, contemporality, simultaneity, sequentiality, reviewability, revisability — mapped across communication channels from face-to-face to structured data APIs. As channels shift from synchronous to asynchronous, they trade repair speed for message permanence.

**[\[\[Pace Layers for Knowledge and Agent Systems\]\]](models/Pace%20Layers%20for%20Knowledge%20and%20Agent%20Systems.html)** — Stewart Brand's six pace layers — fashion, commerce, infrastructure, governance, culture, nature — mapped to both garden form types and agent platform components. Fast layers experiment, slow layers remember. Forced synchronization between layers at different rates destroys the system. Each component has a characteristic rate of change.

**[\[\[Principal-Agent Relationship in Augmented Knowledge Work\]\]](models/Principal-Agent%20Relationship%20in%20Augmented%20Knowledge%20Work.html)** — Model mapping BCR-2026-xxx principal authority terminology to the vault's augmented knowledge system. The vault owner is the principal, Claude Code sessions are agents, rules and skills are conferrals, and the three conditions for meaningful authority (legibility, boundaries, override) are satisfied through session logs, process constraints, and human approval gates.

**[\[\[Status Lifecycle Tracks\]\]](models/Status%20Lifecycle%20Tracks.html)** — Three status tracks for three kinds of knowledge work. Maturity (Seed→Growing→Evergreen→Pruned) for living documents, curation (uncurated→curated→annotated) for static captures, processing (Captured→Transcribed→Cleaned→Summarized→Published) for meetings. The has_status:: predicate is universal; the vocabulary varies by node type.

**[\[\[Vocabulary Lifecycle Through Tending\]\]](models/Vocabulary%20Lifecycle%20Through%20Tending.html)** — Model unifying the degradation mechanism common to growing vocabularies, configuration systems, and knowledge graphs. Any accumulating terminology — predicates, tags, rules, skills — degrades retrieval effectiveness without continuous tending. Three gardening activities maintain health: weeding (removing malformed entries), seeding (introducing needed specificity), and fertilizing (enriching with semantic structure).

### Glosses

**[\[\[Deep Context Graph Vocabulary\]\]](glosses/Deep%20Context%20Graph%20Vocabulary.html)** — Deep context is a typed graph in plain markdown — documents are nodes, predicate wikilinks are edges. Defines seven structural terms (context node, typed edge, compound node, lead file, rendition, archive, sidecar), four classification predicates, and the full semantic predicate catalog in four categories (provenance, structural, lifecycle, generative).

**[\[\[Garden Patch as Composable Knowledge Fragment\]\]](glosses/Garden%20Patch%20as%20Composable%20Knowledge%20Fragment.html)** — A garden patch is a portable, self-contained subset of a garden placed alongside external content to reveal connections through typed knowledge forms. It carries grafted nodes (copied from the source garden), patch-native nodes⊙ (born in the patch), form definitions, and a node directory. Patches function as forks — they diverge from the source garden as they grow, and changes can merge back upstream.

**[\[\[Garden Precinct\]\]](glosses/Garden%20Precinct.html)** — The garden precinct is the zone within Deep Context Architecture where knowledge is curated into typed nodes with structural contracts, tended through growth stages (Seed to Evergreen), and interconnected by typed predicates. It solves the problem of making knowledge retrievable, composable, and trustworthy over time.

**[\[\[Ghost Link as Unplanted Garden Stake\]\]](glosses/Ghost%20Link%20as%20Unplanted%20Garden%20Stake.html)** — A ghost link is a wikilink reference to a node that does not exist yet — neither in this garden patch nor in the source garden. Like a stake marking where to plant, it signals that a concept has been identified as worth developing but has not yet been written. Ghost links appear as plain, non-clickable text.

**[\[\[Grafted Node as Transplanted Knowledge in a Garden Patch\]\]](glosses/Grafted%20Node%20as%20Transplanted%20Knowledge%20in%20a%20Garden%20Patch.html)** — A grafted node is a knowledge node copied from a source garden into a garden patch. Like a horticultural graft, the node is taken from one context and attached to another where it can grow alongside new content. Grafted nodes diverge from their upstream originals as the patch adds connections and context.

**[\[\[Neobooks as Composable Knowledge Objects\]\]](glosses/Neobooks%20as%20Composable%20Knowledge%20Objects.html)** — Jerry Michalski's concept of neobooks — composable knowledge objects that can be assembled, disassembled, and reassembled by different people for different purposes. A successor to the book as knowledge transmission unit. Garden opuses and garden patches are partial implementations of this vision: opuses handle authored composition with renditions, patches handle portable knowledge fragments applied alongside external content.

**[\[\[Patch-Native Node as Original Knowledge in a Garden Patch\]\]](glosses/Patch-Native%20Node%20as%20Original%20Knowledge%20in%20a%20Garden%20Patch.html)** — A patch-native node is a knowledge node born in a garden patch rather than grafted from the source garden. Marked with ⊙, it indicates that this patch is the node's garden home — the place where the concept was first expressed as a garden form. Patch-native nodes may later be adopted upstream into the source garden.

**[\[\[Principal Authority as Agency Law for Digital Identity\]\]](glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html)** — Gloss interpreting principal authority as the application of centuries-old agency law to digital identity. Defines five key terms (principal, agent, conferral, authorship, responsibility), five agency duties, and revocability as the diagnostic test for voluntariness. Rooted in Wyoming SF0039's shift from property to agency law for digital identity.

**[\[\[Structural Contract as Form Type Agreement\]\]](glosses/Structural%20Contract%20as%20Form%20Type%20Agreement.html)** — A structural contract is the agreement that every instance of a form type follows the same internal structure — required sections, naming heuristics, predicate patterns, and the core question the form answers. The contract is what makes forms interoperable: a reader who knows the Model Form contract can navigate any model, and an agent can traverse any form without per-instance instruction.

**[\[\[Upstream Node as Source Garden Reference\]\]](glosses/Upstream%20Node%20as%20Source%20Garden%20Reference.html)** — An upstream node is a knowledge node that exists in the source garden but was not grafted into a garden patch. It is referenced by grafted nodes through predicate links marked with ↑, and its summary is documented on the Upstream References page. The source garden is 'upstream' — the origin from which knowledge flows into the patch.

**[\[\[Vault Precinct\]\]](glosses/Vault%20Precinct.html)** — The vault precinct is the zone within Deep Context Architecture for operational knowledge work — capturing meetings, managing contacts, daily journaling, research intake, and organizing clippings. Uses the same predicate infrastructure as the garden precinct but with lighter conventions suited to capture-first workflows.

### Patterns

**[\[\[Knowledge Compounds Through Typed Edges Not Filing\]\]](patterns/Knowledge%20Compounds%20Through%20Typed%20Edges%20Not%20Filing.html)** — Knowledge compounds when each new insight is wired into the existing graph through typed edges — not merely stored adjacent to prior notes. Researchers spend 75% of publication time on reading, compiling, and filing rather than writing because filing systems create false completeness. Typed edges (supports, contradicts, extends, extracted_from) make traversal meaningful, turning the writing phase into a query against existing structure.

**[\[\[Precinct Boundaries Govern Sharing Not Quality\]\]](patterns/Precinct%20Boundaries%20Govern%20Sharing%20Not%20Quality.html)** — Garden-precinct nodes are context-independent and designed for sharing — they extract the transferable insight from a conversation, strip the attribution, and stand alone. Vault-precinct documents (meeting notes, transcripts, person notes) are context-dependent and carry sensitivity — who said what, with what hedging, in what relationship. This distinction governs what gets added to a garden patch (shared openly) versus what gets zipped as a compound meeting document (shared under Chatham House). The precinct boundary is a sharing boundary, not a quality boundary.

**[\[\[Technology Paternalism Masks Coercion\]\]](patterns/Technology%20Paternalism%20Masks%20Coercion.html)** — Anti-pattern where digital systems shape, restrict, or pre-decide user choices under justifications of safety, efficiency, or protection. Four forms — Design (dark patterns), Algorithmic (filter bubbles), Infrastructural (lock-in), Protective (safety framing) — each embed coercion at a different system layer while appearing benevolent.

**[\[\[Three-Part Enforcement Stack\]\]](patterns/Three-Part%20Enforcement%20Stack.html)** — Pattern identifying three interdependent layers required for accountable authority in digital identity systems: legal duties (agency law), technical delegation (cryptographic enforcement), and anti-lock-in design (real alternatives and proportionate exit costs). Removing any single layer collapses accountability — legal without enforcement is nominal, technical without legal is unaccountable, both without exit is lock-in.

### Principles

**[\[\[Authority Flows from the Person\]\]](principles/Authority%20Flows%20from%20the%20Person.html)** — Principle establishing that identity and authority originate with the person, not institutions or platforms. Identity is delegable but not alienable — it can be conferred to agents but never transferred as property. Grounded in Wyoming SF0039's statutory shift from property law to agency law for digital identity.

**[\[\[Content Over Container\]\]](principles/Content%20Over%20Container.html)** — Principle that a knowledge vault needs searchable content, not file formats. When information can be extracted into a searchable rendition, the original binary's value drops to provenance evidence. Store binaries locally only when no canonical source exists AND the binary provides value beyond its rendition.

**[\[\[Human Authority Over Augmentation Systems\]\]](principles/Human%20Authority%20Over%20Augmentation%20Systems.html)** — Principle committing the vault's design to augmentation over autonomy, expressed through principal authority. The vault owner retains legibility (can see what the agent does), boundary-setting (defines what the agent may do), and override capability (can intervene at any point). Extends Content Over Container by treating the human's reasoning as the content that must not be subordinated to its container.

**[\[\[Living Documents Over Static Publications\]\]](principles/Living%20Documents%20Over%20Static%20Publications.html)** — Garden nodes are living documents that grow, split, merge, and evolve through tending. The current state matters, not a published version. Mutability varies: most nodes evolve freely, cases are immutable records with living interpretation, convictions change rarely. Provenance links to archived sources should upgrade to living targets.

**[\[\[Progressive Disclosure Over Eager Loading\]\]](principles/Progressive%20Disclosure%20Over%20Eager%20Loading.html)** — Operating principle for the deep context graph: start with the question, load the most relevant nodes, follow edges on demand, stop when context is sufficient. Nothing requires loading the full graph. Mirrors the quad model in Claude Code (rules always, references on demand) and extends it across all form types.

**[\[\[Systems Should Listen More Than They Speak\]\]](principles/Systems%20Should%20Listen%20More%20Than%20They%20Speak.html)** — Herbert Simon's design principle applied to information systems: subsystems should absorb more information than they produce. The input/output ratio of a component is measurable. Effective designs compress and filter at each stage; naive designs amplify volume. Protocol success is measured by attention saved, not information delivered.

**[\[\[Zero-Tooling Floor for Knowledge Architecture\]\]](principles/Zero-Tooling%20Floor%20for%20Knowledge%20Architecture.html)** — The deep context architecture preserves a zero-tooling floor: plain markdown, YAML frontmatter, predicate wikilinks, and git. No database, plugin, or schema enforcement required at the authoring or semantic layers. Shell one-liners serve as the query layer. Specialized tools add value but are never prerequisites.

### Convictions

**[\[\[Authentic Collaboration Requires Agency\]\]](convictions/Authentic%20Collaboration%20Requires%20Agency.html)** — The conviction that authentic collaboration — shared intentional creation where participants entrust part of their identity to a joint endeavor — is impossible without agency. Cooperation can be coerced; collaboration cannot. Combined with a second conviction: the world's truly important problems require collaboration to solve. Together these form the argument that agency infrastructure is prerequisite to addressing intractable global challenges.

**[\[\[Filtering Is More Valuable Than Connecting\]\]](convictions/Filtering%20Is%20More%20Valuable%20Than%20Connecting.html)** — The core conviction behind Inter-Face Protocol: the scarce resource is human attention, not human connection. The value of an agent system is measured by what it filters out — the overlaps it does not surface — rather than the connections it enables. Most gossip exchanges should produce silence.

**[\[\[Values Precede Technical Decisions\]\]](convictions/Values%20Precede%20Technical%20Decisions.html)** — The conviction that technical architecture must be grounded in human values — not derived from technical capability, market pressure, or implementation convenience. Every design choice in the deep context architecture traces to a value: augmentation over autonomy, portability over power, simplicity over sophistication, human reasoning over system output. When values and technical convenience conflict, values win.

### Decisions

**[\[\[Deep Context as an Architecture for Captured Reasoning\]\]](decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html)** — The decision to capture personal reasoning as typed markdown forms connected by predicates — not as fine-tuned models, retrieval-augmented documents, or tagged notes. Typed forms with structural contracts make reasoning traversable by agents; predicates make it navigable; progressive disclosure makes it fit in context windows.

### Boundaries

**[\[\[Delegated Decision Authority Spectrum\]\]](boundaries/Delegated%20Decision%20Authority%20Spectrum.html)** — Boundary form defining four zones of decision authority — autonomous, propose-and-approve, human-only, and group-deliberative — applicable to any agent (LLM, delegate, automated system) operating within a deep context garden.

### Inquiries

**[\[\[Cooperation vs Collaboration as Distinct Concepts\]\]](inquiries/Cooperation%20vs%20Collaboration%20as%20Distinct%20Concepts.html)** — Cooperation and collaboration share a Latin prefix (com- = together) but diverge at the root: operari (to produce, from opus = work product) vs laborare (to toil, from labor = exertion). This etymological split persists across modern usage — cooperation implies independent agents aligning toward compatible goals, collaboration implies shared struggle producing something none could alone. The distinction is formal in education, game theory, and biology; informal but consistent in law, diplomacy, and the arts.

**[\[\[Domains and Pattern Languages as Organizational Concepts\]\]](inquiries/Domains%20and%20Pattern%20Languages%20as%20Organizational%20Concepts.html)** — Investigates the relationship between domains (knowledge area indexes across all form types) and pattern languages (collections of patterns organized by scale within a domain). Meeples Together, Group Works, and Rust coding patterns are all pattern languages in different domains — are pattern languages a specialized view of a domain, or a distinct organizational concept?

**[\[\[Gossip Duality Between Human Silence and Agent Noise\]\]](inquiries/Gossip%20Duality%20Between%20Human%20Silence%20and%20Agent%20Noise.html)** — The gossip-as-filter concept produces two opposing outputs: silence for humans (high-value filtering) and noise for agents (high-volume exchange). These serve different stakeholders with different success metrics. Human silence measures filter quality — fewer recommendations that are worth acting on. Agent noise measures coverage — more exchanges that detect more potential overlaps. The duality raises design questions about where to draw boundaries between the two modes.

**[\[\[Group Deliberation Mechanism\]\]](inquiries/Group%20Deliberation%20Mechanism.html)** — Inquiry into how the deep context architecture handles decisions requiring group input — what practical mechanism does an agent use when it reaches a group-deliberative boundary? Explores structured proposals, agenda generation, and the gap between Polis Play philosophy and operational implementation.

**[\[\[Living Document Scale Limits\]\]](inquiries/Living%20Document%20Scale%20Limits.html)** — Open question: is there a scale threshold beyond which the maintenance cost of living documents exceeds their accumulated value? Jerry Michalski's TheBrain (620,000+ nodes, 28 years) is evidence that single-author knowledge graphs can scale, but at what cost to gardening labor and structural coherence?

**[\[\[Trust Layer Activation Criteria\]\]](inquiries/Trust%20Layer%20Activation%20Criteria.html)** — Inquiry into when a garden needs the trust layer — Gordian Envelope's signing, elision, and verified exchange capabilities. The architecture defines the trust layer as a future phase but leaves activation criteria undefined. Explores what triggers the transition from markdown-only to cryptographically-verified exchange.

### Values

**[\[\[Knowledge Durability\]\]](values/Knowledge%20Durability.html)** — The value that knowledge should survive changes in tools, platforms, and formats. A garden's reasoning substrate must outlast the software used to tend it — plain markdown over proprietary formats, git over cloud sync, zero-tooling floors over feature-rich dependencies.

**[\[\[Reasoning Fidelity\]\]](values/Reasoning%20Fidelity.html)** — The value that a knowledge system should capture how its owner actually reasons — the web of values, principles, patterns, and cases that inform decisions — not merely store facts and documents. Fidelity means an agent working from the garden can make decisions consistent with how the owner actually thinks.

### Protocols

**[\[\[Inter-Face Protocol\]\]](protocols/Inter-Face%20Protocol.html)** — Peer-to-peer protocol for AI agents to communicate on behalf of their human operators. Agents talk pairwise to surface moments warranting human conversation. Decentralized with progressive trust through disclosure tiers. Twelve draft specifications cover message format, identity, transport, and capabilities.

### Citations

**[\[\[Allen (2023) Minimum Viable Architecture\]\]](citations/Allen%20%282023%29%20Minimum%20Viable%20Architecture/Allen%20%282023%29%20Minimum%20Viable%20Architecture.html)** — Christopher Allen's minimum viable architecture principle: make a few hard-to-reverse decisions early, defer everything else. Commit to the decisions that would be expensive to change later — the 80/20 choices that shape everything downstream — and leave tactical decisions for when you have more information.

**[\[\[Allen (2024) Progressive Trust\]\]](citations/Allen%20%282024%29%20Progressive%20Trust/Allen%20%282024%29%20Progressive%20Trust.html)** — Christopher Allen's progressive trust framework: trust deepens through stages from initial contact to full collaboration, with each stage requiring verification before advancing. Not binary (trusted/untrusted) but a progression where disclosure, authentication, and commitment deepen together. Provides the conceptual foundation for IFP's progressive authentication and disclosure tier models.

**[\[\[Brand (2018) Pace Layering\]\]](citations/Brand%20%282018%29%20Pace%20Layering/Brand%20%282018%29%20Pace%20Layering.html)** — Brand's pace layering framework describes how complex systems maintain resilience through layers operating at different rates of change. Six civilization layers from fashion to nature interact through slippage — fast layers innovate and absorb shocks, slow layers stabilize and remember. Health comes from the apparent contradictions between layers.

**[\[\[Clark (1991) Grounding in Communication\]\]](citations/Clark%20%281991%29%20Grounding%20in%20Communication/Clark%20%281991%29%20Grounding%20in%20Communication.html)** — Clark and Brennan define grounding as the collaborative process of establishing mutual understanding through continuous evidence exchange. Contributions have two phases — presentation and acceptance. Eight medium-specific constraints (copresence, visibility, audibility, contemporality, simultaneity, sequentiality, reviewability, revisability) determine available grounding strategies.

**[\[\[Ehmke (2023) Dimensions of Digital Coercion\]\]](citations/Ehmke%20%282023%29%20Dimensions%20of%20Digital%20Coercion/Ehmke%20%282023%29%20Dimensions%20of%20Digital%20Coercion.html)** — Four-dimensional framework for digital coercion: attention (excessive cognitive demands), ergonomic (autonomy/usability tradeoffs), trust (unaccountable benign intent assumptions), and cultural (Western norm imposition). Applies the same analytical lens to both commercial and open-source platforms, challenging the assumption that openness alone produces equity.

**[\[\[Kolpondinos (2026) Technology Paternalism\]\]](citations/Kolpondinos%20%282026%29%20Technology%20Paternalism/Kolpondinos%20%282026%29%20Technology%20Paternalism.html)** — Names Technology Paternalism as an anti-pattern with four forms: Design (dark patterns, defaults), Algorithmic (filter bubbles), Infrastructural (lock-in), and Protective (safety-justified restrictions). Extends to agentic AI and digital identity. Proposes four countermeasures: override, contest, inspect, and exit.

**[\[\[Nissenbaum (2004) Privacy as Contextual Integrity\]\]](citations/Nissenbaum%20%282004%29%20Privacy%20as%20Contextual%20Integrity/Nissenbaum%20%282004%29%20Privacy%20as%20Contextual%20Integrity.html)** — Nissenbaum reframes privacy as contextual integrity — appropriate information flows governed by context-specific norms rather than secrecy or individual control. Five parameters define any flow: data subject, sender, recipient, information type, and transmission principle. Privacy violations occur when flows breach the norms governing a particular social context, not when information becomes visible.

**[\[\[Schegloff (1977) Preference for Self-Correction in Repair\]\]](citations/Schegloff%20%281977%29%20Preference%20for%20Self-Correction%20in%20Repair/Schegloff%20%281977%29%20Preference%20for%20Self-Correction%20in%20Repair.html)** — Schegloff, Jefferson, and Sacks map the systematic organization of conversational repair, showing that self-initiated self-correction is structurally preferred over other-correction. The paper classifies repair by who initiates and who completes, revealing a positional hierarchy that gives trouble-source speakers maximum opportunity to fix their own errors.

**[\[\[Simon (1971) Designing Organizations for an Information-Rich World\]\]](citations/Simon%20%281971%29%20Designing%20Organizations%20for%20an%20Information-Rich%20World/Simon%20%281971%29%20Designing%20Organizations%20for%20an%20Information-Rich%20World.html)** — Simon's 1971 essay argues that information abundance creates attention scarcity. Well-designed information systems should allocate attention efficiently by filtering and compressing — 'listening and thinking more than they speak' — rather than amplifying volume at each stage.


---

## Upstream Nodes↑

These nodes exist in the source garden but were not grafted into this patch. When you see **↑** after a wikilink, it points to the entry below.

### Deep Context Architecture

### Model Form

**Captured Reasoning Exchange Pipeline**: Three-layer model for how captured reasoning moves from human authoring (markdown) through agent traversal (semantic graph) to trusted exchange (Gordian Envelope) — each layer serving a different audience while representing the same knowledge.

**Compound Node Anatomy**: Defines the compound node — a folder-based knowledge object with a lead file, sibling files, renditions, and archives. Generalizes the garden's compound document pattern to vault-wide application.

**Cross-Domain Document Lifecycle Parallels**: Three domains — wiki communities, digital gardens, and AI agent context systems — face the same document lifecycle problems (splitting, staleness, ownership, deletion) under different constraints. Maps the parallels and identifies where the analogy breaks down: statelessness, read frequency, token economics, and automated maintenance.

**Document Lifecycle Governance Heuristics**: Maps wiki governance heuristics for document lifecycle (split, merge, redirect, delete, draftify) to garden and agent context operations. Includes failure modes: the append-only trap (growth by accretion without consolidation) and structure ossification (resistance to reorganization over time).

**Guardrail Hierarchy for Graph Maintenance**: Four enforcement tiers for knowledge graph maintenance, ordered by strength: hard limits (absolute boundaries), safety nets (pre-commit validation), golden paths (preferred defaults via templates and conventions), and audit trails (post-hoc diagnosis). The ordering is load-bearing — higher tiers override lower ones when constraints conflict. The garden's current gap is in safety nets: automated structural checks between golden paths and hard limits.

**Personal Knowledge Management Organizing Principle Spectrum**: Model mapping Personal knowledge management systems on an actionability-meaning spectrum — PARA at the actionability end, Zettelkasten at the meaning end, ACE and GRID as hybrids. Includes a second axis (folder vs. link) and our vault's three-axis resolution (function, meaning, form). Comparison matrix across 8 systems and 9 dimensions.

**Quad Model Mapping to Forms**: Maps the Claude Code quad (rule/process/requirements/reference) onto deep context form types as facets, not forms. Any capability may have all four facets. Rules map to Principle or Boundary, Process to Protocol or Skill, Requirements to Pattern consequences or Case outcomes, Reference to Gloss, Reference, or Citation.

**Status Lifecycle Tracks**: Three status tracks for three kinds of knowledge work. Maturity (Seed→Growing→Evergreen→Pruned) for living documents, curation (uncurated→curated→annotated) for static captures, processing (Captured→Transcribed→Cleaned→Summarized→Published) for meetings. The has_status:: predicate is universal; the vocabulary varies by node type.

**Swanson Linking — Undiscovered Public Knowledge**: Don Swanson demonstrated in 1986 that valuable knowledge exists implicitly across disconnected research literatures. His ABC model: if Literature A establishes A-B and Literature C establishes B-C, but the two share nothing, then A-C is a hypothesis no one has formulated. Applied to the garden, cross-domain typed edges enable the same discovery pattern across domain boundaries.

**Sycophantic Confidence Spiral**: Model describing how AI sycophancy creates circular evidence that inflates user confidence without approaching truth. The mechanism: AI generates data conditioned on user hypotheses, user treats this as independent evidence, beliefs concentrate on initial hypothesis. Default LLM behavior is indistinguishable from explicit sycophancy. Discovery drops from 29.5% to 5.9% when sampling is biased.

**Vocabulary Lifecycle Through Tending**: Model unifying the degradation mechanism common to growing vocabularies, configuration systems, and knowledge graphs. Any accumulating terminology — predicates, tags, rules, skills — degrades retrieval effectiveness without continuous tending. Three gardening activities maintain health: weeding (removing malformed entries), seeding (introducing needed specificity), and fertilizing (enriching with semantic structure).

### Pattern Form

**Context Conservation Hierarchy**: Pattern for accessing compound node content in four tiers of increasing token cost — path listing, lead file YAML, lead file body, siblings — so agents triage relevance cheaply before committing context window capacity.

**Cross-Project Learning Repatriation**: When garden work starts in one workstream but moves to an external project (or vice versa), learnings must be deliberately imported back. Learnings belong where they are consumed, not where they are produced. Without deliberate absorption, decisions made externally leave gaps in the garden's decision record.

**Domain Extensions on Common Frontmatter Base**: Different content types (clippings, meetings, authored docs) extend a common frontmatter base (created, summary, reviewed) with domain-specific fields rather than sharing a monolithic schema. Content-type is the primary routing axis — it determines which additional fields are relevant. Each source's fields stay out of the others' schemas.

**Ghost Links as Garden Planning Tools**: Ghost links — wikilinks pointing to notes that don't exist yet — function as planning tools when treated as intentional graph members rather than lint errors. WikiBonsai's Caudex tracks these as 'zombie nodes' with full graph participation. Reframing ghost link reports from error lists to planning indexes reveals which unwritten nodes carry the most incoming predicates and deserve attention first.

**Git Tags for Sent-Version Tracking**: Track what recipients received of shared documents using signed git tags (sent/<recipient>-<doc-slug>-<date>). The tag name goes in sent_to frontmatter, enabling git diff sent/tag-name to show what changed since the document was sent. Solves the 'what version did they see?' problem for living documents shared externally.

**Graph Structure Validation for Garden Nodes**: Pattern for graph-level lint checks complementing form-level validation: every garden node carries at least one typed predicate, every domain page receives incoming in_domain:: edges, and no orphan nodes exist without domain membership. Shell scripts over rg and jq — a recipe, not a dependency.

**Informal Edges Poison the Graph**: Informal edges poison the graph through precedent poisoning: an agent invents a redundant relationship type, future traversals find it and treat it as precedent for further invention, and semantic noise compounds until retrieval becomes unreliable. Prevention requires ongoing vocabulary curation — awareness, review, consolidation, and clarification — not just enforcement at creation time.

**Knowledge on Three Axes**: Pattern resolving the tension between sorting (findability, stability) and connecting (serendipity, expressiveness) by organizing knowledge on three orthogonal axes: folders for function, links for meaning, forms for epistemic type. No single axis resolves all organizational forces.

**Lead File to Sidecar Discovery**: Pattern proposing a typed edge from lead files to sidecars (has_sidecar:: or has_companion::) to enable bidirectional traversal within compound nodes — agents can discover binary metadata from the lead file without folder scanning.

**Lightweight Governance for Personal Gardens**: For a personal garden with one active user, a rule file (loaded every session) plus a reference file (with ADRs) provides sufficient governance without the full quad pattern. Expansion follows actual use — new form-type tags are added as forms of those types are written, not preemptively planned.

**One Context One Concern**: Pattern for separating research and implementation into distinct context windows. Mixing exploration and execution in a single context causes task interference, attention dilution, and compounding assumptions. Solution: complete research in one context, distill findings into a compressed handoff, execute in a fresh context. Validated by Anthropic's sub-agent architecture and empirical context rot research.

**Predicate Maintenance Recipes Over Tools**: Predicate maintenance uses shell one-liners rather than dedicated tools, preserving the architecture's zero-tooling floor. Inverse-link queries, predicate renames, and ghost link discovery are all achievable with rg and sed. Documenting recipes keeps the graph maintainable without adding dependencies.

**Probe Before Commit**: Before building on an assumption about external state — API shape, file location, metadata schema, permission model, or the garden's own backlog — probe the actual state first. Seven instances across system access, web research, API integration, metadata design, and process adherence validated this cross-cutting pattern during garden development.

**Progressive Summary Before Substance**: Pattern for navigating large knowledge graphs within small context windows — check summary fields first to assess relevance, then load full nodes on demand, following edges only as needed. Validated by the first garden: summary-based matching produced 151 accurate matches versus 287 false positives from keyword search.

**Source Adapter for Heterogeneous Imports**: Each content source (X API, email threading, web scraping) gets its own extraction adapter, then a common vault normalization step maps the result to garden conventions. Source-specific complexity stays in the adapter; the garden receives consistent notes. Three adapter responsibilities: field mapping, artifact cleanup, and content-type classification.

**Structured Disagreement Through Persona Review**: Single-perspective AI outputs hide blind spots that multiple persona reviewers expose. Three independent implementations validate the pattern: polarity-paired historical thinkers with deliberation protocols, culturally diverse reflection personas for perspective-taking, and professional role personas with domain expertise. The mechanism is not 'more opinions' but structured opposition — each reviewer has declared strengths and blind spots, and the protocol forces engagement with disagreement before allowing consensus.

**Still Knowledge, Moving Action**: Pattern resolving the restlessness problem in actionability-based personal knowledge management systems — separate the dynamic action layer (workstreams, projects) from the stable knowledge layer (notes, research, garden nodes). Knowledge stays put; action reorganizes freely.

**Summary Fields as Load-Bearing Infrastructure**: Summary fields (~280 characters) are not optional metadata but load-bearing infrastructure for agent traversal. During vault enrichment, summary-based matching produced 151 accurate matches versus 287 false positives from keyword search. Poor summaries produce retrieval failures.

**Temporary Predicate Scaffolding**: Predicates can serve as temporary scaffolding — built for a specific purpose (ghost link analysis, map of content prioritization), then removed after serving that purpose. During tag normalization, 913 relates_to:: predicates were created to build ghost links for map of content prioritization, then removed to prevent graph pollution. Build it, use it, clean it up.

**Vault Content Graduation**: Content moves from vault precinct types to garden precinct nodes through tending — recognizing when operational captures are ready to become curated knowledge. Clippings graduate to citations, meetings produce decisions, research notes become references. Lateral movement between precincts, not promotion up a hierarchy.

### Principle Form

**Standalone Document Test for Form Candidacy**: The test for whether a knowledge type warrants its own form type: does it produce a standalone document with a known internal structure? A form is a knowledge object with a structural contract — required sections that make its shape predictable. Types that only appear embedded in other forms are structural elements, not forms.

### Inquiry Form

**Automated Gardening Trust Problem**: Open question: can agents reliably garden their own context files — detecting staleness, refactoring bloated sections, removing contradictions? Wiki bot policies are the closest precedent. The recursive trust problem: the agent assessing the quality of its own instructions may be biased by those instructions.

**Compound Node Meeting Structure**: Inquiry into how meeting compound nodes should be structured — whether cleaned transcripts or meeting summaries serve as lead files, what goes in renditions vs. siblings, and how the meeting-capture skill should adapt for compound output.

**Cross-Domain Form Indexing**: How should domain pages handle forms that belong to multiple domains? Authority Conferral Chain bridges Deep Context Architecture and Self-Sovereign Identity. Authentic Collaboration Requires Agency spans Synpraxis and Self-Sovereign Identity. Current approach: list the form in each domain page with in_domain:: predicates on the form. But this creates maintenance burden and raises questions about primary vs secondary domain membership.

**Form Type Distinctiveness in Naming and Structure**: Investigates whether the 16 form types are distinguishable in practice — can a reader recognize an instance's form type from its title and structure alone? 15 of 16 types now have instances with documented naming heuristics. Among instantiated types, naming overlaps persist (pattern vs principle both use 'X Over Y'), and structural contracts blur at boundaries (gloss vs model).

**Garden Publishing Path**: Inquiry into how the deep context garden should be published for external consumption. Five approaches evaluated (Quartz, Jekyll+WikiBonsai, Eleventy, custom Python script, raw HTML) against typed relation rendering, Obsidian syntax support, and zero-tooling philosophy. Custom script recommended for maximum control; approaches are composable.

**Graph-Native Skill Execution**: Inquiry into how garden skills can discover, load, and reason from typed graph nodes during execution — moving from hardcoded file paths to predicate-based traversal. Explores the infrastructure gap between current self-contained skills and graph-native skills that compose with garden knowledge.

**IPARAG Term Origins**: Inquiry into the source and exact meaning of 'IPARAG' — a personal knowledge management method recalled from the Zettelkasten community. Extensive search found no canonical source as of March 2026. Four hypotheses proposed; most likely reading is Inbox-Projects-Areas-Resources-Archives-Goals (the two most common PARA extensions combined).

**Inquiry Lifecycle and Resolution**: When is an inquiry 'done'? Inquiries generate other nodes — cases from tested hypotheses, patterns from validated parallels, references from syntheses. The inquiry may persist as an open thread with resolved and unresolved branches, or archive when its questions are addressed elsewhere. No lifecycle model exists yet.

**Living Document Scale Limits**: Open question: is there a scale threshold beyond which the maintenance cost of living documents exceeds their accumulated value? Jerry Michalski's TheBrain (620,000+ nodes, 28 years) is evidence that single-author knowledge graphs can scale, but at what cost to gardening labor and structural coherence?

**Personal Knowledge Management Method Adoption for Vault Architecture**: Inquiry into what our vault should adopt, modify, or reject from personal knowledge management methods (PARA, ACE, GRID, Zettelkasten, Digital Garden). Five open questions spanning inbox workflows, Categories/ map of content evolution, Goals integration, GRID's validation of note typing, and a minimum viable explanation for onboarding.

**Predicate Vocabulary Stabilization**: The predicate grammar started freeform by design — new predicates welcome when existing ones don't fit. The architecture suggested review after 50+ relations and controlled vocabulary after 200+. The garden is well past both thresholds. When does freeform become inconsistency? What stabilization looks like without rigidity.

**Productivity Separation from Knowledge Vault**: The vault mixes garden content (typed knowledge nodes) with productivity content (daily notes, meetings, goals, inbox). Neither depends on the other. Should productivity move to a separate tool or vault? The connection is through wikilinks, which could cross boundaries if separated.

**Scenario Lifecycle and Aging**: Inquiry into how scenario nodes age — when a scenario is validated by events it becomes a case, but invalidated scenarios may still hold value through their force analysis. Explores lifecycle transitions, retention criteria, and whether wrong-but-useful scenarios should persist or archive.

**Universal Document Lifecycle State Machine**: Open question: is there a single document lifecycle state machine that generalizes across wiki pages, garden nodes, and agent context files? The deep context architecture has three status tracks for three kinds of work — but wiki, garden, and agent domains face the same lifecycle problems under different names.

**Vault-Wide Compound Node Adoption**: Inquiry into which vault document types beyond garden nodes benefit from compound node structure — citations, cases, research notes, meetings, clippings — and what criteria trigger graduation from atomic to compound. Addresses whether compound nodes should be vault-wide or garden-only.

### Gloss Form

**ACE as Three Dimensional Personal Knowledge Management**: Interprets Nick Milo's ACE (Atlas, Calendar, Efforts) as a three-dimensional personal knowledge management framework grounded in STIR (Space, Time, Importance, Relatedness). Closer to our vault's philosophy than PARA — acknowledges the linking layer and uses maps of content — but still lacks epistemic note typing.

**Deep Context as Shared Language**: The term 'deep context' originates from Allen's 2014 writing on shared languages. When practitioners share deep context, a single phrase invokes an entire framework — saying 'Cynefin' communicates the complicated/complex distinction and how to work with each. The architecture makes this implicit understanding explicit and navigable through typed nodes and traversable edges.

**Digital Garden as Growth Ethos**: Interprets the digital garden movement (Caufield's stream-vs-garden distinction, Appleton's six patterns) as a growth ethos — organic, imperfect, associative knowledge development. Our deep context garden adopts the philosophy but adds formal structure: typed nodes, typed predicates, and structural contracts that most digital gardens lack.

**GRID as Note Type Organization**: Interprets GRID (Glossary, Reference, Index, Diary) as the mainstream personal knowledge management method closest to our garden nodes — it organizes by note type rather than actionability or topic. GRID's four types map roughly to Gloss, Reference/Citation, Domain, and Case in our 15-form taxonomy.

**Garden Precinct**: The garden precinct is the zone within Deep Context Architecture where knowledge is curated into typed nodes with structural contracts, tended through growth stages (Seed to Evergreen), and interconnected by typed predicates. It solves the problem of making knowledge retrievable, composable, and trustworthy over time.

**IPARAG as Extended PARA**: Interprets IPARAG as a six-category extension of PARA adding Inbox (capture staging) and Goals (strategic alignment). No canonical source text found as of March 2026 — likely a community coinage combining PARA's two most common extensions into one acronym.

**Johnny Decimal as Permanent Addressing**: Interprets Johnny Decimal as a permanence-first organizational system — every file gets a stable numerical address (e.g., 32.14) that never changes. Solves the problem our vault handles differently: we use git for permanence and wikilinks for stable references instead of numerical addressing.

**Lead File Selection Guidance**: Defines the lead file — the primary access point of a compound node, borrowing from journalism's 'lead' concept. Provides selection criteria by content type: citation cards lead citations, transcripts lead meetings, research notes lead investigations.

**Note Titles as APIs**: Glosses Andy Matuschak's claim that note titles function as APIs — stable abstractions usable as reference handles. The garden extends this by observing that different form types answer structurally different questions, so the shape of a good title API varies by form. Three naming traditions (wiki, pattern language, evergreen notes) converge on this insight.

**Research as Workflow Not Precinct**: Research is a workflow that moves information from vault precinct (capture, citation) through analysis into garden precinct (typed nodes with structural contracts), not a third knowledge zone requiring its own precinct. A Research Precinct would fragment the graph by separating methodology claims from domain claims despite shared evidence infrastructure.

**PARA as Actionability-First Design**: Interprets PARA (Projects, Areas, Resources, Archives) as an actionability-first organizational method — four categories sorting information by urgency rather than topic. Maps PARA to our vault, identifies the gap: no connection fabric, no epistemic differentiation, and constant reorganization undermines long-term knowledge stability.

### Citation Form

**Altshuler (2026) Nanograph On-Device GraphDB**: Citation of nanograph, an on-device schema-enforced graph database for agentic workflows built on Rust, Arrow, Lance, and DataFusion. Validates Deep Context Architecture design principles from an independent source: typed predicates prevent semantic drift (naming the failure mode 'precedent poisoning'), local-first storage preserves human authority, and decision traces create compounding reasoning value.

**Batista (2026) Rational Analysis of Sycophantic AI**: Bayesian proof that sycophantic AI creates circular evidence inflating confidence without approaching truth. Wason 2-4-6 experiment (N=557) found default GPT suppresses discovery equivalently to explicit sycophancy (5.9% vs 29.5% for unbiased sampling). Formalizes delusional spiraling: rational agents become increasingly wrong when AI samples data conditioned on user hypotheses.

**Chatlatanagulchai (2025) Agent READMEs**: Empirical study of 2,303 agent context files across 1,925 repositories. Finds that CLAUDE.md, AGENTS.md, and similar files behave more like dynamic configurations than static documentation — maintained through frequent incremental additions, with 59-67% undergoing multiple commits. Identifies 16 instruction categories and a gap in security/performance coverage.

**George (2026) Harness Engineering Is Cybernetics**: Citation of George's X article tracing agent harness engineering through three cybernetic instantiations: Watt's governor, Kubernetes controllers, and LLM harnesses. Each closes a feedback loop at a progressively higher layer. The core insight — making human judgment machine-readable is the real engineering work — provides the theoretical framework for why DCA uses typed predicates and structural contracts.

**Peters (2008) Tag Gardening for Folksonomy Enrichment**: Formalizes tag gardening as three activities — weeding (removing bad tags), seeding (introducing specific tags), and fertilizing (enriching with external knowledge organization systems). Proposes power tags from distribution curves as candidates for semantic enrichment. Introduces TagCare for cross-platform personal tag maintenance. The gardening metaphor is deliberate: vocabularies are living systems requiring continuous tending.

**Rajasekaran (2025) Effective Context Engineering for AI Agents**: Anthropic's applied AI team defines context engineering as curating the smallest high-signal token set at each inference step. Introduces four strategies — Write, Select, Compress, Isolate — with empirical data showing ~90% improvement from sub-agent isolation on research tasks. Grounds context management in transformer attention budget constraints.

**Roy (2026) Words Without Consequence, from The Atlantic**: Deb Roy argues that AI has decoupled speech from consequence for the first time. An LLM's apologies are empty because no accountable speaker stands behind them. Routine fluent speech without responsibility degrades the conditions under which promises and advice carry meaning — a shift in the moral structure of language.

**arscontexta (2026) Skill Graphs**: Proposes skill graphs — networks of small SKILL.md files connected by wikilinks — as an alternative to monolithic skill files. Each node holds one complete thought; wikilinks carry semantic meaning in prose so agents follow relevant paths. Progressive disclosure applies recursively inside the graph: index, descriptions, links, sections, full content.

**systematicls (2026) World-Class Agentic Engineering**: A practitioner guide arguing the best agentic engineers are communicators, not coders. Covers context management as the primary constraint, sycophancy-aware prompting patterns, rule and skill lifecycle for agent configuration, and task contracts as completion criteria. Central insight: strip dependencies, separate research from implementation, and iterate on rules and skills.

### Case Form

**Architecture Document Extraction to Garden Forms**: Case documenting the systematic extraction of a 450-line architecture document into 80+ standalone garden nodes across 15+ form types over 12 sessions. The monolithic source defined the entire deep context framework — form types, principles, patterns, models, decisions — and had to be decomposed into a living typed graph.

**Hybrid Bootstrapping for Garden Migration**: Case documenting the first deep context garden bootstrap — a Python script converted topic tags from 913 archive files into 4,294 relates_to predicates, transforming a flat bag of files into a connected graph. Scripted extraction handled structure; hand-authoring handled interpretation. The hybrid approach proved viable at scale.

### Reference Form

**Deep Context Garden Conventions**: Practical conventions for the first deep context garden in this Obsidian vault. Hard line between tags (flat classification, no graph edges) and links (graph edges). Two-namespace tag system: type/ for document category, status/ for maturity. Topic tags explicitly rejected — wikilinks produce graph edges instead.

**Deep Context Implementation Roadmap**: Iteration-by-iteration plan for building a Deep Context garden inside an Obsidian vault. Defines four phases — Foundation, Seed Graph, Content Migration, Publishing — each independently valuable. Uses predicate::[\[\[target\]\]↑](EXTERNAL.html#:~:text=target) typed relations and targets an hour-a-day tending rhythm with agent assistance between sessions.

**Structural Elements Within Forms**: Reference for knowledge types that don't warrant their own form type — ADR, Narrative, Warrant, Signal, Commitment, Lexicon entry, Tension/Paradox. Each has a home inside existing forms. Answers 'where does X go?' for the seven types that failed the standalone document test.

**Typed Relations as Simple Graphs in Plain Markdown**: predicate::[\[\[Target\]\]↑](EXTERNAL.html#:~:text=Target) typed relations turn markdown files into a directed labeled graph with no database or schema. Plain wikilinks answer \

### Research Form

**Deep Context Content Decision Records**: 26 architectural decisions governing content structure for the deep context garden: predicate-based classification over tags, snake_case predicates, five-category form grouping, taxonomy-expansion-follows-use, compound document graduation, and lightweight governance. Merges the previous C- and N- ADR series into a single themed sequence.

**Research Graphs and Precinct Architecture**: Investigates Cornelius's Research Graphs system against the garden's precinct architecture. Maps his 5 note types to existing garden forms and identifies two infrastructure gaps: confidence metadata and provenance chain propagation. Surfaces Swanson's Literature-Based Discovery as a missing model. First instance of Research Form.

### Scenario Form

**Knowledge Graph as Digital Twin of Principal Reasoning**: Explores what happens when deep context gardens reach sufficient density and connection that agents can reliably act on behalf of the garden owner in routine decisions and external communications, shifting the principal-agent dynamic from augmentation toward delegation.

### Form Type

**Boundary Form**: Defines the Boundary form type: a declaration of what an agent may and may not decide. Not what the right choice is, not how to make it, but who holds authority. Amendable through deliberative process, never unilaterally. 1 instance in [Garden/boundaries/](boundaries/index.html).

**Case Form**: Defines the Case form type: a specific narrative with outcome recording what was attempted, what resulted, and what was learned. Immutable — history doesn't change, though interpretation may.

**Citation Form**: Defines the Citation form type: a structured dossier on a single work containing bibliographic entry, summary, key points, key quotes, influence, sources, and relations. Named as Author (Year) Abbreviated Title. Atomic at Seed stage, graduating to compound (analysis.md, insights.md, Renditions/, Archives/) as analysis deepens. Append-only.

**Model Form**: Defines the Model form type: a structural representation showing elements, relationships, boundaries, and feedback loops. How things relate to each other. Evolving as understanding grows. Models are explanatory (how things work), distinct from patterns (what to do) and scenarios (what might happen).

**Protocol Form**: Defines the Protocol form type: a specification for multi-party coordination across trust boundaries. Distinguished from a process by who must agree — a protocol works only if all parties follow it. Scope includes human coordination methods alongside technical protocols.

**Pruned Stage**: Defines the Pruned Stage: a garden node no longer current but preserved rather than deleted. Pruning replaces deletion so that link chains and reasoning history remain traceable. Uses superseded_by:: predicates to point to replacements. Lowest retrieval priority among all growth stages.

**Reference Form**: Defines the Reference form type: a comprehensive briefing synthesizing multiple sources and forms into a coherent domain picture. May contain model-like tables, principle-like recommendations, and gloss-like interpretations. Source docs in Research/ carry this type.

**Research Form**: Defines the Research form type: a living investigation that grows through active research, contains form-typed sections with their own predicates, and depletes as findings extract into standalone garden nodes. Distinguished from Reference (static briefing) by its depletion lifecycle and from Inquiry (poses questions) by containing evidence and analysis.

**Scenario Form**: Defines the Scenario form type: a plausible narrative of how the future could unfold given specific drivers and conditions. Scenarios don't predict — they prepare. Value lies in spanning the possibility space. Names state the hypothetical trajectory, not the driving forces.

**Seed Stage**: Defines the Seed Stage, the entry point for all garden nodes: raw capture with low confidence, unprocessed structure, and minimal links. Seeds are extraction products that have enough content to stand alone but have not been tested against other nodes, verified, or refined through use.

**Skill Form**: Defines the Skill form type: a compound node bundling trigger, procedure, quality criteria, and rationale — with graph dependencies declaring which garden nodes the skill reads and follows. Skills bridge the garden's knowledge layer and the agent's execution layer.

### Chat Log

**Chat Log**: Defines the Chat Log vault type: a text chat record from a parallel chat during a meeting or AI conversation, always derived from a parent note via derived_from:: predicate. Preserves original timestamps and speaker attribution without cleanup. Captures links shared, brief exchanges, and introductions alongside the spoken conversation.

### Decision Form

**Artifact Predicate for Binary Metadata**: The artifact:: predicate links a sidecar metadata file to the binary it describes, making the relationship explicit and graph-traversable. Agents find metadata for any binary by checking for a sidecar with artifact:: pointing to it.

**Body Predicates for Meeting Attendees**: Meeting attendees are recorded as body predicates (attendee::[\[\[Person Name\]\]↑](EXTERNAL.html#:~:text=Person%20Name)) instead of YAML frontmatter lists. More verbose for large meetings but graph-traversable, enabling queries like 'which meetings did [\[\[Person\]\]↑](EXTERNAL.html#:~:text=Person) attend?' Person names as wikilinks create connections to Person Notes.

**Classification via Predicates Not Tags**: Classification uses body-level typed relations (is_a::, has_status::) instead of YAML tags. The general litmus test: is the value a fixed scalar or a connection to a defined concept? Scalars go in frontmatter fields, connections go in typed relations, subject matter goes in wikilinks. Tags produce sets; links produce graphs.

**Custom Python Generator for Typed Relations**: Chose a custom Python static site generator (~150 lines, four-stage pipeline) over Quartz, Jekyll, Eleventy, and Pandoc for publishing a garden with predicate::[\[\[target\]\]↑](EXTERNAL.html#:~:text=target) typed relations. Standard markdown parsers ignore wikilinks, typed inline relations, and typed block-level relations — the three syntax patterns the garden depends on. A single-file generator with no external parser dependencies handles exactly what's needed.

**Deep Context as an Architecture for Captured Reasoning**: The decision to capture personal reasoning as typed markdown forms connected by predicates — not as fine-tuned models, retrieval-augmented documents, or tagged notes. Typed forms with structural contracts make reasoning traversable by agents; predicates make it navigable; progressive disclosure makes it fit in context windows.

**Descriptive Noun-Phrase Names for Predicate Targets**: Predicate targets use descriptive noun-phrase names with a two-word minimum and type-distinguishing suffixes (Form, Stage) to prevent namespace collisions while remaining readable in predicate context. Ghost links serve as a natural checklist of definition pages to create.

**Descriptive Slugs for Archive Binaries**: Archive binaries are renamed from publisher gibberish to author-year-descriptive-title-slug.ext for browsable directory listings. Original filenames are preserved in the sidecar's original_filename field.

**Display Name Preservation in Compound Documents**: When a form graduates from atomic file to compound folder, the main file keeps its display name so all existing wikilinks continue to resolve without modification. The folder uses a slug; the file inside keeps the human-readable name.

**Extraction Model for Garden Migration**: Migration from Research/ to Garden/ means extraction — surveying source documents for form-type content chunks, extracting each into its own garden node, connecting via predicates, and reducing originals over time. Source files aren't 1:1 with form types; they contain content spanning multiple nodes.

**Folder-Note Pattern for Compound Documents**: Compound documents use the folder-note pattern where the main file shares its folder's name. Graduation from atomic to compound is a git mv into a new folder. Wikilinks stay stable because Obsidian matches on filename.

**Knowledge Hub Not Binary Archive**: The vault serves as a knowledge hub, not a binary archive. Keep markdown (LLM-readable) and binaries with no other canonical source. Remove binaries available from public URLs, git repos, or re-renderable from sources. Sidecars document where removed artifacts live.

**Linear Processing Stages for Meetings**: Meeting processing uses linear stages (Captured → Transcribed → Cleaned → Summarized → Published) via has_status:: plus fork predicates (is_published::URL, is_shared::DATE) for distribution tracking. Distinct from garden content maturity stages.

**Non-Local Artifact References in Sidecars**: Sidecars can reference artifacts archived elsewhere, not just local binaries in Archives/. A sidecar with no local artifact uses derived_from:: to link to its meeting note and documents canonical sources in prose sections: Source Repository for the permanent location and Public URLs for convenience links.

**Precinct as Organizational Unit**: Adopts 'precinct' from urban planning as the organizational unit within Deep Context Architecture. Two precincts — garden and vault — solve different knowledge problems using shared infrastructure (predicates, scripts, typed edges). Neither is a maturity level of the other.

**Predicates Everywhere for Compound Nodes**: All compound nodes use body predicates for classification regardless of vault folder. No tags in frontmatter — YAML retains only scalar properties. Extends the predicate model from Garden/ to all compound structures in the vault, including Meetings/ and Research/.

**Renditions and Archives Replace Sources**: The original sources/ subfolder in compound citations splits into Renditions/ (searchable markdown copies) and Archives/ (preserved original binaries). The distinction matters because they carry different trust implications and serve different retrieval purposes.

**Renditions and Archives as Distinct Artifact Types**: Rendition names format-transformed markdown copies; archive names preserved original binaries. These terms replace the ambiguous 'source' which collides with source code and source_url. The Rendition - prefix identifies standalone renditions.

**Role-Specific Attribution Predicates for Opus Form**: Opus Form uses role-specific predicates for attribution (principal::, produced_by::, authored_by::, copyright_held_by::, foreword_by::, illustrated_by::, etc.) rather than a flat contributor list. Grounded in the principal-agent framework from agency law and the producer/principal distinction from the January 2026 email thread on authorship in the age of AI.

**Sidecar Files as Metadata Envelopes**: Binary archives get optional .sidecar.md companion files with frontmatter, summary, and typed predicates. Only warranted when a binary is actively cited or requires agent discoverability — most archives don't need sidecars.

**Snake Case for Predicate Naming**: Adopts snake_case for typed relation predicates (derived_from, relates_to) over kebab-case, camelCase, or UPPER_SNAKE. Three factors: alignment with deep context grammar, editor ergonomics (double-click selects whole predicate with underscores but not hyphens), and absence of a dominant external standard.

**Spelled-Out Names Over Internal Acronyms**: Decision to avoid acronyms in garden nodes and vault conventions. Spell out Deep Context Architecture, Self-Sovereign Identity, personal knowledge management, and map of content instead of DCA, SSI, PKM, MOC. Acronyms hurt discoverability, risk collisions across domains, and save negligible bytes. External system names (PARA, ACE, GRID) are proper names, not acronyms to expand.

**Structural Retrieval Hierarchy**: Five retrieval tiers derived from folder location and predicates rather than per-file priority fields: garden evergreen/growing nodes, vault notes, renditions, sidecars, binary archives. Priority changes require structural moves, not metadata edits.

**Universal Compound Form Graduation**: Any form may graduate from atomic file to compound folder when it accumulates related material. The original six-form list of compound-eligible types becomes illustrative, not restrictive. The graduation mechanic applies uniformly.

**Vault Type Targets for Non-Garden Notes**: Non-garden vault types (meetings, transcripts, chat logs, sidecars) get is_a:: targets following the same naming conventions as garden form types: Meeting Note, Transcript, Chat Log, Sidecar. Ghost links initially, definition pages later.

### Meeting Note

**Meeting Note**: Defines the Meeting Note vault type: a record of a synchronous conversation with attendees, topics, and outcomes. Uses body predicates for attendees and processing status. May contain compound documents with transcript, chat log, and recording sidecars.

### Person Note

**Person Note**: Defines the Person Note vault type: a contact-style record for individuals referenced across the vault. Lives in People/Individuals/ and serves as the link target for attendee:: predicates in meetings and author:: references. Includes aliases, meeting history, project associations, and relationship context.

### Sidecar

**Sidecar**: Defines the Sidecar vault type: a markdown metadata envelope for binary or non-local artifacts (video, audio, slides, PDFs) that cannot be represented directly in the knowledge graph. Uses artifact:: predicates to point to canonical sources in local Archives/ folders or remote repositories.

### Transcript

**Transcript**: Defines the Transcript vault type: a cleaned speech-to-text record derived from a meeting recording via derived_from:: predicate. Speaker-normalized (full name first, then first name) with three cleanup levels and configurable filler calibration. Always a sidecar to its meeting note, never standalone.

## Self-Sovereign Identity

### Model Form

**Self-Coercion Through Surveillance Awareness**: Model of how surveillance knowledge creates self-censorship before any rule is violated. People avoid legitimate actions fearing discrimination or negative inference. Covers chilling effects, anticipatory compliance, and the mechanism by which Protective Paternalism's safety framing makes objection socially costly.

### Inquiry Form

**Coercion Resistance as Replacement Framing**: Explores whether 'coercion resistance' or related terms (sanctuary technology, technology paternalism, exodus protocols) can replace overloaded terms like 'privacy' and 'censorship resistance' as the framing for what digital autonomy systems protect against. Maps the emerging terminology landscape across Ethereum (CROPS/sanctuary), Self-Sovereign Identity (coercion lenses), and sociotechnical design (technology paternalism).

### Citation Form

**Brignull (2010) Deceptive Patterns Dark Patterns**: Coined 'dark patterns' in 2010 and created the authoritative taxonomy of manipulative interface design now embedded in EU (DSA, DMA) and US (FTC, CPRA) law. Documents 400+ examples and $400M+ in enforcement settlements. Shows 95% of free mobile apps use deceptive patterns.

**Spiekermann and Pallas (2006) Technology Paternalism**: Originating paper for the concept of Technology Paternalism, introducing the term in the context of ubiquitous computing. Argues that beyond privacy and data security, automated environments raise questions about human control, and proposes 'the right for the last word' — the ability to overrule autonomous system behavior.

## Synpraxis

### Inquiry Form

**Participation to Community Progression as Garden Concepts**: Investigates how the participation-engagement-affinity-association-community framework from the author's pedagogy work should be represented in the garden. Individual terms may be Gloss Form nodes; the progression may be a Model or a synthesis gloss; the relationship to cooperation-collaboration research needs exploration.

### Opus Form

**My Hybrid Flipped Learning Environment**: Christopher Allen explains his teaching philosophy at Bainbridge Graduate Institute, where he applied game design principles to hybrid education. Describes the orient-scan-focus-act-reflect learning cycle, iterative feedback design, flow-based engagement, and collaborative artifact creation that later evolved into the sociosocratic learning method.

**Sociosocratic Learning & Seminars**: Christopher Allen describes the sociosocratic learning method, where small groups build shared language and agency through collaborative artifact creation rather than lectures, following an orient-scan-focus-act-reflect cycle across multiple sessions.

### Decision Form

**Synpraxis as Domain Name**: Coins 'synpraxis' (Greek: syn + praxis = acting together) to name the knowledge domain covering how independent agents achieve outcomes together across varying degrees of integration — including anti-patterns. Chosen over existing terms (collective action, shared agency, cooperative systems) because none covers the full territory: constructive patterns, failure modes, preconditions, and the coordination-cooperation-collaboration spectrum.

## Uncategorized

### Reference Form

**Compound Nodes for Knowledge Management**: Defines compound nodes — folder-based knowledge objects with a lead file, sibling files, renditions, and archives. Introduces terminology (context node, typed edge, lead file, compound node) and proposes strategies for context conservation, binary management, and sidecar linking. Generalizes existing deep context garden ADRs (C07-C22) to vault-wide application.

### Opus Form

**Field Notes on Handpan Sound Models & Instruments**: Personal field notes documenting specific handpan instruments and their sound models — the scale templates, acoustic character, modal theory, and ensemble compatibility. Each instrument is documented as both an interactive web page (with tone circles and audio playback) and portable markdown. Planned for publication at www.spiralrhapsody.com/fieldnotes/.

### Person

**Martina Kolpondinos**: Interaction designer and digital identity researcher. Former member of the Swiss federal eID team. Co-editor of WebVH specification. Founder of KosmaConnect. Active in Revisiting Self-Sovereign Identity workshops, contributing perspectives on technology paternalism and coercion resistance.

### Person Note

**Christopher Allen**: Christopher Allen is the founder and president of Blockchain Commons, author of the 10 Principles of Self-Sovereign Identity (2016), co-editor of the TLS 1.0 draft, and principal authority of this vault's augmented knowledge system. His work bridges applied cryptography, digital identity, and trust architecture through the Gordian stack, XIDs, and the principal authority framework rooted in agency law.

**Jonathan Postel**: Jonathan Postel (1943-1998) — RFC Editor from 1969 until his death, creator of IANA, co-architect of TCP/IP, SMTP, and DNS. His Robustness Principle ('be liberal in what you accept') shaped protocol design for decades. The Inter-Face Protocol's 'clarity over tolerance' principle is a direct, respectful departure from Postel's Law for the age of reasoning agents.

**Peter Kaminski**: Profile of Peter Kaminski — wiki gardener, context engineer, agentic AI course instructor. Projects include MassivePub (static site generator for markdown wikis), TextPile, and the Interface Protocol (IFP) for human-agent-agent-human communication. Starting paid agentic AI course March 2026 using Obsidian and Claude Code. Core drive: helping regular people use capable tools.

### Untyped

**Digital Identity**: MOC spanning the range from centralized identity databases to self-sovereign models where individuals control their own credentials. Anchors on W3C standards (DIDs, Verifiable Credentials) and collaborative design forums (Rebooting the Web of Trust), with trust frameworks governing who trusts whom as a key cross-cutting concern.

**Gordian Envelope as Agent Memory Layer**: Analysis of Gordian Envelope — a recursive CBOR type organizing data as subject-predicate-object triples with SHA-256 content-addressing and selective elision — as a trust and exchange layer for AI agent memory. Covers the five enumerated cases, signing, and how elision enables privacy-preserving memory sharing between agents.

**Research Note**: *(no summary available)*

**The Gardening Problem Returns - Document Lifecycle in the Age of AI Agents**: Collaborative article outline arguing wiki communities spent 25 years developing document lifecycle heuristics (split, merge, rewrite, delete) that AI developers now rediscover under new names. Four authors — Allen, Kaminski, Michalski, Udell — each augmented by different tools, ask whether those heuristics transfer.

### reference

**Revisiting Self-Sovereign Identity Initiative**: The Revisiting Self-Sovereign Identity initiative (2025-2026) develops coercion-prevention lenses and revised principles for the 10th anniversary of the original Ten Principles. Pivoted from community-drafting model to curated approach by Christopher Allen and Shannon Appelcline, with workshop participants providing feedback.

### web_clipping

**Dimensions of Digital Coercion**: Four dimensions of coercive control online: attention (manufactured outrage), ergonomic (privacy trade-offs dressed as consent), trust (assumed benign intent without accountability), cultural (dominant norms as participation prerequisites). Coercion is structural — present in open-source ecosystems as much as commercial platforms.

## Ghost Links

These wikilinks appear in the patch but reference nodes that do not exist yet — either in this patch or in the source garden. They mark where a node could grow.

### Upstream Ghost Links (referenced in Synpraxis domain page)

- Agency Before Collaboration
- Is Collaboration Always Superior to Cooperation
- Is Consensus One Mechanism or Three
- Is the Synpraxis Spectrum a True Continuum
- Precondition Dependencies in Joint Action
- Precondition Stack for Joint Action

### Other Ghost Links

- Autonomy
- Choice Architecture
- Coercion Resistance
- Curated
- Descriptive Slugs for Archive Binaries
- Gordian Envelope as Agent Memory Layer
- Progressive Trust
- The Gardening Problem Returns

### People

- Coraline Ada Ehmke
- Roy (2026) Words Without Consequence, from The Atlantic

