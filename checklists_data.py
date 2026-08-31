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
        category="Pleadings & Threshold Challenges",
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
        category="Interim Relief",
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
        category="Government Litigation",
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
        category="Parties & Succession",
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
        category="Interim Relief & Pre-Emption",
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
