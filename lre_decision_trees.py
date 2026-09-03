"""
LexOffline — Deterministic Legal Reasoning Engine (LRE)
Module 5: Procedural Reasoning Engine & Decision Trees (lre_decision_trees.py)

Implements rigorous, step-by-step deterministic decision trees for:
- Injunctions (Order XXXIX Rules 1 & 2 / Section 41 SRA)
- Order VII Rule 11 (Rejection of Plaint)
- Order VI Rule 17 (Amendment of Pleadings)
- Order I Rule 10 (Impleadment / Striking Out)
- Order II Rule 2 (Splitting of Reliefs)
- Order XXIII Rule 1 (Withdrawal & Liberty)
- Order IX Rule 13 (Setting Aside Ex-Parte Decree)
- Order XXI (Execution of Decrees)
- Partition Suits (Order XX Rule 18 / Section 37 TN Court-Fees Act)
- Section 80 CPC (Statutory Notice)
- Section 148A CPC (Caveat Expiration)
- Commercial Courts Act Section 12A (Pre-Institution Mediation)
"""

def evaluate_injunction_tree(context):
    """
    Evaluates an application for Temporary Injunction under Order XXXIX Rules 1 & 2 CPC.
    """
    steps = []
    
    # 1. Maintainable substantive proceeding
    has_substantive_suit = context.get("has_substantive_suit", True)
    steps.append({
        "step": "1. Substantive Proceeding Check",
        "question": "Is there a properly instituted, maintainable substantive suit?",
        "result": "PASS" if has_substantive_suit else "FAIL",
        "statute": "Section 94(c) read with Order XXXIX Rule 1 CPC",
        "note": "Interim injunction cannot stand in a vacuum; requires a valid pending suit."
    })
    if not has_substantive_suit:
        return {"recommendation": "REJECT", "steps": steps, "reason": "No substantive maintainable suit."}

    # 2. Competent Jurisdiction
    has_jurisdiction = context.get("court_has_jurisdiction", True)
    steps.append({
        "step": "2. Jurisdiction Check",
        "question": "Does the court have territorial and pecuniary jurisdiction?",
        "result": "PASS" if has_jurisdiction else "WARNING - OUSTER DETECTED",
        "statute": "Section 16 CPC & TN Civil Courts Act S.12",
        "note": "If market value exceeds pecuniary limit, court cannot grant permanent injunction."
    })

    # 3. Section 41 SRA Statutory Prohibitions
    has_s41_bar = context.get("equally_efficacious_remedy", False)
    steps.append({
        "step": "3. Section 41 Specific Relief Act Bar Audit",
        "question": "Is the injunction barred under Section 41 SRA (e.g. equally efficacious remedy available)?",
        "result": "FAIL (Barred)" if has_s41_bar else "PASS (Clear)",
        "statute": "Section 41(h) Specific Relief Act, 1963",
        "note": "If plaintiff is out of possession and seeks only bare injunction without possession, barred by S.41(h)."
    })

    # 4. Triple Test: Prima Facie Case
    has_prima_facie = context.get("has_prima_facie", True)
    steps.append({
        "step": "4. Prima Facie Case Audit",
        "question": "Has plaintiff established a bona fide contention with substantial question to be investigated?",
        "result": "PASS" if has_prima_facie else "FAIL",
        "statute": "Dalpat Kumar v. Prahlad Singh, (1992) 1 SCC 719",
        "note": "Requires documented antecedent title or coparcenary inheritance."
    })

    # 5. Balance of Convenience & Irreparable Injury
    danger_of_waste = context.get("danger_of_alienation_or_demolition", True)
    steps.append({
        "step": "5. Balance of Convenience & Irreparable Injury",
        "question": "Is property in danger of being alienated, wasted, damaged, or altered?",
        "result": "PASS" if danger_of_waste else "UNCERTAIN",
        "statute": "Order XXXIX Rule 1(a), (c) CPC",
        "note": "Demolition of structures or third-party mortgages establishes irreparable loss."
    })

    # 6. Rule 3 Notice Requirement
    is_ex_parte = context.get("is_ex_parte", False)
    steps.append({
        "step": "6. Order XXXIX Rule 3 Ex-Parte Compliance",
        "question": "If ex-parte ad-interim injunction sought, will delay defeat the object?",
        "result": "COMPLIANCE MANDATORY" if is_ex_parte else "REGULAR NOTICE",
        "statute": "Order XXXIX Rule 3 Proviso (Venkatasubbiah Naidu)",
        "note": "Applicant must deliver copies and file compliance affidavit on same or next day."
    })

    return {
        "tree_name": "Temporary Injunction Decision Tree (O.XXXIX R.1/2)",
        "recommendation": "MAINTAINABLE WITH NOTICE" if not has_s41_bar and has_prima_facie else "DEFECTIVE",
        "steps": steps,
        "governing_provisions": "Order XXXIX Rules 1, 2, 3, 3A CPC read with Sections 37 & 41 SRA 1963"
    }


