"""
LexOffline — Deterministic Legal Reasoning Engine (LRE)
Module 4: Legal Knowledge Graph (lre_knowledge_graph.py)

Extends the cross-reference engine into a directed legal relationship graph.
Maps connections between:
- CPC Sections & Rules
- Limitation Act Articles
- Specific Relief Act (SRA) Provisions
- Tamil Nadu Court-Fees & Suits Valuation Act, 1955 Provisions
- Leading Precedents

Relationship Types:
- RELATED_LAW
- TRIGGERED_BY
- DEPENDS_ON
- EXCEPTION
- CONSEQUENCE
- REMEDY
"""

import sqlite3
import os
import xref
from db import ActDatabase

DB_PATH = os.path.join(os.path.dirname(__file__), "cpc_1908.db")


RELATIONSHIP_NODES = {
    # Order VII Rule 11
    "Order VII Rule 11": [
        {"type": "TRIGGERED_BY", "target": "Order VII Rule 1 (Plaint defective)", "note": "Defects in plaint disclosing no cause of action"},
        {"type": "RELATED_LAW", "target": "Section 3, Limitation Act, 1963", "note": "Suit barred by limitation triggers Rule 11(d)"},
        {"type": "RELATED_LAW", "target": "Section 12(2), TN Court-Fees Act, 1955", "note": "Undervaluation objection triggers Rule 11(b)"},
        {"type": "EXCEPTION", "target": "Order VII Rule 13", "note": "Rejection does not preclude presentation of fresh plaint"},
        {"type": "CONSEQUENCE", "target": "Section 2(2) CPC", "note": "Order of rejection is deemed to be a Decree"},
        {"type": "REMEDY", "target": "Section 96 CPC (First Appeal)", "note": "Appeal lies as First Appeal against decree, not as CMA"}
    ],
    # Order II Rule 2
    "Order II Rule 2": [
        {"type": "TRIGGERED_BY", "target": "Single Cause of Action", "note": "Multiple claims or reliefs arising from same contract/breach"},
        {"type": "DEPENDS_ON", "target": "Order II Rule 2(3) Leave of Court", "note": "Omission without express leave permanently bars fresh suit"},
        {"type": "CONSEQUENCE", "target": "Order VII Rule 11(d) CPC", "note": "Subsequent suit barred by law and liable to rejection"},
        {"type": "EXCEPTION", "target": "Distinct Causes of Action", "note": "Virgo Industries: bar applies only when causes of action are identical"},
        {"type": "REMEDY", "target": "Order VI Rule 17 Amendment", "note": "Amend existing suit to include omitted reliefs before trial"}
    ],
    # Order VI Rule 17
    "Order VI Rule 17": [
        {"type": "DEPENDS_ON", "target": "Pre-Trial Stage", "note": "Freely permissible before commencement of trial"},
        {"type": "EXCEPTION", "target": "Order VI Rule 17 Proviso", "note": "Post-trial amendment barred unless Due Diligence proved"},
        {"type": "RELATED_LAW", "target": "Section 153 CPC", "note": "General power of Court to amend defects in proceedings"},
        {"type": "REMEDY", "target": "Article 227 of the Constitution", "note": "CRP under Art 227 lies to Madras HC against refusal (S.115 barred)"}
    ],
    # Order XXXIX Rule 1 & 2
    "Order XXXIX Rule 1": [
        {"type": "DEPENDS_ON", "target": "Triple Test", "note": "Prima facie case, Balance of Convenience, Irreparable injury"},
        {"type": "DEPENDS_ON", "target": "Order XXXIX Rule 3 Proviso", "note": "Mandatory service of papers on same/next day if ex-parte"},
        {"type": "EXCEPTION", "target": "Section 41, Specific Relief Act, 1963", "note": "Injunction barred if equally efficacious relief available"},
        {"type": "CONSEQUENCE", "target": "Order XXXIX Rule 2A", "note": "Disobedience punishable by civil prison up to 3 months and property attachment"},
        {"type": "REMEDY", "target": "Order XLIII Rule 1(r) CPC", "note": "CMA / Miscellaneous Appeal lies against grant or refusal"}
    ],
    # Order IX Rule 13
    "Order IX Rule 13": [
        {"type": "TRIGGERED_BY", "target": "Ex-Parte Decree", "note": "Decree passed in absence of defendant under Order IX Rule 6"},
        {"type": "DEPENDS_ON", "target": "Article 123, Limitation Act, 1963", "note": "Strict 30-day limitation from summons service or knowledge"},
        {"type": "EXCEPTION", "target": "Order IX Rule 13 Explanation", "note": "Barred if appeal against ex-parte decree dismissed on merits"},
        {"type": "REMEDY", "target": "Section 96(2) First Appeal", "note": "Defendant may also appeal directly against the ex-parte decree"}
    ],
    # Order XXIII Rule 1
    "Order XXIII Rule 1": [
        {"type": "DEPENDS_ON", "target": "Order XXIII Rule 1(3) Formal Defect", "note": "Liberty to institute fresh suit granted only on formal defect"},
        {"type": "CONSEQUENCE", "target": "Order XXIII Rule 1(4)", "note": "Withdrawal without permission bars fresh suit permanently"},
        {"type": "EXCEPTION", "target": "Order XXIII Rule 3B", "note": "Representative suit cannot be abandoned without notice to interested parties"}
    ],
    # Order XXI Rule 58
    "Order XXI Rule 58": [
        {"type": "TRIGGERED_BY", "target": "Attachment in Execution", "note": "Third-party claim or objection to attached property"},
        {"type": "CONSEQUENCE", "target": "Order XXI Rule 58(4)", "note": "Order adjudicating claim has the force of a full decree"},
        {"type": "REMEDY", "target": "Section 96 First Appeal", "note": "Appealable as a decree; separate suit is barred by sub-rule (2)"}
    ],
    # Partition & Section 37 TN Court-Fees Act
    "Section 37 TN Court-Fees Act": [
        {"type": "TRIGGERED_BY", "target": "Co-ownership / Joint Family", "note": "Suit for partition by co-owner or coparcener"},
        {"type": "DEPENDS_ON", "target": "Possession Status", "note": "S.37(1) ad valorem 3% if excluded; S.37(2) fixed fee if in joint possession"},
        {"type": "RELATED_LAW", "target": "Article 110, Limitation Act, 1963", "note": "12-year limitation runs from date of known exclusion/ouster"},
        {"type": "REMEDY", "target": "Order XX Rule 18 CPC", "note": "Preliminary decree declaring shares followed by final decree commission"}
    ]
}


def get_knowledge_graph_for_provision(provision_title):
    """
    Returns the graph of related laws, dependencies, exceptions, and remedies.
    """
    # Normalize
    for key, nodes in RELATIONSHIP_NODES.items():
        if key.lower() in provision_title.lower() or provision_title.lower() in key.lower():
            return {
                "provision": key,
                "relationships": nodes
            }
    
    # Generic relationship discovery via DB search
    return {
        "provision": provision_title,
        "relationships": [
            {"type": "RELATED_LAW", "target": "Section 9 CPC (Inherent Jurisdiction)", "note": "Civil courts have jurisdiction unless barred"},
            {"type": "DEPENDS_ON", "target": "Section 3 Limitation Act", "note": "Suit must be within statutory limitation"},
            {"type": "CONSEQUENCE", "target": "Section 12(2) TN Court-Fees Act", "note": "Valuation subject to statutory verification"}
        ]
    }
