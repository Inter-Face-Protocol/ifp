---
created: 2026-03-18
part_of: "[\[\[Ehmke (2023) Dimensions of Digital Coercion\]\]](Ehmke%20%282023%29%20Dimensions%20of%20Digital%20Coercion.html)"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Analysis: Dimensions of Digital Coercion

## Core Thesis

Ehmke presents digital coercion as "the manifestation of mechanisms of control in online environments" — compelling people to act contrary to their own needs through threats of harm facilitated at internet scale. The report's central argument is that coercion operates systematically across both commercial and open-source platforms through four interconnected dimensions, and that openness alone does not produce equitable outcomes.

This is an internal critique from a movement insider. Ehmke created the Contributor Covenant, the most widely adopted code of conduct in open source. The critique carries weight because it comes from someone who built one of the normative standards she now identifies as insufficient.

## Framework: Four Dimensions

### Attention Coercion

Demanding more time or cognitive load than users would voluntarily consent to.

**Commercial mechanisms**: Dark patterns (popups, screen takeovers, survey bombardment), push notifications enabled by default, engagement maximization through manufactured conflict and radicalization tactics. Impact: hypervigilance, cognitive exhaustion, addiction, erosion of free time.

**Open-source mechanisms**: Ongoing maintenance burdens (manual updates, security patches, dependency management), documentation gaps with "RTFM" culture, requirement that users become system administrators for basic functionality. Impact: digital gatekeeping excluding the majority of potential adopters.

### Ergonomic Coercion

Forcing users to trade autonomy, safety, privacy, time, or effort for usability.

**Commercial mechanisms**: Ergonomic paywalls (disabled copy-paste, gated accessibility features), forced continuity (silent charges after "free trials" with complex cancellation), user-hostile opt-out design (low-contrast text, guilt-inducing pages, phone-only cancellation during business hours).

**Open-source mechanisms**: Platform agnosticism sacrificing native UI components, OS keyboard shortcuts, and spell-checking. OS accessibility frameworks must be independently reproduced and are often simply not implemented. Terminal-only installation and configuration.

### Trust Coercion

Demanding assumption of benign intentions without accountability for trustworthiness.

**Commercial mechanisms**: Transactional trust models claiming "community" while refusing to prioritize safety. Friend spam exploiting personal networks. Opacity: users see what providers say, not what they do.

**Open-source mechanisms**: Merit-based trust enabling successful disinformation from long-time editors (Wikipedia case). Safety barriers preventing marginalized contributors from participating (Black Lives Matter archive example). Code of conduct presence normalized to the point where it no longer signals actual inclusivity.

### Cultural Coercion

Imposing white and Western norms and values as participation prerequisites.

**Commercial mechanisms**: Herbert Schiller's 1976 prediction realized — a handful of US tech corporations shape global cultural life. Algorithmic oppression (Noble's research on Google's sexualization of Black girls in search results). Selective moderation that punishes marginalized communities defending themselves.

**Open-source mechanisms**: Meritocracy assuming level playing fields. Technology neutrality dogma ("Freedom Zero" enshrining unrestricted use). Geographic concentration (7.4% from San Francisco Bay Area). Language barriers (only 17% speak English natively, yet most programming languages originate in English-speaking nations).

## Three Challenged Tenets

The report challenges three core assumptions of traditional open-source philosophy:

1. **Meritocracy is equitable** — It sustains inequity by assuming a level playing field and defining "merit" in the image of the dominant in-group.

2. **Technology is neutral** — Technology is only neutral toward its creators and only to the degree it preserves the dominant culture's social order.

3. **Open access is an unqualified good** — Unrestricted access favors those with the most free time, lowest family responsibilities, and proximity to English-speaking technology hubs.

## Standards as Accountability Technology

The report's constructive argument: without accountability, no trust. Without trust, no consent. Without agency for informed choices, no defense against coercion. Standards operating across four layers provide accountability:

| Layer | Function | Example |
|-------|----------|---------|
| Regulatory | Basic rights and responsibilities | GDPR |
| Technical | Interoperability across implementations | Unicode |
| Normative | Behavioral and social expectations | Contributor Covenant |
| Ethical | What is morally acceptable in context | Ethical Source Principles |

The accessibility example demonstrates how a single ideal manifests across all four layers: Berners-Lee's ethical declaration → Mastodon alt-text norms → W3C standards → UN Convention Article 9.

## Scholarly Foundations

The report draws on established critical theory:
- **Safiya Umoja Noble** (2018) — algorithmic oppression in search engines
- **Herbert Schiller** (1976) — cultural imperialism prediction now realized through tech corporations
- **Leilia Green** (1999) — technological advancement shaped by those with most power
- **Stanford disinformation research** (2016) — successful Wikipedia hoaxes from long-time editors

## Limitations

The report is diagnostic rather than prescriptive — it identifies coercion patterns without detailing specific solutions beyond the general direction of multi-layered standards. It does not address economic alternatives for sustainable platform development, transition pathways from coercive to accountable systems, or Global South perspectives (while criticizing Western dominance, it primarily cites Western academic sources).

## Significance for Identity Systems

For Self-Sovereign Identity and verifiable credential design, the framework exposes a critical blind spot: decentralization and open source do not inherently prevent coercion. If decentralized systems require technical sophistication, ongoing maintenance, and steep learning curves without accessible support, they create attention and ergonomic coercion that excludes most potential users — leaving them subject to centralized platform coercion. The result: decentralized systems used only by a privileged technical elite.
