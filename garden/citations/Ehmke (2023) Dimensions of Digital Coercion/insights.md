---
created: 2026-03-18
part_of: "[\[\[Ehmke (2023) Dimensions of Digital Coercion\]\]](Ehmke%20%282023%29%20Dimensions%20of%20Digital%20Coercion.html)"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Insights: Dimensions of Digital Coercion

## Trust Coercion and Contextual Integrity

Ehmke's trust coercion dimension intersects directly with Nissenbaum's contextual integrity framework. Platforms demand assumption of benign intentions without accountability, creating contexts where appropriate information flow norms are systematically violated. The mechanism: platforms claim "community" context (implying certain trust norms) while actually operating in a "surveillance marketplace" context (with radically different norms). Users cannot maintain contextual integrity when platforms deliberately misrepresent the operative context.

Addressing trust coercion requires transparency not just about data practices but about the actual social context a platform creates. Nissenbaum provides the analytical tools; Ehmke identifies the coercive mechanisms that prevent users from applying them.

## Self-Sovereign Identity Must Design Against All Four Dimensions

The principal-agent reversal that Self-Sovereign Identity proposes — individuals as principals granting limited agency to service providers — addresses ergonomic and trust coercion directly. But the framework reveals that two dimensions receive less attention in Self-Sovereign Identity discourse:

**Attention coercion**: Identity operations should complete without ongoing vigilance. Credential lifecycle management should not require manual intervention. Calm technology principles apply — notify only when user action is genuinely required.

**Cultural coercion**: Identity systems must support diverse cultural practices around identity (collective identities, contextual identities, varied name practices), linguistic diversity (non-Latin scripts, right-to-left languages), and governance diversity (not just Western corporate/foundation governance).

Decentralization alone does not address these dimensions. "Not your keys, not your crypto" creates attention coercion when applied to identity. Platform-agnostic design that breaks accessibility creates ergonomic coercion. English-dominated governance spaces create cultural coercion. The Self-Sovereign Identity community must explicitly design against all four dimensions, not just the two that cryptographic verification addresses.

## The Decentralization Trap

Standard narrative: decentralization provides autonomy, resists centralized coercion. Ehmke's complication: if decentralization requires technical sophistication, ongoing maintenance, steep learning curves, and lacks accessible support, it creates attention and ergonomic coercion that excludes most potential users.

Result: decentralized systems used only by a privileged technical elite, while everyone else remains subject to centralized platform coercion.

Possible approaches that do not recreate this pattern:
- **Trusted intermediaries with exit rights**: Services that simplify usage but do not lock users in (email model)
- **Cooperative infrastructure**: Collective ownership reduces individual maintenance burden
- **Progressive decentralization**: Start with usable centralized service, gradually enable user control as sophistication increases

## Collective Rights Beyond Individual Consent

"Digital rights are not individual concerns that can be addressed by individual choices." This directly challenges Self-Sovereign Identity's emphasis on individual sovereignty. Individual "choice" to participate is meaningless when opting out means unemployment, loss of services, or social exclusion. Network effects mean individual privacy choices affect others (sharing contacts reveals social graphs).

Self-Sovereign Identity may need complementary collective-sovereign identity frameworks that enable groups to exercise collective agency over shared identity contexts. Individual consent is necessary but insufficient; collective governance of shared contexts is the missing layer.

## Standards as Practical Accountability

The multi-layered standards model provides a practical framework for identity system accountability:

| Layer | Identity Application |
|-------|---------------------|
| Ethical | Everyone deserves self-sovereign identity regardless of technical sophistication, wealth, or ability |
| Normative | Community expectations about acceptable surveillance, data minimization, consent practices |
| Technical | Protocols enabling diverse implementations without constraining them |
| Regulatory | Legal recognition of cryptographic credentials, prohibition of coercive practices |

Each layer reinforces the others. Without the ethical layer, technical standards optimize for interoperability without purpose. Without technical standards, ethical principles remain aspirational. Without regulatory backing, normative expectations have no enforcement mechanism.

## Cross-Boundary Analysis as Method

The report's most transferable methodological contribution is applying the same analytical framework to both commercial and open-source platforms. This cross-boundary analysis prevents the common error of treating openness as inherently virtuous. The same approach applies to identity systems: analyzing both centralized and decentralized identity solutions with the same coercion framework prevents premature celebration of any single architectural choice.

## Dynamic Systems Warning

Coercive systems continually adapt and outpace mitigation efforts. Static solutions (a single regulation, a fixed technical standard, a one-time audit) are insufficient. This suggests that identity system governance must include ongoing coercion auditing — not a one-time design review but continuous evaluation as systems evolve and market pressures shift.
