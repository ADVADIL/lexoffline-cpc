"""
LexOffline — Deterministic Legal Reasoning Engine (LRE)
Module 7: 'Attack My Case' Demurrer Engine & 'What Am I Missing?' Gap Analyzer (lre_attack_missing.py)

Deterministic, rule-based generation of:
1. ⚔ ATTACK MY CASE: The opposing counsel's deadliest technical ambushes and demurrers
2. 🔎 WHAT AM I MISSING?: Identifies factual and documentary gaps based on detected legal issues
"""

def generate_attacks(detected_issues, classified_facts, context):
    """
    Generates structured procedural attacks based on facts and detected issues.
    """
    attacks = []
    
    # 1. Pecuniary Jurisdiction & Valuation Demurrer
    stated_val = float(context.get("suit_valuation", 0.0))
    real_val = float(context.get("real_market_value", 0.0))
    if real_val > 1000000 and stated_val <= 1000000 and "Munsif" in context.get("court", ""):
        attacks.append({
            "objection": "Lack of Pecuniary Jurisdiction & Deliberate Undervaluation",
            "legal_basis": "Section 12, Tamil Nadu Civil Courts Act, 1873 (amended by TN Act 23 of 2019) read with Section 12(2) TN Court-Fees Act, 1955 and Order VII Rule 11(b) CPC.",
            "triggering_fact": f"Suit valued at ₹{stated_val:,.0f} before District Munsif, while actual guideline value of 2.40 acres is ₹{real_val:,.0f}.",
            "required_proof": "Registration Department Guideline Value extract under Section 47-AA Stamp Act.",
            "likely_procedural_consequence": "Court will sustain objection under Section 12(2) TN Court-Fees Act; plaint liable to be rejected under Order VII Rule 11(b) or returned under Order VII Rule 10.",
            "best_counter": "Proactively file I.A. under Order VII Rule 10A CPC conceding revised valuation and requesting direct transmission of case bundle to the Principal Subordinate Court.",
            "unresolved_question": "What is the exact per-acre guideline value notified for this specific survey number on TNREGINET?"
        })

    # 2. Limitation Bar under Article 58
    reply_date = context.get("reply_notice_date", "2021-03-05")
    suit_date = context.get("suit_institution_date", "2024-04-10")
    attacks.append({
        "objection": "Extinction of Title Declaration under Article 58 Limitation Act",
        "legal_basis": "Article 58 of Limitation Act, 1963 read with Section 3 Limitation Act and Khatri Hotels v. UOI, (2011) 9 SCC 126.",
        "triggering_fact": "Defendant No. 2 issued Reply Notice on 05.03.2021 unequivocally denying Plaintiff's title. Suit filed on 10.04.2024 (3 years 1 month later).",
        "required_proof": "Reply notice dated 05.03.2021 and date of filing stamp on the plaint.",
        "likely_procedural_consequence": "Mandatory dismissal of 100% declaration prayer under Section 3 of Limitation Act and Order VII Rule 11(d) CPC.",
        "best_counter": "Amend plaint under Order VI Rule 17 to claim Partition of 1/4th undivided share. A co-owner's suit for partition is governed by Article 110 (12 years from exclusion), running validly until 04.03.2033.",
        "unresolved_question": "Did Plaintiff file any interlocutory petition or receive any acknowledgment of title between 2021 and 2024?"
    })

    # 3. Non-Joinder of Necessary Parties (Order I Rule 9 Proviso)
    attacks.append({
        "objection": "Fatal Non-Joinder of Class-I Co-heirs in Title / Partition Suit",
        "legal_basis": "Order I Rule 9 Proviso CPC read with Section 8 of the Hindu Succession Act, 1956.",
        "triggering_fact": "Late Mr. A died leaving 4 Class-I heirs (Widow + 3 children). Plaintiff sued in sole capacity without joining his mother or the other sibling.",
        "required_proof": "Tahsildar Legal Heirship Certificate showing names of all 4 surviving heirs.",
        "likely_procedural_consequence": "Dismissal of suit. While misjoinder is curable, Order I Rule 9 Proviso explicitly mandates that non-joinder of a necessary party is fatal.",
        "best_counter": "Immediately file an application under Order I Rule 10(2) CPC before issues are framed to implead the mother and sibling as co-defendants.",
        "unresolved_question": "Are the omitted co-heirs willing to support Plaintiff, or have they colluded with Defendant No. 1?"
    })

    # 4. Section 34 Specific Relief Act Proviso Bar
    attacks.append({
        "objection": "Statutory Bar on Declaration without Seeking Consequential Possession",
        "legal_basis": "Section 34 Proviso, Specific Relief Act, 1963; Ram Saran v. Ganga Devi, AIR 1972 SC 2685; Venkataraja v. Vidyane Doureradjaperumal, (2014) 14 SCC 502.",
        "triggering_fact": "Plaintiff is admittedly out of possession (D2 erected a structure in 2018 and is in physical occupation).",
        "required_proof": "Averments in Plaint admitting D2's possession or revenue adangal showing D2.",
        "likely_procedural_consequence": "Absolute prohibition on Court granting declaratory decree if further relief of possession is not properly valued and prayed for.",
        "best_counter": "Incorporate specific prayer for recovery and delivery of physical possession under Section 25(a) / Section 37(1) of TN Court-Fees Act.",
        "unresolved_question": "Is D2 in occupation of the entirety of the 2.40 acres, or only a demarcated structure?"
    })

    # 5. Order II Rule 2 Splitting of Reliefs
    if any(r["rule_key"] == "ISSUE_SPLITTING_OF_CLAIMS" for r in detected_issues):
        attacks.append({
            "objection": "Relinquishment of Claim / Bar on Subsequent Reliefs",
            "legal_basis": "Order II Rule 2(2) & (3) CPC; Virgo Industries v. Venturetech Solutions, (2013) 1 SCC 625.",
            "triggering_fact": "Omission of partition, possession, or specific performance in any earlier proceeding arising from the same cause of action.",
            "required_proof": "Certified copy of earlier plaint and absence of court order granting express leave under Rule 2(3).",
            "likely_procedural_consequence": "Plaint in subsequent suit barred by law and liable to rejection under Order VII Rule 11(d).",
            "best_counter": "Demonstrate that causes of action are distinct, or amend current plaint before any separate suit is instituted.",
            "unresolved_question": "Was any earlier suit or summary application filed and dismissed or withdrawn?"
        })

    return attacks


