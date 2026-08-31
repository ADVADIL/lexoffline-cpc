"""
Test suite for courtroom practice checklists module (17 checklists).
"""
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from checklists_data import (
    PRACTICE_CHECKLISTS,
    list_checklists,
    get_checklist,
    list_checklist_categories
)


def test_all_twenty_one_checklists_present():
    assert len(PRACTICE_CHECKLISTS) == 21
    expected_ids = {
        "o7_r11",
        "o39_r1_2",
        "sec_80",
        "o22_lrs",
        "sec_148a",
        "sec_100",
        "sec_115",
        "plaint_scrutiny_o7",
        "written_statement_o8",
        "amendment_pleadings_o6_r17",
        "commissioner_o26_r9",
        "attachment_before_judgment_o38_r5",
        "summary_suit_o37",
        "set_aside_ex_parte_o9_r13",
        "execution_petition_o21",
        "first_appeal_sec96",
        "commercial_suit_cca",
        "sra_sec16c_specific_performance",
        "sra_sec34_declaration_proviso",
        "sra_sec41_injunction_bars",
        "sra_sec6_summary_possession"
    }
    found_ids = {c.id for c in PRACTICE_CHECKLISTS}
    assert found_ids == expected_ids


def test_checklist_structure_completeness():
    for c in PRACTICE_CHECKLISTS:
        assert c.id
        assert c.title
        assert c.provision
        assert c.category
        assert c.summary
        assert len(c.statutory_grounds) > 0
        assert len(c.judicial_principles) > 0
        assert len(c.steps) > 0
        assert len(c.common_pitfalls) > 0
        assert len(c.connected_provisions) > 0

        # Check steps have valid fields
        for s in c.steps:
            assert s.id
            assert s.label
            assert s.description


def test_get_checklist_by_id():
    c = get_checklist("o7_r11")
    assert c is not None
    assert "Order VII Rule 11" in c.provision
    assert any("Dahiben" in p["citation"] for p in c.judicial_principles)

    c_ps = get_checklist("plaint_scrutiny_o7")
    assert c_ps is not None
    assert "Order VII" in c_ps.provision

    c_ws = get_checklist("written_statement_o8")
    assert c_ws is not None
    assert "Order VIII" in c_ws.provision

    c_cca = get_checklist("commercial_suit_cca")
    assert c_cca is not None
    assert "Commercial Courts Act" in c_cca.provision

    missing = get_checklist("non_existent_id")
    assert missing is None


def test_list_checklists_by_category():
    categories = list_checklist_categories()
    assert len(categories) >= 3

    trial_checklists = list_checklists(category="Trial Court Practice & Pleadings")
    assert len(trial_checklists) >= 4
    for c in trial_checklists:
        assert c.category == "Trial Court Practice & Pleadings"


if __name__ == "__main__":
    test_all_seventeen_checklists_present()
    test_checklist_structure_completeness()
    test_get_checklist_by_id()
    test_list_checklists_by_category()
    print(">>> ALL 17 PRACTICE CHECKLIST TESTS PASSED! <<<")
