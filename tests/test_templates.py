"""
Test suite for courtroom drafting templates module.
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


def test_all_eight_templates_present():
    assert len(TEMPLATES) == 8
    expected_ids = {
        "caveat_sec_148a",
        "injunction_o39_r1_2",
        "exparte_o9_r13",
        "execution_o21_tabular",
        "lr_substitution_o22",
        "notice_sec_80",
        "plaint_skeleton_o7",
        "ws_skeleton_o8"
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
        # Check standard placeholders are present
        assert "[" in t.template_text and "]" in t.template_text
        assert len(t.connected_provisions) > 0


def test_get_template_by_id():
    t = get_template("execution_o21_tabular")
    assert t is not None
    assert "Order XXI" in t.provision
    assert "COLUMN NO." in t.template_text

    missing = get_template("non_existent_template")
    assert missing is None


def test_list_templates_by_category():
    categories = list_template_categories()
    assert len(categories) >= 4
    assert "Execution Proceedings" in categories

    exec_templates = list_templates(category="Execution Proceedings")
    assert len(exec_templates) == 1
    assert exec_templates[0].id == "execution_o21_tabular"


def test_all_categories_contain_templates():
    for cat in list_template_categories():
        items = list_templates(category=cat)
        assert len(items) > 0


if __name__ == "__main__":
    test_all_eight_templates_present()
    test_template_structure_and_placeholders()
    test_get_template_by_id()
    test_list_templates_by_category()
    test_all_categories_contain_templates()
    print(">>> ALL DRAFTING TEMPLATE TESTS PASSED! <<<")
