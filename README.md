# LexOffline — CPC, 1908 Module

Offline desktop app (Python + PySide6 + local SQLite) for the Code of
Civil Procedure, 1908. Part of the LexOffline suite (alongside the
Companies Act 2013 module), built to the same rule: every fact shown
comes from the local database or from plain, auditable arithmetic —
nothing is generated or inferred by a model.

Source text: IndiaCode bare act, as on 10 January 2026.

## Run it

```
pip install -r requirements.txt
python3 main.py
```

## What's in this build

- **Act Explorer** — full navigation tree: Sections 1–158 (by Part),
  Orders I–LI with all Rules, Appendices A–I. Full provision text,
  including embedded state-amendment notes where the source recorded
  them.
- **Cross-References tab** — deterministic, regex-based detection of
  explicit in-text citations ("Section 47", "Order XXI Rule 54", "O.
  XXI, R. 58", etc.), resolved against the local database and
  clickable to jump straight there.
- **Search** — full-text search (SQLite FTS5) across sections, rules,
  and appendices.
- **Bookmarks** and **Notes** — per-provision, stored locally.
- **State Amendment toggle** — a "View" selector on every Section/Rule
  (Central Act / one of 11 states). The source data stores state
  amendments as one flat blob per provision, often mixing several
  states together (e.g. Section 60 mixes Kerala, Himachal Pradesh,
  Tamil Nadu, Rajasthan and Uttar Pradesh notes back to back);
  `state_amend.py` deterministically splits that blob on the literal
  state-name headers as they appear in the source (no rewriting, no
  correction — a known source typo, "Orrisa" for Orissa, is recognised
  for grouping but the stored text is left exactly as written).
  Selecting a state with no recorded amendment for that provision
  shows a plain note saying so, rather than nothing.
- **Deadline Tracker** — the fixed CPC timelines from the spec (Written
  Statement, caveat validity, injunction disposal, judgment
  pronouncement, decree preparation, etc.) as pure date arithmetic off
  a single trigger date you enter.

## Known limitation — please read

The Cross-References tab only surfaces citations that are **literally
present in the bare-act text** (e.g. a section that says "as provided
in section 47"). It does **not** reproduce a curated legal
relationship map like the illustrative Section 80 example in the
original spec (Section 80 ↔ Order XXVII, Section 79, Section 81,
Section 82, Order XXVII Rule 5A) — that section's actual text doesn't
contain those citations, so no purely textual/deterministic method can
recover them without someone (a person, not a model) curating that
relationship by hand as a one-time authored dataset.

Coverage today: ~27% of Sections and ~16% of Rules have at least one
detected textual cross-reference. This is honest and useful as far as
it goes, but it is a materially smaller feature than "every provision
gets a cross-reference map."

## Not yet built (from the full spec)

The uploaded spec ("CPC Practice Engine") is far larger than this
build — it also calls for: per-section Practical Tool tabs (one
bespoke deterministic tool per section), Draft Links / a fillable
Appendix A–I form library, a Case Diary, the full Order XXI Execution
Workflow Engine, a Court Fee Calculator, and a Limitation Calculator.

Court Fee and Limitation calculators in particular need real,
verified rate/period tables (which vary by state and by Act) before
they should compute anything a lawyer would rely on — building those
with placeholder or guessed figures would be worse than not building
them, so they're deliberately left out of this build rather than
shipped with invented numbers.

## Architecture

- `db.py` — thin SQLite access layer (`ActDatabase`), shared shape with
  the Companies Act 2013 module.
- `xref.py` — deterministic cross-reference extraction (whitelisted
  Roman-numeral Order matching, footnote-line filtering to avoid
  amendment-history false positives).
- `state_amend.py` — deterministic state-amendment blob splitter.
- `deadlines.py` — fixed CPC deadline rules + date arithmetic.
- `main.py` — PySide6 UI (Explorer / Search / Bookmarks / Deadline
  Tracker tabs).
- `build_cpc_db.py` — one-time ingestion script, bare-act markdown →
  `cpc_1908.db`.
- `tests/` — pytest regression suite for `xref.py`, `deadlines.py`, and
  `state_amend.py` (16 tests, run with `pytest tests/`).
