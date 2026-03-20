---
created: 2026-03-19
author: Christopher Allen
publication_year: 1971
canonical: "https://gwern.net/doc/design/1971-simon.pdf"
brief_summary: "Simon's 1971 essay argues that information abundance creates attention scarcity. Well-designed information systems should allocate attention efficiently by filtering and compressing — 'listening and thinking more than they speak' — rather than amplifying volume at each stage."
tagline: "A wealth of information creates a poverty of attention — design for filtering, not volume"
---

← [Garden Patch Home](../../README.html) · [Citations](../index.html)


- is_a::[\[\[Citation Form\]\]](../../forms/Citation%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../../domains/Deep%20Context%20Architecture.html)
- cites_work_by::[\[\[Herbert A. Simon\]\]↑](../../NODES.html#:~:text=Herbert%20A.%20Simon)

# Simon (1971) Designing Organizations for an Information-Rich World

## Bibliographic Entry

* _**Designing Organizations for an Information-Rich World**_ (1971). [book chapter]. _Simon, Herbert A._ In Martin Greenberger (Ed.), *Computers, Communications, and the Public Interest*, Johns Hopkins Press, 1971, pp. 38-72. Retrieved from: <https://gwern.net/doc/design/1971-simon.pdf>

## Summary

Simon identifies the binding constraint of information-rich environments: attention, not information, is the scarce resource. "A wealth of information creates a poverty of attention and a need to allocate that attention efficiently among the overabundance of information sources that might consume it." The essay treats organizations as information-processing systems and asks how to structure them when the bottleneck has shifted from information scarcity to attention scarcity.

His central design principle: information subsystems should "listen and think more than they speak." A well-designed component absorbs more information than it produces, filtering and compressing as it goes. Naive designs amplify volume at each stage; effective designs reduce it. The goal is not to produce more information but to ensure the right information reaches the right decision-maker at the right time — and that everything else is filtered away.

## Key Points

**Attention as the scarce resource**: Information is cheap; attention is expensive. Any system that increases information volume without proportionally reducing demands on attention makes the problem worse. This inverts the default assumption that more information means better decisions.

**The listen-more-than-speak principle**: Each subsystem in an information-processing organization should absorb, filter, and compress. Output volume should be smaller than input volume. Components that amplify rather than filter are architectural failures.

**Organizational design implications**: Structuring organizations for information richness means designing attention-allocation mechanisms — not information-distribution mechanisms. The architecture question shifts from "how do we get information to people" to "how do we protect people from information they don't need."

**Anticipation of attention economics**: Written in 1971, the essay predicts the design space that notification systems, feeds, dashboards, and algorithmic timelines now occupy. Simon frames these as attention-allocation problems decades before the technology existed to create them at scale.

## Sources

**Primary**: <https://gwern.net/doc/design/1971-simon.pdf> (book chapter, 35 pages)

## Relations

- relates_to::[\[\[Gossip as Social Sensing Filter\]\]](../../glosses/Gossip%20as%20Social%20Sensing%20Filter.html)
  Simon's listen-more-than-speak principle describes exactly what gossip protocols do: absorb social signals broadly, filter for salience, compress into transmissible form. Gossip is a naturally evolved attention-allocation mechanism.

- relates_to::[\[\[Filtering Is More Valuable Than Connecting\]\]](../../convictions/Filtering%20Is%20More%20Valuable%20Than%20Connecting.html)
  Simon provides the theoretical foundation for this conviction. If attention is the scarce resource, then systems that filter (reduce demands on attention) are more valuable than systems that connect (increase information volume). The conviction restates Simon's 1971 design principle in protocol terms.
