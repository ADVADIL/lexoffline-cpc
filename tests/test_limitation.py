"""
Regression test suite for The Limitation Act, 1963 integration in LexOffline.
"""
from datetime import date
from pathlib import Path
import sqlite3

from db import ActDatabase
import deadlines as dl
import limitation_data as ld

DB_PATH = Path(__file__).parent.parent / "cpc_1908.db"


def _adb():
    return ActDatabase(str(DB_PATH))


def test_limitation_sections_count():
    adb = _adb()
    parts = adb.limitation_sections_by_part()
    total_sections = sum(len(rows) for rows in parts.values())
    assert total_sections == 33  # Sections 1-32 + Section 30A
    adb.close()


def test_limitation_articles_count():
    adb = _adb()
    divs = adb.limitation_articles_by_division()
    total_articles = 0
    for pmap in divs.values():
        for arows in pmap.values():
            total_articles += len(arows)
    assert total_articles == 137  # Articles 1-137
    adb.close()


def test_get_specific_sections():
    adb = _adb()
    # Section 5: Condonation of delay
    s5 = adb.get_limitation_section_by_no("5")
    assert s5 is not None
    assert "Extension of prescribed period" in s5["title"]
    assert "Order XXI" in s5["text"]

    # Section 12: Certified copy exclusion
    s12 = adb.get_limitation_section_by_no("12")
    assert s12 is not None
    assert "Exclusion of time in legal proceedings" in s12["title"]
    assert "time requisite for obtaining a copy" in s12["text"]

    # Section 27: Adverse possession / extinguishment
    s27 = adb.get_limitation_section_by_no("27")
    assert s27 is not None
    assert "Extinguishment of right to property" in s27["title"]
    adb.close()


def test_get_specific_articles():
    adb = _adb()
    # Article 54: Specific performance
    a54 = adb.find_article_by_no("54")
    assert a54 is not None
    assert "specific performance" in a54["description"].lower()
    assert a54["period"] == "Three years"

    # Article 116: Civil Appeal
    a116 = adb.find_article_by_no("116")
    assert a116 is not None
    assert "Code of Civil Procedure" in a116["description"]

    # Article 120: Legal Representatives
    a120 = adb.find_article_by_no("120")
    assert a120 is not None
    assert "legal representative" in a120["description"].lower()
    assert a120["period"] == "Ninety days"

    # Article 123: Ex parte decree
    a123 = db_a123 = adb.find_article_by_no("123")
    assert a123 is not None
    assert "ex parte" in a123["description"].lower()
    assert a123["period"] == "Thirty days"

    # Article 136: Execution of decree
    a136 = adb.find_article_by_no("136")
    assert a136 is not None
    assert "execution of any decree" in a136["description"].lower()
    assert a136["period"] == "Twelve years"
    adb.close()


def test_cpc_to_limitation_linkage():
    adb = _adb()
    # Query limitation articles for Order XXII (Abatement / LRs)
    matches = adb.find_articles_for_cpc("Order XXII")
    art_nos = [m["article_no"] for m in matches]
    assert "120" in art_nos
    assert "121" in art_nos

    # Query limitation articles for Order IX (Restoration / Ex-parte)
    matches_o9 = adb.find_articles_for_cpc("Order IX")
    art_nos_o9 = [m["article_no"] for m in matches_o9]
    assert "122" in art_nos_o9
    assert "123" in art_nos_o9

    # Query limitation articles for Section 115 (Revision)
    matches_s115 = adb.find_articles_for_cpc("Section 115")
    art_nos_s115 = [m["article_no"] for m in matches_s115]
    assert "131" in art_nos_s115
    adb.close()


def test_fts5_search_limitation():
    adb = _adb()
    results = adb.search("condonation")
    assert len(results) > 0
    assert any(r["kind"] == "limitation_section" for r in results)

    results_adv = adb.search("easement")
    assert len(results_adv) > 0
    assert any("limitation" in r["kind"] for r in results_adv)
    adb.close()


def test_deadline_calculations_with_limitation():
    # Art 123 (30 days from decree)
    res = dl.compute(date(2026, 3, 1), "lim_art_123")
    assert res["due_date"] == date(2026, 3, 31)
    assert res["days"] == 30

    # Art 120 (90 days from death)
    res_lr = dl.compute(date(2026, 1, 1), "lim_art_120")
    assert res_lr["due_date"] == date(2026, 4, 1)

    # Art 116(a) Appeal to High Court with Section 12 Exclusion (90 days + 14 days for copy)
    res_app = dl.compute(date(2026, 1, 1), "lim_art_116_a", excluded_days=14)
    assert res_app["due_date"] == date(2026, 4, 15)
    assert res_app["excluded_days"] == 14

    # Art 54 Specific performance (3 years)
    res_sp = dl.compute(date(2026, 5, 10), "lim_art_54")
    assert res_sp["due_date"] == date(2029, 5, 10)

    # Art 136 Execution of decree (12 years)
    res_exec = dl.compute(date(2026, 1, 1), "lim_art_136")
    assert res_exec["due_date"] == date(2038, 1, 1)
