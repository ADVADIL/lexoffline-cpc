"""
Authoritative Court-Ready Legal Drafting Templates & Form Library
for Code of Civil Procedure, 1908 & The Limitation Act, 1963.
Contains 54 full, court-tested petition drafts, interlocutory applications,
statutory notices, plaints, execution petitions, and appellate memoranda.
All templates feature bracketed placeholders e.g. [PLAINTIFF NAME], [DATE],
statutory authorities, practice notes, and connected provision references.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class DraftingTemplate:
    id: str
    title: str
    provision: str
    category: str
    summary: str
    practice_notes: str
    template_text: str
    connected_provisions: List[Dict[str, str]] = field(default_factory=list)


TEMPLATES: List[DraftingTemplate] = [
    # -------------------------------------------------------------------------
    # 1. CAVEAT PETITION (SECTION 148A)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="caveat_sec_148a",
        title="Caveat Petition & Supporting Affidavit",
        provision="Section 148A CPC",
        category="Pre-Emptive & Protective Proceedings",
        summary="Pre-emptive protective petition lodged to prevent ex-parte ad-interim orders in anticipated suits, appeals, or interlocutory applications.",
        practice_notes="Under Section 148A(5), caveat remains in force for exactly 90 days. Caveator must serve copy of caveat by RPAD on the expected applicant and file postal receipt/track consignment before the registry.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 148A", "title": "Right to lodge a caveat"},
            {"kind": "rule", "ref": "Order XXXIX Rule 1", "title": "Cases in which temporary injunction may be granted"}
        ],
        template_text="""IN THE COURT OF THE [PRINCIPAL DISTRICT JUDGE / CIVIL JUDGE SENIOR DIVISION] AT [CITY/TALUK]
CAVEAT PETITION NO. _______ OF 202[ ]

IN THE MATTER OF:
[CAVEATOR FULL NAME],
Aged about [ ] years, S/o or D/o [PARENT NAME],
Residing at [FULL RESIDENTIAL ADDRESS],
Contact: [PHONE / EMAIL]                                                ... CAVEATOR
VERSUS
[EXPECTED APPLICANT / OPPOSITE PARTY NAME],
Aged about [ ] years, S/o or D/o [PARENT NAME],
Residing at [FULL RESIDENTIAL ADDRESS]                                  ... EXPECTED APPLICANT

CAVEAT PETITION UNDER SECTION 148A OF THE CODE OF CIVIL PROCEDURE, 1908

The Caveator above named respectfully submits as under:

1. That the Caveator is the absolute owner and in lawful possession of the property described in the Schedule hereunder, having acquired the same by virtue of [SALE DEED / INHERITANCE / GIFT DEED] dated [DATE], registered as Document No. [ ] at SRO [OFFICE NAME].

2. That the Expected Applicant has no manner of right, title, or interest over the Schedule Property, but has recently on [DATE OF INCIDENT / THREAT] held out open threats to dispossess the Caveator / interfere with peaceful possession / alienate the property / institute false civil proceedings.

3. That the Caveator has genuine, reasonable, and grave apprehension that the Expected Applicant is likely to institute a Civil Suit, Original Petition, or Interlocutory Application for Temporary Injunction / Status Quo / Ex-Parte Ad-Interim Order before this Hon'ble Court without notice to the Caveator.

4. That if any ex-parte ad-interim order is passed in favour of the Expected Applicant without hearing the Caveator, the Caveator shall suffer irreparable injury, severe prejudice, and grave hardship which cannot be compensated in terms of money.

5. That the Caveator is entitled to prior notice of any suit, appeal, or application that may be filed by the Expected Applicant relating to the Schedule Property.

6. That as required under Section 148A(2) CPC, a copy of this Caveat Petition has been dispatched to the Expected Applicant by Registered Post with Acknowledgement Due (RPAD) on [DATE OF DISPATCH] vide Postal Receipt No. [ ], which is annexed herewith.

PRAYER:
Wherefore, the Caveator respectfully prays that this Hon'ble Court may be pleased to:
(a) Lodge and register this Caveat Petition on the file of this Hon'ble Court;
(b) Direct that no ex-parte ad-interim order, injunction, or stay be passed in any Suit, Appeal, or Interlocutory Application filed by the Expected Applicant against the Caveator concerning the Schedule Property without prior due notice of the hearing to the Caveator or his Counsel;
(c) Grant such other and further reliefs as this Hon'ble Court deems fit in the interest of justice and equity.

SCHEDULE OF PROPERTY
[Insert detailed description: Municipal/Sy No., Boundaries East, West, North, South, Extent in Sq.Ft/Acres]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR CAVEATOR


VERIFICATION AFFIDAVIT
I, [CAVEATOR FULL NAME], aged about [ ] years, residing at [ADDRESS], do hereby solemnly affirm and state on oath as follows:
1. I am the Caveator in the accompanying petition and am fully conversant with the facts of the case.
2. The averments made in Paragraphs 1 to 6 of the Caveat Petition and the Schedule are true and correct to the best of my personal knowledge and information.
Solemnly affirmed at [CITY] on this [DAY] of [MONTH], 202[ ]
                                                        DEPONENT
"""
    ),

    # -------------------------------------------------------------------------
    # 2. TEMPORARY INJUNCTION (ORDER XXXIX RULES 1 & 2)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="injunction_o39_r1_2",
        title="Application for Temporary Injunction & Supporting Affidavit",
        provision="Order XXXIX Rules 1 & 2 CPC",
        category="Interlocutory Applications",
        summary="Court application for urgent ad-interim temporary injunction restraining defendant from alienating property, creating third-party rights, or dispossessing plaintiff.",
        practice_notes="Must establish the 3-prong test: (1) Strong Prima Facie Case; (2) Balance of Convenience in applicant's favour; (3) Irreparable Injury that cannot be compensated in damages (Dalpat Kumar v. Prahlad Singh). If ex-parte order is obtained, must comply with Rule 3 Proviso on same day or immediate next day.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXXIX Rule 1", "title": "Cases in which temporary injunction may be granted"},
            {"kind": "rule", "ref": "Order XXXIX Rule 2", "title": "Injunction to restrain repetition or continuance of breach"},
            {"kind": "rule", "ref": "Order XXXIX Rule 3", "title": "Before granting injunction, Court to direct notice to opposite party"},
            {"kind": "rule", "ref": "Order XXXIX Rule 3A", "title": "Court to dispose of application for injunction within thirty days"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

IN THE MATTER OF:
[PLAINTIFF FULL NAME]                                              ... APPLICANT / PLAINTIFF
VERSUS
[DEFENDANT FULL NAME]                                              ... RESPONDENT / DEFENDANT

APPLICATION UNDER ORDER XXXIX RULES 1 & 2 READ WITH SECTION 151 CPC

The Applicant / Plaintiff respectfully submits as under:

1. That the Plaintiff has instituted the accompanying Suit against the Defendant praying for [PERMANENT INJUNCTION / SPECIFIC PERFORMANCE / DECLARATION OF TITLE]. The contents of the Plaint may kindly be read as part and parcel of this Application to avoid repetition.

2. PRIMA FACIE CASE:
That the Plaintiff has a strong prima facie case on merits. The Plaintiff is the lawful owner in peaceful physical possession of the Suit Schedule Property by virtue of [REGISTERED SALE DEED / TITLE DEED] dated [DATE]. The revenue entries, property tax receipts, and electricity bills stand mutated in the name of the Plaintiff.

3. BALANCE OF CONVENIENCE:
That the balance of convenience lies entirely in favour of the Plaintiff and against the Defendant. The Plaintiff is running a lawful business / residing in the Suit Property with his family, whereas the Defendant has no manner of title, right, or possession over the property.

4. IRREPARABLE INJURY:
That on [DATE OF RECENT THREAT], the Defendant along with his henchmen unlawfully attempted to trespass into the Suit Property / threatened to create third-party encumbrances / alter the physical status. If the Defendant is not immediately restrained by an ad-interim order of temporary injunction, the Plaintiff will suffer irreparable injury and catastrophic loss that cannot be quantified or compensated in monetary terms, and the subject matter of the Suit will be irreversibly damaged.

5. URGENCY & EX-PARTE RELIEF (RULE 3 PROVISO):
That the object of granting the injunction would be defeated by delay if prior notice is issued to the Defendant, as the Defendant is threatening to alienate the property / alter the status quo forthwith. The Plaintiff undertakes to strictly comply with the Proviso to Order XXXIX Rule 3 CPC immediately upon grant of the ad-interim order.

PRAYER:
Wherefore, the Applicant / Plaintiff prays that this Hon'ble Court may be pleased to:
(a) Pass an ad-interim ex-parte order of Temporary Injunction restraining the Respondent / Defendant, his agents, servants, or anyone claiming through him from [DISPOSSESSING THE PLAINTIFF / ALIENATING OR CREATING THIRD-PARTY RIGHTS / ALTERING THE PHYSICAL FEATURES] in respect of the Suit Schedule Property, pending disposal of the Suit;
(b) Confirm the said interim order after hearing the Respondent;
(c) Grant such other reliefs as this Hon'ble Court deems fit in the interest of justice.

SCHEDULE OF SUIT PROPERTY
[Insert detailed description with survey number, boundaries East, West, North, South, and extent]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 3. SETTING ASIDE EX-PARTE DECREE (ORDER IX RULE 13)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="set_aside_ex_parte_o9_r13",
        title="Application to Set Aside Ex-Parte Decree & Condonation of Delay",
        provision="Order IX Rule 13 CPC r/w Section 5 Limitation Act",
        category="Post-Decree & Restoration Remedies",
        summary="Application by defendant to set aside an ex-parte decree on grounds of non-service of summons or sufficient cause preventing appearance, with composite condonation application under Section 5.",
        practice_notes="Limitation under Article 123 is 30 days from date of decree, or where summons was not duly served, 30 days from date of KNOWLEDGE of the decree. Second proviso to Rule 13: Court shall not set aside decree merely on irregularity of service if satisfied defendant had notice in time.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order IX Rule 13", "title": "Setting aside decree ex parte against defendant"},
            {"kind": "section", "ref": "Section 5", "title": "Extension of prescribed period in certain cases (Limitation Act)"},
            {"kind": "limitation_article", "ref": "Article 123", "title": "To set aside a decree passed ex parte (30 days)"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
MISC. CIVIL APPLICATION NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

IN THE MATTER OF:
[DEFENDANT FULL NAME]                                              ... APPLICANT / DEFENDANT
VERSUS
[PLAINTIFF FULL NAME]                                              ... RESPONDENT / PLAINTIFF

APPLICATION UNDER ORDER IX RULE 13 READ WITH SECTION 151 CPC FOR SETTING ASIDE EX-PARTE DECREE

The Applicant / Defendant respectfully submits as under:

1. That the Respondent / Plaintiff instituted the above Suit O.S. No. [ ] of 202[ ] against the Applicant for [RELIEF SOUGHT IN SUIT].

2. That this Hon'ble Court was pleased to pass an Ex-Parte Judgment and Decree dated [DATE OF EX-PARTE DECREE] against the Applicant.

3. GROUNDS FOR SETTING ASIDE EX-PARTE DECREE:
[CHOOSE APPLICABLE GROUND (A) OR (B)]
(A) NON-SERVICE OF SUMMONS:
That summons in the suit was never duly served upon the Applicant. The address shown in the Plaint cause-title was incorrect / incomplete / Applicant had shifted residence to [NEW ADDRESS] on [DATE]. The bailiff endorsement reporting service / refusal is fraudulent, collusive, and manufactured. The Applicant had absolutely no knowledge of the institution or pendency of the Suit.
OR
(B) SUFFICIENT CAUSE FOR NON-APPEARANCE:
That summons was served, but the Applicant was prevented by sufficient cause from appearing on [DATE CASE WAS CALLED]: [EXPLAIN REASON: GRAVE ILLNESS / HOSPITALIZATION / DEATH IN FAMILY / WRONG DATE NOTED BY CLERK]. The medical certificates and hospital discharge summary are annexed herewith as Annexure A.

4. DATE OF KNOWLEDGE & LIMITATION (ARTICLE 123):
That the Applicant first gained knowledge of the passing of the ex-parte decree only on [DATE OF KNOWLEDGE], when [EXPLAIN: e.g. Court Bailiff arrived with execution warrant / JD checked revenue records]. The present Application is filed within 30 days of the date of knowledge as prescribed under Article 123 of the Limitation Act, 1963.

5. SUBSTANTIAL DEFENSE ON MERITS:
That the Applicant has a meritorious and complete defense to the Suit. The Plaintiff's claim is false, frivolous, and barred by limitation. If the ex-parte decree is not set aside, the Applicant will be condemned unheard, causing irreparable miscarriage of justice.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Set aside the ex-parte judgment and decree dated [DATE] passed in O.S. No. [ ] of 202[ ];
(b) Restore the Suit O.S. No. [ ] of 202[ ] to its original file and stage;
(c) Permit the Applicant / Defendant to file Written Statement and contest the Suit on merits;
(d) Grant such other and further reliefs as deemed fit in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 4. TABULAR EXECUTION PETITION (ORDER XXI RULE 11(2))
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="execution_o21_tabular",
        title="Tabular Execution Petition (Mandatory 10-Column Civil Format)",
        provision="Order XXI Rule 11(2) CPC",
        category="Execution Proceedings",
        summary="Mandatory statutory format for executing civil decrees for money recovery, attachment, and sale of judgment debtor's property.",
        practice_notes="Order XXI Rule 11(2) requires a written application containing in a tabular form all 10 statutory particulars (a) to (j). Certified copy of decree must be annexed (Rule 11(3)). Limitation under Article 136 is 12 years.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXI Rule 11", "title": "Application for execution"},
            {"kind": "rule", "ref": "Order XXI Rule 54", "title": "Attachment of immovable property"},
            {"kind": "limitation_article", "ref": "Article 136", "title": "Execution of decree (12 years)"}
        ],
        template_text="""IN THE COURT OF THE [PRINCIPAL DISTRICT JUDGE / SENIOR CIVIL JUDGE] AT [CITY]
EXECUTION PETITION NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[DECREE HOLDER FULL NAME]
Aged [ ] years, Residing at [ADDRESS]                               ... DECREE HOLDER (DH)
VERSUS
[JUDGMENT DEBTOR FULL NAME]
Aged [ ] years, Residing at [ADDRESS]                               ... JUDGMENT DEBTOR (JD)

EXECUTION PETITION UNDER ORDER XXI RULE 11(2) OF THE CODE OF CIVIL PROCEDURE, 1908

The Decree Holder respectfully submits the mandatory 10-column execution particulars:

+-----------------------------------------------------------------------------------------------+
| COLUMN NO. & STATUTORY REQUIREMENT                            | PARTICULARS                   |
+-----------------------------------------------------------------------------------------------+
| 1. Suit Number:                                               | O.S. No. [   ] of 202[ ]       |
+-----------------------------------------------------------------------------------------------+
| 2. Names of Parties:                                          | [DH NAME] vs [JD NAME]        |
+-----------------------------------------------------------------------------------------------+
| 3. Date of Decree:                                            | [DATE DECREE WAS PASSED]      |
+-----------------------------------------------------------------------------------------------+
| 4. Whether any Appeal preferred:                              | [None / Appeal dismissed on   |
|                                                               | DATE / No stay granted]       |
+-----------------------------------------------------------------------------------------------+
| 5. Whether any payment made since decree:                     | [None / Nil / Rs. _____ paid] |
+-----------------------------------------------------------------------------------------------+
| 6. Previous Execution Applications (if any, with dates):      | [First E.P. / E.P. No. ___    |
|                                                               | disposed on DATE]             |
+-----------------------------------------------------------------------------------------------+
| 7. Amount with interest due upon decree:                      | Principal:  Rs. [         ]   |
|                                                               | Interest:   Rs. [         ]   |
|                                                               | Costs:      Rs. [         ]   |
|                                                               | TOTAL:      Rs. [         ]   |
+-----------------------------------------------------------------------------------------------+
| 8. Amount of costs awarded by decree:                         | Rs. [         ] as per decree |
+-----------------------------------------------------------------------------------------------+
| 9. Against whom execution is sought:                          | [FULL NAME OF JUDGMENT DEBTOR]|
+-----------------------------------------------------------------------------------------------+
| 10. Mode in which Court's assistance is prayed:               | By attachment and sale of JD's|
|                                                               | immovable property described  |
|                                                               | in Schedule hereunder u/O XXI |
|                                                               | Rule 54 CPC; AND/OR           |
|                                                               | By arrest and detention of JD |
|                                                               | in civil prison u/O XXI R 37. |
+-----------------------------------------------------------------------------------------------+

SCHEDULE OF PROPERTY TO BE ATTACHED
[Insert detailed description: Survey No., Municipal Assessment No., Boundaries: East, West, North, South, Extent]

VERIFICATION:
I, [DECREE HOLDER NAME], the Decree Holder above named, do hereby verify that the contents of Columns 1 to 10 are true to the best of my knowledge and belief.
Verified at [CITY] on this [DAY] day of [MONTH], 202[ ]
                                                        DECREE HOLDER
"""
    ),

    # -------------------------------------------------------------------------
    # 5. LR SUBSTITUTION (ORDER XXII RULE 3/4)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="lr_substitution_o22_r3_4",
        title="Application for Substitution of Legal Representatives (LRs)",
        provision="Order XXII Rule 3 / Rule 4 CPC",
        category="Parties & Capacity",
        summary="Application to bring legal heirs / representatives of a deceased plaintiff (Rule 3) or deceased defendant (Rule 4) on record.",
        practice_notes="Limitation under Article 120 of Limitation Act is 90 days from the date of death. If not filed within 90 days, the suit abates automatically against the deceased party. If filed after 90 days, composite application to set aside abatement (Order XXII Rule 9, Article 121: 60 days) and condone delay under Section 5 must be filed.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXII Rule 3", "title": "Procedure in case of death of one of several plaintiffs or of sole plaintiff"},
            {"kind": "rule", "ref": "Order XXII Rule 4", "title": "Procedure in case of death of one of several defendants or of sole defendant"},
            {"kind": "limitation_article", "ref": "Article 120", "title": "To have the legal representative of a deceased party made a party (90 days)"},
            {"kind": "limitation_article", "ref": "Article 121", "title": "To set aside an abatement (60 days)"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

IN THE MATTER OF:
[PLAINTIFF NAME]                                                   ... PLAINTIFF / APPLICANT
VERSUS
[DEFENDANT NAME] (DECEASED)                                        ... DEFENDANT / RESPONDENT

APPLICATION UNDER ORDER XXII RULE 4 READ WITH SECTION 151 CPC

The Applicant / Plaintiff respectfully submits as under:

1. That the Plaintiff has instituted the above Suit against the Defendant for [PARTITION / INJUNCTION / SPECIFIC PERFORMANCE].

2. That the sole Defendant / Defendant No. [ ] died on [DATE OF DEATH] at [PLACE OF DEATH]. The Death Certificate issued by the Municipal Corporation / Registrar of Births & Deaths is annexed herewith as Annexure A.

3. That the right to sue survives against the legal representatives of the deceased Defendant.

4. That the deceased Defendant left behind the following surviving legal heirs / representatives who inherit the estate:
   (a) [NAME OF HEIR 1], Aged about [ ] years, [RELATIONSHIP: e.g. Widow / Son / Daughter], Residing at [ADDRESS].
   (b) [NAME OF HEIR 2], Aged about [ ] years, [RELATIONSHIP], Residing at [ADDRESS].

5. That apart from the persons mentioned above, there are no other legal heirs surviving the deceased Defendant.

6. That the present application is filed on [FILING DATE], which is within the statutory limitation period of 90 days from the date of death as prescribed under Article 120 of the Limitation Act, 1963.

PRAYER:
Wherefore, the Applicant / Plaintiff prays that this Hon'ble Court may be pleased to:
(a) Bring the proposed Legal Representatives (a) to (b) above named on record as Defendants No. [ ] to [ ] in the place of the deceased Defendant;
(b) Permit the Plaintiff to amend the Plaint cause-title accordingly;
(c) Issue summons / notice to the newly added Defendants; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 6. STATUTORY PRE-SUIT NOTICE TO GOVERNMENT (SECTION 80)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="notice_sec_80",
        title="Statutory Pre-Suit Notice to Government",
        provision="Section 80(1) CPC",
        category="Statutory Notices",
        summary="Mandatory 2-month statutory notice required before instituting any suit against the Government (Central/State) or a Public Officer in respect of any official act.",
        practice_notes="Section 80(1) requires notice to be delivered/left at the office of: (a) Secretary to Govt (Central/Railway/State); (b) Collector of the District. Suit cannot be instituted until expiration of 2 months next after notice delivered. If urgent interim relief is required, prior leave of court under Section 80(2) must be obtained.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 80", "title": "Notice"}
        ],
        template_text="""BY REGISTERED POST WITH ACKNOWLEDGEMENT DUE (RPAD)

