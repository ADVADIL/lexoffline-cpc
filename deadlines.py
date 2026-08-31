"""
Deterministic CPC & Limitation Act deadline calculator.
Every entry is a fixed rule straight from the Code of Civil Procedure, 1908 or
The Limitation Act, 1963 — pure date arithmetic off a single trigger date. No
AI, no estimation.
"""
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional, List
import re


def add_years(d: date, years: int) -> date:
    """Add years to a date safely handling leap years."""
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        return d.replace(month=2, day=28, year=d.year + years)


@dataclass
class DeadlineRule:
    key: str
    label: str
    days: Optional[int]
    years: Optional[int]
    provision: str
    category: str
    note: str = ""


DEADLINE_RULES = [
    # --- CPC Procedural Timelines ---
    DeadlineRule("ws_30", "Written Statement (ordinary, 30 days)", 30, None, "O.VIII R.1", "CPC Procedural Timelines"),
    DeadlineRule("ws_90", "Written Statement (extended, up to 90 days)", 90, None, "O.VIII R.1", "CPC Procedural Timelines"),
    DeadlineRule("ws_120", "Written Statement (commercial suits, outer limit 120 days)", 120, None, "O.VIII R.1 (Commercial Courts Act proviso)", "CPC Procedural Timelines"),
    DeadlineRule("caveat", "Caveat validity (90 days)", 90, None, "S.148A(5)", "CPC Procedural Timelines"),
    DeadlineRule("injunction_disposal", "Application for temporary injunction — 30-day disposal endeavour", 30, None, "O.XXXIX R.3A", "CPC Procedural Timelines"),
    DeadlineRule("commissioner_report", "Commissioner's report submission (60 days)", 60, None, "O.XVIII R.4", "CPC Procedural Timelines"),
    DeadlineRule("judgment_30", "Judgment pronouncement (ordinary, 30 days)", 30, None, "O.XX R.1", "CPC Procedural Timelines"),
    DeadlineRule("judgment_60", "Judgment pronouncement (extended, exceptional reasons, 60 days)", 60, None, "O.XX R.1", "CPC Procedural Timelines"),
    DeadlineRule("decree_prep", "Decree preparation after judgment (15 days)", 15, None, "O.XX R.6A", "CPC Procedural Timelines"),
    DeadlineRule("amendment", "Amendment of pleadings — compliance (14 days)", 14, None, "O.VI R.18", "CPC Procedural Timelines"),
    DeadlineRule("witness_list", "Filing list of witnesses from settlement of issues (15 days)", 15, None, "O.XVI R.1", "CPC Procedural Timelines"),
    DeadlineRule("inspection_commercial", "Inspection of documents (Commercial Courts, 30 days)", 30, None, "O.XI R.3 (Commercial)", "CPC Procedural Timelines"),
    DeadlineRule("admission_docs", "Admission of documents after notice (7 days)", 7, None, "O.XII R.2", "CPC Procedural Timelines"),
    DeadlineRule("written_args", "Written arguments — before oral arguments", 28, None, "O.XVIII R.2A", "CPC Procedural Timelines", "4 weeks"),
    DeadlineRule("case_mgmt", "First case management hearing", 28, None, "O.XV-A R.1", "CPC Procedural Timelines", "4 weeks"),
    DeadlineRule("args_closure", "Closure of oral arguments after conclusion of evidence", 180, None, "O.XV-A R.3", "CPC Procedural Timelines", "6 months (Commercial)"),

    # --- Limitation Act: Applications ---
    DeadlineRule("lim_art_118", "Summary Suit: Leave to appear & defend (10 days)", 10, None, "Article 118 (Order XXXVII R.3(5))", "Limitation Act: Applications", "From service of summons for judgment"),
    DeadlineRule("lim_art_120", "Bring Legal Representatives on record (90 days)", 90, None, "Article 120 (Order XXII R.3/4)", "Limitation Act: Applications", "From date of death"),
    DeadlineRule("lim_art_121", "Set aside abatement of suit (60 days)", 60, None, "Article 121 (Order XXII R.9)", "Limitation Act: Applications", "From date of abatement"),
    DeadlineRule("lim_art_122", "Restore suit/appeal dismissed for default (30 days)", 30, None, "Article 122 (Order IX R.4/9, O.XLI R.19)", "Limitation Act: Applications", "From date of dismissal"),
    DeadlineRule("lim_art_123", "Set aside ex-parte decree (30 days)", 30, None, "Article 123 (Order IX R.13, O.XLI R.21)", "Limitation Act: Applications", "From decree or knowledge date if summons not served"),
    DeadlineRule("lim_art_124", "Review of judgment (30 days)", 30, None, "Article 124 (Section 114, Order XLVII R.1)", "Limitation Act: Applications", "From date of decree or order"),
    DeadlineRule("lim_art_125", "Record adjustment / satisfaction of decree (30 days)", 30, None, "Article 125 (Order XXI R.2)", "Limitation Act: Applications", "When payment or adjustment is made"),
    DeadlineRule("lim_art_127", "Set aside execution sale of property (60 days)", 60, None, "Article 127 (Order XXI R.89/90/91)", "Limitation Act: Applications", "From date of sale"),
    DeadlineRule("lim_art_128", "Possession by person dispossessed in execution (30 days)", 30, None, "Article 128 (Order XXI R.99)", "Limitation Act: Applications", "From date of dispossession"),
    DeadlineRule("lim_art_129", "Possession after removing obstruction/resistance (30 days)", 30, None, "Article 129 (Order XXI R.97)", "Limitation Act: Applications", "From date of resistance/obstruction"),
    DeadlineRule("lim_art_131", "Civil Revision under CPC (90 days)", 90, None, "Article 131 (Section 115)", "Limitation Act: Applications", "From decree/order sought to be revised"),
    DeadlineRule("lim_art_134", "Delivery of possession by purchaser in execution sale (1 year)", None, 1, "Article 134 (Order XXI R.95)", "Limitation Act: Applications", "When sale becomes absolute"),
    DeadlineRule("lim_art_135", "Enforcement of mandatory injunction decree (3 years)", None, 3, "Article 135 (Order XXI R.32(5))", "Limitation Act: Applications", "From decree date or date fixed for performance"),
    DeadlineRule("lim_art_136", "Execution of any decree/order (12 years)", None, 12, "Article 136 (Section 38, Order XXI)", "Limitation Act: Applications", "When decree becomes enforceable"),
    DeadlineRule("lim_art_137", "Residuary application under CPC (3 years)", None, 3, "Article 137 (Section 151 / Miscellaneous)", "Limitation Act: Applications", "When right to apply accrues"),

    # --- Limitation Act: Appeals ---
    DeadlineRule("lim_art_116_a", "Civil Appeal to High Court (90 days)", 90, None, "Article 116(a) (Section 96/100, Order XLI/XLII)", "Limitation Act: Appeals", "From date of decree or order"),
    DeadlineRule("lim_art_116_b", "Civil Appeal to District Court / other court (30 days)", 30, None, "Article 116(b) (Section 96, Order XLI)", "Limitation Act: Appeals", "From date of decree or order"),
    DeadlineRule("lim_art_117", "Intra-Court / Letters Patent Appeal in High Court (30 days)", 30, None, "Article 117 (Section 100A, Order XLI)", "Limitation Act: Appeals", "From date of decree or order"),
    DeadlineRule("lim_art_130_a", "Leave to appeal as indigent person to High Court (60 days)", 60, None, "Article 130(a) (Order XLIV R.1)", "Limitation Act: Appeals", "From date of decree"),
    DeadlineRule("lim_art_130_b", "Leave to appeal as indigent person to other court (30 days)", 30, None, "Article 130(b) (Order XLIV R.1)", "Limitation Act: Appeals", "From date of decree"),

    # --- Limitation Act: Suits ---
    DeadlineRule("lim_art_54", "Specific Performance of contract (3 years)", None, 3, "Article 54 (Order XX R.12A)", "Limitation Act: Suits", "Date fixed for performance or notice of refusal"),
    DeadlineRule("lim_art_55", "Compensation for breach of contract (3 years)", None, 3, "Article 55", "Limitation Act: Suits", "When contract is broken or breach ceases"),
    DeadlineRule("lim_art_58", "Declaratory suit (3 years)", None, 3, "Article 58 (Section 9)", "Limitation Act: Suits", "When right to sue first accrues"),
    DeadlineRule("lim_art_59", "Cancel / set aside instrument or decree (3 years)", None, 3, "Article 59", "Limitation Act: Suits", "When facts entitling cancellation first known"),
    DeadlineRule("lim_art_64", "Possession of immovable property on previous possession (12 years)", None, 12, "Article 64", "Limitation Act: Suits", "Date of dispossession"),
    DeadlineRule("lim_art_65", "Possession of immovable property based on title (12 years)", None, 12, "Article 65", "Limitation Act: Suits", "When possession of defendant becomes adverse"),
    DeadlineRule("lim_art_67", "Landlord recovery of possession from tenant (12 years)", None, 12, "Article 67", "Limitation Act: Suits", "When tenancy is determined"),
    DeadlineRule("lim_art_112", "Suit by or on behalf of Central / State Government (30 years)", None, 30, "Article 112 (Section 79)", "Limitation Act: Suits", "When period would run against private person"),
    DeadlineRule("lim_art_113", "Residuary Suit (3 years)", None, 3, "Article 113 (Section 9)", "Limitation Act: Suits", "When right to sue accrues"),
]

