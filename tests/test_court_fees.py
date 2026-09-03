"""
tests/test_court_fees.py - Unit tests for Tamil Nadu Court Fees Calculator
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import court_fees as cf


def test_money_suit_sec22():
    res = cf.calculate_court_fee("sec22_money", {"claim_amount": 500000, "interest_amount": 0}, include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    # 3% of 5,00,000 = 15,000
    assert res["principal_court_fee"] == 15000
    assert res["total_payable"] == 15000
    assert "Section 22" in res["section"]


def test_money_suit_with_rounding_sec21a():
    # 3% of 100.33 = 3.0099 -> rounded up to 4
    res = cf.calculate_court_fee("sec22_money", {"claim_amount": 101, "interest_amount": 0}, include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    assert res["principal_court_fee"] == 4  # 101 * 0.03 = 3.03 -> ceil to 4


def test_declaration_possession_sec25a_minimum():
    # Value below min Rs. 5,000 should use Rs. 5,000 base
    res = cf.calculate_court_fee("sec25a_dec_poss", {"market_value": 2000}, include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    assert res["statutory_base"] == 5000
    assert res["principal_court_fee"] == 150  # 3% of 5000


def test_declaration_injunction_sec25b():
    # 1/2 of market value (10,00,000 * 0.5 = 5,00,000) at 3% = 15,000
    res = cf.calculate_court_fee("sec25b_dec_inj", {"market_value": 1000000}, include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    assert res["statutory_base"] == 500000
    assert res["principal_court_fee"] == 15000


def test_partition_joint_possession_sec37_2():
    # Subordinate courts: Fixed Rs. 5,000
    res_sub = cf.calculate_court_fee("sec37_2_partition_joint", {"jurisdictional_val": 2500000}, court_type="subordinate", include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    assert res_sub["principal_court_fee"] == 5000

    # High Court: Fixed Rs. 10,000
    res_hc = cf.calculate_court_fee("sec37_2_partition_joint", {"jurisdictional_val": 2500000}, court_type="highcourt", include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    assert res_hc["principal_court_fee"] == 10000


def test_partition_excluded_sec37_1():
    # 3% on share value (15,00,000 * 0.03 = 45,000)
    res = cf.calculate_court_fee("sec37_1_partition_excluded", {"plaintiff_share_val": 1500000}, include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    assert res["principal_court_fee"] == 45000


def test_probate_cap_sch1_art6():
    # 3% on 30,00,000 = 90,000, capped at statutory max 25,000
    res = cf.calculate_court_fee("probate", {"probate_gross": 3200000, "probate_deductions": 200000}, include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    assert res["statutory_base"] == 3000000
    assert res["principal_court_fee"] == 25000


def test_cheque_bounce_sec138_ni_cap():
    # 0.5% on 5,00,000 = 2,500
    res1 = cf.calculate_court_fee("sec138_ni", {"cheque_amount": 500000}, include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    assert res1["principal_court_fee"] == 2500

    # 0.5% on 40,00,000 = 20,000, capped at max 10,000
    res2 = cf.calculate_court_fee("sec138_ni", {"cheque_amount": 4000000}, include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    assert res2["principal_court_fee"] == 10000


def test_refund_sec89():
    res = cf.calculate_court_fee("sec22_money", {"claim_amount": 1000000}, stage="sec89_refund")
    assert res["principal_court_fee"] == 30000
    assert res["refund_amount"] == 30000
    assert "Section 69-A" in res["refund_note"]


def test_stamping_addons():
    res = cf.calculate_court_fee("sec22_money", {"claim_amount": 100000}, include_vakalat=True, include_adv_welfare=True, include_clerk_welfare=True, include_process_fee=True, num_defendants=2)
    # Principal fee = 3,000
    # Vakalat = 10, Advocate welfare = 120, Clerk welfare = 20, Process (2 * 30) = 60
    # Additional = 210 -> Total = 3,210
    assert res["principal_court_fee"] == 3000
    assert res["additional_fee"] == 210
    assert res["total_payable"] == 3210


def test_writ_226_2021_amendment():
    res = cf.calculate_court_fee("writ_226", include_vakalat=False, include_adv_welfare=False, include_clerk_welfare=False)
    # Reduced from 1,000 to 750 by TN Act 20 of 2021
    assert res["principal_court_fee"] == 750
    assert "Act 20 of 2021" in res["citation"]


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
        print(f"  OK  {t.__name__}")
    print(f"\nAll {len(tests)} court fee engine tests passed!")
