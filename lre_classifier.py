"""
LexOffline — Deterministic Legal Reasoning Engine (LRE)
Module 2: Deterministic Fact Classifier (lre_classifier.py)

Rule-based fact extraction and deterministic classification without ML/AI:
Classifies material facts into:
- PROVED: Backed by registered deed, public/revenue record, official certificate, or RTGS bank record.
- ADMITTED: Formally conceded in pleadings, notices, or admitted by party against interest.
- PLEADED: Asserted in plaint/WS awaiting proof at trial (e.g. oral agreement, unrecorded payment).
- DISPUTED: Directly conflicting assertions creating an issue under Order XIV Rule 1.
- ASSUMED: Working valuation or legal assumptions subject to verification.
- UNKNOWN: Critical missing facts or documentation requiring chamber instructions.
"""

import re


def extract_sentences(text):
    """Splits raw text into clean, non-empty sentences."""
    if not text:
        return []
    # Clean text
    clean = text.replace("\r\n", "\n").replace("\r", "\n")
    # Split on periods followed by space/newline or numbered bullet points
    raw_sentences = re.split(r'(?<=[.!?])\s+|\n+(?=[0-9A-Za-z\(\)])', clean)
    sentences = [s.strip() for s in raw_sentences if s.strip() and len(s.strip()) > 8]
    return sentences


def classify_sentence(sentence, context_flags=None):
    """
    Deterministically evaluates a sentence against procedural and evidentiary rules.
    Returns: (classification, confidence_reason, linked_issue, statutory_implication)
    """
    s_lower = sentence.lower()
    
    # 1. Check for PROVED facts: Registered deeds, bank records, official certificates
    if any(k in s_lower for k in [
        "registered sale deed", "registered settlement deed", "registered mortgage",
        "registered document", "death certificate", "legal heir", "rtgs", "encumbrance certificate"
    ]):
        return (
            "PROVED",
            "Backed by primary registered document, official revenue certificate, or verified banking transaction.",
            "Title & Devolution of Rights",
            "Admissible as primary evidence under Sections 61, 62 & 35 of the Indian Evidence Act, 1872."
        )

    # 2. Check for ADMITTED facts: Admission against interest, possession concessions
    if any(k in s_lower for k in [
        "plaintiff admits", "admitted", "defendant is in possession", "claims to have been in possession",
        "put up a small structure", "protested orally but did not file"
    ]):
        return (
            "ADMITTED",
            "Fact conceded by party against interest or uncontradicted on contemporaneous record.",
            "Possession & Physical Control",
            "Operates as admission under Section 17/58 IEA; triggers Section 34 SRA Proviso possession bar."
        )

    # 3. Check for DISPUTED facts: Conflicting claims, denial in reply, ouster, rival patta
    if any(k in s_lower for k in [
        "denied", "denying", "disputed", "written statement contending", "contends",
        "barred by limitation", "ouster", "exclusive title", "undervalued", "res judicata"
    ]):
        return (
            "DISPUTED",
            "Conflicting rival contentions pleaded between parties, requiring judicial trial.",
            "Triable Issue under Order XIV Rule 1",
            "Forms basis of distinct issue of fact or law under Order XIV Rule 1 CPC."
        )

    # 4. Check for PLEADED facts: Oral agreement, oral arrangement, unverified cultivation
    if any(k in s_lower for k in [
        "orally agreed", "oral agreement", "oral family arrangement", "plaintiff claims that",
        "continued cultivating", "accepted agricultural income", "believed that"
    ]):
        return (
            "PLEADED",
            "Averment made in pleading without registered documentary corroboration.",
            "Enforceability of Oral Agreement",
            "Burden of proof lies squarely on plaintiff under Section 101/102 IEA; hit by Section 17/49 Registration Act if claiming title."
        )

    # 5. Check for ASSUMED facts: Valuation, general knowledge
    if any(k in s_lower for k in [
        "guideline value is", "valued at", "assumed", "estimated market value", "court-fee and jurisdiction"
    ]):
        return (
            "ASSUMED",
            "Valuation or procedural benchmark assumed for filing, subject to Section 12(2) Court Fees audit.",
            "Pecuniary Competence & Valuation",
            "Subject to court enquiry under Section 12(2) of TN Court-Fees Act, 1955."
        )

    # Default fallback: Treat as PLEADED if affirmative, else UNKNOWN
    if any(v in s_lower for v in ["is", "was", "has", "had", "filed", "issued", "purchased"]):
        return (
            "PLEADED",
            "Statement of fact pleaded by party requiring standard trial proof.",
            "Factual Foundation",
            "Requires proof through deposition under Order XVIII Rule 4 CPC."
        )
    else:
        return (
            "UNKNOWN",
            "Ambiguous or incomplete factual assertion requiring chamber verification.",
            "Evidentiary Gap",
            "Needs specific instructions from client before framing pleadings."
        )


def analyze_facts(narrative_text, structured_docs=None):
    """
    Extracts, classifies, and indexes all material facts from narrative and documents.
    """
    sentences = extract_sentences(narrative_text)
    classified_facts = []

    for s in sentences:
        classification, reason, issue, implication = classify_sentence(s)
        classified_facts.append({
            "fact": s,
            "classification": classification,
            "confidence_reason": reason,
            "linked_issue": issue,
            "statutory_implication": implication
        })

    # Add missing/unknown indicators based on legal prerequisites
    # Check if co-heirs' consent is mentioned
    text_lower = narrative_text.lower()
    if "widow" in text_lower or "mother" in text_lower or "three children" in text_lower:
        if not any("mother is party" in s.lower() or "other sibling" in s.lower() for s in sentences):
            classified_facts.append({
                "fact": "Status, whereabouts, and consent of the Mother and remaining sibling (co-heirs).",
                "classification": "UNKNOWN",
                "confidence_reason": "Plaint narrative mentions 4 heirs of father A, but fails to account for why two heirs are omitted.",
                "linked_issue": "Non-Joinder of Necessary Parties",
                "statutory_implication": "Fatal bar under Order I Rule 9 Proviso if suit is maintained without all co-sharers."
            })

    if "guideline" not in text_lower and "stamp" not in text_lower:
        classified_facts.append({
            "fact": "Official guideline value per acre for the suit village from Registration Department.",
            "classification": "UNKNOWN",
            "confidence_reason": "Plaint states valuation at ₹9,50,000 without citing official guideline value certificate.",
            "linked_issue": "Pecuniary Jurisdiction & Court Fee",
            "statutory_implication": "Risk of rejection under Order VII Rule 11(b) CPC and Section 12(2) TN Court-Fees Act."
        })

    return classified_facts
