from datetime import date

import deadlines as dl


def test_written_statement_30_days():
    result = dl.compute(date(2026, 1, 1), "ws_30")
    assert result["due_date"] == date(2026, 1, 31)


def test_caveat_90_days():
    result = dl.compute(date(2026, 1, 1), "caveat")
    assert result["due_date"] == date(2026, 4, 1)


def test_unknown_rule_raises():
    try:
        dl.compute(date(2026, 1, 1), "not_a_real_rule")
        assert False, "should have raised"
    except KeyError:
        pass


def test_all_rules_computable():
    for rule in dl.list_rules():
        result = dl.compute(date(2026, 1, 1), rule.key)
        assert result["due_date"] > result["trigger_date"]


def test_parse_single_period():
    assert dl.parse_limitation_period("Three years") == [("", 3, "years")]
    assert dl.parse_limitation_period("Thirty days") == [("", 30, "days")]


def test_parse_compound_period():
    parsed = dl.parse_limitation_period("(a) Ninety days\n(b) Thirty days")
    assert parsed == [("(a)", 90, "days"), ("(b)", 30, "days")]


def test_compute_limitation_article_single_period():
    import limitation_data as ld
    art = next(a for a in ld.LIMITATION_ARTICLES if a["article_no"] == "1")
    result = dl.compute_limitation_article(date(2026, 1, 1), art)
    assert len(result["options"]) == 1
    assert result["options"][0]["due_date"] == date(2029, 1, 1)


def test_compute_limitation_article_compound_period():
    import limitation_data as ld
    art = next(a for a in ld.LIMITATION_ARTICLES if a["article_no"] == "61")
    result = dl.compute_limitation_article(date(2026, 1, 1), art)
    assert len(result["options"]) == 3
    labels = [o["label"] for o in result["options"]]
    assert labels == ["(a)", "(b)", "(c)"]


def test_apply_section4_shifts_sunday_to_monday():
    sunday = date(2026, 2, 1)
    assert sunday.weekday() == 6
    out = dl.apply_section4(sunday)
    assert out["section4_applied"] is True
    assert out["final_date"] == date(2026, 2, 2)
    assert out["final_date"].weekday() == 0


def test_apply_section4_no_change_on_weekday():
    tuesday = date(2026, 2, 3)
    assert tuesday.weekday() == 1
    out = dl.apply_section4(tuesday)
    assert out["section4_applied"] is False
    assert out["final_date"] == tuesday


def test_apply_section4_skips_consecutive_closed_days():
    # Sunday followed by a declared court holiday on Monday must roll to Tuesday.
    sunday = date(2026, 2, 1)
    monday_holiday = date(2026, 2, 2)
    out = dl.apply_section4(sunday, court_holidays=[monday_holiday])
    assert out["final_date"] == date(2026, 2, 3)
    assert out["section4_applied"] is True


def test_compute_applies_section4_to_final_due_date():
    # 2026-02-01 is a Sunday. Choose a trigger date/rule whose plain
    # arithmetic due date lands exactly there: 30 days before is 2026-01-02.
    result = dl.compute(date(2026, 1, 2), "ws_30")
    assert result["pre_section4_due_date"] == date(2026, 2, 1)
    assert result["pre_section4_due_date"].weekday() == 6
    assert result["section4_applied"] is True
    assert result["due_date"] == date(2026, 2, 2)


def test_compute_limitation_article_applies_section4():
    import limitation_data as ld
    art = next(a for a in ld.LIMITATION_ARTICLES if a["article_no"] == "1")
    # Article 1: three years. Trigger 2023-02-01 (Wed) + 3 years = 2026-02-01 (Sunday).
    result = dl.compute_limitation_article(date(2023, 2, 1), art)
    opt = result["options"][0]
    assert opt["pre_section4_due_date"] == date(2026, 2, 1)
    assert opt["section4_applied"] is True
    assert opt["due_date"] == date(2026, 2, 2)


def test_all_137_articles_computable():
    # Every Article must be computable, not just the ~30 curated as named
    # DeadlineRules above — this is the whole point of the general parser:
    # no Article should be a dead end just because it lacks a named entry.
    import limitation_data as ld
    for article in ld.LIMITATION_ARTICLES:
        result = dl.compute_limitation_article(date(2026, 1, 1), article)
        assert len(result["options"]) >= 1
        for opt in result["options"]:
            assert opt["due_date"] > result["trigger_date"]
