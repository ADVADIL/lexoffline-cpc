"""
court_fees.py - Tamil Nadu Court-Fees and Suits Valuation Calculator Engine
Based on Tamil Nadu Court-Fees and Suits Valuation Act, 1955 (TN Act XIV of 1955)
incorporating:
- Tamil Nadu Act 01 of 2016 (e-Stamping provisions, Sections 74 & 75)
- Tamil Nadu Act 06 of 2017 (3% flat Ad Valorem rate, Section 21-A rounding,
  Section 7 guideline value, Section 37(2) partition fixed fees, Section 69/69-A full refund,
  Schedule II amendments including Sec 138 NI Act, Writs, and CRPs).
"""
import math
from typing import Dict, Any, Optional

AD_VALOREM_RATE = 0.03  # 3% as amended by TN Act 06 of 2017


def round_statutory_rupee(amount: float) -> int:
    """
    Section 21-A (substituted by TN Act 6 of 2017):
    'In the determination and computation of the amount of fee payable under this Act,
    any fraction of a rupee be rounded off to one rupee.'
    """
    if amount <= 0:
        return 0
    return math.ceil(amount)


CATEGORIES = {
    "sec22_money": {
        "title": "Section 22: Suit for Money / Damages / Arrears",
        "section": "Section 22 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Fee computed on exact amount claimed at 3%."
    },
    "sec25a_dec_poss": {
        "title": "Section 25(a): Declaration & Possession of Property",
        "section": "Section 25(a) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on Market Value or Rs. 5,000 (whichever higher) at 3%."
    },
    "sec25b_dec_inj": {
        "title": "Section 25(b): Declaration & Injunction (Immovable Property)",
        "section": "Section 25(b) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on 1/2 of Market Value or Rs. 5,000 (whichever higher) at 3%."
    },
    "sec25c_dec_ipr": {
        "title": "Section 25(c): Declaration - Copyright / Trademark / Patent",
        "section": "Section 25(c) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on relief valuation or Rs. 5,000 (whichever higher) at 3%."
    },
    "sec25cc_adverse": {
        "title": "Section 25(cc) & 30: Defence of Adverse Possession (Counter Claim)",
        "section": "Section 25(cc) & Section 30 Proviso",
        "type": "ad_valorem",
        "tip": "Treated as counter claim: computed on full market value of property at 3%."
    },
    "sec25d_dec_other": {
        "title": "Section 25(d): Declaration - Other Cases",
        "section": "Section 25(d) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on relief valuation or Rs. 5,000 (whichever higher) at 3%."
    },
    "sec26_adoption": {
        "title": "Section 26: Adoption Suit",
        "section": "Section 26 (Fixed Fees)",
        "type": "tiered_fixed",
        "tip": "Fixed court fee based on Court and market value of property affected."
    },
    "sec27a_inj_immovable": {
        "title": "Section 27(a): Injunction (Immovable property where title disputed)",
        "section": "Section 27(a) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on 1/2 Market Value or Rs. 750 (whichever higher) at 3%."
    },
    "sec27b_inj_ipr": {
        "title": "Section 27(b): Injunction (Trade name / Mark / Design)",
        "section": "Section 27(b) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on relief valuation or Rs. 2,000 (whichever higher) at 3%."
    },
    "sec27c_inj_other": {
        "title": "Section 27(c): Injunction - Other Cases",
        "section": "Section 27(c) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on relief valuation or Rs. 1,000 (whichever higher) at 3%."
    },
    "sec37_1_partition_excluded": {
        "title": "Section 37(1): Partition (Plaintiff Excluded from Possession)",
        "section": "Section 37(1) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on full market value of plaintiff's share at 3%."
    },
    "sec37_2_partition_joint": {
        "title": "Section 37(2): Partition (Plaintiff in Joint Possession)",
        "section": "Section 37(2) (2017 Amendment)",
        "type": "fixed",
        "tip": "Fixed fee: Rs. 10,000 (High Court) / Rs. 5,000 (Subordinate Courts)."
    },
    "sec37_3_partition_def": {
        "title": "Section 37(3): Partition - Defendant's Share Claimed",
        "section": "Section 37(3)",
        "type": "ad_valorem_or_fixed",
        "tip": "Defendant in joint possession: 1/2 fixed fee (Rs. 2,500/5,000). Excluded: 3% on 1/2 share MV."
    },
    "sec42a_spec_sale": {
        "title": "Section 42(a): Specific Performance of Contract of Sale",
        "section": "Section 42(a) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on agreed sale consideration at 3%."
    },
    "sec42c_spec_lease": {
        "title": "Section 42(c): Specific Performance of Contract of Lease",
        "section": "Section 42(c) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on premium/fine + average annual rent at 3%."
    },
    "sec30_possession": {
        "title": "Section 30: Suit for Possession not otherwise provided for",
        "section": "Section 30 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on Market Value or Rs. 5,000 (whichever higher) at 3%."
    },
    "sec29_possession_sra": {
        "title": "Section 29: Possession under Section 6 of Specific Relief Act",
        "section": "Section 29 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on 1/2 Market Value or Rs. 800 (whichever higher) at 3%."
    },
    "sec40_cancellation": {
        "title": "Section 40: Cancellation of Decree or Document",
        "section": "Section 40 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on value of property or amount for which decree/document executed at 3%."
    },
    "sec33_1_mortgage_rec": {
        "title": "Section 33(1): Suit to recover money due on Mortgage",
        "section": "Section 33(1) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on total amount claimed at 3%."
    },
    "sec33_8_mortgage_red": {
        "title": "Section 33(8): Suit for Redemption of Mortgage",
        "section": "Section 33(8) • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on amount due or 1/4th principal secured (whichever higher) at 3%."
    },
    "sec43_tenancy": {
        "title": "Section 43: Landlord & Tenant (Eviction / Arrears / Ejectment)",
        "section": "Section 43 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on premium (if any) + 1 year rent at 3%."
    },
    "sec35_accounts": {
        "title": "Section 35: Suit for Accounts",
        "section": "Section 35 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on estimated sum sued for at 3%."
    },
    "sec36_partnership": {
        "title": "Section 36: Dissolution of Partnership & Accounts",
        "section": "Section 36 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on estimated share value at 3%."
    },
    "sec31_easement": {
        "title": "Section 31: Suits relating to Easements",
        "section": "Section 31 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Relief valuation (min Rs. 1,000) + compensation at 3%."
    },
    "sec32_preemption": {
        "title": "Section 32: Pre-emption Suits",
        "section": "Section 32 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on sale consideration or market value, whichever LESS, at 3%."
    },
    "sec41_attachment": {
        "title": "Section 41: Suit to Set Aside Attachment",
        "section": "Section 41 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on amount attached or 1/4th market value, whichever LESS, at 3%."
    },
    "sec44_mesne_profit": {
        "title": "Section 44: Suit for Mesne Profits",
        "section": "Section 44 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "Computed on estimated mesne profits at 3%."
    },
    "sec45_survey": {
        "title": "Section 45: Survey and Boundaries Act Suit",
        "section": "Section 45 • Schedule I Article 1",
        "type": "ad_valorem",
        "tip": "1/2 market value of affected property or Rs. 1,000 (whichever higher) at 3%."
    },
    "sec28_trust": {
        "title": "Section 28: Suits relating to Trust Property",
        "section": "Section 28",
        "type": "capped",
        "tip": "1/5th market value at 3%, capped at maximum Rs. 1,000."
    },
    "sec39_administration": {
        "title": "Section 39: Administration Suit",
        "section": "Section 39 (Fixed Fees)",
        "type": "tiered_fixed",
        "tip": "Tiered fixed fee: Rs. 100 / 500 / 750 (Subordinate Courts) or Rs. 1,000 (High Court)."
    },
    "sec47_public": {
        "title": "Section 47: Section 91 / 92 CPC / Religious Endowments Act",
        "section": "Section 47 (Fixed Fee)",
        "type": "fixed",
        "tip": "Fixed fee: Rs. 200."
    },
    "sec50_residuary": {
        "title": "Section 50: Suits Not Otherwise Provided For (Residuary)",
        "section": "Section 50 (Residuary)",
        "type": "tiered_fixed",
        "tip": "Tiered fixed fee: Rs. 100 / 500 / 750 (Subordinate Courts) or Rs. 1,000 (High Court)."
    },
    "probate": {
        "title": "Probate / Letters of Administration (Schedule I Art 6 & Sec 56)",
        "section": "Schedule I Article 6 (2017 Amendment)",
        "type": "capped",
        "tip": "3% on Net Estate value, capped at maximum Rs. 25,000."
    },
    "succession_cert": {
        "title": "Succession Certificate (Schedule I Art 7)",
        "section": "Schedule I Article 7",
        "type": "tiered_percentage",
        "tip": "2% up to Rs. 5,000; 3% when value exceeds Rs. 5,000."
    },
    "sec138_ni": {
        "title": "Section 138 Negotiable Instruments Act (Cheque Bounce - Sch II Art 20)",
        "section": "Schedule II Article 20 (2017 Amendment)",
        "type": "capped",
        "tip": "0.5% (Half per cent) ad valorem, capped at maximum Rs. 10,000."
    },
    "arbitration_app": {
        "title": "Arbitration & Conciliation Act Application / Appeal",
        "section": "Schedule II Article 4 & 11(m) (2017 Amendment)",
        "type": "capped",
        "tip": "3% of jurisdictional value, capped at maximum Rs. 1,00,000."
    },
    "writ_226": {
        "title": "Writ Petition under Article 226 (Sch II Art 11(r)(i))",
        "section": "Schedule II Article 11(r)(i) (2021 Amendment)",
        "type": "fixed",
        "tip": "Fixed fee: Rs. 750 (reduced from Rs. 1,000 by TN Act 20 of 2021)."
    },
    "writ_227": {
        "title": "Petition under Article 227 (Sch II Art 11(r)(ii))",
        "section": "Schedule II Article 11(r)(ii)",
        "type": "fixed",
        "tip": "Fixed fee: Rs. 500."
    },
    "cpc_revision_hc": {
        "title": "Civil Revision Petition (CRP) to High Court (Sch II Art 11(o))",
        "section": "Schedule II Article 11(o)",
        "type": "fixed",
        "tip": "Fixed fee: Rs. 200."
    },
    "cpc_revision_dist": {
        "title": "Revision Petition to District Court (Sch II Art 11(p))",
        "section": "Schedule II Article 11(p)",
        "type": "fixed",
        "tip": "Fixed fee: Rs. 200."
    },
    "vakalatnama": {
        "title": "Vakalatnama / Mukhtarnama (Sch II Art 16)",
        "section": "Schedule II Article 16",
        "type": "fixed",
        "tip": "Fixed court fee: Rs. 10."
    },
    "caveat": {
        "title": "Caveat Petition (Sch II Art 18)",
        "section": "Schedule II Article 18",
        "type": "fixed",
        "tip": "Fixed fee: Rs. 20."
    },
    "interlocutory_app": {
        "title": "Interlocutory Application (IA / Injunction / Attachment) (Sch II Art 11(h))",
        "section": "Schedule II Article 11(h)",
        "type": "fixed",
        "tip": "Fixed fee: Rs. 20."
    },
    "memo_appearance": {
        "title": "Memo of Appearance in Criminal Courts (Sch II Art 19)",
        "section": "Schedule II Article 19",
        "type": "fixed",
        "tip": "Fixed fee: Rs. 10."
    },
    "matrimonial_petition": {
        "title": "Matrimonial / Divorce Petitions (Sch II Art 1)",
        "section": "Schedule II Article 1",
        "type": "fixed",
        "tip": "Fixed fee: Rs. 50."
    }
}


