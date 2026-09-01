"""
Test suite for Case Diary & Procedural Stage Deadline Suggester.
"""
import sys
from datetime import date
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from db import ActDatabase
from case_stages import CIVIL_STAGES, suggest_statutory_deadline


def test_civil_stages_list():
    assert len(CIVIL_STAGES) >= 10
    assert "Service of Summons (Awaiting Written Statement)" in CIVIL_STAGES
    assert "Caveat Lodged (Section 148A)" in CIVIL_STAGES
    assert "Death of Party Reported (Order XXII)" in CIVIL_STAGES


def test_statutory_deadline_suggester_summons():
    t_date = date(2026, 4, 1)
    adv = suggest_statutory_deadline("Service of Summons (Awaiting Written Statement)", t_date)
    assert "Order VIII Rule 1" in adv.statutory_rule
    assert adv.statutory_due_date == date(2026, 5, 1)
    assert "Written Statement" in adv.advice
    assert "90 days" in adv.period_str


def test_statutory_deadline_suggester_caveat():
    t_date = date(2026, 1, 1)
    adv = suggest_statutory_deadline("Caveat Lodged (Section 148A)", t_date)
    assert adv.statutory_rule == "Section 148A(5) CPC"
    assert adv.statutory_due_date == date(2026, 4, 1)
    assert "90 days" in adv.advice


def test_statutory_deadline_suggester_death_lr():
    t_date = date(2026, 2, 1)
    adv = suggest_statutory_deadline("Death of Party Reported (Order XXII)", t_date)
    assert "Order XXII" in adv.statutory_rule
    assert adv.statutory_due_date == date(2026, 5, 2)
    assert "abates" in adv.advice.lower()


def test_statutory_deadline_suggester_applies_section4():
    # 2026-01-02 (Friday) + 30 days = 2026-02-01, a Sunday. The advisor must
    # not hand the advocate a due date that falls on a day court is closed.
    t_date = date(2026, 1, 2)
    adv = suggest_statutory_deadline("Service of Summons (Awaiting Written Statement)", t_date)
    assert adv.statutory_due_date == date(2026, 2, 2)
    assert adv.statutory_due_date.weekday() != 6
    assert "02 February 2026" in adv.advice


def test_statutory_deadline_suggester_respects_extra_holiday():
    # Sunday 2026-02-01 followed by a declared court holiday on Monday
    # 2026-02-02 must roll all the way to Tuesday.
    t_date = date(2026, 1, 2)
    adv = suggest_statutory_deadline(
        "Service of Summons (Awaiting Written Statement)", t_date,
        court_holidays=[date(2026, 2, 2)]
    )
    assert adv.statutory_due_date == date(2026, 2, 3)


def test_case_diary_crud_in_db():
    db = ActDatabase()
    
    # 1. Create case
    cid = db.add_case(
        case_no="O.S. 999/2026",
        court_name="Senior Civil Judge, Bangalore",
        client_name="Ramesh Kumar",
        client_role="Plaintiff",
        opposite_party="Suresh Patel",
        opposite_counsel="Adv. Sharma",
        stage="Service of Summons (Awaiting Written Statement)",
        next_date="2026-05-15",
        notes="Suit for permanent injunction"
    )
    assert cid > 0

    # 2. Get case
    c = db.get_case(cid)
    assert c is not None
    assert c["case_no"] == "O.S. 999/2026"
    assert c["client_name"] == "Ramesh Kumar"

    # 3. Add hearing
    hid = db.add_hearing(
        case_id=cid,
        hearing_date="2026-04-10",
        business_done="Summons served on Defendant. Awaiting WS.",
        next_date="2026-05-15",
        next_purpose="For filing of Written Statement"
    )
    assert hid > 0

    # 4. Get hearings
    hearings = db.hearings_for_case(cid)
    assert len(hearings) == 1
    assert hearings[0]["business_done"] == "Summons served on Defendant. Awaiting WS."

    # 5. Check updated case next_date
    c_updated = db.get_case(cid)
    assert c_updated["next_date"] == "2026-05-15"

    # 6. Delete case
    db.delete_case(cid)
    assert db.get_case(cid) is None
    assert len(db.hearings_for_case(cid)) == 0

    db.close()


if __name__ == "__main__":
    test_civil_stages_list()
    test_statutory_deadline_suggester_summons()
    test_statutory_deadline_suggester_caveat()
    test_statutory_deadline_suggester_death_lr()
    test_case_diary_crud_in_db()
    print(">>> ALL CASE DIARY TESTS PASSED! <<<")