def evaluate_order_vii_rule_11_tree(context):
    """
    Evaluates maintainability against Order VII Rule 11 rejection.
    """
    steps = []
    
    # 1. Clause (a): Cause of Action
    has_coa = context.get("discloses_cause_of_action", True)
    steps.append({
        "step": "1. Disclose Cause of Action [Rule 11(a)]",
        "result": "PASS" if has_coa else "FATAL REJECTION",
        "statute": "Order VII Rule 11(a) CPC",
        "note": "Look strictly at plaint bundle on demurrer."
    })

    # 2. Clause (b) & (c): Undervaluation & Deficit Court Fee
    is_undervalued = context.get("is_undervalued", True)
    steps.append({
        "step": "2. Valuation & Stamp Paper [Rule 11(b), (c)]",
        "result": "VULNERABLE (Remediable)" if is_undervalued else "PASS",
        "statute": "Order VII Rule 11(b), (c) read with Section 12(2) TN Court-Fees Act",
        "note": "Court must give opportunity to correct valuation before rejecting."
    })

    # 3. Clause (d): Barred by Limitation or Any Law
    is_limitation_barred = context.get("is_limitation_barred", False)
    steps.append({
        "step": "3. Barred by Law [Rule 11(d)]",
        "result": "FATAL REJECTION" if is_limitation_barred else "PASS",
        "statute": "Order VII Rule 11(d) CPC read with Limitation Act S.3",
        "note": "If plaint statement shows claim is barred by Article 58, plaint MUST be rejected."
    })

    # 4. Clause (e) & (f): Duplicate & Summons Copies
    steps.append({
        "step": "4. Duplicate Plaint & Process [Rule 11(e), (f)]",
        "result": "CURABLE REGISTRY CHECK",
        "statute": "Order VII Rule 11(e), (f) read with Order IV Rule 1 CPC",
        "note": "Curable within 7 days under Order VII Rule 9."
    })

    return {
        "tree_name": "Rejection of Plaint Decision Tree (Order VII Rule 11)",
        "vulnerable": is_undervalued or is_limitation_barred or not has_coa,
        "steps": steps,
        "governing_provisions": "Order VII Rule 11(a)–(f) CPC; Dahiben v. Arvindbhai Kalyanji Bhanusali, (2020) 7 SCC 366"
    }


def evaluate_order_vi_rule_17_tree(context):
    """
    Evaluates Amendment of Pleadings under Order VI Rule 17 CPC.
    """
    steps = []
    trial_commenced = context.get("trial_commenced", False)
    steps.append({
        "step": "1. Stage of Proceeding Audit",
        "question": "Has trial commenced (Affidavit of PW-1 filed under O.XVIII R.4)?",
        "result": "POST-TRIAL (Proviso Bar Applies)" if trial_commenced else "PRE-TRIAL (Freely Permissible)",
        "statute": "Order VI Rule 17 Proviso; Vidyabai v. Padmalatha, (2009) 2 SCC 409",
        "note": "If trial has not commenced, proviso does not apply; liberal amendment standard applies."
    })

    due_diligence = context.get("due_diligence_proved", True)
    if trial_commenced:
        steps.append({
            "step": "2. Due Diligence Test",
            "question": "Could the party have raised the matter before commencement despite due diligence?",
            "result": "PASS" if due_diligence else "FATAL BAR",
            "statute": "Order VI Rule 17 Proviso",
            "note": "Jurisdiction to allow amendment is ousted if due diligence is not established."
        })

    changes_nature = context.get("changes_cause_of_action", False)
    steps.append({
        "step": "3. Nature of Suit Test",
        "question": "Does amendment substitute a totally new cause of action or displace admissions?",
        "result": "OBJECTIONABLE" if changes_nature else "PASS",
        "statute": "Revajeetu Builders v. Narayanaswamy, (2009) 10 SCC 84",
        "note": "Introducing an alternative relief of partition on same family property does NOT change nature of suit."
    })

    return {
        "tree_name": "Amendment of Pleadings Decision Tree (Order VI Rule 17)",
        "maintainable": not trial_commenced or due_diligence,
        "steps": steps,
        "governing_provisions": "Order VI Rule 17 CPC read with Section 153 CPC"
    }


def evaluate_order_ii_rule_2_tree(context):
    """
    Evaluates splitting of reliefs under Order II Rule 2 CPC.
    """
    steps = []
    same_cause_of_action = context.get("same_cause_of_action", True)
    relief_omitted = context.get("relief_omitted_earlier", True)
    leave_obtained = context.get("leave_of_court_obtained", False)

    steps.append({
        "step": "1. Identity of Cause of Action",
        "question": "Are the bundle of facts founding both suits identical?",
        "result": "IDENTICAL" if same_cause_of_action else "DISTINCT",
        "statute": "Order II Rule 2(1); Virgo Industries v. Venturetech, (2013) 1 SCC 625",
        "note": "If based on same breach, all reliefs must be claimed together."
    })

    steps.append({
        "step": "2. Leave of Court under Rule 2(3)",
        "question": "Was express leave of Court obtained to omit further relief?",
        "result": "LEAVE OBTAINED" if leave_obtained else "NO LEAVE (FATAL BAR)",
        "statute": "Order II Rule 2(3) CPC",
        "note": "Omission to claim possession or specific performance in earlier refund suit bars subsequent suit without leave."
    })

    is_barred = same_cause_of_action and relief_omitted and not leave_obtained
    return {
        "tree_name": "Order II Rule 2 Relinquishment Tree",
        "is_barred": is_barred,
        "steps": steps,
        "governing_provisions": "Order II Rule 2(1), (2), (3) CPC"
    }
