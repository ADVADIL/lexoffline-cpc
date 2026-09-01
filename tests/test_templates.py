"""
Test suite for comprehensive courtroom drafting templates module (54 templates).
"""
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from templates_data import (
    TEMPLATES,
    list_templates,
    get_template,
    list_template_categories
)


def test_all_58_templates_present():
    assert len(TEMPLATES) == 58
    expected_ids = {
        "caveat_sec_148a",
        "injunction_o39_r1_2",
        "set_aside_ex_parte_o9_r13",
        "execution_o21_tabular",
        "lr_substitution_o22_r3_4",
        "notice_sec_80",
        "plaint_skeleton_o7",
        "ws_skeleton_o8",
        "amendment_o6_r17",
        "commissioner_o26_r9",
        "rejection_plaint_o7_r11",
        "attachment_before_judgment_o38_r5",
        "recall_witness_o18_r17",
        "condonation_delay_sec5",
        "judgment_admissions_o12_r6",
        "adjournment_memo_o17_r1",
        "leave_to_defend_o37_r3",
        "police_aid_execution_sec151",
        "break_open_locks_o21_r35",
        "claim_petition_o21_r58",
        "removal_resistance_o21_r97",
        "regular_first_appeal_sec96",
        "cma_o43_r1",
        "review_petition_sec114",
        "plaint_specific_performance",
        "plaint_partition",
        "plaint_declaration_possession",
        "cert_sec_65b_evidence",
        "impleadment_o1_r10",
        "representative_suit_o1_r8",
        "guardian_ad_litem_o32_r3",
        "strike_out_party_o1_r10",
        "chief_affidavit_o18_r4",
        "witness_summons_o16_r1_2",
        "interrogatories_o11_r1_8",
        "notice_admit_documents_o12_r2",
        "return_documents_o13_r9",
        "handwriting_expert_sec45",
        "commission_witness_o26_r1_4",
        "plaint_cancellation_deed",
        "plaint_ejectment_tenant",
        "plaint_easement_injunction",
        "plaint_commercial_suit",
        "suit_indigent_person_o33",
        "compromise_petition_o23_r3",
        "withdrawal_suit_o23_r1",
        "restoration_suit_o9_r9",
        "restoration_suit_o9_r4",
        "preliminary_issue_o14_r2",
        "correction_decree_sec152",
        "restitution_sec144",
        "regular_second_appeal_sec100",
        "civil_revision_sec115",
        "writ_art227_supervisory",
        "sra_sec20_notice",
        "sra_sec6_plaint",
        "sra_sec28_application",
        "sra_sec14a_expert"
    }
    found_ids = {t.id for t in TEMPLATES}
    assert found_ids == expected_ids


def test_template_structure_and_placeholders():
    for t in TEMPLATES:
        assert t.id
        assert t.title
        assert t.provision
        assert t.category
        assert t.summary
        assert t.practice_notes
        assert len(t.template_text) > 100
        # Check standard bracketed placeholders are present
        assert "[" in t.template_text and "]" in t.template_text
        assert len(t.connected_provisions) > 0


def test_get_template_by_id():
    t = get_template("execution_o21_tabular")
    assert t is not None
    assert "Order XXI" in t.provision
    assert "COLUMN NO." in t.template_text

    t_impl = get_template("impleadment_o1_r10")
    assert t_impl is not None
    assert "Order I Rule 10" in t_impl.provision
    assert "necessary and proper party" in t_impl.template_text.lower()

    t_comm = get_template("plaint_commercial_suit")
    assert t_comm is not None
    assert "statement of truth" in t_comm.template_text.lower()
    assert "15A" in t_comm.provision

    t_rsa = get_template("regular_second_appeal_sec100")
    assert t_rsa is not None
    assert "Section 100" in t_rsa.provision
    assert "substantial questions of law" in t_rsa.template_text.lower()

    t_writ = get_template("writ_art227_supervisory")
    assert t_writ is not None
    assert "227" in t_writ.provision

    missing = get_template("non_existent_template")
    assert missing is None


def test_list_templates_by_category():
    categories = list_template_categories()
    assert len(categories) >= 7
    assert "Interlocutory Applications" in categories
    assert "Execution Proceedings" in categories
    assert "Appeals & Revisions" in categories
    assert "Core Pleadings" in categories
    assert "Parties & Capacity" in categories
    assert "Evidence & Trial Proceedings" in categories
    assert "Settlement & Compromise" in categories

    evidence_templates = list_templates(category="Evidence & Trial Proceedings")
    assert len(evidence_templates) >= 6
    for t in evidence_templates:
        assert t.category == "Evidence & Trial Proceedings"


def test_compromise_and_restoration_templates():
    t_comp = get_template("compromise_petition_o23_r3")
    assert t_comp is not None
    assert "refund" in t_comp.template_text.lower()

    t_rest = get_template("restoration_suit_o9_r9")
    assert t_rest is not None
    assert "Order IX Rule 9" in t_rest.provision
    assert "Article 122" in t_rest.template_text


def test_no_hardcoded_rates_outside_brackets():
    # Every case-specific interest rate must be a [BRACKETED] field the
    # advocate reviews per case, matching how every other case-specific
    # figure in these templates is presented — not left as bare text
    # that reads like fixed statutory boilerplate.
    t = get_template("sra_sec20_notice")
    assert "18% per annum" not in t.template_text
    assert "[CLAIMED INTEREST RATE]% per annum" in t.template_text

    # General scan: no template should contain a bare "N% per annum"
    # rate that isn't part of a bracketed placeholder.
    import re
    for tpl in TEMPLATES:
        for m in re.finditer(r'(?<!\])\s\d{1,2}% per annum', tpl.template_text):
            raise AssertionError(f"{tpl.id}: found unbracketed rate {m.group(0)!r}")


if __name__ == "__main__":
    test_all_58_templates_present()
    test_template_structure_and_placeholders()
    test_get_template_by_id()
    test_list_templates_by_category()
    test_compromise_and_restoration_templates()
    test_no_hardcoded_rates_outside_brackets()
    print(">>> ALL 58 TEMPLATE TESTS PASSED! <<<")
