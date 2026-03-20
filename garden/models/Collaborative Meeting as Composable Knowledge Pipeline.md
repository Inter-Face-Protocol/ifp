---
created: 2026-03-19
author: Christopher Allen
brief_summary: "Seven-stage pipeline for turning collaborative meetings into garden nodes, tool notes, person notes, and patch updates. Stages: pre-work (agenda from prior session output), meeting, compound capture (audio+transcript+folder), post-processing (cleanup+notes+triage), garden integration (seed+graft+repatriate), report-out (cover letter+zip+PR merge), and close. Each stage filters — a 90-minute call produced 120+ patch files, 9 tool notes, 4 person notes, 8 garden nodes, and 8 garden-foundation tasks. First exercised on the 2026-03-19 Peter Kaminski garden patch review."
tagline: "Seven composable stages from meeting to garden — each stage filters, each output feeds the next"
---

← [Garden Patch Home](../) · [Models](index.html)

- is_a::[Model Form](../forms/Model%20Form.html)
- has_status::[Seed Stage](../forms/Seed%20Stage.html)
- in_domain::[Deep Context Architecture](../domains/Deep%20Context%20Architecture.html)

# Collaborative Meeting as Composable Knowledge Pipeline

A meeting with a knowledge collaborator is not an event to document — it is a pipeline input that produces garden nodes, tool notes, person notes, and patch updates. The pipeline has seven stages. Each is independently useful, composable with others, and produces outputs that feed downstream stages.

## The Seven Stages

### 1. Pre-Work

**Input**: Prior session outputs (garden patch, research, citations)
**Output**: Updated agenda reflecting current state

Update the meeting agenda with work done since it was written. The agenda is a living document — it should reflect the current state of the garden, not the state when originally drafted. Add new items, note what's changed, prepare questions that reference specific nodes.

**Composable parts**: Agenda template, workstream state review

### 2. Meeting

