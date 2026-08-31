"""
Deterministic State Amendment splitter (Part 5 of the spec).

The ingested `state_amendments` column is a single flat blob per
provision that can mix several states' amendment notes together (see
e.g. Section 60, which carries Kerala + Himachal Pradesh + Tamil Nadu
+ Rajasthan + Uttar Pradesh notes back to back). This module splits
that blob into per-state segments using the state names as they
literally appear as standalone header lines in the source text —
no inference, no rewriting, no correction of the underlying source.

If the source text has an error or a mislabeled block, that error is
preserved verbatim: this is a structural split only.
"""
import re

# States actually covered in the CPC bare-act text, per the spec.
# Canonical name -> list of literal spellings seen in the source text
# (the bare act itself misspells "Orissa" as "Orrisa" in at least one
# place — recognised here for grouping purposes only; the stored text
# is never altered).
STATE_ALIASES = {
    "Jammu and Kashmir and Ladakh": ["Jammu and Kashmir and Ladakh"],
    "Uttar Pradesh": ["Uttar Pradesh"],
    "Maharashtra": ["Maharashtra"],
    "Kerala": ["Kerala"],
    "Rajasthan": ["Rajasthan"],
    "Karnataka": ["Karnataka"],
    "Tamil Nadu": ["Tamil Nadu"],
    "Himachal Pradesh": ["Himachal Pradesh"],
    "Assam": ["Assam"],
    "Orissa": ["Orissa", "Orrisa"],
    "Punjab": ["Punjab"],
}
KNOWN_STATES = list(STATE_ALIASES.keys())

_ALIAS_TO_CANONICAL = {
    alias: canonical for canonical, aliases in STATE_ALIASES.items() for alias in aliases
}
# Longest-first, and "Jammu and Kashmir and Ladakh" before any shorter
# alias, so the header match is greedy on the correct full name.
_ALL_ALIASES = sorted(_ALIAS_TO_CANONICAL.keys(), key=len, reverse=True)

# A header line is (almost) just the state name, optionally with a
# parenthetical like "(UTs)" and/or trailing punctuation such as
# ".—", ". —", "-", "—" in any whitespace/punctuation combination.
_HEADER_RX = re.compile(
    r"^\s*(" + "|".join(re.escape(s) for s in _ALL_ALIASES) + r")"
    r"(\s*\([^)]*\))?"
    r"[\s.\u2014\-—]*$"
)


def split_by_state(blob):
    """Return an ordered dict-like list of (state_name_or_None, text)
    segments. state_name is None for any text appearing before the
    first recognised state header (rare, but preserved rather than
    dropped)."""
    if not blob or not blob.strip():
        return []

    segments = []
    current_state = None
    current_lines = []

    for line in blob.splitlines():
        m = _HEADER_RX.match(line)
        if m:
            if current_lines:
                segments.append((current_state, "\n".join(current_lines).strip()))
            current_state = _ALIAS_TO_CANONICAL[m.group(1)]
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        segments.append((current_state, "\n".join(current_lines).strip()))

    return [(s, t) for s, t in segments if t]


def states_present(blob):
    """Which known states have at least one segment in this blob."""
    return sorted({s for s, _ in split_by_state(blob) if s})


def text_for_state(blob, state_name):
    """Concatenate all segments matching state_name (a provision can
    have more than one block for the same state, as with S.60/UP)."""
    parts = [t for s, t in split_by_state(blob) if s == state_name]
    return "\n\n".join(parts)
