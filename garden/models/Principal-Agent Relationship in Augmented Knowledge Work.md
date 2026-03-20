---
created: 2026-03-05
author: Christopher Allen
brief_summary: "Model mapping BCR-2026-xxx principal authority terminology to the vault's augmented knowledge system. The vault owner is the principal, Claude Code sessions are agents, rules and skills are conferrals, and the three conditions for meaningful authority (legibility, boundaries, override) are satisfied through session logs, process constraints, and human approval gates."
tagline: "How principal authority maps to vault owner, Claude sessions, rules, and approval gates"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Models](index.html)


- is_a::[\[\[Model Form\]\]](../forms/Model%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Principal-Agent Relationship in Augmented Knowledge Work

The vault embodies a principal-agent relationship where the BCR-2026-xxx framework applies directly. The five terms defined in the Self-Sovereign Identity domain map to concrete vault mechanisms:

| Self-Sovereign Identity Term | Vault Implementation |
|----------|---------------------|
| **Principal** | Vault owner ([\[\[Christopher Allen\]\]↑](../NODES.html#:~:text=Christopher%20Allen)) — directs all work, reviews outputs, bears responsibility |
| **Agent** | Claude Code sessions — generate content, execute tasks, operate within conferral |
| **Conferral** | Rules, skills, processes — what Claude may do, how, and within what boundaries |
| **Authorship** | Claude generates content: notes, summaries, code, form extractions |
| **Responsibility** | The vault owner reviews, approves, and stands behind every committed change |

The authorship/responsibility split is visible in every session. Claude authors draft content. The vault owner accepts, rejects, or revises it. Git commits carry the owner's signature (`-S -s`), not Claude's — because responsibility, not authorship, determines attribution.

## Three Conditions Applied

The vault satisfies all three conditions for meaningful authority:

**Legibility** — The vault owner can observe what Claude does and comprehend why. Session logs record actions. Learning loops capture process insights. WORKSTATE.md tracks current task and progress. The `AskUserQuestion` tool surfaces decisions that require human judgment. Nothing happens invisibly.

**Boundaries** — Claude operates within constraints the vault owner established. Rules define imperatives (what must and must not happen). Skills define capabilities (what Claude can do). Processes define workflows (how multi-step operations proceed). The `paths:` trigger system loads constraints contextually — [Garden/](../) files get garden rules, meeting files get meeting rules.

**Override** — The vault owner can intervene at any time. The `AskUserQuestion` tool creates approval gates. The commit protocol requires human sign-off. The `directed_at::` predicate on inquiry forms flags questions requiring human judgment. Session exit checkpoints verify state before closing. The vault owner can revoke any conferral by editing rules.

## Conferral Mechanisms

The vault's conferral system has explicit structure:

- **CLAUDE.md** — identity-level conferral. What this project is and what it does not do.
- **Rules** — imperative conferrals. Behavioral constraints that load automatically.
- **Skills** — capability conferrals. What Claude can do when invoked.
- **Processes** — workflow conferrals. How multi-step operations proceed.
- **Templates** — output conferrals. What generated content should look like.

Each mechanism is editable by the vault owner, version-controlled in git, and subject to review. The conferral chain is legible: any session can trace its authority from CLAUDE.md through rules to the specific skill being invoked.

## Augmentation, Not Substitution

The model distinguishes augmentation from substitution. Augmentation preserves the principal's authority — Claude extends capability while the human retains judgment. Substitution erodes authority — the agent makes decisions the principal cannot see, understand, or override.

The diagnostic: if removing the human from the loop changes nothing about the system's behavior, the relationship has shifted from augmentation to substitution. The vault's approval gates, learning loops, and commit protocols exist to prevent this drift.

## Sources

- BCR-2026-xxx — principal authority predicates and definitions
- Chat archive: agency-and-autonomy-in-agentic-ai-systems.md — application to AI tools
- Vault configuration: .claude/CLAUDE.md, rules/, skills/, processes/

## Relations

- depends_on::[\[\[Authority Conferral Chain\]\]](Authority%20Conferral%20Chain.html)
  - The vault's conferral mechanisms implement the formal predicate model.

- depends_on::[\[\[Principal Authority as Agency Law for Digital Identity\]\]](../glosses/Principal%20Authority%20as%20Agency%20Law%20for%20Digital%20Identity.html)
  - The five-term vocabulary (principal, agent, conferral, authorship, responsibility) defines this model's concepts.

- relates_to::[\[\[Delegated Decision Authority Spectrum\]\]](../boundaries/Delegated%20Decision%20Authority%20Spectrum.html)
  - The four authority zones operationalize this model's boundary condition.

- relates_to::[\[\[Human Authority Over Augmentation Systems\]\]](../principles/Human%20Authority%20Over%20Augmentation%20Systems.html)
  - The principle that justifies this model's design commitments.

- relates_to::[\[\[Opus Form\]\]](../forms/Opus%20Form.html) — Opus Form's principal:: and authored_by:: predicates reflect the authorship/responsibility split