**Input**: Agenda, shared context, collaborator's pre-loaded topics
**Output**: Recording, live notes (collaborator's edits to agenda)

The meeting itself. Accept that the agenda will diverge — the collaborator's topics often reveal more than planned questions. Pete's Section 0 dominated 60 of 90 minutes and produced more garden-relevant content than the planned walkthrough.

**Composable parts**: Recording setup, Chatham House protocol, live collaborative editing (HackMD or equivalent)

### 3. Compound Capture

**Input**: Recording, live notes
**Output**: Compound meeting folder (lead file, raw transcript, audio in Archives/, recording sidecar)

Set up the compound folder structure immediately after the call. Copy audio from Zoom to Archives/. Create the whisper transcript placeholder. Create the recording sidecar with artifact predicates. Touch the raw transcript file for whisper output.

**Composable parts**: Compound folder template, recording sidecar template, whisper pipeline

### 4. Post-Processing

**Input**: Raw transcript, agenda with live edits
**Output**: Cleaned transcript, meeting notes (lead file), person notes, daily note, spelling reference updates

Four sub-stages, each with its own skill:
- **Transcript cleanup** (`/transcript-cleanup`): Raw → cleaned. Speaker normalization, term correction, filler calibration. Medium level for internal reference.
- **Meeting notes** (`/meeting-notes`): Cleaned transcript → topic-organized synthesis. Summary above divider, quotes above divider, detail below. Decisions, action items, resources shared (table with vault links).
- **Person notes**: Create or update notes for all people mentioned. Track status: Updated, Created, or Ghost.
- **Daily note + spelling reference**: Capture session activity and new transcription errors.

**Composable parts**: /transcript-cleanup skill, /meeting-notes skill (with AI Summaries conditional), person note status tracking pattern, spelling reference as cumulative asset

### 5. Garden Integration

**Input**: Meeting notes, call observations, resources shared, consequences triage
**Output**: Garden nodes, tool notes, clippings, garden-foundation tasks, workstream BACKLOG updates

The stage where meeting content feeds the garden. Five sub-stages:
- **Consequence triage**: Walk through each call outcome, route to destination (this workstream, garden-foundation, future workstream, meeting notes only). One item at a time with AskUserQuestion.
- **Resource capture**: Resources mentioned → Tools/ (software), Clippings/ (articles), [Garden/](../) (concepts with 3+ independent validations). Resources Shared section becomes a table with vault wikilinks.
- **Garden node seeding**: Call observations that map to form types → seed in source garden. Peter's gossip duality observation became an inquiry. Jerry's neobooks concept became a gloss. Three-source validation (Nyk's council + Peter's personas + agency-agents) became a pattern.
- **Patch grafting**: New source garden nodes → convert links, graft to patch, update index pages.
- **Repatriation**: General-purpose nodes created in the patch → copy back to source garden. Forked improvements → merge back where they add value without creating ghost links.

**Composable parts**: Consequence triage protocol, resource routing rules (Tools/ vs Clippings/ vs [Garden/](../)), three-source validation signal, link conversion scripts, repatriation checklist

### 6. Report-Out

**Input**: Updated meeting notes, updated patch, compound folder
**Output**: Cover letter, zip (without Archives/), merged PR, next-meeting agenda items

Package the work for the collaborator:
- **Cover letter** in the user's raw voice (casual, conversational, "I" heavy). Include specific requests (try AGENTS.md, make your changes). Reference next meeting topics.
- **Zip** the compound folder excluding Archives/ (too large). Sidecar tells where to get audio.
- **Merge PR** or push changes to the shared repo.
- **Seed next-meeting agenda** in the daily note and person note.

**Composable parts**: Cover letter template (raw voice), compound zip script, PR merge checklist, next-meeting seeding

### 7. Close

**Input**: All prior outputs, workstream state
**Output**: Updated workstream state, deep learning captures, session log

Update the workstream BACKLOG (check off completed, defer blocked, move items to next call). Run deep learning to catch patterns and cascade improvements. Capture the session in the session log. Update MEMORY.md where session insights change persistent state.

**Composable parts**: Deep learning skill, session capture skill, workstream state machine

## Filtering Ratios

Each stage filters. The 2026-03-19 Peter Kaminski call produced:

```
90 min call
  → 13K words raw transcript
    → 12K words cleaned
      → 9 topic sections in meeting notes
        → 18 consequence items triaged
          → 8 garden nodes seeded (2 inquiries, 2 glosses, 2 patterns, 1 model, 1 gloss)
          → 8 garden-foundation tasks
          → 9 tool notes
          → 4 person notes (2 created, 2 updated)
          → 120+ file garden patch (from 118+)
          → 31 URLs triaged from queue
```

The pipeline is a funnel at each stage and a cycle overall — garden outputs become next meeting's pre-work inputs.

## What This Model Does Not Cover

- Meetings with 3+ participants (different triage dynamics)
- Meetings without a shared knowledge garden (the garden integration stage assumes one)
- Meetings where the collaborator's LLM participates live (future: AGENTS.md enables this)
- The composable knowledge pipeline domain itself (this model is one instance of that unnamed domain)

## First Instance

2026-03-19 Peter Kaminski - Garden Patch Review — the meeting that produced this model. Compound folder with cleaned transcript, exemplar meeting notes structure, cover letter, and recording sidecar. All seven stages exercised in a single Claude Code session.

## Relations

- relates_to::[Neobooks as Composable Knowledge Objects](../glosses/Neobooks%20as%20Composable%20Knowledge%20Objects.html)
  - The compound meeting document is a vault-precinct parallel to garden-precinct patches — portable, self-contained, shareable.

- relates_to::↑ [Structured Disagreement Through Persona Review](../NODES.html#structured-disagreement-through-persona-review)
  - Future meetings could use persona review on meeting notes before garden integration — multiple perspectives on which observations deserve garden nodes.

- extends::↑ [Research as Workflow Not Precinct](../NODES.html#research-as-workflow-not-precinct)
  - Meetings are another pipeline input type alongside web research. Same filtering principle (source → clip → cite → form), different source.

- in_domain::[Deep Context Architecture](../domains/Deep%20Context%20Architecture.html)
