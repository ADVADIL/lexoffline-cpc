"""
LexOffline — Deterministic Legal Reasoning Engine (LRE)
Test Suite for LRE Components (tests/test_lre_engine.py)

Tests required scenarios:
1. Order II Rule 2 (Splitting of claims)
2. Order VII Rule 11 (Rejection of plaint on limitation & valuation)
3. Order XXIII Rule 1(4) (Withdrawal without liberty bar)
4. Specific Performance Article 54 limitation
5. Declaration Article 58 limitation
6. Possession Article 65 adverse possession ouster
7. Tamil Nadu Court-Fees Act valuation & 3% calculation
8. Tamil Nadu Civil Courts Act pecuniary jurisdiction thresholds (TN Act 23 of 2019)
9. Necessary-party detection (Order I Rule 9 Proviso)
10. Injunction decision tree (Order XXXIX Rules 1 & 2 / Section 41 SRA)
11. Execution procedure (Order XXI)
12. Appeal limitation computation
13. Tamil Nadu local-rule verification failure ([UNVERIFIED — DO NOT RELY])
14. Full LRE Audit Pipeline
"""

import sys
import os
from datetime import date

# Add project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import lre_brain
import lre_classifier
import lre_issue_detector
import lre_decision_trees
import lre_tn_locallaw
import lre_attack_missing
import lre_drafter
import lre_engine
import court_fees as cf
import deadlines as dl

# Ensure schema is initialized before test execution
lre_brain.init_lre_schema()
lre_issue_detector.seed_rules_to_db()


def test_order_ii_rule_2_splitting():
    context_barred = {
        "same_cause_of_action": True,
        "relief_omitted_earlier": True,
        "leave_of_court_obtained": False
    }
    res = lre_decision_trees.evaluate_order_ii_rule_2_tree(context_barred)
    assert res["is_barred"] is True
    assert "Order II Rule 2" in res["governing_provisions"]

    context_permitted = {
        "same_cause_of_action": True,
        "relief_omitted_earlier": True,
        "leave_of_court_obtained": True
    }
    res2 = lre_decision_trees.evaluate_order_ii_rule_2_tree(context_permitted)
    assert res2["is_barred"] is False


def test_order_vii_rule_11_rejection():
    context_vulnerable = {
        "discloses_cause_of_action": True,
        "is_undervalued": True,
        "is_limitation_barred": True
    }
    res = lre_decision_trees.evaluate_order_vii_rule_11_tree(context_vulnerable)
    assert res["vulnerable"] is True

    context_clean = {
        "discloses_cause_of_action": True,
        "is_undervalued": False,
        "is_limitation_barred": False
    }
    res2 = lre_decision_trees.evaluate_order_vii_rule_11_tree(context_clean)
    assert res2["vulnerable"] is False


def test_order_xxiii_rule_1_withdrawal_bar():
    narrative = "The previous suit was dismissed as withdrawn. No liberty was granted by the court."
    issues = lre_issue_detector.detect_issues(narrative)
    rule_keys = [i["rule_key"] for i in issues]
    assert "ISSUE_WITHDRAWAL_LIBERTY_BAR" in rule_keys


def test_specific_performance_art_54():
    # Fixed date: 12.07.2022 -> 3 years -> 12.07.2025
    trigger = date(2022, 7, 12)
    expected_due = date(2025, 7, 12)
    calc = dl.compute_limitation_article(trigger, {"period": "Three years"})
    assert calc["options"][0]["due_date"] == expected_due


def test_declaration_art_58():
    # Trigger 05.03.2021 -> 3 years -> 05.03.2024
    trigger = date(2021, 3, 5)
    expected_due = date(2024, 3, 5)
    calc = dl.compute_limitation_article(trigger, {"period": "Three years"})
    assert calc["options"][0]["due_date"] == expected_due


def test_possession_art_65():
    # 12 years from adverse possession
    trigger = date(2021, 3, 5)
    calc = dl.compute_limitation_article(trigger, {"period": "Twelve years"})
    assert calc["options"][0]["amount"] == 12
    assert calc["options"][0]["unit"] == "years"