Date: [DATE]

TO:
1. THE CHIEF SECRETARY,
   Government of [STATE NAME],
   State Secretariat, [CITY - PINCODE].

2. THE DISTRICT COLLECTOR / DEPUTY COMMISSIONER,
   [DISTRICT NAME], [CITY - PINCODE].

SUBJECT: NOTICE UNDER SECTION 80 OF THE CODE OF CIVIL PROCEDURE, 1908
INTENDED SUIT: [PLAINTIFF NAME] VERSUS STATE OF [STATE] & OTHERS

Sir / Madam,

Under instructions from and on behalf of my client, [CLIENT FULL NAME], aged about [ ] years, residing at [ADDRESS], I hereby serve upon you this Statutory Notice under Section 80 CPC:

1. IDENTITY & CAPACITY OF INTENDED PLAINTIFF:
My client is the absolute lawful owner in possession of [PROPERTY DESCRIPTION / BUSINESS] situated at [ADDRESS].

2. CAUSE OF ACTION & RELEVANT FACTS:
(a) That on [DATE], my client acquired the property vide Registered Sale Deed No. [ ]...
(b) That on [DATE], the officials of the Department of [ ] unlawfully attempted to demolish / interfere / cancel licence without following due process of law...
(c) That the said impugned action / Order No. [ ] dated [DATE] passed by [OFFICER DESIGNATION] is illegal, ultra vires, arbitrary, and violative of the principles of natural justice.

3. RELIEFS SOUGHT IN INTENDED SUIT:
My client intends to institute a Civil Suit before the competent Civil Court at [CITY] praying for:
(a) Declaration that [IMPUGNED ORDER / ACTION] is null, void, and non-est in the eye of law;
(b) Permanent Injunction restraining the Government, its officers, servants, and agents from interfering with my client's peaceful possession;
(c) Mandatory Injunction directing restoration of [STATUS / PROPERTY / COMPENSATION OF RS. ______].

TAKE NOTICE that you are hereby called upon to redress my client's grievance within two (2) months from the date of receipt of this notice, failing which my client will institute the aforesaid Civil Suit against the Government at your sole risk, cost, and consequences.

Yours faithfully,

[ADVOCATE NAME], Advocate
[ENROLLMENT NO., CHAMBER ADDRESS, PHONE, EMAIL]
"""
    ),

    # -------------------------------------------------------------------------
    # 7. GENERAL PLAINT SKELETON (ORDER VII)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="plaint_skeleton_o7",
        title="Plaint General Skeleton (Order VII CPC Compliant)",
        provision="Order VII CPC",
        category="Core Pleadings",
        summary="Complete civil plaint framework incorporating mandatory Order VII requirements: facts, cause of action, valuation, jurisdiction, court fees, prayer, and verification.",
        practice_notes="Order VII Rule 1 requires mandatory particulars: court name, parties, facts, cause of action date, jurisdiction, valuation, and specific relief. Plaint must be verified under Order VI Rule 15 and accompanied by Statement of Truth / Affidavit.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"},
            {"kind": "rule", "ref": "Order VII Rule 11", "title": "Rejection of plaint"},
            {"kind": "section", "ref": "Section 26", "title": "Institution of suits"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF FULL NAME],
Aged about [ ] years, S/o [PARENT NAME],
Residing at [ADDRESS]                                              ... PLAINTIFF
VERSUS
[DEFENDANT FULL NAME],
Aged about [ ] years, S/o [PARENT NAME],
Residing at [ADDRESS]                                              ... DEFENDANT

SUIT FOR [DECLARATION OF TITLE, PERMANENT INJUNCTION, AND POSSESSION]

The Plaintiff above named respectfully submits as under:

1. DESCRIPTION OF PARTIES:
(a) The Plaintiff is [OCCUPATION / CITIZEN], residing at the address given in the cause-title.
(b) The Defendant is [OCCUPATION / CITIZEN], residing at the address given in the cause-title.

2. CHRONOLOGICAL FACTS OF THE CASE:
(a) That the Plaintiff is the absolute owner of the Suit Schedule Property...
(b) That on [DATE], the Plaintiff purchased the property vide Sale Deed No. [ ]...
(c) That the Defendant on [DATE] without any semblance of right attempted to...

3. CAUSE OF ACTION:
That the cause of action for the Suit arose on [FIRST DATE: e.g. date of title acquisition], and subsequently on [DATE OF THREAT/INTERFERENCE], and finally on [RECENT DATE] when the Defendant refused to desist from his unlawful acts, within the territorial jurisdiction of this Hon'ble Court.

4. VALUATION & COURT FEES:
(a) The relief of Declaration is valued at Rs. [        ] under Section [  ] of the Court Fees and Suits Valuation Act, and court fee of Rs. [        ] is paid thereon.
(b) The relief of Permanent Injunction is valued at Rs. [        ], and court fee of Rs. [        ] is paid thereon.
Total Court Fee paid: Rs. [        ].

5. JURISDICTION:
(a) TERRITORIAL: The Suit Schedule Property is situated within the territorial limits of this Hon'ble Court.
(b) PECUNIARY: The total valuation of the suit is Rs. [        ], which falls well within the pecuniary jurisdiction of this Hon'ble Court.

6. LIMITATION:
The Suit is within the period of limitation prescribed under Article [   ] of the Limitation Act, 1963.

PRAYER:
Wherefore, the Plaintiff respectfully prays for a judgment and decree:
(a) Declaring that the Plaintiff is the absolute owner of the Suit Schedule Property;
(b) Granting a Permanent Injunction restraining the Defendant from interfering with possession;
(c) Awarding costs of this Suit;
(d) Granting such other reliefs as this Hon'ble Court deems fit in the interest of justice.

SCHEDULE OF SUIT PROPERTY
[Insert boundaries East, West, North, South, survey number, and total measurement]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF

VERIFICATION
I, [PLAINTIFF NAME], do hereby verify that the contents of Paragraphs 1 to [ ] are true to my personal knowledge, and Paragraphs [ ] to [ ] are based on legal advice believed by me to be true.
Verified at [CITY] on this [DAY] day of [MONTH], 202[ ]
                                                        PLAINTIFF
"""
    ),

    # -------------------------------------------------------------------------
    # 8. GENERAL WRITTEN STATEMENT (ORDER VIII)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="ws_skeleton_o8",
        title="Written Statement Skeleton (Order VIII CPC Compliant)",
        provision="Order VIII CPC",
        category="Core Pleadings",
        summary="Defense pleading incorporating preliminary legal objections, para-wise specific denials compliant with Rules 3 & 5, and verification.",
        practice_notes="Order VIII Rule 1 requires WS to be filed within 30 days of summons service (outer limit 90 days). Rule 3: denial must be specific; general denial is no denial. Rule 5: every allegation of fact not denied specifically or by necessary implication is deemed to be admitted.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VIII Rule 1", "title": "Written statement"},
            {"kind": "rule", "ref": "Order VIII Rule 3", "title": "Denial to be specific"},
            {"kind": "rule", "ref": "Order VIII Rule 5", "title": "Specific denial"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF NAME]                                                   ... PLAINTIFF
VERSUS
[DEFENDANT NAME]                                                   ... DEFENDANT

WRITTEN STATEMENT FILED BY THE DEFENDANT UNDER ORDER VIII RULE 1 CPC

The Defendant above named respectfully submits as under:

PRELIMINARY OBJECTIONS:
1. NO CAUSE OF ACTION: The Plaint discloses no cause of action against the Defendant and is liable to be rejected under Order VII Rule 11(a) CPC.
2. BARRED BY LIMITATION: The Suit is hopelessly barred by limitation under Article [  ] of the Limitation Act, 1963.
3. UNDERVALUATION & DEFICIENT COURT FEE: The suit has been deliberately undervalued to invoke the jurisdiction of this Court.
4. NON-JOINDER OF NECESSARY PARTIES: The Suit is bad for non-joinder of [NAME OF NECESSARY PARTY] under Order I Rule 9 CPC.

PARA-WISE REPLY ON MERITS:
1. That the averments in Paragraph 1 of the Plaint are matters of record.
2. That with reference to Paragraph 2 of the Plaint, it is SPECIFICALLY DENIED that the Plaintiff is the lawful owner or in possession of the Suit Property. The alleged Sale Deed dated [DATE] is void, sham, and nominal...
3. That the averments in Paragraph 3 are SPECIFICALLY DENIED as false and concocted. The Defendant never held out any threats...
4. [Continue specific para-wise denials complying with Order VIII Rules 3 & 5 CPC]...

DEFENDANT'S ADDITIONAL STATEMENT OF FACTS:
1. That the true and correct facts are that the Defendant has been in open, continuous, uninterrupted, and peaceful possession of the property since [YEAR]...

PRAYER:
Wherefore, the Defendant prays that this Hon'ble Court may be pleased to:
(a) Dismiss the Plaint with exemplary costs under Section 35A CPC;
(b) Grant such other reliefs as deemed fit in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR DEFENDANT

VERIFICATION
I, [DEFENDANT NAME], do hereby verify that the contents of Paragraphs [ ] to [ ] are true to my personal knowledge, and Paragraphs [ ] are based on legal advice.
Verified at [CITY] on this [DAY] day of [MONTH], 202[ ]
                                                        DEFENDANT
"""
    ),

    # -------------------------------------------------------------------------
    # 9. AMENDMENT OF PLEADINGS (ORDER VI RULE 17)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="amendment_o6_r17",
        title="Application for Amendment of Pleadings & Supporting Affidavit",
        provision="Order VI Rule 17 CPC",
        category="Interlocutory Applications",
        summary="Application to amend plaint or written statement to introduce newly discovered facts, correct typographical/schedule errors, or mould relief.",
        practice_notes="Proviso to Rule 17: No application for amendment shall be allowed after the trial has commenced, unless the court concludes that in spite of 'due diligence', the party could not have raised the matter before the commencement of trial (Vidyabai v. Padmalatha). Amendments must not alter the fundamental character of the suit.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VI Rule 17", "title": "Amendment of pleadings"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

IN THE MATTER OF:
[PLAINTIFF / DEFENDANT NAME]                                       ... APPLICANT
VERSUS
[OPPOSITE PARTY NAME]                                              ... RESPONDENT

APPLICATION UNDER ORDER VI RULE 17 READ WITH SECTION 151 CPC FOR AMENDMENT OF [PLAINT / WRITTEN STATEMENT]

The Applicant respectfully submits as under:

1. That the Applicant has instituted / is contesting the above Suit for [RELIEF SOUGHT].

2. STAGE OF SUIT & DUE DILIGENCE:
[CHOOSE (A) BEFORE TRIAL OR (B) AFTER COMMENCEMENT OF TRIAL]
(A) BEFORE COMMENCEMENT OF TRIAL: The issues have not yet been framed / Plaintiff's evidence has not commenced.
OR
(B) AFTER COMMENCEMENT OF TRIAL (DUE DILIGENCE PROVISO):
That although trial has commenced, the Applicant in spite of due diligence could not have raised the proposed amendments earlier because [STATE PRECISE FACTUAL GROUND: e.g. certified copy of document was obtained only on DATE / subsequent event occurred on DATE / revenue mutation was passed pending suit].

3. NATURE OF AMENDMENT:
The proposed amendment is necessary for the purpose of determining the real questions in controversy between the parties. It does not alter the fundamental nature or character of the suit, nor does it cause any prejudice to the opposite party that cannot be compensated by costs.

4. DETAILS OF PROPOSED AMENDMENTS:
(a) In Paragraph [ ], line [ ], after the word '[ ]', insert the following:
    "[INSERT NEW SENTENCE/PARAGRAPH]"
(b) In the Schedule of Property, substitute the boundary on the East as '[NEW BOUNDARY]'.
(c) In the Prayer Column, insert additional prayer (a-1):
    "[INSERT ADDITIONAL RELIEF]"

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Permit the Applicant to amend the [Plaint / Written Statement] as detailed in Paragraph 4 above;
(b) Grant leave to file the Amended [Plaint / Written Statement]; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT

VERIFICATION AFFIDAVIT
I, [APPLICANT NAME], aged [ ] years, residing at [ADDRESS], do hereby solemnly affirm that the contents of Paragraphs 1 to 4 are true to my knowledge and information.
Solemnly affirmed at [CITY] on this [DAY] day of [MONTH], 202[ ]
                                                        DEPONENT
"""
    ),

    # -------------------------------------------------------------------------
    # 10. APPOINTMENT OF COURT COMMISSIONER (ORDER XXVI RULE 9)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="commissioner_o26_r9",
        title="Application for Appointment of Court Commissioner & Affidavit",
        provision="Order XXVI Rule 9 CPC",
        category="Interlocutory Applications",
        summary="Application for local investigation by an Advocate Commissioner / Taluk Surveyor to inspect the suit property, report physical status, boundaries, or encroachment.",
        practice_notes="Order XXVI Rule 9 is designed for elucidating any matter in dispute, or ascertaining market value/mesne profits. Crucial rule: Commissioner cannot be appointed to collect evidence or determine possession (possession must be proved by parties through oral/documentary evidence).",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXVI Rule 9", "title": "Commissions to make local investigations"},
            {"kind": "rule", "ref": "Order XXVI Rule 10", "title": "Procedure of Commissioner"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF / DEFENDANT NAME]                                       ... APPLICANT
VERSUS
[OPPOSITE PARTY NAME]                                              ... RESPONDENT

APPLICATION UNDER ORDER XXVI RULE 9 READ WITH SECTION 151 CPC FOR APPOINTMENT OF COURT COMMISSIONER

The Applicant respectfully submits as under:

1. That the Applicant has filed the accompanying Suit for [DECLARATION, POSSESSION, AND REMOVAL OF ENCROACHMENT].

2. That the core dispute between the parties pertains to the exact identity, physical boundaries, and alleged encroachment on the [EASTERN / WESTERN] side of the Suit Schedule Property.

3. That the Respondent has falsely disputed the measurement and location of the boundary wall / fence, asserting that the disputed portion falls within his property Survey No. [ ].

4. That in order to elucidate the matter in dispute and bring the true physical features on record, it is just, necessary, and imperative that a practicing Advocate of this Court be appointed as Court Commissioner, with assistance of a Government / Taluk Surveyor, to:
   (a) Conduct local inspection of the Suit Schedule Property and adjoining land;
   (b) Measure both properties with reference to survey records and village maps;
   (c) Report whether any encroachment exists, and if so, demarcate the exact extent;
   (d) Note the existing physical features (structures, trees, pathway, boundary marks).

5. That the appointment of a Commissioner will prevent multiplicity of proceedings and assist this Hon'ble Court in arriving at a just decision. No prejudice will be caused to the Respondent as the inspection will be conducted after prior notice to both parties.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Appoint an Advocate Commissioner with direction to visit the Suit Property with a qualified Government Surveyor;
(b) Direct the Commissioner to inspect, measure, draw a sketch, and submit a detailed report on the memo of instructions;
(c) Fix the Commissioner's fee payable by the Applicant; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 11. REJECTION OF PLAINT (ORDER VII RULE 11)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="rejection_plaint_o7_r11",
        title="Application for Rejection of Plaint & Supporting Affidavit",
        provision="Order VII Rule 11 CPC",
        category="Defense & Summary Proceedings",
        summary="Defendant's formal application to reject the plaint under clauses (a) to (f) of Order VII Rule 11 based strictly on plaint averments.",
        practice_notes="Settled Supreme Court law (Dahiben v. Arvindbhai; Saleem Bhai v. State of Maharashtra): Court must look ONLY at the averments in the Plaint and documents annexed thereto. Defense in Written Statement or defendant's documents CANNOT be looked into. Plaint cannot be rejected in part (Madhav Prasad Aggarwal).",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VII Rule 11", "title": "Rejection of plaint"},
            {"kind": "section", "ref": "Section 3", "title": "Bar of limitation (Limitation Act)"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[DEFENDANT FULL NAME]                                              ... APPLICANT / DEFENDANT
VERSUS
[PLAINTIFF FULL NAME]                                              ... RESPONDENT / PLAINTIFF

APPLICATION UNDER ORDER VII RULE 11 READ WITH SECTION 151 CPC FOR REJECTION OF PLAINT

The Applicant / Defendant respectfully submits as under:

1. That the Respondent has instituted the above Suit for [RELIEF SOUGHT IN PLAINT].

2. That on a meaningful reading of the Plaint averments alone, the Plaint is liable to be rejected at the threshold under Order VII Rule 11 clauses [(a) / (b) / (c) / (d)] on the following grounds:

   (A) CLAUSE (a) — NO CAUSE OF ACTION:
   The Plaint does not disclose any clear, subsisting right to sue or cause of action against this Applicant. The alleged cause of action is purely illusory and created by clever drafting.

   (B) CLAUSE (d) — EXPRESSLY BARRED BY LAW (LIMITATION):
   As per the Plaintiff's own averments in Paragraph [ ] of the Plaint, the alleged agreement / cause of action occurred on [DATE], whereas the Suit was instituted on [DATE], which is well beyond the prescribed limitation period of 3 years under Article [ ] of the Limitation Act, 1963. The suit is hopelessly barred by limitation on the face of the plaint.

   (C) BARRED BY RES JUDICATA / SPECIFIC STATUTORY BAR:
   The suit is expressly barred by the provisions of [Section 11 CPC / Section 34 Specific Relief Act / Order II Rule 2 CPC].

3. That it is well-settled law by the Hon'ble Supreme Court in Dahiben v. Arvindbhai Kalyanji Bhanusali (2020) 7 SCC 366 that where a suit is manifestly vexatious and meritless in the sense of not disclosing a clear right to sue, the Court must exercise its power under Order VII Rule 11 CPC to nip the litigation in the bud.

PRAYER:
Wherefore, the Applicant / Defendant prays that this Hon'ble Court may be pleased to:
(a) Reject the Plaint in O.S. No. [ ] of 202[ ] under Order VII Rule 11 CPC;
(b) Award costs of these proceedings to the Applicant; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 12. ATTACHMENT BEFORE JUDGMENT (ORDER XXXVIII RULE 5)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="attachment_before_judgment_o38_r5",
        title="Application for Attachment Before Judgment (ABJ) & Affidavit",
        provision="Order XXXVIII Rule 5 CPC",
        category="Interlocutory Applications",
        summary="Urgent application directing defendant to furnish security, and on failure, attaching defendant's immovable/movable property before decree.",
        practice_notes="Drastic remedy: Court must be satisfied that defendant is about to dispose of the whole or any part of his property with intent to obstruct or delay execution. Vague allegations are insufficient; specific details of attempted sale must be pleaded (Raman Tech v. Bharat Perfumes). Under Rule 5(4), attachment without complying with Rule 5(1) is void.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXXVIII Rule 5", "title": "Where defendant may be called upon to furnish security for production of property"},
            {"kind": "rule", "ref": "Order XXXVIII Rule 6", "title": "Attachment where cause not shown or security not furnished"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF NAME]                                                   ... APPLICANT / PLAINTIFF
