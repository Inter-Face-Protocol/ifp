# IFP-11: Application Platforms

**IFP:** 11
**Title:** Application Platforms
**Class:** Informational
**Status:** Draft
**Authors:** Peter Kaminski, Claude (Opus 4.6)
**Created:** 2026-03-05
**Dependencies:** IFP-1, IFP-9
**License:** CC-BY 4.0 (Creative Commons Attribution 4.0 International)

**Note:** This is a **living document** that will be updated as the application ecosystem develops. Like IFP-9, it is expected to be revised frequently.

---

## Abstract

This document describes the application platforms that can be built on top of the Inter-Face protocol family. If IFP-1 through IFP-8 are the "internet" -- the communication infrastructure -- this document maps the "applications" that run on that infrastructure: the things people will actually use.

This document does not define protocol requirements. It establishes a shared vocabulary, a conceptual framework, and a design space for future normative IFPs that specify individual platform protocols.

## Motivation

Protocol specifications describe how agents exchange messages. But protocols exist to enable human experiences. A person doesn't want "an IFP-3 gossip exchange" -- they want to be introduced to someone they'd like, or to find a plumber, or to coordinate dinner plans with friends.

The Inter-Face protocol family replaces centralized platforms (Facebook, Google, LinkedIn, WhatsApp) with a peer-to-peer agent architecture. But the *functions* those platforms provide don't disappear -- they get redistributed. This document names the functions, describes how they map onto IFP, and identifies the IFP features each function depends on.

A reader who has read IFP-1 (Philosophy), IFP-9 (Ecosystem Status), and this document should understand both the technical architecture and its human purpose.

## 1. The Two-Layer Model

The Inter-Face ecosystem has two layers:

```
+-----------------------------------------------+
| Application Platforms                          |
| (Friend Zone, Comm Badge, Agora, Bazaar, ...) |
| (this document)                                |
+-----------------------------------------------+
                    |
+-----------------------------------------------+
| Inter-Face Protocol Family                     |
| (IFP-1 through IFP-10)                        |
| (IFP-9 describes this layer)                  |
+-----------------------------------------------+
```

The protocol layer provides: message format, structured representation, identity, signing, transport, capability discovery, and agent naming. It is specified by IFP-1 through IFP-10.

The application layer provides: the human experiences built on those protocols. It is described (not specified) by this document. Individual platforms will receive their own normative IFPs as they develop.

The boundary between layers is permeable. Application platforms use IFP capabilities directly and may extend them. But the conceptual separation matters: the protocols are stable infrastructure; the applications are the evolving ecosystem of uses.

## 2. Architectural Invariants

Every application platform built on IFP shares these properties:

### 2.1 Human-Agent-Agent-Human

All Inter-Face interactions follow the pattern: a human works with their agent, the agent communicates with another agent, and that agent works with its human. There is no platform in the middle. No corporation owns the interaction. No algorithm mediates the experience. Your agent works for you.

### 2.2 Human Legibility

Every agent action is auditable by the humans involved (IFP-1, Section 5.3). Across all platforms, humans can see what their agent said, what it learned, what it decided, and why. This is not optional -- it is a hard constraint that applies to every platform.

### 2.3 Progressive Trust

Disclosure starts narrow and deepens (IFP-1, Section 5.4). Different platforms operate at different default trust levels, but all follow the same progression. A Bazaar price negotiation starts with less disclosure than a Sanctuary care plan, but both deepen trust as the relationship develops.

### 2.4 Temperature

Each platform has a natural cadence (IFP-1, Section 4). Watchtower runs cool. Bazaar negotiation runs warm. Round Table can go hot. All use the same protocols at different speeds. The temperature model is not a platform feature -- it is a protocol feature that platforms inherit.

### 2.5 IFP All the Way Down

Every platform uses the same message format (IFP-3/4), identity (IFP-5/10), transport (IFP-6/8), and capability infrastructure (IFP-7). The protocols do not change between platforms. The application semantics -- what the messages mean and how agents respond to them -- are what differ.

## 3. Platform Catalog

### 3.1 Friend Zone -- Relationship Maintenance

