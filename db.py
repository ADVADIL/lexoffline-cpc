import sqlite3
import os
import sys


def _resource_dir():
    """Directory to look for bundled resources (the database) in — the
    PyInstaller-extraction directory when running as a frozen executable,
    or this file's own directory when running from source. Using plain
    __file__-based resolution unconditionally is a well-known PyInstaller
    gotcha: it works fine in development but can silently fail to locate
    bundled data once packaged, since a frozen app's modules don't always
    resolve __file__ the same way source files do."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


DB_PATH = os.path.join(_resource_dir(), "cpc_1908.db")


class ActDatabase:
    def __init__(self, path=DB_PATH):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self._ensure_user_tables()

    def _ensure_user_tables(self):
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS bookmarks (
                id INTEGER PRIMARY KEY,
                kind TEXT NOT NULL,
                ref_id INTEGER NOT NULL,
                UNIQUE(kind, ref_id)
            );
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                kind TEXT NOT NULL,
                ref_id INTEGER NOT NULL,
                text TEXT NOT NULL DEFAULT '',
                updated_at TEXT DEFAULT (datetime('now')),
                UNIQUE(kind, ref_id)
            );
            CREATE TABLE IF NOT EXISTS case_diary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                case_no TEXT NOT NULL,
                court_name TEXT NOT NULL,
                client_name TEXT NOT NULL,
                client_role TEXT NOT NULL DEFAULT 'Plaintiff',
                opposite_party TEXT NOT NULL DEFAULT '',
                opposite_counsel TEXT NOT NULL DEFAULT '',
                stage TEXT NOT NULL,
                next_date TEXT NOT NULL DEFAULT '',
                notes TEXT NOT NULL DEFAULT '',
                created_at TEXT DEFAULT (datetime('now'))
            );
            CREATE TABLE IF NOT EXISTS case_hearings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                case_id INTEGER NOT NULL,
                hearing_date TEXT NOT NULL,
                business_done TEXT NOT NULL DEFAULT '',
                next_date TEXT NOT NULL DEFAULT '',
                next_purpose TEXT NOT NULL DEFAULT '',
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (case_id) REFERENCES case_diary(id) ON DELETE CASCADE
            );
            """
        )
        self.conn.commit()

    # ---------- sections ----------
    def sections_by_part(self):
        rows = self.conn.execute(
            "SELECT id, section_no, title, part FROM sections ORDER BY id"
        ).fetchall()
        parts = {}
        for r in rows:
            parts.setdefault(r["part"] or "OTHER", []).append(r)
        return parts

    def get_section(self, section_id):
        return self.conn.execute("SELECT * FROM sections WHERE id=?", (section_id,)).fetchone()

    def get_section_by_no(self, section_no):
        return self.conn.execute(
            "SELECT * FROM sections WHERE section_no=? ORDER BY id LIMIT 1", (section_no,)
        ).fetchone()

    # ---------- orders / rules ----------
    def all_orders(self):
        return self.conn.execute("SELECT * FROM orders ORDER BY id").fetchall()

    def rules_for_order(self, order_id):
        return self.conn.execute(
            "SELECT * FROM rules WHERE order_id=? ORDER BY id", (order_id,)
        ).fetchall()

    def get_rule(self, rule_id):
        return self.conn.execute("SELECT * FROM rules WHERE id=?", (rule_id,)).fetchone()

    def get_order(self, order_id):
        return self.conn.execute("SELECT * FROM orders WHERE id=?", (order_id,)).fetchone()

    def find_order_by_no(self, order_no):
        return self.conn.execute(
            "SELECT * FROM orders WHERE order_no=? ORDER BY id LIMIT 1", (order_no,)
        ).fetchone()

    def find_rule_in_order(self, order_no, rule_no):
        return self.conn.execute(
            """SELECT r.* FROM rules r JOIN orders o ON r.order_id=o.id
               WHERE o.order_no=? AND r.rule_no=? ORDER BY r.id LIMIT 1""",
            (order_no, rule_no),
        ).fetchone()

    # ---------- appendices ----------
    def all_appendices(self):
        return self.conn.execute("SELECT * FROM appendices ORDER BY id").fetchall()

    def get_appendix(self, appendix_id):
        return self.conn.execute("SELECT * FROM appendices WHERE id=?", (appendix_id,)).fetchone()

    # ---------- search ----------
    @staticmethod
    def _int_to_roman(n: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        for i in range(len(val)):
            while n >= val[i]:
                roman += syb[i]
                n -= val[i]
        return roman

    def _parse_advocate_query(self, query: str):
        import re
        pinned = []
        q = query.strip()

        # 1. Order and Rule: e.g. "Order 39 Rule 1", "O.39 R.1", "O 39 R 1", "Order XXXIX Rule 1"
        m_or = re.search(r'(?i)\b(?:order|o)\.?\s*([ivxldcm]+|\d+)\s*(?:rule|r)\.?\s*(\d+[a-z]?)', q)
        if m_or:
            raw_order, rule_no = m_or.group(1), m_or.group(2)
            order_roman = raw_order.upper() if re.match(r'^[ivxldcm]+$', raw_order, re.I) else self._int_to_roman(int(raw_order))
            rule_row = self.conn.execute(
                """SELECT r.id, r.rule_no, r.title, o.order_no 
                   FROM rules r JOIN orders o ON r.order_id=o.id 
                   WHERE o.order_no=? AND r.rule_no=? LIMIT 1""",
                (order_roman, rule_no)
            ).fetchone()
            if rule_row:
                pinned.append({
                    "kind": "rule",
                    "ref_id": rule_row["id"],
                    "label": f"Order {rule_row['order_no']}, Rule {rule_row['rule_no']}. {rule_row['title']}",
                    "snip": f"Direct Citation Match: Order {rule_row['order_no']} Rule {rule_row['rule_no']}"
                })

        # 2. Section: e.g. "Section 16(c)", "16(c)", "Section 100", "S.100", "SRA Section 16"
        m_sec = re.search(r'(?i)\b(?:sra\s*)?(?:section|sec|s)\.?\s*(\d+[a-z]?)(?:\s*\(([a-z0-9]+)\))?', q)
        if not m_sec and re.match(r'^\d+[a-z]?(?:\s*\([a-z0-9]+\))?$', q, re.I):
            m_sec = re.search(r'^(\d+[a-z]?)(?:\s*\(([a-z0-9]+)\))?', q)

        if m_sec:
            s_no = m_sec.group(1)
            if "sra" in q.lower():
                sra_row = self.conn.execute("SELECT id, section_no, title FROM sra_sections WHERE section_no=? LIMIT 1", (s_no,)).fetchone()
                if sra_row:
                    pinned.append({
                        "kind": "sra_section",
                        "ref_id": sra_row["id"],
                        "label": f"SRA Section {sra_row['section_no']}. {sra_row['title']}",
                        "snip": f"Specific Relief Act, 1963 — Section {sra_row['section_no']}"
                    })
            else:
                sec_row = self.conn.execute("SELECT id, section_no, title FROM sections WHERE section_no=? LIMIT 1", (s_no,)).fetchone()
                if sec_row:
                    pinned.append({
                        "kind": "section",
                        "ref_id": sec_row["id"],
                        "label": f"Section {sec_row['section_no']}. {sec_row['title']}",
                        "snip": f"Code of Civil Procedure, 1908 — Section {sec_row['section_no']}"
                    })
                sra_row = self.conn.execute("SELECT id, section_no, title FROM sra_sections WHERE section_no=? LIMIT 1", (s_no,)).fetchone()
                if sra_row:
                    pinned.append({
                        "kind": "sra_section",
                        "ref_id": sra_row["id"],
                        "label": f"SRA Section {sra_row['section_no']}. {sra_row['title']}",
                        "snip": f"Specific Relief Act, 1963 — Section {sra_row['section_no']}"
                    })

        # 3. Article: e.g. "Article 54", "Art. 54", "Art 136"
        m_art = re.search(r'(?i)\b(?:article|art)\.?\s*(\d+)', q)
        if m_art:
            art_no = m_art.group(1)
            art_row = self.conn.execute("SELECT id, article_no, period, description FROM limitation_articles WHERE article_no=? LIMIT 1", (art_no,)).fetchone()
            if art_row:
                pinned.append({
                    "kind": "limitation_article",
                    "ref_id": art_row["id"],
                    "label": f"Limitation Article {art_row['article_no']} ({art_row['period']})",
                    "snip": f"{art_row['description'][:120]}"
                })

        return pinned

    def search(self, query, limit=60):
        import re
        q = query.strip()
        if not q:
            return []

        pinned = self._parse_advocate_query(q)
        pinned_keys = {(p["kind"], p["ref_id"]) for p in pinned}

        fts_results = []
        # Clean query tokens for FTS5: strip parentheses, quotes, punctuation
        tokens = [re.sub(r'[^a-zA-Z0-9]', '', t) for t in re.split(r'[\s(),;:]+', q) if t]
        tokens = [t for t in tokens if t]

        if tokens:
            fts_q = ' '.join(f'"{t}"*' for t in tokens)
            try:
                rows = self.conn.execute(
                    """SELECT kind, ref_id, label,
                              snippet(search_index, 3, '[', ']', ' ... ', 12) AS snip
                       FROM search_index WHERE search_index MATCH ? LIMIT ?""",
                    (fts_q, limit),
                ).fetchall()
                fts_results = [dict(r) for r in rows]
            except sqlite3.OperationalError:
                pass

        if not fts_results:
            like = f"%{q}%"
            rows = self.conn.execute(
                """SELECT kind, ref_id, label, substr(body,1,150) AS snip
                   FROM search_index WHERE label LIKE ? OR body LIKE ? LIMIT ?""",
                (like, like, limit),
            ).fetchall()
            fts_results = [dict(r) for r in rows]

        # Merge pinned items at top without duplicate
        combined = list(pinned)
        for r in fts_results:
            if (r["kind"], r["ref_id"]) not in pinned_keys:
                combined.append(r)
                if len(combined) >= limit:
                    break

        return combined

    # ---------- bookmarks ----------
    def is_bookmarked(self, kind, ref_id):
        r = self.conn.execute(
            "SELECT 1 FROM bookmarks WHERE kind=? AND ref_id=?", (kind, ref_id)
        ).fetchone()
        return r is not None

    def toggle_bookmark(self, kind, ref_id):
        if self.is_bookmarked(kind, ref_id):
            self.conn.execute("DELETE FROM bookmarks WHERE kind=? AND ref_id=?", (kind, ref_id))
        else:
            self.conn.execute(
                "INSERT OR IGNORE INTO bookmarks (kind, ref_id) VALUES (?,?)", (kind, ref_id)
            )
        self.conn.commit()

    def all_bookmarks(self):
        return self.conn.execute("SELECT * FROM bookmarks ORDER BY id").fetchall()

    # ---------- notes ----------
    def get_note(self, kind, ref_id):
        r = self.conn.execute(
            "SELECT text FROM notes WHERE kind=? AND ref_id=?", (kind, ref_id)
        ).fetchone()
        return r["text"] if r else ""

    def save_note(self, kind, ref_id, text):
        self.conn.execute(
            """INSERT INTO notes (kind, ref_id, text, updated_at) VALUES (?,?,?,datetime('now'))
               ON CONFLICT(kind, ref_id) DO UPDATE SET text=excluded.text, updated_at=datetime('now')""",
            (kind, ref_id, text),
        )
        self.conn.commit()

    # ---------- Limitation Act 1963 ----------
    def limitation_sections_by_part(self):
        rows = self.conn.execute(
            "SELECT id, section_no, title, part FROM limitation_sections ORDER BY id"
        ).fetchall()
        parts = {}
        for r in rows:
            parts.setdefault(r["part"] or "OTHER", []).append(r)
        return parts

    def get_limitation_section(self, section_id):
        return self.conn.execute(
            "SELECT * FROM limitation_sections WHERE id=?", (section_id,)
        ).fetchone()

    def get_limitation_section_by_no(self, section_no):
        return self.conn.execute(
            "SELECT * FROM limitation_sections WHERE section_no=? ORDER BY id LIMIT 1", (str(section_no),)
        ).fetchone()

    def limitation_articles_by_division(self):
        rows = self.conn.execute(
            "SELECT id, article_no, division, part, description, period, time_begins, cpc_ref FROM limitation_articles ORDER BY id"
        ).fetchall()
        divs = {}
        for r in rows:
            div = r["division"] or "OTHER"
            pt = r["part"] or "OTHER"
            divs.setdefault(div, {}).setdefault(pt, []).append(r)
        return divs

    def get_limitation_article(self, article_id):
        return self.conn.execute(
            "SELECT * FROM limitation_articles WHERE id=?", (article_id,)
        ).fetchone()

    def find_article_by_no(self, article_no):
        return self.conn.execute(
            "SELECT * FROM limitation_articles WHERE article_no=? ORDER BY id LIMIT 1", (str(article_no),)
        ).fetchone()

    def find_articles_for_cpc(self, search_term):
        like = f"%{search_term}%"
        return self.conn.execute(
            "SELECT * FROM limitation_articles WHERE cpc_ref LIKE ? ORDER BY id", (like,)
        ).fetchall()

    # ---------- The Specific Relief Act, 1963 ----------
    def sra_sections_by_part(self):
        from collections import OrderedDict
        rows = self.conn.execute(
            "SELECT id, section_no, title, part, chapter FROM sra_sections ORDER BY id"
        ).fetchall()
        parts = OrderedDict()
        for r in rows:
            p = r["part"] or "OTHER"
            parts.setdefault(p, []).append(r)
        return parts

    def get_sra_section(self, section_id):
        return self.conn.execute(
            "SELECT * FROM sra_sections WHERE id=?", (section_id,)
        ).fetchone()

    def get_sra_section_by_no(self, section_no):
        return self.conn.execute(
            "SELECT * FROM sra_sections WHERE section_no=? ORDER BY id LIMIT 1", (str(section_no),)
        ).fetchone()

    def all_sra_sections(self):
        return self.conn.execute("SELECT * FROM sra_sections ORDER BY id").fetchall()

    # ---------- case diary ----------
    def add_case(self, case_no, court_name, client_name, client_role="Plaintiff",
                 opposite_party="", opposite_counsel="", stage="", next_date="", notes=""):
        cur = self.conn.execute(
            """
            INSERT INTO case_diary (case_no, court_name, client_name, client_role,
                                    opposite_party, opposite_counsel, stage, next_date, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (case_no, court_name, client_name, client_role,
             opposite_party, opposite_counsel, stage, next_date, notes)
        )
        self.conn.commit()
        return cur.lastrowid

    def update_case(self, case_id, case_no, court_name, client_name, client_role,
                    opposite_party, opposite_counsel, stage, next_date, notes):
        self.conn.execute(
            """
            UPDATE case_diary
            SET case_no=?, court_name=?, client_name=?, client_role=?,
                opposite_party=?, opposite_counsel=?, stage=?, next_date=?, notes=?
            WHERE id=?
            """,
            (case_no, court_name, client_name, client_role,
             opposite_party, opposite_counsel, stage, next_date, notes, case_id)
        )
        self.conn.commit()

    def delete_case(self, case_id):
        self.conn.execute("DELETE FROM case_hearings WHERE case_id=?", (case_id,))
        self.conn.execute("DELETE FROM case_diary WHERE id=?", (case_id,))
        self.conn.commit()

    def get_case(self, case_id):
        return self.conn.execute("SELECT * FROM case_diary WHERE id=?", (case_id,)).fetchone()

    def all_cases(self, stage=None):
        if stage:
            return self.conn.execute(
                "SELECT * FROM case_diary WHERE stage=? ORDER BY next_date ASC, id DESC", (stage,)
            ).fetchall()
        return self.conn.execute("SELECT * FROM case_diary ORDER BY next_date ASC, id DESC").fetchall()

    def upcoming_cases(self, limit=20):
        return self.conn.execute(
            "SELECT * FROM case_diary WHERE next_date != '' AND next_date >= date('now') ORDER BY next_date ASC LIMIT ?",
            (limit,)
        ).fetchall()

    def add_hearing(self, case_id, hearing_date, business_done="", next_date="", next_purpose=""):
        cur = self.conn.execute(
            """
            INSERT INTO case_hearings (case_id, hearing_date, business_done, next_date, next_purpose)
            VALUES (?, ?, ?, ?, ?)
            """,
            (case_id, hearing_date, business_done, next_date, next_purpose)
        )
        if next_date:
            self.conn.execute("UPDATE case_diary SET next_date=? WHERE id=?", (next_date, case_id))
        self.conn.commit()
        return cur.lastrowid

    def hearings_for_case(self, case_id):
        return self.conn.execute(
            "SELECT * FROM case_hearings WHERE case_id=? ORDER BY hearing_date DESC, id DESC", (case_id,)
        ).fetchall()

    def close(self):
        self.conn.close()

