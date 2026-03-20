---
created: 2026-03-06
author: Christopher Allen
brief_summary: "Domain index for Synpraxis — the study of how independent agents achieve outcomes together across varying degrees of integration. From Greek syn (together) + praxis (purposeful action). Covers the full spectrum from loose coordination through cooperation to deep collaboration, including anti-patterns: defection, free-riding, parasitism, coercion, and capture. Spans biology, game theory, governance, organizational theory, computer science, and the arts."
tagline: "How independent agents achieve outcomes together — and how it breaks down"
---

← [Garden Patch Home](../) · [Domains](index.html)


- is_a::[\[\[Domain Form\]\]](../forms/Domain%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)

# Synpraxis

Synpraxis (Greek: syn + praxis = "acting together") is the study of how independent agents achieve outcomes together across varying degrees of integration — and how those arrangements fail, are exploited, or turn adversarial. The domain encompasses coordination, cooperation, and collaboration as points on a spectrum, not as interchangeable synonyms, along with their anti-patterns: defection, free-riding, capture, coercion, and parasitism.

The term is coined to name what no existing term covers cleanly. "Cooperation" and "collaboration" each name one region of the spectrum. "Collective action" (Olson) is narrowed to public goods and free-rider problems. "Game theory" covers the formal mathematics but not the institutional, biological, or creative dimensions. "Interdependence" names the condition but not the dynamics. Synpraxis names the full territory: the constructive patterns, the failure modes, and the structural conditions that favor one over the other.

## Scope

**Covers**: The coordination-cooperation-collaboration spectrum and its orthogonal dimensions; preconditions for authentic joint action (privacy, agency, identity sovereignty, fair incentives, trust); mechanisms of joint action (consensus — human and machine, governance, incentives, protocols); dynamics under interdependence (reciprocity, defection, coopetition, arms races); anti-patterns and failure modes; institutional design for collective outcomes (commons governance, cooperative structures); biological cooperation (mutualism, symbiosis, kin selection); computational cooperation (consensus algorithms, Byzantine fault tolerance, multi-agent systems, collaborative editing); creative collaboration (co-creation, emergent output, shared intentionality); cooperative play and game design; pattern languages for group process.

**Does not cover**: Individual cognition or solo performance. Competition and conflict are in scope only where they interact with cooperative dynamics (coopetition, competitive escalation, defection within cooperative frames). Pure market competition without cooperative structure belongs elsewhere. Personal history and case studies of synpraxis in practice are separate forms (future cases), not part of the domain definition.

## The Spectrum

The cooperation-collaboration inquiry identified persistent axes across all domains examined. The spectrum has three positions — coordination, cooperation, collaboration — but many orthogonal dimensions that do not all move together. A given arrangement can show high trust with low identity-merging, or shared goals with no shared governance. The three positions are useful landmarks, not rigid categories; real joint action often occupies the spaces between them or combines elements from different levels.

### How the work happens

| Dimension | Coordination | Cooperation | Collaboration |
|-----------|-------------|-------------|---------------|
| Division of labor | Align timing, avoid conflict | Split tasks, assemble results | Work intertwined throughout |
| Goals | Avoid mutual harm | Compatible but separate | Genuinely shared |
| Output | Deconflicted actions | Sum of parts | Greater than sum of parts |
| Structure | Rules, protocols | Roles, incentives | Self-organizing, emergent |
| Authority | Central or protocol-based | Each party autonomous | Joint governance |
| Accountability | Each for own compliance | Each for own deliverable | Joint, mutual |
| Information sharing | Signals, minimal | Relevant information exchanged | Open, full transparency |

### What the work requires

| Dimension | Coordination | Cooperation | Collaboration |
|-----------|-------------|-------------|---------------|
| Agency required | Procedural | Behavioral | Intentional, shared cognition |
| Trust required | Predictability | Good faith | Vulnerability, psychological safety |
| Power symmetry | Can be imposed top-down | Accommodates asymmetry | Implies rough equality of agency |
| Identity | Separate, unaffected | Separate, acknowledged | Partially merged ("we" for this purpose) |

