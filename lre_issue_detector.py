"""
LexOffline — Deterministic Legal Reasoning Engine (LRE)
Module 3: Extensible Legal Issue Detector (lre_issue_detector.py)

Uses declarative trigger patterns, rule conditions, and database-stored rules
to detect civil litigation issues across CPC, Limitation Act, SRA, and TN enactments.
"""

import re
import json
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "cpc_1908.db")


DEFAULT_RULES = [
    {
        "rule_key": "ISSUE_LIMITATION_AUDIT",
        "category": "Limitation & Temporal Bar",
        "triggers": ["limitation", "barred by limitation", "delay", "time-barred", "years"],
        "provision": "Section 3, Limitation Act, 1963 read with Order VII Rule 11(d) CPC",
        "description": "Limitation is a mandatory threshold. Court must dismiss suit filed after limitation period even if limitation is not set up as defense.",
        "action": "Audit limitation for each relief separately under Articles 54, 58, 59, 65, 110.",
        "danger_level": "CRITICAL"
    },
    {
        "rule_key": "ISSUE_NON_EXECUTANT_CANCELLATION",
        "category": "Substantive Relief & Court Fees",
        "triggers": ["settlement deed", "sale deed", "not executant", "no title to convey", "cancellation", "settled"],
        "provision": "Section 31 & 34 SRA; Section 40 vs 25 TN Court-Fees Act; Suhrid Singh (2010 12 SCC 112)",
        "description": "Non-executant co-owner not in possession seeking to avoid deed executed by another co-owner need only sue for declaration and possession, NOT cancellation under Section 40.",
        "action": "Frame prayer as declaration that deed is void and does not bind Plaintiff's share; avoid Section 40 ad valorem fee.",
        "danger_level": "HIGH"
    },
    {
        "rule_key": "ISSUE_ORDER_VIII_WRITTEN_STATEMENT",
        "category": "Pleading Defaults & Timelines",
        "triggers": ["written statement", "failed to file written statement", "delay in filing ws", "90 days", "120 days"],
        "provision": "Order VIII Rule 1 & Rule 10 CPC",
        "description": "WS must be presented within 30 days, extendable up to 90 days for recorded reasons. In Commercial Courts, forfeiture is absolute after 120 days (SCG Contracts).",
        "action": "Check date of summons service; if past 120 days in Commercial Court, move for judgment under Order VIII Rule 10.",
        "danger_level": "HIGH"
    },
    {
        "rule_key": "ISSUE_WITHDRAWAL_LIBERTY_BAR",
        "category": "Maintainability & Prior Proceedings",
        "triggers": ["withdrawn suit", "withdrew", "fresh suit", "dismissed as withdrawn", "no liberty", "order xxiii"],
        "provision": "Order XXIII Rule 1(1), (3), (4) CPC",
        "description": "Where a plaintiff withdraws or abandons a suit without express permission under sub-rule (3), he is precluded from instituting any fresh suit in respect of the same subject-matter or claim.",
        "action": "Examine if cause of action of fresh suit is distinct or if order granting withdrawal can be reviewed / challenged.",
        "danger_level": "CRITICAL"
    },
    {
        "rule_key": "ISSUE_SPLITTING_OF_CLAIMS",
        "category": "Maintainability & Frame of Suit",
        "triggers": ["same cause of action", "omitted", "relinquished", "order ii rule 2", "separate suit"],
        "provision": "Order II Rule 2 CPC",
        "description": "Plaintiff must include whole claim arising from cause of action. Omission to sue for all reliefs without leave of Court permanently bars subsequent suit for omitted reliefs.",
        "action": "Ensure all reliefs (declaration, partition, possession, mesne profits) are united in the present suit or leave is sought.",
        "danger_level": "CRITICAL"
    },
    {
        "rule_key": "ISSUE_LIS_PENDENS_TRANSFER",
        "category": "Interim & Third Party Rights",
        "triggers": ["property transferred during suit", "mortgage", "alienate", "alienating", "third party", "d3", "d4", "developer"],
        "provision": "Section 52 Transfer of Property Act, 1882 read with Order I Rule 10 CPC",
        "description": "Transfers pendente lite do not affect the rights of any party to the suit. Transferee is a proper party and bound by decree.",
        "action": "Implead transferee / mortgagee under Order I Rule 10(2) CPC; seek interim injunction under Order XXXIX Rules 1 & 2.",
        "danger_level": "HIGH"
    },
    {
        "rule_key": "ISSUE_TEMPORARY_INJUNCTION_BARS",
        "category": "Interlocutory Reliefs",
        "triggers": ["injunction", "temporary injunction", "restraining", "demolition", "structure", "status quo"],
        "provision": "Order XXXIX Rules 1, 2, 3A CPC read with Section 41 Specific Relief Act, 1963",
        "description": "Injunction requires Prima Facie case, Balance of Convenience, and Irreparable Injury. Section 41 SRA bars injunction where equally efficacious relief is available or to restrain judicial proceedings.",
        "action": "Ensure possession is claimed as substantive relief if out of possession; comply with Order XXXIX Rule 3 proviso notice rules.",
        "danger_level": "HIGH"
    },
    {
        "rule_key": "ISSUE_REJECTION_OF_PLAINT",
        "category": "Threshold Defense",
        "triggers": ["plaint", "rejection", "order vii rule 11", "barred by law", "cause of action", "undervalued"],
        "provision": "Order VII Rule 11(a), (b), (c), (d) CPC",
        "description": "Plaint liable to rejection if no cause of action, barred by law, or undervalued and uncorrected.",
        "action": "Audit plaint on demurrer basis; correct valuation under Section 12(2) TN Court-Fees Act before court inquiry.",
        "danger_level": "CRITICAL"
    },
    {
        "rule_key": "ISSUE_DEATH_OF_PARTY_ABATEMENT",
        "category": "Parties & Succession",
        "triggers": ["death", "died", "deceased", "legal representative", "abated", "abatement"],
        "provision": "Order XXII Rules 3, 4, 9, 10A CPC",
        "description": "Death of party requires substitution of legal representative within 90 days (Art. 120 Limitation Act), failing which suit abates.",
        "action": "File application under Order XXII Rule 3 or 4 within 90 days; if abated, file under Rule 9 with Section 5 Limitation application.",
        "danger_level": "HIGH"
    },
    {
        "rule_key": "ISSUE_EXECUTION_PROCEDURE",
        "category": "Decree Enforcement",
        "triggers": ["execution", "decree-holder", "judgment-debtor", "order xxi", "warrant", "attachment of property"],
        "provision": "Section 47 & Order XXI CPC",
        "description": "All questions relating to execution, discharge, or satisfaction must be decided by executing court, not by separate suit.",
        "action": "Determine mode of execution: money recovery, immovable delivery under Rule 35, or removal of obstruction under Rule 97.",
        "danger_level": "PROCEDURAL"
    },
    {
        "rule_key": "ISSUE_APPEAL_AND_REVISION",
        "category": "Appellate Remedies",
        "triggers": ["appeal", "revision", "first appeal", "second appeal", "section 96", "section 100", "section 115", "article 227"],
        "provision": "Sections 96, 100, 104, 115 CPC; Order XLI, XLII, XLIII; Article 227 of Constitution",
        "description": "First Appeal lies on fact and law (S.96). Second Appeal strictly on Substantial Question of Law (S.100). Revision barred where appeal lies.",
        "action": "Check appealability under Order XLIII Rule 1 vs Section 115 / Article 227 supervisory jurisdiction.",
        "danger_level": "PROCEDURAL"
    },
    {
        "rule_key": "ISSUE_SECTION_80_NOTICE",
        "category": "Pre-Institution Condition Precedent",
        "triggers": ["government", "state of tamil nadu", "collector", "tahsildar", "public officer", "section 80"],
        "provision": "Section 80(1) & (2) CPC",
        "description": "Mandatory 2-month notice before suing Government. Urgent interim relief requires express leave under Section 80(2).",
        "action": "Verify if Section 80 notice was served or if leave under Section 80(2) was sought and granted.",
        "danger_level": "CRITICAL"
    },
    {
        "rule_key": "ISSUE_SECTION_148A_CAVEAT",
        "category": "Pre-Emptive Procedural Shield",
        "triggers": ["caveat", "caveator", "section 148a", "ex-parte injunction", "lodged"],
        "provision": "Section 148A(1)–(5) CPC",
        "description": "Right to lodge caveat to receive notice before any interlocutory order is passed. Caveat expires strictly after 90 days under sub-section (5).",
        "action": "Check if caveat is subsisting (within 90 days); verify applicant served copies under Section 148A(4).",
        "danger_level": "MEDIUM"
    },
    {
        "rule_key": "ISSUE_SECTION_34_SRA_PROVISO_BAR",
        "category": "Maintainability of Declaratory Suit",
        "triggers": ["declaration", "not in possession", "dispossessed", "cloud on title", "bare declaration"],
        "provision": "Section 34 Proviso, Specific Relief Act, 1963",
        "description": "No Court shall make any declaration where the plaintiff, being able to seek further relief (possession/consequential relief), omits to do so.",
        "action": "Since D2 is in possession, plaintiff MUST pray for recovery of possession; bare declaration is fatally barred (Ram Saran v. Ganga Devi).",
        "danger_level": "CRITICAL"
    }
]