_BY_KEY = {r.key: r for r in DEADLINE_RULES}


# ---------------------------------------------------------------------------
# General-purpose calculator covering all 137 Schedule Articles, not just the
# ~29 curated as named DeadlineRules above. The curated rules exist because
# their provision cross-references (Order/Rule numbers) are worth spelling
# out explicitly; this covers everything else so no article is a dead end —
# an advocate can compute a deadline for any of the 137, not only the ones
# that happened to get a named entry.
_WORD_NUMBERS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "twelve": 12,
    "thirty": 30, "sixty": 60, "ninety": 90,
}


def _parse_single_period(text: str):
    """Parse a period phrase like 'Three years' or 'Thirty days' into
    (amount, unit). Raises ValueError if the phrasing isn't recognised —
    callers should treat that as 'cannot compute automatically', never
    guess a number."""
    words = text.strip().lower().replace(".", "").split()
    if len(words) != 2:
        raise ValueError(f"Unrecognised period phrasing: {text!r}")
    amount_word, unit_word = words
    if amount_word not in _WORD_NUMBERS:
        raise ValueError(f"Unrecognised amount word: {amount_word!r}")
    amount = _WORD_NUMBERS[amount_word]
    if unit_word.startswith("year"):
        unit = "years"
    elif unit_word.startswith("day"):
        unit = "days"
    else:
        raise ValueError(f"Unrecognised unit word: {unit_word!r}")
    return amount, unit


