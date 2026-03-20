---
created: 2026-03-19
author: Christopher Allen
publication_year: 2004
canonical: "https://digitalcommons.law.uw.edu/wlr/vol79/iss1/10/"
brief_summary: "Nissenbaum reframes privacy as contextual integrity — appropriate information flows governed by context-specific norms rather than secrecy or individual control. Five parameters define any flow: data subject, sender, recipient, information type, and transmission principle. Privacy violations occur when flows breach the norms governing a particular social context, not when information becomes visible."
tagline: "Privacy means appropriate information flow within context-specific norms, not secrecy or control"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)
- in_domain::[\[\[Self-Sovereign Identity\]\]](../../domains/Self-Sovereign%20Identity.html)
- cites_work_by::[\[\[Helen Nissenbaum\]\]↑](../../NODES.html#:~:text=Helen%20Nissenbaum)

# Nissenbaum (2004) Privacy as Contextual Integrity

## Bibliographic Entry

* _**Privacy as Contextual Integrity**_ (2004). [journal article]. _Nissenbaum, Helen._ Washington Law Review, Vol. 79, No. 1, pp. 119-157, 2004. Retrieved from: <https://digitalcommons.law.uw.edu/wlr/vol79/iss1/10/>

## Summary

Nissenbaum argues that dominant privacy theories — privacy as secrecy, privacy as control over personal information, privacy as limited access — fail to account for why surveillance in public spaces feels like a privacy violation. People walking down a street have no reasonable expectation of secrecy, yet pervasive CCTV monitoring strikes most people as a privacy intrusion. These frameworks cannot explain the gap.

Drawing from Michael Walzer's "spheres of justice," Nissenbaum proposes that privacy is maintained when information flows conform to the norms appropriate to a given social context. Every social domain — healthcare, education, friendship, commerce — has its own informational norms governing what information is appropriate to share, with whom, and under what conditions.

## Key Points

**Five parameters of information flow**: Any information flow is described by five parameters: (1) data subject — who the information concerns, (2) sender — who transmits it, (3) recipient — who receives it, (4) information type — what kind of information it is, and (5) transmission principle — the terms under which the flow occurs (consent, legal requirement, purchase, reciprocity).

**Two classes of norms**: Norms of appropriateness govern which information types belong in which contexts. Medical details are appropriate in a doctor's office but not at a dinner party. Norms of distribution govern onward flow — a doctor may know a patient's condition but confidentiality norms restrict further sharing.

**Privacy violations as norm breaches**: A practice violates privacy when it breaches either appropriateness norms (wrong information type for the context) or distribution norms (wrong transmission principle for the flow). Aggregating individually public data points can violate privacy because aggregation changes the effective information type and transmission principle.

**Public surveillance**: Systematic surveillance violates contextual integrity because it transforms the transmission principle from incidental observation to systematic collection and aggregation. The underlying information (presence in a public space) is technically observable, but the collection regime changes the context.

**Walzer's spheres applied to information**: Just as Walzer argued that goods appropriate in one sphere of justice (money in markets) should not dominate another sphere (political office), Nissenbaum argues that information appropriate in one social context should not flow unconstrained into another.

## Key Quotes

> Privacy is maintained when information flows conform to the norms appropriate to a given social context.

## Influence

Contextual integrity became the dominant philosophical framework for information privacy after publication. The framework reframes privacy from a property of information (secret vs. public) to a property of information flows (appropriate vs. inappropriate for context). This reframing directly supports disclosure tier design in Self-Sovereign Identity systems: each disclosure tier defines a context with its own norms of appropriateness and distribution, and privacy violations occur when information crosses tier boundaries without conforming to the destination context's norms.

## Sources

**Primary**: <https://digitalcommons.law.uw.edu/wlr/vol79/iss1/10/> (Washington Law Review)

**Related patch citations**:
- [\[\[Ehmke (2023) Dimensions of Digital Coercion\]\]](../Ehmke%20%282023%29%20Dimensions%20of%20Digital%20Coercion/Ehmke%20%282023%29%20Dimensions%20of%20Digital%20Coercion.html) — Trust coercion dimension directly intersects contextual integrity: platforms misrepresent the operative social context

## Relations

- relates_to::[\[\[Self-Sovereign Identity\]\]](../../domains/Self-Sovereign%20Identity.html)
  Contextual integrity provides the philosophical foundation for why identity systems must support selective disclosure — each context has its own norms governing appropriate information flow.

- relates_to::[\[\[Progressive Trust\]\]↑](../../NODES.html#:~:text=Progressive%20Trust)
  Progressive trust builds disclosure tiers that map to social contexts. Contextual integrity explains why those tiers matter: crossing them without norm compliance is a privacy violation regardless of whether the information was "secret."
