"""
Populates limitation_sections, limitation_articles, and rebuilds search_index with full column storage in cpc_1908.db.
"""
import sqlite3
import os
import sys
import limitation_data as ld

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cpc_1908.db")

def migrate():
    print(f"Opening database: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. Create Limitation tables
    cur.execute("DROP TABLE IF EXISTS limitation_sections")
    cur.execute("DROP TABLE IF EXISTS limitation_articles")
    
    cur.execute("""
        CREATE TABLE limitation_sections (
            id INTEGER PRIMARY KEY,
            section_no TEXT NOT NULL,
            title TEXT NOT NULL,
            part TEXT NOT NULL,
            text TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE limitation_articles (
            id INTEGER PRIMARY KEY,
            article_no TEXT NOT NULL,
            division TEXT NOT NULL,
            part TEXT NOT NULL,
            description TEXT NOT NULL,
            period TEXT NOT NULL,
            time_begins TEXT NOT NULL,
            cpc_ref TEXT
        )
    """)

    # 2. Insert sections
    for s in ld.LIMITATION_SECTIONS:
        cur.execute(
            "INSERT INTO limitation_sections (section_no, title, part, text) VALUES (?,?,?,?)",
            (s["section_no"], s["title"], s["part"], s["text"])
        )
    print(f"Inserted {len(ld.LIMITATION_SECTIONS)} Limitation Act sections.")

    # 3. Insert articles
    for a in ld.LIMITATION_ARTICLES:
        cur.execute(
            """INSERT INTO limitation_articles 
               (article_no, division, part, description, period, time_begins, cpc_ref)
               VALUES (?,?,?,?,?,?,?)""",
            (a["article_no"], a["division"], a["part"], a["description"], a["period"], a["time_begins"], a["cpc_ref"])
        )
    print(f"Inserted {len(ld.LIMITATION_ARTICLES)} Limitation Act articles.")

    # 4. Rebuild full FTS search_index with full content support
    cur.execute("DROP TABLE IF EXISTS search_index")
    cur.execute("CREATE VIRTUAL TABLE search_index USING fts5(kind, ref_id UNINDEXED, label, body)")

    # Index CPC sections
    cur.execute("SELECT id, section_no, title, text FROM sections")
    for row in cur.fetchall():
        cur.execute(
            "INSERT INTO search_index (kind, ref_id, label, body) VALUES (?,?,?,?)",
            ("section", row[0], f"Section {row[1]}. {row[2]}", row[3])
        )

    # Index CPC rules
    cur.execute("""
        SELECT r.id, o.order_no, r.rule_no, r.title, r.text 
        FROM rules r JOIN orders o ON r.order_id = o.id
    """)
    for row in cur.fetchall():
        cur.execute(
            "INSERT INTO search_index (kind, ref_id, label, body) VALUES (?,?,?,?)",
            ("rule", row[0], f"Order {row[1]}, Rule {row[2]}. {row[3]}", row[4])
        )

    # Index CPC appendices
    cur.execute("SELECT id, letter, text FROM appendices")
    for row in cur.fetchall():
        cur.execute(
            "INSERT INTO search_index (kind, ref_id, label, body) VALUES (?,?,?,?)",
            ("appendix", row[0], f"Appendix {row[1]}", row[2])
        )

    # Index Limitation Sections
    cur.execute("SELECT id, section_no, title, text FROM limitation_sections")
    for row in cur.fetchall():
        cur.execute(
            "INSERT INTO search_index (kind, ref_id, label, body) VALUES (?,?,?,?)",
            ("limitation_section", row[0], f"Limitation Act S.{row[1]} — {row[2]}", f"{row[2]}\n{row[3]}")
        )

    # Index Limitation Articles
    cur.execute("SELECT id, article_no, period, description, time_begins, cpc_ref FROM limitation_articles")
    for row in cur.fetchall():
        cur.execute(
            "INSERT INTO search_index (kind, ref_id, label, body) VALUES (?,?,?,?)",
            ("limitation_article", row[0], f"Limitation Article {row[1]} ({row[2]})",
             f"{row[3]}\nPeriod: {row[2]}\nTime from which period begins: {row[4]}\nCPC Reference: {row[5] or ''}")
        )

    conn.commit()
    print("Database updated and unified FTS search index built successfully!")
    conn.close()

if __name__ == "__main__":
    migrate()
