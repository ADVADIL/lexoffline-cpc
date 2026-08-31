import sqlite3
from pathlib import Path

import xref

DB_PATH = Path(__file__).parent.parent / "cpc_1908.db"


def _db():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


def test_section_citation_is_found():
    refs = xref.extract_refs("subject to the provisions of section 47 of this Code")
    assert any(r["kind"] == "section" and r["section_no"] == "47" for r in refs)


def test_order_rule_citation_is_found():
    refs = xref.extract_refs("as provided in Order XXI Rule 58")
    assert any(
        r["kind"] == "order_rule" and r["order_no"] == "XXI" and r["rule_no"] == "58"
        for r in refs
    )


def test_amendment_footnote_is_not_a_false_positive():
    """'6. Subs. by s. 27, ibid.' is an amending Act's own section
    number, not a CPC cross-reference — must not be extracted."""
    text = "5. S. 80 renumbered as sub-section (1) by Act 104 of 1976, s. 27 (w.e.f. 1-2-1977)."
    refs = xref.extract_refs(text)
    assert refs == []


def test_order_regex_does_not_match_ordinary_english():
    """'the High Court may make such order in the case' must not be
    parsed as 'Order IN'."""
    text = "the High Court may make such order in the case as it thinks fit"
    refs = xref.extract_refs(text)
    assert refs == []


def test_self_reference_excluded():
    refs = xref.extract_refs("Section 80 also provides that...", self_kind="section", self_ref="80")
    assert not any(r["section_no"] == "80" for r in refs)


def test_resolve_refs_against_real_db():
    db = _db()
    from db import ActDatabase
    adb = ActDatabase(str(DB_PATH))
    refs = xref.extract_refs("as provided in section 47")
    resolved = xref.resolve_refs(adb, refs)
    assert resolved[0]["target"] is not None
    assert resolved[0]["target"]["section_no"] == "47"
