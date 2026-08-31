"""
Unit tests for Composite Multi-Statute Pleading Generator & Drafter.
"""
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

import composite_drafter as cdraft


def test_composite_pleadings_count():
    pleadings = cdraft.list_composite_pleadings()
    assert len(pleadings) == 8
    ids = [p.id for p in pleadings]
    assert "composite_specific_performance" in ids
    assert "composite_declaration_possession" in ids
    assert "composite_cancellation_deed" in ids
    assert "composite_temp_injunction" in ids
    assert "composite_summary_possession" in ids
    assert "composite_commercial_suit" in ids
    assert "composite_rescission_sec28" in ids
    assert "composite_condonation_delay" in ids


def test_specific_performance_statutory_merger():
    p = cdraft.get_composite_pleading("composite_specific_performance")
    assert p is not None
    assert "ORDER VII" in p.statutory_header
    assert "SECTIONS 10" in p.statutory_header
    assert "ARTICLE 54" in p.statutory_header
    assert "SECTION 55(6)(b)" in p.statutory_header

    # Verify statutory components
    act_names = [sm.act_name for sm in p.statutes_merged]
    assert "Code of Civil Procedure, 1908" in act_names
    assert "The Specific Relief Act, 1963" in act_names
    assert "The Limitation Act, 1963" in act_names
    assert "Transfer of Property Act, 1882" in act_names

    # Test generation with default parameters
    text = p.generate()
    assert "COMPOSITE PLAINT FOR SPECIFIC PERFORMANCE" in text
    assert "16(c)" in text
    assert "22(1)(a)" in text
    assert "Article 54" in text

    # Test generation with custom parameters
    custom = {
        "COURT_NAME": "COURT OF THE SUB JUDGE, COIMBATORE",
        "PLAINTIFF_NAME": "Adv. Rajesh Kumar",
        "TOTAL_CONSIDERATION": "Rs. 75,00,000/-"
    }
    custom_text = p.generate(custom)
    assert "COURT OF THE SUB JUDGE, COIMBATORE" in custom_text
    assert "Adv. Rajesh Kumar" in custom_text
    assert "Rs. 75,00,000/-" in custom_text


def test_declaration_possession_proviso_compliance():
    p = cdraft.get_composite_pleading("composite_declaration_possession")
    assert p is not None
    text = p.generate()
    assert "Ram Saran v. Ganga Devi" in text
    assert "Section 34 Proviso" in text
    assert "Order XX Rule 12" in text
    assert "Article 65" in text


def test_cancellation_suhrid_singh_compliance():
    p = cdraft.get_composite_pleading("composite_cancellation_deed")
    assert p is not None
    text = p.generate()
    assert "Suhrid Singh v. Randhir Singh" in text
    assert "Section 31(2)" in text
    assert "Article 59" in text


if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    for t in tests:
        t()
        print(f'  OK  {t.__name__}')
    print(f'\n>>> ALL {len(tests)} COMPOSITE DRAFTER TESTS PASSED! <<<')
