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
- **Court-Ready Drafting Templates Library (54 Court-Tested Formats)**:
  - **Core Interlocutory Applications (IAs)**:
    - **Temporary Injunction Application (Order XXXIX Rules 1 & 2 CPC)** + Supporting Affidavit + Rule 3 Urgency grounds.
    - **Amendment of Pleadings (Order VI Rule 17 CPC)** + Affidavit (satisfying statutory *due diligence* proviso).
    - **Appointment of Court Commissioner (Order XXVI Rule 9 CPC)** + Affidavit (local investigation, boundaries, encroachment).
    - **Attachment Before Judgment (Order XXXVIII Rule 5 CPC)** + Affidavit (preventing fraudulent disposal of property).
    - **Recall of Witness & Re-Opening Evidence (Order XVIII Rule 17 & Order XVI Rule 1(3) CPC)**.
    - **Standalone Condonation of Delay Application (Section 5 Limitation Act, 1963)** + Affidavit.
    - **Judgment on Admissions (Order XII Rule 6 CPC)** (summary decree on unequivocal admissions).
    - **Formal Application for Adjournment (Order XVII Rule 1 CPC)** (compliant with 3-adjournment rule).
  - **Parties & Capacity Issues (Order I & Order XXXII)**:
    - **Impleadment Application (Order I Rule 10(2) CPC)** (adding necessary/proper parties) + Supporting Affidavit.
    - **Representative Suit Application (Order I Rule 8 CPC)** + Public Notice Advertisement draft.
    - **Appointment of Guardian ad Litem for Minor / Unsound Mind (Order XXXII Rules 3 & 15 CPC)** + Fitness Affidavit.
    - **Striking Out Improperly Joined Party (Order I Rule 10(1) CPC)**.
  - **Evidence, Discovery & Trial Proceedings (Orders XI, XII, XIII, XVI, XVIII, XXVI)**:
    - **Evidence-in-Chief Affidavit of Witness (Order XVIII Rule 4 CPC)** (standard sworn trial affidavit for PW-1 / DW-1).
    - **Witness Summons Application & Batta Calculation Memo (Order XVI Rules 1 & 2 CPC)** (summoning public custodians).
    - **Interrogatories for Examination of Opposite Party & Answer Affidavit (Order XI Rules 1 & 8 CPC)**.
    - **Notice to Admit Documents and Facts (Order XII Rules 2 & 4 CPC)** (7-day admission notice).
    - **Application for Return of Original Marked Exhibits (Order XIII Rule 9 CPC)** (substituting certified copies).
    - **Application for Forensic / Handwriting Expert Opinion (Section 45 IEA / Sec 39 BSA r/w Order XXVI Rule 10A CPC)**.
    - **Commission to Examine Infirm / Bedridden Witness at Residence (Order XXVI Rules 1 & 4 CPC)** + Medical Affidavit.
    - **Section 65B Electronic Evidence Certificate** (WhatsApp chats, emails, CCTV, computer printouts).
  - **Core Pleadings & Substantive Plaints**:
    - **Plaint for Specific Performance of Agreement to Sell** (mandatory Section 16(c) SRA readiness & willingness).
    - **Plaint for Partition and Separate Possession** (genealogy, ancestral coparcenary schedule, metes & bounds).
    - **Plaint for Declaration of Title, Recovery of Possession & Mesne Profits (Order XX Rule 12 CPC)**.
    - **Plaint in Commercial Suit with Mandatory Statement of Truth (Order VI Rule 15A CPC / Commercial Courts Act)** & Section 12A Non-Starter report.
    - **Plaint for Cancellation of Fraudulent / Voidable Sale Deed (Section 31 Specific Relief Act)**.
    - **Plaint for Ejectment / Eviction of Tenant & Arrears of Rent (Section 106 Transfer of Property Act r/w Order VII CPC)**.
    - **Plaint for Injunction Protecting Easementary Rights of Light, Air & Way (Sections 38 & 39 SRA r/w Easements Act)**.
    - **Application for Leave to Sue as an Indigent Person (In Forma Pauperis) (Order XXXIII Rule 1 CPC)** + Schedule of Assets.
    - **General Plaint Skeleton (Order VII CPC)** (facts, cause of action, valuation, court fees, jurisdiction, prayer).
    - **General Written Statement Skeleton (Order VIII CPC)** (preliminary objections, specific denials).
    - **Substitution of Legal Representatives (Order XXII Rule 3/4 CPC)** + Surviving legal heirs schedule.
    - **Statutory Notice to Government (Section 80 CPC)** (2-month mandatory pre-suit notice).
  - **Settlement, Compromise & Withdrawal (Order XXIII)**:
    - **Joint Compromise Petition & Settlement Terms (Order XXIII Rule 3 CPC)** + Section 16 Court Fees refund prayer.
    - **Withdrawal of Suit with Liberty to File Fresh Suit on Same Cause of Action (Order XXIII Rule 1(3) CPC)**.
  - **Pre-Emptive, Summary & Restoration Remedies (Orders VII, IX, XIV, XXXVII, Sections 144, 148A, 152)**:
    - **Caveat Petition (Section 148A CPC)** + Verification Affidavit + RPAD Notice.
    - **Rejection of Plaint Application (Order VII Rule 11 CPC)** + Affidavit (*Dahiben* principles).
    - **Leave to Defend in Summary Suit (Order XXXVII Rule 3(5) CPC)** + Affidavit (*Hubtown* triable issues).
    - **Setting Aside Ex-Parte Decree (Order IX Rule 13 CPC)** + Section 5 Condonation Application.
    - **Restoration of Suit Dismissed for Default under Rule 8 (Order IX Rule 9 CPC r/w Section 151)**.
    - **Restoration of Suit Dismissed under Order IX Rule 2 or 3 CPC (Order IX Rule 4 CPC)**.
    - **Application for Trial of Preliminary Issue on Law / Jurisdiction / Limitation (Order XIV Rule 2(2) CPC)**.
    - **Application for Correction of Clerical / Arithmetical Errors in Decree (Slip Rule) (Section 152 CPC)**.
    - **Application for Restitution upon Reversal of Decree (Section 144 CPC)**.
  - **Execution Court Applications (Order XXI)**:
    - **Tabular Execution Petition (Order XXI Rule 11(2) CPC)** (mandatory 10-column civil execution format).
    - **Police Aid Application in Execution (Section 151 CPC)** + Affidavit.
    - **Application to Break Open Locks for Delivery of Possession (Order XXI Rule 35(3) CPC)**.
    - **Third-Party Claim / Objection Petition (Order XXI Rule 58 CPC)** (independent title claim against attachment).
    - **Application for Removal of Resistance / Obstruction to Possession (Order XXI Rule 97 CPC)**.
  - **Appeals, Revisions & Constitutional Remedies**:
    - **Memorandum of Regular First Appeal (Section 96 & Order XLI Rule 1 CPC)** + Stay Petition (Order XLI Rule 5).
    - **Civil Miscellaneous Appeal (CMA) against Injunction Order (Order XLIII Rule 1(r) CPC)**.
    - **Memorandum of Regular Second Appeal to High Court (Section 100 CPC)** (Substantial Questions of Law formulation).
    - **Civil Revision Petition (Section 115 CPC)** (jurisdictional error tests & 1999 Proviso satisfaction).
    - **Review Petition (Section 114 & Order XLVII Rule 1 CPC)** (error apparent on face of record).
    - **Writ Petition under Article 227 of the Constitution of India** (supervisory jurisdiction over subordinate civil courts).
  - Features 1-click clipboard copy on desktop and web, in-app editor, and `.txt` file download.