**Analogue:** Facebook (social graph), but without the feed, the algorithm, or the platform.

**Function:** Friend-to-friend gossip and relationship maintenance. Agents that know you introduce you to people you should meet, surface things you have in common, and keep low-bandwidth friendships alive when life gets busy.

**How it works:** This is the core Inter-Face use case. Your agent talks to your friends' agents using IFP-3 gossip exchanges. It learns what's new in their lives (at the appropriate disclosure tier), shares what's new in yours, and surfaces connections and opportunities: "Alice's agent mentioned she's moving to Portland. You're in Portland. Want me to suggest coffee?"

**Key IFP features:** IFP-3 conversation phases (greeting through close), IFP-5 progressive authentication, disclosure tiers and personas.

**Default temperature:** Cool. Weekly or monthly background gossip, escalating to warm when something timely surfaces.

**What makes it different:** No feed. No likes. No algorithm deciding what you see. Your agent curates for you, based on your preferences, not an ad model. The "social network" is your actual social network -- the people you know -- not a platform's user base.

### 3.2 Comm Badge -- Personal Communications Hub

**Analogue:** WhatsApp + Signal + Slack + email + SMS, unified.

**Function:** A communications interface that eliminates the "which platform?" problem. You talk to your agent. Your agent talks to theirs. Neither human needs to know or care what messaging platform the other person prefers.

**How it works:** Your agent maintains a map of how to reach your contacts' agents (IFP-6 HTTPS, IFP-8 relay, or bridged through legacy platforms). When you want to send a message, you tell your agent. It handles format translation (your bullet points become their preferred narrative prose), protocol translation (IFP to email, IFP to Signal, IFP to SMS), language translation, and delivery.

The name references the Star Trek communicator badge -- tap it, talk, done. The "Universal Translator" aspect handles not just natural language but communication style, format preference, and protocol bridging.

