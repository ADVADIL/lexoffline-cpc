"""
Authoritative Courtroom Practice Checklists & Statutory Compliance Tests
for Code of Civil Procedure, 1908 & The Limitation Act, 1963.
Deterministic reference data containing statutory grounds, settled judicial
principles (Supreme Court precedents), step-by-step procedural checklists,
and common pitfalls.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class ChecklistItem:
    id: str
    label: str
    description: str
    statutory_ref: str = ""
    is_mandatory: bool = True


@dataclass
class PracticeChecklist:
    id: str
    title: str
    provision: str
    category: str
    summary: str
    statutory_grounds: List[Dict[str, str]]
    judicial_principles: List[Dict[str, str]]
    steps: List[ChecklistItem]
    common_pitfalls: List[str]
    connected_provisions: List[Dict[str, str]]


PRACTICE_CHECKLISTS: List[PracticeChecklist] = [
    # -------------------------------------------------------------------------
    # 1. ORDER VII RULE 11 — REJECTION OF PLAINT
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="o7_r11",
        title="Rejection of Plaint (Threshold Dismissal)",
        provision="Order VII Rule 11 CPC",
        category="Trial Court Practice & Pleadings",
        summary="A summary remedy terminating the suit at the threshold before trial where the plaint suffers from incurable legal defects specified in clauses (a) to (f).",
        statutory_grounds=[
            {
                "clause": "Rule 11(a)",
                "ground": "Non-disclosure of cause of action",
                "detail": "Plaint fails to disclose bundle of essential facts which, if proved, entitle plaintiff to relief. Illusory cause of action created by clever drafting must be rejected."
            },
            {
                "clause": "Rule 11(b)",
                "ground": "Undervaluation of relief",
                "detail": "Relief claimed is undervalued and plaintiff, on being required by the Court to correct the valuation within a time to be fixed by the Court, fails to do so."
            },
            {
                "clause": "Rule 11(c)",
                "ground": "Insufficiently stamped plaint",
                "detail": "Plaint is written upon paper insufficiently stamped and plaintiff, on being required by Court to supply requisite stamp-paper within a fixed time, fails to do so."
            },
            {
                "clause": "Rule 11(d)",
                "ground": "Suit barred by any law",
                "detail": "Where suit appears from the statement in the plaint to be barred by any law (e.g. Limitation Act, Section 9 CPC, Section 80 CPC, SARFAESI Act, Specific Relief Act)."
            },
            {
                "clause": "Rule 11(e)",
                "ground": "Not filed in duplicate",
                "detail": "Plaint is not filed in duplicate as mandated by Order IV Rule 1(1) CPC."
            },
            {
                "clause": "Rule 11(f)",
                "ground": "Non-compliance with Rule 9",
                "detail": "Plaintiff fails to comply with the provisions of Order VII Rule 9 regarding process fee, copies, and summons delivery."
            }
        ],
        judicial_principles=[
            {
                "principle": "Plaint must be read as a whole",
                "citation": "Dahiben v. Arvindbhai Kalyanji Bhanusali (2020) 7 SCC 366",
                "detail": "The court must read the entire plaint meaningfully. Neither isolated sentences nor piecemeal reading can be adopted to find a cause of action or create a bar."
            },
            {
                "principle": "Only plaint averments and documents can be looked into",
                "citation": "Saleem Bhai v. State of Maharashtra (2003) 1 SCC 557",
                "detail": "Defence of the defendant in the Written Statement or application under O.7 R.11 cannot be considered. The averments in the plaint are assumed to be true at this stage."
            },
            {
                "principle": "No partial rejection of plaint",
                "citation": "Madhav Prasad Aggarwal v. Axis Bank Ltd. (2019) 7 SCC 158",
                "detail": "A plaint cannot be rejected in part. It must either be rejected as a whole or not at all against a particular set of defendants."
            },
            {
                "principle": "Bar of Limitation on face of plaint",
                "citation": "Raghwendra Sharan Singh v. Ram Prasanna Singh (2020) 16 SCC 601",
                "detail": "Where the suit is palpably barred by limitation from the admitted dates in the plaint itself, clever drafting or illusory cause of action will not save it."
            }
        ],
        steps=[
            ChecklistItem(
                id="o7_step1",
                label="Scrutinize Plaint Averments Exclusively",
                description="Verify that your challenge relies strictly on the statements in the plaint and accompanying documents produced by the plaintiff. Do NOT rely on defendant's documents.",
                statutory_ref="Order VII Rule 11",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o7_step2",
                label="Check Cause of Action Bundle",
                description="Examine if every element of the cause of action (right + infringement + date/place) is pleaded. Check if cause of action is purely speculative.",
                statutory_ref="Order VII Rule 11(a)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o7_step3",
                label="Compute Limitation from Admitted Starting Dates",
                description="Calculate statutory limitation using admitted dates of instrument, dispossession, demand, or decree. Check applicable Limitation Act Article.",
                statutory_ref="Order VII Rule 11(d) r/w Section 3 Limitation Act",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o7_step4",
                label="Verify Statutory Pre-condition / Jurisdictional Bars",
                description="Check if statutory bars apply: Section 80 CPC (Govt notice), Section 9 (express/implied bar), Section 34 SARFAESI, Section 12A Commercial Courts Act.",
                statutory_ref="Order VII Rule 11(d)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o7_step5",
                label="Verify Valuation and Court Fee Adequacy",
                description="Ensure relief is correctly valued under the Court Fees Act and Suits Valuation Act. Court must give opportunity to correct before rejecting under (b) or (c).",
                statutory_ref="Order VII Rule 11(b), (c)",
                is_mandatory=False
            ),
            ChecklistItem(
                id="o7_step6",
                label="Stage of Application Check",
                description="An application under Order VII Rule 11 can be filed at ANY stage of the suit before conclusion of trial. Filing Written Statement is NOT a prerequisite.",
                statutory_ref="Order VII Rule 11",
                is_mandatory=False
            )
        ],
        common_pitfalls=[
            "Filing an application under O.7 R.11 relying on documents annexed to the Written Statement (fatal — court will dismiss the application).",
            "Seeking partial rejection of the plaint (e.g. rejecting Plaint regarding Property A while proceeding for Property B) — legally impermissible.",
            "Confusing disputed questions of limitation (where limitation is a mixed question of fact and law requiring evidence) with a patent bar apparent on the face of the plaint.",
            "Failing to challenge undervaluation before the framing of issues."
        ],
        connected_provisions=[
            {"kind": "section", "ref": "Section 9", "title": "Courts to try all civil suits unless barred"},
            {"kind": "section", "ref": "Section 80", "title": "Notice against Government / Public Officers"},
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"},
            {"kind": "rule", "ref": "Order VII Rule 13", "title": "Where rejection of plaint does not preclude presentation of fresh plaint"},
            {"kind": "limitation_section", "ref": "Section 3", "title": "Bar of limitation"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 2. ORDER XXXIX RULES 1 & 2 — TEMPORARY INJUNCTION
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="o39_r1_2",
        title="Temporary Injunction & Interlocutory Orders",
        provision="Order XXXIX Rules 1 & 2 CPC",
        category="Interlocutory & Emergency Remedies",
        summary="Equitable interim relief to preserve the status quo of property or restrain alienation, wastage, damage, or breach of contract pending final disposal of the suit.",
        statutory_grounds=[
            {
                "clause": "Rule 1(a)",
                "ground": "Property in danger of being wasted, damaged or alienated",
                "detail": "Any property in dispute in a suit is in danger of being wasted, damaged, or alienated by any party, or wrongfully sold in execution of a decree."
            },
            {
                "clause": "Rule 1(b)",
                "ground": "Threat to remove or dispose of property to defraud creditors",
                "detail": "Defendant threatens, or intends, to remove or dispose of his property with a view to defrauding his creditors."
            },
            {
                "clause": "Rule 1(c)",
                "ground": "Threat of dispossession or injury to plaintiff in relation to property",
                "detail": "Defendant threatens to dispossess the plaintiff, or otherwise cause injury to the plaintiff in relation to any property in dispute."
            },
            {
                "clause": "Rule 2",
                "ground": "Injunction to restrain repetition or continuance of breach",
                "detail": "In any suit for restraining defendant from committing a breach of contract or other injury of any kind."
            }
        ],
        judicial_principles=[
            {
                "principle": "The Classic Three-Pronged Test (All 3 must co-exist)",
                "citation": "Dalpat Kumar v. Prahlad Singh (1992) 1 SCC 719",
                "detail": "Grant of injunction requires satisfaction of: (1) Prima facie case; (2) Balance of convenience; and (3) Irreparable injury that cannot be compensated in terms of money."
            },
            {
                "principle": "Prima facie case is not proof beyond doubt",
                "citation": "Gujarat Bottling Co. Ltd. v. Coca Cola Co. (1995) 5 SCC 545",
                "detail": "Plaintiff needs only to show a bona fide contention and serious question to be tried, with probability of being entitled to relief."
            },
            {
                "principle": "Mandatory compliance with Rule 3 Proviso for ex-parte orders",
                "citation": "Morgan Stanley Mutual Fund v. Kartick Das (1994) 4 SCC 225",
                "detail": "Ex-parte ad-interim injunction is an exception. Reasons must be recorded why delay would defeat justice. Statutory compliance with Rule 3 proviso is mandatory."
            },
            {
                "principle": "Endeavour to dispose of injunction application in 30 days",
                "citation": "Order XXXIX Rule 3A CPC",
                "detail": "Where an injunction has been granted without notice, the court shall make an endeavour to finally dispose of the application within 30 days."
            }
        ],
        steps=[
            ChecklistItem(
                id="o39_step1",
                label="Establish Prima Facie Title and Possession",
                description="Attach certified title documents, revenue records (khasra/khatauni/patta), electricity bills, tax receipts demonstrating lawful possession.",
                statutory_ref="Order XXXIX Rule 1",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o39_step2",
                label="Establish Balance of Convenience",
                description="Demonstrate that the comparative mischief/hardship to the plaintiff if injunction is refused is greater than the inconvenience to defendant if granted.",
                statutory_ref="Dalpat Kumar Test",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o39_step3",
                label="Establish Irreparable Injury",
                description="Plead facts showing monetary compensation will be completely inadequate (e.g. destruction of ancestral structure, cutting of trees, third-party alienation).",
                statutory_ref="Order XXXIX Rule 1",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o39_step4",
                label="Urgency Justification for Ex-Parte Relief (Rule 3)",
                description="State reasons why giving prior notice would defeat the very purpose of the injunction. Plead imminent threat of construction or alienation.",
                statutory_ref="Order XXXIX Rule 3 Proviso",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o39_step5",
                label="MANDATORY Rule 3 Proviso Post-Injunction Compliance",
                description="Immediately upon getting ex-parte injunction: (1) Deliver copies of application, plaint, affidavit, documents by registered post on same day or next day; (2) File affidavit of compliance in court on the same day or immediately next day.",
                statutory_ref="Order XXXIX Rule 3(a), (b)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o39_step6",
                label="Track 30-Day Disposal Window (Rule 3A)",
                description="Apply for early hearing and final disposal of application within 30 days. Prevent indefinite adjournments keeping ex-parte order pending.",
                statutory_ref="Order XXXIX Rule 3A",
                is_mandatory=False
            )
        ],
        common_pitfalls=[
            "Failing to file compliance affidavit under Order XXXIX Rule 3 proviso after obtaining ex-parte injunction — this entitles defendant to get the injunction vacated solely on this ground.",
            "Seeking an injunction against true owner by a person in permissive possession/licensee.",
            "Suppression of material facts in ex-parte application (under Rule 4 proviso, court shall vacate injunction if plaintiff knowingly made false or misleading statement).",
            "Failing to initiate Order XXXIX Rule 2A contempt proceedings promptly upon breach of injunction."
        ],
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXXIX Rule 2A", "title": "Consequences of disobedience or breach of injunction"},
            {"kind": "rule", "ref": "Order XXXIX Rule 3", "title": "Before granting injunction, Court to direct notice to opposite party"},
            {"kind": "rule", "ref": "Order XXXIX Rule 3A", "title": "Court to dispose of application for injunction within thirty days"},
            {"kind": "rule", "ref": "Order XXXIX Rule 4", "title": "Order for injunction may be discharged, varied or set aside"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 3. SECTION 80 — SUITS AGAINST GOVERNMENT OR PUBLIC OFFICERS
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="sec_80",
        title="Notice to Government / Public Officers",
        provision="Section 80 CPC",
        category="Pre-Suit Procedures & Statutory Bars",
        summary="Statutory condition precedent requiring 2 months' written notice before instituting any suit against the Government or a public officer for acts done in official capacity.",
        statutory_grounds=[
            {
                "clause": "Section 80(1)",
                "ground": "Mandatory 2 Months Pre-Suit Notice",
                "detail": "No suit shall be instituted until the expiration of two months next after notice in writing has been delivered to or left at the office of specified authorities."
            },
            {
                "clause": "Section 80(1)(a)",
                "ground": "Central Government Suits (other than Railways)",
                "detail": "Notice delivered to a Secretary to the Central Government."
            },
            {
                "clause": "Section 80(1)(b)",
                "ground": "State Government Suits",
                "detail": "Notice delivered to a Secretary to that Government or the Collector of the District."
            },
            {
                "clause": "Section 80(2)",
                "ground": "Urgent or Immediate Relief Exception",
                "detail": "Suit for urgent/immediate relief may be instituted with leave of the Court without serving two months notice. But no interim relief can be granted without hearing the Govt."
            }
        ],
        judicial_principles=[
            {
                "principle": "Notice requirement is express, mandatory, and strict",
                "citation": "Bihari Chowdhary v. State of Bihar (1984) 2 SCC 627",
                "detail": "Section 80(1) is mandatory and admits of no exception. A suit instituted before expiry of 2 months is incompetent and must be rejected under Order VII Rule 11(d)."
            },
            {
                "principle": "Substantial compliance with contents of notice is sufficient",
                "citation": "State of Punjab v. Geeta Iron & Brass Works (1978) 1 SCC 68",
                "detail": "Notice is not an empty formality, but hyper-technical construction should be avoided if cause of action, identity of plaintiff, and relief are clearly indicated."
            },
            {
                "principle": "Leave under Section 80(2) must be explicitly prayed and granted",
                "citation": "State of A.P. v. Pioneer Builders (2006) 12 SCC 119",
                "detail": "Leave under Section 80(2) is not an empty ritual. The court must be satisfied of real urgency. If court finds no urgency, it must return the plaint for compliance."
            }
        ],
        steps=[
            ChecklistItem(
                id="s80_step1",
                label="Verify Correct Authority for Service",
                description="Central Govt: Secretary to Govt. Railways: General Manager. State Govt: Secretary to State Govt or District Collector. Public Officer: directly to officer.",
                statutory_ref="Section 80(1)(a), (b), (c)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s80_step2",
                label="Include the Three Statutory Essentials in Notice",
                description="Must state: (1) Cause of action; (2) Name, description and place of residence of the plaintiff; (3) Relief claimed.",
                statutory_ref="Section 80(1)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s80_step3",
                label="Calculate Two Complete Calendar Months from Delivery",
                description="Do not calculate from date of posting. Count 2 complete calendar months from the date of physical receipt/delivery acknowledged by the authority.",
                statutory_ref="Section 80(1)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s80_step4",
                label="Averment in Plaint Confirming Notice",
                description="Plaint must contain an explicit statement that such notice was delivered, stating the date, and that two months have expired.",
                statutory_ref="Section 80(1)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s80_step5",
                label="If Urgent: File Section 80(2) Leave Application",
                description="Where urgent relief is needed (e.g. demolition, eviction, auction within 2 weeks): File application u/s 80(2) with affidavit stating specific urgency reasons.",
                statutory_ref="Section 80(2)",
                is_mandatory=False
            ),
            ChecklistItem(
                id="s80_step6",
                label="Notice Opportunity Before Interim Relief",
                description="Under Sec 80(2) proviso, court CANNOT grant ex-parte interim injunction without giving reasonable opportunity to Govt to show cause.",
                statutory_ref="Section 80(2) Proviso",
                is_mandatory=True
            )
        ],
        common_pitfalls=[
            "Filing suit on the 60th day thinking the requirement is '60 days' — the statute says 'two months', which means two full calendar months from date of delivery.",
            "Mismatch between the relief claimed in Section 80 notice and the relief claimed in the plaint.",
            "Serving notice only on a subordinate local officer (e.g. Tehsildar or Junior Engineer) instead of the District Collector or Secretary to Government.",
            "Assuming ex-parte ad-interim injunction can be obtained against Government under Section 80(2) — proviso strictly bars interim relief without hearing the Govt."
        ],
        connected_provisions=[
            {"kind": "section", "ref": "Section 79", "title": "Suits by or against Government"},
            {"kind": "rule", "ref": "Order XXVII Rule 1", "title": "Suits by or against Government or Public Officers"},
            {"kind": "rule", "ref": "Order VII Rule 11(d)", "title": "Rejection of plaint where suit barred by any law"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 4. ORDER XXII — DEATH, ABATEMENT & SUBSTITUTION OF LRS
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="o22_lrs",
        title="Death of Parties, Abatement & LR Substitution",
        provision="Order XXII CPC r/w Articles 120–121 Limitation Act",
        category="Parties & Trial Proceedings",
        summary="Procedural roadmap when a plaintiff or defendant dies pending suit: survival of right to sue, 90-day limitation for substitution, automatic abatement, and setting aside abatement.",
        statutory_grounds=[
            {
                "clause": "Order XXII Rule 1",
                "ground": "Survival of Right to Sue",
                "detail": "Death of a plaintiff or defendant shall not cause the suit to abate if the right to sue survives."
            },
            {
                "clause": "Order XXII Rule 3 / Rule 4",
                "ground": "Application to Substitute Legal Representatives",
                "detail": "Where sole plaintiff/defendant dies, court on application made in that behalf shall cause legal representative to be made a party."
            },
            {
                "clause": "Article 120 Limitation Act",
                "ground": "90-Day Limitation for Substitution",
                "detail": "Application to have the legal representative of a deceased plaintiff or defendant made a party must be made within 90 days from date of death."
            },
            {
                "clause": "Article 121 Limitation Act",
                "ground": "60-Day Limitation to Set Aside Abatement",
                "detail": "Application under Order XXII Rule 9 to set aside an abatement must be made within 60 days from the date of abatement (i.e. between 90 and 150 days of death)."
            }
        ],
        judicial_principles=[
            {
                "principle": "Abatement is automatic by operation of law",
                "citation": "Madan Naik v. Hansubala Devi (1983) 3 SCC 15",
                "detail": "Abatement does not depend on an order of the court. Upon expiry of 90 days from the death without an application, the suit abates automatically."
            },
            {
                "principle": "Liberal approach in setting aside abatement",
                "citation": "Perumon Bhagvathy Devaswom v. Bhargavi Amma (2008) 8 SCC 321",
                "detail": "Courts adopt a liberal approach on condonation of delay in bringing LRs on record, as refusal to condone terminates litigation without adjudication on merits."
            },
            {
                "principle": "Decree against dead person is a nullity",
                "citation": "Amba Bai v. Gopal (2001) 5 SCC 570",
                "detail": "A decree passed against a defendant who was dead at the time of the decree (and whose legal representatives were not brought on record) is a complete nullity."
            }
        ],
        steps=[
            ChecklistItem(
                id="o22_step1",
                label="Check Survival of Right to Sue",
                description="Determine whether the cause of action is purely personal (actio personalis moritur cum persona, e.g. defamation, personal damages) or survives against estate (property, contract, partition).",
                statutory_ref="Order XXII Rule 1",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o22_step2",
                label="Calculate 90 Days from Date of Death",
                description="Ascertain the exact date of death (death certificate). Compute 90 calendar days under Article 120 of Limitation Act.",
                statutory_ref="Article 120 Limitation Act",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o22_step3",
                label="Identify and Array All Legal Representatives",
                description="Obtain legal heirship certificate or family tree. State names, ages, relationship, and complete addresses of all legal heirs in the application.",
                statutory_ref="Section 2(11) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o22_step4",
                label="If 90 Days Expired but within 150 Days: File Setting Aside Application",
                description="Suit has abated. File composite application: (1) Setting aside abatement under O.22 R.9; (2) Substitution of LRs under O.22 R.4.",
                statutory_ref="Order XXII Rule 9 r/w Article 121",
                is_mandatory=False
            ),
            ChecklistItem(
                id="o22_step5",
                label="If Beyond 150 Days: File Section 5 Condonation with Affidavit",
                description="File three-fold application: (1) Condonation of delay u/s 5 Limitation Act explaining each day of delay; (2) Setting aside abatement u/O.22 R.9; (3) Substitution u/O.22 R.4.",
                statutory_ref="Section 5 Limitation Act",
                is_mandatory=False
            ),
            ChecklistItem(
                id="o22_step6",
                label="Advocate's Duty Under Rule 10A",
                description="Advocate appearing for a party who dies must immediately inform the court of the death. Court gives notice to the other side.",
                statutory_ref="Order XXII Rule 10A",
                is_mandatory=True
            )
        ],
        common_pitfalls=[
            "Filing only an LR substitution application after 90 days without praying for setting aside of abatement (abatement is automatic; without setting it aside, LR application is non-maintainable).",
            "Calculating limitation from the date the opposite side gained knowledge of death rather than date of death (limitation runs strictly from date of death, though lack of knowledge is sufficient cause under Section 5).",
            "Proceeding with arguments and obtaining judgment when one defendant had died months earlier (the judgment is a nullity and unenforceable).",
            "Failing to substitute legal heirs in an appeal (provisions of Order XXII apply equally to appeals under Rule 11)."
        ],
        connected_provisions=[
            {"kind": "section", "ref": "Section 2(11)", "title": "Definition of Legal Representative"},
            {"kind": "rule", "ref": "Order XXII Rule 9", "title": "Effect of abatement or dismissal"},
            {"kind": "rule", "ref": "Order XXII Rule 10A", "title": "Duty of pleader to communicate to Court death of a party"},
            {"kind": "rule", "ref": "Order XXII Rule 11", "title": "Application of Order XXII to appeals"},
            {"kind": "limitation_article", "ref": "Article 120", "title": "To have the legal representative of deceased plaintiff/defendant made a party (90 days)"},
            {"kind": "limitation_article", "ref": "Article 121", "title": "To set aside an abatement (60 days)"},
            {"kind": "limitation_section", "ref": "Section 5", "title": "Extension of prescribed period (Condonation of delay)"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 5. SECTION 148A — CAVEAT PRACTICE
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="sec_148a",
        title="Caveat Petition & Notice Protection",
        provision="Section 148A CPC",
        category="Pre-Emptive & Protective Proceedings",
        summary="Statutory safeguard preventing adverse ex-parte orders by requiring mandatory notice and hearing before any interlocutory order or injunction is granted.",
        statutory_grounds=[
            {
                "clause": "Section 148A(1)",
                "ground": "Right to Lodge Caveat",
                "detail": "Any person claiming a right to appear before the Court on the hearing of an application which is expected to be made, or has been made, in a suit or proceeding may lodge a caveat."
            },
            {
                "clause": "Section 148A(2)",
                "ground": "Caveator's Duty of Service",
                "detail": "The caveator shall serve a notice of the caveat by registered post, acknowledgement due, on the person by whom the application was made or is expected to be made."
            },
            {
                "clause": "Section 148A(3)",
                "ground": "Court's Duty of Notice",
                "detail": "Where a caveat has been lodged, the Court shall serve a notice of the application on the caveator."
            },
            {
                "clause": "Section 148A(4)",
                "ground": "Applicant's Duty to Furnish Pleadings",
                "detail": "Where a notice of caveat has been served on the applicant, he shall forthwith furnish the caveator with a copy of the application, plaint, and documents filed in support."
            },
            {
                "clause": "Section 148A(5)",
                "ground": "90-Day Statutory Expiry",
                "detail": "The caveat shall not remain in force after the expiry of ninety days from the date on which it was lodged, unless the application has been made before the expiry."
            }
        ],
        judicial_principles=[
            {
                "principle": "Order passed without hearing caveator is irregular",
                "citation": "Reserve Bank of India Employees Association v. RBI (1981) 1 ILR Kant 224",
                "detail": "The right conferred by Section 148A is substantial. Passing an ex-parte interim order without issuing notice to caveator deprives caveator of a valuable statutory right."
            },
            {
                "principle": "Caveat applies only to substantive proceedings",
                "citation": "Deepak Khosla v. Union of India (2011) 182 DLT 372",
                "detail": "A caveat can be lodged only by a person who has a right to appear on the hearing of the application. A stranger with no locus cannot lodge a caveat."
            }
        ],
        steps=[
            ChecklistItem(
                id="s148a_step1",
                label="Verify Locus and Expected Proceeding",
                description="Confirm caveator is a party or necessary party in the expected suit/appeal/application. Identify opposing party accurately.",
                statutory_ref="Section 148A(1)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s148a_step2",
                label="Describe Subject Matter and Relief Specifically",
                description="Specify the exact property, contract, decree, or order in respect of which an application (injunction, stay, appointment of receiver) is anticipated.",
                statutory_ref="Section 148A(1)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s148a_step3",
                label="Mandatory Service by Registered Post",
                description="Serve copy of caveat by Registered Post AD on the opposite party. Obtain postal receipt and online tracking report.",
                statutory_ref="Section 148A(2)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s148a_step4",
                label="File Caveat Petition with Verification Affidavit",
                description="Lodge caveat in the competent court registry accompanied by an affidavit verifying the facts and annexing postal proof of dispatch.",
                statutory_ref="Section 148A(1), (2)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s148a_step5",
                label="Calendar 90-Day Expiry Date",
                description="Caveat is valid for exactly 90 days from the lodging date. Mark the 85th day on chamber calendar. If no proceeding filed, lodge fresh caveat on 91st day.",
                statutory_ref="Section 148A(5)",
                is_mandatory=True
            )
        ],
        common_pitfalls=[
            "Failing to dispatch copy of caveat to opposite party by Registered Post AD (failure to comply with sub-section (2) may invalidate protection).",
            "Letting the 90-day period expire without re-filing — opposite party intentionally waits for 91st day to obtain ex-parte injunction.",
            "Vague description of subject matter, enabling opposite party to file suit under a slightly different title or description to evade caveat notice."
        ],
        connected_provisions=[
            {"kind": "section", "ref": "Section 148", "title": "Enlargement of time"},
            {"kind": "rule", "ref": "Order XXXIX Rule 1", "title": "Cases in which temporary injunction may be granted"},
            {"kind": "rule", "ref": "Order XLI Rule 5", "title": "Stay by Appellate Court"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 6. SECTION 100 — SECOND APPEAL
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="sec_100",
        title="Second Appeal Formulation (Substantial Question of Law)",
        provision="Section 100 CPC",
        category="Appeals & Revisions",
        summary="Statutory jurisdiction of the High Court in Second Appeal: strictly confined to substantial questions of law, barring re-appreciation of concurrent findings of fact.",
        statutory_grounds=[
            {
                "clause": "Section 100(1)",
                "ground": "Substantial Question of Law Required",
                "detail": "An appeal shall lie to the High Court from every decree passed in appeal by any court subordinate, if the High Court is satisfied that the case involves a substantial question of law."
            },
            {
                "clause": "Section 100(3)",
                "ground": "Mandatory Formulation in Memorandum",
                "detail": "In an appeal under this section, the memorandum of appeal shall precisely state the substantial question of law involved in the appeal."
            },
            {
                "clause": "Section 100(4)",
                "ground": "Framing of Question by High Court",
                "detail": "Where High Court is satisfied that a substantial question of law is involved in any case, it shall formulate that question."
            },
            {
                "clause": "Section 100(5)",
                "ground": "Hearing Confined to Formulated Questions",
                "detail": "The appeal shall be heard on the question so formulated and the respondent shall be allowed to argue that the case does not involve such question."
            }
        ],
        judicial_principles=[
            {
                "principle": "What is a 'Substantial Question of Law'?",
                "citation": "Sir Chunilal V. Mehta & Sons Ltd. v. Century Spg. & Mfg. Co. Ltd. AIR 1962 SC 1314",
                "detail": "The test is whether it is of general public importance or directly/substantially affects rights of parties; whether it is an open question or settled by the Supreme Court; or whether settled principles were misapplied."
            },
            {
                "principle": "Formulation of Question of Law is Mandatory",
                "citation": "Santosh Hazari v. Purushottam Tiwari (2001) 3 SCC 179",
                "detail": "A second appeal cannot be decided without formulating the substantial question of law. Judgment rendered without framing question is legally unsustainable."
            },
            {
                "principle": "Perversity of Finding of Fact is a Question of Law",
                "citation": "Hero Vinoth v. Seshammal (2006) 5 SCC 545",
                "detail": "High Court cannot interfere with concurrent findings of fact unless: (1) findings are perverse; (2) based on no evidence; or (3) vital admissible evidence was ignored."
            }
        ],
        steps=[
            ChecklistItem(
                id="s100_step1",
                label="Screen for Statutory Bars (Sec 100A & 102)",
                description="Confirm suit is NOT barred by Section 102 (no second appeal in suits of cognizable by Small Causes when subject matter <= Rs. 25,000) or Sec 100A.",
                statutory_ref="Section 100A, Section 102",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s100_step2",
                label="Verify 90-Day Limitation with Sec. 12 Exclusion",
                description="Limitation is 90 days under Article 116(a). Deduct days taken to obtain certified copy of decree and judgment of first appellate court.",
                statutory_ref="Article 116(a) r/w Section 12 Limitation Act",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s100_step3",
                label="Draft Precise Substantial Questions of Law",
                description="Do NOT frame questions as 'Whether findings are erroneous'. Frame specific legal questions: e.g. 'Whether First Appellate Court erred in reversing decree without meeting trial court reasons?'",
                statutory_ref="Section 100(3)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s100_step4",
                label="Grounds of Perversity / Misconstruction of Documents",
                description="If challenging fact findings, identify exact material documents ignored or misread (construction of document of title is a question of law).",
                statutory_ref="Hero Vinoth Precedent",
                is_mandatory=False
            ),
            ChecklistItem(
                id="s100_step5",
                label="File Application for Stay of Execution (O.41 R.5)",
                description="Second appeal does NOT operate as stay. File separate application under Order XLI Rule 5 r/w Order XLII Rule 1 with supporting affidavit.",
                statutory_ref="Order XLI Rule 5",
                is_mandatory=False
            )
        ],
        common_pitfalls=[
            "Treating second appeal as a second chance to re-argue oral evidence (High Court will dismiss in limine).",
            "Failing to draft specific substantial questions of law in the appeal memo.",
            "Not annexing certified copies of both the Trial Court and First Appellate Court judgments and decrees."
        ],
        connected_provisions=[
            {"kind": "section", "ref": "Section 100A", "title": "No further appeal in certain cases"},
            {"kind": "section", "ref": "Section 102", "title": "No second appeal in certain suits"},
            {"kind": "rule", "ref": "Order XLII Rule 1", "title": "Appeals from appellate decrees"},
            {"kind": "limitation_article", "ref": "Article 116(a)", "title": "Civil appeal to High Court (90 days)"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 7. SECTION 115 — CIVIL REVISION
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="sec_115",
        title="Civil Revision (Jurisdictional Errors)",
        provision="Section 115 CPC",
        category="Appeals & Revisions",
        summary="High Court's supervisory jurisdiction to correct jurisdictional errors of subordinate courts in cases where no appeal lies.",
        statutory_grounds=[
            {
                "clause": "Section 115(1)(a)",
                "ground": "Jurisdiction not vested by law",
                "detail": "Subordinate court exercised a jurisdiction not vested in it by law."
            },
            {
                "clause": "Section 115(1)(b)",
                "ground": "Failure to exercise vested jurisdiction",
                "detail": "Subordinate court failed to exercise a jurisdiction so vested."
            },
            {
                "clause": "Section 115(1)(c)",
                "ground": "Illegal or material irregular exercise of jurisdiction",
                "detail": "Subordinate court acted in the exercise of its jurisdiction illegally or with material irregularity."
            },
            {
                "clause": "Section 115(1) Proviso",
                "ground": "Dispositive Order Requirement",
                "detail": "High Court shall not vary or reverse any order deciding an issue, except where the order, if it had been made in favour of the applicant, would have finally disposed of the suit or other proceeding."
            }
        ],
        judicial_principles=[
            {
                "principle": "Revision is not an appeal in disguise",
                "citation": "D.L.F. Housing & Construction Co. v. Sarup Singh (1969) 3 SCC 807",
                "detail": "Section 115 applies to jurisdiction alone — the irregular exercise or non-exercise of it, or illegal assumption of it. The mere fact that the decision is erroneous on law or fact does not warrant revision."
            },
            {
                "principle": "The 1999 Amendment Proviso is a Strict Limitation",
                "citation": "Shiv Shakti Coop. Housing Society v. Swaraj Developers (2003) 6 SCC 659",
                "detail": "No revision lies against an interlocutory order unless the order, if passed in favour of the revision petitioner, would have brought about a final termination of the proceedings."
            }
        ],
        steps=[
            ChecklistItem(
                id="s115_step1",
                label="Confirm 'No Appeal Lies' Against the Impugned Order",
                description="Verify that no appeal (first appeal, miscellaneous appeal under Section 104 or Order XLIII Rule 1) lies against the order. If appeal lies, revision is barred.",
                statutory_ref="Section 115(1), (2)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s115_step2",
                label="Apply the Proviso Test (Final Termination Test)",
                description="Ask: If the High Court allows this revision, will the suit/proceeding finally terminate? (e.g. Order VII Rule 11 rejection allowed -> suit terminates -> revision maintainable. Order VII Rule 11 rejected -> suit continues -> revision doubtful).",
                statutory_ref="Section 115(1) Proviso",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s115_step3",
                label="Plead Jurisdictional Error Specifically",
                description="Classify error under (a), (b), or (c). Mere error of law or fact without jurisdictional deficit is not revisable.",
                statutory_ref="Section 115(1)(a)-(c)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s115_step4",
                label="Verify 90-Day Limitation under Article 131",
                description="File within 90 days from the date of the impugned order, plus Section 12 certified copy exclusion time.",
                statutory_ref="Article 131 Limitation Act",
                is_mandatory=True
            ),
            ChecklistItem(
                id="s115_step5",
                label="Section 115(3) No Automatic Stay Rule",
                description="Filing revision does NOT operate as stay. File specific application for stay of trial court proceedings with affidavit of irreparable injury.",
                statutory_ref="Section 115(3)",
                is_mandatory=False
            )
        ],
        common_pitfalls=[
            "Filing a revision against an order against which a miscellaneous appeal lies under Order XLIII Rule 1 (sub-section (2) strictly bars revision).",
            "Filing a revision against an interim procedural order (e.g. framing of issues, amendment of plaint, document marking) that violates the 1999 Proviso.",
            "Not seeking a stay from the High Court, leading to the trial court proceeding and passing final judgment while revision is pending."
        ],
        connected_provisions=[
            {"kind": "section", "ref": "Section 104", "title": "Orders from which appeal lies"},
            {"kind": "rule", "ref": "Order XLIII Rule 1", "title": "Appeals from orders"},
            {"kind": "limitation_article", "ref": "Article 131", "title": "Civil Revision to High Court (90 days)"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 8. PLAINT INSTITUTION & REGISTRY SCRUTINY (ORDER VII)
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="plaint_scrutiny_o7",
        title="Plaint Institution & Registry Scrutiny Checklist",
        provision="Section 26 & Order VII Rules 1–18 CPC",
        category="Trial Court Practice & Pleadings",
        summary="Statutory registry scrutiny checklist for instituting civil plaints, ensuring full compliance with Order VII particulars, valuation, court fees, and document production.",
        statutory_grounds=[
            {"ground": "Order VII Rule 1", "description": "Mandatory particulars to be contained in every plaint (court name, parties, facts, cause of action, jurisdiction, valuation, and specific relief claimed)."},
            {"ground": "Order VII Rule 3", "description": "Where the subject matter is immovable property, description sufficient to identify it with survey number, boundaries, and extent."},
            {"ground": "Order VII Rule 14", "description": "Mandatory production of documents sued upon in plaintiff's possession and list of documents not in possession."},
            {"ground": "Order VI Rule 15", "description": "Mandatory verification of pleadings by plaintiff at foot on personal knowledge and belief, supported by affidavit."}
        ],
        judicial_principles=[
            {"citation": "Salem Advocate Bar Association v. Union of India (2005) 6 SCC 344", "principle": "Procedural compliance under Order VII is intended to eliminate frivolous litigation at the threshold and ensure fair notice."},
            {"citation": "Sopan Sukhdeo Sable v. Asst Charity Commr (2004) 3 SCC 137", "principle": "Cause of action is a bundle of essential facts which plaintiff must prove to obtain a decree; distinct dates and places must be pleaded."}
        ],
        steps=[
            ChecklistItem(
                id="ps_parties_description",
                label="Proper Description & Capacity of Parties (Rule 1(a)-(c))",
                description="Verify accurate names, parentage, occupations, and full residential addresses of all parties. If minors or persons of unsound mind are arrayed, ensure representation through next friend / guardian under Order XXXII.",
                statutory_ref="Order VII Rule 1(a)-(c) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ps_cause_of_action_bundle",
                label="Specific Bundle of Facts & Dates Constituting Cause of Action",
                description="Plaint must specifically plead: (1) The bundle of facts constituting the cause of action; (2) The exact date and place where the cause of action first arose and subsequently subsisted.",
                statutory_ref="Order VII Rule 1(e) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ps_jurisdiction_facts",
                label="Territorial & Pecuniary Jurisdiction Averments (Rule 1(f))",
                description="Plead facts demonstrating court's jurisdiction: (a) Immovable property situated within territorial jurisdiction (Sec 16); (b) Cause of action wholly or in part arose within jurisdiction (Sec 20(c)); (c) Suit valuation is within pecuniary limits.",
                statutory_ref="Order VII Rule 1(f) & Sections 15-20 CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ps_valuation_court_fees",
                label="Valuation Slip & Court Fee Calculation (Rule 1(i))",
                description="File separate Valuation Slip setting out valuation for purposes of court fees and jurisdiction under the State Court Fees & Suits Valuation Act, attaching appropriate court fee stamps or e-Challan receipt.",
                statutory_ref="Order VII Rule 1(i) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ps_specific_relief_prayed",
                label="Precise & Categorical Prayer Clause (Rule 7)",
                description="Every plaint must state specifically the relief which plaintiff claims, either simply or in the alternative. Also include prayer for costs and general relief.",
                statutory_ref="Order VII Rule 7 CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ps_schedule_property_boundaries",
                label="Property Schedule with Four Boundaries & Sy. No. (Rule 3)",
                description="Where the suit is for immovable property, the plaint must contain a description of the property sufficient to identify it: Survey No., Municipal assessment no., extent, and boundaries East, West, North, South.",
                statutory_ref="Order VII Rule 3 CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ps_document_list_rule_14",
                label="Order VII Rule 14 Document Production & List",
                description="Plaintiff must append: (1) List of documents sued upon / in his possession produced with plaint; (2) List of documents relied upon but NOT in his possession, stating in whose custody they are.",
                statutory_ref="Order VII Rule 14(1) & (2) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ps_verification_statement_truth",
                label="Order VI Rule 15 Verification & Supporting Affidavit",
                description="Plaint must be verified by plaintiff at foot, stating specifically what paragraphs are verified on personal knowledge and what on information received and believed to be true, accompanied by supporting affidavit.",
                statutory_ref="Order VI Rule 15 & Section 26(2) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ps_summons_copies_batta",
                label="Duplicate Copies of Plaint & Process Fee (Order VII Rule 9)",
                description="Plaintiff must present one copy of plaint for each defendant along with summons forms, postal covers, and process fee (batta) within 7 days of summons order.",
                statutory_ref="Order VII Rule 9 CPC",
                is_mandatory=True
            )
        ],
        common_pitfalls=[
            "Omitting specific boundaries in the schedule, making physical execution of decree impossible under Order XXI Rule 35.",
            "Failing to file list of documents relied upon under Order VII Rule 14, preventing their subsequent admission at trial without leave.",
            "Pleading a vague cause of action date like 'arose recently', inviting rejection under Order VII Rule 11(a) or (d).",
            "Failing to pay process fees (batta) within 7 days, resulting in dismissal of suit under Order IX Rule 2 CPC."
        ],
        connected_provisions=[
            {"kind": "section", "ref": "Section 26", "title": "Institution of suits"},
            {"kind": "rule", "ref": "Order VII Rule 1", "title": "Particulars to be contained in plaint"},
            {"kind": "rule", "ref": "Order VII Rule 11", "title": "Rejection of plaint"},
            {"kind": "rule", "ref": "Order VII Rule 14", "title": "Production of document on which plaintiff sues or relies"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 9. WRITTEN STATEMENT & COUNTER-CLAIM COMPLIANCE (ORDER VIII)
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="written_statement_o8",
        title="Written Statement & Counter-Claim Compliance Checklist",
        provision="Order VIII Rules 1–10 CPC",
        category="Trial Court Practice & Pleadings",
        summary="Strict timelines, specific denial tests, doctrine of non-traverse, preliminary objections, and counter-claim compliance under Order VIII.",
        statutory_grounds=[
            {"ground": "Order VIII Rule 1", "description": "Written statement must be filed within 30 days of summons service; extendable up to 90 days for reasons recorded in writing."},
            {"ground": "Order VIII Rule 3", "description": "Denial to be specific; general denial is no denial in the eye of law."},
            {"ground": "Order VIII Rule 5", "description": "Every allegation of fact not denied specifically or by necessary implication is deemed to be admitted (Doctrine of Non-Traverse)."},
            {"ground": "Order VIII Rule 6A", "description": "Counter-claim maintainable before defense is delivered or time for delivery expires, having effect of a cross-suit."}
        ],
        judicial_principles=[
            {"citation": "Kailash v. Nanhku (2005) 4 SCC 480", "principle": "90-day time limit under Order VIII Rule 1 is directory in ordinary civil suits, but extension requires extraordinary recorded reasons."},
            {"citation": "SCG Contracts (India) Pvt Ltd v. K.S. Chamankar Infrastructure (2019) 12 SCC 210", "principle": "In Commercial Suits, the 120-day outer limit is mandatory and non-extendable, resulting in total forfeiture of right to file WS."},
            {"citation": "Badat & Co. v. East India Trading Co. AIR 1964 SC 538", "principle": "Rules of specific denial under Rules 3 and 5 are mandatory; evasive denials constitute clear admission of fact."},
            {"citation": "Ashok Kumar Kalra v. Wing Cdr. Surendra Agnihotri (2020) 2 SCC 394", "principle": "Counter-claim cannot be permitted to be filed after framing of issues."}
        ],
        steps=[
            ChecklistItem(
                id="ws_strict_limitation_audit",
                label="30-Day / 90-Day Limitation Audit (O.8 R.1)",
                description="Written statement must be filed within 30 days of summons service. Court may extend up to 90 days for reasons recorded in writing. (In Commercial Suits, strict 120-day outer limit forfeits defense).",
                statutory_ref="Order VIII Rule 1 CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ws_specific_denial_rule",
                label="Specific Para-Wise Denials (Rules 3 & 4)",
                description="Denial of allegations of fact in plaint must be specific. Defendant must deal specifically with each allegation of fact of which he does not admit the truth.",
                statutory_ref="Order VIII Rules 3 & 4 CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ws_doctrine_of_non_traverse",
                label="Doctrine of Non-Traverse Audit (O.8 R.5)",
                description="Every allegation of fact in the plaint, if not denied specifically or by necessary implication, shall be taken to be admitted by the defendant.",
                statutory_ref="Order VIII Rule 5(1) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ws_preliminary_legal_objections",
                label="Mandatory Preliminary Legal Objections Formulated",
                description="Pleas of limitation (Sec 3 Limitation Act), res judicata (Sec 11 CPC), non-joinder of necessary parties (O.1 R.9), lack of jurisdiction, or deficient court fee must be raised at the threshold.",
                statutory_ref="Order VIII Rule 2 CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ws_counter_claim_rules",
                label="Order VIII Rule 6A Counter-Claim Compliance",
                description="Counter-claim must relate to a cause of action accruing before delivery of defense or before time limited for delivery has expired. Court fees must be paid as on a separate plaint.",
                statutory_ref="Order VIII Rule 6A CPC",
                is_mandatory=False
            ),
            ChecklistItem(
                id="ws_document_disclosure",
                label="Order VIII Rule 1A Document List & Production",
                description="Defendant must produce all documents in his possession or power upon which he bases his defense or counter-claim in court when WS is presented.",
                statutory_ref="Order VIII Rule 1A CPC",
                is_mandatory=True
            )
        ],
        common_pitfalls=[
            "Using evasive or general denials like 'contents of paragraph 3 are denied as false', leading to deemed admission under Rule 5.",
            "Filing Written Statement beyond 30 days without an accompanying condonation application explaining sufficient cause.",
            "Attempting to file a counter-claim after issues are framed, which is barred under Ashok Kumar Kalra (2020).",
            "Failing to produce defense title documents under Rule 1A, precluding their admission in evidence at trial."
        ],
        connected_provisions=[
            {"kind": "rule", "ref": "Order VIII Rule 1", "title": "Written statement"},
            {"kind": "rule", "ref": "Order VIII Rule 3", "title": "Denial to be specific"},
            {"kind": "rule", "ref": "Order VIII Rule 5", "title": "Specific denial"},
            {"kind": "rule", "ref": "Order VIII Rule 6A", "title": "Counter-claim by defendant"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 10. AMENDMENT OF PLEADINGS (ORDER VI RULE 17)
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="amendment_pleadings_o6_r17",
        title="Order VI Rule 17 Amendment of Pleadings Checklist",
        provision="Order VI Rule 17 CPC",
        category="Trial Court Practice & Pleadings",
        summary="Pre-trial vs post-commencement of trial tests, statutory due diligence proviso, fundamental character rule, and limitation bars under Order VI Rule 17.",
        statutory_grounds=[
            {"ground": "Order VI Rule 17 Main Body", "description": "Court may at any stage of proceedings allow either party to alter or amend pleadings in such manner as may be just for determining real questions in controversy."},
            {"ground": "Order VI Rule 17 Proviso", "description": "Mandatory bar: No application for amendment shall be allowed after trial has commenced, unless court concludes that in spite of due diligence, the party could not have raised the matter before trial commenced."},
            {"ground": "Order VI Rule 18", "description": "Failure to amend within 14 days of order prevents amendment without leave of court."}
        ],
        judicial_principles=[
            {"citation": "Vidyabai v. Padmalatha (2009) 2 SCC 409", "principle": "Court lacks jurisdiction to allow post-trial amendment unless the condition precedent of 'due diligence' is strictly pleaded and proved."},
            {"citation": "Revajeetu Builders & Developers v. Narayanaswamy & Sons (2009) 10 SCC 84", "principle": "Amendment cannot be allowed if it alters the fundamental character of the suit, causes irreparable prejudice, or takes away an accrued right of limitation."},
            {"citation": "Life Insurance Corporation of India v. Sanjeev Builders (2022) 16 SCC 1", "principle": "All amendments ought to be allowed which satisfy two conditions: (a) not working injustice to other side; (b) necessary for determining real questions in controversy."},
            {"citation": "Mohinder Kumar Mehra v. Roop Rani Mehra (2018) 2 SCC 132", "principle": "Trial commences when issues are framed and affidavit of examination-in-chief of witness is tendered."}
        ],
        steps=[
            ChecklistItem(
                id="amend_stage_trial_commenced",
                label="Stage Audit: Has the Trial Commenced?",
                description="Has the court framed issues and has the plaintiff filed the affidavit in examination-in-chief of witness under Order XVIII Rule 4?",
                statutory_ref="Order VI Rule 17 Proviso",
                is_mandatory=True
            ),
            ChecklistItem(
                id="amend_due_diligence_proviso",
                label="Statutory Due Diligence Test (Post-Trial Proviso)",
                description="If trial has commenced, has the applicant pleaded and proven with cogent evidence that in spite of due diligence, he could not have raised the matter before trial commenced?",
                statutory_ref="Order VI Rule 17 Proviso & Vidyabai (2009)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="amend_fundamental_character",
                label="Fundamental Character & Nature of Suit Unaltered",
                description="Does the proposed amendment change the fundamental nature or character of the suit? (e.g. converting a bare injunction suit into a declaration and possession suit after limitation).",
                statutory_ref="Revajeetu Builders (2009) 10 SCC 84",
                is_mandatory=True
            ),
            ChecklistItem(
                id="amend_accrued_limitation_right",
                label="No Deprivation of Accrued Limitation Defense",
                description="Does the amendment seek to introduce a time-barred claim that would defeat a valuable accrued right of limitation acquired by the opposite party?",
                statutory_ref="Revajeetu Builders (2009) 10 SCC 84",
                is_mandatory=True
            ),
            ChecklistItem(
                id="amend_real_question_controversy",
                label="Determination of Real Question in Controversy",
                description="Is the amendment necessary for the purpose of determining the real questions in controversy between the parties and avoiding multiplicity of suits?",
                statutory_ref="Order VI Rule 17 Main Body",
                is_mandatory=True
            ),
            ChecklistItem(
                id="amend_rule_18_fourteen_days",
                label="Order VI Rule 18 Fourteen-Day Filing Window",
                description="Once amendment is allowed, the party must amend the pleading and file amended copy within 14 days from the date of the order (or time fixed by court).",
                statutory_ref="Order VI Rule 18 CPC",
                is_mandatory=True
            )
        ],
        common_pitfalls=[
            "Failing to plead 'due diligence' in the supporting affidavit when moving an amendment application after trial has commenced.",
            "Attempting to withdraw an unequivocal admission made in the Written Statement by way of amendment.",
            "Failing to file the amended copy of plaint or written statement within the mandatory 14-day window under Order VI Rule 18.",
            "Seeking an amendment that introduces a time-barred cause of action, depriving adversary of statutory limitation defense."
        ],
        connected_provisions=[
            {"kind": "rule", "ref": "Order VI Rule 17", "title": "Amendment of pleadings"},
            {"kind": "rule", "ref": "Order VI Rule 18", "title": "Failure to amend after Order (14 days)"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 11. COURT COMMISSIONER (ORDER XXVI RULE 9)
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="commissioner_o26_r9",
        title="Order XXVI Rule 9 Court Commissioner Checklist",
        provision="Order XXVI Rule 9 CPC",
        category="Interlocutory & Emergency Remedies",
        summary="Statutory tests for local investigation, boundaries, encroachment, and the cardinal rule prohibiting collection of evidence or possession enquiry.",
        statutory_grounds=[
            {"ground": "Order XXVI Rule 9", "description": "Court may issue commission to any person directing him to make local investigation for purpose of elucidating any matter in dispute, or ascertaining market value or mesne profits."},
            {"ground": "Order XXVI Rule 10(2)", "description": "Report of Commissioner and evidence taken by him shall be evidence in the suit and form part of the record."},
            {"ground": "Order XXVI Rule 10A", "description": "Commission for scientific investigation, expert examination, or performance of experiment."}
        ],
        judicial_principles=[
            {"citation": "Haryana Waqf Board v. Shanti Sarup (2008) 8 SCC 671", "principle": "Controversy regarding demarcation and encroachment can only be resolved by appointing a commissioner with surveyor assistance."},
            {"citation": "Padam Sen v. State of Uttar Pradesh AIR 1961 SC 218", "principle": "Inherent powers cannot be exercised to appoint commissioner to seize private documents or usurp court functions."},
            {"citation": "Southern Command Military Engg Services v. V.K.K. Nair (1987)", "principle": "Commissioner cannot be appointed to collect evidence or report who is in physical possession."}
        ],
        steps=[
            ChecklistItem(
                id="comm_legitimate_object",
                label="Legitimate Object for Local Investigation",
                description="Is the commission required for: (a) Elucidating any matter in dispute; (b) Ascertaining market value / mesne profits; (c) Inspecting physical boundaries and demarcating encroachment?",
                statutory_ref="Order XXVI Rule 9 CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="comm_no_possession_enquiry",
                label="Cardinal Prohibition: No Commission on Possession",
                description="Ensure application does NOT pray for commissioner to report 'who is in physical possession' of the property.",
                statutory_ref="Settled Supreme Court & High Court Law",
                is_mandatory=True
            ),
            ChecklistItem(
                id="comm_no_collection_of_evidence",
                label="Prohibition Against 'Collection of Evidence'",
                description="Verify that the applicant is not using the commissioner to gather evidence to fill up gaps or lacunae in his own case.",
                statutory_ref="Padam Sen AIR 1961 SC 218",
                is_mandatory=True
            ),
            ChecklistItem(
                id="comm_surveyor_assistance_memo",
                label="Surveyor Assistance & Record Reference",
                description="Does the application seek assistance of a qualified Government / Taluk Surveyor to measure the property with reference to village maps and survey records?",
                statutory_ref="Order XXVI Rule 9 CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="comm_memo_of_instructions",
                label="Clear & Precise Memo of Instructions Ready",
                description="Have specific, objective, and non-argumentative points of reference been drafted for the commissioner's inspection memo?",
                statutory_ref="Order XXVI Rule 10 CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="comm_evidentiary_value",
                label="Evidentiary Status of Report (Rule 10(2))",
                description="The report of the Commissioner and evidence taken by him shall be evidence in the suit and form part of the record, but either party may examine the commissioner in court.",
                statutory_ref="Order XXVI Rule 10(2) CPC",
                is_mandatory=False
            )
        ],
        common_pitfalls=[
            "Praying for commissioner to ascertain 'who is in actual possession', leading to immediate dismissal.",
            "Appointing an advocate commissioner without government surveyor assistance in boundary encroachment disputes.",
            "Failing to file formal written Objections to the commissioner's report within 14 days of filing in court.",
            "Failing to summon the commissioner for cross-examination when challenging an erroneous survey sketch."
        ],
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXVI Rule 9", "title": "Commissions to make local investigations"},
            {"kind": "rule", "ref": "Order XXVI Rule 10", "title": "Procedure of Commissioner. Report and evidence"},
            {"kind": "rule", "ref": "Order XXVI Rule 10A", "title": "Commission for scientific investigation"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 12. ATTACHMENT BEFORE JUDGMENT (ORDER XXXVIII RULE 5)
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="attachment_before_judgment_o38_r5",
        title="Order XXXVIII Rule 5 Attachment Before Judgment Checklist",
        provision="Order XXXVIII Rule 5 CPC",
        category="Interlocutory & Emergency Remedies",
        summary="Drastic remedy standards, strict proof of intent to obstruct execution, show-cause mandate, and Rule 5(4) voidness rule.",
        statutory_grounds=[
            {"ground": "Order XXXVIII Rule 5(1)", "description": "Court satisfied defendant is about to dispose of or remove property from jurisdiction with intent to obstruct or delay execution."},
            {"ground": "Order XXXVIII Rule 5(1) Proviso", "description": "Court must direct defendant to furnish security or appear and show cause why he should not furnish security."},
            {"ground": "Order XXXVIII Rule 5(4)", "description": "Attachment made without complying with sub-rule (1) shall be VOID."},
            {"ground": "Order XXXVIII Rule 6", "description": "Attachment where cause not shown or security not furnished."}
        ],
        judicial_principles=[
            {"citation": "Raman Tech. & Process Engg. Co. v. Bharat Perfumes Ltd. (2008) 2 SCC 302", "principle": "Power under Order XXXVIII Rule 5 is a drastic and extraordinary power; cannot be used to convert an unsecured debt into a secured debt."},
            {"citation": "Rajendran v. Shankar Sundaram (2008) 2 SCC 724", "principle": "Prima facie case of debt and concrete material showing imminent attempt to defeat execution must co-exist."}
        ],
        steps=[
            ChecklistItem(
                id="abj_drastic_remedy_standard",
                label="Drastic & Extraordinary Remedy Standard",
                description="Is the plaintiff aware that ABJ is a drastic power that should not be exercised mechanically merely because plaintiff has a good case on merits?",
                statutory_ref="Raman Tech (2008) 2 SCC 302",
                is_mandatory=True
            ),
            ChecklistItem(
                id="abj_specific_intent_to_defraud",
                label="Specific Evidence of Attempt to Dispose of Property",
                description="Has plaintiff placed concrete, specific facts showing defendant is about to dispose of or remove property from court jurisdiction with INTENT to obstruct or delay execution?",
                statutory_ref="Order XXXVIII Rule 5(1) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="abj_mandatory_show_cause",
                label="Mandatory Show-Cause / Security Option (Rule 5(1))",
                description="Court MUST first direct defendant either to furnish security in sum specified or appear and show cause why he should not furnish security.",
                statutory_ref="Order XXXVIII Rule 5(1) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="abj_rule_5_4_voidness_rule",
                label="Rule 5(4) Mandatory Voidness Rule",
                description="If an order of attachment is made without complying with the provisions of sub-rule (1), such attachment shall be VOID.",
                statutory_ref="Order XXXVIII Rule 5(4) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="abj_unencumbered_property_schedule",
                label="Detailed Schedule of Unencumbered Immovable Property",
                description="Provide full particulars of the property sought to be attached: survey number, boundaries, municipal number, and verify absence of prior bank mortgage.",
                statutory_ref="Order XXXVIII Rule 5(1) CPC",
                is_mandatory=True
            )
        ],
        common_pitfalls=[
            "Making mechanical, bald assertions that 'defendant is attempting to sell property' without specifying brokers, buyers, or deeds.",
            "Obtaining an absolute order of attachment without giving the defendant the mandatory statutory opportunity to furnish security.",
            "Seeking to attach property situated outside the territorial jurisdiction of the trial court.",
            "Seeking attachment of property already mortgaged to a secured creditor bank, which takes statutory precedence."
        ],
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXXVIII Rule 5", "title": "Attachment before judgment"},
            {"kind": "rule", "ref": "Order XXXVIII Rule 6", "title": "Attachment where cause not shown"},
            {"kind": "rule", "ref": "Order XXXVIII Rule 9", "title": "Removal of attachment when security furnished"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 13. SUMMARY SUITS & LEAVE TO DEFEND (ORDER XXXVII)
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="summary_suit_o37",
        title="Order XXXVII Summary Suit & Leave to Defend Checklist",
        provision="Order XXXVII Rules 1, 2 & 3 CPC",
        category="Trial Court Practice & Pleadings",
        summary="Summary suit eligibility, strict 10-day appearance & leave to defend timelines, and the IDBI Trusteeship 5-prong test.",
        statutory_grounds=[
            {"ground": "Order XXXVII Rule 1(2)", "description": "Applicable to suits upon bills of exchange, hundis, promissory notes, or for recovery of debts/liquidated demands arising on written contracts or guarantees."},
            {"ground": "Order XXXVII Rule 2(3)", "description": "Defendant shall not defend suit unless he enters appearance; in default of appearance, allegations in plaint deemed admitted and plaintiff entitled to decree."},
            {"ground": "Order XXXVII Rule 3(5)", "description": "Defendant may apply for leave to defend within 10 days from service of summons for judgment, disclosing substantial defense."},
            {"ground": "Article 118 Limitation Act", "description": "10 days limitation for leave to appear and defend a summary suit."}
        ],
        judicial_principles=[
            {"citation": "IDBI Trusteeship Services Ltd v. Hubtown Ltd (2017) 1 SCC 568", "principle": "Re-formulated 5-point test for leave to defend: substantial defense entitles unconditional leave; triable issue entitles unconditional leave; plausible/doubtful defense entitles conditional leave upon deposit."},
            {"citation": "B.L. Kashyap & Sons Ltd. v. JMS Steels (2022) 3 SCC 294", "principle": "Leave to defend should not be granted on illusory or moonshine defense, but summary procedure is not a shortcut to shut out real defenses."}
        ],
        steps=[
            ChecklistItem(
                id="o37_eligible_class_of_suit",
                label="Eligible Subject Matter under Rule 1(2)",
                description="Suit must be upon: (a) Bills of exchange, hundis, or promissory notes; OR (b) Recovery of a debt or liquidated demand arising on a written contract, enactment, or guarantee.",
                statutory_ref="Order XXXVII Rule 1(2) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o37_strict_10_day_appearance",
                label="10-Day Summons for Appearance (Rule 3(1))",
                description="Defendant must enter appearance within 10 days of service of summons under Form No. 4, Appendix B, and file address for service in court.",
                statutory_ref="Order XXXVII Rule 3(1) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o37_summons_for_judgment",
                label="Service of Summons for Judgment (Rule 3(4))",
                description="Plaintiff must serve Summons for Judgment in Form No. 4A supported by affidavit verifying cause of action and amount claimed, stating belief of no defense.",
                statutory_ref="Order XXXVII Rule 3(4) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o37_strict_10_day_leave_defend",
                label="10-Day Leave to Defend Window (Article 118)",
                description="Defendant must apply for leave to defend by affidavit disclosing facts sufficient to entitle him to defend within STRICT 10 DAYS from service of summons for judgment.",
                statutory_ref="Order XXXVII Rule 3(5) CPC & Article 118",
                is_mandatory=True
            ),
            ChecklistItem(
                id="o37_idbi_hubtown_test",
                label="IDBI Trusteeship v. Hubtown 5-Prong Merits Test",
                description="Examine defense against Hubtown principles: (1) Substantial defense -> Unconditional leave; (2) Triable issue showing fair/reasonable defense -> Unconditional leave; (3) Dubious/plausible defense -> Conditional leave (deposit of money); (4) Sham/moonshine defense -> Refusal of leave.",
                statutory_ref="IDBI Trusteeship (2017) 1 SCC 568",
                is_mandatory=True
            )
        ],
        common_pitfalls=[
            "Filing regular Written Statement instead of entering appearance within 10 days of summons, resulting in default decree.",
            "Missing the strict 10-day deadline for applying for leave to defend from summons for judgment.",
            "Instituting suit under Order XXXVII for unliquidated damages or tortious claims, resulting in conversion to ordinary suit.",
            "Failing to annex original negotiable instruments / written contracts to the summary plaint."
        ],
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXXVII Rule 1", "title": "Application of Order"},
            {"kind": "rule", "ref": "Order XXXVII Rule 2", "title": "Institution of summary suits"},
            {"kind": "rule", "ref": "Order XXXVII Rule 3", "title": "Procedure for appearance of defendant"},
            {"kind": "limitation_article", "ref": "Article 118", "title": "Leave to defend summary suit (10 days)"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 14. SETTING ASIDE EX-PARTE DECREE (ORDER IX RULE 13)
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="set_aside_ex_parte_o9_r13",
        title="Order IX Rule 13 Setting Aside Ex-Parte Decree Checklist",
        provision="Order IX Rule 13 CPC & Article 123 Limitation Act",
        category="Post-Decree & Restoration Remedies",
        summary="Grounds of non-service vs sufficient cause, date of knowledge limitation audit, second proviso safeguard, and conditional restoration.",
        statutory_grounds=[
            {"ground": "Order IX Rule 13", "description": "Defendant may apply to court by which decree was passed for an order to set it aside upon satisfying court of non-service of summons or sufficient cause for non-appearance."},
            {"ground": "Order IX Rule 13 Second Proviso", "description": "Court shall not set aside decree on ground of irregularity in service of summons if satisfied defendant had notice in sufficient time."},
            {"ground": "Article 123 Limitation Act", "description": "Limitation is 30 days from date of decree, or where summons not duly served, 30 days from date of knowledge of decree."}
        ],
        judicial_principles=[
            {"citation": "Parimal v. Veena (2011) 3 SCC 545", "principle": "Sufficient cause must be an explanation beyond control of party; court must record clear finding on whether defendant was prevented by bona fide cause."},
            {"citation": "G.P. Srivastava v. R.K. Raizada (2000) 3 SCC 54", "principle": "Court should adopt liberal approach on date of hearing if non-appearance was not intentional, so matter is decided on merits."},
            {"citation": "Sunil Poddar v. Union Bank of India (2008) 2 SCC 326", "principle": "Under second proviso, if defendant had knowledge of suit proceedings, technical irregularity in summons service does not justify setting aside decree."}
        ],
        steps=[
            ChecklistItem(
                id="exparte_two_statutory_grounds",
                label="Two Exclusive Statutory Grounds under Rule 13",
                description="Defendant must satisfy court that: EITHER (1) Summons was not duly served; OR (2) He was prevented by any 'sufficient cause' from appearing when suit was called on for hearing.",
                statutory_ref="Order IX Rule 13 CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="exparte_limitation_article_123",
                label="Article 123 Limitation: Date of Decree vs Date of Knowledge",
                description="Limitation is 30 DAYS: (a) From date of decree (if summons served); OR (b) From date of KNOWLEDGE of the decree (where summons was NOT duly served).",
                statutory_ref="Article 123, Limitation Act 1963",
                is_mandatory=True
            ),
            ChecklistItem(
                id="exparte_second_proviso_bar",
                label="Second Proviso Safeguard (Notice in Sufficient Time)",
                description="Court SHALL NOT set aside decree merely on irregularity in service of summons, if satisfied that defendant had notice of date of hearing in sufficient time to appear.",
                statutory_ref="Order IX Rule 13 Second Proviso",
                is_mandatory=True
            ),
            ChecklistItem(
                id="exparte_sufficient_cause_proof",
                label="Sufficient Cause Substantiated by Cogent Evidence",
                description="Was non-appearance on the hearing date caused by genuine illness, accident, bereavement, or unavoidable circumstances? Produce medical records / hospital discharge summary.",
                statutory_ref="Parimal v. Veena (2011) 3 SCC 545",
                is_mandatory=True
            ),
            ChecklistItem(
                id="exparte_terms_costs",
                label="Terms as to Costs & Deposit under Rule 13",
                description="Court may set aside decree upon such terms as to costs, payment into court, or otherwise as it thinks fit.",
                statutory_ref="Order IX Rule 13 CPC",
                is_mandatory=False
            )
        ],
        common_pitfalls=[
            "Filing application beyond 30 days from date of decree without explaining the date of knowledge or filing Section 5 condonation application.",
            "Relying on technical defects in bailiff report when defendant in fact had actual notice of the suit.",
            "Failing to demonstrate a meritorious prima facie defense to the suit in the supporting affidavit.",
            "Failing to deposit conditional costs or security ordered by court, resulting in dismissal of restoration application."
        ],
        connected_provisions=[
            {"kind": "rule", "ref": "Order IX Rule 13", "title": "Setting aside decree ex parte against defendant"},
            {"kind": "section", "ref": "Section 5", "title": "Extension of prescribed period (Limitation Act)"},
            {"kind": "limitation_article", "ref": "Article 123", "title": "To set aside an ex-parte decree (30 days)"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 15. EXECUTION PETITION SCRUTINY (ORDER XXI)
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="execution_petition_o21",
        title="Order XXI Execution Petition Scrutiny Checklist",
        provision="Order XXI Rules 11, 22 & Section 60 CPC",
        category="Execution Proceedings",
        summary="Mandatory 10-column execution particulars, Rule 22 notice requirements, Section 60 property exemptions, and 12-year limitation audit.",
        statutory_grounds=[
            {"ground": "Order XXI Rule 11(2)", "description": "Written application for execution containing in tabular form all 10 statutory particulars (a) to (j)."},
            {"ground": "Order XXI Rule 22", "description": "Mandatory show-cause notice to JD if EP is filed after two years from decree date or against legal representatives."},
            {"ground": "Section 60 CPC", "description": "Statutory list of properties liable to attachment and sale, and mandatory list of non-attachable exempt properties."},
            {"ground": "Article 136 Limitation Act", "description": "12-year limitation period for execution of any decree (other than mandatory injunction)."}
        ],
        judicial_principles=[
            {"citation": "Rahul S. Shah v. Jinendra Kumar Gandhi (2021) 6 SCC 418", "principle": "Supreme Court directions: executing court must dispose of execution petitions within 6 months and ensure decree holder gets fruits of decree."},
            {"citation": "Jagan Singh v. Dhanwanti (2012) 2 SCC 628", "principle": "Executing court cannot go behind the decree; it must execute the decree as it stands."}
        ],
        steps=[
            ChecklistItem(
                id="ep_limitation_article_136",
                label="Limitation Audit: Article 136 (12 Years) vs Article 135",
                description="Execution for money, possession, or general decree: 12 YEARS from when decree becomes enforceable. Mandatory injunction: 3 YEARS under Article 135.",
                statutory_ref="Articles 135 & 136, Limitation Act 1963",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ep_rule_11_ten_columns",
                label="Mandatory 10-Column Tabular Format (Rule 11(2))",
                description="Execution petition must be in writing, verified by DH, containing in tabular form all 10 particulars: suit no., parties, decree date, appeal status, payments made, costs, mode of assistance.",
                statutory_ref="Order XXI Rule 11(2) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ep_rule_22_notice_audit",
                label="Order XXI Rule 22 Mandatory Show-Cause Notice",
                description="Notice to JD is MANDATORY where EP is filed: (a) More than two years after date of decree; OR (b) Against legal representatives of deceased JD; OR (c) Where decree is against assignee in insolvency.",
                statutory_ref="Order XXI Rule 22(1) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ep_section_60_exemptions",
                label="Section 60 Statutory Property Exemptions Audit",
                description="Verify that property sought to be attached is NOT exempt: tools of artisans, agricultural implements, wearing apparel, cooking vessels, 2/3rd of salary above first Rs. 1,000, pensions, and gratuities.",
                statutory_ref="Section 60(1) Provisos (a)-(p) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="ep_jurisdiction_transmission",
                label="Territorial Jurisdiction & Transfer of Decree (Sec 38/39)",
                description="Is the property situated within this court's territorial jurisdiction? If property is in another district, obtain Certificate of Non-Satisfaction and decree transmission under Section 39.",
                statutory_ref="Sections 38 & 39 CPC",
                is_mandatory=True
            )
        ],
        common_pitfalls=[
            "Executing a mandatory injunction decree after 3 years under the mistaken belief that 12-year limitation applies.",
            "Issuing attachment warrant without serving Rule 22 notice when execution is filed after 2 years from decree date.",
            "Attempting to attach properties exempt under Section 60 CPC (e.g. pension, basic agricultural tools, 2/3rd salary).",
            "Executing against property in another district without obtaining transfer of decree under Section 39 CPC."
        ],
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXI Rule 11", "title": "Application for execution"},
            {"kind": "rule", "ref": "Order XXI Rule 22", "title": "Notice to show cause against execution"},
            {"kind": "section", "ref": "Section 60", "title": "Property liable to attachment and sale"},
            {"kind": "limitation_article", "ref": "Article 136", "title": "Execution of decree (12 years)"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 16. REGULAR FIRST APPEAL FILING (SECTION 96 & ORDER XLI)
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="first_appeal_sec96",
        title="Section 96 & Order XLI Regular First Appeal Checklist",
        provision="Section 96 & Order XLI Rules 1–5 CPC",
        category="Appeals & Revisions",
        summary="Certified copy requirements, limitation periods, Section 12 exclusion, grounds of appeal drafting, and Order XLI Rule 5 stay tests.",
        statutory_grounds=[
            {"ground": "Section 96 CPC", "description": "Appeal lies from every original decree passed by any court exercising original jurisdiction to court authorized to hear appeals."},
            {"ground": "Order XLI Rule 1", "description": "Form of appeal; memorandum must be accompanied by certified copy of decree and judgment."},
            {"ground": "Order XLI Rule 5", "description": "Stay by Appellate Court; filing appeal does not operate as automatic stay of execution."},
            {"ground": "Article 116 Limitation Act", "description": "Limitation for appeal under CPC: 30 days to District Court; 90 days to High Court."}
        ],
        judicial_principles=[
            {"citation": "Santosh Hazari v. Purushottam Tiwari (2001) 3 SCC 179", "principle": "First appellate court is the final court of fact and must address all points of controversy and re-appreciate evidence."},
            {"citation": "Atma Ram Properties v. Federal Motors (2005) 1 SCC 705", "principle": "Appellate court has discretion to impose reasonable conditions including deposit of market rent/damages when granting stay under Order XLI Rule 5."}
        ],
        steps=[
            ChecklistItem(
                id="rfa_certified_copies_attached",
                label="Certified Copy of Decree & Judgment (Order XLI Rule 1)",
                description="Memorandum of appeal must be accompanied by a certified copy of the decree appealed from and (unless appellate court dispenses) a copy of the judgment.",
                statutory_ref="Order XLI Rule 1(1) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="rfa_limitation_article_116",
                label="Limitation Audit: 30 Days (District Court) vs 90 Days (High Court)",
                description="Appeal to District Court: 30 DAYS under Article 116(a). Appeal to High Court: 90 DAYS under Article 116(b).",
                statutory_ref="Article 116, Limitation Act 1963",
                is_mandatory=True
            ),
            ChecklistItem(
                id="rfa_section_12_exclusion",
                label="Section 12 Exclusion of Time for Certified Copy",
                description="The time requisite for obtaining a copy of the decree and the judgment shall be excluded from computing limitation.",
                statutory_ref="Section 12(2) & (3) Limitation Act 1963",
                is_mandatory=True
            ),
            ChecklistItem(
                id="rfa_grounds_of_appeal_format",
                label="Grounds of Appeal Formulated Distinctly (Rule 1(2))",
                description="Grounds must set forth concisely and under distinct heads the grounds of objection to the decree without any argument or narrative, numbered consecutively.",
                statutory_ref="Order XLI Rule 1(2) CPC",
                is_mandatory=True
            ),
            ChecklistItem(
                id="rfa_stay_order_41_rule_5",
                label="Order XLI Rule 5 Stay Application & 3-Prong Test",
                description="Filing appeal does NOT operate as an automatic stay of decree. Stay application must establish: (1) Substantial loss may result unless stay is granted; (2) Application made without unreasonable delay; (3) Security has been given for performance.",
                statutory_ref="Order XLI Rule 5(1) & (3) CPC",
                is_mandatory=False
            )
        ],
        common_pitfalls=[
            "Assuming that mere filing of an appeal operates as an automatic stay of the trial court decree.",
            "Failing to calculate certified copy exclusion under Section 12, incorrectly believing appeal is barred by limitation.",
            "Drafting argumentative essays instead of distinct, concise grounds of appeal under Order XLI Rule 1(2).",
            "Failing to offer security for performance of decree when seeking stay of money or possession decree under Rule 5."
        ],
        connected_provisions=[
            {"kind": "section", "ref": "Section 96", "title": "Appeal from original decree"},
            {"kind": "rule", "ref": "Order XLI Rule 1", "title": "Form of appeal. What to accompany memorandum"},
            {"kind": "rule", "ref": "Order XLI Rule 5", "title": "Stay by Appellate Court"},
            {"kind": "limitation_article", "ref": "Article 116", "title": "Appeal under CPC (30/90 days)"}
        ]
    ),

    # -------------------------------------------------------------------------
    # 17. COMMERCIAL COURTS ACT PRE-FILING (COMMERCIAL COURTS ACT)
    # -------------------------------------------------------------------------
    PracticeChecklist(
        id="commercial_suit_cca",
        title="Commercial Courts Act Pre-Filing Compliance Checklist",
        provision="Commercial Courts Act, 2015",
        category="Pre-Suit Procedures & Statutory Bars",
        summary="Section 2(1)(c) classification, specified value threshold, Section 12A mandatory pre-institution mediation, Statement of Truth, and strict document discovery.",
        statutory_grounds=[
            {"ground": "Section 2(1)(c)", "description": "Exhaustive classification of commercial disputes arising out of ordinary transactions of merchants, bankers, financiers, trade, and IP."},
            {"ground": "Section 2(1)(i) & 12", "description": "Specified value of subject matter of commercial dispute not less than three lakh rupees (Rs. 3,00,000/-)."},
            {"ground": "Section 12A", "description": "Mandatory Pre-Institution Mediation through Legal Services Authority unless urgent interim relief is contemplated."},
            {"ground": "Order VI Rule 15A", "description": "Mandatory verification of pleadings by Statement of Truth; without it, pleading cannot be read in evidence."}
        ],
        judicial_principles=[
            {"citation": "Patil Automation Pvt Ltd v. Rakheja Engineers (2022) 10 SCC 1", "principle": "Section 12A pre-institution mediation is MANDATORY; suit filed without it is liable to be rejected under Order VII Rule 11."},
            {"citation": "Yamini Manohar v. T.K.D. Keerthi (2024) 5 SCC 815", "principle": "Urgent interim relief plea must be bona fide on meaningful reading of plaint, not a subterfuge to bypass Section 12A."},
            {"citation": "Ambalal Sarabhai Enterprises v. KS Infraspace (2020) 15 SCC 585", "principle": "Immovable property disputes qualify as commercial disputes only if property is used exclusively in trade or commerce."}
        ],
        steps=[
            ChecklistItem(
                id="cca_commercial_dispute_classification",
                label="Section 2(1)(c) Commercial Dispute Classification",
                description="Does the dispute fall squarely within one of clauses (i) to (xxii) of Section 2(1)(c)? (e.g. mercantile transactions, export/import, carriage of goods, franchising, distribution, IP, partnership, infrastructure).",
                statutory_ref="Section 2(1)(c) Commercial Courts Act, 2015",
                is_mandatory=True
            ),
            ChecklistItem(
                id="cca_specified_value_threshold",
                label="Specified Value Verification (Threshold Rs. 3,00,000+)",
                description="Verify that the 'Specified Value' of the subject matter computed under Section 12 is NOT less than three lakh rupees (Rs. 3,00,000/-) or higher state threshold.",
                statutory_ref="Section 2(1)(i) & Section 12 Commercial Courts Act",
                is_mandatory=True
            ),
            ChecklistItem(
                id="cca_section_12a_mediation",
                label="Section 12A Pre-Institution Mediation Compliance",
                description="Has plaintiff completed Pre-Institution Mediation through DLSA and obtained Non-Starter Report, OR has plaintiff demonstrated genuine need for urgent interim relief?",
                statutory_ref="Section 12A Commercial Courts Act & Patil Automation (2022)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="cca_statement_of_truth_mandatory",
                label="Mandatory Statement of Truth (Order VI Rule 15A)",
                description="Plaint and Written Statement MUST be verified by a Statement of Truth in Appendix I format under Order VI Rule 15A, signed by authorized representative.",
                statutory_ref="Order VI Rule 15A CPC (Commercial Schedule)",
                is_mandatory=True
            ),
            ChecklistItem(
                id="cca_order_11_disclosure",
                label="Order XI Mandatory Document Disclosure with Plaint",
                description="Plaintiff must file an exhaustive list and copies of ALL documents in his power, possession, control, or custody relating to suit, and make declaration on oath.",
                statutory_ref="Order XI Rule 1 CPC (as amended by CCA)",
                is_mandatory=True
            )
        ],
        common_pitfalls=[
            "Filing a commercial suit without exhausting Section 12A Pre-Institution Mediation where no genuine urgent interim relief is needed, inviting threshold rejection under Order VII Rule 11.",
            "Failing to file the mandatory Statement of Truth under Order VI Rule 15A, preventing the plaint from being read in evidence.",
            "Withholding relevant commercial documents from the initial filing under Order XI, resulting in total preclusion from producing them at trial.",
            "Filing in Commercial Court where specified value is below Rs. 3,00,000, resulting in return of plaint."
        ],
        connected_provisions=[
            {"kind": "section", "ref": "Section 12A", "title": "Pre-Institution Mediation and Settlement"},
            {"kind": "rule", "ref": "Order VI Rule 15A", "title": "Statement of Truth"},
            {"kind": "rule", "ref": "Order VII Rule 11", "title": "Rejection of plaint"}
        ]
    )
]

def list_checklists(category: Optional[str] = None) -> List[PracticeChecklist]:
    if category:
        return [c for c in PRACTICE_CHECKLISTS if c.category == category]
    return list(PRACTICE_CHECKLISTS)


def get_checklist(checklist_id: str) -> Optional[PracticeChecklist]:
    for c in PRACTICE_CHECKLISTS:
        if c.id == checklist_id:
            return c
    return None


def list_checklist_categories() -> List[str]:
    cats = []
    for c in PRACTICE_CHECKLISTS:
        if c.category not in cats:
            cats.append(c.category)
    return cats
