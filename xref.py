"""
Deterministic cross-reference extraction for CPC provisions.
No AI / no inference — pure regex pattern matching against the bare-act
text, resolved against the local database. This powers Tab 2
(Cross-References) for every Section and Rule screen.
"""
import re

# "Section 80", "section 80", "S. 80", "s.80", with optional sub-section e.g. "Section 80(2)"
SECTION_RX = re.compile(r"\b[Ss]ection[s]?\s+(\d{1,3}[A-Za-z]?)\b")
S_ABBR_RX = re.compile(r"\b[Ss]\.\s*(\d{1,3}[A-Za-z]?)\b")

# Canonical CPC order numbers (exact whitelist — matches the Order titles as
# they exist in the local database). Using an explicit whitelist, rather than
# a generic [IVXL]+ pattern, avoids matching ordinary English words like
# "order in" or "order it" as if they were Roman numerals.
_ORDER_NUMERALS = [
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII",
    "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII",
    "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI",
    "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX",
    "XL", "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII",
    "XLIX", "L", "LI",
]
# Longest-first so e.g. "XIII" isn't cut short by an earlier "XI" alternative.
_ORDER_ALT = "|".join(sorted(_ORDER_NUMERALS, key=len, reverse=True))

# "Order XXI", "Order XXI Rule 54", "Order XV-A" — case-sensitive on the
# numeral itself (real citations are always capitalised), whitelisted set.
ORDER_RULE_RX = re.compile(
    rf"\bOrder\s+({_ORDER_ALT})(-A)?\b\s*(?:,?\s*Rule\s+(\d{{1,3}}[A-Za-z]?))?"
)
O_R_ABBR_RX = re.compile(
    rf"\bO\.\s*({_ORDER_ALT})(-A)?\.?\s*,?\s*R\.\s*(\d{{1,3}}[A-Za-z]?)"
)

# Amendment/footnote lines (e.g. "1. Subs. by Act 2 of 1951, s. 3, for ...")
# get embedded inline in the ingested body text. Their "s. 3" / "Act X of Y"
# refer to the AMENDING ACT's section, not a CPC cross-reference — strip
# these lines before scanning, or every section would wrongly "link" to
# whatever section number happens to appear in its own footnotes.
_FOOTNOTE_LEAD_RX = re.compile(r"^\s*\d{1,3}\.\s")
_FOOTNOTE_SIGNAL_RX = re.compile(
    r"(Subs\.|Ins\.|Omitted|Rep\.|Added|Renumbered|renumbered|w\.e\.f\.|"
    r"Act\s+\d+\s+of\s+\d{4}|A\.O\.\s*\d{4}|Substituted|Inserted)"
)


def _strip_footnotes(text):
    """Drop numbered footnote/amendment-history lines. These are always
    lead-numbered ('N. ...') AND carry an amendment signal (Subs./Ins./
    'Act X of YYYY'/'w.e.f.'/etc) — both conditions together avoid
    stripping genuine numbered list items in the operative text."""
    kept = []
    for line in text.splitlines():
        if _FOOTNOTE_LEAD_RX.match(line) and _FOOTNOTE_SIGNAL_RX.search(line):
            continue
        kept.append(line)
    return "\n".join(kept)


def extract_refs(text, self_kind=None, self_ref=None):
    """Return a de-duplicated, ordered list of reference dicts:
    {'kind': 'section'|'order_rule', 'label': str, 'section_no': ..} or
    {'kind': 'order_rule', 'order_no':.., 'rule_no': .. or None, 'label':..}
    Excludes a self-reference if self_kind/self_ref given.
    """
    found = []
    seen = set()
    text = _strip_footnotes(text)

    for rx in (SECTION_RX, S_ABBR_RX):
        for m in rx.finditer(text):
            no = m.group(1)
            key = ("section", no)
            if key in seen:
                continue
            if self_kind == "section" and self_ref == no:
                continue
            seen.add(key)
            found.append({"kind": "section", "section_no": no, "label": f"Section {no}"})

    for rx in (ORDER_RULE_RX, O_R_ABBR_RX):
        for m in rx.finditer(text):
            order_no = m.group(1) + (m.group(2) or "")
            rule_no = m.group(3)
            key = ("order_rule", order_no, rule_no)
            if key in seen:
                continue
            seen.add(key)
            label = f"Order {order_no}" + (f" Rule {rule_no}" if rule_no else "")
            found.append({"kind": "order_rule", "order_no": order_no, "rule_no": rule_no, "label": label})

    return found


def resolve_refs(db, refs):
    """Resolve extracted refs against the database. Returns list of
    dicts with an added 'target' (row) or None if not found locally."""
    resolved = []
    for r in refs:
        if r["kind"] == "section":
            row = db.get_section_by_no(r["section_no"])
            resolved.append({**r, "target_kind": "section", "target": row})
        else:
            order_row = db.find_order_by_no(r["order_no"])
            if order_row and r["rule_no"]:
                rule_row = db.find_rule_in_order(r["order_no"], r["rule_no"])
                resolved.append({**r, "target_kind": "rule", "target": rule_row})
            elif order_row:
                resolved.append({**r, "target_kind": "order", "target": order_row})
            else:
                resolved.append({**r, "target_kind": "order", "target": None})
    return resolved