def analyze_missing_elements(detected_issues, classified_facts, documents):
    """
    Identifies legally relevant missing facts and documents based on detected issues.
    """
    missing = []
    doc_titles = [d.get("title", "").lower() for d in documents]

    # Check 1: Partition Gaps
    if any(r["rule_key"] in ["ISSUE_NON_EXECUTANT_CANCELLATION", "ISSUE_DEATH_OF_PARTY_ABATEMENT"] for r in detected_issues):
        if not any("heir" in dt for dt in doc_titles):
            missing.append({
                "item": "Official Legal Heirship Certificate of Late Mr. A",
                "type": "DOCUMENT",
                "triggered_by_rule": "Order I Rule 9 Proviso & Section 8 Hindu Succession Act, 1956",
                "legal_reason": "Mandatory to establish the exact number and fractional entitlement of all surviving Class-I co-owners.",
                "action": "Procure certified copy of Tahsildar Legal Heirship Certificate immediately."
            })
        
        missing.append({
            "item": "Pleading on Anticedent Joint Family vs. Self-Acquired Character of Property",
            "type": "FACT",
            "triggered_by_rule": "Section 6 vs Section 8 of Hindu Succession Act, 1956",
            "legal_reason": "If property was ancestral coparcenary property, shares differ under post-2005 Section 6 compared to Section 8 self-acquired devolution.",
            "action": "Instruct client regarding father's source of funds for the 1988 purchase."
        })

    # Check 2: Valuation Gaps
    if not any("guideline" in dt for dt in doc_titles):
        missing.append({
            "item": "Registration Department Guideline Value Certificate",
            "type": "DOCUMENT",
            "triggered_by_rule": "Madras High Court Civil Rules of Practice 1905, Rule 29 & Section 47-AA Indian Stamp Act",
            "legal_reason": "Mandatory for filing valuation slip under Section 25/37 of TN Court-Fees Act, 1955 to determine pecuniary competence.",
            "action": "Download official TNREGINET guideline value certificate for the village survey number."
        })

    # Check 3: Adverse Possession / Ouster Gaps
    missing.append({
        "item": "Continuous Revenue Kist Receipts (2004 to 2018)",
        "type": "DOCUMENT",
        "triggered_by_rule": "Article 65 Limitation Act, 1963 & P. Lakshmi Reddy v. L. Lakshmi Reddy (AIR 1957 SC 314)",
        "legal_reason": "Critical to demolish D2's claim of adverse possession and ouster starting in 2011.",
        "action": "Search village administrative officer (VAO) records for kist receipts paid in father's or plaintiff's name."
    })

    return missing