### What's at stake

| Dimension | Coordination | Cooperation | Collaboration |
|-----------|-------------|-------------|---------------|
| Risk | None assumed | Minimal, individual | Shared, mutual |
| Exit cost | Trivial | Moderate switching cost | High — entangled work, shared IP/liability |
| Coercion vulnerability | Low (exit is cheap) | Medium (can be compelled) | High (identity is entangled) |
| Conflict resolution | Exit or escalate | Negotiate | Internal governance |

### Cross-cutting mechanisms

Some mechanisms are not spectrum positions but operate *across* the spectrum, taking different forms at each level.

**Consensus** is the most important cross-cutting mechanism. It operates at three distinct levels:

- **Machine consensus** (coordination level) — Algorithms that enable distributed nodes to agree on state without a trusted central authority. The Byzantine generals problem (Lamport, 1982) formalized the challenge; proof-of-work (Nakamoto, 2008) demonstrated a practical solution. Machine consensus is deterministic or probabilistic, operates on data, and requires no shared understanding — only protocol compliance.

- **Negotiated consensus** (cooperation level) — Parties with compatible but separate goals reach agreement through structured process. Parliamentary procedure, standards bodies, treaty negotiation. Each party retains autonomy; the consensus is an agreed outcome, not a shared mental state. Groupware (in its original definition: "intentional group processes and software to support them") was designed to facilitate this level.

- **Emergent shared understanding** (collaboration level) — Meaning converges through joint work. Not a vote or a protocol outcome but an alignment of mental models that emerges from sustained interaction. Jazz improvisation converging on a feel. A writing partnership arriving at a shared voice. This cannot be algorithmed — it requires the full stack of preconditions (agency, trust, psychological safety).

