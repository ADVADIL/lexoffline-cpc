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