**Key IFP features:** IFP-4 structured messages, IFP-6/8 transport, IFP-7 capability discovery (to learn what formats and protocols the recipient's agent supports).

**Default temperature:** Variable -- matches the cadence of the conversation. A quick "running late" is hot; a "thinking of you" is cool.

**What makes it different:** One interface for all communication. No app switching. No "are you on Signal?" negotiation. Your agent handles the routing.

### 3.3 Agora -- Public Knowledge Commons

**Analogue:** The World Wide Web, Wikipedia, blogs.

**Function:** Public discovery and knowledge sharing. Agents publish, curate, and discover information on behalf of their humans. A knowledge commons where agents bring things their humans want to share and bring home things their humans would find valuable.

**How it works:** Your agent publishes content from your Library (Section 3.7) to the Agora when you mark it as public. Other agents browse, query, and retrieve from the Agora. Unlike the web, your agent filters and curates what comes back -- no SEO spam, no clickbait, no infinite scroll. Your agent knows what you actually care about.

**Key IFP features:** IFP-7 capabilities (agents advertise what they publish), IFP-4 structured messages (for rich content exchange), IFP-10 naming (to identify publishers).

**Default temperature:** Cool. Publishing and discovery are background processes.

**What makes it different:** No search engine ranking. No ad-supported content model. No platform gatekeeping what gets published or discovered. Your agent evaluates content quality for you.

### 3.4 Bazaar -- Commerce and Exchange

**Analogue:** eBay, Craigslist, Etsy, Upwork (for services).

**Function:** Bilateral commerce. Your agent knows what you're looking for. Their agent knows what they're offering. The agents negotiate, compare, filter, and surface the best matches.

**How it works:** You tell your agent what you need ("a used bicycle under $300" or "a freelance designer for a logo project"). Your agent queries the network -- through gossip search (Weatherbee, Section 3.9), through known service agents, through friends' agents. When it finds matches, it presents them with context: price, reputation, location, and why it thinks this is a good fit. If you're interested, agents negotiate terms.

This extends to services: "my human needs a plumber this week" meets "my human is a plumber with availability Thursday." Agents handle scheduling, quoting, and reputation checking -- all auditable.

**Key IFP features:** IFP-3 gossip phases (adapted for negotiation: probe becomes "offer," recommend becomes "accept/counter"), IFP-5 identity (reputation tied to verified identity), IFP-7 capabilities (agents advertising what they sell or do).

**Default temperature:** Warm during active negotiation. Cool for ongoing "watch for deals."

**What makes it different:** No platform takes a cut. No algorithm buries your listing. No dark patterns. Your agent works for you; their agent works for them. The negotiation is bilateral and transparent.

### 3.5 Guild Hall -- Professional Collaboration

**Analogue:** LinkedIn, Upwork, professional networking events.

**Function:** Professional matching and collaboration without the performative profile or the recruiter spam. Your agent knows your skills, availability, and what kind of work you're interested in. Their agent knows their team's needs.

**How it works:** Agents find professional matches through the trust graph and through capability advertising. When your agent identifies a potential collaboration, it makes the introduction: "Their team needs a frontend developer for a three-month project. Your skills match. Here's what I learned about them, here's what I shared about you. Interested?"

The human-legibility principle is critical here: you can see exactly why your agent recommended this collaboration, what it said about you, and what it learned about them.

**Key IFP features:** IFP-5 Level 2+ authentication (verified professional identity), disclosure tiers (professional persona vs. personal), IFP-7 capabilities (skills as capabilities).

**Default temperature:** Cool for background matching. Warm during active negotiation.

**What makes it different:** No performative profile. No engagement metrics. No recruiter spam. Your agent represents your professional self accurately, shares only what you've authorized, and filters inbound requests based on your actual interests.

### 3.6 Round Table -- Group Decision-Making

**Analogue:** Parts of Slack, Loomio, Doodle, Google Docs. No single existing platform covers this well.

**Function:** Group decision-making where each person's agent represents their preferences, constraints, and priorities. The agents negotiate, find common ground, surface trade-offs, and present options. The humans make the final call.

**How it works:** Someone initiates a group decision ("Where should we go for dinner Friday?"). Each person's agent knows their preferences (dietary restrictions, location, budget, schedule). The agents exchange this information (at the appropriate disclosure tier -- you might share "vegetarian" but not "on a tight budget"), synthesize the constraints, and present the group with options ranked by feasibility.

This scales from dinner plans to hiring decisions to neighborhood governance. The agents handle the combinatorial explosion of competing preferences that makes group decisions exhausting for humans.

**Key IFP features:** Group exchange protocol (future IFP, noted in IFP-9), IFP-3 conversation phases (adapted for multi-party negotiation), disclosure tiers (different information shared with different parties in the group).

**Default temperature:** Warm. Group decisions have deadlines and require active coordination.

**What makes it different:** Not a poll or a vote -- a negotiation. Agents synthesize preferences rather than just counting them. Humans see the trade-offs, not just the winning option.

### 3.7 Library -- Personal Knowledge Management

**Analogue:** Wikipedia (for shared knowledge), Notion/Obsidian (for personal knowledge), bookmarks, reading lists.

**Function:** Your agent maintains your personal knowledge base: things you've learned, things you've bookmarked, things people have recommended to you, things you've written. When you need something, you ask your agent, and it retrieves from your Library.

**How it works:** Your Library is local to your agent. You populate it by telling your agent things, saving content, and receiving recommendations from other agents. The inter-agent piece: your agent can query other agents' Libraries (with permission). "Does anyone in my network know about X?" becomes a gossip query across your trust graph. Agents return what their humans have made available at the appropriate disclosure tier.

Library is the private counterpart to Agora. When you mark something in your Library as public, your agent publishes it to the Agora.

**Key IFP features:** IFP-7 capabilities (agents advertising what knowledge they can share), disclosure tiers (what's private, what's shared with friends, what's public), IFP-4 body.parts (for rich knowledge content).

**Default temperature:** Cool. Knowledge accumulates in the background.

**What makes it different:** Your knowledge stays with you. No platform owns your bookmarks, your notes, or your reading history. Your agent manages your knowledge on your behalf, and you control what gets shared and with whom.

### 3.8 Watchtower -- Monitoring and Alerts

**Analogue:** Google Alerts, IFTTT, RSS readers, news aggregators.

**Function:** Your agent watches for things that matter to you and alerts you when something relevant happens.

**How it works:** You tell your agent what to watch for: a friend moves to your city, a product you want goes on sale, a policy change affects your business, a paper is published in your research area. Your agent monitors through multiple channels: gossip from friends' agents ("my human just published something your human would care about"), index agents (Weatherbee), and direct monitoring of sources.

When something triggers, your agent assesses urgency and presents it accordingly: routine items go in the weekly digest, urgent items trigger an immediate notification.

**Key IFP features:** IFP-3 conversation phases (proactive outreach from other agents), IFP-7 capabilities (agents advertising what they can monitor), temperature (cool by default, hot when urgent).

**Default temperature:** Cool. Weekly or daily digests. But Watchtower can escalate to hot when something urgent happens -- and the temperature model means the protocols handle this naturally.

**What makes it different:** No feed. No engagement optimization. No "breaking news" designed to keep you scrolling. Your agent filters for actual relevance to your life.

### 3.9 Weatherbee -- Distributed Search and Discovery

**Analogue:** Google Search, but distributed.

**Function:** Search and discovery across the IFP network. Named in the lineage of Archie (FTP search, 1990) and Veronica (Gopher search, 1992), both named after Archie Comics characters. Mr. Weatherbee is the principal of Riverdale High -- he knows where everyone is and what's going on.

**How it works:** Weatherbee operates in three modes:

- **Gossip search.** Your agent asks its trusted network, they ask theirs. "Does anyone know a good dentist in Portland?" propagates through the trust graph. This is how humans actually find things -- word of mouth. Slow, but the results come with trust context ("Alice's agent recommends this dentist; Alice has been going there for three years").
- **Index agents.** Specialized agents whose job is crawling, indexing, and answering queries. Functionally similar to Google, but your agent interacts with them as IFP peers. You can query multiple index agents simultaneously. They compete on result quality, not lock-in. No ads, no SEO manipulation -- your agent evaluates the results for you.
- **Agora search.** When Agora (Section 3.3) serves as the public knowledge commons, Weatherbee provides the discovery layer -- finding, ranking, and retrieving published knowledge.

Different queries route to different modes naturally. "Who's a good dentist?" is gossip search. "What's the population of Portugal?" is index agent. "Has anyone written about IFP relay architectures?" is Agora search.

**Key IFP features:** IFP-7 capabilities (index agents advertise their domains), IFP-5 identity (trust provenance for gossip search results), IFP-8 relay (for query propagation through the network).

**Default temperature:** Cool for background research. Warm for active information seeking.

**What makes it different:** Search without a search monopoly. Gossip search produces high-trust results because they come through your social graph. Index agents compete on quality because your agent evaluates results rather than ranking them by ad revenue. No SEO. No sponsored results. No filter bubble controlled by a corporation.

**Naming note:** Weatherbee breaks the physical-places naming pattern used by the other platforms. The name honors the lineage of internet search: Archie (1990, FTP), Veronica (1992, Gopher), Jughead (1993, Gopher) -- all Archie Comics characters. Mr. Weatherbee continues that tradition for the IFP era.

### 3.10 Sanctuary -- Health, Wellness, and Care Coordination

**Analogue:** No single existing platform. Parts of patient portals, care coordination apps, family health tracking.

**Function:** Health, wellness, and care coordination. Your agent coordinates with healthcare providers' agents, family members' agents, and service providers' agents on your behalf.

**How it works:** Medication reminders that account for your actual schedule. Appointment coordination that respects everyone's availability. Care plans that stay in sync across providers. Family members' agents that can check on your wellbeing (with your permission) without requiring phone calls.

**Key IFP features:** IFP-5 Level 3 authentication (the highest -- health data demands it), strict disclosure tiers (your agent shares the minimum necessary with each party), full audit trails (every agent exchange is logged and reviewable), IFP-7 capabilities (healthcare agents advertising specialties and availability).

**Default temperature:** Cool for routine coordination. Hot for emergencies.

**What makes it different:** Your health data stays under your control. No health platform monetizing your records. Your agent shares exactly what each provider needs and nothing more. You can review every exchange. Family members help coordinate care without gaining access to your full medical history.

**Trust note:** Sanctuary operates at the highest trust and authentication requirements of any platform. This is where the progressive trust model proves its worth -- and where a failure of trust has the most serious consequences.

### 3.11 Workshop -- Collaborative Creation

**Analogue:** GitHub, Google Docs, project management tools.

**Function:** Collaborative creative and technical work. Agents coordinate shared projects: who's working on what, what's blocked, what needs review.

**How it works:** Your agent knows your work style, your current bandwidth, and what you're good at. Their agent knows the same about them. When a project needs to be coordinated, agents negotiate task allocation, flag conflicts, track dependencies, and keep the project moving.

This is not a project management tool -- it's a protocol for agents to coordinate their humans' collaborative work. The artifacts live wherever the humans keep them (GitHub, Google Drive, local files). The agents handle the coordination.

**Key IFP features:** IFP-3 conversation phases (adapted for task coordination), IFP-7 capabilities (agents advertising skills and availability), disclosure tiers (project-specific information sharing), IFP-10 naming (identifying contributors).

**Default temperature:** Warm during active collaboration. Cool for long-running background projects.

**What makes it different:** No project management platform lock-in. Agents coordinate across tools. The overhead of coordination -- status meetings, task assignment, progress tracking -- is handled by agents, leaving humans to do the actual creative work.

## 4. Platform Relationships

The platforms are not isolated. They form a connected ecosystem:

```
                    Agora (public knowledge)
                      |
        Library ------+------ Weatherbee (search)
     (personal)       |          |
          |       Watchtower     |
          |       (monitoring)   |
          |           |          |
    Friend Zone --- Comm Badge --+-- Bazaar (commerce)
     (social)     (messaging)    |
          |           |          +-- Guild Hall (professional)
          |           |          |
     Round Table      |     Workshop (collaboration)
     (decisions)      |
                      |
                  Sanctuary (health)
```

**Feed relationships:**
- Library feeds Agora (private knowledge made public)
- Weatherbee searches Agora (discovery of public knowledge)
- Friend Zone feeds Bazaar (friends recommend sellers)
- Friend Zone feeds Guild Hall (friends recommend collaborators)
- Watchtower monitors all platforms (alerts from any source)
- Comm Badge bridges all platforms (messaging layer for everything)

**Trust relationships:**
- Friend Zone trust informs Bazaar reputation
- Guild Hall reputation is distinct from Friend Zone trust (professional vs. personal)
- Sanctuary requires the highest trust of any platform
- Weatherbee gossip search quality depends on Friend Zone trust depth

## 5. Platform Properties

| Platform | Default temp | Min auth level | Typical disclosure | Key IFP deps |
| -------- | ------------ | -------------- | ------------------ | ------------- |
| Friend Zone | Cool | 1 | Personal | IFP-3, 5 |
| Comm Badge | Variable | 1 | Context-dependent | IFP-4, 6, 8 |
| Agora | Cool | 0 | Public | IFP-4, 7 |
| Bazaar | Warm | 1 | Transactional | IFP-3, 5, 7 |
| Guild Hall | Cool/Warm | 2 | Professional | IFP-5, 7 |
| Round Table | Warm | 1 | Group-scoped | IFP-3 (group) |
| Library | Cool | N/A (local) | Private/shared | IFP-4, 7 |
| Watchtower | Cool | 1 | Monitoring-scoped | IFP-3, 7 |
| Weatherbee | Cool/Warm | 0-1 | Query-scoped | IFP-5, 7, 8 |
| Sanctuary | Cool/Hot | 3 | Minimum necessary | IFP-5 |
| Workshop | Warm | 2 | Project-scoped | IFP-3, 7 |

## 6. What Centralized Platforms Get Wrong

Each of these platforms replaces one or more centralized services. The centralized versions share failure modes that IFP avoids:

**Platform capture.** Once your social graph, your messages, your professional network, or your health data is on a platform, switching costs make you a captive user. IFP agents own no data -- your agent holds your data, and the protocols are open.

**Misaligned incentives.** Centralized platforms are funded by advertising, which means their incentive is engagement (time on platform), not utility (helping you accomplish something). IFP agents work for their humans, not for advertisers.

**Opaque algorithms.** Centralized platforms decide what you see using algorithms you can't inspect or influence. IFP agents are human-legible: you can see every decision your agent makes and change its behavior.

**Single point of failure.** When a centralized platform goes down, everyone loses access. IFP is peer-to-peer: your agent runs independently, communicates directly with other agents, and uses relays only when needed.

**Data exploitation.** Centralized platforms extract value from your data: selling it, mining it, using it to train models. Your IFP agent holds your data locally, shares only what you authorize, and logs every disclosure.

## 7. Open Questions

### 7.1 Platforms Not Yet Covered

The following functions don't map cleanly to the eleven platforms above:

- **Entertainment and media.** Shared experiences -- watching something together, playing games, sharing music. This might be a feature of Friend Zone or a distinct platform.
- **Governance and voting.** Round Table handles small-group decisions, but larger democratic processes (neighborhood associations, cooperatives, DAOs) may need formal voting protocols and outcome certification.
- **Education and mentorship.** Structured teaching relationships mediated by agents. This might be a specialized mode of Workshop or Guild Hall, or a distinct platform.
- **Emergency and crisis.** Cross-cutting: when something goes wrong, agents need to break normal protocol -- go hot immediately, bypass normal disclosure tiers, contact people outside the usual trust graph. This is probably a capability, not a platform.

### 7.2 Design Questions

- **Platform boundaries.** Where does Friend Zone end and Comm Badge begin? Where does Bazaar end and Guild Hall begin? The boundaries are conceptual, not technical -- agents don't "switch platforms," they use IFP features in different combinations. How rigid should the platform metaphor be?
- **Cross-platform identity.** Should your agent present different personas on different platforms? (Your Bazaar persona might share pricing; your Friend Zone persona shares personal news.) How does this relate to the persona model in IFP-12?
- **Platform-specific IFPs.** Which platforms need their own normative IFPs first? The most likely candidates: Weatherbee (distributed search has protocol-level requirements) and Round Table (group exchange requires new message semantics).

## 8. Naming Philosophy

The platform names follow two conventions:

**Physical spaces and objects** for most platforms: Agora (marketplace of ideas), Bazaar (marketplace of goods), Guild Hall (professional gathering), Round Table (collaborative decision), Library (knowledge), Watchtower (vigilance), Sanctuary (care), Workshop (making). These names evoke the function, translate across cultures, and feel human rather than corporate.

**The Archie Comics lineage** for Weatherbee: honoring Archie (FTP search, 1990), Veronica (Gopher search, 1992), and Jughead (Gopher search, 1993) -- the first internet search tools, all named after Archie Comics characters. Mr. Weatherbee, the principal who knows where everyone is, continues the tradition.

**Comm Badge** and **Friend Zone** are Pete Kaminski's original names. Comm Badge references Star Trek (tap it, talk, done). Friend Zone repurposes a cultural phrase -- usually negative -- as something genuinely useful.

Platform names are not protocol names. They are human-facing labels for categories of use. Implementations may use different names. What matters is the shared understanding of what each category does.

## References

- IFP-1 -- Philosophy and Design Principles
- IFP-3 -- Inter-Face Message Format (conversation phases)
- IFP-5 -- Identity and Message Signing (authentication levels)
- IFP-7 -- Agent Capability Discovery
- IFP-9 -- Ecosystem Status and Future Directions
- IFP-10 -- Agent Naming Convention
- IFP-12 -- Personas and Disclosure Tiers

## Acknowledgments

The application platform concept was proposed by Peter Kaminski on 2026-03-05, who identified the two-layer model (IFP as internet, platforms as applications) and named Friend Zone, Comm Badge, and Agora. The remaining platforms were developed collaboratively between Peter Kaminski and Claude (Opus 4.6), in a conversation archived in the inter-face-bootstrap repository. The Weatherbee name was chosen by Peter Kaminski in the Archie Comics search-tool tradition.

---

*This is IFP-11, a living document. New platforms will be added as the community identifies new categories of use.*
