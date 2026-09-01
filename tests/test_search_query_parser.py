"""
Tests for ActDatabase._parse_advocate_query — the quick-citation parser
that pins an exact Order/Rule, Section, or Article match to the top of
search results.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from db import ActDatabase


def test_plain_arabic_order_rule():
    db = ActDatabase()
    result = db._parse_advocate_query("Order 39 Rule 1")
    assert result
    assert result[0]["kind"] == "rule"
    assert "XXXIX" in result[0]["label"]
    db.close()


def test_plain_roman_order_rule():
    db = ActDatabase()
    result = db._parse_advocate_query("Order XXXIX Rule 1")
    assert result
    assert "XXXIX" in result[0]["label"]
    db.close()


def test_abbreviated_order_rule():
    db = ActDatabase()
    result = db._parse_advocate_query("O.39 R.1")
    assert result
    assert "XXXIX" in result[0]["label"]
    db.close()


def test_suffixed_order_hyphen_stored_without_hyphen():
    # Order 20-A (COSTS) is stored in the DB as 'XXA' (no hyphen) — the
    # query itself uses the standard hyphenated citation form. Both the
    # arabic and roman forms of the query must still resolve.
    db = ActDatabase()
    result = db._parse_advocate_query("Order 20-A Rule 1")
    assert result, "Order 20-A Rule 1 should resolve despite the DB storing it as XXA"
    assert result[0]["kind"] == "rule"
    assert "XXA" in result[0]["label"] or "XX-A" in result[0]["label"]

    result2 = db._parse_advocate_query("Order XX-A Rule 1")
    assert result2
    db.close()


def test_suffixed_order_family_matters():
    # Order 32-A (SUITS RELATING TO MATTERS CONCERNING THE FAMILY) is also
    # stored without a hyphen ('XXXIIA').
    db = ActDatabase()
    result = db._parse_advocate_query("Order 32-A Rule 6")
    assert result
    assert result[0]["kind"] == "rule"
    db.close()


def test_suffixed_order_hyphen_stored_with_hyphen():
    # Order 16-A (Attendance of Witnesses Confined in Prisons) IS stored
    # with a hyphen ('XVI-A') — both a hyphenated and unhyphenated query
    # must still resolve to it.
    db = ActDatabase()
    result = db._parse_advocate_query("Order 16-A Rule 1")
    assert result
    assert "XVI-A" in result[0]["label"]

    result2 = db._parse_advocate_query("Order XVIA Rule 1")
    assert result2
    assert "XVI-A" in result2[0]["label"]
    db.close()


def test_unknown_order_rule_returns_empty():
    db = ActDatabase()
    result = db._parse_advocate_query("Order 999 Rule 1")
    assert result == []
    db.close()


def test_section_query():
    db = ActDatabase()
    result = db._parse_advocate_query("Section 100")
    assert any(r["kind"] == "section" for r in result)
    db.close()


def test_article_query():
    db = ActDatabase()
    result = db._parse_advocate_query("Article 54")
    assert result
    assert result[0]["kind"] == "limitation_article"
    db.close()


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    for t in tests:
        t()
    print(">>> ALL SEARCH QUERY PARSER TESTS PASSED! <<<")