VERSUS
[DEFENDANT NAME]                                                   ... RESPONDENT / DEFENDANT

APPLICATION UNDER ORDER XXXVIII RULE 5 READ WITH SECTION 151 CPC

The Applicant / Plaintiff respectfully submits as under:

1. That the Plaintiff has instituted the above Suit for recovery of a sum of Rs. [AMOUNT] along with interest against the Defendant.

2. That the Plaintiff has an unassailable and iron-clad case on merits supported by [CHEQUES / PROMISSORY NOTE / ACKNOWLEDGEMENT OF DEBT].

3. INTENT TO DEFRAUD & OBSTRUCT EXECUTION:
That on [RECENT DATE], the Plaintiff reliably learnt that the Defendant is actively negotiating to sell, transfer, and alienate his only unencumbered immovable property described in the Schedule hereunder to third parties, with the deliberate and dishonest intention of defeating and delaying the execution of the decree that may be passed against him.

4. That the Defendant has engaged property brokers [NAME/DETAILS] and entered into an oral agreement to dispose of the property at a distress price, and is preparing to leave the jurisdiction of this Hon'ble Court.

5. That if the Schedule Property is alienated before passing of the decree, the Plaintiff will be left with a paper decree and no means of realization.

PRAYER:
Wherefore, the Applicant / Plaintiff prays that this Hon'ble Court may be pleased to:
(a) Direct the Respondent / Defendant to furnish security in the sum of Rs. [AMOUNT] within a time to be fixed by this Hon'ble Court;
(b) Conditionally attach the immovable property described in the Schedule hereunder pending furnishing of security or disposal of this application;
(c) On failure of Defendant to furnish security, make the order of attachment absolute under Order XXXVIII Rule 6 CPC; in the interest of justice.

SCHEDULE OF PROPERTY SOUGHT TO BE ATTACHED
[Insert full property particulars, survey no., boundaries, estimated market value]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 13. RECALL OF WITNESS & RE-OPENING (ORDER XVIII RULE 17)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="recall_witness_o18_r17",
        title="Application to Recall Witness & Re-Open Evidence",
        provision="Order XVIII Rule 17 & Order XVI Rule 1(3) CPC",
        category="Interlocutory Applications",
        summary="Application to re-open evidence and recall plaintiff's or defendant's witness for further examination-in-chief, cross-examination, or confronting newly obtained records.",
        practice_notes="Supreme Court in Vadiraj Naggappa Vernekar v. Sharadchandra: Rule 17 is discretionary and primarily for court's convenience, but parties may invoke it in exceptional cases where crucial evidence was inadvertently omitted or subsequent documents surfaced. Cannot be used to fill up lacunae.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XVIII Rule 17", "title": "Court may recall and examine witness"},
            {"kind": "rule", "ref": "Order XVI Rule 1", "title": "List of witnesses and summons to witnesses"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF / DEFENDANT NAME]                                       ... APPLICANT
VERSUS
[OPPOSITE PARTY NAME]                                              ... RESPONDENT

APPLICATION UNDER ORDER XVIII RULE 17 READ WITH SECTION 151 CPC

The Applicant respectfully submits as under:

1. That the above Suit is posted for [FINAL ARGUMENTS / DEFENDANT EVIDENCE].

2. That earlier, [PW-1 / DW-1] was examined and discharged on [DATE].

3. REASON FOR RECALL:
That on [DATE], the Applicant obtained certified copies of [DESCRIBE NEW VITAL DOCUMENT: e.g. Registered Partition Deed / Bank Statement / Encumbrance Certificate] from [AUTHORITY], which was not in the possession or knowledge of the Applicant despite diligent search at the time when the witness was in the witness box.

4. That it is indispensable and vital in the interest of justice to confront the witness [NAME] with the said document, and to elicit answers on Paragraph [ ] of the pleadings.

5. That the Applicant is not seeking to fill up any lacunae, but to place true facts on record to assist this Hon'ble Court in arriving at a truthful and just adjudication. The Applicant undertakes to conclude the further examination in a single sitting without seeking any adjournment.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Re-open the stage of evidence in O.S. No. [ ] of 202[ ];
(b) Recall witness [PW-1 / DW-1, FULL NAME] for the limited purpose of further cross-examination / tender of documents; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 14. STANDALONE CONDONATION OF DELAY (SECTION 5 LIMITATION ACT)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="condonation_delay_sec5",
        title="Application for Condonation of Delay (Section 5 Limitation Act)",
        provision="Section 5 of The Limitation Act, 1963",
        category="Interlocutory Applications",
        summary="Exhaustive standalone application and supporting affidavit praying for condonation of delay in filing appeal, review, or interlocutory applications, establishing 'sufficient cause'.",
        practice_notes="Section 5 applies to appeals and applications, but EXPRESSLY DOES NOT APPLY to execution petitions under Order XXI. Delay must be explained with plausible, genuine reasons. Supreme Court in Collector Land Acquisition v. Katiji: 'Every day's delay must be explained does not mean a pedantic approach; justice on merits must prevail over technicalities.'",
        connected_provisions=[
            {"kind": "section", "ref": "Section 5", "title": "Extension of prescribed period in certain cases"},
            {"kind": "section", "ref": "Section 12", "title": "Exclusion of time in legal proceedings"}
        ],
        template_text="""IN THE COURT OF THE [DISTRICT JUDGE / HIGH COURT] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
REGULAR FIRST APPEAL / MISC. APPEAL NO. _______ OF 202[ ]

[APPELLANT / APPLICANT FULL NAME]                                  ... APPLICANT
VERSUS
[RESPONDENT FULL NAME]                                             ... RESPONDENT

APPLICATION UNDER SECTION 5 OF THE LIMITATION ACT, 1963 READ WITH SECTION 151 CPC FOR CONDONATION OF DELAY

The Applicant above named respectfully submits as under:

1. That the Applicant has preferred the accompanying [Regular First Appeal / Application] challenging the judgment and decree dated [DATE] passed by the Court of [TRIAL COURT] in O.S. No. [ ].

2. That the statutory period of limitation for filing the appeal expired on [EXPIRY DATE]. The appeal is presented on [FILING DATE], resulting in a delay of [NUMBER OF DAYS] days.

3. SUFFICIENT CAUSE EXPLAINING DELAY:
The delay of [ ] days was occasioned due to bona fide, unavoidable, and genuine circumstances beyond the Applicant's control, and not due to any deliberate negligence:
(a) The certified copy of the judgment was applied for on [DATE] and was delivered on [DATE] (Annexure A).
(b) That immediately thereafter, on [DATE], the Applicant suffered from [GRAVE MEDICAL CONDITION: e.g. severe cardiac ailment / viral encephalitis / fracture] and was strictly advised complete bed rest and hospitalization from [DATE] to [DATE], as evidenced by the medical certificate issued by [HOSPITAL/DOCTOR] annexed herewith as Annexure B.
(c) That the Applicant's counsel's office was relocated / counsel was indisposed from [DATE] to [DATE]...
(d) That as soon as the Applicant regained physical fitness on [DATE], immediate instructions were given to counsel to prepare and file the appeal.

4. That the Applicant has a prima facie winning case on merits, and if the delay is not condoned, the Applicant will suffer grave and irreparable injustice without adjudication on merits.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Condone the delay of [NUMBER OF DAYS] days in preferring the accompanying Appeal;
(b) Admit the Appeal for hearing on merits; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 15. JUDGMENT ON ADMISSIONS (ORDER XII RULE 6)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="judgment_admissions_o12_r6",
        title="Application for Judgment on Admissions (Order XII Rule 6 CPC)",
        provision="Order XII Rule 6 CPC",
        category="Interlocutory Applications",
        summary="Plaintiff's application praying for immediate summary judgment and decree based on clear, unambiguous admissions made by the defendant in pleadings or documents.",
        practice_notes="Order XII Rule 6 enables the court to pass judgment at any stage, either on application or suo motu, upon admissions of fact made either in pleadings or otherwise, without waiting for the determination of other questions between parties. Admission must be clear, unequivocal, and unconditional (Uttam Singh Dugal v. UBI).",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XII Rule 6", "title": "Judgment on admissions"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF NAME]                                                   ... APPLICANT / PLAINTIFF
VERSUS
[DEFENDANT NAME]                                                   ... RESPONDENT / DEFENDANT

APPLICATION UNDER ORDER XII RULE 6 READ WITH SECTION 151 CPC FOR JUDGMENT ON ADMISSIONS

The Applicant / Plaintiff respectfully submits as under:

1. That the Plaintiff has instituted the above Suit for [RECOVERY OF MONEY / POSSESSION / PARTITION].

2. That the Defendant has entered appearance and filed his Written Statement on [DATE].

3. UNEQUIVOCAL ADMISSION BY DEFENDANT:
That in Paragraph [ ] of the Written Statement, the Defendant has unequivocally and categorically admitted as under:
   "[QUOTE EXACT SENTENCE OF ADMISSION FROM WS: e.g. 'It is true that the Defendant borrowed Rs. 10,00,000/- from the Plaintiff on DATE and agreed to repay with interest...']"

4. That the said admission is clear, unambiguous, unconditional, and deliberate. There is no triable issue left regarding the admitted liability / title.

5. That under Order XII Rule 6 CPC, this Hon'ble Court is empowered to pronounce judgment and pass a decree in respect of the admitted claim without subjecting the Plaintiff to the protracted ordeal of a full trial.

PRAYER:
Wherefore, the Applicant / Plaintiff prays that this Hon'ble Court may be pleased to:
(a) Pass a judgment and decree under Order XII Rule 6 CPC against the Defendant in terms of the clear admissions made in Paragraph [ ] of the Written Statement;
(b) Award costs of the Suit to the Plaintiff; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 16. FORMAL ADJOURNMENT APPLICATION (ORDER XVII RULE 1)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="adjournment_memo_o17_r1",
        title="Formal Application for Adjournment (Order XVII Rule 1 CPC)",
        provision="Order XVII Rule 1 CPC",
        category="Interlocutory Applications",
        summary="Chamber application / memo praying for an adjournment of hearing date showing unavoidable sufficient cause, compliant with the statutory 3-adjournment rule.",
        practice_notes="Order XVII Rule 1 Proviso (b): No adjournment shall be granted more than three times to a party during the hearing of the suit. Proviso (c): Fact that pleader is engaged in another court is NOT a valid ground for adjournment. Must plead genuine personal illness, sudden bereavement, or non-availability of witness due to reasons beyond control.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XVII Rule 1", "title": "Court may grant time and adjourn hearing"},
            {"kind": "rule", "ref": "Order XVII Rule 2", "title": "Procedure if parties fail to appear on day fixed"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. / MEMO NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF / DEFENDANT NAME]                                       ... APPLICANT
VERSUS
[OPPOSITE PARTY NAME]                                              ... RESPONDENT

APPLICATION FOR ADJOURNMENT UNDER ORDER XVII RULE 1 READ WITH SECTION 151 CPC

The Applicant respectfully submits as under:

1. That the above Suit is posted today for [CROSS-EXAMINATION OF PW-1 / ARGUMENTS / ISSUES].

2. That the Applicant / counsel for the Applicant is unable to proceed with the matter today on account of the following unavoidable and genuine circumstances:
   [STATE GENUINE CAUSE: e.g.
   (a) The witness was taken suddenly ill with acute food poisoning / viral fever last evening and has been advised complete rest (Medical memo annexed); OR
   (b) The counsel conducting the trial has suffered sudden bereavement in his immediate family and had to travel out of station.]

3. That the non-appearance / inability to proceed today is completely unintentional and due to reasons beyond human control.

4. That the Applicant has not availed the 3 adjournments contemplated under Order XVII Rule 1 CPC and undertakes to proceed without fail on the next date of hearing.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
Adjourn the hearing of the Suit to any convenient short date; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 17. LEAVE TO DEFEND IN SUMMARY SUIT (ORDER XXXVII RULE 3(5))
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="leave_to_defend_o37_r3",
        title="Application for Leave to Defend in Summary Suit & Affidavit",
        provision="Order XXXVII Rule 3(5) CPC",
        category="Defense & Summary Proceedings",
        summary="Defendant's application and supporting affidavit in a summary suit under Order XXXVII disclosing triable issues and substantial defense to obtain unconditional leave to defend.",
        practice_notes="Must be filed within STRICT 10 DAYS from the date of service of summons for judgment (Article 118: 10 days). Supreme Court principles in IDBI Trusteeship Services v. Hubtown Ltd (2017): If defendant discloses substantial defense, unconditional leave is granted. If defense is shadowy or dubious, conditional leave on deposit is granted.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXXVII Rule 3", "title": "Procedure for the appearance of defendant"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
SUMMARY SUIT NO. _______ OF 202[ ]

[DEFENDANT FULL NAME]                                              ... APPLICANT / DEFENDANT
VERSUS
[PLAINTIFF FULL NAME]                                              ... RESPONDENT / PLAINTIFF

APPLICATION UNDER ORDER XXXVII RULE 3(5) READ WITH SECTION 151 CPC FOR LEAVE TO DEFEND

The Applicant / Defendant respectfully submits as under:

1. That the Plaintiff has instituted the above Summary Suit under Order XXXVII CPC for recovery of Rs. [AMOUNT] based on an alleged [PROMISSORY NOTE / BILL OF EXCHANGE / CHEQUE].

2. That the summons for judgment was served on the Defendant on [DATE]. The present application is filed on [DATE], which is strictly within the statutory period of 10 days as prescribed by law.

3. SUBSTANTIAL DEFENSE & TRIABLE ISSUES:
That the Defendant has a bona fide, plausible, and substantial defense to the Plaintiff's claim, raising serious triable issues:
(a) FAILURE OF CONSIDERATION: The alleged promissory note was issued as an advance for supply of goods which were never delivered by the Plaintiff...
(b) MATERIAL ALTERATION: The cheque / bill of exchange has been materially altered without consent, voiding the instrument under Section 87 Negotiable Instruments Act...
(c) DISCHARGE / SATISFACTION: The Defendant has already remitted Rs. [AMOUNT] vide bank transfer dated [DATE], which has been deliberately suppressed...

4. That in terms of the landmark ruling of the Hon'ble Supreme Court in IDBI Trusteeship Services Ltd v. Hubtown Ltd (2017) 1 SCC 568, where the defendant raises substantial triable issues, he is entitled to UNCONDITIONAL leave to defend.

PRAYER:
Wherefore, the Applicant / Defendant prays that this Hon'ble Court may be pleased to:
(a) Grant unconditional leave to the Applicant / Defendant to defend Summary Suit No. [ ] of 202[ ];
(b) Permit the Defendant to file Written Statement within the statutory time; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 18. POLICE AID APPLICATION IN EXECUTION (SECTION 151)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="police_aid_execution_sec151",
        title="Application for Police Aid in Execution & Supporting Affidavit",
        provision="Section 151 CPC r/w High Court Civil Rules of Practice",
        category="Execution Proceedings",
        summary="Application by decree holder praying for directions to the jurisdictional Station House Officer (SHO) to provide armed police protection to the court bailiff to execute a delivery warrant.",
        practice_notes="Court will not grant police protection as a routine measure. The decree holder must produce bailiff endorsement or cogent evidence showing apprehension of violent resistance, breach of peace, or criminal intimidation by the judgment debtor or his associates.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 151", "title": "Saving of inherent powers of Court"},
            {"kind": "rule", "ref": "Order XXI Rule 35", "title": "Decree for immovable property"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
E.A. NO. _______ OF 202[ ]
IN
EXECUTION PETITION NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[DECREE HOLDER NAME]                                               ... DECREE HOLDER / APPLICANT
VERSUS
[JUDGMENT DEBTOR NAME]                                             ... JUDGMENT DEBTOR / RESPONDENT

APPLICATION UNDER SECTION 151 CPC FOR EXTENSION OF POLICE AID

The Decree Holder respectfully submits as under:

1. That the Decree Holder obtained a lawful decree for delivery of vacant physical possession of the Schedule Property in O.S. No. [ ] on [DATE].

2. That this Hon'ble Court was pleased to issue a Delivery Warrant under Order XXI Rule 35 CPC on [DATE] directing the court bailiff to put the Decree Holder in physical possession.

3. RESISTANCE & BREACH OF PEACE:
That when the court bailiff visited the spot on [DATE] to execute the warrant, the Judgment Debtor along with 10 to 15 anti-social elements gathered at the premises, held out lethal threats, and physically obstructed the bailiff from discharging his official duties. The Bailiff returned the warrant unexecuted with a specific endorsement of resistance and apprehension of blood-shed (Bailiff Report annexed).

4. That the Judgment Debtor is openly proclaiming that he will violently resist any attempt by court staff to execute the decree.

5. That unless armed police protection is provided to the court bailiff, the solemn decree of this Court cannot be executed and the majesty of law will be defeated.

PRAYER:
Wherefore, the Decree Holder prays that this Hon'ble Court may be pleased to:
(a) Direct the Station House Officer (SHO), [POLICE STATION NAME] to provide adequate armed police protection and assistance to the Court Bailiff / Nazir on the date of execution;
(b) Authorize the Bailiff to execute the Delivery Warrant with police aid and put the Decree Holder in vacant physical possession of the Schedule Property; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR DECREE HOLDER
"""
    ),

    # -------------------------------------------------------------------------
    # 19. BREAK OPEN LOCKS APPLICATION (ORDER XXI RULE 35(3))
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="break_open_locks_o21_r35",
        title="Application to Break Open Locks for Delivery of Possession",
        provision="Order XXI Rule 35(3) CPC",
        category="Execution Proceedings",
        summary="Application by decree holder authorizing the bailiff to break open locks, doors, and gates of the suit premises to effect physical delivery of possession.",
        practice_notes="Order XXI Rule 35(3) gives statutory authority to break open any lock, bolt, or door if the person in possession refuses to open it. If women in purdah occupy the premises, bailiff must give notice to withdraw under Rule 35(3) proviso before breaking in.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXI Rule 35", "title": "Decree for immovable property"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