def test_tn_court_fee_valuation():
    # Tamil Nadu Act 14 of 1955: 3% on market value of property
    res = cf.calculate_court_fee("sec25a_dec_poss", {"market_value": 1000000.0})
    # 3% of 1,000,000 = 30,000
    assert res["principal_court_fee"] == 30000


def test_tn_pecuniary_jurisdiction_thresholds():
    # District Munsif ceiling is ₹10 Lakhs under TN Act 23 of 2019
    res_dm = lre_tn_locallaw.get_tn_local_forum("Coimbatore", "Pollachi", 800000.0)
    assert "District Munsif" in res_dm["assigned_court"]

    # ₹45 Lakhs belongs to Subordinate Court
    res_sub = lre_tn_locallaw.get_tn_local_forum("Coimbatore", "Pollachi", 4500000.0)
    assert "Subordinate Court" in res_sub["assigned_court"]

    # ₹1.5 Crores belongs to District Court
    res_dc = lre_tn_locallaw.get_tn_local_forum("Coimbatore", "Pollachi", 15000000.0)
    assert "District Court" in res_dc["assigned_court"]


def test_necessary_party_detection():
    narrative = "Late A died intestate leaving behind his widow and three children, including the plaintiff."
    facts = lre_classifier.analyze_facts(narrative)
    # Must flag the unknown/missing status of mother and co-heir
    assert any("widow" in f["fact"].lower() or "mother" in f["fact"].lower() for f in facts)


def test_injunction_decision_tree():
    ctx_maintainable = {
        "has_substantive_suit": True,
        "court_has_jurisdiction": True,
        "equally_efficacious_remedy": False,
        "has_prima_facie": True,
        "danger_of_alienation_or_demolition": True,
        "is_ex_parte": False
    }
    tree = lre_decision_trees.evaluate_injunction_tree(ctx_maintainable)
    assert "MAINTAINABLE" in tree["recommendation"]


def test_execution_procedure_detection():
    narrative = "The decree-holder applied for attachment of property of the judgment-debtor under Order XXI."
    issues = lre_issue_detector.detect_issues(narrative)
    rule_keys = [i["rule_key"] for i in issues]
    assert "ISSUE_EXECUTION_PROCEDURE" in rule_keys


def test_appeal_limitation():
    # Appeal to High Court under Article 116(a): 90 days
    trigger = date(2026, 1, 1)
    calc = dl.compute_limitation_article(trigger, {"period": "Ninety days"})
    assert calc["options"][0]["amount"] == 90
    assert calc["options"][0]["unit"] == "days"


def test_tn_local_rule_verification_failure():
    # Non-existent unverified rule must trigger [UNVERIFIED — DO NOT RELY]
    res = lre_tn_locallaw.verify_tn_procedural_rule("Fake_TN_Government_Notification_9999")
    assert res["status"] == "[UNVERIFIED — DO NOT RELY]"


def test_full_lre_audit_pipeline():
    sample_input = {
        "title": "Mr. X v. D1 & D2 (Agricultural Land 2.40 Acres)",
        "client_name": "Mr. X (Co-owner)",
        "district": "Coimbatore",
        "taluk": "Pollachi",
        "court": "District Munsif Court",
        "procedural_stage": "Post-Written Statement",
        "suit_valuation": 950000.0,
        "real_market_value": 4500000.0,
        "raw_narrative": "Mr. A died intestate leaving 4 heirs. D1 executed settlement deed in 2011 to D2. D2 in possession, mortgaged to D3 in 2023. Suit filed on 10.04.2024 for sole declaration."
    }
    audit = lre_engine.run_full_lre_audit(sample_input)
    assert audit.get("strategic_summary") is not None
    assert len(audit["classified_facts"]) > 0
    assert len(audit["detected_issues"]) > 0
    assert "Subordinate Court" in audit["forum_info"]["assigned_court"]
    assert len(audit["attacks"]) > 0
    assert len(audit["drafts"]) >= 3
