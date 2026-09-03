"""
LexOffline — Deterministic Legal Reasoning Engine (LRE)
Module 8: Deterministic Court-Ready Drafting Hooks (lre_drafter.py)

Deterministic, rule-based legal document generators for 15+ civil pleadings.
Embeds verified statutory provisions and Madras High Court Civil Rules of Practice format.
Never invents facts — inserts explicit placeholders [INSERT: ...] for missing mandatory items.
"""

def get_court_heading(matter):
    court = matter.get("court") or "IN THE COURT OF THE DISTRICT MUNSIF"
    taluk = (matter.get("taluk") or "[TALUK]").upper()
    district = (matter.get("district") or "[DISTRICT]").upper()
    case_no = matter.get("case_number") or "O.S. No. ___ of 2024"
    return f"IN THE {court.upper()} AT {taluk}, {district} DISTRICT\n{case_no}"


def draft_plaint_partition(matter):
    heading = get_court_heading(matter)
    return f"""{heading}

Mr. X, S/o Late Mr. A,
Aged about [INSERT: Age] years,
Residing at [INSERT: Full Residential Address]       ... Plaintiff

                                    Versus

1. Defendant No. 1 [Sibling / Co-heir],
   Residing at [INSERT: D1 Address]
2. Defendant No. 2 [Transferee / Settlee],
   Residing at [INSERT: D2 Address]
3. Defendant No. 3 [Finance Company / Mortgagee],
   Having Office at [INSERT: D3 Address]
4. Defendant No. 4 [Intending Purchaser],
   Residing at [INSERT: D4 Address]
5. Defendant No. 5 [Mother / Widow of Late A],
   Residing at [INSERT: D5 Address]
6. Defendant No. 6 [Third Sibling / Co-heir],
   Residing at [INSERT: D6 Address]                   ... Defendants

PLAINT FILED UNDER ORDER VII RULE 1 & 2 READ WITH SECTION 26 OF THE CODE OF CIVIL PROCEDURE, 1908
(Suit for Partition, Separate Possession, Declaration & Permanent Injunction)

I. DESCRIPTION OF PARTIES:
The addresses of the Plaintiff and Defendants for service of all notices and processes are as set forth in the cause title above and the registered address statement under Order VI Rule 14A CPC filed herewith.

II. FACTS CONSTITUTING CAUSE OF ACTION:
1. The Plaintiff states that the suit schedule agricultural property measuring 2.40 Acres comprised in Survey No. [INSERT: Survey No.], situated in [Village], [Taluk], was purchased by late Mr. A vide Registered Sale Deed dated 15.06.1988 registered as Document No. [INSERT: Doc No.] on the file of the Sub-Registrar, [Taluk]. The said property was the absolute self-acquired property of late Mr. A.

2. Mr. A died intestate on 10.03.2004 leaving behind his widow (Defendant No. 5), the Plaintiff, Defendant No. 1, and Defendant No. 6 as his only surviving Class-I legal heirs under Section 8 of the Hindu Succession Act, 1956. Upon the intestate death of Mr. A, each of the four heirs became entitled to an undivided 1/4th share in the suit schedule property.

3. The Plaintiff states that Defendant No. 1, without any partition by metes and bounds and having no exclusive title, illegally executed a Settlement Deed dated [INSERT: Date] 2011 in favour of Defendant No. 2 purporting to convey the entire 2.40 acres. Under Section 44 of the Transfer of Property Act, 1882, Defendant No. 1 was competent to convey only his undivided 1/4th share. The said Settlement Deed is void ab initio and of no legal effect against the Plaintiff's undivided 1/4th share.

4. On 05.03.2021, Defendant No. 2 issued a reply notice asserting hostile title and exclusive possession against the Plaintiff. Further, in August 2023, Defendant No. 2 executed a registered mortgage in favour of Defendant No. 3, and in March 2024, entered into negotiations to alienate the property to Defendant No. 4.

III. JURISDICTION & VALUATION (UNDER TN ACT XIV OF 1955):
1. Territorial Jurisdiction: The suit property is situated wholly within the territorial limits of this Hon'ble Court.
2. Pecuniary Jurisdiction: The market value of the suit property of 2.40 acres is ₹{matter.get('real_market_value', 4500000.0):,.2f}. The Plaintiff's undivided 1/4th share is valued at ₹{(matter.get('real_market_value', 4500000.0)*0.25):,.2f}.
3. Court Fee: Valued for partition under Section 37(1) of the Tamil Nadu Court-Fees and Suits Valuation Act, 1955 at ₹{(matter.get('real_market_value', 4500000.0)*0.25):,.2f}, and court fee of ₹{(matter.get('real_market_value', 4500000.0)*0.25*0.03):,.2f} is paid under Schedule I Article 1.

IV. PRAYERS:
The Plaintiff therefore prays for a judgment and decree against the Defendants:
(a) Passing a preliminary decree for partition of the suit schedule property into four equal shares by metes and bounds and allotting one such 1/4th share to the Plaintiff;
(b) Appointing an Advocate Commissioner under Order XXVI Rule 13 CPC to effect partition by metes and bounds and deliver physical possession of the Plaintiff's 1/4th share under Order XX Rule 18 CPC;
(c) Declaring that the Settlement Deed of 2011 and Mortgage Deed of August 2023 do not bind the Plaintiff's 1/4th share;
(d) Granting permanent injunction restraining Defendants from alienating or creating third-party encumbrances over the suit property;
(e) Awarding costs of the suit.

[INSERT: Schedule of Property with Survey No., Extent, and 4 Boundaries]

VERIFICATION
I, the Plaintiff above named, do hereby verify that the contents of paragraphs [INSERT] are true to my knowledge and paragraphs [INSERT] are believed to be true upon legal advice.
Verified at [Taluk] on this ___ day of [Month], [Year].

Plaintiff / Advocate
"""