E.A. NO. _______ OF 202[ ]
IN
EXECUTION PETITION NO. _______ OF 202[ ]

[DECREE HOLDER NAME]                                               ... DECREE HOLDER / APPLICANT
VERSUS
[JUDGMENT DEBTOR NAME]                                             ... JUDGMENT DEBTOR / RESPONDENT

APPLICATION UNDER ORDER XXI RULE 35(3) READ WITH SECTION 151 CPC

The Decree Holder respectfully submits as under:

1. That this Hon'ble Court was pleased to issue a Warrant of Delivery of Possession against the Judgment Debtor in respect of the Schedule Property.

2. That the Judgment Debtor has deliberately locked the outer main gate and entrance doors of the suit premises and absconded / remains inside, refusing to open the locks to deliberately frustrate the execution process.

3. That the Court Bailiff visited the spot and returned the warrant reporting that the premises were found locked.

4. That unless specific permission is granted to break open the locks, remove fasteners, and prepare an inventory of any articles found inside, the decree cannot be executed.

PRAYER:
Wherefore, the Decree Holder prays that this Hon'ble Court may be pleased to:
(a) Authorize and empower the Court Bailiff / Nazir to break open the outer locks, doors, and gates of the Schedule Property with the help of a locksmith;
(b) Direct the Bailiff to prepare an inventory of articles found inside, remove the same, and deliver vacant physical possession to the Decree Holder; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR DECREE HOLDER
"""
    ),

    # -------------------------------------------------------------------------
    # 20. THIRD-PARTY CLAIM PETITION (ORDER XXI RULE 58)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="claim_petition_o21_r58",
        title="Third-Party Claim / Objection Petition Against Attachment",
        provision="Order XXI Rule 58 CPC",
        category="Execution Proceedings",
        summary="Claim petition filed by a third party asserting independent title, ownership, or possessory lien over property wrongfully attached in execution of a decree.",
        practice_notes="Order XXI Rule 58(2): All questions including title, right, or interest arising between the parties MUST be determined by the executing court; no separate suit lies. Order XXI Rule 58(4): The order made has the force of a DECREE and is appealable under Section 96 CPC.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXI Rule 58", "title": "Adjudication of claims to, or objections to attachment of, property"},
            {"kind": "rule", "ref": "Order XXI Rule 59", "title": "Stay of sale"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
E.A. NO. _______ OF 202[ ]
IN
EXECUTION PETITION NO. _______ OF 202[ ]

IN THE MATTER OF:
[THIRD PARTY CLAIMANT FULL NAME],
Aged about [ ] years, Residing at [ADDRESS]                        ... CLAIMANT / OBJECTOR
VERSUS
1. [DECREE HOLDER NAME]                                            ... DECREE HOLDER / RESPONDENT 1
2. [JUDGMENT DEBTOR NAME]                                          ... JUDGMENT DEBTOR / RESPONDENT 2

CLAIM PETITION UNDER ORDER XXI RULE 58 READ WITH SECTION 151 CPC

The Claimant / Objector respectfully submits as under:

1. That the Claimant is a bona fide third party who has no connection whatsoever with the dispute between the Decree Holder and the Judgment Debtor in O.S. No. [ ].

2. That under an order of attachment passed by this Hon'ble Court on [DATE], the property described in the Schedule was attached as if it belonged to the Judgment Debtor.

3. INDEPENDENT TITLE & POSSESSION:
That the Claimant is the absolute owner and in continuous physical possession of the Schedule Property. The Claimant purchased the property for valuable consideration vide Registered Sale Deed dated [DATE] (registered as Doc No. [ ] at SRO [ ]) LONG PRIOR to the institution of the suit / attachment.

4. That the Judgment Debtor has NO manner of right, title, equity, or interest in the attached property.

5. That the attachment of the Claimant's property is illegal, ultra vires, and void ab initio.

PRAYER:
Wherefore, the Claimant prays that this Hon'ble Court may be pleased to:
(a) Adjudicate the claim of the Claimant under Order XXI Rule 58(2) CPC;
(b) Release the Schedule Property from the order of attachment dated [DATE];
(c) Stay the proclamation and sale of the Schedule Property pending disposal of this claim petition; in the interest of justice.

SCHEDULE OF PROPERTY
[Insert detailed description of attached property]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR CLAIMANT
"""
    ),

    # -------------------------------------------------------------------------
    # 21. REMOVAL OF RESISTANCE (ORDER XXI RULE 97)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="removal_resistance_o21_r97",
        title="Application for Removal of Resistance / Obstruction to Possession",
        provision="Order XXI Rule 97 CPC",
        category="Execution Proceedings",
        summary="Application by decree holder or auction purchaser complaining of resistance or obstruction offered by judgment debtor or third parties in obtaining physical possession.",
        practice_notes="Limitation under Article 129 of Limitation Act is 30 DAYS from the date of resistance or obstruction. Order XXI Rule 101: All questions of right, title, or interest arising between the parties MUST be determined by the executing court; no separate suit lies.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXI Rule 97", "title": "Resistance or obstruction to possession of immovable property"},
            {"kind": "rule", "ref": "Order XXI Rule 98", "title": "Orders after adjudication"},
            {"kind": "rule", "ref": "Order XXI Rule 101", "title": "Question to be determined"},
            {"kind": "limitation_article", "ref": "Article 129", "title": "For possession by DH or purchaser obstructed (30 days)"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
E.A. NO. _______ OF 202[ ]
IN
EXECUTION PETITION NO. _______ OF 202[ ]

[DECREE HOLDER / PURCHASER NAME]                                   ... APPLICANT / DECREE HOLDER
VERSUS
1. [OBSTRUCTOR / RESISTER NAME],
   Residing at [ADDRESS]                                           ... OBSTRUCTOR / RESPONDENT 1
2. [JUDGMENT DEBTOR NAME]                                          ... JUDGMENT DEBTOR / RESPONDENT 2

APPLICATION UNDER ORDER XXI RULE 97 READ WITH SECTION 151 CPC

The Decree Holder respectfully submits as under:

1. That the Applicant obtained a decree for possession of the Schedule Property in O.S. No. [ ] on [DATE].

2. That when the Court Bailiff visited the property on [DATE OF RESISTANCE] along with the Delivery Warrant to put the Applicant in possession, Respondent No. 1 (Obstructor), claiming to be [STATE OBSTRUCTOR'S CLAIM: e.g. tenant / purchaser pendente lite / family member of JD], wrongfully resisted and obstructed the bailiff from executing the warrant.

3. That the resistance was offered on [DATE], and the present application is filed on [DATE], which is strictly within the 30-day limitation period prescribed under Article 129 of the Limitation Act, 1963.

4. That Respondent No. 1 has no independent right or title. He is a setting-up / nominee / transferee pendente lite of the Judgment Debtor bound by the decree under Order XXI Rule 102 CPC.

5. That under Order XXI Rule 101 CPC, all questions of title, right, or possession between the parties must be determined by this Hon'ble Court.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Adjudicate the obstruction offered by Respondent No. 1 under Order XXI Rule 97 & 101 CPC;
(b) Order removal of the obstruction and direct that the Applicant be put in vacant physical possession of the Schedule Property with police aid;
(c) Direct committal of the obstructor to civil prison under Rule 98(2) if resistance is found without just cause; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 22. REGULAR FIRST APPEAL (SECTION 96 & ORDER XLI RULE 1)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="regular_first_appeal_sec96",
        title="Memorandum of Regular First Appeal (RFA) & Stay Petition",
        provision="Section 96 & Order XLI Rule 1 CPC",
        category="Appeals & Revisions",
        summary="Comprehensive Memorandum of Regular First Appeal challenging a trial court civil decree on findings of fact and law, with companion stay application under Order XLI Rule 5.",
        practice_notes="Limitation under Article 116(a): 30 days to District Court; Article 116(b): 90 days to High Court. Time requisite for obtaining certified copy is excluded under Section 12. Certified copy of decree and judgment must accompany memo (Rule 1).",
        connected_provisions=[
            {"kind": "section", "ref": "Section 96", "title": "Appeal from original decree"},
            {"kind": "rule", "ref": "Order XLI Rule 1", "title": "Form of appeal. What to accompany memorandum"},
            {"kind": "rule", "ref": "Order XLI Rule 5", "title": "Stay by Appellate Court"},
            {"kind": "limitation_article", "ref": "Article 116", "title": "Under the Code of Civil Procedure, 1908 to a Court of a District Judge (30 days) / to a High Court (90 days)"}
        ],
        template_text="""IN THE COURT OF THE [PRINCIPAL DISTRICT JUDGE / HIGH COURT] AT [CITY]
REGULAR FIRST APPEAL NO. _______ OF 202[ ]

[APPELLANT FULL NAME],
Aged about [ ] years, S/o [PARENT NAME],
Residing at [ADDRESS]
(Original Defendant in O.S. No. [   ] / 202[ ])                    ... APPELLANT
VERSUS
[RESPONDENT FULL NAME],
Aged about [ ] years, S/o [PARENT NAME],
Residing at [ADDRESS]
(Original Plaintiff in O.S. No. [   ] / 202[ ])                    ... RESPONDENT

MEMORANDUM OF REGULAR FIRST APPEAL UNDER SECTION 96 READ WITH ORDER XLI RULE 1 OF THE CODE OF CIVIL PROCEDURE, 1908

The Appellant above named respectfully submits as under:

1. PARTICULARS OF IMPUGNED DECREE:
This Appeal is directed against the Judgment and Decree dated [DATE] passed by the learned [TRIAL COURT NAME] in Original Suit No. [ ] of 202[ ], decreeing the plaintiff's suit for [SPECIFIC PERFORMANCE / INJUNCTION / RECOVERY].

2. VALUATION & COURT FEES:
The value of the appeal is Rs. [AMOUNT], and court fee of Rs. [AMOUNT] is paid as per the Court Fees Act.

3. GROUNDS OF APPEAL:
(a) The impugned judgment is contrary to law, facts, and settled legal principles.
(b) The Trial Court grossly erred in holding that the Plaintiff proved his readiness and willingness under Section 16(c) of the Specific Relief Act, completely overlooking the bank records showing total lack of funds.
(c) The Trial Court failed to appreciate the material contradictions in the testimony of PW-1 and PW-2.
(d) The Trial Court misconstrued the documentary evidence Exhibits P-1 to P-5, which were unregistered and inadmissible in law.
(e) The Trial Court erroneously rejected the Defendant's plea of limitation, as the suit was instituted beyond 3 years from the date of breach.
(f) The findings recorded on Issue Nos. 1, 2, and 4 are perverse and based on conjectures and surmises.

PRAYER:
Wherefore, the Appellant prays that this Hon'ble Court may be pleased to:
(a) Call for the lower court records in O.S. No. [ ] of 202[ ];
(b) Allow the Appeal and set aside the impugned Judgment and Decree dated [DATE] passed by [TRIAL COURT];
(c) Dismiss the Suit O.S. No. [ ] of 202[ ] with costs throughout;
(d) Grant such other reliefs as deemed fit in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPELLANT

INTERIM STAY APPLICATION UNDER ORDER XLI RULE 5 CPC
[Insert prayer for ad-interim stay of execution and operation of the impugned decree pending appeal]
"""
    ),

    # -------------------------------------------------------------------------
    # 23. CIVIL MISCELLANEOUS APPEAL (ORDER XLIII RULE 1)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="cma_o43_r1",
        title="Civil Miscellaneous Appeal (CMA) Against Injunction Order",
        provision="Order XLIII Rule 1(r) CPC",
        category="Appeals & Revisions",
        summary="Appeal against an interlocutory order granting or refusing temporary injunction under Order XXXIX Rules 1 & 2.",
        practice_notes="An order granting or refusing temporary injunction is an appealable order under Order XLIII Rule 1(r). Appellate court will not interfere with discretionary order of trial court unless the exercise of discretion was arbitrary, capricious, or perverse (Wander Ltd v. Antox India).",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XLIII Rule 1", "title": "Appeal from orders"},
            {"kind": "rule", "ref": "Order XXXIX Rule 1", "title": "Cases in which temporary injunction may be granted"}
        ],
        template_text="""IN THE COURT OF THE [PRINCIPAL DISTRICT JUDGE] AT [CITY]
CIVIL MISCELLANEOUS APPEAL NO. _______ OF 202[ ]

[APPELLANT FULL NAME],
Aged about [ ] years, Residing at [ADDRESS]
(Original Defendant in O.S. No. [   ] / 202[ ])                    ... APPELLANT
VERSUS
[RESPONDENT FULL NAME],
Aged about [ ] years, Residing at [ADDRESS]
(Original Plaintiff in O.S. No. [   ] / 202[ ])                    ... RESPONDENT

MEMORANDUM OF MISCELLANEOUS APPEAL UNDER ORDER XLIII RULE 1(r) READ WITH SECTION 104 CPC

The Appellant above named respectfully submits as under:

1. PARTICULARS OF IMPUGNED ORDER:
This Appeal is directed against the Interlocutory Order dated [DATE] passed by the learned [COURT NAME] on I.A. No. [ ] in O.S. No. [ ], [GRANTING / REJECTING] an ad-interim temporary injunction under Order XXXIX Rules 1 & 2 CPC.

2. GROUNDS OF APPEAL:
(a) The Trial Court exercised its judicial discretion arbitrarily, capriciously, and in total disregard of the three cardinal tests governing injunctions.
(b) The Trial Court recorded a perverse finding of prima facie case in favour of the Respondent without considering the registered title documents of the Appellant.
(c) The Trial Court failed to appreciate that the Respondent was never in physical possession of the suit property on the date of suit.
(d) The Trial Court ignored the mandatory requirements of the Proviso to Order XXXIX Rule 3 CPC.

PRAYER:
Wherefore, the Appellant prays that this Hon'ble Court may be pleased to:
(a) Set aside the impugned order dated [DATE] passed on I.A. No. [ ] in O.S. No. [ ];
(b) Dismiss the injunction application I.A. No. [ ];
(c) Grant ad-interim stay of the operation of the impugned order pending this appeal; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPELLANT
"""
    ),

    # -------------------------------------------------------------------------
    # 24. REVIEW PETITION (SECTION 114 & ORDER XLVII RULE 1)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="review_petition_sec114",
        title="Petition for Review of Judgment / Decree & Affidavit",
        provision="Section 114 & Order XLVII Rule 1 CPC",
        category="Appeals & Revisions",
        summary="Review petition filed before the same court that passed the decree on grounds of discovery of new and important evidence or error apparent on the face of the record.",
        practice_notes="Limitation under Article 124 of Limitation Act is 30 DAYS from the date of decree or order. Review is NOT an appeal in disguise. Grounds are strictly restricted to: (1) discovery of new evidence which could not be produced after due diligence; (2) mistake or error apparent on the face of the record; or (3) any other sufficient reason (Kamlesh Verma v. Mayawati).",
        connected_provisions=[
            {"kind": "section", "ref": "Section 114", "title": "Review"},
            {"kind": "rule", "ref": "Order XLVII Rule 1", "title": "Application for review of judgment"},
            {"kind": "limitation_article", "ref": "Article 124", "title": "For a review of judgment by a court other than the Supreme Court (30 days)"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
CIVIL REVIEW PETITION NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[REVIEW PETITIONER FULL NAME]                                      ... PETITIONER
VERSUS
[RESPONDENT FULL NAME]                                             ... RESPONDENT

PETITION FOR REVIEW UNDER SECTION 114 READ WITH ORDER XLVII RULE 1 CPC

The Review Petitioner respectfully submits as under:

1. That this Hon'ble Court was pleased to pronounce Judgment and Decree in O.S. No. [ ] on [DATE].

2. That no appeal has been preferred against the said Judgment and Decree / no appeal lies from the said order.

3. GROUNDS FOR REVIEW:
[CHOOSE (A) ERROR APPARENT OR (B) DISCOVERY OF NEW EVIDENCE]
(A) ERROR APPARENT ON THE FACE OF THE RECORD:
That there is a manifest and patent error apparent on the face of the judgment, in that this Hon'ble Court has recorded at Paragraph [ ] that [STATE ERROR: e.g. the defendant admitted receipt of notice, whereas on the record Exhibit D-1 clearly proves refusal / court overlooked statutory bar under Section 80 CPC]. The error is self-evident and does not require any long-drawn reasoning to detect.
OR
(B) DISCOVERY OF NEW & IMPORTANT EVIDENCE:
That on [DATE], the Petitioner discovered a crucial public document [DESCRIBE DOCUMENT: e.g. certified village map / registered cancellation deed] which in spite of the exercise of due diligence was not within his knowledge and could not be produced at the trial.

4. That the present Review Petition is filed within 30 days of the decree as required under Article 124 of the Limitation Act, 1963.

PRAYER:
Wherefore, the Petitioner prays that this Hon'ble Court may be pleased to:
(a) Review and recall the Judgment and Decree dated [DATE] passed in O.S. No. [ ];
(b) Re-hear the matter on the specific points raised herein; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PETITIONER
"""
    ),

    # -------------------------------------------------------------------------
    # 25. SUIT FOR SPECIFIC PERFORMANCE (AGREEMENT TO SELL)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="plaint_specific_performance",
        title="Plaint in Suit for Specific Performance of Agreement to Sell",
        provision="Order VII CPC r/w Specific Relief Act, 1963",
        category="Core Pleadings",
        summary="Complete civil plaint for enforcing an Agreement to Sell immovable property, with mandatory Section 16(c) readiness and willingness averments and alternative refund prayer.",
        practice_notes="Section 16(c) of the Specific Relief Act, 1963: Plaintiff must aver and prove continuous readiness and willingness to perform his part of the contract from date of agreement to date of decree. Limitation under Article 54: 3 years from date fixed for performance, or if no date fixed, from date plaintiff has notice of refusal.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"},
            {"kind": "limitation_article", "ref": "Article 54", "title": "For specific performance of a contract (3 years)"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF FULL NAME],
Aged [ ] years, S/o [PARENT NAME], Residing at [ADDRESS]            ... PLAINTIFF
VERSUS
[DEFENDANT FULL NAME],
Aged [ ] years, S/o [PARENT NAME], Residing at [ADDRESS]            ... DEFENDANT

SUIT FOR SPECIFIC PERFORMANCE OF AGREEMENT OF SALE DATED [DATE] AND VACANT POSSESSION

The Plaintiff above named respectfully submits as under:

1. That the Defendant is the absolute owner of the immovable property described in the Schedule hereunder.

2. AGREEMENT OF SALE & ADVANCE CONSIDERATION:
That on [DATE], the Defendant entered into a written and registered / notarized Agreement to Sell with the Plaintiff agreeing to sell the Schedule Property for a total consideration of Rs. [TOTAL SALE PRICE]. On the date of agreement, the Plaintiff paid a sum of Rs. [ADVANCE AMOUNT] as earnest money deposit, the receipt whereof was duly acknowledged by the Defendant.

3. TERMS OF PERFORMANCE:
That the balance sale consideration of Rs. [BALANCE AMOUNT] was agreed to be paid on or before [STIPULATED DATE], upon which the Defendant agreed to execute the registered Sale Deed and hand over vacant physical possession.

4. MANDATORY AVERMENT OF READINESS & WILLINGNESS (SECTION 16(c) SRA):
That the Plaintiff has always been, and continues to be, ready and willing to perform his part of the contract by paying the balance sale consideration of Rs. [BALANCE] and purchasing the requisite stamp papers. The Plaintiff has the necessary liquid funds in his Bank Account No. [ ] at [BANK NAME] to demonstrate financial readiness.

5. DEFENDANT'S BREACH & LEGAL NOTICE:
That despite repeated requests, the Defendant failed to execute the Sale Deed. The Plaintiff caused a Legal Notice dated [DATE] calling upon the Defendant to receive the balance money and execute the deed on [DATE] at the Sub-Registrar's office. The Plaintiff remained present at the Sub-Registrar's office on the appointed date, but the Defendant deliberately failed to turn up.

6. CAUSE OF ACTION & LIMITATION:
The cause of action arose on [DATE FIXED / REFUSAL DATE]. The suit is within the 3-year limitation period prescribed under Article 54 of the Limitation Act, 1963.

PRAYER:
Wherefore, the Plaintiff prays for a judgment and decree:
(a) Directing the Defendant to execute a registered Sale Deed in favour of the Plaintiff in respect of the Schedule Property upon receiving the balance sale consideration, and deliver vacant physical possession;
(b) In default, directing this Hon'ble Court to execute the Sale Deed in favour of the Plaintiff under Order XXI Rule 34 CPC;
(c) IN THE ALTERNATIVE: Directing refund of earnest money of Rs. [ ] with interest at 18% p.a. and damages of Rs. [ ];
(d) Awarding costs of this suit.

SCHEDULE OF PROPERTY
[Insert survey no., measurement, boundaries East, West, North, South]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF
"""
    ),

    # -------------------------------------------------------------------------
    # 26. SUIT FOR PARTITION & SEPARATE POSSESSION
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="plaint_partition",
        title="Plaint in Suit for Partition and Separate Possession",
        provision="Order VII CPC r/w Hindu Succession Act",
        category="Core Pleadings",
        summary="Civil plaint for partition and separate possession of joint family / ancestral coparcenary properties, detailing genealogy, shares, and preliminary decree prayer.",
        practice_notes="Under Order XX Rule 18 CPC, court passes a preliminary decree declaring the rights/shares of parties, followed by a final decree appointing an advocate commissioner for division by metes and bounds. Limitation under Article 110: 12 years from when exclusion from share becomes known.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"},
            {"kind": "rule", "ref": "Order XX Rule 18", "title": "Decree in suit for partition of property or separate possession of a share therein"},
            {"kind": "limitation_article", "ref": "Article 110", "title": "By a person excluded from a joint family property to enforce a right to share therein (12 years)"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF FULL NAME],
