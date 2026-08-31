# LexOffline — CPC, 1908 & The Limitation Act, 1963 Module

Offline desktop app (Python + PySide6 + local SQLite) for the **Code of
Civil Procedure, 1908** and **The Limitation Act, 1963**. Part of the
LexOffline suite, built to the same rule: every fact shown comes from the
local database or from plain, auditable arithmetic — nothing is generated
or inferred by a model.

Source texts: IndiaCode bare acts, verified statutory texts.

## Download (no Python required)

Prebuilt executables for Windows, macOS, and Linux are attached to each
[GitHub Release](../../releases) — download, double-click, no installation
of Python or any dependency needed. Built automatically by GitHub Actions
from this repo's own source on every release (see
`.github/workflows/build_desktop.yml`), so what you download is exactly
what's in this code.

**Get it from GitHub Releases, not WhatsApp or email** — the file is
around 50–85MB depending on platform, larger than most messaging apps
allow as an attachment.

**Windows users — an important, expected warning:** since this is a free,
independently-built tool (not signed by a paid commercial certificate),
Windows will show a blue "Windows protected your PC" SmartScreen warning
the first time you run it. This is normal for unsigned software and does
not mean anything is wrong — click **"More info"**, then **"Run anyway"**.

**Mac users — the equivalent warning on macOS:** unzip the download, drag
`LexOfflineCPC.app` to your Applications folder, then macOS will likely
say it "cannot be opened because the developer cannot be verified." This
is Gatekeeper, the same kind of unsigned-software warning as Windows
SmartScreen — **right-click (or Control-click) the app → Open**, then
confirm **"Open"** in the dialog that appears. You only need to do this
once; after that it opens normally.

**Linux users:** if the app doesn't open a window when you run it, you may
be missing `libxcb-cursor0` — install it with your package manager
(`sudo apt install libxcb-cursor0` on Debian/Ubuntu).

## Run from source instead

### Desktop App
```
pip install -r requirements.txt
python3 main.py
```

### Web Companion (Online Access)
```
pip install -r web/requirements.txt
python3 web/app.py
```
Open `http://localhost:5000` in your browser.

## What's in this build

- **Act Explorer (Dual Statutory Coverage)**:
  - **Code of Civil Procedure, 1908**: Sections 1–158 (by Part), Orders I–LI with all Rules, Appendices A–I.
  - **The Limitation Act, 1963**: Full substantive Sections 1–32 (Parts I–V) plus the complete Schedule of Articles 1–137 (First Division: Suits, Second Division: Appeals, Third Division: Applications).
- **Cross-References & Limitation Linkage**:
  - Deterministic in-text citation detection ("Section 47", "Order XXI Rule 54", "O. XXI, R. 58", etc.), resolved against the local database.
  - **CPC ↔ Limitation Linkage**: Automatically surfaces corresponding Limitation Articles when viewing CPC provisions (e.g. Order IX Rule 13 ↔ Article 123, Order XXII ↔ Articles 120/121, Order XLI ↔ Article 116, Order XXI ↔ Articles 127–136, Section 115 ↔ Article 131).
- **Full-Text Search (SQLite FTS5)**:
  - Instant full-text search indexing CPC sections, rules, appendices, Limitation Act sections, and all 137 schedule articles.
- **Bookmarks and Notes**:
  - Per-provision bookmarks and personal notes stored locally for both CPC and Limitation Act provisions.
- **State Amendment Toggle (CPC)**:
  - View selector on every CPC Section/Rule across 11 states, deterministically split on source state headers.
