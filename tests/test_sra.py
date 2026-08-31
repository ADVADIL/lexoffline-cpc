"""
Test suite for The Specific Relief Act, 1963 (Act No. 47 of 1963).
Validates statutory data integrity, post-2018 amendments, and FTS5 search indexing.
"""
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from db import ActDatabase

DB_PATH = Path(__file__).parent.parent / "cpc_1908.db"


def _get_db():
    return ActDatabase(str(DB_PATH))


def test_all_sra_sections_count():
    db = _get_db()
    rows = db.all_sra_sections()
    assert len(rows) == 47, f"Expected 47 SRA sections, got {len(rows)}"
    sec_nos = [r["section_no"] for r in rows]
    assert "1" in sec_nos
    assert "6" in sec_nos
    assert "10" in sec_nos
    assert "14" in sec_nos
    assert "14A" in sec_nos
    assert "16" in sec_nos
    assert "20" in sec_nos
    assert "20A" in sec_nos
    assert "20B" in sec_nos
    assert "20C" in sec_nos
    assert "34" in sec_nos
    assert "38" in sec_nos
    assert "39" in sec_nos
    assert "41" in sec_nos
    assert "Schedule" in sec_nos


def test_sra_sections_by_part():
    db = _get_db()
    parts = db.sra_sections_by_part()
    assert "PART I — PRELIMINARY" in parts
    assert "PART II — SPECIFIC RELIEF" in parts
    assert "PART III — PREVENTIVE RELIEF" in parts
    assert "THE SCHEDULE" in parts
    assert len(parts["PART I — PRELIMINARY"]) == 4


def test_post_2018_mandatory_specific_performance():
    db = _get_db()
    sec10 = db.get_sra_section_by_no("10")
    assert sec10 is not None
    assert "shall be enforced by the court" in sec10["text"]
    assert "discretion" not in sec10["text"].split("\n")[0]


def test_section_16c_amendment():
    db = _get_db()
    sec16 = db.get_sra_section_by_no("16")
    assert sec16 is not None
    assert "who fails to prove" in sec16["text"]
    assert "not essential for the plaintiff to actually tender to the defendant or to deposit in court any money" in sec16["text"]


def test_substituted_performance_section_20():
    db = _get_db()
    sec20 = db.get_sra_section_by_no("20")
    assert sec20 is not None
    assert "Substituted performance of contract" in sec20["title"]
    assert "notice in writing, of not less than thirty days" in sec20["text"]


def test_infrastructure_injunction_bar():
    db = _get_db()
    sec20a = db.get_sra_section_by_no("20A")
    assert sec20a is not None
    assert "No injunction shall be granted by a court in a suit under this Act involving a contract relating to an infrastructure project" in sec20a["text"]

    sec41 = db.get_sra_section_by_no("41")
    assert sec41 is not None
    assert "(ha)" in sec41["text"]
    assert "infrastructure project" in sec41["text"]


def test_fts5_sra_search():
    db = _get_db()
    results = db.search("substituted performance")
    sra_hits = [r for r in results if r["kind"] == "sra_section"]
    assert len(sra_hits) > 0
    assert any("Section 20" in r["label"] for r in sra_hits)

    infra_results = db.search("infrastructure project")
    infra_hits = [r for r in infra_results if r["kind"] == "sra_section"]
    assert len(infra_hits) > 0


if __name__ == "__main__":
    test_all_sra_sections_count()
    test_sra_sections_by_part()
    test_post_2018_mandatory_specific_performance()
    test_section_16c_amendment()
    test_substituted_performance_section_20()
    test_infrastructure_injunction_bar()
    test_fts5_sra_search()
    print(">>> ALL 7 SPECIFIC RELIEF ACT TESTS PASSED! <<<")
