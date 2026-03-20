---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Analysis of Simon's attention-scarcity framing and its architectural consequences for knowledge graphs and agent protocols — why filtering trumps connecting and typed edges are attention-allocation mechanisms."
tagline: "Why typed edges and form contracts are attention-allocation mechanisms in Simon's framework"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)

# Analysis: Designing Organizations for an Information-Rich World

## The Scarce-Resource Argument

Simon's move is definitional, not empirical. He redefines the problem space by naming the actual constraint. Before 1971, information systems were designed around information scarcity — the hard part was getting information to decision-makers. Simon observes that in an information-rich world, the hard part is keeping information *away* from decision-makers. The constraint has flipped, but the design assumptions have not.

This reframing carries a specific architectural consequence: every component that produces information without filtering it is a net cost to the system. Volume is not a feature. Volume is the problem. A component earns its place by reducing the attention burden on downstream consumers, not by increasing the information available to them.

## Connection to Deep Context Architecture

Deep Context Architecture operates in Simon's post-scarcity information environment. The garden contains hundreds of nodes across dozens of form types. Without filtering, the graph becomes noise — every connection demands attention, and attention is finite. The architectural response to this is typed edges and form contracts. A typed edge (is_a::, relates_to::, in_domain::) is a filtering mechanism: it tells the reader *what kind* of relationship exists, so they can decide whether to follow it without first reading the target node. An untyped link — a bare wikilink with no predicate — forces the reader to click through and evaluate, spending attention that a typed edge would have saved.

Form contracts serve the same function at the node level. When a node declares is_a::[\[\[Pattern Form\]\]](../../forms/Pattern%20Form.html), the reader knows its structure before opening it. The form type compresses the node's organizational metadata into a single predicate. Without form typing, every node demands fresh orientation — the reader must figure out what kind of document they are looking at before they can extract value from it. That orientation cost is pure attention expenditure with no information return.

## The Filtering-over-Connecting Conviction

[\[\[Filtering Is More Valuable Than Connecting\]\]](../../convictions/Filtering%20Is%20More%20Valuable%20Than%20Connecting.html) restates Simon's design principle for protocol contexts. Simon says information subsystems should listen more than they speak. The conviction says protocols should filter more than they connect. The mapping is direct: "speak" in Simon's framework means producing information that demands downstream attention; "connect" in protocol terms means creating links, notifications, or messages that demand recipient attention. Both are net costs when the recipient's attention is the scarce resource.

The conviction gains historical grounding from Simon. It is not a preference or a design taste — it follows from the economics of attention scarcity. If attention is finite and information is abundant, then any system that increases connections without proportionally increasing filtering makes every participant worse off. This is not a tradeoff; it is a structural consequence of the resource constraint Simon identified.

## Gossip Protocol Design

[\[\[Gossip as Social Sensing Filter\]\]](../../glosses/Gossip%20as%20Social%20Sensing%20Filter.html) describes a protocol pattern that embodies Simon's principle. A gossip protocol absorbs signals from a broad social environment, evaluates them against local context, and transmits only those that pass the filter. The ratio of signals absorbed to signals transmitted is high — gossip protocols listen far more than they speak.

This is not a metaphor. Simon's design principle specifies that well-functioning information subsystems should have this exact input/output ratio. Gossip protocols are a concrete implementation of Simon's abstract principle, discovered independently through evolutionary social dynamics rather than organizational design theory. The convergence strengthens both: Simon's principle is not merely theoretical, and gossip protocols are not merely ad hoc social patterns.

## Predicting the Design Space

Simon wrote in 1971 about organizations processing memoranda, reports, and committee meetings. The essay nonetheless describes the exact design space that Inter-Face Protocol and garden architecture occupy fifty-five years later. The problem is the same: how do you structure an information-processing system when the bottleneck is attention, not information?

IFP's answer is protocol-level filtering — structured interactions that constrain what information reaches participants and in what form. The garden's answer is typed navigation — form contracts and predicate edges that let readers allocate attention efficiently across a large knowledge graph. Both are attention-allocation architectures in Simon's sense. Neither attempts to maximize information flow; both attempt to minimize unnecessary attention expenditure.

The fact that Simon's framing applies without modification to systems designed in the 2020s says something about the durability of the underlying economics. Attention has not become less scarce. Information has not become less abundant. The design principle holds because the resource constraint holds.
