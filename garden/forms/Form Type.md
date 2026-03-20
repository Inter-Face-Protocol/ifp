---
created: 2026-03-06
author: Christopher Allen
brief_summary: "A form type is a knowledge object category with a known internal structure — a contract about what sections it contains and what question it answers. 17 form types are defined across five categories (Orientation, Structural, Action, Generative, Governance)."
tagline: "The structural contract that defines what shape a knowledge object takes"
---

← [Garden Patch Home](../) · [Form Definitions](index.html)


- is_a::[\[\[Form Type\]\]](Form%20Type.html)
- has_status::[\[\[Seed Stage\]\]](Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)
- in_precinct::[\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html)
- in_precinct::[\[\[Vault Precinct\]\]](../glosses/Vault%20Precinct.html)

# Form Type

A form type is a knowledge object category with a known internal structure — a contract about its shape. Each form type answers a distinct question and serves a distinct purpose.

Form types belong to five categories:

### Orientation Forms

*What matters? What do we believe?*

| Form Type | Core Question |
|-----------|---------------|
| [\[\[Conviction Form\]\]](Conviction%20Form.html) | What do we believe is true about the world? |
| [\[\[Value Form\]\]](Value%20Form.html) | What do we care about? |
| [\[\[Principle Form\]\]](Principle%20Form.html) | What must we always or never do? |

### Structural Forms

*How do things relate? What do we understand?*

| Form Type | Core Question |
|-----------|---------------|
| [\[\[Model Form\]\]](Model%20Form.html) | How do these elements relate to each other? |
| [\[\[Reference Form\]\]↑](../NODES.html#:~:text=Reference%20Form) | What do I need to know about this domain to act effectively? |
| [\[\[Gloss Form\]\]](Gloss%20Form.html) | What does this specific source or concept mean? |
| [\[\[Citation Form\]\]](Citation%20Form.html) | What do I need to know about this source? |
| [\[\[Opus Form\]\]](Opus%20Form.html) | What am I saying here, and how does it connect? |
| [\[\[Domain Form\]\]](Domain%20Form.html) | What knowledge area does this cluster of forms belong to? |

### Action Forms

*What to do? What happened?*

| Form Type | Core Question |
|-----------|---------------|
| [\[\[Pattern Form\]\]](Pattern%20Form.html) | What resolves this recurring tension? |
| [\[\[Case Form\]\]↑](../NODES.html#:~:text=Case%20Form) | What happened when this was tried? |
| [\[\[Decision Form\]\]](Decision%20Form.html) | Why did we choose this over the alternatives? |
| [\[\[Protocol Form\]\]↑](../NODES.html#:~:text=Protocol%20Form) | How do independent parties coordinate reliably? |
| [\[\[Skill Form\]\]↑](../NODES.html#:~:text=Skill%20Form) | How does an agent execute this reliably? |

### Generative Forms

*What should we investigate? What might happen?*

| Form Type | Core Question |
|-----------|---------------|
| [\[\[Inquiry Form\]\]](Inquiry%20Form.html) | What should we think about X, and how would we find out? |
| [\[\[Scenario Form\]\]↑](../NODES.html#:~:text=Scenario%20Form) | What might happen if these forces play out? |

### Governance Forms

*Who decides? How do rules change?*

| Form Type | Core Question |
|-----------|---------------|
| [\[\[Boundary Form\]\]](Boundary%20Form.html) | Where does this system's authority end? |

All 17 form types have definition pages. 14 types have instantiated nodes in the garden; 3 types (Protocol, Skill, Scenario) have definition pages but no content nodes yet. Opus Form is new (2026-03-15) and awaits its first exemplar.

## Garden Nodes and Vault Nodes

Form types serve two precincts within the deep context architecture. [\[\[Garden Precinct\]\]](../glosses/Garden%20Precinct.html) nodes (the 16 types above) carry structural contracts — required sections, specific shapes, enforceable constraints. [\[\[Vault Precinct\]\]](../glosses/Vault%20Precinct.html) nodes (Meeting Note, Transcript, Person Note, Chat Log, Sidecar) are operational templates with conventions but lighter structural requirements. Both precincts use `is_a::` predicates, typed edges, and the same graph infrastructure. Some form types (Status Stages, Domain Form) serve both precincts.

The two precincts solve different problems — the garden curates durable knowledge, the vault captures operational information — rather than representing different maturity levels of the same thing.

## Sources

Taxonomy from [\[\[Deep Context as an Architecture for Captured Reasoning\]\]](../decisions/Deep%20Context%20as%20an%20Architecture%20for%20Captured%20Reasoning.html), "The Forms" section.

## Relations

- relates_to::[\[\[Seed Stage\]\]](Seed%20Stage.html) — all nodes start at seed stage
- relates_to::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html) — the domain that defines the type system
