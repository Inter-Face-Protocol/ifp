---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Analysis of how Christopher Allen's progressive trust framework maps to IFP's authentication levels and disclosure tiers — where IFP faithfully operationalizes the framework, where it departs, and where the gaps are."
tagline: "How faithfully does IFP operationalize the progressive trust framework?"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Analysis: Progressive Trust Applied to Inter-Face Protocol

Inter-Face Protocol's progressive authentication (IFP-5) and disclosure tiers (IFP-12) are operationalizations of Christopher Allen's progressive trust framework. This analysis examines where the operationalization is faithful, where it departs, and where gaps remain.

## Where IFP Faithfully Operationalizes Progressive Trust

**Authentication deepens with relationship.** IFP-5's four levels (shared secret → signed → verified → DID-bound) track the progressive trust principle that verification should be proportional to the relationship stage. You do not demand cryptographic proof before saying hello.

**No downgrading.** IFP-5 prohibits authentication downgrade within an exchange, matching the progressive trust principle that trust should not regress without cause.

**Disclosure parallels authentication.** IFP-12's disclosure tiers deepen alongside authentication levels. Narrow disclosure at low trust, broader disclosure at high trust. The two progressions reinforce each other, as the progressive trust framework predicts.

**Temperature tracks engagement depth.** Cool → warm → hot cadence parallels the progressive trust stages from initial contact to active collaboration. Temperature is not explicitly part of the progressive trust framework, but IFP's addition is compatible.

## Where IFP Departs

**Discretization.** The progressive trust framework describes a continuous spectrum. IFP discretizes it into four authentication levels and six disclosure tiers. The framework does not specify how many stages are appropriate — but it does emphasize that the progression is smooth, not stepped. IFP's discrete stages may create artificial cliffs where the original model has gradual slopes.

**Disclosure tier names.** The progressive trust framework does not prescribe specific sharing categories. IFP-12's six tiers (public → close) embed assumptions about relationship types (professional vs personal, community vs individual) that the framework leaves open. The tier names are IFP's addition, not derived from progressive trust.

**Persona-specific disclosure.** The progressive trust framework does not address personas — it describes trust between two parties, not trust across multiple contexts of the same party. IFP-12's persona model extends progressive trust in a direction the framework does not anticipate.

## Gaps

**The Level 0 → 1 cliff.** Progressive trust describes a gradual deepening from initial contact. IFP's jump from shared secret (Level 0) to public-key signatures (Level 1) is a large technical leap that may not match the social experience of gradually building trust. An intermediate stage — verified introduction, or reputation-based bootstrapping — might smooth this transition.

**Mutual but asymmetric trust.** The progressive trust framework focuses on bilateral trust deepening. IFP allows asymmetric authentication and disclosure levels between two parties. The implications of asymmetric trust for progressive trust theory are unexplored.

**Trust regression.** Progressive trust says trust should not regress without cause. IFP prohibits authentication downgrade within an exchange, but says nothing about between-exchange regression. Can a relationship that reached Level 2 drop back to Level 1 across exchanges? The progressive trust framework would say yes — trust can be lost — but IFP does not specify the mechanism.

## Sources

- [\[\[Allen (2024) Progressive Trust\]\]](Allen%20%282024%29%20Progressive%20Trust.html) — the source framework
- [IFP-5: Identity and Message Signing](../../ifp-5-identity-signing.md) — authentication operationalization
- [IFP-12: Personas and Disclosure Tiers](../../ifp-12-personas.md) — disclosure operationalization