Aged [ ] years, Residing at [ADDRESS]                              ... PLAINTIFF
VERSUS
1. [DEFENDANT 1 FULL NAME]                                         ... DEFENDANT 1
2. [DEFENDANT 2 FULL NAME]                                         ... DEFENDANT 2

SUIT FOR PARTITION AND SEPARATE POSSESSION OF PLAINTIFF'S [e.g. 1/3RD] SHARE

The Plaintiff above named respectfully submits as under:

1. GENEALOGY / FAMILY TREE:
That the parties are governed by Hindu Law. The common ancestor [NAME] died on [DATE], leaving behind the following surviving legal heirs:
                     [PROPOSITUS: COMMON ANCESTOR]
                                    |
            +-----------------------+-----------------------+
            |                                               |
      [PLAINTIFF]                                    [DEFENDANT 1]

2. NATURE OF PROPERTIES:
The properties described in the Schedule hereunder are ancestral and joint family coparcenary properties acquired from joint family nucleus. No partition by metes and bounds has ever taken place between the parties.

3. CAUSE FOR PARTITION:
That recently on [DATE], Defendant No. 1 began acting adversely to the Plaintiff's interest, denying his legitimate share and attempting to alienate Item No. [ ] of the Schedule. The Plaintiff demanded partition by metes and bounds, which the Defendants wrongfully refused on [DATE].

4. SHARE ENTITLEMENT:
The Plaintiff is entitled to an undivided [1/3rd] share in all the suit schedule properties.

PRAYER:
Wherefore, the Plaintiff prays for a judgment and decree:
(a) Passing a Preliminary Decree for partition declaring the Plaintiff's [1/3rd] share in all the Suit Schedule Properties;
(b) Appointing a Court Commissioner to divide the Suit Properties by metes and bounds and putting the Plaintiff in separate physical possession;
(c) Permanent Injunction restraining the Defendants from alienating or creating third-party rights in the properties;
(d) Awarding costs of the suit.

SCHEDULE OF SUIT PROPERTIES
Item 1: [Agricultural land, Sy No., Extent, Boundaries]
Item 2: [Residential house, Municipal No., Boundaries]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF
"""
    ),

    # -------------------------------------------------------------------------
    # 27. SUIT FOR DECLARATION, POSSESSION & MESNE PROFITS
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="plaint_declaration_possession",
        title="Plaint for Declaration of Title, Possession & Mesne Profits",
        provision="Order VII CPC r/w Specific Relief Act & Order XX Rule 12",
        category="Core Pleadings",
        summary="Comprehensive plaint for title declaration, recovery of physical possession from an unauthorized occupant/trespasser, and enquiry into past and future mesne profits.",
        practice_notes="Limitation under Article 65: 12 years for possession of immovable property based on title. Order XX Rule 12 enables the court to direct an enquiry into past and future mesne profits up to delivery of possession.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"},
            {"kind": "rule", "ref": "Order XX Rule 12", "title": "Decree for possession and mesne profits"},
            {"kind": "limitation_article", "ref": "Article 65", "title": "For possession of immovable property or any interest therein based on title (12 years)"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF FULL NAME],
Aged [ ] years, Residing at [ADDRESS]                              ... PLAINTIFF
VERSUS
[DEFENDANT FULL NAME],
Aged [ ] years, Residing at [ADDRESS]                              ... DEFENDANT

SUIT FOR DECLARATION OF TITLE, RECOVERY OF VACANT POSSESSION, AND MESNE PROFITS

The Plaintiff above named respectfully submits as under:

1. That the Plaintiff is the absolute title-holder of the Suit Schedule Property, having acquired ownership by virtue of [REGISTERED TITLE DEED / INHERITANCE] dated [DATE].

2. ILLEGAL DISPOSSESSION & TRESPASS:
That the Defendant was initially inducted as a licensee / tenant / had no right, but on [DATE], the Defendant unlawfully trespassed and occupied the property without authority of law. The Plaintiff issued a legal notice dated [DATE] terminating permission and demanding vacant possession, but the Defendant failed to vacate.

3. WRONGFUL POSSESSION & MESNE PROFITS:
The Defendant's possession is wrongful and unauthorized. The Suit Property is capable of fetching a monthly rental income of Rs. [AMOUNT]. The Plaintiff is entitled to past mesne profits of Rs. [ ] and future mesne profits from the date of suit till delivery of vacant possession under Order XX Rule 12 CPC.

PRAYER:
Wherefore, the Plaintiff prays for a judgment and decree:
(a) Declaring that the Plaintiff is the absolute owner of the Suit Schedule Property;
(b) Directing the Defendant to quit, vacate, and deliver vacant physical possession of the Suit Schedule Property to the Plaintiff;
(c) Directing an enquiry into future mesne profits under Order XX Rule 12 CPC until actual delivery of possession;
(d) Awarding costs of this suit.

SCHEDULE OF SUIT PROPERTY
[Insert complete description, survey no., boundaries, measurements]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF
"""
    ),

    # -------------------------------------------------------------------------
    # 28. SECTION 65B ELECTRONIC EVIDENCE CERTIFICATE
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="cert_sec_65b_evidence",
        title="Certificate of Electronic Evidence (Section 65B / BSA Equivalent)",
        provision="Section 65B Indian Evidence Act / Section 63 BSA",
        category="Evidence & Trial Proceedings",
        summary="Mandatory statutory affidavit/certificate certifying electronic records (WhatsApp chats, emails, CCTV footage, call detail records, computer printouts).",
        practice_notes="Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal (2020) 7 SCC 1: Section 65B(4) certificate is MANDATORY as a condition precedent to the admissibility of any electronic record produced as secondary evidence. Must be signed by a person occupying a responsible official position in relation to the device.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 65B", "title": "Admissibility of electronic records (Indian Evidence Act)"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF NAME]                                                   ... PLAINTIFF
VERSUS
[DEFENDANT NAME]                                                   ... DEFENDANT

CERTIFICATE UNDER SECTION 65B OF THE INDIAN EVIDENCE ACT, 1872 (OR SECTION 63 OF BHARATIYA SAKSHYA ADHINIYAM, 2023)

I, [DEPONENT FULL NAME], aged about [ ] years, residing at [ADDRESS], do hereby solemnly affirm and state on oath as follows:

1. That I am the Plaintiff / Author / Custodian of the computer system / mobile phone from which the accompanying electronic records are generated.

2. DETAILS OF COMPUTER DEVICE & OUTPUT:
(a) Device: [e.g. Dell Laptop / iPhone Model / Samsung Mobile Phone, Serial No. ______].
(b) Nature of Output: Printouts of [EMAILS / WHATSAPP CHATS / BANK STATEMENTS / CCTV STILLS] dated [DATE RANGE], marked as Document Nos. [ ] to [ ].

3. MANDATORY SECTION 65B STATUTORY DECLARATION:
(a) The said computer output containing the information was produced by the computer during the period over which the computer was used regularly to store and process information for the purposes of my lawful activities.
(b) Throughout the said period, information of the kind contained in the electronic record was regularly and lawfully fed into the computer in the ordinary course of activities.
(c) Throughout the material part of the said period, the computer was operating properly; or if not, the period of malfunction did not affect the electronic record or the accuracy of its contents.
(d) The electronic record produced herewith is a true and faithful reproduction of the original data stored in the said device.

4. I certify that the printouts produced before this Hon'ble Court are true, complete, and authentic copies of the electronic communications.

Place: [CITY]
Date: [DATE]
                                                        DEPONENT / SIGNATORY
                                                        [NAME, DESIGNATION & CONTACT]
"""
    ),

    # -------------------------------------------------------------------------
    # 29. IMPLEADMENT APPLICATION (ORDER I RULE 10(2))
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="impleadment_o1_r10",
        title="Application for Impleadment of Necessary / Proper Party",
        provision="Order I Rule 10(2) CPC",
        category="Parties & Capacity",
        summary="Application by plaintiff or proposed third-party intervener praying to be added as a party defendant/plaintiff to prevent multiplicity of suits.",
        practice_notes="Kasturi v. Iyyamperumal (2005) 6 SCC 733: A necessary party is one without whom no effective decree can be passed at all; a proper party is one whose presence enables the court to completely, effectively, and adequately adjudicate all matters in dispute.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order I Rule 10", "title": "Suit in name of wrong plaintiff. Court may strike out or add parties"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF / PROPOSED APPLICANT NAME]                              ... APPLICANT
VERSUS
1. [PLAINTIFF NAME]                                                ... RESPONDENT 1
2. [DEFENDANT NAME]                                                ... RESPONDENT 2

APPLICATION UNDER ORDER I RULE 10(2) READ WITH SECTION 151 CPC FOR IMPLEADMENT

The Applicant respectfully submits as under:

1. That the Plaintiff has instituted the above Suit against the Defendant for [PARTITION / INJUNCTION / DECLARATION OF TITLE].

2. INTEREST & NECESSITY OF PROPOSED PARTY:
That the Applicant is a direct title-holder / co-owner / subsequent purchaser pendente lite / mortgagee having substantial and subsisting legal interest in the Suit Schedule Property:
[EXPLAIN SUBSTANTIVE INTEREST: e.g. The Applicant purchased Item No. 2 of the Suit Property vide Registered Sale Deed dated DATE, prior to the filing of the suit, and is in continuous physical possession.]

3. That the Plaintiff has deliberately and mischievously omitted to array the Applicant as a party to the suit with the oblique motive of obtaining a collusive decree behind the back of the Applicant.

4. That the Applicant is both a necessary and proper party. If any decree is passed in the present suit without the Applicant on record, it will prejudice the Applicant's valuable property rights and lead to multiple rounds of litigation.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Implead the Applicant as Defendant No. [ ] in O.S. No. [ ] of 202[ ];
(b) Permit the Applicant to file Written Statement and participate in the proceedings; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 30. REPRESENTATIVE SUIT (ORDER I RULE 8)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="representative_suit_o1_r8",
        title="Application for Leave to Sue in Representative Capacity & Notice",
        provision="Order I Rule 8 CPC",
        category="Parties & Capacity",
        summary="Application for permission of the court to institute or defend a suit in a representative capacity on behalf of numerous persons having the same interest.",
        practice_notes="Order I Rule 8(2): Court MUST give notice of the institution of the suit to all persons so interested, either by personal service or by public advertisement at plaintiff's expense. No compromise or abandonment can be made without leave of the court and prior notice under Rule 8(4).",
        connected_provisions=[
            {"kind": "rule", "ref": "Order I Rule 8", "title": "One person may sue or defend on behalf of all in same interest"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF REPRESENTATIVES NAMES]                                  ... APPLICANTS / PLAINTIFFS
VERSUS
[DEFENDANT NAMES]                                                  ... RESPONDENTS / DEFENDANTS

APPLICATION UNDER ORDER I RULE 8 READ WITH SECTION 151 CPC

The Applicants / Plaintiffs respectfully submit as under:

1. That the Plaintiffs have instituted the accompanying Suit for [DECLARATION OF PUBLIC CHARITABLE TRUST / COMMON PATHWAY EASEMENT / RESIDENTS WELFARE].

2. COMMONALITY OF INTEREST:
That there are numerous persons (more than [NUMBER] residents/beneficiaries) who have the same common interest in the subject matter of the Suit. It is practically impossible to join all such persons individually as co-plaintiffs.

3. That the Plaintiffs are members / office bearers of the [NAME OF ASSOCIATION / COMMUNITY] and represent the common grievances of all persons interested.

4. That the Plaintiffs undertake to bear all expenses for publishing public notice of the institution of the suit in two leading newspapers (one English and one vernacular) as directed by this Court.

PRAYER:
Wherefore, the Applicants pray that this Hon'ble Court may be pleased to:
(a) Grant leave to the Plaintiffs to sue in a representative capacity on behalf of all [RESIDENTS / BENEFICIARIES] under Order I Rule 8 CPC;
(b) Approve the draft public advertisement notice and direct publication in daily newspapers; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANTS
"""
    ),

    # -------------------------------------------------------------------------
    # 31. GUARDIAN AD LITEM (ORDER XXXII RULES 3 & 15)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="guardian_ad_litem_o32_r3",
        title="Application for Appointment of Guardian ad Litem for Minor",
        provision="Order XXXII Rules 3 & 15 CPC",
        category="Parties & Capacity",
        summary="Application for appointment of a fit and proper person as guardian ad litem to represent a minor or person of unsound mind in civil litigation.",
        practice_notes="Order XXXII Rule 3(3): Application must be supported by an affidavit stating that the proposed guardian has no interest in the matters in controversy adverse to that of the minor. A decree passed against a minor without appointing a guardian ad litem is null and void (Ram Chandra v. Man Singh).",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXXII Rule 3", "title": "Guardian for the suit to be appointed by Court for minor defendant"},
            {"kind": "rule", "ref": "Order XXXII Rule 15", "title": "Rules 1 to 14 (except rule 2A) to apply to persons of unsound mind"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF NAME]                                                   ... APPLICANT / PLAINTIFF
VERSUS
[DEFENDANT 1 NAME] (MINOR),
Represented by natural guardian / proposed guardian [NAME]         ... RESPONDENT / DEFENDANT

APPLICATION UNDER ORDER XXXII RULE 3 READ WITH SECTION 151 CPC

The Applicant / Plaintiff respectfully submits as under:

1. That the Plaintiff has instituted the above Suit for [PARTITION / DECLARATION OF TITLE].

2. That Defendant No. [ ] is a minor aged about [ ] years, having been born on [DATE OF BIRTH], and is incapable of defending the suit on his own behalf.

3. That [PROPOSED GUARDIAN FULL NAME], aged about [ ] years, residing at [ADDRESS], is the natural mother / uncle / brother of the minor defendant.

4. That the proposed guardian is a fit and proper person to act as guardian ad litem, is in custody of the minor, and has NO interest whatsoever adverse to that of the minor in the subject matter of the Suit.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
Appoint [PROPOSED GUARDIAN NAME] as the Guardian ad Litem to represent the minor Defendant No. [ ] in the present Suit; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 32. STRIKE OUT IMPROPER PARTY (ORDER I RULE 10(1))
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="strike_out_party_o1_r10",
        title="Application for Striking Out Improperly Joined Defendant",
        provision="Order I Rule 10(1) & (2) CPC",
        category="Parties & Capacity",
        summary="Application by a misjoined defendant praying to be deleted and struck off from the array of parties on grounds of no relief claimed and misjoinder.",
        practice_notes="Where a defendant is neither a necessary nor proper party and no relief or cause of action is disclosed against him, the court will strike out his name under Order I Rule 10(2) to save him from unnecessary litigation costs and harassment.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order I Rule 10", "title": "Court may strike out or add parties"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[DEFENDANT NO. ___ FULL NAME]                                      ... APPLICANT / DEFENDANT
VERSUS
[PLAINTIFF FULL NAME]                                              ... RESPONDENT / PLAINTIFF

APPLICATION UNDER ORDER I RULE 10(2) READ WITH SECTION 151 CPC FOR DELETION OF PARTY

The Applicant / Defendant respectfully submits as under:

1. That the Plaintiff has arrayed the Applicant as Defendant No. [ ] in the above Suit.

2. MISJOINDER & LACK OF PRIVITY:
That a bare reading of the Plaint discloses that the Applicant has no privity of contract, no interest in the suit property, and no cause of action has been alleged against the Applicant. No substantive relief has been prayed against the Applicant.

3. That the Applicant was merely an attesting witness / broker / proforma officer having no personal or legal claim.

