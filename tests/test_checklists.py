"""
Test suite for courtroom practice checklists module.
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


def test_all_seven_checklists_present():
    assert len(PRACTICE_CHECKLISTS) == 7
    expected_ids = {"o7_r11", "o39_r1_2", "sec_80", "o22_lrs", "sec_148a", "sec_100", "sec_115"}
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

    missing = get_checklist("non_existent_id")
    assert missing is None


def test_list_checklists_by_category():
    categories = list_checklist_categories()
    assert len(categories) >= 3
    assert "Interim Relief" in categories

    relief_checklists = list_checklists(category="Interim Relief")
    assert len(relief_checklists) >= 1
    assert any(c.id == "o39_r1_2" for c in relief_checklists)


def test_all_categories_contain_checklists():
    for cat in list_checklist_categories():
        items = list_checklists(category=cat)
        assert len(items) > 0


if __name__ == "__main__":
    test_all_seven_checklists_present()
    test_checklist_structure_completeness()
    test_get_checklist_by_id()
    test_list_checklists_by_category()
    test_all_categories_contain_checklists()
    print(">>> ALL CHECKLIST TESTS PASSED! <<<")