def calculate_court_fee(
    category: str,
    inputs: Optional[Dict[str, Any]] = None,
    court_type: str = "subordinate",
    stage: str = "plaint",
    include_vakalat: bool = True,
    include_adv_welfare: bool = True,
    include_clerk_welfare: bool = True,
    num_defendants: int = 1,
    include_process_fee: bool = False
) -> Dict[str, Any]:
    if inputs is None:
        inputs = {}
    cat_meta = CATEGORIES.get(category, CATEGORIES["sec22_money"])
    subject_val = 0.0
    statutory_base = 0.0
    principal_fee = 0
    rate_desc = "3% Ad Valorem"
    citation = ""

    if category == "sec22_money":
        claim = float(inputs.get("claim_amount", 0.0))
        interest = float(inputs.get("interest_amount", 0.0))
        subject_val = claim + interest
        statutory_base = subject_val
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Amount Claimed"
        citation = "Under Section 22 read with Schedule I Article 1 of TN Act 14 of 1955 (as amended by Act 6 of 2017), fee is 3% ad valorem on the total amount claimed."

    elif category == "sec25a_dec_poss":
        mv = float(inputs.get("market_value", 0.0))
        subject_val = mv
        statutory_base = max(mv, 5000.0)
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Max(MV, Rs. 5,000)"
        citation = "Under Section 25(a) (as amended by Act 6 of 2017), fee is computed on the market value of the property or Rs. 5,000, whichever is higher, at 3% ad valorem."

    elif category == "sec25b_dec_inj":
        mv = float(inputs.get("market_value", 0.0))
        subject_val = mv
        statutory_base = max(mv * 0.5, 5000.0)
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Max(1/2 MV, Rs. 5,000)"
        citation = "Under Section 25(b) (as amended by Act 6 of 2017), fee is computed on 1/2 the market value of immovable property or Rs. 5,000, whichever is higher, at 3%."

    elif category in ("sec25c_dec_ipr", "sec25d_dec_other"):
        relief = float(inputs.get("relief_value", 0.0))
        subject_val = relief
        statutory_base = max(relief, 5000.0)
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Max(Valuation, Rs. 5,000)"
        citation = f"Under {cat_meta['section']}, fee is computed on plaint valuation or Rs. 5,000, whichever is higher, at 3%."

    elif category == "sec25cc_adverse":
        mv = float(inputs.get("market_value", 0.0))
        subject_val = mv
        statutory_base = mv
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Full Market Value"
        citation = "Under Section 25(cc) & Section 30 Proviso (inserted by Act 6 of 2017), defence of adverse possession is treated as a counter claim and fee is computed on the market value of the property at 3%."

    elif category == "sec26_adoption":
        mv = float(inputs.get("market_value", 0.0))
        subject_val = mv
        statutory_base = mv
        if court_type == "highcourt":
            principal_fee = 1000
            rate_desc = "Fixed Rs. 1,000 (High Court)"
        else:
            if mv <= 30000:
                principal_fee = 250
                rate_desc = "Fixed Rs. 250 (MV <= Rs. 30,000)"
            elif mv < 100000:
                principal_fee = 500
                rate_desc = "Fixed Rs. 500 (Rs. 30,000 < MV < Rs. 1,00,000)"
            else:
                principal_fee = 750
                rate_desc = "Fixed Rs. 750 (MV >= Rs. 1,00,000)"
        citation = "Under Section 26, fixed court fees are payable depending on court jurisdiction and property value."

    elif category == "sec27a_inj_immovable":
        mv = float(inputs.get("market_value", 0.0))
        subject_val = mv
        statutory_base = max(mv * 0.5, 750.0)
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Max(1/2 MV, Rs. 750)"
        citation = "Under Section 27(a), where title is disputed/framed in issue, fee is 3% on 1/2 market value or Rs. 750, whichever is higher."

    elif category == "sec27b_inj_ipr":
        relief = float(inputs.get("relief_value", 0.0))
        subject_val = relief
        statutory_base = max(relief, 2000.0)
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Max(Valuation, Rs. 2,000)"
        citation = "Under Section 27(b), fee is computed on plaint valuation or Rs. 2,000, whichever is higher, at 3%."

    elif category == "sec27c_inj_other":
        relief = float(inputs.get("relief_value", 0.0))
        subject_val = relief
        statutory_base = max(relief, 1000.0)
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Max(Valuation, Rs. 1,000)"
        citation = "Under Section 27(c), fee is computed on plaint valuation or Rs. 1,000, whichever is higher, at 3%."

    elif category == "sec37_1_partition_excluded":
        share_val = float(inputs.get("plaintiff_share_val", 0.0))
        subject_val = share_val
        statutory_base = share_val
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Plaintiff's Share"
        citation = "Under Section 37(1), when plaintiff is excluded from possession, fee is 3% ad valorem on the market value of plaintiff's share."

    elif category == "sec37_2_partition_joint":
        juris_val = float(inputs.get("jurisdictional_val", 0.0))
        subject_val = juris_val
        statutory_base = juris_val
        if court_type == "highcourt":
            principal_fee = 10000
            rate_desc = "Fixed Rs. 10,000 (High Court)"
        else:
            principal_fee = 5000
            rate_desc = "Fixed Rs. 5,000 (Courts other than High Court)"
        citation = "Under Section 37(2) as amended by TN Act 6 of 2017, fixed court fee is Rs. 10,000 in High Court and Rs. 5,000 in all other Courts."

    elif category == "sec37_3_partition_def":
        status = inputs.get("defendant_possession_status", "joint")
        if status == "joint":
            principal_fee = 5000 if court_type == "highcourt" else 2500
            rate_desc = f"Fixed Rs. {principal_fee} (1/2 of Sec 37(2) rate)"
            statutory_base = 0.0
        else:
            def_share_val = float(inputs.get("defendant_share_val", 0.0))
            subject_val = def_share_val
            statutory_base = def_share_val * 0.5
            principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
            rate_desc = "3% on 1/2 Defendant's Share"
        citation = "Under Section 37(3), defendant pays 1/2 of rates under sub-section (1) or (2) on written statement claiming partition."

    elif category == "sec42a_spec_sale":
        consideration = float(inputs.get("sale_consideration", 0.0))
        subject_val = consideration
        statutory_base = consideration
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% of Sale Consideration"
        citation = "Under Section 42(a) read with Schedule I Article 1, fee is computed at 3% on the agreed sale consideration."

    elif category == "sec42c_spec_lease":
        prem = float(inputs.get("lease_premium", 0.0))
        rent = float(inputs.get("lease_annual_rent", 0.0))
        subject_val = prem + rent
        statutory_base = subject_val
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% of (Premium + 1 Yr Rent)"
        citation = "Under Section 42(c), fee is 3% on aggregate of premium and average annual rent."

    elif category == "sec30_possession":
        mv = float(inputs.get("market_value", 0.0))
        subject_val = mv
        statutory_base = max(mv, 5000.0)
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Max(MV, Rs. 5,000)"
        citation = "Under Section 30 (as amended by Act 6 of 2017), fee is 3% on market value or Rs. 5,000, whichever is higher."

    elif category == "sec29_possession_sra":
        mv = float(inputs.get("market_value", 0.0))
        subject_val = mv
        statutory_base = max(mv * 0.5, 800.0)
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Max(1/2 MV, Rs. 800)"
        citation = "Under Section 29, fee is 3% on 1/2 market value of property or Rs. 800, whichever is higher."

    elif category == "sec40_cancellation":
        doc_val = float(inputs.get("doc_value", 0.0))
        subject_val = doc_val
        statutory_base = doc_val
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% of Document / Decree Value"
        citation = "Under Section 40, fee is 3% on the amount or value of property for which decree/document was executed."

    elif category == "sec33_1_mortgage_rec":
        claim = float(inputs.get("claim_amount", 0.0))
        subject_val = claim
        statutory_base = claim
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Mortgage Claim"
        citation = "Under Section 33(1), fee is 3% on the mortgage amount claimed."

    elif category == "sec33_8_mortgage_red":
        due = float(inputs.get("mortgage_due", 0.0))
        secured = float(inputs.get("mortgage_principal", 0.0))
        subject_val = due
        statutory_base = max(due, secured * 0.25)
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Max(Due, 1/4th Principal)"
        citation = "Under Section 33(8), fee is 3% on amount due or 1/4th of principal secured, whichever is higher."

    elif category == "sec43_tenancy":
        rent = float(inputs.get("tenancy_annual_rent", 0.0))
        prem = float(inputs.get("tenancy_premium", 0.0))
        subject_val = rent + prem
        statutory_base = subject_val
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on (1 Yr Rent + Premium)"
        citation = "Under Section 43, fee is 3% on premium plus 1 year rent."

    elif category in ("sec35_accounts", "sec36_partnership", "sec44_mesne_profit"):
        claim = float(inputs.get("claim_amount", 0.0))
        subject_val = claim
        statutory_base = claim
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Estimated Sum"
        citation = f"Under {cat_meta['section']}, fee is 3% on estimated sum in plaint."

    elif category == "sec31_easement":
        relief = float(inputs.get("relief_value", 0.0))
        comp = float(inputs.get("compensation_amount", 0.0))
        subject_val = relief + comp
        statutory_base = max(relief, 1000.0) + comp
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Valuation (min Rs. 1,000) + Compensation"
        citation = "Under Section 31, fee is 3% on relief valuation (min Rs. 1,000) plus any compensation claimed."

    elif category == "sec32_preemption":
        sale = float(inputs.get("preempt_sale_val", 0.0))
        mv = float(inputs.get("market_value", 0.0))
        subject_val = min(sale, mv)
        statutory_base = subject_val
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Min(Sale Price, MV)"
        citation = "Under Section 32, fee is 3% on sale consideration or market value, whichever is less."

    elif category == "sec41_attachment":
        attach_amt = float(inputs.get("attachment_amount", 0.0))
        mv = float(inputs.get("market_value", 0.0))
        subject_val = min(attach_amt, mv * 0.25)
        statutory_base = subject_val
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Min(Attached Sum, 1/4 MV)"
        citation = "Under Section 41, fee is 3% on attached sum or 1/4th market value, whichever is less."

    elif category == "sec45_survey":
        mv = float(inputs.get("market_value", 0.0))
        subject_val = mv
        statutory_base = max(mv * 0.5, 1000.0)
        principal_fee = round_statutory_rupee(statutory_base * AD_VALOREM_RATE)
        rate_desc = "3% on Max(1/2 MV, Rs. 1,000)"
        citation = "Under Section 45, fee is 3% on 1/2 market value of affected property or Rs. 1,000, whichever is higher."

    elif category == "sec28_trust":
        mv = float(inputs.get("market_value", 0.0))
        subject_val = mv
        statutory_base = mv * 0.2
        raw = statutory_base * AD_VALOREM_RATE
        principal_fee = min(round_statutory_rupee(raw), 1000)
        rate_desc = "3% on 1/5 MV (Max Cap Rs. 1,000)"
        citation = "Under Section 28, fee is 3% on 1/5th market value, capped at maximum Rs. 1,000."

    elif category in ("sec39_administration", "sec50_residuary"):
        val = float(inputs.get("jurisdictional_val", 0.0))
        subject_val = val
        statutory_base = val
        if court_type == "highcourt":
            principal_fee = 1000
            rate_desc = "Fixed Rs. 1,000 (High Court)"
        else:
            if val <= 30000:
                principal_fee = 100
                rate_desc = "Fixed Rs. 100 (Value <= Rs. 30,000)"
            elif val < 100000:
                principal_fee = 500
                rate_desc = "Fixed Rs. 500 (Rs. 30,000 < Value < Rs. 1,00,000)"
            else:
                principal_fee = 750
                rate_desc = "Fixed Rs. 750 (Value >= Rs. 1,00,000)"
        citation = f"Under {cat_meta['section']}, tiered fixed court fee applies."

    elif category == "sec47_public":
        principal_fee = 200
        rate_desc = "Fixed Rs. 200"
        citation = "Under Section 47, suits under Sec 91/92 CPC or Sec 14 Religious Endowments Act pay fixed Rs. 200."

    elif category == "probate":
        gross = float(inputs.get("probate_gross", 0.0))
        deductions = float(inputs.get("probate_deductions", 0.0))
        net = max(0.0, gross - deductions)
        subject_val = net
        statutory_base = net
        raw = round_statutory_rupee(net * AD_VALOREM_RATE)
        principal_fee = min(raw, 25000)
        rate_desc = "3% on Net Estate (Max Cap Rs. 25,000)"
        citation = "Under Schedule I Article 6 (as amended by Act 6 of 2017), fee is 3% on net estate, subject to a maximum cap of Rs. 25,000."

    elif category == "succession_cert":
        val = float(inputs.get("succession_amount", 0.0))
        subject_val = val
        statutory_base = val
        if val <= 5000:
            principal_fee = round_statutory_rupee(val * 0.02)
            rate_desc = "2% on Amount"
        else:
            principal_fee = round_statutory_rupee(val * 0.03)
            rate_desc = "3% on Amount"
        citation = "Under Schedule I Article 7, succession certificate fee is 2% up to Rs. 5,000 and 3% beyond."

    elif category == "sec138_ni":
        cheque = float(inputs.get("cheque_amount", 0.0))
        subject_val = cheque
        statutory_base = cheque
        raw = round_statutory_rupee(cheque * 0.005)
        principal_fee = min(raw, 10000)
        rate_desc = "0.5% (Half per cent, Max Rs. 10,000)"
        citation = "Under Schedule II Article 20 as amended by Act 6 of 2017, fee on complaint under Sec 138 NI Act is 0.5% ad valorem, subject to a maximum of Rs. 10,000."

    elif category == "arbitration_app":
        val = float(inputs.get("arbitration_val", 0.0))
        subject_val = val
        statutory_base = val
        raw = round_statutory_rupee(val * 0.03)
        principal_fee = min(raw, 100000)
        rate_desc = "3% (Max Cap Rs. 1,00,000)"
        citation = "Under Schedule II Article 4 and 11(m) (2017 Amendment), fee is 3% of jurisdictional value subject to a maximum of Rs. 1,00,000."

    elif category == "writ_226":
        principal_fee = 750
        rate_desc = "Fixed Rs. 750"
        citation = "Under Schedule II Article 11(r)(i) (as amended by TN Act 20 of 2021), Writ Petition under Art 226 is Rs. 750 (reduced from Rs. 1,000)."

    elif category == "writ_227":
        principal_fee = 500
        rate_desc = "Fixed Rs. 500"
        citation = "Under Schedule II Article 11(r)(ii) (2017 Amendment), petition under Art 227 is Rs. 500."

    elif category in ("cpc_revision_hc", "cpc_revision_dist"):
        principal_fee = 200
        rate_desc = "Fixed Rs. 200"
        citation = "Under Schedule II Article 11(o)/(p) (2017 Amendment), revision petition is Rs. 200."

    elif category in ("vakalatnama", "memo_appearance"):
        principal_fee = 10
        rate_desc = "Fixed Rs. 10"
        citation = "Under Schedule II Article 16/19 (2017 Amendment), fee is Rs. 10."

    elif category in ("caveat", "interlocutory_app"):
        principal_fee = 20
        rate_desc = "Fixed Rs. 20"
        citation = "Under Schedule II Article 18/11(h) (2017 Amendment), fee is Rs. 20."

    elif category == "matrimonial_petition":
        principal_fee = 50
        rate_desc = "Fixed Rs. 50"
        citation = "Under Schedule II Article 1, matrimonial petition court fee is Rs. 50."

    if stage == "appeal":
        citation += " [Under Section 52, fee on appeal is identical to fee payable in court of first instance]."

    additional_fee = 0
    addons_breakdown = {}
    if include_vakalat:
        additional_fee += 10
        addons_breakdown["Vakalatnama Court Fee (Art 16)"] = 10
    if include_adv_welfare:
        additional_fee += 120
        addons_breakdown["Advocates Welfare Fund Stamp"] = 120
    if include_clerk_welfare:
        additional_fee += 20
        addons_breakdown["Advocates Clerks Welfare Stamp"] = 20
    if include_process_fee:
        p_fee = max(1, num_defendants) * 30
        additional_fee += p_fee
        addons_breakdown[f"Process Fee / Batta ({num_defendants} defs)"] = p_fee

    total_court_fee = principal_fee + additional_fee

    refund_amount = 0
    refund_note = ""
    if stage == "sec89_refund":
        refund_amount = principal_fee
        refund_note = "Under Section 69-A (as substituted by Act 6 of 2017), 100% of court fee is refunded immediately upon reference to ADR under Sec 89 CPC, without awaiting settlement."
    elif stage == "sec69_refund":
        refund_amount = principal_fee
        refund_note = "Under Section 69 (as amended by Act 6 of 2017), 100% full refund is ordered when suit is settled out of court before recording evidence."

    return {
        "category": category,
        "title": cat_meta["title"],
        "section": cat_meta["section"],
        "court_type": court_type,
        "stage": stage,
        "subject_value": subject_val,
        "statutory_base": statutory_base,
        "rate_description": rate_desc,
        "principal_court_fee": principal_fee,
        "additional_fee": additional_fee,
        "addons_breakdown": addons_breakdown,
        "total_payable": total_court_fee,
        "refund_amount": refund_amount,
        "refund_note": refund_note,
        "citation": citation,
        "payment_mode": "Physical Stamps or e-Stamps (Sections 74 & 75)"
    }