4. That the retention of the Applicant on record causes severe prejudice, embarrassment, and unwarranted legal expenses.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
Strike out and delete the name of the Applicant (Defendant No. [ ]) from the array of parties in O.S. No. [ ] of 202[ ]; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 33. EVIDENCE-IN-CHIEF AFFIDAVIT (ORDER XVIII RULE 4)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="chief_affidavit_o18_r4",
        title="Evidence-in-Chief Affidavit of Witness (PW-1 / DW-1)",
        provision="Order XVIII Rule 4 CPC",
        category="Evidence & Trial Proceedings",
        summary="Standard sworn evidence-in-chief affidavit of witness under Order XVIII Rule 4 CPC, with document marking clauses and formal verification.",
        practice_notes="Order XVIII Rule 4(1): The examination-in-chief of a witness shall be on affidavit. The deponent must enter the witness box to formally tender the affidavit on oath and identify original documents for marking exhibits. Cross-examination follows immediately thereafter.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XVIII Rule 4", "title": "Recording of evidence"},
            {"kind": "rule", "ref": "Order XVIII Rule 5", "title": "How evidence shall be taken in appealable cases"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF NAME]                                                   ... PLAINTIFF
VERSUS
[DEFENDANT NAME]                                                   ... DEFENDANT

EVIDENCE AFFIDAVIT OF [PW-1 / DW-1] UNDER ORDER XVIII RULE 4 OF THE CODE OF CIVIL PROCEDURE, 1908

I, [WITNESS FULL NAME], aged about [ ] years, S/o or D/o [PARENT NAME], residing at [ADDRESS], do hereby solemnly affirm and state on oath as follows:

1. I am the Plaintiff / Defendant in the above suit and am fully acquainted with the facts of the case. I am competent to depose to this affidavit.

2. I reiterate all the averments and contentions set out in the [Plaint / Written Statement] as part and parcel of this evidence affidavit to avoid prolixity.

3. [CHRONOLOGICAL FACTUAL DEPOSITION]:
That I acquired ownership of the Suit Schedule Property vide registered Sale Deed dated [DATE]. Since the date of purchase, I have been in lawful, peaceful, and uninterrupted physical possession. The electricity bills, tax receipts, and municipal khata extracts stand in my name.

4. That on [DATE], the Defendant along with his agents illegally attempted to trespass into the Suit Property...

5. TENDER & MARKING OF DOCUMENTS:
In support of my claim, I produce and tender the following original documents which may kindly be marked as Exhibits:
(a) Original Registered Sale Deed dated [DATE] marked as EXHIBIT P-1.
(b) Certified Khata Certificate dated [DATE] marked as EXHIBIT P-2.
(c) Property Tax Paid Receipts (5 Nos.) marked as EXHIBITS P-3 to P-7.
(d) Office copy of Statutory Legal Notice dated [DATE] marked as EXHIBIT P-8.
(e) Postal Acknowledgement card signed by Defendant marked as EXHIBIT P-9.

6. I state that the Plaintiff's claim is genuine, bona fide, and lawful, and the suit deserves to be decreed as prayed for.

                                                        DEPONENT

VERIFICATION
I, [WITNESS NAME], the deponent above named, do hereby verify that the contents of Paragraphs 1 to 6 are true and correct to my personal knowledge. Nothing material has been concealed therefrom.
Verified at [CITY] on this [DAY] day of [MONTH], 202[ ]
                                                        DEPONENT
"""
    ),

    # -------------------------------------------------------------------------
    # 34. WITNESS SUMMONS APPLICATION (ORDER XVI RULES 1 & 2)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="witness_summons_o16_r1_2",
        title="Application for Issuance of Witness Summons & Batta Memo",
        provision="Order XVI Rules 1 & 2 CPC",
        category="Evidence & Trial Proceedings",
        summary="Application praying for issuance of witness summons to official witnesses (Sub-Registrar, Bank Manager, Surveyor) to produce records and give evidence.",
        practice_notes="Order XVI Rule 2: The party applying for summons shall, before summons is granted, pay into court such sum of money as appears to the court reasonable to defray the expenses of the witness in travelling to and from court (diet money and travelling allowance).",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XVI Rule 1", "title": "List of witnesses and summons to witnesses"},
            {"kind": "rule", "ref": "Order XVI Rule 2", "title": "Expenses of witness to be paid into Court on applying for summons"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF / DEFENDANT NAME]                                       ... APPLICANT
VERSUS
[OPPOSITE PARTY NAME]                                              ... RESPONDENT

APPLICATION UNDER ORDER XVI RULES 1 & 2 READ WITH SECTION 151 CPC

The Applicant respectfully submits as under:

1. That the above Suit is posted for [PLAINTIFF / DEFENDANT] Evidence.

2. That in order to prove [FACT TO BE PROVED: e.g. genuine execution of Sale Deed / disbursement of loan / certified village map], the evidence and production of official records by the following witness is absolutely essential and crucial:

   WITNESS DETAILS:
   THE SENIOR SUB-REGISTRAR,
   Office of the Sub-Registrar, [LOCATION/CITY].
   RECORDS TO BE PRODUCED: Original Volume Register Book 1 containing Document No. [ ] of [YEAR] registered on [DATE].

3. That the said witness is an official public custodian who cannot attend court without official summons issued by this Hon'ble Court.

4. That the Applicant has deposited the prescribed witness batta and conveyance charges into court vide Batta Memo annexed herewith.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
Issue official Witness Summons to the witness named above directing him to appear before this Court on [DATE] with the specified original records to give evidence; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 35. INTERROGATORIES & ANSWERS (ORDER XI RULES 1 & 8)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="interrogatories_o11_r1_8",
        title="Interrogatories for Examination of Opposite Party & Answer Affidavit",
        provision="Order XI Rules 1 & 8 CPC",
        category="Evidence & Trial Proceedings",
        summary="Written interrogatories delivered by one party for examination of the adversary, with the statutory form of affidavit in answer.",
        practice_notes="Order XI Rule 1 enables delivery of interrogatories relating to matters in question in the suit. Interrogatories that do not relate to any matters in question are irrelevant. Answer must be by affidavit filed within 10 days under Rule 8.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XI Rule 1", "title": "Discovery by interrogatories"},
            {"kind": "rule", "ref": "Order XI Rule 8", "title": "Affidavit in answer, filing"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF NAME]                                                   ... PLAINTIFF
VERSUS
[DEFENDANT NAME]                                                   ... DEFENDANT

INTERROGATORIES DELIVERED BY THE PLAINTIFF FOR EXAMINATION OF THE DEFENDANT UNDER ORDER XI RULE 1 CPC

The Plaintiff requires the Defendant, [DEFENDANT FULL NAME], to answer on oath the following interrogatories within 10 days:

1. Did you or did you not sign the Agreement to Sell dated [DATE] in the presence of witnesses [NAMES]?
2. Did you receive a sum of Rs. [AMOUNT] on [DATE] through RTGS Transaction Ref No. [ ] from the Plaintiff's bank account?
3. State whether on the date of execution of the said Agreement, you had mortgaged the suit property with [BANK NAME].
4. State the name and branch of the Bank where your savings account was maintained on [DATE].

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF


AFFIDAVIT IN ANSWER TO INTERROGATORIES (ORDER XI RULE 8 CPC)
I, [DEFENDANT FULL NAME], aged [ ] years, residing at [ADDRESS], do hereby state on oath:
In answer to the interrogatories delivered by the Plaintiff, I state as follows:
To Interrogatory No. 1: I answer that [INSERT SPECIFIC ANSWER].
To Interrogatory No. 2: I answer that [INSERT SPECIFIC ANSWER].
Solemnly affirmed at [CITY] on this [DAY] day of [MONTH], 202[ ]
                                                        DEPONENT
"""
    ),

    # -------------------------------------------------------------------------
    # 36. NOTICE TO ADMIT DOCUMENTS / FACTS (ORDER XII RULES 2 & 4)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="notice_admit_documents_o12_r2",
        title="Notice to Admit Documents and Facts (Order XII Rules 2 & 4 CPC)",
        provision="Order XII Rules 2 & 4 CPC",
        category="Evidence & Trial Proceedings",
        summary="Formal notice calling upon the opposite party to admit the authenticity/execution of specific documents within 7 days, shifting the costs of proof.",
        practice_notes="Order XII Rule 2: Either party may call upon the other to admit any document. In case of refusal or neglect to admit after notice, the costs of proving such document shall be paid by the party so neglecting or refusing, whatever the result of the suit may be.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XII Rule 2", "title": "Notice to admit documents"},
            {"kind": "rule", "ref": "Order XII Rule 4", "title": "Notice to admit facts"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF NAME]                                                   ... PLAINTIFF
VERSUS
[DEFENDANT NAME]                                                   ... DEFENDANT

NOTICE TO ADMIT DOCUMENTS UNDER ORDER XII RULE 2 OF THE CODE OF CIVIL PROCEDURE, 1908

TO:
[DEFENDANT / PLAINTIFF FULL NAME],
Through his Counsel, [ADVOCATE NAME], Advocate, [CITY].

TAKE NOTICE that the Plaintiff [or Defendant] in this Suit proposes to adduce in evidence the several documents specified in the Schedule below, and that the same may be inspected by the Defendant [or Plaintiff], his pleader or agent, at [OFFICE/COURT LOCATION] on [DATE] between [TIME] AM and [TIME] PM.

YOU ARE HEREBY REQUIRED within seven (7) days from the service of this notice to admit that such of the said documents as are specified to be originals were respectively written, signed, or executed as they purport respectively to have been; that such as are specified as copies are true copies; and such documents as are stated to have been served, sent, or delivered were so served, sent, or delivered respectively.

