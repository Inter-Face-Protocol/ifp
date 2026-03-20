---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Analysis of Nissenbaum's contextual integrity framework applied to agent-mediated identity protocols — how the five information flow parameters map to protocol design decisions, and why contextual integrity beats privacy-as-secrecy for agent systems."
tagline: "Five information flow parameters as concrete agent protocol design decisions"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Analysis: Privacy as Contextual Integrity

## Core Thesis

Nissenbaum's central move is replacing the question "Is this information private?" with "Does this information flow conform to the norms of this context?" Privacy is not a binary state attached to data. It is a relational property of information flows evaluated against context-specific norms. A medical record is not inherently private — it flows appropriately within a healthcare context and inappropriately when sold to an advertiser. The five parameters (data subject, sender, recipient, information type, transmission principle) describe any information flow completely enough to evaluate its normative status.

This reframing dissolves the classic problem that stalls most privacy-as-secrecy arguments: once information is "out," secrecy frameworks have nothing left to protect. Contextual integrity still has something to say. The information may be known, but flowing it into a new context with different norms is still a violation.

## Five Parameters as Agent Protocol Decisions

Each of Nissenbaum's five parameters maps to a concrete design choice in agent-mediated identity protocols:

**Data subject** maps to the persona or identity graph node under discussion. In a multi-persona system, the same human operates different identity presentations in different contexts. The data subject is not the human — it is the persona active in that context.

**Sender and recipient** map to the (persona, peer) pair in any disclosure event. Each pair defines a context. A credential presented to an employer operates under workplace norms; the same credential presented to a social peer operates under friendship norms. The protocol must track not just what was disclosed but to whom, because the normative evaluation depends on the recipient.

**Information type** maps to claim schemas and credential types. A proof-of-age credential is a different information type than a full birth certificate, even though one derives from the other. Selective disclosure and zero-knowledge proofs exist precisely to control information type — revealing membership in a set ("over 21") without revealing the underlying datum (birth date).

**Transmission principle** maps to the terms of disclosure: consent, legal compulsion, contractual obligation, reciprocity, or delegation. The transmission principle is where Progressive Trust operates — each tier advancement carries an implicit transmission principle that both parties understand. Violating the expected principle (surveilling instead of requesting, purchasing instead of earning through relationship) breaches contextual integrity even if the information type and recipient would otherwise be appropriate.

## Connection to Trust Coercion

[\[\[Ehmke (2023) Dimensions of Digital Coercion\]\]](../Ehmke%20%282023%29%20Dimensions%20of%20Digital%20Coercion/Ehmke%20%282023%29%20Dimensions%20of%20Digital%20Coercion.html)'s trust coercion dimension describes what happens when platforms misrepresent the operative context. A platform claims "community" context (implying norms of reciprocity, mutual care, confidentiality) while operating in a "surveillance marketplace" context (implying norms of extraction, monetization, asymmetric access). Users cannot maintain contextual integrity when the context itself is falsified.

This connects the two citations directly: Nissenbaum provides the analytical framework for identifying norm violations, and Ehmke identifies the coercive mechanism — context misrepresentation — that makes violations systematic rather than incidental. Trust coercion is the industrial-scale production of contextual integrity violations.

## Why Contextual Integrity Beats Privacy-as-Secrecy for Agent Systems

Privacy-as-secrecy forces a binary: either information is hidden or it is exposed. Agent systems that operate on this model can only lock down or open up. They have no vocabulary for "appropriate sharing."

Contextual integrity provides that vocabulary. An agent operating on contextual integrity principles can evaluate a disclosure request against: Is this the right context? Is the recipient appropriate? Is the information type granular enough? Is the transmission principle what the principal expects? These are the questions that selective disclosure protocols, verifiable presentations, and trust negotiation actually answer — but without Nissenbaum's framework, they lack the philosophical grounding that explains why these distinctions matter.

The practical consequence: systems designed around contextual integrity produce disclosure policies that humans recognize as matching their intuitions about appropriate sharing. Systems designed around secrecy produce policies that feel either paranoid (refuse everything) or reckless (share everything once any barrier is crossed). The five-parameter model occupies the space between those extremes where actual human privacy expectations live.
