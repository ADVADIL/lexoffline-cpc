#!/usr/bin/env python3
"""
LexOffline — CPC, 1908 module ingestion.
Parses the IndiaCode bare-act markdown export into a clean, act-agnostic
SQLite schema: sections (Ss. 1-158), orders/rules (First Schedule),
and appendices (prescribed forms), with FTS5 full-text search.
"""
import re
import sqlite3
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else "/mnt/user-data/uploads/a1908-05__1_.md"
DB_PATH = "/home/claude/lexoffline_cpc/cpc_1908.db"

NOISE_LINE_RES = [
    re.compile(r"^```\s*$"),
    re.compile(r"^IndiaCode\s*$"),
    re.compile(r"^\d{1,4}\s*$"),          # bare page-number lines
    re.compile(r"^#+\s*IndiaCode\s*$"),
]

# Verified, individually-checked source corruptions: each is a stray digit
# inserted between a footnote bracket and the real rule number (e.g.
# '1[1.' rendered as '1[ 21.') during the original PDF-to-markdown
# conversion, plus one unbracketed plain typo ('13.' for '3.'). There is
# no consistent arithmetic pattern across these (the stray digit isn't a
# fixed offset from the footnote marker), so each is listed explicitly
# rather than guessed at via a general regex — the correct rule number
# for each is confirmed against the source's own table-of-contents
# listing before being applied here. No other text is altered; this only
# repairs the numbering so the provision attaches to the right rule
# instead of breaking heading detection entirely.
KNOWN_LINE_CORRECTIONS = {
    "1[ 21. Judgment when pronounced.": "1[1. Judgment when pronounced.",
    "1[ 25. How evidence shall be taken in appealable cases.": "1[5. How evidence shall be taken in appealable cases.",
    "4[ 313. Memorandum of evidence in unappealable cases.": "4[13. Memorandum of evidence in unappealable cases.",
    "13. Substance of examination to be written.": "3. Substance of examination to be written.",
    "37. Procedure at hearing.": "7. Procedure at hearing.",
    # Section-level instance of the same stray-digit pattern, found while
    # auditing the Limitation Act module's CPC cross-references — Article
    # 92-96's citations to "Section 92" were failing because Section 92
    # itself was silently absent from the parsed output.
    "392. Public charities.": "92. Public charities.",
    "335. Date and contents of decree.": "35. Date and contents of decree.",
    # The following were found via a systematic document-wide scan for this
    # same corruption signature (a stray digit prepended to the real rule
    # number), cross-checked against the ToC for each exact title text —
    # not guessed. Heavily concentrated in Orders XVIII and XX, which
    # explains why those two orders were still missing many rules after
    # the earlier, more piecemeal round of fixes.
    "860. Property liable to attachment and sale in execution of decree.": "60. Property liable to attachment and sale in execution of decree.",
    "310. Return of plaint.": "10. Return of plaint.",
    "36. When deposition to be interpreted.": "6. When deposition to be interpreted.",
    "37. Evidence under section 138.": "7. Evidence under section 138.",
    "38. Memorandum when evidence not taken down by Judge.": "8. Memorandum when evidence not taken down by Judge.",
    "1[29. When evidence may be taken in English.": "1[9. When evidence may be taken in English.",
    "311. Questions objected to and allowed by Court.": "11. Questions objected to and allowed by Court.",
    "315. Power to deal with evidence taken before another Judge.": "15. Power to deal with evidence taken before another Judge.",
    "316. Power to examine witness immediately.": "16. Power to examine witness immediately.",
    "13. Judgment to be signed.": "3. Judgment to be signed.",
    "14. Judgments of Small Cause Courts.": "4. Judgments of Small Cause Courts.",
    "15. Court to state its decision on each issue.": "5. Court to state its decision on each issue.",
}

# Shared heading-detection pattern for both section and rule numbers. The
# title text after 'N. ' normally starts with an uppercase letter or a
# footnote-continuation '[', but defined-term provisions (e.g. '"Decree"
# defined.') start with a curly/smart quotation mark instead — U+201C for
# a double quote, U+2018 for a single quote — which would otherwise fail
# to match and silently drop the provision.
NUM_RX = re.compile(r"^(?:\d{1,2}\[)?(\d{1,3}-?[A-Z]{0,2})\.\s*((?:[A-Z\[\u201c\u2018]|\d\[).*)")


