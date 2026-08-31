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
    def search(self, query, limit=60):
        if not query.strip():
            return []
        try:
            return self.conn.execute(
                """SELECT kind, ref_id, label,
                          snippet(search_index, 3, '[', ']', ' ... ', 12) AS snip
                   FROM search_index WHERE search_index MATCH ? LIMIT ?""",
                (query + "*", limit),
            ).fetchall()
        except sqlite3.OperationalError:
            like = f"%{query}%"
            return self.conn.execute(
                """SELECT kind, ref_id, label, substr(body,1,150) AS snip
                   FROM search_index WHERE label LIKE ? OR body LIKE ? LIMIT ?""",
                (like, like, limit),
            ).fetchall()

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

    def close(self):
        self.conn.close()