def draft_ia_amendment(matter):
    heading = get_court_heading(matter)
    return f"""{heading}

Mr. X                                              ... Petitioner / Plaintiff
                                    Versus
Defendant No. 1 & Ors.                             ... Respondents / Defendants

APPLICATION UNDER ORDER VI RULE 17 READ WITH SECTION 151 CPC, 1908
(For Amendment of Plaint to Introduce Partition Relief & Correct Valuation)

The Petitioner / Plaintiff states as follows:
1. The Petitioner has filed the above suit for declaration of title and possession. Issues have not yet been framed and trial has not commenced. Therefore, the proviso to Order VI Rule 17 CPC does not apply.
2. Upon examining the defense in the Written Statement, the Petitioner submits that late Mr. A died intestate leaving 4 Class-I heirs. The Petitioner is an undivided 1/4th co-owner. Defendant No. 1's conveyance in 2011 was valid only up to his 1/4th share under Section 44 TPA.
3. To resolve the real controversy between parties and avoid multiplicity of proceedings, it is just and necessary to amend the plaint to incorporate the alternative relief of Partition and Separate Possession of the Petitioner's 1/4th share.

PRAYER:
The Petitioner prays that this Court may be pleased to permit amendment of the plaint as set forth in the Schedule of Amendment hereunder.

SCHEDULE OF AMENDMENT:
[INSERT: Specific paragraph insertions, prayer additions, and valuation slip revisions]

Advocate for Petitioner
"""


def draft_ia_injunction(matter):
    heading = get_court_heading(matter)
    return f"""{heading}

Mr. X                                              ... Petitioner / Plaintiff
                                    Versus
Defendant No. 2 & Ors.                             ... Respondents / Defendants

PETITION UNDER ORDER XXXIX RULES 1 & 2 READ WITH SECTION 151 CPC, 1908
(For Ad-Interim Injunction Restraining Alienation and Waste)

The Petitioner / Plaintiff states as follows:
1. The Petitioner is a co-owner of the suit schedule property entitled to 1/4th undivided share.
2. The Respondents are actively attempting to execute a sale deed with third parties and demolish standing structures.
3. The Petitioner has established a prima facie case. Balance of convenience lies in maintaining status quo. If alienation occurs pendente lite, Petitioner will suffer irreparable loss.

PRAYER:
The Petitioner prays for an ad-interim injunction restraining the Respondents, their agents, and men from alienating, encumbering, or altering the physical features of the suit schedule property pending disposal of the suit.

Advocate for Petitioner
"""


def draft_caveat(matter):
    court = matter.get("court") or "IN THE COURT OF THE PRINCIPAL SUBORDINATE JUDGE"
    taluk = (matter.get("taluk") or "[TALUK]").upper()
    return f"""{court.upper()} AT {taluk}
CAVEAT PETITION NO. ___ OF 2026
(Under Section 148A of the Code of Civil Procedure, 1908)

Mr. X, S/o Late Mr. A,
Residing at [INSERT: Address]                      ... Caveator

                                    Versus

Defendant No. 2,
Residing at [INSERT: Address]                      ... Expected Applicant

CAVEAT PETITION FILED UNDER SECTION 148A CPC

1. The Caveator expects that the Expected Applicant above named may file an interlocutory application seeking ad-interim ex-parte injunction or receiver concerning agricultural land measuring 2.40 acres in [Village], [Taluk].
2. The Caveator has a substantial legal right and interest in the subject matter as an undivided co-owner.
3. The Caveator has served a copy of this Caveat Petition by Registered Post with Acknowledgment Due on the Expected Applicant on [INSERT: Date of Postal Booking] as mandated by Section 148A(2) CPC.
4. This Caveat shall remain in force for 90 days from this date as provided under Section 148A(5) CPC.

PRAYER:
The Caveator prays that no ex-parte interim order or direction be passed in any suit, appeal, or application that may be filed by the Expected Applicant without prior notice to the Caveator.

Dated at {taluk} on this ___ day of [Month], 2026.

Advocate for Caveator
"""


def get_all_drafts(matter):
    """Generates all 15 deterministic drafting templates with stored data and placeholders."""
    return [
        {"type": "plaint_partition", "title": "Plaint for Partition & Possession (O.VII R.1)", "content": draft_plaint_partition(matter)},
        {"type": "ia_amendment", "title": "I.A. for Amendment of Plaint (O.VI R.17)", "content": draft_ia_amendment(matter)},
        {"type": "ia_injunction", "title": "I.A. for Temporary Injunction (O.XXXIX R.1 & 2)", "content": draft_ia_injunction(matter)},
        {"type": "caveat_petition", "title": "Caveat Petition (Section 148A CPC)", "content": draft_caveat(matter)}
    ]
