"""
Authoritative Court-Ready Drafting Templates & Form Library
for Code of Civil Procedure, 1908 & The Limitation Act, 1963.
Contains standard court-tested Indian legal drafts with bracketed placeholders,
practice guidance notes, statutory provisions, and verification clauses.
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
    connected_provisions: List[Dict[str, str]]


TEMPLATES: List[DraftingTemplate] = [
    # -------------------------------------------------------------------------
    # 1. CAVEAT PETITION (SECTION 148A)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="caveat_sec_148a",
        title="Caveat Petition with Verification Affidavit",
        provision="Section 148A CPC",
        category="Pre-Emptive & Protective Proceedings",
        summary="Statutory caveat petition to prevent adverse ex-parte interim orders or injunctions without prior notice and hearing.",
        practice_notes="Must be served on the expected applicant by Registered Post AD under Section 148A(2). Remains in force for exactly 90 days from the lodging date under Section 148A(5).",
        connected_provisions=[
            {"kind": "section", "ref": "Section 148A", "title": "Right to lodge a caveat"},
            {"kind": "rule", "ref": "Order XXXIX Rule 1", "title": "Cases in which temporary injunction may be granted"}
        ],
        template_text="""IN THE COURT OF THE [DESIGNATION OF JUDGE / COURT, e.g. PRINCIPAL SENIOR CIVIL JUDGE / DISTRICT JUDGE / HIGH COURT]
AT [CITY / PLACE, e.g. BANGALORE / CHENNAI / DELHI / MUMBAI]

CAVEAT PETITION NO. _______ OF 202[ ]

IN THE MATTER OF:

[NAME OF CAVEATOR],
Aged about [AGE] years,
S/o or D/o or W/o [PARENT / SPOUSE NAME],
Residing at [COMPLETE RESIDENTIAL ADDRESS],
[PHONE / EMAIL]
                                                              ... CAVEATOR / APPLICANT

                                   VERSUS

[NAME OF EXPECTED APPLICANT / OPPOSITE PARTY],
Aged about [AGE] years,
S/o or D/o or W/o [PARENT / SPOUSE NAME],
Residing at [COMPLETE RESIDENTIAL ADDRESS]
                                                              ... EXPECTED APPLICANT / OPPOSITE PARTY

----------------------------------------------------------------------------------
CAVEAT PETITION UNDER SECTION 148A OF THE CODE OF CIVIL PROCEDURE, 1908
----------------------------------------------------------------------------------

The Caveator above named most respectfully submits as follows:

1. The Caveator is the absolute owner and in lawful possession of the property described in the Schedule hereunder written (hereinafter referred to as the "Schedule Property") by virtue of [TITLE DEED / SALE DEED / PARTITION DEED / GIFT DEED] dated [DATE], registered as Document No. [DOC NO.] in the office of the Sub-Registrar, [PLACE].

2. The Expected Applicant / Opposite Party has no right, title, interest, or possession whatsoever in respect of the Schedule Property. However, the Expected Applicant has recently held out threats of dispossession and interference with the peaceful possession of the Caveator.

3. The Caveator reliably learns that the Expected Applicant is actively contemplating and preparing to institute a Civil Suit / Appeal / Miscellaneous Petition before this Hon'ble Court against the Caveator and to move an urgent ex-parte interlocutory application seeking ad-interim temporary injunction / stay / appointment of receiver in respect of the Schedule Property.

4. If any ex-parte interim order is passed by this Hon'ble Court without affording a fair opportunity of hearing to the Caveator, the Caveator will suffer irreparable loss, grave hardship, and serious injury which cannot be compensated in terms of money.

5. The Caveator has a substantial and legitimate right to appear and oppose any such suit, appeal, or application that may be filed by the Expected Applicant.

6. As mandated by Section 148A(2) of the Code of Civil Procedure, 1908, the Caveator has dispatched a true copy of this Caveat Petition to the Expected Applicant by Registered Post with Acknowledgement Due on [DATE OF POSTING]. The original postal receipt is annexed hereto as Annexure-A.

PRAYER

Wherefore, the Caveator most respectfully prays that this Hon'ble Court be pleased to:
(a) Lodge this Caveat under Section 148A of the Code of Civil Procedure, 1908;
(b) Direct that no ex-parte interim order, ad-interim temporary injunction, or direction be passed in any Suit, Appeal, or Application that may be instituted by the Expected Applicant against the Caveator in respect of the Schedule Property without prior due notice and opportunity of hearing to the Caveator or his Counsel;
(c) Pass such other or further order(s) as this Hon'ble Court may deem fit and proper in the circumstances of the case, and thus render justice.

SCHEDULE OF PROPERTY
[GIVE FULL DETAILED PROPERTY BOUNDARIES, SURVEY NO., CTS NO., MUNICIPAL DOOR NO., MEASUREMENTS]
East by   : [BOUNDARY]
West by   : [BOUNDARY]
North by  : [BOUNDARY]
South by  : [BOUNDARY]

