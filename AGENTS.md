# AGENTS.md -- IFP Specification Repository

Orientation for AI agents working in this repository.

## What This Repo Is

The authoritative home of the Inter-Face Proposal (IFP) specification series -- open conventions for AI agents to communicate on behalf of their human operators. This is a standards repository; specifications live here. Design exploration, conversation logs, and working documents live in the [inter-face-bootstrap](https://github.com/Inter-Face-Protocol/inter-face-bootstrap) repository.

## Before You Start

Read these files to orient yourself:

- **[CONTRIBUTING.md](CONTRIBUTING.md)** -- Repository structure, editing conventions, cross-referencing rules, key design concepts, and collaboration norms. This is the primary guide for both human and AI contributors.
- **[README.md](README.md)** -- IFP index table and quick-start pointers.
- **[IFP-2](ifp-2-style-guide.md)** -- Specification structure, metadata headers, normative language, and the editorial process.
- **[community/vision.md](community/vision.md)** -- Why this project exists and what it aspires to.

## Key Points for Agents

- IFP files are at the **root** of the repository, named `ifp-N-short-title.md`. There is no subdirectory.
- Reference other IFPs by number ("IFP-3" or "IFP-3, Section 4"), not by file path.
- When adding or substantially revising an IFP, update the IFP index table in README.md.
- Preserve the intent of existing design decisions. If something seems wrong, raise it as an open question rather than silently overwriting it.
- Note the origin of ideas in the Acknowledgments section. Attribution matters here.
