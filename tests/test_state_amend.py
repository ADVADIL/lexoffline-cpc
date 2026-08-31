import sqlite3
from pathlib import Path

from state_amend import split_by_state, states_present, text_for_state

DB_PATH = Path(__file__).parent.parent / "cpc_1908.db"


def _blob(section_no):
    c = sqlite3.connect(DB_PATH)
    row = c.execute(
        "SELECT state_amendments FROM sections WHERE section_no=?", (section_no,)
    ).fetchone()
    return row[0] if row else ""


def test_single_state_section():
    assert states_present(_blob("9")) == ["Maharashtra"]


def test_multi_state_section():
    # This data genuinely belongs to Section 60 ("Property liable to
    # attachment and sale in execution of decree") — the amendment text
    # itself says "In clause (g) of the Proviso to sub-section (1) of
    # section 60...". It was previously stored under Section 59 due to a
    # parser bug: Section 60's own heading line was corrupted in the
    # source ("860. Property liable..." instead of "60."), so nothing
    # marked where Section 59 ended and 60 began, and Section 60's whole
    # body — including this trailing state-amendments block — got folded
    # into Section 59's text. Fixed at the source (build_cpc_db.py's
    # KNOWN_LINE_CORRECTIONS); this test now checks the corrected home.
    assert set(states_present(_blob("60"))) == {
        "Himachal Pradesh", "Kerala", "Rajasthan", "Tamil Nadu", "Uttar Pradesh",
    }


def test_misspelled_orissa_is_recognised():
    # source text literally spells this "Orrisa" — must still resolve
    # to the canonical "Orissa" for grouping/UI purposes.
    assert "Orissa" in states_present(_blob("115"))


def test_jk_and_ladakh_full_name_with_UTs_suffix():
    assert "Jammu and Kashmir and Ladakh" in states_present(_blob("35"))


def test_missing_state_returns_empty_text():
    assert text_for_state(_blob("9"), "Kerala") == ""


def test_empty_blob_returns_no_segments():
    assert split_by_state("") == []
    assert split_by_state(None) == []