- **Order XXI Execution Roadmap & Navigator**:
    - **Money Decrees (Attachment & Sale)**: 9 sequential stages covering limitation audits, Rule 11 petitions, Rule 22 notices, Rule 41 asset disclosures, Rule 43/46/48/54 attachments, Section 60 statutory exemptions, Rule 58 claims, Rule 64–72 auctions, Rule 89/90 setting aside sale, and Rule 92/94 confirmation.
    - **Delivery of Immovable Property (Possession)**: Actual physical possession (Rule 35(1)), symbolic delivery (Rule 36), police protection applications, Rule 97 resistance removal, Rule 99 dispossession, and Rule 101 full title trials.
    - **Injunction & Specific Performance Decrees**: Rule 34 court-executed conveyance, Rule 32 attachment/civil prison, and Rule 32(5) court-appointed commissioner.
    - **Garnishee Proceedings**: Rules 46A–46I third-party debt recovery and statutory discharge.
- **Advocate Case Diary & Hearing Timeline Tracker**:
  - Offline chamber notebook stored directly in local SQLite (`case_diary` and `case_hearings` tables):
    - Track active litigation: Case Number, Court Name, Client Name & Role, Opposite Party & Counsel, Current Procedural Stage, and Board Postings.
    - **Automatic Statutory Deadline Suggester**: Computes governing CPC rules and limitation periods based on the active stage (e.g. 30/90-day WS deadline under Order VIII Rule 1, 90-day LR substitution under Article 120, 30/90-day appeal windows under Article 116, 90-day caveat validity under Section 148A).
    - **Daily Orders & Hearings Log**: Records per-hearing court proceedings, business done, and next adjourned dates.
    - Upcoming court board calendar view on desktop and web.
- **Web Companion (`web/`)**:
  - Lightweight, server-rendered Flask web app sharing the exact same underlying SQLite database and deterministic logic.
  - Accessible from chambers, mobile, or home for quick statutory lookups, checklists, templates, execution workflows, and case diary.

## Architecture

- `db.py` — SQLite access layer (`ActDatabase`) querying `cpc_1908.db` with user storage for bookmarks, notes, case diary, and hearing logs.
- `case_stages.py` — Deterministic litigation stage definitions and statutory deadline suggester.
- `limitation_data.py` — Structured statutory dataset for The Limitation Act, 1963 (Sections 1–32 + Schedule Articles 1–137).
- `checklists_data.py` — Structured courtroom practice checklists, statutory grounds, and landmark precedents.
- `templates_data.py` — Structured court-ready petition templates, statutory notices, and execution formats.
- `execution_data.py` — Structured Order XXI execution workflows, sequential stages, and advocate tactics.
- `deadlines.py` — Fixed CPC deadline rules, Limitation Act schedule rules, and Section 12 exclusion arithmetic.
- `xref.py` — Deterministic in-text cross-reference extraction and database resolution.
- `state_amend.py` — Deterministic state-amendment blob splitter.
- `main.py` — PySide6 desktop interface (Explorer, Case Diary, Practice Checklists, Drafting Templates, Execution Navigator, Search, Bookmarks, Deadline & Limitation Tracker).
- `web/` — Flask web companion application (`app.py`, templates, responsive CSS, and tests).
- `build_cpc_db.py` — Ingestion and database compilation script.
- `tests/` — Desktop regression test suite covering `test_case_diary.py`, `test_execution.py`, `test_templates.py`, `test_checklists.py`, `test_limitation.py`, `test_deadlines.py`, `test_state_amend.py`, and `test_xref.py` (48 tests).
- `web/tests/` — Web test suite covering all 38 web routes, case diary, execution roadmaps, templates, checklists, and calculator endpoints.





