---
created: 2026-03-04
author: Christopher Allen
brief_summary: "Principle that a knowledge vault needs searchable content, not file formats. When information can be extracted into a searchable rendition, the original binary's value drops to provenance evidence. Store binaries locally only when no canonical source exists AND the binary provides value beyond its rendition."
tagline: "The knowledge vault needs searchable content, not file formats — renditions replace binaries when canonical sources exist"
formatted: "2026-03-14"
---

← [Garden Patch Home](../) · [Principles](index.html)


- is_a::[\[\[Principle Form\]\]](../forms/Principle%20Form.html)
- has_status::[\[\[Seed Stage\]\]](../forms/Seed%20Stage.html)
- in_domain::[\[\[Deep Context Architecture\]\]](../domains/Deep%20Context%20Architecture.html)

# Content Over Container

**The knowledge vault needs searchable content, not file formats.** The value of a stored binary is the information it contains. When that information can be extracted into a searchable, lightweight rendition, the original binary's value drops to provenance evidence — and often a sidecar pointing to the canonical source is sufficient.

## Implications by File Type

**PDFs**: Extract text via pdf2txt or similar tool into a rendition. If the canonical PDF is available at a stable URL, a sidecar with `derived_from::` replaces local storage. Store the PDF locally only when no canonical source exists.

**Apple iWork files** (.key, .pages, .numbers): These change their modification date when opened without edits. In a git-tracked vault, this generates phantom diffs — files that appear changed in `git status` without actual content changes. iWork files should never be stored where git can see them. If the content matters, create a rendition (export to PDF, then pdf2txt). If the canonical file lives on iCloud or a shared drive, a sidecar with `derived_from::` is sufficient.

**Audio and video**: Canonical sources (YouTube, Zoom cloud recordings) are better storage than local files. A sidecar links to the canonical URL. The transcript (a rendition of the audio) serves the vault's needs. Store locally only when no canonical source exists AND the binary provides value beyond its transcript — for example, a recording needed for generating VTT timecodes for subtitle upload.

**Whisper/VTT intermediate files**: A .whisper file is a raw intermediate — reproducible by running the audio through Whisper again. A .vtt timecode file is more useful (uploadable to YouTube as subtitles) but also reproducible. Neither needs git tracking. A sidecar can note "reproducible from audio via Whisper Large v3 Turbo" for provenance.

## Binary Storage Criteria

Store a binary locally only when both conditions are met:

1. No canonical source exists (or the canonical source is unreliable)
2. The binary provides value beyond its rendition (timecodes, visual layout, fidelity)

When either condition fails, a rendition + sidecar replaces local storage.

## Sources

Extracted from the Content Over Container principle section of the compound nodes research note.

## Relations

- extracted_from::[\[\[Compound Nodes for Knowledge Management\]\]↑](../NODES.html#:~:text=Compound%20Nodes%20for%20Knowledge%20Management)
  - The principle section, lines 144-168.

- constrains::[\[\[Compound Node Anatomy\]\]↑](../NODES.html#:~:text=Compound%20Node%20Anatomy)
  - This principle determines when archives/ subfolders contain actual binaries vs. just sidecars pointing to canonical sources.
