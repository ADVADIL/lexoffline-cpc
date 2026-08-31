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
    assert set(states_present(_blob("59"))) == {
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