Whether these three levels are one mechanism at different scales or three distinct mechanisms that share a label is an open question (see [\[\[Is Consensus One Mechanism or Three\]\]↑](../NODES.html#:~:text=Is%20Consensus%20One%20Mechanism%20or%20Three)). The levels do inform each other in both directions. Machine consensus proved that distributed agreement is achievable without trusted third parties — a result that reshapes what's thinkable about human coordination. Conversely, groupware research demonstrated that computational solutions for human consensus fail without human preconditions: people will not use collaborative software if they believe it is a panopticon. Privacy is not a feature of consensus tools; it is a precondition for the cooperation those tools are meant to support.

**Pattern languages** are another cross-cutting mechanism — structured collections of recurring solutions that can operate at any spectrum level. The Group Works Project produced 91 patterns for group process spanning facilitation, decision-making, and collective intelligence. *Meeples Together* produced patterns for cooperative game design. Alexander's original architectural pattern language was itself a collaborative artifact. Pattern languages are both a product of synpraxis and a tool for improving it.

## Preconditions

The spectrum is not just descriptive — each position has structural preconditions. Remove a precondition and you don't get a lesser form of joint action; you get an anti-pattern. This dependency chain is a thesis, not established fact; the strength of each link varies and some are contested (see [\[\[Precondition Dependencies in Joint Action\]\]↑](../NODES.html#:~:text=Precondition%20Dependencies%20in%20Joint%20Action)).

| Precondition | What it enables | What breaks without it |
|-------------|----------------|----------------------|
| **Predictability** | Coordination | Collision, deadlock |
| **Privacy** | Coercion-resistance → agency | Surveillance chills authentic participation |
| **Agency** | Genuine (not performative) cooperation | Coerced cooperation, compliance theater |
| **Incentive compatibility** | Sustained cooperation | Rational defection, free-riding |
| **Identity sovereignty** | Full participation as an agent, not a subject | Capture, exploitation |
| **Exit rights** | Voluntary participation at every level | Coercion disguised as cooperation |
| **Trust** (built on the above) | Collaboration | Groupthink (false trust) or paralysis (no trust) |

The dependency runs upward: privacy enables coercion-resistance, which enables agency, which enables genuine cooperation, which (with incentive compatibility and identity sovereignty) builds the trust required for collaboration. Each layer depends on those below it. This is why security infrastructure, identity systems, and incentive design are synpraxis problems — they are preconditions for authentic joint action, not separate concerns.

Two notes on contested preconditions. "Fair incentive distribution" is better framed as **incentive compatibility** — a system-design property where individual rationality aligns with collective benefit. Bitcoin demonstrated this: the system works because defection is expensive, not because a central authority distributes rewards "fairly." Fairness is a value judgment; incentive compatibility is a structural property. Second, **exit rights** deserve explicit status as a precondition rather than being implicit in "agency." The ability to leave a cooperative arrangement without catastrophic cost is what keeps cooperation voluntary. Markets work as coordination mechanisms precisely because exit is cheap. When exit becomes prohibitively expensive, cooperation shades into coercion regardless of how it started.

The deepest pattern across all domains: cooperation describes behavioral outcomes regardless of cognitive sophistication (bacteria cooperate, OS processes cooperate, nations cooperate). Collaboration implies shared intentional creation — it requires minds that can hold shared representations and produce emergent novelty. But collaboration also requires the most preconditions, which is why it is the most fragile and the most rewarding — and why collaboration is not always the right choice (see [\[\[Is Collaboration Always Superior to Cooperation\]\]↑](../NODES.html#:~:text=Is%20Collaboration%20Always%20Superior%20to%20Cooperation)).

## Anti-Patterns and Defection Dynamics

Understanding how joint action breaks down is not optional — it is half the domain. Anti-patterns are not simply failure modes to avoid; they are dynamics to understand because the same behavior can be pathological or adaptive depending on the system it occurs within. Schneier argues in *Liars and Outliers* that while defectors threaten trust (liars, criminals, cheaters), certain forms of rule-breaking — whistleblowing, civil disobedience, resistance to unjust laws — help societies adapt and correct flawed norms. The goal is not eliminating defection but managing it. A system with zero defection is either totalitarian or fictional.

This has a design consequence: you cannot build resilient cooperative systems without modeling the predator. Understanding the incentives and motivations of defectors, parasites, and coercers is prerequisite to designing systems that withstand them — or that become antifragile (Taleb), gaining strength from stressors rather than merely surviving them. Security infrastructure, incentive design, and governance all require threat models, and threat models require understanding anti-patterns from the inside.

These dynamics operate at different levels of analysis — individual moves (defection), group dynamics (groupthink), institutional structures (capture) — which is a feature of the domain's breadth, not a flaw in the taxonomy.

### Insufficient cooperation

- **Defection** — choosing individual gain over collective benefit (prisoner's dilemma). But defection from an unjust system is resistance; defection that reveals hidden information is whistleblowing. Context determines whether defection is pathological or adaptive.
- **Free-riding** — consuming collective goods without contributing (Olson's collective action problem)
- **Tragedy of the commons** — uncoordinated exploitation of shared resources (Hardin; answered by Ostrom)
- **Social loafing** — reduced individual effort in group settings

### Exploited cooperation

- **Parasitism** — one-sided extraction disguised as mutualism
- **Capture** — regulatory, institutional, or governance capture by concentrated interests
- **Collusion** — cooperation *against* third parties (antitrust, cartel behavior)
- **Collaboration with the enemy** — cooperation weaponized against one's own community; the wartime anti-pattern that permanently stained the word

### Excessive integration

- **Coercion** — forced cooperation that destroys the voluntary basis
- **Groupthink** — pathological consensus that suppresses dissent; false collaboration without genuine agency
- **Forced consensus** — demanding agreement as a social obligation rather than earning it through process
- **Identity submersion** — collaboration that demands total identity-merging without exit rights; the commune failure mode where individual voice is sacrificed to collective harmony
- **Tyranny of the majority** — democratic process used to override minority agency rather than accommodate it

## Key Thinkers and Frameworks

### Spectrum and Dynamics

- **Mattessich** — cooperation-coordination-collaboration continuum in organizational theory
- **Deutsch** — interdependence theory; cooperation and competition as social processes
- **Bratman** — shared agency; philosophical account of shared intentional activity
- **Johnson & Johnson** — cooperative learning; formal structure for educational cooperation
- **Dillenbourg** — collaborative learning; "in cooperation partners split the work; in collaboration they do it together"

### Game Theory and Evolution

- **Nash** — cooperative vs non-cooperative game theory; binding agreements as the formal distinction
- **Axelrod** — evolution of cooperation; iterated prisoner's dilemma, tit-for-tat
- **Nowak** — five rules for the evolution of cooperation (kin selection, direct/indirect reciprocity, network reciprocity, group selection)

### Governance and Collective Action

- **Ostrom** — commons governance; 8 design principles for managing shared resources without privatization or state control
- **Olson** — collective action problem; why rational individuals fail to act for group benefit

### Trust, Defection, and Resilience

- **Schneier** — *Liars and Outliers*; trust as societal infrastructure, useful defectors (whistleblowers, civil disobedience), managing defection rather than eliminating it
- **Taleb** — *Antifragile*; systems that gain from stressors; understanding predatory dynamics as prerequisite for resilient design

### Consensus

- **Lamport** — Byzantine generals problem; foundational framing of distributed consensus
- **Nakamoto** — proof-of-work consensus; demonstrated that distributed agreement is achievable without trusted third parties

### Pattern Languages for Group Process

- **Group Works Project** — pattern language for helping groups function (deck of 91 patterns)
- **Allen & Appelcline** — *Meeples Together*; pattern language for cooperative game design

## Key Forms

### Decisions

- [\[\[Synpraxis as Domain Name\]\]↑](../NODES.html#:~:text=Synpraxis%20as%20Domain%20Name) — why we coined "synpraxis" over existing terms; alternatives evaluated, collisions found

### Convictions

- [\[\[Authentic Collaboration Requires Agency\]\]](../convictions/Authentic%20Collaboration%20Requires%20Agency.html) — authentic collaboration is impossible without agency; the world's important problems require collaboration; therefore agency infrastructure is prerequisite

### Inquiries

- [\[\[Cooperation vs Collaboration as Distinct Concepts\]\]](../inquiries/Cooperation%20vs%20Collaboration%20as%20Distinct%20Concepts.html) — etymological, lexical, and cross-domain analysis of the distinction

## Open Questions

### Inquiry candidates (ghost links)

These questions are substantial enough to warrant their own inquiry forms:

- [\[\[Is Consensus One Mechanism or Three\]\]↑](../NODES.html#:~:text=Is%20Consensus%20One%20Mechanism%20or%20Three) — Does "consensus" at machine, negotiated, and emergent levels name one mechanism at different scales, or three distinct mechanisms sharing a label? (Referenced from Cross-cutting mechanisms above.)
- [\[\[Is Collaboration Always Superior to Cooperation\]\]↑](../NODES.html#:~:text=Is%20Collaboration%20Always%20Superior%20to%20Cooperation) — The spectrum's own "what's at stake" table shows collaboration has the highest coercion vulnerability, exit cost, and risk. When is staying at the cooperation level the right choice? Markets are the most successful coordination mechanism in history and they operate through cooperation, not collaboration. (Referenced from Preconditions above.)
- [\[\[Precondition Dependencies in Joint Action\]\]↑](../NODES.html#:~:text=Precondition%20Dependencies%20in%20Joint%20Action) — Is the preconditions dependency chain (privacy → agency → cooperation → trust → collaboration) a logical necessity or an empirical claim? Open source communities collaborate in radical transparency. Scientists collaborate across political systems with minimal privacy. Which links are strong and which are contested? (Referenced from Preconditions above.)
- [\[\[Is the Synpraxis Spectrum a True Continuum\]\]↑](../NODES.html#:~:text=Is%20the%20Synpraxis%20Spectrum%20a%20True%20Continuum) — Are coordination, cooperation, and collaboration points on a single axis, or categorically different phenomena? The 15 dimensions don't all move together. Wittgenstein might ask whether they share a family resemblance rather than a common essence.

### Research questions

- Where does "coordination" sit formally on the spectrum? It appears between cooperation and collaboration in Mattessich's continuum and as distinct from cooperation in IR theory.
- How does synpraxis relate to the vault's principal-agent relationship? Is the human-agent relationship cooperation (agent assists principal's goals) or collaboration (shared creation)?
- What forms should be extracted from Ostrom's commons governance work? Her 8 design principles are natural pattern or principle candidates.
- Does the biological cooperation literature (kin selection, reciprocal altruism, mutualism) yield forms that inform institutional design?
- How do cooperative play patterns (broader than cooperative games — play doesn't require success) relate to cooperative dynamics in non-game contexts?
- What is the relationship between the Group Works patterns (91 patterns for group process) and the synpraxis spectrum? Are they cooperation patterns, collaboration patterns, or both?
- Is "coopetition" (simultaneous cooperation and competition) a distinct spectrum position, a dynamic between positions, or an anti-pattern? (Brandenburger & Nalebuff, 1996, have a substantial literature not yet engaged here.)
- Is "psychological safety" (Edmondson) the right precondition for dissent within collaboration, or is "exit rights" sufficient? The libertarian argument: adults need freedom to leave, not protection to stay.

## Sources

- Axelrod, R. (1984). *The Evolution of Cooperation*
- Ostrom, E. (1990). *Governing the Commons*
- Olson, M. (1965). *The Logic of Collective Action*
- Deutsch, M. (1949). "A Theory of Cooperation and Competition"
- Nowak, M. (2006). "Five Rules for the Evolution of Cooperation"
- Bratman, M. (2014). *Shared Agency: A Planning Theory of Acting Together*
- Mattessich, P. et al. (2001). *Collaboration: What Makes It Work*
- Dillenbourg, P. (1999). "What do you mean by collaborative learning?"
- Keohane, R. (1984). *After Hegemony: Cooperation and Discord*
- Schneier, B. (2012). *Liars and Outliers: Enabling the Trust that Society Needs to Thrive*
- Taleb, N. N. (2012). *Antifragile: Things That Gain from Disorder*
- Brandenburger, A. & Nalebuff, B. (1996). *Co-opetition*
- Edmondson, A. (1999). "Psychological Safety and Learning Behavior in Work Teams"
- Lamport, L. et al. (1982). "The Byzantine Generals Problem"
- Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System"
- Allen, C. & Appelcline, S. (2019). *Meeples Together: How and Why Cooperative Board Games Work*
- Group Works Project. *Group Works: A Pattern Language for Bringing Life to Meetings and Other Gatherings* (deck of 91 cards)

## Extraction Manifest

This domain page currently carries content that belongs in typed forms. The sections above will be trimmed as forms are extracted. Content remains here until extracted — this is a living document, not a finished index.

### Models (extract from Spectrum, Preconditions, Anti-Patterns, Consensus sections)

- Coordination-Cooperation-Collaboration Spectrum — 15 dimensions across 3 tables
- Precondition Stack for Joint Action — dependency chain from privacy to trust
- Consensus Across Synpraxis Levels — machine, negotiated, emergent
- Synpraxis Anti-Pattern Taxonomy — 3 categories, 13+ failure modes

### Glosses (extract from inline definitions)

- Synpraxis as Coined Domain — etymology, why existing terms don't cover the territory
- Useful Defection (Schneier) — whistleblowing, civil disobedience, resistance to unjust norms as adaptive defection
- Incentive Compatibility vs Fairness — Bitcoin's insight: expensive defection, not administered fairness
- Cooperative Play vs Cooperative Games — play doesn't require success
- Groupware (Original Definition) — "intentional group processes and software to support them"
- Coopetition — simultaneous cooperation and competition (Brandenburger & Nalebuff)
- Antifragility in Cooperative Systems — systems that gain strength from stressors (Taleb); requires understanding predatory dynamics

### Principles

- Agency Before Collaboration — the precondition stack as a priority declaration

### Boundaries

- Cooperation Without Agency Is Compliance — the line between genuine cooperation and performative compliance

### Patterns

- Privacy as Cooperation Prerequisite — people won't use collaborative tools they perceive as panopticons
- Out-Cooperating Incumbents — winning through superior cooperative structure rather than superior resources

### Cases (from personal experience — future forms)

- SSL/TLS: Out-Cooperating Incumbents
- Groupware to Security Pivot
- Arkham Horror Second Edition Revival
- Group Works Pattern Language
- Bitcoin and Incentive Compatibility
- Self-Sovereign Identity as Cooperation Enabler

### From Open Development article

- Accessibility of Participation — open communities must have clearly stated rules for joining, participating, and remaining a member (principle)
- Diversity as Creative Fuel — not only accept diversity of ideas but seek it out; deep-level diversity (cultures, disciplines, roles) is beneficial to core creativity (conviction or principle)
- Open Development as Spectrum Not Binary — openness is a spectrum of practices (levels 0-7), not a licensing binary; incremental improvement is achievable (model)
- Sustainability of Cooperative Infrastructure — cooperative systems must be dependable over their entire lifespan; the Heartbleed lesson applied to institutional design (principle)
- Collaborative Ecosystem Building — no single entity controls evolution; innovation across a diverse network ensures adaptability and inclusivity (pattern)
- Techno-Social Contract — bridging technical capabilities with cultural, economic, and legislative frameworks for sustainable cooperative systems (model)
- Progressive Trust as Relationship Evolution — systems reflecting the natural evolution of trust through selective disclosure (pattern, bridges [\[\[Self-Sovereign Identity\]\]](Self-Sovereign%20Identity.html))

### Inquiries (ghost links already in Open Questions)

- Is Consensus One Mechanism or Three
- Is Collaboration Always Superior to Cooperation
- Precondition Dependencies in Joint Action
- Is the Synpraxis Spectrum a True Continuum
- Cooperative Play as Synpraxis Model

## Relations

- relates_to::[\[\[Deep Context Architecture\]\]](Deep%20Context%20Architecture.html) — synpraxis dynamics inform how the vault models multi-agent knowledge work
- relates_to::[\[\[Self-Sovereign Identity\]\]](Self-Sovereign%20Identity.html) — without identity sovereignty, cooperation is performative; self-sovereign identity provides a synpraxis precondition
- relates_to::[\[\[Authority Flows from the Person\]\]](../principles/Authority%20Flows%20from%20the%20Person.html) — agency as a non-alienable precondition for authentic joint action
- relates_to::[\[\[Principal-Agent Relationship in Augmented Knowledge Work\]\]](../models/Principal-Agent%20Relationship%20in%20Augmented%20Knowledge%20Work.html) — the vault-agent relationship sits somewhere on the synpraxis spectrum
- relates_to::[\[\[Opus Form\]\]](../forms/Opus%20Form.html) — opus (Latin: work product) shares the etymological root of cooperation (operari, from opus); the author's substantial works on synpraxis topics are tracked as Opuses
- relates_to::[\[\[Participation to Community Progression as Garden Concepts\]\]↑](../NODES.html#:~:text=Participation%20to%20Community%20Progression%20as%20Garden%20Concepts) — the participation-engagement-affinity-association-community progression operates within synpraxis territory
- relates_to::[\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html) — where authority is shared vs retained maps onto the cooperation-collaboration axis