SCHEDULE OF DOCUMENTS
1. Agreement of Sale dated [DATE] executed between [PARTY A] and [PARTY B].
2. Legal Notice dated [DATE] dispatched by RPAD.
3. Postal Acknowledgement Card dated [DATE] bearing signature of [DEFENDANT].

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF
"""
    ),

    # -------------------------------------------------------------------------
    # 37. RETURN OF ORIGINAL DOCUMENTS (ORDER XIII RULE 9)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="return_documents_o13_r9",
        title="Application for Return of Original Documents / Exhibits",
        provision="Order XIII Rule 9 CPC",
        category="Evidence & Trial Proceedings",
        summary="Application by party praying for return of marked original exhibits (title deeds, cheques, accounts) upon substituting certified/authenticated copies.",
        practice_notes="Order XIII Rule 9: Any person desirous of receiving back any document produced by him in the suit may receive the same upon substituting a certified copy, provided that no document shall be returned which has, by force of the decree, become wholly void or useless.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XIII Rule 9", "title": "Return of admitted documents"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF / DEFENDANT NAME]                                       ... APPLICANT
VERSUS
[OPPOSITE PARTY NAME]                                              ... RESPONDENT

APPLICATION UNDER ORDER XIII RULE 9 READ WITH SECTION 151 CPC FOR RETURN OF DOCUMENTS

The Applicant respectfully submits as under:

1. That the above Suit was disposed of on [DATE] / is currently pending trial.

2. That the Applicant has marked and produced the following original valuable documents in evidence as exhibits:
   (a) Exhibit P-1: Original Registered Sale Deed dated [DATE] (Document No. [ ] of [YEAR]).
   (b) Exhibit P-2: Original Approved Building Plan / Sanction Order.

3. That the Applicant urgently requires the said original documents for producing before [BANK NAME for loan processing / MUNICIPAL CORPORATION for khata registration].

4. That the Applicant undertakes to substitute verified true photocopies / certified copies of the said documents to remain on the court record, and further undertakes to produce the originals whenever directed by this Hon'ble Court.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Permit the Applicant to substitute certified copies of Exhibits P-1 and P-2 on record;
(b) Return the original documents Exhibits P-1 and P-2 to the Applicant or his counsel; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 38. FORENSIC / HANDWRITING EXPERT (SECTION 45 EVIDENCE ACT)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="handwriting_expert_sec45",
        title="Application for Scientific / Forensic Handwriting Expert Opinion",
        provision="Section 45 Indian Evidence Act r/w Order XXVI Rule 10A CPC",
        category="Evidence & Trial Proceedings",
        summary="Application praying to send disputed signatures or thumb impressions to the State Forensic Science Laboratory (FSL) for comparison with admitted signatures.",
        practice_notes="Order XXVI Rule 10A authorizes the court to issue a commission for scientific investigation. The disputed signature must be compared with contemporaneous admitted signatures (signatures made around the same period, not signatures created decades later).",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXVI Rule 10A", "title": "Commission for scientific investigation"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[DEFENDANT / PLAINTIFF FULL NAME]                                  ... APPLICANT
VERSUS
[OPPOSITE PARTY NAME]                                              ... RESPONDENT

APPLICATION UNDER ORDER XXVI RULE 10A READ WITH SECTION 151 CPC AND SECTION 45 OF EVIDENCE ACT

The Applicant respectfully submits as under:

1. That the Plaintiff has based his claim on an alleged [PROMISSORY NOTE / WILL / AGREEMENT OF SALE] dated [DATE] marked as Exhibit [ ].

2. That the Applicant has categorically and specifically denied the execution of the said document in his Written Statement, stating that the signature appearing thereon is a forged and fabricated signature.

3. CONTEMPORANEOUS ADMITTED SIGNATURES:
That the Applicant has produced contemporaneous admitted signatures appearing on:
   (a) Registered Sale Deed dated [DATE] (Exhibit D-1).
   (b) Bank Account Opening Form / Specimen Signature Card of [BANK NAME] (Exhibit D-2).

4. That in order to arrive at a just conclusion on the issue of forgery, it is indispensable that the disputed signature on Exhibit [ ] and the admitted signatures on Exhibit [ ] be referred to the State Forensic Science Laboratory (FSL) / qualified Handwriting and Questioned Document Expert for scientific examination and report.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Refer the disputed document Exhibit [ ] and admitted documents Exhibit [ ] to the Director, Forensic Science Laboratory (FSL) for scientific comparison and opinion;
(b) Direct the Expert to submit a detailed report on the genuineness of the signature; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 39. COMMISSION TO EXAMINE WITNESS (ORDER XXVI RULES 1 & 4)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="commission_witness_o26_r1_4",
        title="Application for Examination of Witness on Commission & Affidavit",
        provision="Order XXVI Rules 1 & 4 CPC",
        category="Evidence & Trial Proceedings",
        summary="Application for appointment of an Advocate Commissioner to record the deposition/evidence of an elderly, bedridden, or infirm witness at their residence.",
        practice_notes="Order XXVI Rule 1: Any court may issue a commission for the examination on interrogatories or otherwise of any person resident within the local limits of its jurisdiction who is from sickness or infirmity unable to attend it. Medical certificate must be annexed.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXVI Rule 1", "title": "Cases in which Court may issue commission to examine witness"},
            {"kind": "rule", "ref": "Order XXVI Rule 4", "title": "Persons for whose examination commission may issue"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF / DEFENDANT NAME]                                       ... APPLICANT
VERSUS
[OPPOSITE PARTY NAME]                                              ... RESPONDENT

APPLICATION UNDER ORDER XXVI RULES 1 & 4 READ WITH SECTION 151 CPC

The Applicant respectfully submits as under:

1. That the above Suit is posted for examination of [PW-2 / DW-2], namely [WITNESS NAME].

2. That the said witness is aged about [ ] years and is suffering from [GRAVE INFIRMITY: e.g. advanced Parkinson's disease / paralytic stroke / acute cardiac ailment], and is completely bedridden and unable to move or travel to court.

3. That the medical certificate issued by Dr. [NAME], [HOSPITAL/CLINIC] certifying the physical inability of the witness to attend court is annexed herewith as Annexure A.

4. That the evidence of the said witness is vital, material, and indispensable to the Applicant's case.

5. That it is just and necessary that an Advocate Commissioner be appointed to visit the residence of the witness at [ADDRESS] and record his evidence.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Appoint an Advocate Commissioner to record the examination-in-chief and cross-examination of the witness [NAME] at his residence;
(b) Fix the date, time, and Commissioner's remuneration; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 40. SUIT FOR CANCELLATION OF SALE DEED (SECTION 31 SRA)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="plaint_cancellation_deed",
        title="Plaint in Suit for Cancellation of Void / Voidable Sale Deed",
        provision="Section 31 Specific Relief Act r/w Order VII CPC",
        category="Core Pleadings",
        summary="Plaint challenging a fraudulent registered sale deed executed by impersonation, fraud, or undue influence, with prayer to adjudge deed void and send copy to Sub-Registrar.",
        practice_notes="Section 31 Specific Relief Act: Any person against whom a written instrument is void or voidable may sue to have it adjudged void; the court will order it delivered up and cancelled and send a copy of the decree to the registration officer. Limitation under Article 59: 3 years from when facts entitling plaintiff to have instrument cancelled become known.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"},
            {"kind": "limitation_article", "ref": "Article 59", "title": "To cancel or set aside an instrument or decree (3 years)"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF FULL NAME],
Aged [ ] years, Residing at [ADDRESS]                              ... PLAINTIFF
VERSUS
1. [DEFENDANT 1 FULL NAME (PURCHASER)]                             ... DEFENDANT 1
2. [DEFENDANT 2 FULL NAME (IMPERSONATOR / VENDOR)]                 ... DEFENDANT 2

SUIT FOR CANCELLATION OF REGISTERED SALE DEED DATED [DATE] UNDER SECTION 31 OF THE SPECIFIC RELIEF ACT, 1963

The Plaintiff above named respectfully submits as under:

1. That the Plaintiff is the true, absolute, and lawful owner in possession of the Suit Schedule Property, having acquired the same vide [TITLE DEED] dated [DATE].

2. FRAUD & IMPERSONATION:
That on [DATE], the Plaintiff was shocked to discover from an Encumbrance Certificate that a registered Sale Deed dated [DATE] (Document No. [ ] of [YEAR] at SRO [ ]) had been fraudulently registered in favour of Defendant No. 1, purporting to have been executed by the Plaintiff.

3. That the Plaintiff NEVER executed the said Sale Deed, never appeared before the Sub-Registrar, and never received any consideration. Defendant No. 2 impersonated the Plaintiff by affixing a forged photograph and forged signatures in active collusion with Defendant No. 1.

4. That the impugned Sale Deed is void ab initio, fraudulent, non-est, and sham, casting a dark cloud over the Plaintiff's lawful title.

5. LIMITATION (ARTICLE 59):
The Plaintiff first discovered the existence of the fraudulent Sale Deed on [DATE OF KNOWLEDGE]. The suit is within the 3-year limitation period from the date of knowledge under Article 59 of the Limitation Act, 1963.

PRAYER:
Wherefore, the Plaintiff prays for a judgment and decree:
(a) Adjudging and declaring that the registered Sale Deed dated [DATE] (Doc No. [ ]) is null, void, and fraudulent;
(b) Ordering cancellation of the said Sale Deed and directing that a copy of the decree be sent to the Sub-Registrar, [SRO NAME] to cancel the registration entry under Section 31(2) SRA;
(c) Permanent Injunction restraining Defendant No. 1 from alienating or interfering with the property;
(d) Awarding costs of the suit.

SCHEDULE OF PROPERTY
[Insert full property particulars, survey no., boundaries]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF
"""
    ),

    # -------------------------------------------------------------------------
    # 41. EJECTMENT / EVICTION OF TENANT (SECTION 106 TPA)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="plaint_ejectment_tenant",
        title="Plaint in Suit for Ejectment of Tenant & Arrears of Rent",
        provision="Section 106 Transfer of Property Act r/w Order VII CPC",
        category="Core Pleadings",
        summary="Civil suit for recovery of physical possession of commercial/residential premises from an overstaying tenant after statutory termination of lease, with mesne profits.",
        practice_notes="Mandatory compliance with Section 106 TPA: 15 days notice expiring with the end of the tenancy month (or 6 months for agricultural/manufacturing leases). Proof of service of termination notice by RPAD/courier is a condition precedent to maintainability.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"},
            {"kind": "limitation_article", "ref": "Article 67", "title": "By a landlord to recover possession from a tenant (12 years from determination of tenancy)"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[LANDLORD FULL NAME],
Aged [ ] years, Residing at [ADDRESS]                              ... PLAINTIFF
VERSUS
[TENANT FULL NAME],
Aged [ ] years, Residing at [SUIT PREMISES ADDRESS]                ... DEFENDANT

SUIT FOR EJECTMENT / EVICTION, RECOVERY OF ARREARS OF RENT, AND DAMAGES FOR USE AND OCCUPATION

The Plaintiff above named respectfully submits as under:

1. That the Plaintiff is the absolute owner and landlord of the commercial / residential premises described in the Schedule hereunder.

2. TENANCY TERMS:
That the Defendant was inducted as a monthly tenant under an oral / written Lease Agreement dated [DATE] on a monthly rent of Rs. [RENT AMOUNT], payable on or before the [5th] of every English calendar month.

3. ARREARS OF RENT:
That the Defendant chronically defaulted in payment of rents and has failed to pay rent from [MONTH/YEAR] to [MONTH/YEAR], accumulating arrears of Rs. [TOTAL ARREARS].

4. STATUTORY TERMINATION OF TENANCY (SECTION 106 TPA):
That the Plaintiff caused a Statutory Notice dated [DATE] under Section 106 of the Transfer of Property Act, 1882 terminating the monthly tenancy with the expiry of 15 days from the date of receipt, and demanding delivery of vacant possession on or before [DATE]. The notice was duly served on the Defendant on [DATE] (Postal Acknowledgement annexed).

5. STATUS AS UNAUTHORIZED OCCUPANT:
With the expiration of the notice period on [DATE], the tenancy stood determined. The Defendant is occupying the premises as a trespasser / unauthorized occupant, and is liable to pay damages / mesne profits at the market rate of Rs. [AMOUNT] per month until delivery of vacant possession.

PRAYER:
Wherefore, the Plaintiff prays for a judgment and decree:
(a) Directing the Defendant to quit, vacate, and deliver vacant physical possession of the Schedule Premises to the Plaintiff;
(b) Directing payment of arrears of rent of Rs. [AMOUNT];
(c) Directing an enquiry into mesne profits / damages from the date of suit till delivery of possession under Order XX Rule 12 CPC;
(d) Awarding costs of the suit.

SCHEDULE OF LEASED PREMISES
[Insert shop/flat number, floor, boundaries, and measurements]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF
"""
    ),

    # -------------------------------------------------------------------------
    # 42. EASEMENTARY INJUNCTION (SECTIONS 38 & 39 SRA)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="plaint_easement_injunction",
        title="Plaint for Injunction Protecting Easementary Rights of Light & Air",
        provision="Sections 38 & 39 Specific Relief Act r/w Indian Easements Act",
        category="Core Pleadings",
        summary="Civil suit for perpetual and mandatory injunction to restrain construction that obstructs ancient lights, air, and prescriptive right of way.",
        practice_notes="Under Section 15 of the Indian Easements Act, 1882, the right to access of light and air must have been peaceably enjoyed without interruption for twenty years. Limitation under Article 25 Limitation Act: Suit must be brought within 2 years of the end of the 20-year period.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"},
            {"kind": "limitation_article", "ref": "Article 25", "title": "For compensation for obstructing an easement (3 years)"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF FULL NAME],
Residing at [ADDRESS]                                              ... PLAINTIFF
VERSUS
[DEFENDANT FULL NAME],
Residing at [ADDRESS]                                              ... DEFENDANT

SUIT FOR PERPETUAL AND MANDATORY INJUNCTION PROTECTING EASEMENTARY RIGHTS

The Plaintiff above named respectfully submits as under:

1. That the Plaintiff is the owner and occupier of the residential building described in Schedule 'A' hereunder, constructed in the year [YEAR].

2. ACQUISITION OF PRESCRIPTIVE EASEMENT (SECTION 15 EASEMENTS ACT):
That on the [EASTERN / SOUTHERN] wall of the Plaintiff's house, there are ancient windows and ventilators through which the Plaintiff and his family have enjoyed uninterrupted, open, and peaceful access of light and air for more than 30 continuous years, thereby acquiring an absolute and indefeasible prescriptive easementary right.

3. DEFENDANT'S ILLEGAL CONSTRUCTION:
That the Defendant, owner of the adjacent plot described in Schedule 'B', has recently commenced unauthorized construction of a high-rise structure without leaving statutory setbacks, deliberately erecting a concrete wall flush against the Plaintiff's windows, completely choking and extinguishing all light, ventilation, and air.

4. That the obstruction renders the Plaintiff's residential premises uninhabitable, dark, and damp, causing severe physical discomfort.

PRAYER:
Wherefore, the Plaintiff prays for a judgment and decree:
(a) Granting a Permanent Injunction restraining the Defendant from raising any construction in violation of statutory setback rules obstructing the Plaintiff's access to light and air;
(b) Granting a Mandatory Injunction directing the Defendant to demolish the unauthorized concrete structure erected adjacent to the Plaintiff's windows;
(c) Awarding costs of the suit.

SCHEDULE 'A' (PLAINTIFF'S DOMINANT HERITAGE)
SCHEDULE 'B' (DEFENDANT'S SERVIENT HERITAGE)

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF
"""
    ),

    # -------------------------------------------------------------------------
    # 43. COMMERCIAL SUIT PLAINT & STATEMENT OF TRUTH
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="plaint_commercial_suit",
        title="Plaint in Commercial Suit with Mandatory Statement of Truth",
        provision="Commercial Courts Act, 2015 r/w Order VI Rule 15A CPC",
        category="Core Pleadings",
        summary="Complete commercial suit plaint for unpaid commercial invoices with mandatory Statement of Truth (Order VI Rule 15A) and Section 12A Pre-Institution Mediation averments.",
        practice_notes="Commercial Courts Act, 2015: Section 12A mandates Pre-Institution Mediation unless urgent interim relief is contemplated. Order VI Rule 15A: Statement of Truth is MANDATORY; if not filed, pleadings cannot be treated as evidence. Commercial suits require strict disclosure of all documents in plaintiff's custody under Order XI.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"}
        ],
        template_text="""IN THE COURT OF THE PRINCIPAL DISTRICT & SESSIONS JUDGE (COMMERCIAL COURT) AT [CITY]
COMMERCIAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF COMPANY / ENTERPRISE NAME],
Through its Authorized Signatory, [NAME],
Registered Office at [ADDRESS]                                     ... PLAINTIFF
VERSUS
[DEFENDANT FIRM / COMPANY NAME],
Having Office at [ADDRESS]                                         ... DEFENDANT

COMMERCIAL SUIT FOR RECOVERY OF RS. [AMOUNT] UNDER COMMERCIAL COURTS ACT, 2015

The Plaintiff above named respectfully submits as under:

1. COMMERCIAL DISPUTE & JURISDICTION:
The dispute arises out of a commercial transaction for sale and purchase of goods between merchants, falling squarely within the definition of a 'Commercial Dispute' under Section 2(1)(c) of the Commercial Courts Act, 2015. The specified value is Rs. [AMOUNT], which exceeds the threshold limit of Rs. 3,00,000/-.

2. SECTION 12A PRE-INSTITUTION MEDIATION COMPLIANCE:
The Plaintiff initiated Pre-Institution Mediation before the District Legal Services Authority (DLSA) on [DATE]. The Defendant failed to appear, and a Non-Starter Report dated [DATE] was issued by the DLSA (Annexure A). / The Plaintiff seeks urgent interim relief under Section 12A(1) proviso.

3. INVOICES & OUTSTANDING DEBT:
The Plaintiff supplied [GOODS] vide Tax Invoices Nos. [ ] to [ ] dated [DATES]. The Defendant accepted delivery without protest, but failed to clear the principal invoice amount of Rs. [AMOUNT] despite statutory demand notice dated [DATE].

PRAYER:
Wherefore, the Plaintiff prays for a judgment and decree:
(a) Directing the Defendant to pay a sum of Rs. [AMOUNT] along with commercial interest at 18% p.a. from due date till realization under Section 34 CPC;
(b) Awarding actual commercial costs under Section 35 CPC.


STATEMENT OF TRUTH UNDER ORDER VI RULE 15A CPC
(MANDATORY UNDER COMMERCIAL COURTS ACT, 2015)
I, [AUTHORIZED SIGNATORY NAME], aged [ ] years, residing at [ADDRESS], do hereby solemnly affirm and declare:
1. I am the Authorized Signatory of the Plaintiff Company and am duly competent to depose.
2. I say that the contents of the Plaint from Paragraphs 1 to [ ] are true to my knowledge and information.
3. I say that all documents in the power, possession, control, or custody of the Plaintiff relating to any matter in question in the proceedings have been disclosed and copies produced with the plaint, and that the Plaintiff does not have any other documents with him.
Solemnly affirmed at [CITY] on this [DAY] day of [MONTH], 202[ ]
                                                        DEPONENT
"""
    ),

    # -------------------------------------------------------------------------
    # 44. INDIGENT PERSON APPLICATION (ORDER XXXIII)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="suit_indigent_person_o33",
        title="Application for Leave to Sue as an Indigent Person (In Forma Pauperis)",
        provision="Order XXXIII Rule 1 CPC",
        category="Pre-Emptive & Protective Proceedings",
        summary="Application by an impoverished litigant praying for exemption from payment of ad-valorem court fees, with mandatory schedule of movable/immovable assets.",
        practice_notes="Order XXXIII Rule 1 Explanation: An indigent person is one who is not possessed of sufficient means to pay the fee prescribed by law for the plaint. Order XXXIII Rule 2 requires a schedule of any movable or immovable property belonging to the applicant with the estimated value thereof.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXXIII Rule 1", "title": "Suits may be instituted by indigent persons"},
            {"kind": "rule", "ref": "Order XXXIII Rule 2", "title": "Contents of application"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
MISC. APPLICATION NO. _______ OF 202[ ] (INDIGENT OP)
IN
PROPOSED ORIGINAL SUIT NO. _______ OF 202[ ]

[APPLICANT FULL NAME],
Aged [ ] years, S/o [PARENT NAME], Residing at [ADDRESS]            ... APPLICANT
VERSUS
1. [DEFENDANT FULL NAME]                                           ... RESPONDENT 1
2. THE DISTRICT COLLECTOR, [DISTRICT NAME]                         ... RESPONDENT 2 (GOVT)

APPLICATION UNDER ORDER XXXIII RULES 1 & 2 READ WITH SECTION 151 CPC

The Applicant respectfully submits as under:

1. That the Applicant has prepared the accompanying Plaint claiming damages / compensation of Rs. [AMOUNT] for [ROAD ACCIDENT / TORT / BREACH OF CONTRACT].

2. That the ad-valorem court fee payable on the Plaint under the Court Fees Act is Rs. [AMOUNT].

3. PAUPER STATUS / LACK OF MEANS:
The Applicant is a daily-wage laborer / destitute widow living in extreme penury, with no regular income. The Applicant does not possess sufficient means to pay the heavy court fee of Rs. [AMOUNT] prescribed by law.

4. That the Applicant has not entered into any agreement with reference to the subject matter of the proposed suit under which any other person has obtained an interest in such subject-matter.

5. SCHEDULE OF ASSETS (ORDER XXXIII RULE 2):
A full, true, and exhaustive schedule of all movable and immovable property belonging to the Applicant with their estimated value is set forth in the Schedule hereunder. The total value of all assets does not exceed Rs. [2,000/-], excluding necessary wearing apparel.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Hold an enquiry into the pauperism of the Applicant through the District Collector under Order XXXIII Rule 6 CPC;
(b) Grant leave and permission to the Applicant to institute the Suit as an indigent person without paying court fees; in the interest of justice.

SCHEDULE OF ASSETS BELONGING TO APPLICANT
1. Wearing apparel and cooking utensils (exempted u/s 60 CPC) : Rs. Nil
2. Utensils and bedding                                       : Rs. 800/-
Total estimated value of all assets                           : Rs. 800/-

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 45. COMPROMISE PETITION (ORDER XXIII RULE 3)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="compromise_petition_o23_r3",
        title="Joint Compromise Petition & Settlement Terms (Order XXIII Rule 3 CPC)",
        provision="Order XXIII Rule 3 CPC",
        category="Settlement & Compromise",
        summary="Bilateral compromise petition signed by both parties and advocates recording lawful settlement terms, requesting decree in terms thereof and refund of court fees.",
        practice_notes="Order XXIII Rule 3: Agreement must be in writing and signed by parties. It must be lawful (not contrary to public policy or prohibited by law). Under Section 16 of Court Fees Act / Section 89 CPC, parties are entitled to full refund of court fees on settlement.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXIII Rule 3", "title": "Compromise of suit"},
            {"kind": "section", "ref": "Section 89", "title": "Settlement of disputes outside the Court"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF FULL NAME]                                              ... PLAINTIFF
VERSUS
[DEFENDANT FULL NAME]                                              ... DEFENDANT

JOINT COMPROMISE PETITION UNDER ORDER XXIII RULE 3 READ WITH SECTION 151 CPC

The Plaintiff and the Defendant above named respectfully submit as under:

1. That with the intervention of elders, mutual friends, and well-wishers, the parties have amicably resolved and settled all their disputes and claims in the Suit on the following lawful terms:

TERMS OF COMPROMISE:
(a) The Defendant admits the Plaintiff's title and lawful ownership over the Suit Schedule Property.
(b) The Defendant has this day voluntarily vacated and delivered vacant physical possession of the Suit Property to the Plaintiff, the receipt whereof the Plaintiff hereby acknowledges.
(c) The Defendant has agreed to pay, and has this day paid, a sum of Rs. [AMOUNT] to the Plaintiff vide Demand Draft No. [ ] dated [DATE] drawn on [BANK NAME] in full and final satisfaction of all arrears and mesne profits.
(d) The Plaintiff gives up all further claims against the Defendant in respect of damages and costs.
(e) Neither party shall have any remaining claim against the other arising out of the subject matter of this Suit.

2. That the compromise is entered into voluntarily, out of the parties' free will and consent, without any coercion, fraud, or undue influence, and is entirely lawful.

PRAYER:
Wherefore, the parties jointly pray that this Hon'ble Court may be pleased to:
(a) Record this Joint Compromise Petition under Order XXIII Rule 3 CPC;
(b) Pass a Decree in terms of the compromise;
(c) Direct refund of the admissible institution Court Fee to the Plaintiff under Section 16 of the Court Fees Act; in the interest of justice.

PLAINTIFF                                               DEFENDANT

