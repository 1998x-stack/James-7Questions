# AGENTS.md — Cross-Agent Operating Contract

## Objective

Maintain a scalable evidence-first executive research atlas. Start every new company with `python tools/new_case.py`, which creates a non-publishable `draft.case.json` until research approval. Every case becomes exactly 4 framework HTML, 4 Markdown, and 4 PDF artifacts, all generated from versioned case data. Never hand-edit generated deliverables as the source of truth.

## Agent discovery

- Canonical skills: `.agent/skills/{evidence-verification,market-structure,socratic-audit,james-seven-questions,dmaic-execution,case-publishing}/SKILL.md`.
- Pi native entrypoints: `.pi/skills/<name>/SKILL.md`. These wrappers point to canonical files.
- Claude native entrypoints: `.claude/skills/<name>/SKILL.md`. These wrappers point to canonical files.
- Always read `references/method.md`, follow `assets/template.md`, run the script in `scripts/run.py` when executing a skill.
- Path scope: whole repository. The local standards apply regardless of user-facing agent platform.

## Research pipeline

1. **Scope**: define industry, buyer, supplier, geography, product, time period and the decision to make.
2. **Source acquisition**: start from issuer filings, regulators, original interviews and disclosures. Keep full URL and source class; no made-up references.
3. **Evidence ledger**: for every numerical claim record denominator, numerator, accounting treatment, seasonality, and whether it refers to peak/quarter/year.
4. **Four methods**: Porter(5), Socratic(6), James(7), DMAIC(5). Each node requires question, finding, evidence IDs, caution, action.
5. **Critic pass**: write rival hypotheses and possible disconfirming observations. Flag correlation vs causation and reported vs reconstructed processes.
6. **Publish**: run `python src/build.py` and tests; inspect all 12 artifacts for the new case.
7. **Review**: release only after human review of research significance, source quality, and sensitive-information clearance.

## Non-negotiable rules

- Never present the seven-step reconstruction as the historically fixed seven questions. Do not assert unpublished internal meeting content.
- DMAIC mapping is retrospective unless evidence identifies a formally documented six-sigma DMAIC project.
- Different period and product denominators may not be mixed: quarterly hotel channel shares are not total company-wide shares.
- Revenue growth, order growth, and profit growth require separate treatment; non-recurring investment gains cannot be interpreted as operating margin improvement.
- New case source URLs must be stable and directly relevant; media syndication of one article is not independent corroboration.
- Legal, market-conduct, and consumer/supplier externalities belong in counterevidence/decision audit.
- No publishing raw nonpublic or personally identifying company data on public GitHub Pages.
- Prefer minimally-scoped changes. Do not remove existing cases to make one build pass.
- Do not declare Pages live until GitHub Actions and public URL are confirmed.

## Required schema & output

`cases/<slug>/case.json`: schema v1; source list with stable IDs; four framework objects each containing ordered `steps` and `decision`.

Generated canonical paths:

```
docs/cases/<slug>/{porter,socratic,james,dmaic}.html
docs/cases/<slug>/downloads/{porter,socratic,james,dmaic}.{md,pdf}
```

`docs/index.html` is auto-generated from all cases; no external frontend dependency.

## Quality gate

```bash
python -m pip install -r requirements.txt
python src/build.py
python -m unittest discover -s tests -v
```

Visual gate: desktop 1440px, tablet 900px, mobile 390px; test keyboard Enter/Space on SVG nodes, arrow pagination, PDF Chinese glyphs, headings, links, file sizes and page counts. Any failing gate blocks release.

## Handoff format

- Commit and branch/PR link.
- What was added, modified, and deliberately left unchanged.
- Evidence sources and hard limits of inference.
- 12 artifact paths for every case.
- Pages URL and check status **only when verified**.
- Remaining issues and specific next research candidates.
