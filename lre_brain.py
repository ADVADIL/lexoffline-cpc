"""
LexOffline — Deterministic Legal Reasoning Engine (LRE)
Module 1: Case Brain & Matter Store (lre_brain.py)

Provides persistent, offline SQLite storage for matters, case metadata,
chronological events, documents, and historical audit snapshots.
Completely deterministic; zero external API or LLM dependency.
"""

import os
import json
import sqlite3
from datetime import datetime, date

DB_PATH = os.path.join(os.path.dirname(__file__), "cpc_1908.db")


def get_db_connection():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_lre_schema():
    """Initializes schema migrations for LRE without dropping existing tables."""
    con = get_db_connection()
    cur = con.cursor()

    # 1. Matter master table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lre_matters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        case_number TEXT,
        client_name TEXT NOT NULL,
        client_role TEXT DEFAULT 'Plaintiff', -- Plaintiff / Defendant / Petitioner / Respondent / Appellant
        state TEXT DEFAULT 'Tamil Nadu',
        district TEXT NOT NULL,
        taluk TEXT,
        court TEXT,
        procedural_stage TEXT NOT NULL,
        suit_valuation REAL DEFAULT 0.0,
        real_market_value REAL DEFAULT 0.0,
        property_details TEXT,
        raw_narrative TEXT,
        reliefs_sought TEXT,
        prior_orders TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 2. Chronological events table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lre_chronology (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matter_id INTEGER NOT NULL,
        event_date TEXT NOT NULL, -- YYYY-MM-DD or approx date
        event_title TEXT NOT NULL,
        event_description TEXT,
        category TEXT NOT NULL, -- contract, possession, notice, litigation, order, execution, appeal, limitation
        source_doc_id INTEGER,
        linked_issue TEXT,
        procedural_consequence TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (matter_id) REFERENCES lre_matters(id) ON DELETE CASCADE
    )
    """)

    # 3. Matter documents table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lre_documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matter_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        doc_date TEXT,
        doc_type TEXT NOT NULL, -- Registered Deed, Revenue Record, Advocate Notice, Court Order, Bank Record, etc.
        exhibit_mark TEXT, -- Ex. A-1, Ex. B-1, etc.
        status TEXT DEFAULT 'AVAILABLE', -- AVAILABLE, MISSING, REGISTERED, UNSTAMPED, CERTIFIED_COPY
        is_original INTEGER DEFAULT 0,
        file_path TEXT,
        relevance_notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (matter_id) REFERENCES lre_matters(id) ON DELETE CASCADE
    )
    """)

    # 4. Extracted & Classified Facts
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lre_facts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matter_id INTEGER NOT NULL,
        fact_statement TEXT NOT NULL,
        classification TEXT NOT NULL, -- PROVED, ADMITTED, PLEADED, DISPUTED, ASSUMED, UNKNOWN
        source_sentence TEXT,
        confidence_reason TEXT,
        linked_issue TEXT,
        statutory_implication TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (matter_id) REFERENCES lre_matters(id) ON DELETE CASCADE
    )
    """)

    # 5. Full Audit Snapshots (Historical preservation)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lre_audit_snapshots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matter_id INTEGER NOT NULL,
        audit_version INTEGER DEFAULT 1,
        audit_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (matter_id) REFERENCES lre_matters(id) ON DELETE CASCADE
    )
    """)

    # 6. Generated Court Drafts
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lre_drafts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        matter_id INTEGER NOT NULL,
        draft_type TEXT NOT NULL,
        title TEXT NOT NULL,
        court_heading TEXT,
        content TEXT NOT NULL,
        placeholders_count INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (matter_id) REFERENCES lre_matters(id) ON DELETE CASCADE
    )
    """)

    # 7. Declarative Rules & Trigger Patterns
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lre_rule_definitions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rule_key TEXT UNIQUE NOT NULL,
        category TEXT NOT NULL,
        trigger_keywords TEXT NOT NULL, -- JSON list of regex/tokens
        primary_provision TEXT NOT NULL,
        description TEXT NOT NULL,
        action_required TEXT,
        danger_level TEXT DEFAULT 'HIGH' -- CRITICAL, HIGH, MEDIUM, PROCEDURAL
    )
    """)

    # 8. Source Verification Ledger Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS lre_source_ledger (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_key TEXT UNIQUE NOT NULL,
        source_type TEXT NOT NULL, -- STATUTE, STATE_AMENDMENT, HIGH_COURT_RULE, SC_PRECEDENT, MHC_PRECEDENT
        statute_or_court TEXT NOT NULL,
        provision_or_citation TEXT NOT NULL,
        bench_strength TEXT,
        decision_date TEXT,
        effective_date TEXT,
        jurisdiction TEXT DEFAULT 'Central',
        ratio_or_rule TEXT NOT NULL,
        subsequent_treatment TEXT,
        verification_status TEXT NOT NULL, -- VERIFIED LAW, UNVERIFIED — DO NOT RELY
        primary_source_reference TEXT
    )
    """)

    con.commit()
    con.close()


def create_matter(data):
    """Persists a new matter into lre_matters."""
    init_lre_schema()
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("""
    INSERT INTO lre_matters (
        title, case_number, client_name, client_role, state, district, taluk, court,
        procedural_stage, suit_valuation, real_market_value, property_details,
        raw_narrative, reliefs_sought, prior_orders
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("title", "Untitled Civil Matter"),
        data.get("case_number", ""),
        data.get("client_name", "Client"),
        data.get("client_role", "Plaintiff"),
        data.get("state", "Tamil Nadu"),
        data.get("district", "Coimbatore"),
        data.get("taluk", "Pollachi"),
        data.get("court", "District Munsif Court"),
        data.get("procedural_stage", "Pre-trial"),
        float(data.get("suit_valuation", 0.0) or 0.0),
        float(data.get("real_market_value", 0.0) or 0.0),
        data.get("property_details", ""),
        data.get("raw_narrative", ""),
        data.get("reliefs_sought", ""),
        data.get("prior_orders", "")
    ))
    matter_id = cur.lastrowid
    con.commit()
    con.close()
    return matter_id