def seed_rules_to_db():
    import lre_brain
    lre_brain.init_lre_schema()
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    for r in DEFAULT_RULES:
        cur.execute("""
        INSERT OR REPLACE INTO lre_rule_definitions 
        (rule_key, category, trigger_keywords, primary_provision, description, action_required, danger_level)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            r["rule_key"],
            r["category"],
            json.dumps(r["triggers"]),
            r["provision"],
            r["description"],
            r["action"],
            r["danger_level"]
        ))
    con.commit()
    con.close()


def detect_issues(narrative_text, structured_fields=None):
    """
    Scans narrative and structured fields against database-backed declarative rules.
    Returns list of matched legal issues with statutory provisions and required actions.
    """
    seed_rules_to_db()
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute("SELECT * FROM lre_rule_definitions").fetchall()
    con.close()

    text_lower = (narrative_text or "").lower()
    if structured_fields:
        for v in structured_fields.values():
            if isinstance(v, str):
                text_lower += " " + v.lower()

    detected = []
    for r in rows:
        triggers = json.loads(r["trigger_keywords"])
        # Check matching triggers
        matched_triggers = [t for t in triggers if re.search(r'\b' + re.escape(t) + r'\b', text_lower)]
        if matched_triggers:
            detected.append({
                "rule_key": r["rule_key"],
                "category": r["category"],
                "matched_terms": matched_triggers,
                "provision": r["primary_provision"],
                "description": r["description"],
                "action_required": r["action_required"],
                "danger_level": r["danger_level"]
            })

    return detected