- **Deadline & Limitation Tracker**:
  - Category-filtered calculator for CPC procedural deadlines and ~30 curated, commonly-cited statutory Limitation periods, each with its full Order/Rule/Section cross-reference spelled out.
  - Plus a general calculator covering **all 137 Schedule Articles** to the Limitation Act — not just the curated ones — so no Article is browsable-only. Handles Articles with alternative periods (e.g. Article 61's three sub-clauses) by showing every option rather than guessing which applies.
  - **Section 12 Exclusion Support**: Deduct/exclude time taken for obtaining certified copies of decrees and judgments.
- **Courtroom Practice Checklists**:
  - 7 essential statutory compliance checklists for core courtroom proceedings:
    - **Order VII Rule 11**: Rejection of Plaint (7 statutory clauses, *Dahiben* / *Saleem Bhai* threshold tests, no-partial-rejection rule).
    - **Order XXXIX Rules 1 & 2**: Temporary Injunctions (3-prong test, Rule 3 Proviso same-day delivery mandate, Rule 3A 30-day disposal endeavour).
    - **Section 80**: Notice to Government (2 full months requirement, essential ingredients, Section 80(2) urgency waiver application).
    - **Order XXII**: Death of Parties & LR Substitution (90-day limitation under Art. 120, automatic abatement, 60-day set aside under Art. 121, Sec. 5 condonation, Rule 10A pleader duty).
    - **Section 148A**: Caveat Practice (service obligations, 90-day expiry rule).
    - **Section 100**: Second Appeal (Substantial Question of Law test, *Sir Chunilal Mehta* formulation rules, Sections 100A/102 bars).
    - **Section 115**: Civil Revision (3 jurisdictional error tests, 1999 Proviso final-disposition bar, Art. 131 90-day limitation).
- **Court-Ready Drafting Templates**:
  - 8 standard court-tested civil drafts with bracketed substitution placeholders:
    - **Caveat Petition (Section 148A CPC)** + Verification Affidavit + RPAD Notice.
    - **Temporary Injunction Application (Order XXXIX Rules 1 & 2 CPC)** + Supporting Affidavit + Rule 3 Urgency grounds.
    - **Setting Aside Ex-Parte Decree (Order IX Rule 13 CPC)** + Section 5 Limitation Condonation Application & Affidavit.
    - **Tabular Execution Petition (Order XXI Rule 11(2) CPC)** (mandatory 10-column civil execution format).
    - **Substitution of Legal Representatives (Order XXII Rule 3/4 CPC)** + Surviving legal heirs schedule + Affidavit.
    - **Statutory Notice to Government (Section 80 CPC)** (2-month mandatory pre-suit notice).
    - **Plaint General Skeleton (Order VII CPC)** (chronological facts, cause of action, valuation, jurisdiction, prayer, verification).
    - **Written Statement General Skeleton (Order VIII CPC)** (preliminary objections, specific para-wise denials, verification).
- **Order XXI Execution Roadmap & Navigator**:
  - 5 interactive execution pathways navigating the 106 rules of Order XXI:
    - **Money Decrees (Attachment & Sale)**: 9 sequential stages covering limitation audits, Rule 11 petitions, Rule 22 notices, Rule 41 asset disclosures, Rule 43/46/48/54 attachments, Section 60 statutory exemptions, Rule 58 claims, Rule 64–72 auctions, Rule 89/90 setting aside sale, and Rule 92/94 confirmation.
    - **Delivery of Immovable Property (Possession)**: Actual physical possession (Rule 35(1)), symbolic delivery (Rule 36), police protection applications, Rule 97 resistance removal, Rule 99 dispossession, and Rule 101 full title trials.
    - **Injunction & Specific Performance Decrees**: Rule 34 court-executed conveyance, Rule 32 attachment/civil prison, and Rule 32(5) court-appointed commissioner.
    - **Garnishee Proceedings**: Rules 46A–46I third-party debt recovery and statutory discharge.
    - **Arrest & Detention in Civil Prison**: Section 51 Proviso means test, Section 56 absolute protection for women, Section 58 duration tiers, Rule 37 show-cause notice, and Rule 39 subsistence allowance.
  - Features sequential stage timeline, governing statutory rule badges, limitation indicators, advocate tactical insights, and one-click provision jumps.
- **Web Companion (`web/`)**:
  - Lightweight, server-rendered Flask web app sharing the exact same underlying SQLite database and deterministic logic.
  - Accessible from chambers, mobile, or home for quick statutory lookups, checklists, templates, and execution workflows.

## Architecture

- `db.py` — SQLite access layer (`ActDatabase`) querying `cpc_1908.db`.
- `limitation_data.py` — Structured statutory dataset for The Limitation Act, 1963 (Sections 1–32 + Schedule Articles 1–137).
- `checklists_data.py` — Structured courtroom practice checklists, statutory grounds, and landmark precedents.
- `templates_data.py` — Structured court-ready petition templates, statutory notices, and execution formats.
- `execution_data.py` — Structured Order XXI execution workflows, sequential stages, and advocate tactics.
- `deadlines.py` — Fixed CPC deadline rules, Limitation Act schedule rules, and Section 12 exclusion arithmetic.
- `xref.py` — Deterministic in-text cross-reference extraction and database resolution.
- `state_amend.py` — Deterministic state-amendment blob splitter.
- `main.py` — PySide6 desktop interface (Explorer, Practice Checklists, Drafting Templates, Execution Navigator, Search, Bookmarks, Deadline & Limitation Tracker).
- `web/` — Flask web companion application (`app.py`, templates, responsive CSS, and tests).
- `build_cpc_db.py` — Ingestion and database compilation script.
- `tests/` — Desktop regression test suite covering `test_execution.py`, `test_templates.py`, `test_checklists.py`, `test_limitation.py`, `test_deadlines.py`, `test_state_amend.py`, and `test_xref.py` (43 tests).
- `web/tests/` — Web test suite covering all 34 web routes, execution roadmaps, templates, checklists, and calculator endpoints.