def get_matter(matter_id):
    """Retrieves matter with all attached entities."""
    init_lre_schema()
    con = get_db_connection()
    cur = con.cursor()
    row = cur.execute("SELECT * FROM lre_matters WHERE id = ?", (matter_id,)).fetchone()
    if not row:
        con.close()
        return None
    matter = dict(row)

    # Attach events
    ev_rows = cur.execute(
        "SELECT * FROM lre_chronology WHERE matter_id = ? ORDER BY event_date ASC, id ASC", 
        (matter_id,)
    ).fetchall()
    matter["chronology"] = [dict(r) for r in ev_rows]

    # Attach documents
    doc_rows = cur.execute(
        "SELECT * FROM lre_documents WHERE matter_id = ? ORDER BY id ASC", 
        (matter_id,)
    ).fetchall()
    matter["documents"] = [dict(r) for r in doc_rows]

    # Attach facts
    fact_rows = cur.execute(
        "SELECT * FROM lre_facts WHERE matter_id = ? ORDER BY id ASC", 
        (matter_id,)
    ).fetchall()
    matter["facts"] = [dict(r) for r in fact_rows]

    # Attach drafts
    draft_rows = cur.execute(
        "SELECT * FROM lre_drafts WHERE matter_id = ? ORDER BY id ASC", 
        (matter_id,)
    ).fetchall()
    matter["drafts"] = [dict(r) for r in draft_rows]

    # Attach latest audit
    audit_row = cur.execute(
        "SELECT audit_json FROM lre_audit_snapshots WHERE matter_id = ? ORDER BY id DESC LIMIT 1",
        (matter_id,)
    ).fetchone()
    if audit_row:
        matter["latest_audit"] = json.loads(audit_row["audit_json"])
    else:
        matter["latest_audit"] = None

    con.close()
    return matter


def list_matters():
    """Lists all active matters in the workspace."""
    init_lre_schema()
    con = get_db_connection()
    cur = con.cursor()
    rows = cur.execute("SELECT * FROM lre_matters ORDER BY id DESC").fetchall()
    matters = [dict(r) for r in rows]
    con.close()
    return matters


def save_audit_snapshot(matter_id, audit_dict):
    """Saves a point-in-time complete audit snapshot."""
    init_lre_schema()
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("""
    INSERT INTO lre_audit_snapshots (matter_id, audit_json)
    VALUES (?, ?)
    """, (matter_id, json.dumps(audit_dict)))
    snapshot_id = cur.lastrowid
    con.commit()
    con.close()
    return snapshot_id
