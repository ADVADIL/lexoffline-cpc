"""
Deterministic CPC deadline calculator (Part 6, Screen 2 of the spec).
Every entry is a fixed rule straight from the Code — pure date
arithmetic off a single trigger date. No AI, no estimation.

IMPORTANT: these are the general Central Act timelines. State
amendments (e.g. Order VIII Rule 1 in commercial disputes, or state
variants) can change some of these — always cross-check the section
text and applicable state amendment before relying on a computed date.
"""
from dataclasses import dataclass
from datetime import date, timedelta


@dataclass
class DeadlineRule:
    key: str
    label: str
    days: int
    provision: str
    note: str = ""


DEADLINE_RULES = [
    DeadlineRule("ws_30", "Written Statement (ordinary, 30 days)", 30, "O.VIII R.1"),
    DeadlineRule("ws_90", "Written Statement (extended, up to 90 days)", 90, "O.VIII R.1"),
    DeadlineRule("ws_120", "Written Statement (commercial suits, outer limit 120 days)", 120, "O.VIII R.1 (Commercial Courts Act proviso)"),
    DeadlineRule("caveat", "Caveat validity", 90, "S.148A"),
    DeadlineRule("injunction_disposal", "Application for temporary injunction — disposal", 30, "O.XXXIX R.3A"),
    DeadlineRule("commissioner_report", "Commissioner's report submission", 60, "O.XVIII R.4"),
    DeadlineRule("judgment_30", "Judgment pronouncement (ordinary)", 30, "O.XX R.1"),
    DeadlineRule("judgment_60", "Judgment pronouncement (extended, exceptional reasons)", 60, "O.XX R.1"),
    DeadlineRule("decree_prep", "Decree preparation after judgment", 15, "O.XX R.6A"),
    DeadlineRule("amendment", "Amendment of pleadings — compliance", 14, "O.VI R.18"),
    DeadlineRule("witness_list", "Filing list of witnesses from settlement of issues", 15, "O.XVI R.1"),
    DeadlineRule("inspection_commercial", "Inspection of documents (Commercial Courts)", 30, "O.XI R.3 (Commercial)"),
    DeadlineRule("written_args", "Written arguments — before oral arguments", 28, "O.XVIII R.2A", "4 weeks"),
    DeadlineRule("case_mgmt", "First case management hearing", 28, "O.XV-A R.1", "4 weeks"),
    DeadlineRule("args_closure", "Closure of oral arguments after conclusion of evidence", 180, "O.XV-A R.3", "6 months (Commercial)"),
]

_BY_KEY = {r.key: r for r in DEADLINE_RULES}


def list_rules():
    return list(DEADLINE_RULES)


def compute(trigger_date: date, rule_key: str):
    rule = _BY_KEY.get(rule_key)
    if not rule:
        raise KeyError(f"Unknown deadline rule: {rule_key}")
    due = trigger_date + timedelta(days=rule.days)
    return {
        "rule": rule,
        "trigger_date": trigger_date,
        "due_date": due,
        "days": rule.days,
    }