def parse_limitation_period(period_text: str):
    """Parse a LIMITATION_ARTICLES period string into a list of
    (label, amount, unit) tuples — usually one entry, but some Articles
    prescribe alternative periods depending on which sub-clause applies
    (e.g. Article 5: '(a) Ninety days\\n(b) Thirty days'), in which case
    every option is returned rather than picking one, since which
    sub-clause applies depends on case facts this function can't know."""
    lines = [l.strip() for l in period_text.split("\n") if l.strip()]
    results = []
    for line in lines:
        m = re.match(r"^(\([a-z]+\)(?:\([ivx]+\))?)\s*(.+)$", line)
        if m:
            label, rest = m.group(1), m.group(2)
        else:
            label, rest = "", line
        amount, unit = _parse_single_period(rest)
        results.append((label, amount, unit))
    return results


def compute_limitation_article(trigger_date: date, article: dict, excluded_days: int = 0) -> dict:
    """Compute the due date(s) for any Schedule Article from
    limitation_data.LIMITATION_ARTICLES, given its 'period' field. Returns
    every option when the Article prescribes alternatives (see
    parse_limitation_period) rather than silently picking one."""
    parsed = parse_limitation_period(article["period"])
    options = []
    for label, amount, unit in parsed:
        if unit == "years":
            base_due = add_years(trigger_date, amount)
        else:
            base_due = trigger_date + timedelta(days=amount)
        due = base_due + timedelta(days=excluded_days)
        options.append({
            "label": label,
            "amount": amount,
            "unit": unit,
            "due_date": due,
            "base_due_date": base_due,
        })
    return {
        "article": article,
        "trigger_date": trigger_date,
        "excluded_days": excluded_days,
        "options": options,
    }


def list_rules(category: Optional[str] = None) -> List[DeadlineRule]:
    if category:
        return [r for r in DEADLINE_RULES if r.category == category]
    return list(DEADLINE_RULES)


def list_categories() -> List[str]:
    cats = []
    for r in DEADLINE_RULES:
        if r.category not in cats:
            cats.append(r.category)
    return cats


def compute(trigger_date: date, rule_key: str, excluded_days: int = 0) -> dict:
    rule = _BY_KEY.get(rule_key)
    if not rule:
        raise KeyError(f"Unknown deadline rule: {rule_key}")

    if rule.days is not None:
        base_due = trigger_date + timedelta(days=rule.days)
        due = base_due + timedelta(days=excluded_days)
        period_str = f"{rule.days} days"
    else:
        base_due = add_years(trigger_date, rule.years)
        due = base_due + timedelta(days=excluded_days)
        period_str = f"{rule.years} year{'s' if rule.years > 1 else ''}"

    return {
        "rule": rule,
        "trigger_date": trigger_date,
        "due_date": due,
        "base_due_date": base_due,
        "period_str": period_str,
        "excluded_days": excluded_days,
        "days": rule.days if rule.days is not None else (base_due - trigger_date).days,
    }