ADVOCATE FOR PLAINTIFF                                  ADVOCATE FOR DEFENDANT
"""
    ),

    # -------------------------------------------------------------------------
    # 46. WITHDRAWAL OF SUIT (ORDER XXIII RULE 1)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="withdrawal_suit_o23_r1",
        title="Application for Withdrawal of Suit with Liberty to File Fresh Suit",
        provision="Order XXIII Rule 1(3) CPC",
        category="Settlement & Compromise",
        summary="Application by plaintiff seeking permission to withdraw suit on account of a formal defect with express liberty to institute a fresh suit on the same cause of action.",
        practice_notes="Order XXIII Rule 1(3): Court may grant permission to withdraw with liberty ONLY where: (a) suit must fail by reason of some formal defect; or (b) there are sufficient grounds for allowing the plaintiff to institute a fresh suit. If withdrawn without liberty, plaintiff is barred from suing afresh.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXIII Rule 1", "title": "Withdrawal of suit or abandonment of part of claim"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF NAME]                                                   ... APPLICANT / PLAINTIFF
VERSUS
[DEFENDANT NAME]                                                   ... RESPONDENT / DEFENDANT

APPLICATION UNDER ORDER XXIII RULE 1(3) READ WITH SECTION 151 CPC

The Applicant / Plaintiff respectfully submits as under:

1. That the Plaintiff has instituted the above Suit for [PERMANENT INJUNCTION / DECLARATION].

2. FORMAL DEFECT:
That due to an inadvertent error and miscommunication in instructions, the Plaint suffers from a fatal formal defect: [STATE FORMAL DEFECT: e.g. Failure to issue statutory notice under Section 80 CPC / incorrect survey number given in schedule / non-joinder of co-owner which cannot be cured by simple amendment].

3. That on account of the said technical and formal defect, the Suit is likely to fail without any adjudication on the merits of the Plaintiff's valuable substantive rights.

4. That no prejudice will be caused to the Defendant if the Plaintiff is permitted to withdraw the present suit with liberty to institute a fresh, comprehensive suit on the same cause of action curing the formal defect.

PRAYER:
Wherefore, the Applicant / Plaintiff prays that this Hon'ble Court may be pleased to:
(a) Permit the Plaintiff to withdraw the Suit O.S. No. [ ] of 202[ ];
(b) Grant express liberty to the Plaintiff under Order XXIII Rule 1(3) CPC to institute a fresh suit on the same cause of action; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 47. RESTORATION OF SUIT (ORDER IX RULE 9)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="restoration_suit_o9_r9",
        title="Application for Restoration of Suit Dismissed for Default & Affidavit",
        provision="Order IX Rule 9 CPC r/w Section 151",
        category="Post-Decree & Restoration Remedies",
        summary="Application by plaintiff to set aside dismissal of suit for default (when defendant appeared but plaintiff failed to appear under Rule 8) showing sufficient cause.",
        practice_notes="Limitation under Article 122 Limitation Act: STRICT 30 DAYS from the date of dismissal. If filed after 30 days, Section 5 condonation application must accompany. Order IX Rule 9(1) bars any fresh suit on the same cause of action; restoration application is the sole remedy.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order IX Rule 8", "title": "Procedure where defendant only appears"},
            {"kind": "rule", "ref": "Order IX Rule 9", "title": "Decree against plaintiff by default bars fresh suit"},
            {"kind": "limitation_article", "ref": "Article 122", "title": "To restore a suit or appeal or application for review or revision (30 days)"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
MISC. APPLICATION NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF FULL NAME]                                              ... APPLICANT / PLAINTIFF
VERSUS
[DEFENDANT FULL NAME]                                              ... RESPONDENT / DEFENDANT

APPLICATION UNDER ORDER IX RULE 9 READ WITH SECTION 151 CPC FOR RESTORATION OF SUIT

The Applicant / Plaintiff respectfully submits as under:

1. That the Plaintiff instituted the above Suit against the Defendant for [PARTITION / INJUNCTION / RECOVERY].

2. That the Suit was posted on [DATE] for [HEARING / ISSUES / EVIDENCE].

3. SUFFICIENT CAUSE FOR NON-APPEARANCE:
That when the case was called on [DATE], the Plaintiff and his counsel could not appear before this Court because [STATE PRECISE FACTUAL GROUND: e.g. The counsel's vehicle broke down en route / counsel was held up arguing a part-heard matter before Court Hall No. 3 / Plaintiff was struck in unprecedented traffic jam / sudden severe medical emergency]. This Hon'ble Court was pleased to dismiss the Suit for default under Order IX Rule 8 CPC.

4. That the absence of the Plaintiff and his counsel was completely unintentional, accidental, and due to bona fide circumstances beyond control.

5. LIMITATION (ARTICLE 122):
The suit was dismissed on [DATE], and the present application is filed on [DATE], which is strictly within the statutory limitation period of 30 days under Article 122 of the Limitation Act, 1963.

6. That the Plaintiff has a strong prima facie case, and if the suit is not restored, the Plaintiff will suffer irreparable injury without hearing on merits.

PRAYER:
Wherefore, the Applicant / Plaintiff prays that this Hon'ble Court may be pleased to:
(a) Set aside the order of dismissal for default dated [DATE];
(b) Restore Original Suit No. [ ] of 202[ ] to its original file and stage; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 48. RESTORATION UNDER ORDER IX RULE 4
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="restoration_suit_o9_r4",
        title="Application for Restoration of Suit Dismissed under Order IX Rule 2 or 3",
        provision="Order IX Rule 4 CPC",
        category="Post-Decree & Restoration Remedies",
        summary="Application to restore a suit dismissed for failure to pay process fees/postal charges (Rule 2) or where neither party appeared when called (Rule 3).",
        practice_notes="Under Order IX Rule 4, the plaintiff may either bring a fresh suit (subject to limitation) OR apply for an order to set the dismissal aside upon showing sufficient cause for not paying process fee or not appearing.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order IX Rule 2", "title": "Dismissal of suit where summons not served in consequence of plaintiff's failure to pay costs"},
            {"kind": "rule", "ref": "Order IX Rule 3", "title": "Where neither party appears, suit to be dismissed"},
            {"kind": "rule", "ref": "Order IX Rule 4", "title": "Plaintiff may bring fresh suit or Court may restore suit to file"}
        ],
        template_text="""IN THE COURT OF THE [CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
MISC. APPLICATION NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[PLAINTIFF FULL NAME]                                              ... APPLICANT / PLAINTIFF
VERSUS
[DEFENDANT FULL NAME]                                              ... RESPONDENT / DEFENDANT

APPLICATION UNDER ORDER IX RULE 4 READ WITH SECTION 151 CPC

The Applicant / Plaintiff respectfully submits as under:

1. That the Plaintiff instituted the above Suit for [RELIEF].

2. That the Suit was posted on [DATE] for [PAYMENT OF PROCESS FEE / APPEARANCE OF PARTIES].

3. That when the matter was called, this Hon'ble Court was pleased to dismiss the Suit under Order IX Rule [2 / 3] CPC as [process fee was not paid / neither party appeared].

4. SUFFICIENT CAUSE:
That the process fee could not be paid within time / counsel could not appear because [EXPLAIN: e.g. clerk mistakenly noted the date as [WRONG DATE] in the court diary / court process fee stamps were unavailable].

5. That the default was purely unintentional. The Plaintiff has now tendered the requisite process fee stamps along with summons forms.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
Set aside the dismissal order dated [DATE] and restore O.S. No. [ ] of 202[ ] to file; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 49. TRIAL OF PRELIMINARY ISSUE (ORDER XIV RULE 2(2))
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="preliminary_issue_o14_r2",
        title="Application for Trial of Preliminary Issue on Law / Jurisdiction",
        provision="Order XIV Rule 2(2) CPC",
        category="Defense & Summary Proceedings",
        summary="Application by defendant praying the court to try issues of law relating to jurisdiction, limitation, or statutory bar as preliminary issues before embarking on full trial.",
        practice_notes="Order XIV Rule 2(2): Where issues both of law and of fact arise, and the court is of opinion that the case or any part thereof may be disposed of on an issue of law only relating to: (a) jurisdiction of the court; or (b) a statutory bar created by any law, the court may try that issue first.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XIV Rule 2", "title": "Court to pronounce judgment on all issues"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[DEFENDANT FULL NAME]                                              ... APPLICANT / DEFENDANT
VERSUS
[PLAINTIFF FULL NAME]                                              ... RESPONDENT / PLAINTIFF

APPLICATION UNDER ORDER XIV RULE 2(2) READ WITH SECTION 151 CPC

The Applicant / Defendant respectfully submits as under:

1. That this Hon'ble Court was pleased to frame issues in the above Suit on [DATE].

2. That Issue No. [ ] framed by this Hon'ble Court reads as under:
   "Whether the Suit is barred by limitation under Article 54 of the Limitation Act, 1963 / barred by Section 11 CPC (Res Judicata)?"

3. That the said issue is a pure issue of law relating to a statutory bar created by law, which goes to the root of the jurisdiction of this Court to entertain the Suit.

4. That if the said preliminary issue of law is heard and decided first, it will dispose of the entire suit and spare both parties and the Court the protracted ordeal and enormous expenditure of examining dozens of witnesses.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
Try and decide Issue No. [ ] as a Preliminary Issue under Order XIV Rule 2(2) CPC before recording evidence on other issues; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 50. CORRECTION OF DECREE (SECTION 152)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="correction_decree_sec152",
        title="Application for Correction of Clerical / Arithmetical Errors in Decree",
        provision="Section 152 CPC",
        category="Post-Decree & Restoration Remedies",
        summary="Application under the 'slip rule' to correct accidental omissions, typographical errors, wrong survey numbers, or calculation errors in judgment or decree.",
        practice_notes="Section 152: Clerical or arithmetical mistakes in judgments, decrees or orders or errors arising therein from any accidental slip or omission may at any time be corrected by the Court either of its own motion or on the application of any of the parties. No limitation period applies.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 152", "title": "Amendment of judgments, decrees or orders"}
        ],
        template_text="""IN THE COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]
I.A. NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[DECREE HOLDER / PLAINTIFF NAME]                                   ... APPLICANT
VERSUS
[JUDGMENT DEBTOR / DEFENDANT NAME]                                 ... RESPONDENT

APPLICATION UNDER SECTION 152 READ WITH SECTION 151 CPC FOR AMENDMENT OF DECREE

The Applicant respectfully submits as under:

1. That this Hon'ble Court was pleased to decree the above Suit on [DATE].

2. ACCIDENTAL SLIP / CLERICAL ERROR:
That due to an inadvertent typographical error, in the Schedule of the Judgment and Decree, the Survey Number of the property has been typed as 'Sy. No. 44/2' instead of the true survey number 'Sy. No. 44/2B', and the boundary on the East is typed as 'Property of X' instead of 'Property of Y'.

3. That the correct survey number and boundaries are correctly reflected in the original registered title deed Exhibit P-1.

4. That the mistake is purely a clerical error arising from an accidental slip, which can be corrected at any time under Section 152 CPC without altering the substance of the judgment.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
Correct the clerical and typographical errors in the Judgment and Decree dated [DATE] by substituting 'Sy. No. 44/2B' in place of 'Sy. No. 44/2'; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 51. RESTITUTION (SECTION 144)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="restitution_sec144",
        title="Application for Restitution upon Reversal of Decree (Section 144 CPC)",
        provision="Section 144 CPC",
        category="Post-Decree & Restoration Remedies",
        summary="Application by successful appellant to restore possession of immovable property or refund of money taken under trial court decree which was reversed in appeal.",
        practice_notes="Section 144 embodies the cardinal maxim: 'Actus curiae neminem gravabit' (an act of the court shall prejudice no man). No separate suit lies for restitution (Section 144(2) express bar). Limitation under Article 136: 12 years.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 144", "title": "Application for restitution"}
        ],
        template_text="""IN THE COURT OF THE [TRIAL COURT NAME] AT [CITY]
MISC. APPLICATION NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[SUCCESSFUL APPELLANT / DEFENDANT NAME]                            ... APPLICANT
VERSUS
[ORIGINAL PLAINTIFF NAME]                                          ... RESPONDENT

APPLICATION UNDER SECTION 144 READ WITH SECTION 151 CPC FOR RESTITUTION

The Applicant respectfully submits as under:

1. That the Respondent instituted O.S. No. [ ] against the Applicant and obtained an ex-parte / trial court decree for possession / recovery of Rs. [AMOUNT] on [DATE].

2. EXECUTION UNDER ERRONEOUS DECREE:
That pending appeal, the Respondent executed the said decree in E.P. No. [ ] and forcibly took possession of the Schedule Property / attached and withdrew Rs. [AMOUNT] from the court on [DATE].

3. REVERSAL BY APPELLATE COURT:
That the Applicant preferred Regular First Appeal No. [ ] before the Hon'ble [APPELLATE COURT]. The Appellate Court vide Judgment and Decree dated [DATE] ALLOWED the appeal, set aside the trial court decree, and dismissed the suit with costs.

4. That upon reversal of the decree, the Applicant is entitled under Section 144 CPC to be restored to the exact position he would have occupied had the erroneous decree not been executed, along with restitution of possession, mesne profits, and interest.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court may be pleased to:
(a) Direct the Respondent to forthwith restore vacant physical possession of the Schedule Property to the Applicant;
(b) Direct refund of Rs. [AMOUNT] along with interest at 12% p.a. from the date of withdrawal till restitution; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT
"""
    ),

    # -------------------------------------------------------------------------
    # 52. REGULAR SECOND APPEAL (SECTION 100)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="regular_second_appeal_sec100",
        title="Memorandum of Regular Second Appeal (RSA) to High Court",
        provision="Section 100 CPC",
        category="Appeals & Revisions",
        summary="Second Appeal before the High Court challenging First Appellate Court decree on formulated Substantial Questions of Law.",
        practice_notes="Section 100(1): Second Appeal lies ONLY if the High Court is satisfied that the case involves a SUBSTANTIAL QUESTION OF LAW. Sir Chunilal Mehta v. Century Spg (Constitution Bench): Question must be debatable, not previously settled by Supreme Court, and materially affecting the rights of parties.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 100", "title": "Second appeal"},
            {"kind": "section", "ref": "Section 100A", "title": "No further appeal in certain cases"},
            {"kind": "section", "ref": "Section 102", "title": "No second appeal in certain suits (under Rs. 25,000)"}
        ],
        template_text="""IN THE HIGH COURT OF JUDICATURE AT [HIGH COURT LOCATION]
REGULAR SECOND APPEAL NO. _______ OF 202[ ]

[APPELLANT FULL NAME],
Residing at [ADDRESS]
(Original Defendant / Appellant in R.A. No. [   ])                 ... APPELLANT
VERSUS
[RESPONDENT FULL NAME],
Residing at [ADDRESS]
(Original Plaintiff / Respondent in R.A. No. [   ])                ... RESPONDENT

MEMORANDUM OF REGULAR SECOND APPEAL UNDER SECTION 100 OF THE CODE OF CIVIL PROCEDURE, 1908

The Appellant above named respectfully submits as under:

1. PARTICULARS OF DECREES:
This Second Appeal is preferred against the Judgment and Decree dated [DATE] passed by the learned [FIRST APPELLATE COURT] in Regular Appeal No. [ ], confirming / reversing the decree dated [DATE] passed by [TRIAL COURT] in O.S. No. [ ].

2. SUBSTANTIAL QUESTIONS OF LAW:
The following substantial questions of law arise for consideration in this Second Appeal:

   QUESTION NO. 1:
   Whether the Lower Appellate Court was justified in decreeing the suit for specific performance in the complete absence of any plea or proof of continuous readiness and willingness under Section 16(c) of the Specific Relief Act, 1963?

   QUESTION NO. 2:
   Whether the Lower Appellate Court committed a grave error of law in reversing the well-considered judgment of the Trial Court on limitation, without meeting the specific findings recorded by the Trial Court on Article 54?

   QUESTION NO. 3:
   Whether unregistered Agreement to Sell Exhibit P-1 could be admitted in evidence to prove possession in the teeth of Section 17(1A) of the Registration Act, 1908 and Section 53A of the Transfer of Property Act?

3. GROUNDS OF APPEAL:
(a) The judgment of the Lower Appellate Court is perverse and contrary to binding precedents of the Hon'ble Supreme Court.
(b) The Lower Appellate Court failed to exercise its jurisdiction as the final court of fact by ignoring the vital admissions of PW-1 in cross-examination.

PRAYER:
Wherefore, the Appellant prays that this Hon'ble Court may be pleased to:
(a) Admit this Second Appeal on the Substantial Questions of Law formulated above;
(b) Set aside the Judgment and Decree of the Lower Appellate Court;
(c) Grant ad-interim stay of execution pending appeal; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPELLANT
"""
    ),

    # -------------------------------------------------------------------------
    # 53. CIVIL REVISION PETITION (SECTION 115)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="civil_revision_sec115",
        title="Civil Revision Petition (CRP) under Section 115 CPC",
        provision="Section 115 CPC",
        category="Appeals & Revisions",
        summary="Revision petition to High Court challenging jurisdictional errors of subordinate courts where no appeal lies, satisfying the 1999 Proviso.",
        practice_notes="Section 115(1) Proviso: High Court shall not vary or reverse any order made in the course of a suit EXCEPT where the order, if it had been made in favour of the revision petitioner, would have FINALLY DISPOSED OF the suit or other proceedings. Limitation under Article 131: 90 DAYS.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 115", "title": "Revision"},
            {"kind": "limitation_article", "ref": "Article 131", "title": "To any court for the exercise of its powers of revision (90 days)"}
        ],
        template_text="""IN THE HIGH COURT OF JUDICATURE AT [HIGH COURT LOCATION]
CIVIL REVISION PETITION NO. _______ OF 202[ ]

[REVISION PETITIONER FULL NAME]                                    ... PETITIONER
VERSUS
[RESPONDENT FULL NAME]                                             ... RESPONDENT

CIVIL REVISION PETITION UNDER SECTION 115 OF THE CODE OF CIVIL PROCEDURE, 1908

The Petitioner above named respectfully submits as under:

1. PARTICULARS OF IMPUGNED ORDER:
This Civil Revision Petition is filed challenging the Order dated [DATE] passed by the learned [SUBORDINATE COURT] on I.A. No. [ ] in O.S. No. [ ], whereby the Trial Court illegally rejected the Petitioner's application under Order VII Rule 11 CPC.

2. SATISFACTION OF SECTION 115(1) PROVISO:
The present revision is strictly maintainable because if the application under Order VII Rule 11 had been allowed in favour of the Petitioner, the Suit would have been FINALLY DISPOSED OF and terminated.

3. JURISDICTIONAL ERRORS (SECTION 115 TESTS):
(a) EXERCISE OF JURISDICTION NOT VESTED: The Subordinate Court exercised jurisdiction not vested in it by entertaining a suit patently barred by limitation on the face of the plaint.
(b) FAILURE TO EXERCISE JURISDICTION: The Court failed to exercise jurisdiction vested in it by law under Order VII Rule 11(d) CPC.
(c) ILLEGALITY & MATERIAL IRREGULARITY: The Court acted in the exercise of its jurisdiction illegally and with material irregularity by considering defense pleas instead of restricting scrutiny to plaint averments.

PRAYER:
Wherefore, the Petitioner prays that this Hon'ble Court may be pleased to:
(a) Call for the records and set aside the impugned Order dated [DATE] passed on I.A. No. [ ];
(b) Reject the Plaint in O.S. No. [ ] under Order VII Rule 11 CPC;
(c) Stay all further proceedings in the suit pending this revision; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PETITIONER
"""
    ),

    # -------------------------------------------------------------------------
    # 54. ARTICLE 227 WRIT PETITION (SUPERVISORY JURISDICTION)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="writ_art227_supervisory",
        title="Writ Petition under Article 227 of the Constitution of India",
        provision="Article 227 of the Constitution of India",
        category="Appeals & Revisions",
        summary="High Court petition invoking supervisory jurisdiction over subordinate civil courts to correct grave patent injustice and breach of fundamental procedural principles where no statutory appeal or revision lies.",
        practice_notes="Radhey Shyam v. Chhabi Nath (2015) 5 SCC 423: Judicial orders of civil courts are NOT amenable to writ of certiorari under Article 226; remedy lies exclusively under Article 227. Jurisdiction is supervisory (not appellate), invoked to prevent manifest failure of justice or patent perversity.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 115", "title": "Revision"}
        ],
        template_text="""IN THE HIGH COURT OF JUDICATURE AT [HIGH COURT LOCATION]
WRIT PETITION (CIVIL) NO. _______ OF 202[ ]
(UNDER ARTICLE 227 OF THE CONSTITUTION OF INDIA)

IN THE MATTER OF:
[PETITIONER FULL NAME],
Residing at [ADDRESS]                                              ... PETITIONER
VERSUS
[RESPONDENT FULL NAME],
Residing at [ADDRESS]                                              ... RESPONDENT

WRIT PETITION UNDER ARTICLE 227 OF THE CONSTITUTION OF INDIA INVOKING SUPERVISORY JURISDICTION

The Petitioner above named respectfully submits as under:

1. PARTICULARS OF IMPUGNED ORDER:
This Writ Petition under Article 227 is preferred challenging the Order dated [DATE] passed by the learned [TRIAL COURT] on I.A. No. [ ] in O.S. No. [ ], arbitrarily rejecting the Petitioner's application for amendment of pleadings under Order VI Rule 17 CPC.

2. NON-AVAILABILITY OF ALTERNATIVE REMEDY:
No appeal or civil revision lies against the impugned interlocutory order under Section 104/Order XLIII Rule 1 CPC, nor does it satisfy the final disposal test under Section 115(1) Proviso. The Petitioner has no other efficacious alternative remedy except invoking the supervisory jurisdiction of this Hon'ble High Court under Article 227.

3. GROUNDS FOR SUPERVISORY INTERFERENCE:
(a) The Trial Court acted in patent violation of fundamental principles of law, causing grave dereliction of duty.
(b) The Trial Court completely misdirected itself by holding that pre-trial amendment requires proof of due diligence, overlooking that trial had not commenced.
(c) The refusal to allow amendment to correct an obvious typographical error in the suit schedule has resulted in gross miscarriage of justice.

PRAYER:
Wherefore, the Petitioner prays that this Hon'ble Court may be pleased to:
(a) Exercise its supervisory jurisdiction under Article 227 of the Constitution of India;
(b) Quash and set aside the impugned Order dated [DATE] passed on I.A. No. [ ] in O.S. No. [ ];
(c) Allow I.A. No. [ ] and permit the Petitioner to amend the pleadings;
(d) Stay all further trial court proceedings pending disposal of this petition; in the interest of justice.

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PETITIONER
"""
    )
]


def list_templates(category: Optional[str] = None) -> List[DraftingTemplate]:
    if category:
        return [t for t in TEMPLATES if t.category == category]
    return list(TEMPLATES)


def list_template_categories() -> List[str]:
    seen = []
    for t in TEMPLATES:
        if t.category not in seen:
            seen.append(t.category)
    return seen


def get_template(template_id: str) -> Optional[DraftingTemplate]:
    for t in TEMPLATES:
        if t.id == template_id:
            return t
    return None
