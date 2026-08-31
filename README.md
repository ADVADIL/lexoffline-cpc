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

```
pip install -r requirements.txt
python3 main.py
```

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
  - Category-filtered calculator for CPC procedural deadlines and statutory Limitation periods (10 days, 30 days, 60 days, 90 days, 1 year, 2 years, 3 years, 12 years, 30 years).
  - **Section 12 Exclusion Support**: Deduct/exclude time taken for obtaining certified copies of decrees and judgments.

## Architecture

- `db.py` — SQLite access layer (`ActDatabase`) querying `cpc_1908.db`.
- `limitation_data.py` — Structured statutory dataset for The Limitation Act, 1963 (Sections 1–32 + Schedule Articles 1–137).
- `deadlines.py` — Fixed CPC deadline rules, Limitation Act schedule rules, and Section 12 exclusion arithmetic.
- `xref.py` — Deterministic in-text cross-reference extraction and database resolution.
- `state_amend.py` — Deterministic state-amendment blob splitter.
- `main.py` — PySide6 desktop interface (Explorer, Search, Bookmarks, Deadline & Limitation Tracker).
- `build_cpc_db.py` — Ingestion and database compilation script.
- `tests/` — Regression test suite covering `test_limitation.py`, `test_deadlines.py`, `test_state_amend.py`, and `test_xref.py` (23 tests).
