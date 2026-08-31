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


def clean_lines(lines):
    """Strip code-fence markers and IndiaCode/page-number watermark lines,
    while preserving all operative text and its original line order."""
    out = []
    for ln in lines:
        stripped = ln.rstrip("\n")
        if any(p.match(stripped.strip()) for p in NOISE_LINE_RES):
            continue
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
    r"Sub-section|Sub-clause|For |See |Vide |Existing|Substituted|Inserted|"
    r"Explanation|Proviso|Certain)",
)


def _heading_candidates(lines, start, end, num_rx):
    """Find lines that look like '<no>. <Capitalised text>' headings, then
    keep only a plausible monotonically-increasing subsequence — this drops
    footnote/amendment-note lines (e.g. '1. Subs. by Act 104 of 1976...')
    which share the same 'digit. word' shape but reset the numbering."""
    raw_hits = []
    for i in range(start, end):
        m = num_rx.match(lines[i].strip())
        if not m:
            continue
        no, rest = m.group(1), m.group(2)
        if FOOTNOTE_LEAD_RX.match(rest):
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
    # Handles a leading footnote-citation marker like '4[25. Power ...'
    num_rx = re.compile(r"^(?:\d{1,2}\[)?(\d{1,3}[A-Z]{0,2})\.\s+([A-Z\[].*)")
    part_rx = re.compile(r"^PART\s+([IVXL]+)\s*$")

    parts_at = {}
    current_part = "PRELIMINARY"
    for i in range(body_start, body_end):
        m_part = part_rx.match(lines[i].strip())
        if m_part:
            current_part = m_part.group(1)
        parts_at[i] = current_part

    hits = _heading_candidates(lines, body_start, body_end, num_rx)
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


def parse_orders(lines, sched_start, sched_end):
    """Parse Orders I-LI and their Rules from the First Schedule region."""
    order_rx = re.compile(r"^ORDER\s+([IVXLA0-9]+)\s*$")
    num_rx = re.compile(r"^(?:\d{1,2}\[)?(\d{1,3}[A-Z]{0,2})\.\s+([A-Z\[].*)")
    order_hits = find_all(lines, r"^ORDER\s+[IVXLA0-9]+\s*$")
    order_hits = [i for i in order_hits if sched_start <= i < sched_end]

    orders = []
    for oi, i in enumerate(order_hits):
        order_no = order_rx.match(lines[i].strip()).group(1)
        # Title is usually the next non-empty line
        j = i + 1
        while j < sched_end and not lines[j].strip():
            j += 1
        title = lines[j].strip() if j < sched_end else ""
        order_end = order_hits[oi + 1] if oi + 1 < len(order_hits) else sched_end

        rule_hits = _heading_candidates(lines, j + 1, order_end, num_rx)

        rules = []
        for ri, (k, rno, rtitle) in enumerate(rule_hits):
            rend = rule_hits[ri + 1][0] if ri + 1 < len(rule_hits) else order_end
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

        orders.append({
            "order_no": order_no,
            "title": title,
            "rules": rules,
        })
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
        kind, ref_id UNINDEXED, label, body, content=''
    );
    """)
    conn.commit()


def main():
    lines = load_body(SRC)
    n = len(lines)
    print(f"Loaded {n} cleaned lines")

    # Boundaries established from structural markers in the source.
    # Each marker appears once in the front-matter table of contents and
    # once at the actual operative heading further down — take the last
    # (operative) occurrence in each case.
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
    orders = parse_orders(lines, sched_start, sched_end)
    appendices = parse_appendices(lines, appx_start, appx_end)

    total_rules = sum(len(o["rules"]) for o in orders)
    print(f"Parsed {len(sections)} sections, {len(orders)} orders, {total_rules} rules, {len(appendices)} appendices")

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

    conn.commit()
    conn.close()
    print("Database built:", DB_PATH)


if __name__ == "__main__":
    main()
