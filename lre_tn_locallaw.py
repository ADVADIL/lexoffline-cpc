"""
LexOffline — Deterministic Legal Reasoning Engine (LRE)
Module 6: Tamil Nadu Local-Law Engine (lre_tn_locallaw.py)

Maps District & Taluk to:
- Territorial civil courts
- Pecuniary jurisdiction (TN Act 23 of 2019)
- Madras High Court Civil Rules of Practice, 1905
- Tamil Nadu State Amendments to CPC
- Tamil Nadu Court-Fees and Suits Valuation Act, 1955
- Hard-verification failure tagging ([UNVERIFIED — DO NOT RELY])
"""

import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "cpc_1908.db")

# Verified Tamil Nadu Districts and Taluks database
TN_TERRITORIAL_MAP = {
    "coimbatore": {
        "pollachi": {
            "munsif": "District Munsif Court, Pollachi",
            "sub_court": "Principal Subordinate Court, Pollachi",
            "district_court": "Principal District Court, Coimbatore"
        },
        "coimbatore": {
            "munsif": "District Munsif Court, Coimbatore",
            "sub_court": "Principal Subordinate Court, Coimbatore",
            "district_court": "Principal District Court, Coimbatore"
        }
    },
    "chennai": {
        "egmore": {
            "munsif": "Assistant City Civil Court, Chennai (≤ ₹10 Lakhs)",
            "sub_court": "Principal City Civil Court, Chennai (₹10L to ₹1Cr)",
            "district_court": "High Court of Judicature at Madras (Ordinary Original Civil Jurisdiction > ₹1Cr)"
        },
        "mytapore": {
            "munsif": "Assistant City Civil Court, Chennai (≤ ₹10 Lakhs)",
            "sub_court": "Principal City Civil Court, Chennai (₹10L to ₹1Cr)",
            "district_court": "High Court of Judicature at Madras (Ordinary Original Civil Jurisdiction > ₹1Cr)"
        }
    },
    "madurai": {
        "madurai_north": {
            "munsif": "District Munsif Court, Madurai",
            "sub_court": "Principal Subordinate Court, Madurai",
            "district_court": "Principal District Court, Madurai"
        }
    }
}


def get_tn_local_forum(district, taluk, valuation):
    """
    Returns exact territorial and pecuniary court in Tamil Nadu with statutory citations.
    """
    dist_clean = (district or "coimbatore").strip().lower()
    tal_clean = (taluk or "pollachi").strip().lower()
    val = float(valuation or 0.0)

    # Check if district/taluk is mapped
    dist_info = TN_TERRITORIAL_MAP.get(dist_clean)
    if dist_info and tal_clean in dist_info:
        courts = dist_info[tal_clean]
        is_known_territory = True
    else:
        # Fallback generic Tamil Nadu Mofussil naming
        courts = {
            "munsif": f"District Munsif Court, {taluk.title()}",
            "sub_court": f"Principal Subordinate Court (Sub Court), {taluk.title()}",
            "district_court": f"Principal District Court, {district.title()}"
        }
        is_known_territory = False

    is_chennai = "chennai" in dist_clean

    if is_chennai:
        if val <= 1000000:
            assigned_court = courts["munsif"]
            bracket = "Up to ₹10,00,000"
            statutory_authority = "Section 3-A, Chennai City Civil Court Act, 1892 (as amended by TN Act 23 of 2019)"
        elif val <= 10000000:
            assigned_court = courts["sub_court"]
            bracket = "₹10,00,001 to ₹1,00,00,000"
            statutory_authority = "Section 3-A, Chennai City Civil Court Act, 1892 (as amended by TN Act 23 of 2019)"
        else:
            assigned_court = courts["district_court"]
            bracket = "Exceeding ₹1,00,00,000"
            statutory_authority = "Clause 12, Letters Patent, 1865 read with Madras High Court (Jurisdictional Limits) Act"
    else:
        if val <= 1000000:
            assigned_court = courts["munsif"]
            bracket = "Up to ₹10,00,000"
            statutory_authority = "Section 12, Tamil Nadu Civil Courts Act, 1873 (as amended by TN Act 23 of 2019)"
        elif val <= 10000000:
            assigned_court = courts["sub_court"]
            bracket = "₹10,00,001 to ₹1,00,00,000"
            statutory_authority = "Section 12, Tamil Nadu Civil Courts Act, 1873 (as amended by TN Act 23 of 2019)"
        else:
            assigned_court = courts["district_court"]
            bracket = "Exceeding ₹1,00,00,000"
            statutory_authority = "Section 12, Tamil Nadu Civil Courts Act, 1873 (as amended by TN Act 23 of 2019)"

    return {
        "district": district,
        "taluk": taluk,
        "valuation": val,
        "assigned_court": assigned_court,
        "pecuniary_bracket": bracket,
        "statutory_authority": statutory_authority,
        "is_chennai": is_chennai,
        "territorial_verification": "VERIFIED LAW" if is_known_territory else "[UNVERIFIED TALUK BOUNDARY — VERIFY LOCALLY]"
    }


def verify_tn_procedural_rule(rule_name):
    """
    Hard-verifies a Tamil Nadu local rule against verified statutory records.
    Returns: status, verified_text, citation
    """
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    row = cur.execute(
        "SELECT * FROM tn_verified_authorities WHERE citation LIKE ? OR title LIKE ?", 
        (f"%{rule_name}%", f"%{rule_name}%")
    ).fetchone()
    con.close()

    if row:
        return {
            "status": "VERIFIED LAW",
            "citation": row[1],
            "title": row[2],
            "bench_or_body": row[4],
            "ratio": row[5],
            "effective_text": row[8]
        }
    else:
        return {
            "status": "[UNVERIFIED — DO NOT RELY]",
            "citation": rule_name,
            "title": f"Local Rule / Notification: {rule_name}",
            "bench_or_body": "Unknown",
            "ratio": "Not verified in local authoritative gazette database.",
            "effective_text": "Verify from Tamil Nadu Government Gazette or Madras High Court Rules."
        }