def clean_lines(lines):
    """Strip code-fence markers and IndiaCode/page-number watermark lines,
    while preserving all operative text and its original line order. Also
    applies KNOWN_LINE_CORRECTIONS for verified, individually-checked
    source corruptions (see comment above that table)."""
    out = []
    for ln in lines:
        stripped = ln.rstrip("\n")
        if any(p.match(stripped.strip()) for p in NOISE_LINE_RES):
            continue
        for bad, good in KNOWN_LINE_CORRECTIONS.items():
            if stripped.strip().startswith(bad):
                stripped = stripped.replace(bad, good, 1)
                break
        out.append(stripped)
    return out


def load_body(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        raw = f.readlines()
    return clean_lines(raw)


def find_all(lines, pattern):
    rx = re.compile(pattern)
    return [i for i, l in enumerate(lines) if rx.match(l.strip())]


def slice_join(lines, start, end):
    return "\n".join(lines[start:end]).strip()


FOOTNOTE_LEAD_RX = re.compile(
    r"^(Subs\.|Ins\.|Omitted|Rep\.|Added|Renumbered|The words|The word|Clause|"
    r"Sub-section|Sub-clause|For |See |Vide |Existing|Substituted by|Inserted|"
    r"Explanation|Proviso|Certain)",
)
# Amendment-citation lines in this document reliably contain one of these
# phrases regardless of their leading word (e.g. "Cls. (b)... omitted by
# s. 89, ibid, (w.e.f. 1-2-1977)." doesn't start with any word above, but
# still carries the citation boilerplate) — matching on these is a more
# robust signal than trying to enumerate every possible leading word.
FOOTNOTE_CITATION_RX = re.compile(
    r"\bibid\b|\(w\.e\.f\.|by Act \d+ of (?:17|18|19|20)\d{2}|by the A\.?O\.|"
    r"by the Adaptation of Laws",
    re.IGNORECASE,
)


def _heading_candidates(lines, start, end, num_rx):
    """Find lines that look like '<no>. <Capitalised text>' headings, then
    keep only a plausible monotonically-increasing subsequence — this drops
    footnote/amendment-note lines (e.g. '1. Subs. by Act 104 of 1976...')
    which share the same 'digit. word' shape but reset the numbering.

    A citation-style line (containing 'ibid', '(w.e.f.', etc.) is only
    treated as a footnote if the line immediately BEFORE it is confirmed as
    a footnote by its leading word (Ins./Subs./Rep./...) — i.e. it's the
    continuation of a citation cluster attached to a nearby rule. Checking
    only the preceding line (not the following one) matters: a genuinely
    repealed, terse provision (e.g. '48. [Execution barred in certain
    cases.] Rep. by the Limitation Act, 1963...') can legitimately be
    followed by an unrelated footnote block for other, earlier provisions
    — that trailing adjacency doesn't make the provision itself a footnote."""
    confirmed_footnote = set()
    for i in range(start, end):
        m = num_rx.match(lines[i].strip())
        if m and FOOTNOTE_LEAD_RX.match(m.group(2)):
            confirmed_footnote.add(i)

    raw_hits = []
    for i in range(start, end):
        m = num_rx.match(lines[i].strip())
        if not m:
            continue
        no, rest = m.group(1), m.group(2)
        no = no.replace("-", "")  # normalize e.g. '46-I' to '46I', matching
        # how every other letter-suffixed number in this document is styled
        if i in confirmed_footnote:
            continue
        if FOOTNOTE_CITATION_RX.search(rest) and (i - 1) in confirmed_footnote:
            continue
        numeric = int(re.match(r"\d+", no).group())
        raw_hits.append((i, no, numeric, rest.split(".")[0].strip()))

    kept = []
    last_numeric = 0
    for i, no, numeric, title_guess in raw_hits:
        if numeric < last_numeric or numeric > last_numeric + 15:
            continue
        kept.append((i, no, title_guess))
        last_numeric = numeric
    return kept


def parse_sections(lines, body_start, body_end):
    """Parse Sections 1-158 between body_start and body_end (exclusive)."""
    part_rx = re.compile(r"^PART\s+([IVXL]+)\s*$")

    parts_at = {}
    current_part = "PRELIMINARY"
    for i in range(body_start, body_end):
        m_part = part_rx.match(lines[i].strip())
        if m_part:
            current_part = m_part.group(1)
        parts_at[i] = current_part

    hits = _heading_candidates(lines, body_start, body_end, NUM_RX)
    sections = []
    for idx, (i, no, title_guess) in enumerate(hits):
        end = hits[idx + 1][0] if idx + 1 < len(hits) else body_end
        text = slice_join(lines, i, end)
        state_split = re.split(r"^STATE AMENDMENTS\s*$", text, flags=re.M, maxsplit=1)
        main_text = state_split[0].strip()
        state_text = state_split[1].strip() if len(state_split) > 1 else ""
        sections.append({
            "section_no": no,
            "title": title_guess,
            "part": parts_at.get(i, ""),
            "text": main_text,
            "state_amendments": state_text,
        })
    return sections


def parse_toc_orders(lines, toc_start, toc_end):
    """Ground truth: the sequence of Orders (55 entries, including the four
    amendment-inserted 'A' orders — XVI-A, XXA, XXVII-A, XXXIIA) as they
    appear in the source's own table-of-contents listing, together with the
    exact text of each order's first rule line. The operative full-text
    section is missing the 'ORDER <no>' heading line for 5 of these 55
    orders (a source-conversion gap, not a numbering irregularity) — their
    rules exist in the operative text but with no boundary marker. The
    first-rule text is the anchor used to locate them there."""
    order_rx = re.compile(r"^ORDER\s+([IVXLA0-9\-]+)\s*$")
    rule_rx = re.compile(r"^(\d{1,3}[A-Z]{0,2})\.\s+(.+)$")
    noise = {"IndiaCode", "RULES"}
    hits = [(i, order_rx.match(lines[i].strip()).group(1)) for i in range(toc_start, toc_end) if order_rx.match(lines[i].strip())]

    toc = []
    for idx, (i, no) in enumerate(hits):
        end = hits[idx + 1][0] if idx + 1 < len(hits) else toc_end
        title_lines, first_rule = [], None
        for j in range(i + 1, end):
            s = lines[j].strip()
            if not s or s in noise or s.isdigit():
                continue
            if rule_rx.match(s):
                first_rule = s
                break
            title_lines.append(s)
        toc.append({"order_no": no, "title": " ".join(title_lines), "first_rule": first_rule})
    return toc


def locate_order_boundaries(lines, sched_start, sched_end, toc_orders):
    """For each of the 55 orders in the ToC, find where it actually starts in
    the operative body: at its own 'ORDER <no>' heading if one exists there,
    or — for the 5 that don't — at the exact line where its first rule's
    text begins, using the ToC's short rule title as a prefix match against
    the operative body's full rule text (which starts identically before
    continuing into the substantive text after the em-dash)."""
    order_rx = re.compile(r"^ORDER\s+([IVXLA0-9\-]+)\s*$")
    explicit = {}
    for i in range(sched_start, sched_end):
        m = order_rx.match(lines[i].strip())
        if m and m.group(1) not in explicit:
            explicit[m.group(1)] = i

    boundaries = []
    for entry in toc_orders:
        no = entry["order_no"]
        if no in explicit:
            boundaries.append({"line": explicit[no], "order_no": no, "title": None, "explicit": True})
        elif entry["first_rule"]:
            found = next((i for i in range(sched_start, sched_end) if lines[i].strip().startswith(entry["first_rule"])), None)
            if found is not None:
                boundaries.append({"line": found, "order_no": no, "title": entry["title"], "explicit": False})
            else:
                print(f"WARNING: Order {no} not found in operative body even by first-rule text — provision may be genuinely absent from this source, verify manually.")
        else:
            print(f"WARNING: Order {no} has no ToC first-rule anchor to locate it by — skipped.")
    boundaries.sort(key=lambda b: b["line"])
    return boundaries


def parse_orders(lines, sched_start, sched_end, toc_orders):
    """Parse all Orders and their Rules from the First Schedule region,
    using ToC-derived boundaries so orders whose heading line is missing
    from the operative body (see locate_order_boundaries) are still
    correctly separated from their neighbors instead of having their rules
    silently absorbed into the preceding order."""
    boundaries = locate_order_boundaries(lines, sched_start, sched_end, toc_orders)

    orders = []
    for bi, b in enumerate(boundaries):
        seg_end = boundaries[bi + 1]["line"] if bi + 1 < len(boundaries) else sched_end

        if b["explicit"]:
            i = b["line"]
            j = i + 1
            while j < seg_end and not lines[j].strip():
                j += 1
            title = lines[j].strip() if j < seg_end else ""
            rules_start = j + 1
        else:
            # No heading line in the source; the boundary IS the first rule's
            # own start, and the title comes from the ToC instead.
            title = b["title"]
            rules_start = b["line"]

        rule_hits = _heading_candidates(lines, rules_start, seg_end, NUM_RX)
        rules = []
        for ri, (k, rno, rtitle) in enumerate(rule_hits):
            rend = rule_hits[ri + 1][0] if ri + 1 < len(rule_hits) else seg_end
            rtext = slice_join(lines, k, rend)
            state_split = re.split(r"^STATE AMENDMENTS\s*$", rtext, flags=re.M, maxsplit=1)
            main_text = state_split[0].strip()
            state_text = state_split[1].strip() if len(state_split) > 1 else ""
            rules.append({
                "rule_no": rno,
                "title": rtitle,
                "text": main_text,
                "state_amendments": state_text,
            })

        orders.append({"order_no": b["order_no"], "title": title, "rules": rules})
    return orders


def parse_appendices(lines, app_start, app_end):
    app_rx = re.compile(r"^APPENDIX[\s\-–—]*([A-Z])\b")
    hits = []
    for i in range(app_start, app_end):
        m = app_rx.match(lines[i].strip())
        if m:
            hits.append((i, m.group(1)))
    appendices = []
    for idx, (i, letter) in enumerate(hits):
        end = hits[idx + 1][0] if idx + 1 < len(hits) else app_end
        text = slice_join(lines, i, end)
        appendices.append({"letter": letter, "text": text})
    return appendices


def build_schema(conn):
    conn.executescript("""
    DROP TABLE IF EXISTS sections;
    DROP TABLE IF EXISTS orders;
    DROP TABLE IF EXISTS rules;
    DROP TABLE IF EXISTS appendices;
    DROP TABLE IF EXISTS bookmarks;
    DROP TABLE IF EXISTS notes;
    DROP TABLE IF EXISTS search_index;
    DROP TABLE IF EXISTS limitation_sections;
    DROP TABLE IF EXISTS limitation_articles;

    CREATE TABLE sections (
        id INTEGER PRIMARY KEY,
        section_no TEXT NOT NULL,
        title TEXT,
        part TEXT,
        text TEXT,
        state_amendments TEXT
    );
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        order_no TEXT NOT NULL,
        title TEXT
    );
    CREATE TABLE rules (
        id INTEGER PRIMARY KEY,
        order_id INTEGER NOT NULL REFERENCES orders(id),
        rule_no TEXT NOT NULL,
        title TEXT,
        text TEXT,
        state_amendments TEXT
    );
    CREATE TABLE appendices (
        id INTEGER PRIMARY KEY,
        letter TEXT NOT NULL,
        text TEXT
    );
    CREATE TABLE limitation_sections (
        id INTEGER PRIMARY KEY,
        section_no TEXT NOT NULL,
        title TEXT NOT NULL,
        part TEXT NOT NULL,
        text TEXT NOT NULL
    );
    CREATE TABLE limitation_articles (
        id INTEGER PRIMARY KEY,
        article_no TEXT NOT NULL,
        division TEXT NOT NULL,
        part TEXT NOT NULL,
        description TEXT NOT NULL,
        period TEXT NOT NULL,
        time_begins TEXT NOT NULL,
        cpc_ref TEXT
    );
    CREATE TABLE bookmarks (
        id INTEGER PRIMARY KEY,
        kind TEXT NOT NULL,
        ref_id INTEGER NOT NULL,
        UNIQUE(kind, ref_id)
    );
    CREATE TABLE notes (
        id INTEGER PRIMARY KEY,
        kind TEXT NOT NULL,
        ref_id INTEGER NOT NULL,
        text TEXT NOT NULL DEFAULT '',
        updated_at TEXT DEFAULT (datetime('now')),
        UNIQUE(kind, ref_id)
    );

    CREATE VIRTUAL TABLE search_index USING fts5(
        kind, ref_id UNINDEXED, label, body
    );
    """)
    conn.commit()


def main():
    lines = load_body(SRC)
    n = len(lines)
    print(f"Loaded {n} cleaned lines")

    sec1_idx = [i for i in range(n) if lines[i].strip().startswith("1. Short title")]
    body_start = sec1_idx[-1]
    sched_marker_idx = [i for i in range(n) if lines[i].strip() == "THE FIRST SCHEDULE"]
    sched_start = sched_marker_idx[-1]
    body_end = sched_start
    appx_marker_idx = [i for i in range(n) if lines[i].strip().startswith("APPENDIX A") and "PLEADINGS" not in lines[i]]
    appx_start = appx_marker_idx[-1] if appx_marker_idx else sched_start
    sched_end = appx_start
    appx_end_candidates = [i for i in range(n) if "SECOND SCHEDULE" in lines[i]]
    appx_end = appx_end_candidates[-1] if appx_end_candidates else n

    print(f"body: {body_start}-{body_end} | schedule: {sched_start}-{sched_end} | appendices: {appx_start}-{appx_end}")

    sections = parse_sections(lines, body_start, body_end)
    toc_orders = parse_toc_orders(lines, 300, sched_start)
    orders = parse_orders(lines, sched_start, sched_end, toc_orders)
    appendices = parse_appendices(lines, appx_start, appx_end)

    total_rules = sum(len(o["rules"]) for o in orders)
    print(f"Parsed {len(sections)} sections, {len(orders)} orders, {total_rules} rules, {len(appendices)} appendices")

    expected_orders = {e["order_no"] for e in toc_orders}
    found_orders = {o["order_no"] for o in orders}
    missing = expected_orders - found_orders
    if missing:
        print(f"WARNING: {len(missing)} order(s) from the ToC were not parsed: {sorted(missing)}")
    else:
        print(f"Completeness check passed: all {len(expected_orders)} orders from the ToC are present.")
    if len(orders) != len(toc_orders):
        print(f"WARNING: order count mismatch — ToC has {len(toc_orders)}, parsed {len(orders)}.")

    conn = sqlite3.connect(DB_PATH)
    build_schema(conn)
    cur = conn.cursor()

    for s in sections:
        cur.execute(
            "INSERT INTO sections (section_no, title, part, text, state_amendments) VALUES (?,?,?,?,?)",
            (s["section_no"], s["title"], s["part"], s["text"], s["state_amendments"]),
        )
        sid = cur.lastrowid
        cur.execute(
            "INSERT INTO search_index (kind, ref_id, label, body) VALUES (?,?,?,?)",
            ("section", sid, f"Section {s['section_no']}. {s['title']}", s["text"]),
        )

    for o in orders:
        cur.execute("INSERT INTO orders (order_no, title) VALUES (?,?)", (o["order_no"], o["title"]))
        oid = cur.lastrowid
        for r in o["rules"]:
            cur.execute(
                "INSERT INTO rules (order_id, rule_no, title, text, state_amendments) VALUES (?,?,?,?,?)",
                (oid, r["rule_no"], r["title"], r["text"], r["state_amendments"]),
            )
            rid = cur.lastrowid
            cur.execute(
                "INSERT INTO search_index (kind, ref_id, label, body) VALUES (?,?,?,?)",
                ("rule", rid, f"Order {o['order_no']}, Rule {r['rule_no']}. {r['title']}", r["text"]),
            )

    for a in appendices:
        cur.execute("INSERT INTO appendices (letter, text) VALUES (?,?)", (a["letter"], a["text"]))
        aid = cur.lastrowid
        cur.execute(
            "INSERT INTO search_index (kind, ref_id, label, body) VALUES (?,?,?,?)",
            ("appendix", aid, f"Appendix {a['letter']}", a["text"]),
        )

    try:
        import limitation_data as ld
        for s in ld.LIMITATION_SECTIONS:
            cur.execute(
                "INSERT INTO limitation_sections (section_no, title, part, text) VALUES (?,?,?,?)",
                (s["section_no"], s["title"], s["part"], s["text"]),
            )
            sid = cur.lastrowid
            cur.execute(
                "INSERT INTO search_index (kind, ref_id, label, body) VALUES (?,?,?,?)",
                ("limitation_section", sid, f"Limitation Act S.{s['section_no']} — {s['title']}", f"{s['title']}\n{s['text']}"),
            )

        for a in ld.LIMITATION_ARTICLES:
            cur.execute(
                """INSERT INTO limitation_articles 
                   (article_no, division, part, description, period, time_begins, cpc_ref)
                   VALUES (?,?,?,?,?,?,?)""",
                (a["article_no"], a["division"], a["part"], a["description"], a["period"], a["time_begins"], a["cpc_ref"]),
            )
            aid = cur.lastrowid
            cur.execute(
                "INSERT INTO search_index (kind, ref_id, label, body) VALUES (?,?,?,?)",
                ("limitation_article", aid, f"Limitation Article {a['article_no']} ({a['period']})",
                 f"{a['description']}\nPeriod: {a['period']}\nTime from which period begins: {a['time_begins']}\nCPC Reference: {a['cpc_ref'] or ''}"),
            )
        print(f"Populated {len(ld.LIMITATION_SECTIONS)} Limitation Act sections & {len(ld.LIMITATION_ARTICLES)} articles.")
    except ImportError:
        print("Note: limitation_data not found, skipping Limitation Act population.")

    conn.commit()
    conn.close()
    print("Database built:", DB_PATH)


if __name__ == "__main__":
    main()
