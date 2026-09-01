"""
Authoritative Order XXI Execution Roadmap & Navigator
for Code of Civil Procedure, 1908 & The Limitation Act, 1963.
Contains 5 comprehensive execution roadmaps covering Money Decrees,
Possession of Immovable Property, Injunctions & Specific Performance,
Garnishee Proceedings, and Arrest & Detention.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class ExecutionStage:
    stage_number: int
    title: str
    governing_rules: str
    limitation_period: str
    actions_required: List[str]
    statutory_provisos: List[str]
    advocate_tactics: str


@dataclass
class ExecutionWorkflow:
    id: str
    title: str
    decree_type: str
    summary: str
    stages: List[ExecutionStage]
    connected_provisions: List[Dict[str, str]]


EXECUTION_WORKFLOWS: List[ExecutionWorkflow] = [
    # -------------------------------------------------------------------------
    # 1. EXECUTION OF MONEY DECREES (ATTACHMENT & SALE)
    # -------------------------------------------------------------------------
    ExecutionWorkflow(
        id="money_decree",
        title="Execution of Money Decrees (Attachment & Sale)",
        decree_type="Money Decrees (Order XXI Rules 11, 30, 41, 43, 54, 64–94)",
        summary="Complete statutory roadmap to enforce a money decree through oral/written application, asset discovery, attachment of movable/immovable assets, and court auction.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXI Rule 11", "title": "Oral and written execution applications"},
            {"kind": "rule", "ref": "Order XXI Rule 22", "title": "Notice to show cause against execution"},
            {"kind": "rule", "ref": "Order XXI Rule 41", "title": "Examination of judgment debtor as to his property"},
            {"kind": "rule", "ref": "Order XXI Rule 54", "title": "Attachment of immovable property"},
            {"kind": "rule", "ref": "Order XXI Rule 58", "title": "Adjudication of claims to, or objections to attachment of, property"},
            {"kind": "rule", "ref": "Order XXI Rule 66", "title": "Proclamation of sale by public auction"},
            {"kind": "rule", "ref": "Order XXI Rule 89", "title": "Application to set aside sale on deposit"},
            {"kind": "rule", "ref": "Order XXI Rule 90", "title": "Application to set aside sale on ground of irregularity or fraud"},
            {"kind": "section", "ref": "Section 60", "title": "Property liable to attachment and sale in execution of decree"},
            {"kind": "limitation_article", "ref": "Article 136", "title": "Execution of any decree or order (12 years)"},
            {"kind": "limitation_article", "ref": "Article 127", "title": "To set aside a sale in execution of a decree (60 days)"}
        ],
        stages=[
            ExecutionStage(
                stage_number=1,
                title="Limitation Audit & Decree Preparation",
                governing_rules="Section 38, Order XXI Rule 11(3) CPC",
                limitation_period="12 Years (Article 136 Limitation Act) from date decree becomes enforceable",
                actions_required=[
                    "Obtain certified copy of decree and judgment from the registry.",
                    "Audit whether any appellate court stayed execution or modified the decree.",
                    "Verify if decree is enforceable immediately or upon happening of a condition."
                ],
                statutory_provisos=[
                    "Under Article 136, period is 12 years. If decree directs payment at certain dates, limitation runs from each default date."
                ],
                advocate_tactics="If approaching 12 years, file execution immediately to stop limitation. A pending execution petition keeps the decree alive."
            ),
            ExecutionStage(
                stage_number=2,
                title="Presentation of Execution Petition",
                governing_rules="Order XXI Rule 11(1), Rule 11(2) CPC",
                limitation_period="Within 12 years (Article 136)",
                actions_required=[
                    "If Judgment Debtor (JD) is present in court when decree is passed: make immediate oral application for arrest under Rule 11(1).",
                    "Otherwise, file formal 10-column Tabular Execution Petition under Rule 11(2) signed and verified by Decree Holder (DH).",
                    "Attach certified copy of decree (Rule 11(3)).",
                    "Specify exact mode of assistance: attachment of movables, bank accounts, immovables, or arrest."
                ],
                statutory_provisos=[
                    "Court registry will examine petition under Rule 17. Deficiencies must be cured within time fixed by court."
                ],
                advocate_tactics="Always include both attachment of assets AND arrest in Column 10 prayer to prevent JD from transferring property."
            ),
            ExecutionStage(
                stage_number=3,
                title="Notice to Judgment Debtor (When Mandatory)",
                governing_rules="Order XXI Rule 22 CPC",
                limitation_period="Notice required if > 2 years from decree date",
                actions_required=[
                    "If petition filed within 2 years of decree: court can issue process immediately without notice.",
                    "If petition filed MORE than 2 years after decree date: Court MUST issue show-cause notice under Rule 22.",
                    "If execution sought against legal representative of deceased JD: Rule 22 notice is mandatory."
                ],
                statutory_provisos=[
                    "Under Rule 22(2), court may dispense with notice if it would cause unreasonable delay or defeat the ends of justice (reasons to be recorded in writing)."
                ],
                advocate_tactics="If filing after 2 years, plead urgent grounds under Rule 22(2) for dispensing with notice if JD is attempting to liquidate bank accounts."
            ),
            ExecutionStage(
                stage_number=4,
                title="Discovery & Oral Examination of Assets",
                governing_rules="Order XXI Rule 41 CPC",
                limitation_period="At any time during execution",
                actions_required=[
                    "Where JD fails to satisfy decree: File application under Rule 41(1) for oral examination of JD.",
                    "Apply under Rule 41(2) directing JD to file an affidavit stating particulars of all his assets (bank accounts, shares, vehicles, immovables).",
                    "If JD disobeys order to attend or file affidavit: apply under Rule 41(3) for detention in civil prison up to 3 months."
                ],
                statutory_provisos=[
                    "Rule 41 is a potent coercive weapon: JD cannot evade disclosure of assets under oath."
                ],
                advocate_tactics="Move Rule 41 early if you do not have exact details of JD's bank accounts or property numbers. It compels disclosure under pain of prison."
            ),
            ExecutionStage(
                stage_number=5,
                title="Attachment of Judgment Debtor's Property",
                governing_rules="Order XXI Rules 43, 46, 48, 54 CPC r/w Section 60",
                limitation_period="Upon admission of execution petition",
                actions_required=[
                    "Movables in possession of JD: Seizure by court bailiff under Rule 43.",
                    "Debts, shares, bank accounts: Prohibitory order under Rule 46 / 46A Garnishee notice.",
                    "Salary of employee: Prohibitory order to employer under Rule 48 (Section 60(1)(i): first Rs. 1,000 and two-thirds of the remainder is exempt — only one-third of the remainder is attachable, or one-third of the entire salary for a maintenance decree).",
                    "Immovable Property: Prohibitory order under Rule 54 proclaimed by beat of drums and affixation at Collectorate and property."
                ],
                statutory_provisos=[
                    "STRICT SECTION 60 EXEMPTIONS: Necessary wearing apparel, cooking vessels, tools of artisans, books of accounts, pensions, and agricultural produce necessary for livelihood CANNOT be attached."
                ],
                advocate_tactics="For bank accounts, specify branch and account number if known, but a prohibitory order addressed to the Principal Officer / Branch Manager will freeze all accounts of the JD."
            ),
            ExecutionStage(
                stage_number=6,
                title="Adjudication of Claims & Third-Party Objections",
                governing_rules="Order XXI Rule 58 CPC",
                limitation_period="Must be raised without unreasonable delay before sale",
                actions_required=[
                    "If third party claims attached property is not liable to attachment: third party files objection u/r 58.",
                    "Court must adjudicate all questions of title, right, and interest arising between the parties under Rule 58(2).",
                    "No separate suit lies to contest the attachment (Rule 58(2) express bar)."
                ],
                statutory_provisos=[
                    "Under Rule 58(4), the order made by the court has the force of a DECREE and is appealable as a decree under Section 96 CPC."
                ],
                advocate_tactics="Check if objection is filed late after proclamation of sale. Court shall refuse to entertain claim under Rule 58(1) proviso if designedly delayed."
            ),
            ExecutionStage(
                stage_number=7,
                title="Proclamation of Sale & Public Auction",
                governing_rules="Order XXI Rules 64, 66, 68, 72 CPC",
                limitation_period="Notice of 15 days (immovable) / 7 days (movable) under Rule 68",
                actions_required=[
                    "Apply under Rule 64 for court order directing sale of attached property.",
                    "Court issues notice to both parties to settle terms of sale proclamation under Rule 66.",
                    "Proclamation must state: property to be sold, revenue assessed, encumbrances, and estimated value.",
                    "Apply under Rule 72 if Decree Holder wishes to participate in auction and bid (mandatory permission required)."
                ],
                statutory_provisos=[
                    "Under Rule 72A (mortgage suits), court will not grant DH leave to bid unless reserve price is fixed exceeding principal + interest + costs."
                ],
                advocate_tactics="Always obtain Rule 72 permission before auction so DH can bid and set off the purchase price against the decree amount."
            ),
            ExecutionStage(
                stage_number=8,
                title="Auction Bidding & Deposit Requirements",
                governing_rules="Order XXI Rules 84, 85, 86 CPC",
                limitation_period="25% immediately; balance within 15 days",
                actions_required=[
                    "Highest bidder declared purchaser by auction officer.",
                    "Purchaser must immediately deposit 25% of purchase money under Rule 84.",
                    "Balance 75% purchase money must be paid into court on or before the 15th day from sale under Rule 85."
                ],
                statutory_provisos=[
                    "Mandatory default rule under Rule 86: If balance not paid within 15 days, 25% deposit may be forfeited to Govt and property re-sold."
                ],
                advocate_tactics="If DH is permitted bidder under Rule 72, DH only pays the excess amount over the decree amount."
            ),
            ExecutionStage(
                stage_number=9,
                title="Setting Aside Sale / Final Confirmation & Sale Certificate",
                governing_rules="Order XXI Rules 89, 90, 92, 94 CPC r/w Article 127",
                limitation_period="Strict 60 Days (Article 127 Limitation Act) from date of sale",
                actions_required=[
                    "Rule 89: JD or interested person may apply to set aside sale upon depositing decree amount + 5% penalty payable to auction purchaser.",
                    "Rule 90: Application to set aside sale on ground of material irregularity or fraud in publishing or conducting sale.",
                    "If no application filed within 60 days (or application dismissed): Court makes order confirming sale under Rule 92.",
                    "Court grants Sale Certificate to purchaser under Rule 94 specifying property and date sale became absolute."
                ],
                statutory_provisos=[
                    "Sale becomes absolute on order under Rule 92. No separate suit lies to set aside an order made under Rule 92(3)."
                ],
                advocate_tactics="Sale certificate under Rule 94 is conclusive title document. Purchaser can apply under Rule 95 for delivery of possession within 1 year (Article 134)."
            )
        ]
    ),

    # -------------------------------------------------------------------------
    # 2. EXECUTION FOR DELIVERY OF IMMOVABLE PROPERTY (POSSESSION)
    # -------------------------------------------------------------------------
    ExecutionWorkflow(
        id="immovable_possession",
        title="Delivery of Immovable Property (Possession Decrees)",
        decree_type="Possession Decrees (Order XXI Rules 35, 36, 97–103)",
        summary="Procedural execution roadmap for enforcing decrees for delivery of physical possession of land, houses, or buildings, handling resistance, police aid, and third-party claims.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXI Rule 35", "title": "Decree for immovable property (actual possession)"},
            {"kind": "rule", "ref": "Order XXI Rule 36", "title": "Decree for delivery of immovable property when in occupancy of tenant"},
            {"kind": "rule", "ref": "Order XXI Rule 97", "title": "Resistance or obstruction to possession of immovable property"},
            {"kind": "rule", "ref": "Order XXI Rule 99", "title": "Dispossession by decree-holder or purchaser"},
            {"kind": "rule", "ref": "Order XXI Rule 101", "title": "Question to be determined (treated as suit)"},
            {"kind": "limitation_article", "ref": "Article 128", "title": "For possession by one dispossessed in execution (30 days)"},
            {"kind": "limitation_article", "ref": "Article 129", "title": "For possession by DH or purchaser obstructed (30 days)"}
        ],
        stages=[
            ExecutionStage(
                stage_number=1,
                title="Filing Petition for Possession",
                governing_rules="Order XXI Rule 11(2), Rule 35 CPC",
                limitation_period="12 Years (Article 136 Limitation Act)",
                actions_required=[
                    "File Execution Petition describing the property with identical boundaries as decree schedule.",
                    "Verify if possession sought is actual physical vacant possession (Rule 35(1)) or symbolic possession against tenant (Rule 36).",
                    "Attach certified copy of decree and site plan."
                ],
                statutory_provisos=[
                    "If boundary discrepancy exists between plaint and spot inspection, apply for appointment of Court Commissioner before warrant issuance."
                ],
                advocate_tactics="Ensure boundaries match the decree schedule verbatim to prevent bailiff returning warrant unexecuted due to identity dispute."
            ),
            ExecutionStage(
                stage_number=2,
                title="Issuance of Delivery Warrant",
                governing_rules="Order XXI Rule 35(1), (3) CPC",
                limitation_period="Within validity date of warrant (Rule 25)",
                actions_required=[
                    "Court issues Warrant of Delivery of Possession directing court bailiff to put DH in possession.",
                    "If property is locked: Apply for breaking open locks under Rule 35(3).",
                    "If female in purdah: Bailiff must give notice to withdraw under Rule 35(3) proviso before entry."
                ],
                statutory_provisos=[
                    "Bailiff has statutory authority to remove any person bound by the decree who refuses to vacate."
                ],
                advocate_tactics="Accompany the bailiff on the execution date with independent village/ward witnesses and a lock-smith."
            ),
            ExecutionStage(
                stage_number=3,
                title="Securing Police Aid (Section 151 Application)",
                governing_rules="Section 151 CPC r/w High Court Civil Rules of Practice",
                limitation_period="Prior to spot execution",
                actions_required=[
                    "Where JD holds out threats of violence, breach of peace, or organized resistance: File application under Section 151.",
                    "Plead specific facts of threat with police complaint details.",
                    "Court directs jurisdictional Station House Officer (SHO) to provide necessary police protection to bailiff."
                ],
                statutory_provisos=[
                    "Police aid cannot be granted mechanically — court must be satisfied of real threat of breach of peace."
                ],
                advocate_tactics="If previous delivery warrant returned with note 'resistance offered', produce bailiff endorsement as conclusive justification for police protection."
            ),
            ExecutionStage(
                stage_number=4,
                title="Handling Resistance / Obstruction (Rule 97 Application)",
                governing_rules="Order XXI Rule 97, 98, 101, 103 CPC",
                limitation_period="30 Days (Article 129 Limitation Act) from date of resistance",
                actions_required=[
                    "If resistance or obstruction offered by ANY person (whether JD or third party): DH files application under Rule 97.",
                    "State the date of obstruction and identity of resister.",
                    "Court shall proceed to adjudicate the application under Rule 101."
                ],
                statutory_provisos=[
                    "UNDER RULE 101: All questions relating to right, title, or interest arising between the parties MUST be determined by the executing court. NO SEPARATE SUIT LIES."
                ],
                advocate_tactics="Do not file a fresh suit against an obstructor. Rule 97 r/w Rule 101 is a full trial within execution, and the order has the force of a decree (Rule 103)."
            ),
            ExecutionStage(
                stage_number=5,
                title="Dispossession of Third Parties (Rule 99 Remedy)",
                governing_rules="Order XXI Rule 99, 100, 101 CPC",
                limitation_period="30 Days (Article 128 Limitation Act) from date of dispossession",
                actions_required=[
                    "If a third party (other than JD) is wrongfully dispossessed by DH: third party applies under Rule 99.",
                    "Court conducts trial under Rule 101 to determine if applicant has independent title/possession.",
                    "If bona fide title proved: court directs restoration of possession under Rule 100."
                ],
                statutory_provisos=[
                    "Transferee pendente lite from JD cannot maintain an application under Rule 99 (Order XXI Rule 102 express bar)."
                ],
                advocate_tactics="If resisting a Rule 99 application, check alienation date. If third party purchased after suit was filed, invoke Rule 102 to dismiss in limine."
            )
        ]
    ),

    # -------------------------------------------------------------------------
    # 3. SPECIFIC PERFORMANCE & INJUNCTION DECREES
    # -------------------------------------------------------------------------
    ExecutionWorkflow(
        id="injunction_decree",
        title="Execution of Injunction & Specific Performance Decrees",
        decree_type="Non-Monetary Injunctions & Conveyances (Order XXI Rules 32, 34)",
        summary="Enforcement mechanisms for mandatory and permanent injunctions, restitution of conjugal rights, and execution of sale deeds/conveyances by court on JD's default.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXI Rule 32", "title": "Decree for specific performance, for restitution of conjugal rights, or for an injunction"},
            {"kind": "rule", "ref": "Order XXI Rule 34", "title": "Decree for execution of document, or endorsement of negotiable instrument"},
            {"kind": "limitation_article", "ref": "Article 135", "title": "For the enforcement of a decree granting a mandatory injunction (3 years)"},
            {"kind": "limitation_article", "ref": "Article 136", "title": "Execution of decree for specific performance (12 years)"}
        ],
        stages=[
            ExecutionStage(
                stage_number=1,
                title="Specific Performance — Draft Conveyance Submission",
                governing_rules="Order XXI Rule 34(1), (2) CPC",
                limitation_period="12 Years (Article 136)",
                actions_required=[
                    "Deposit balance sale consideration into court in terms of the decree.",
                    "Prepare draft Sale Deed / conveyance and deliver to court.",
                    "Court serves draft conveyance on JD with notice inviting objections within prescribed time (Rule 34(2))."
                ],
                statutory_provisos=[
                    "If JD fails to file objections within time, court approves draft or amends as proper."
                ],
                advocate_tactics="Ensure stamp duty amount is calculated accurately under the relevant State Stamp Act before presenting the draft conveyance."
            ),
            ExecutionStage(
                stage_number=2,
                title="Execution of Conveyance by Judge",
                governing_rules="Order XXI Rule 34(4), (5) CPC",
                limitation_period="Upon approval of draft",
                actions_required=[
                    "DH tenders stamp paper of requisite value.",
                    "Presiding Judge executes the document in the format: 'C.D., Judge of the Court of ... (for A.B. in a suit by E.F. against A.B.)'.",
                    "Court sends deed for registration to the Sub-Registrar.",
                    "Registration operates as if executed by the party himself (Rule 34(5))."
                ],
                statutory_provisos=[
                    "Court's execution has identical legal efficacy as execution by the JD."
                ],
                advocate_tactics="Move for delivery of physical possession under Rule 35 in the same execution petition so title and possession are achieved together."
            ),
            ExecutionStage(
                stage_number=3,
                title="Injunction Breach Enforcement",
                governing_rules="Order XXI Rule 32(1), (5) CPC",
                limitation_period="Permanent Injunction: Article 136 (12 years) / Mandatory: Article 135 (3 years)",
                actions_required=[
                    "Where JD willfully fails to obey injunction decree: apply for attachment of JD's property.",
                    "Apply for detention of JD in civil prison for up to 3 months (Rule 32(1)).",
                    "Under Rule 32(5): Apply directing that the act required to be done may be done by DH or court commissioner at JD's expense."
                ],
                statutory_provisos=[
                    "Attachment of property under Rule 32 remains in force for 6 months. If disobedience continues, property may be sold to compensate DH (Rule 32(3))."
                ],
                advocate_tactics="For mandatory injunctions (e.g. demolish wall, remove encroachment), Rule 32(5) is the most effective remedy — court appoints commissioner with police aid to demolish at JD's cost."
            )
        ]
    ),

    # -------------------------------------------------------------------------
    # 4. GARNISHEE PROCEEDINGS (THIRD-PARTY DEBTS)
    # -------------------------------------------------------------------------
    ExecutionWorkflow(
        id="garnishee_proceedings",
        title="Garnishee Proceedings (Third-Party Debts & Bank Balances)",
        decree_type="Debts, Balances & Deposits in Hands of Third Parties (Order XXI Rules 46A–46I)",
        summary="Direct statutory process compelling third parties (banks, employers, tenants, debtors of JD) to deposit funds directly into court toward decree satisfaction.",
        connected_provisions=[
            {"kind": "rule", "ref": "Order XXI Rule 46", "title": "Attachment of debt, share and other property not in possession"},
            {"kind": "rule", "ref": "Order XXI Rule 46A", "title": "Notice to garnishee"},
            {"kind": "rule", "ref": "Order XXI Rule 46B", "title": "Order against garnishee"},
            {"kind": "rule", "ref": "Order XXI Rule 46F", "title": "Payment by garnishee is valid discharge"}
        ],
        stages=[
            ExecutionStage(
                stage_number=1,
                title="Application for Garnishee Notice",
                governing_rules="Order XXI Rule 46A CPC",
                limitation_period="During pendency of money execution",
                actions_required=[
                    "Identify third party who owes money to JD (e.g. Bank where JD holds FD/savings, tenant paying rent, or debtor).",
                    "File application under Rule 46A for issuance of notice to Garnishee.",
                    "Notice calls upon Garnishee to pay debt into court or show cause why he should not do so."
                ],
                statutory_provisos=[
                    "Debt must be an existing legal debt due or accruing to the JD."
                ],
                advocate_tactics="File Rule 46A notice along with prohibitory order under Rule 46 to restrain the garnishee from releasing funds to JD pending hearing."
            ),
            ExecutionStage(
                stage_number=2,
                title="Order on Default or Failure to Show Cause",
                governing_rules="Order XXI Rule 46B CPC",
                limitation_period="On returnable date of notice",
                actions_required=[
                    "If Garnishee fails to pay money into court and does not appear to show cause: Court makes order directing execution against Garnishee.",
                    "Order executed against property of Garnishee as if it were a decree against him."
                ],
                statutory_provisos=[
                    "Garnishee who ignores court notice becomes personally liable to the decree amount."
                ],
                advocate_tactics="If the bank fails to file reply to 46A notice, move for issuance of attachment warrant directly against the bank's currency chest / property."
            ),
            ExecutionStage(
                stage_number=3,
                title="Trial of Disputed Debt & Statutory Discharge",
                governing_rules="Order XXI Rules 46C, 46F CPC",
                limitation_period="During inquiry",
                actions_required=[
                    "If Garnishee disputes liability: Court frames issues and tries the liability under Rule 46C as an issue in a suit.",
                    "Upon determination, court orders payment or discharges notice.",
                    "UNDER RULE 46F: Payment made by Garnishee into court operates as a FULL AND VALID DISCHARGE of his debt to the JD."
                ],
                statutory_provisos=[
                    "Under Rule 46H, any order passed under Rule 46B or 46C is appealable as a decree."
                ],
                advocate_tactics="Point out Rule 46F to reluctant garnishees: paying the court gives them absolute statutory immunity against any future claim by the JD."
            )
        ]
    ),

    # -------------------------------------------------------------------------
    # 5. ARREST & DETENTION IN CIVIL PRISON
    # -------------------------------------------------------------------------
    ExecutionWorkflow(
        id="arrest_detention",
        title="Arrest & Detention in Civil Prison",
        decree_type="Personal Coercion for Money Decrees (Section 51, 56, 58 & Order XXI Rules 37–40)",
        summary="Strict statutory procedure for personal arrest and civil imprisonment of defaulting judgment debtors, with statutory safeguards, means inquiries, and women's exemption.",
        connected_provisions=[
            {"kind": "section", "ref": "Section 51", "title": "Powers of Court to enforce execution"},
            {"kind": "section", "ref": "Section 56", "title": "Prohibition of arrest or detention of women in execution of decree for money"},
            {"kind": "section", "ref": "Section 58", "title": "Duration of detention and release"},
            {"kind": "rule", "ref": "Order XXI Rule 37", "title": "Discretionary power to permit judgment debtor to show cause against detention in prison"},
            {"kind": "rule", "ref": "Order XXI Rule 39", "title": "Subsistence allowance"},
            {"kind": "rule", "ref": "Order XXI Rule 40", "title": "Proceedings on appearance of judgment debtor"}
        ],
        stages=[
            ExecutionStage(
                stage_number=1,
                title="Pre-Condition Audit & Section 51 Proviso Test",
                governing_rules="Section 51 Proviso CPC, Jolly George Varghese Precedent",
                limitation_period="During execution",
                actions_required=[
                    "VERIFY SECTION 56 BAR: Women CANNOT be arrested or detained in civil prison for money decrees.",
                    "SATISFY SECTION 51 PROVISO: Must plead and prove that JD has: (a) intention to abscond; or (b) dishonestly transferred/concealed property; or (c) HAS THE MEANS to pay the decree amount and refuses or neglects to pay.",
                    "Poverty or bona fide inability to pay is NOT a ground for detention (Supreme Court: Jolly George Varghese)."
                ],
                statutory_provisos=[
                    "Article 21 & Jolly George Varghese (1980) 2 SCC 360: Mere non-payment without bad faith/means cannot deprive a citizen of personal liberty."
                ],
                advocate_tactics="Place documentary proof of JD's current income, lavish lifestyle, or ongoing business on record to prove 'means to pay' under Section 51(c)."
            ),
            ExecutionStage(
                stage_number=2,
                title="Show Cause Notice & Subsistence Allowance",
                governing_rules="Order XXI Rules 37, 39 CPC",
                limitation_period="Returnable date of notice",
                actions_required=[
                    "Court issues notice under Rule 37 requiring JD to appear and show cause why he should not be committed to civil prison.",
                    "(Court may issue arrest warrant directly only if satisfied by affidavit that JD is likely to abscond).",
                    "DECREE HOLDER MUST DEPOSIT SUBSISTENCE ALLOWANCE under Rule 39 in advance for JD's maintenance in prison as fixed by State Govt scale."
                ],
                statutory_provisos=[
                    "If DH fails to deposit subsistence allowance, JD must be released immediately (Rule 39(4))."
                ],
                advocate_tactics="Deposit subsistence allowance on the exact day ordered. Subsistence costs are added to the decree costs and recoverable from JD."
            ),
            ExecutionStage(
                stage_number=3,
                title="Inquiry on Appearance & Committal Order",
                governing_rules="Order XXI Rule 40 CPC r/w Section 58",
                limitation_period="Upon hearing JD",
                actions_required=[
                    "Court gives opportunity to JD to show cause why he should not be detained.",
                    "If court is satisfied of conditions under Section 51, court issues warrant of committal to civil prison.",
                    "SECTION 58 DURATION LIMITS:",
                    "  - Decree amount > Rs. 5,000: Detention up to 3 months maximum.",
                    "  - Decree amount Rs. 2,000 to Rs. 5,000: Detention up to 6 weeks.",
                    "  - Decree amount <= Rs. 2,000: NO detention permitted."
                ],
                statutory_provisos=[
                    "UNDER SECTION 58(2): Release of JD from civil prison does NOT discharge the debt. Decree remains executable against his property."
                ],
                advocate_tactics="Most JDs offer settlement or installment payments immediately upon warrant of arrest being issued to avoid incarceration."
            )
        ]
    )
]


def list_execution_workflows() -> List[ExecutionWorkflow]:
    return list(EXECUTION_WORKFLOWS)


def get_execution_workflow(workflow_id: str) -> Optional[ExecutionWorkflow]:
    for w in EXECUTION_WORKFLOWS:
        if w.id == workflow_id:
            return w
    return None