Place: [CITY]
Date : [DATE]                                                    ADVOCATE FOR CAVEATOR

----------------------------------------------------------------------------------
VERIFICATION AFFIDAVIT
----------------------------------------------------------------------------------

I, [NAME OF CAVEATOR], S/o [FATHER'S NAME], aged about [AGE] years, residing at [ADDRESS], do hereby solemnly affirm and state on oath as follows:

1. I am the Caveator in the above petition and I am well conversant with the facts of the case and competent to swear to this affidavit.
2. I state that the statements made in paragraphs 1 to 6 of the accompanying Caveat Petition are true and correct to the best of my knowledge, belief, and records.
3. I state that I have served a notice of this caveat upon the Expected Applicant by Registered Post AD on [DATE].

DEPONENT

VERIFICATION:
Verified at [PLACE] on this [DAY] day of [MONTH], 202[ ] that the contents of my above affidavit are true and correct, no part of it is false and nothing material has been concealed therefrom.

DEPONENT
Sworn before me:
NOTARY PUBLIC / OATH COMMISSIONER"""
    ),

    # -------------------------------------------------------------------------
    # 2. TEMPORARY INJUNCTION APPLICATION (ORDER XXXIX RULES 1 & 2)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="injunction_o39_r1_2",
        title="Application for Temporary Injunction with Supporting Affidavit",
        provision="Order XXXIX Rules 1 & 2 CPC",
        category="Interlocutory Applications",
        summary="Standard application seeking ad-interim temporary injunction to restrain alienation, wastage, damage, or dispossession pending suit.",
        practice_notes="Must plead all three prongs: Prima Facie Case, Balance of Convenience, and Irreparable Injury. If ex-parte relief is granted, compliance with Rule 3 Proviso (dispatch on same day/next day and affidavit of compliance) is strictly mandatory.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXXIX Rule 1", "title": "Cases in which temporary injunction may be granted"},
            {"kind": "rule", "ref": "Order XXXIX Rule 2", "title": "Injunction to restrain repetition or continuance of breach"},
            {"kind": "rule", "ref": "Order XXXIX Rule 3", "title": "Before granting injunction, Court to direct notice to opposite party"},
            {"kind": "rule", "ref": "Order XXXIX Rule 3A", "title": "Court to dispose of application for injunction within thirty days"}
        ],
        template_text="""IN THE COURT OF THE [DESIGNATION OF JUDGE / COURT]
AT [CITY / PLACE]

ORIGINAL SUIT NO. _______ OF 202[ ]

[NAME OF PLAINTIFF]                                           ... PLAINTIFF / APPLICANT

                                   VERSUS

[NAME OF DEFENDANT]                                           ... DEFENDANT / RESPONDENT

----------------------------------------------------------------------------------
APPLICATION UNDER ORDER XXXIX RULES 1 & 2 READ WITH SECTION 151 OF CPC
----------------------------------------------------------------------------------

The Applicant / Plaintiff above named most respectfully submits as follows:

1. The Plaintiff has instituted the accompanying Suit for [RELIEF, e.g. Permanent Injunction / Declaration of Title and Injunction / Specific Performance of Agreement of Sale dated [DATE]] against the Defendant in respect of the Suit Schedule Property. The averments made in the Plaint may be read as part and parcel of this application to avoid repetition.

2. PRIMA FACIE CASE:
The Plaintiff is the lawful owner in peaceful physical possession of the Suit Schedule Property having acquired the same through [DETAILS OF TITLE DEED / REGISTERED DOCUMENT NO. DATED [DATE]]. The revenue records, mutation extracts, property tax receipts, and electricity bills stand in the name of the Plaintiff, demonstrating continuous possession. The Plaintiff has established a strong prima facie case with high probability of succeeding in the suit.

3. BALANCE OF CONVENIENCE:
The balance of convenience lies entirely in favour of the Plaintiff and against the Defendant. If the Defendant is restrained from altering the nature of the property, creating third-party encumbrances, or dispossessing the Plaintiff, no injury will be caused to the Defendant. On the other hand, if the injunction is refused, the Plaintiff will be subjected to immense hardship and multi-fold litigation.

4. IRREPARABLE INJURY:
On [DATE OF THREAT], the Defendant along with his henchmen came near the Suit Schedule Property and attempted to forcibly dispossess the Plaintiff and threatened to alienate / construct / demolish the structure. If the Defendant is not restrained by an immediate ad-interim temporary injunction, the Defendant will alter the status quo of the property, creating irreversible third-party interests, thereby defeating the very subject matter of the suit, causing irreparable injury to the Plaintiff that cannot be compensated by any amount of damages.

5. URGENCY / EX-PARTE REQUISITE (RULE 3 PROVISO):
The threat held out by the Defendant is imminent and real. If prior notice is issued to the Defendant, the Defendant will accelerate the illegal alienation / demolition / construction before the date of hearing, thereby rendering the relief infructuous and defeating the ends of justice.

PRAYER

Wherefore, the Applicant / Plaintiff prays that this Hon'ble Court be pleased to:
(a) Grant an ad-interim temporary injunction restraining the Defendant, his agents, servants, representatives, or anyone acting through or under him, from interfering with the Plaintiff's peaceful possession and enjoyment of the Suit Schedule Property, pending disposal of the suit;
(b) Restrain the Defendant from creating any third-party encumbrance, mortgage, lease, sale, or altering the nature of the Suit Schedule Property, pending disposal of the suit;
(c) Pass such other and further orders as this Hon'ble Court deems fit in the interests of justice and equity.

SUIT SCHEDULE PROPERTY
[INSERT COMPLETE BOUNDARIES AND DESCRIPTION]

Place: [CITY]
Date : [DATE]                                                    ADVOCATE FOR PLAINTIFF

----------------------------------------------------------------------------------
SUPPORTING AFFIDAVIT
----------------------------------------------------------------------------------

I, [PLAINTIFF NAME], S/o [FATHER'S NAME], aged about [AGE] years, residing at [ADDRESS], do hereby solemnly affirm and state on oath as follows:

1. I am the Plaintiff / Applicant in the above matter and am well conversant with the facts of the case.
2. I state that the facts narrated in paragraphs 1 to 5 of the accompanying Interlocutory Application are true and correct to my knowledge and belief.
3. I state that I have a prima facie case, the balance of convenience is in my favour, and I will suffer irreparable injury if the temporary injunction is not granted.

DEPONENT

VERIFICATION:
Verified at [PLACE] on this [DAY] day of [MONTH], 202[ ] that the contents of my above affidavit are true and correct.

DEPONENT
Sworn before me:
NOTARY PUBLIC / OATH COMMISSIONER"""
    ),

    # -------------------------------------------------------------------------
    # 3. SETTING ASIDE EX-PARTE DECREE (ORDER IX RULE 13 + SEC 5 LIMITATION)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="exparte_o9_r13",
        title="Application to Set Aside Ex-Parte Decree with Condonation of Delay",
        provision="Order IX Rule 13 CPC r/w Article 123 & Section 5 Limitation Act",
        category="Post-Decree & Restoration Remedies",
        summary="Composite application to set aside an ex-parte decree on grounds of non-service of summons or sufficient cause for non-appearance, with condonation of delay.",
        practice_notes="Limitation is 30 days under Article 123 of the Limitation Act. If summons was not duly served, limitation runs from the date of knowledge of the decree. If beyond 30 days, a Section 5 condonation application explaining each day's delay must accompany.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order IX Rule 13", "title": "Setting aside decree ex parte against defendant"},
            {"kind": "limitation_article", "ref": "Article 123", "title": "To set aside a decree passed ex parte (30 days)"},
            {"kind": "limitation_section", "ref": "Section 5", "title": "Extension of prescribed period (Condonation of delay)"}
        ],
        template_text="""IN THE COURT OF THE [DESIGNATION OF JUDGE / COURT]
AT [CITY / PLACE]

ORIGINAL SUIT NO. _______ OF 202[ ]
(MISCELLANEOUS APPLICATION NO. _______ OF 202[ ])

[NAME OF DEFENDANT / APPLICANT]                               ... DEFENDANT / APPLICANT

                                   VERSUS

[NAME OF PLAINTIFF / RESPONDENT]                              ... PLAINTIFF / RESPONDENT

----------------------------------------------------------------------------------
APPLICATION UNDER ORDER IX RULE 13 READ WITH SECTION 151 OF CPC
TO SET ASIDE EX-PARTE DECREE DATED [DATE OF DECREE]
----------------------------------------------------------------------------------

The Applicant / Defendant above named most respectfully submits as follows:

1. The Respondent / Plaintiff instituted the above Suit for [NATURE OF SUIT] against the Applicant. This Hon'ble Court was pleased to pass an ex-parte judgment and decree dated [DATE OF DECREE] in the above suit.

2. GROUND OF NON-SERVICE / SUFFICIENT CAUSE:
The Applicant submits that summons in the above suit was never duly served upon the Applicant. The process server's report alleging service / refusal is false and manipulated. The Applicant never resided at the address where summons was purportedly delivered, having shifted residence to [NEW ADDRESS] since [DATE].
[OR ALTERNATIVELY: The summons was served, but the Applicant was prevented by sufficient cause from appearing when the suit was called on for hearing on [DATE], because the Applicant was hospitalized / bedridden due to [MEDICAL CONDITION] from [DATE] to [DATE], as evidenced by the medical certificate annexed hereto as Annexure-B.]

3. DATE OF KNOWLEDGE:
The Applicant had no knowledge whatsoever regarding the institution of the suit or the passing of the ex-parte decree until [DATE OF KNOWLEDGE], when the Applicant received notice in Execution Petition No. [EP NO.] / when the bailiff visited the property. Immediately upon acquiring knowledge on [DATE], the Applicant applied for certified copies on [DATE] which were delivered on [DATE], and this application is presented without any delay thereafter.

4. MERITORIOUS DEFENCE:
The Applicant has a substantial and meritorious defence to the claim of the Plaintiff. The claim of the Plaintiff is false, frivolous, and barred by law. If the ex-parte decree is not set aside, the Applicant will suffer serious injustice without a trial on merits.

PRAYER

Wherefore, the Applicant prays that this Hon'ble Court be pleased to:
(a) Set aside the ex-parte judgment and decree dated [DATE] passed in O.S. No. [NO.] against the Applicant / Defendant;
(b) Restore Original Suit No. [NO.] to its original file and afford the Applicant an opportunity to file Written Statement and contest the suit on merits;
(c) Stay all further execution proceedings in E.P. No. [EP NO.] pending disposal of this application.

Place: [CITY]
Date : [DATE]                                                    ADVOCATE FOR APPLICANT

----------------------------------------------------------------------------------
APPLICATION UNDER SECTION 5 OF THE LIMITATION ACT, 1963
FOR CONDONATION OF DELAY IN FILING APPLICATION UNDER ORDER IX RULE 13
----------------------------------------------------------------------------------

The Applicant respectfully submits as follows:

1. The Applicant has filed the accompanying application under Order IX Rule 13 of the Code of Civil Procedure to set aside the ex-parte decree dated [DATE].
2. As stated in the accompanying application, the Applicant acquired knowledge of the decree only on [DATE OF KNOWLEDGE]. If limitation is computed from the date of the decree, there is a delay of [NUMBER] days.
3. The delay in filing the application was neither intentional nor deliberate, but occasioned by the bona fide reasons set forth above. The Applicant was completely unaware of the proceedings.
4. The cause of justice will be advanced if the delay is condoned and the suit is heard on merits.

PRAYER:
Wherefore, the Applicant prays that this Hon'ble Court be pleased to condone the delay of [NUMBER] days in filing the application under Order IX Rule 13 CPC, in the interests of justice.

ADVOCATE FOR APPLICANT

[ANNEX VERIFICATION AFFIDAVIT SWORN BY APPLICANT]"""
    ),

    # -------------------------------------------------------------------------
    # 4. TABULAR EXECUTION PETITION (ORDER XXI RULE 11(2))
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="execution_o21_tabular",
        title="Tabular Execution Petition (Mandatory 10-Column Format)",
        provision="Order XXI Rule 11(2) CPC",
        category="Execution Proceedings",
        summary="The mandatory statutory 10-column execution petition format required by every executing court in India to enforce money, property, or injunction decrees.",
        practice_notes="Must be in tabular form containing all 10 columns prescribed under Order XXI Rule 11(2). Accompanied by a certified copy of the decree under Rule 11(3). If filed after 2 years from decree date, notice under Rule 22 is mandatory.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 38", "title": "Court by which decree may be executed"},
            {"kind": "rule", "ref": "Order XXI Rule 11", "title": "Oral application and written application"},
            {"kind": "rule", "ref": "Order XXI Rule 22", "title": "Notice to show cause against execution in certain cases"},
            {"kind": "limitation_article", "ref": "Article 136", "title": "Execution of decree (12 years)"}
        ],
        template_text="""IN THE COURT OF THE [DESIGNATION OF EXECUTING COURT]
AT [CITY / PLACE]

EXECUTION PETITION NO. _______ OF 202[ ]
IN
ORIGINAL SUIT NO. _______ OF 202[ ]

[NAME OF DECREE HOLDER],
S/o [FATHER'S NAME],
Residing at [ADDRESS]                                         ... DECREE HOLDER

                                   VERSUS

[NAME OF JUDGMENT DEBTOR],
S/o [FATHER'S NAME],
Residing at [ADDRESS]                                         ... JUDGMENT DEBTOR

----------------------------------------------------------------------------------
EXECUTION PETITION UNDER ORDER XXI RULE 11(2) OF THE CODE OF CIVIL PROCEDURE, 1908
----------------------------------------------------------------------------------

The Decree Holder named above states as follows:

==================================================================================
COLUMN NO. | STATUTORY PARTICULARS REQUIRED                | PARTICULARS IN THIS CASE
==================================================================================
1.         | Number of Suit                                | O.S. No. [SUIT NO.] of 202[ ]
-----------+-----------------------------------------------+----------------------
2.         | Names of Parties                              | [PLAINTIFF NAME] vs [DEFENDANT NAME]
-----------+-----------------------------------------------+----------------------
3.         | Date of Decree                                | [DATE OF DECREE]
-----------+-----------------------------------------------+----------------------
4.         | Whether any Appeal has been preferred         | No Appeal preferred / [Appeal preferred and dismissed on [DATE]]
-----------+-----------------------------------------------+----------------------
5.         | Whether any payment or adjustment made        | Nil / Rs. [AMOUNT] paid on [DATE]
-----------+-----------------------------------------------+----------------------
6.         | Previous application, if any, with date/result| Nil / E.P. No. [ ] dismissed on [DATE]
-----------+-----------------------------------------------+----------------------
7.         | Amount with interest due upon the decree or   | Principal Sum: Rs. [AMOUNT]
           | other relief granted, together with interest  | Interest at [RATE]% p.a. from [DATE]
           | cross-decrees, if any                         | to [DATE]: Rs. [INTEREST AMOUNT]
           |                                               | Total Claim: Rs. [TOTAL]
-----------+-----------------------------------------------+----------------------
8.         | Amount of costs, if any, awarded              | Rs. [COSTS AWARDED AS PER DECREE]
-----------+-----------------------------------------------+----------------------
9.         | Against whom execution is sought              | Against the Judgment Debtor named above
-----------+-----------------------------------------------+----------------------
10.        | Mode in which assistance of Court is required | (a) By attachment and sale of movable /
           |                                               | immovable property of Judgment Debtor
           |                                               | described in Schedule 'A' below;
           |                                               | (b) By arrest and detention of Judgment
           |                                               | Debtor in civil prison;
           |                                               | (c) By delivery of possession of Schedule 'B' property.
==================================================================================

SCHEDULE 'A' — PROPERTY TO BE ATTACHED
[INSERT FULL DESCRIPTION OF BANK ACCOUNTS, VEHICLES, OR IMMOVABLE ASSETS]

PRAYER:
The Decree Holder prays that this Hon'ble Court may be pleased to issue warrant of attachment / arrest / possession in terms of Column 10 above and execute the decree with costs.

Place: [CITY]
Date : [DATE]                                                    ADVOCATE FOR DECREE HOLDER

----------------------------------------------------------------------------------
VERIFICATION
----------------------------------------------------------------------------------
I, [NAME OF DECREE HOLDER], the Decree Holder above named, do hereby verify and declare that the contents of Columns 1 to 10 above are true to the best of my knowledge, information, and belief.

DECREE HOLDER"""
    ),

    # -------------------------------------------------------------------------
    # 5. LEGAL REPRESENTATIVE SUBSTITUTION (ORDER XXII RULE 3/4)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="lr_substitution_o22",
        title="Application to Bring Legal Representatives on Record",
        provision="Order XXII Rule 3 / Rule 4 CPC r/w Article 120 Limitation Act",
        category="Parties & Succession",
        summary="Application to substitute legal heirs upon the death of a sole or co-party where the right to sue survives.",
        practice_notes="Limitation is 90 days from the date of death under Article 120. If filed after 90 days, add prayer to set aside abatement under Rule 9 (Article 121: 60 days). If beyond 150 days from death, an application under Section 5 Limitation Act is required.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 2(11)", "title": "Definition of Legal Representative"},
            {"kind": "rule", "ref": "Order XXII Rule 3", "title": "Procedure in case of death of one of several plaintiffs or of sole plaintiff"},
            {"kind": "rule", "ref": "Order XXII Rule 4", "title": "Procedure in case of death of one of several defendants or of sole defendant"},
            {"kind": "limitation_article", "ref": "Article 120", "title": "To have the legal representative of deceased plaintiff/defendant made a party (90 days)"}
        ],
        template_text="""IN THE COURT OF THE [DESIGNATION OF JUDGE / COURT]
AT [CITY / PLACE]

ORIGINAL SUIT NO. _______ OF 202[ ]

[NAME OF PLAINTIFF]                                           ... PLAINTIFF

                                   VERSUS

[NAME OF DEFENDANT]                                           ... DEFENDANT

----------------------------------------------------------------------------------
APPLICATION UNDER ORDER XXII RULE 4 READ WITH SECTION 151 OF CPC
TO BRING LEGAL REPRESENTATIVES OF DECEASED DEFENDANT ON RECORD
----------------------------------------------------------------------------------

The Plaintiff above named most respectfully submits as follows:

1. The Plaintiff has instituted the above suit for [RELIEF, e.g. partition / specific performance / recovery of money] against the Defendant.

2. The sole Defendant / Defendant No. [NO.], namely [NAME OF DECEASED], passed away on [DATE OF DEATH] at [PLACE OF DEATH]. The certified copy of the Death Certificate issued by the competent authority is produced herewith as Annexure-A.

3. The right to sue survives against the legal representatives of the deceased Defendant in respect of the Suit Schedule Property / cause of action.

4. The deceased Defendant has left behind the following persons as his only surviving legal heirs and representatives:
   (a) [NAME OF HEIR 1], Aged [AGE] years, [RELATIONSHIP, e.g. Wife / Son / Daughter], Residing at [ADDRESS]
   (b) [NAME OF HEIR 2], Aged [AGE] years, [RELATIONSHIP], Residing at [ADDRESS]
   (c) [NAME OF HEIR 3], Aged [AGE] years, [RELATIONSHIP], Residing at [ADDRESS]

5. The aforesaid persons are the sole legal heirs who have succeeded to the estate of the deceased Defendant and are necessary and proper parties to the present suit.

6. This application is filed within the prescribed statutory period of 90 days from the date of death as per Article 120 of the Limitation Act, 1963.

PRAYER:
Wherefore, the Plaintiff prays that this Hon'ble Court be pleased to permit the Plaintiff to bring the legal representatives of the deceased Defendant (as detailed in paragraph 4 above) on record as Defendants No. 1(a), 1(b), and 1(c) respectively, in the interests of justice.

Place: [CITY]
Date : [DATE]                                                    ADVOCATE FOR PLAINTIFF

[ANNEX VERIFICATION AFFIDAVIT SWORN BY PLAINTIFF]"""
    ),

    # -------------------------------------------------------------------------
    # 6. STATUTORY PRE-SUIT NOTICE (SECTION 80)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="notice_sec_80",
        title="Statutory Pre-Suit Notice to Government / Public Officer",
        provision="Section 80 CPC",
        category="Statutory Notices",
        summary="Formal statutory legal notice delivered to the Government or public officer 2 complete months prior to instituting a civil suit.",
        practice_notes="Must state the cause of action, name/description/residence of plaintiff, and the relief claimed. Count 2 complete calendar months from the date of physical receipt/delivery before presenting the plaint.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 80", "title": "Notice against Government / Public Officers"},
            {"kind": "rule", "ref": "Order VII Rule 11(d)", "title": "Rejection of plaint where suit barred by any law"}
        ],
        template_text="""REGISTERED POST WITH ACKNOWLEDGEMENT DUE

Date: [DATE OF NOTICE]

TO:
1. THE SECRETARY TO GOVERNMENT OF [STATE / INDIA],
   DEPARTMENT OF [REVENUE / URBAN DEVELOPMENT / PUBLIC WORKS],
   [ADDRESS OF SECRETARIAT / MINISTRY]

2. THE DISTRICT COLLECTOR / DEPUTY COMMISSIONER,
   DISTRICT OF [NAME OF DISTRICT],
   OFFICE OF THE COLLECTORATE, [CITY / PLACE]

----------------------------------------------------------------------------------
STATUTORY NOTICE UNDER SECTION 80 OF THE CODE OF CIVIL PROCEDURE, 1908
----------------------------------------------------------------------------------

Sir / Madam,

Under instructions from and on behalf of my client, [NAME OF CLIENT / INTENDING PLAINTIFF], S/o [FATHER'S NAME], aged about [AGE] years, residing at [FULL ADDRESS] (hereinafter referred to as "my Client"), I hereby serve upon you this Statutory Notice under Section 80 of the Code of Civil Procedure, 1908:

1. CAUSE OF ACTION:
My Client is the absolute owner and in lawful possession of land measuring [AREA] in Survey No. [SURVEY NO.], situated at [VILLAGE / TALUK / DISTRICT], having acquired the same by virtue of [TITLE DEED DETAILS] dated [DATE].
On [DATE OF ACTION / INTERFERENCE], officials subordinate to you from the Department of [DEPARTMENT], without any authority of law, notice, or acquisition proceedings, wrongfully entered upon my Client's property and attempted to [DETAILS OF WRONGFUL ACTION, e.g. demolish boundary wall / dispossess my client / claim government ownership].
The cause of action arose on [DATE] when the wrongful interference was attempted within the jurisdiction of the Civil Court at [PLACE].

2. IDENTITY OF INTENDING PLAINTIFF:
Name       : [FULL NAME OF CLIENT]
Father's   : [FATHER'S NAME]
Residence  : [COMPLETE POSTAL ADDRESS]
Occupation : [OCCUPATION]

3. RELIEF CLAIMED:
My Client intends to institute a Civil Suit before the competent Civil Court at [PLACE] for:
(a) A decree of Declaration declaring that my Client is the absolute owner of the property described in the Schedule below;
(b) A decree of Permanent Injunction restraining the State Government and its officers, subordinates, and agents from in any manner interfering with my Client's peaceful possession or demolishing any structure thereon;
(c) Damages for wrongful trespass and costs.

YOU ARE HEREBY CALLED UPON to take note of the above claim and redress the grievance of my Client within two months from the date of receipt of this notice, failing which my Client shall institute the suit in the competent Civil Court on the expiry of two months, holding the Government and officers liable for all costs and consequences thereof.

SCHEDULE OF PROPERTY
[GIVE FULL BOUNDARIES AND MEASUREMENTS]

Yours faithfully,

[NAME OF ADVOCATE]
Advocate, Enrolment No. [ENROLMENT NO.]
Chamber Address: [CHAMBER ADDRESS]
Phone: [PHONE] | Email: [EMAIL]"""
    ),

    # -------------------------------------------------------------------------
    # 7. PLAINT GENERAL SKELETON (ORDER VII)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="plaint_skeleton_o7",
        title="Plaint General Skeleton with Verification & Statement of Truth",
        provision="Order VII Rule 1 CPC",
        category="Core Pleadings",
        summary="Standard civil plaint format compliant with Order VII Rule 1 including cause of action, jurisdiction, valuation, and verification.",
        practice_notes="Must state date when cause of action arose (Rule 1(e)), valuation for jurisdiction and court fee (Rule 1(i)), and be filed in duplicate (Order IV Rule 1).",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"},
            {"kind": "rule", "ref": "Order VII Rule 11", "title": "Rejection of plaint"},
            {"kind": "rule", "ref": "Order VI Rule 15", "title": "Verification of pleadings"}
        ],
        template_text="""IN THE COURT OF THE [DESIGNATION OF JUDGE / COURT, e.g. SENIOR CIVIL JUDGE]
AT [CITY / DISTRICT]

ORIGINAL SUIT NO. _______ OF 202[ ]

[NAME OF PLAINTIFF],
Aged about [AGE] years,
S/o [FATHER'S NAME],
Residing at [COMPLETE ADDRESS]
                                                              ... PLAINTIFF
                                   VERSUS

[NAME OF DEFENDANT],
Aged about [AGE] years,
S/o [FATHER'S NAME],
Residing at [COMPLETE ADDRESS]
                                                              ... DEFENDANT

----------------------------------------------------------------------------------
PLAINT UNDER ORDER VII RULES 1 & 2 OF THE CODE OF CIVIL PROCEDURE, 1908
----------------------------------------------------------------------------------

The Plaintiff above named respectfully states as follows:

1. DESCRIPTION OF PARTIES:
The Plaintiff is an individual residing at the address stated above. The address for service of all notices and process on the Plaintiff is that of his counsel: [COUNSEL ADDRESS].
The Defendant is an individual residing at the address stated in the cause title, where process may be served.

2. FACTUAL BACKGROUND:
[Narrate chronological facts clearly in numbered paragraphs. State title, agreement, transaction, or events establishing plaintiff's right.]

3. BREACH / WRONGFUL ACT OF DEFENDANT:
[State the exact wrongful act, default, refusal, breach of contract, or interference committed by defendant.]

4. CAUSE OF ACTION:
The cause of action for the suit arose on [DATE] when [FIRST EVENT], and subsequently on [DATE] when [DEMAND NOTICE ISSUED / REFUSAL / TRESPASS ATTEMPTED], within the local limits of the jurisdiction of this Hon'ble Court. The suit is filed well within the statutory period of limitation under Article [ARTICLE NO.] of the Limitation Act, 1963.

5. JURISDICTION:
The Suit Schedule Property is situated at [PLACE] / The contract was executed and breached at [PLACE] / The Defendant resides and works for gain within the local territorial limits of this Hon'ble Court. This Court has territorial and pecuniary jurisdiction to try and determine the present suit.

6. VALUATION AND COURT FEES:
The suit is valued for the purpose of Court Fee and Jurisdiction at Rs. [VALUATION AMOUNT] under Section [SECTION NO.] of the [STATE] Court Fees and Suits Valuation Act. A court fee of Rs. [FEE AMOUNT] is paid herewith on the plaint.

PRAYER:
Wherefore, the Plaintiff prays for a judgment and decree against the Defendant:
(a) [SPECIFIC RELIEF 1, e.g. Declaring that plaintiff is absolute owner...];
(b) [SPECIFIC RELIEF 2, e.g. Granting permanent injunction restraining defendant...];
(c) Awarding costs of this suit;
(d) Granting such other relief as this Hon'ble Court deems fit in the circumstances.

SCHEDULE OF SUIT PROPERTY
[INSERT FULL PARTICULARS AND BOUNDARIES]

Place: [CITY]
Date : [DATE]                                                    ADVOCATE FOR PLAINTIFF

----------------------------------------------------------------------------------
VERIFICATION
----------------------------------------------------------------------------------
I, [PLAINTIFF NAME], the Plaintiff above named, do hereby verify that the contents of paragraphs 1 to [NUMBER] are true to my personal knowledge, and paragraphs [NUMBER] to [NUMBER] are based on legal advice received and believed by me to be true.
Verified at [PLACE] on this [DAY] day of [MONTH], 202[ ].

PLAINTIFF"""
    ),

    # -------------------------------------------------------------------------
    # 8. WRITTEN STATEMENT GENERAL SKELETON (ORDER VIII)
    # -------------------------------------------------------------------------
    DraftingTemplate(
        id="ws_skeleton_o8",
        title="Written Statement Skeleton with Preliminary Objections",
        provision="Order VIII Rule 1 CPC",
        category="Core Pleadings",
        summary="Standard Written Statement format with preliminary legal objections, para-wise specific denials, and verification.",
        practice_notes="Must be filed within 30 days from service of summons (extendable up to 90 days for reasons recorded). Every allegation of fact must be specifically denied under Rule 3 and Rule 5 — evasive denial is deemed to be an admission.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order VIII Rule 1", "title": "Written statement"},
            {"kind": "rule", "ref": "Order VIII Rule 3", "title": "Denial to be specific"},
            {"kind": "rule", "ref": "Order VIII Rule 5", "title": "Specific denial"}
        ],
        template_text="""IN THE COURT OF THE [DESIGNATION OF JUDGE / COURT]
AT [CITY / DISTRICT]

ORIGINAL SUIT NO. _______ OF 202[ ]

[NAME OF PLAINTIFF]                                           ... PLAINTIFF

                                   VERSUS

[NAME OF DEFENDANT]                                           ... DEFENDANT

----------------------------------------------------------------------------------
WRITTEN STATEMENT ON BEHALF OF THE DEFENDANT UNDER ORDER VIII RULE 1 OF CPC
----------------------------------------------------------------------------------

The Defendant above named respectfully submits as follows:

I. PRELIMINARY OBJECTIONS:

1. SUIT NOT MAINTAINABLE:
The suit filed by the Plaintiff is false, frivolous, vexatious, and an abuse of the process of this Hon'ble Court, and is liable to be dismissed in limine.

2. BARRED BY LIMITATION:
The suit is palpably barred by the law of limitation. The alleged cause of action arose on [DATE], whereas the suit has been instituted on [DATE], beyond the statutory period prescribed under Article [NO.] of the Limitation Act, 1963.

3. NO CAUSE OF ACTION (ORDER VII RULE 11(a)):
The plaint discloses no real or subsisting cause of action against the Defendant. The alleged cause of action is purely illusory and created by clever drafting.

4. UNDERVALUATION / INSUFFICIENT COURT FEE:
The suit has been deliberately undervalued. The true market value of the property exceeds Rs. [VALUE], and the Plaintiff has failed to pay the requisite ad-valorem court fee.

5. NON-JOINDER OF NECESSARY PARTIES:
The suit is bad for non-joinder of necessary parties, namely [NAMES OF NECESSARY PARTIES], without whose presence no effective decree can be passed.

II. PARA-WISE REPLY ON MERITS:

6. The averments made in paragraph 1 of the Plaint are matters of record / denied as false.
7. With reference to paragraph 2 of the Plaint, the allegations that [QUOTE ALLEGATION] are specifically denied. It is false to suggest that [STATE CONTRARY FACTS].
8. With reference to paragraph 3 of the Plaint, the Defendant denies that [SPECIFIC DENIAL COMPLIANT WITH ORDER VIII RULE 3 & 5].
9. The averments made in the paragraph relating to Cause of Action are wholly imaginary and manufactured. No cause of action ever accrued to the Plaintiff against this Defendant.

PRAYER:
Wherefore, the Defendant prays that this Hon'ble Court be pleased to dismiss the suit of the Plaintiff with exemplary costs under Section 35A of the Code of Civil Procedure, 1908, in the interests of justice.

Place: [CITY]
Date : [DATE]                                                    ADVOCATE FOR DEFENDANT

----------------------------------------------------------------------------------
VERIFICATION
----------------------------------------------------------------------------------
I, [DEFENDANT NAME], the Defendant above named, do hereby verify that the contents of paragraphs 1 to 5 of the Preliminary Objections and paragraphs 6 to [NO.] of the reply are true and correct to my personal knowledge and belief, and based on legal advice received.
Verified at [PLACE] on this [DAY] day of [MONTH], 202[ ].

DEFENDANT"""
    )
]


def list_templates(category: Optional[str] = None) -> List[DraftingTemplate]:
    if category:
        return [t for t in TEMPLATES if t.category == category]
    return list(TEMPLATES)


def get_template(template_id: str) -> Optional[DraftingTemplate]:
    for t in TEMPLATES:
        if t.id == template_id:
            return t
    return None


def list_template_categories() -> List[str]:
    cats = []
    for t in TEMPLATES:
        if t.category not in cats:
            cats.append(t.category)
    return cats
