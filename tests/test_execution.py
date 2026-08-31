"""
Test suite for Order XXI execution roadmap module.
"""
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from execution_data import (
    EXECUTION_WORKFLOWS,
    list_execution_workflows,
    get_execution_workflow
)


def test_all_five_workflows_present():
    assert len(EXECUTION_WORKFLOWS) == 5
    expected_ids = {
        "money_decree",
        "immovable_possession",
        "injunction_decree",
        "garnishee_proceedings",
        "arrest_detention"
    }
    found_ids = {w.id for w in EXECUTION_WORKFLOWS}
    assert found_ids == expected_ids


def test_workflow_structure_completeness():
    for w in EXECUTION_WORKFLOWS:
        assert w.id
        assert w.title
        assert w.decree_type
        assert w.summary
        assert len(w.stages) >= 3
        assert len(w.connected_provisions) > 0

        # Check sequential stages
        for i, s in enumerate(w.stages):
            assert s.stage_number == i + 1
            assert s.title
            assert s.governing_rules
            assert s.limitation_period
            assert len(s.actions_required) > 0
            assert len(s.statutory_provisos) > 0
            assert s.advocate_tactics


def test_get_workflow_by_id():
    w = get_execution_workflow("money_decree")
    assert w is not None
    assert "Money Decrees" in w.title
    assert len(w.stages) == 9

    missing = get_execution_workflow("non_existent_workflow")
    assert missing is None


def test_money_decree_stages_coverage():
    w = get_execution_workflow("money_decree")
    stage_titles = [s.title for s in w.stages]
    assert any("Limitation Audit" in t for t in stage_titles)
    assert any("Attachment" in t for t in stage_titles)
    assert any("Proclamation of Sale" in t for t in stage_titles)
    assert any("Setting Aside Sale" in t for t in stage_titles)


def test_possession_decree_coverage():
    w = get_execution_workflow("immovable_possession")
    assert any("Rule 35" in s.governing_rules for s in w.stages)
    assert any("Rule 97" in s.governing_rules for s in w.stages)


if __name__ == "__main__":
    test_all_five_workflows_present()
    test_workflow_structure_completeness()
    test_get_workflow_by_id()
    test_money_decree_stages_coverage()
    test_possession_decree_coverage()
    print(">>> ALL EXECUTION WORKFLOW TESTS PASSED! <<<")
