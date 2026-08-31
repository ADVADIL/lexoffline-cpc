"""
Test suite for expanded courtroom drafting templates module (28 templates).
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


def test_all_28_templates_present():
    assert len(TEMPLATES) == 28
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
        "cert_sec_65b_evidence"
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

    t_amend = get_template("amendment_o6_r17")
    assert t_amend is not None
    assert "Order VI Rule 17" in t_amend.provision
    assert "due diligence" in t_amend.template_text.lower()

    t_comm = get_template("commissioner_o26_r9")
    assert t_comm is not None
    assert "Order XXVI Rule 9" in t_comm.provision

    t_rfa = get_template("regular_first_appeal_sec96")
    assert t_rfa is not None
    assert "Section 96" in t_rfa.provision

    missing = get_template("non_existent_template")
    assert missing is None


def test_list_templates_by_category():
    categories = list_template_categories()
    assert len(categories) >= 6
    assert "Interlocutory Applications" in categories
    assert "Execution Proceedings" in categories
    assert "Appeals & Revisions" in categories
    assert "Core Pleadings" in categories

    ia_templates = list_templates(category="Interlocutory Applications")
    assert len(ia_templates) >= 6
    for t in ia_templates:
        assert t.category == "Interlocutory Applications"


def test_substantive_plaint_templates():
    t_sp = get_template("plaint_specific_performance")
    assert t_sp is not None
    assert "ready and willing" in t_sp.template_text.lower()
    assert "16(c)" in t_sp.template_text

    t_part = get_template("plaint_partition")
    assert t_part is not None
    assert "GENEALOGY" in t_part.template_text
    assert "metes and bounds" in t_part.template_text.lower()


if __name__ == "__main__":
    test_all_28_templates_present()
    test_template_structure_and_placeholders()
    test_get_template_by_id()
    test_list_templates_by_category()
    test_substantive_plaint_templates()
    print(">>> ALL 28 TEMPLATE TESTS PASSED! <<<")
