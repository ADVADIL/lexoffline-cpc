"""
Advocate Litigation Brief & Case Strategy Workbench.
Unifies Case Strategy, Temporal Limitation Audits, Fatal Proviso Checks,
Mandatory Statutory Prayers, Practice Checklists, Court-Ready Composite Drafts,
and Chamber Case Diary into a single operative trial workspace.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import date, timedelta


@dataclass
class LitigationMatter:
    id: str
    title: str
    category: str
    forum: str
    governing_statutes: str
    cause_of_action_rule: str
    limitation_article: str
    limitation_period_str: str
    limitation_days: Optional[int]
    limitation_years: Optional[int]
    trigger_event: str
    fatal_statutory_traps: List[str]
    mandatory_prayers: List[str]
    statutory_preconditions: List[str]
    checklist_id: Optional[str]
    template_id: Optional[str]
    composite_draft_id: Optional[str]
    court_fee_rule: str
    required_documents: List[str]


LITIGATION_MATTERS: List[LitigationMatter] = [
    # 1. Specific Performance of Agreement of Sale
    LitigationMatter(
        id="specific_performance",
        title="Specific Performance of Immovable Property Agreement",
        category="Contract & Real Estate",
        forum="Civil Judge / Senior Civil Judge / District Judge (as per valuation)",
        governing_statutes="SRA 1963 (Sections 10, 16(c), 20, 22), CPC 1908 (Sec 26, Order VII), Limitation Act 1963 (Art. 54), TPA 1882 (Sec 55(6)(b))",
        cause_of_action_rule="Refusal to execute sale deed upon tender of balance sale consideration or expiry of date fixed for completion.",
        limitation_article="Article 54, Limitation Act 1963",
        limitation_period_str="3 Years",
        limitation_days=None,
        limitation_years=3,
        trigger_event="Date fixed for performance in contract, or if no date is fixed, when plaintiff has notice that performance is refused.",
        fatal_statutory_traps=[
            "Section 16(c) SRA Mandate: Failure to continuously plead and prove readiness (financial capacity) and willingness (mental readiness) from date of agreement up to decree (N.P. Thirugnanam).",
            "Section 22 SRA Fatal Omission: Failure to specifically pray for possession or refund of earnest money. Such relief CANNOT be granted unless specifically claimed in plaint.",
            "Section 20 SRA Substituted Performance: If buyer engages a third party without 30-day statutory written notice, right to specific performance is forfeited.",
            "Commercial/Infrastructure Bar: Injunction barred against infrastructure projects listed in SRA Schedule under Section 20A / 41(ha)."
        ],
        mandatory_prayers=[
            "Decree for Specific Performance directing defendant to execute and register sale deed receiving balance consideration.",
            "Order directing delivery of actual, physical possession of the suit property (Mandatory under Section 22(1)(a) SRA).",
            "Alternative prayer for refund of earnest money with 18% interest and statutory charge under Section 55(6)(b) TPA (Mandatory under Section 22(1)(b) SRA).",
            "Permanent injunction restraining alienation or encumbrance to third parties pending conveyance."
        ],
        statutory_preconditions=[
            "Written agreement of sale with clear identification of property and consideration.",
            "Issuance of registered legal notice tendering balance consideration.",
            "Readiness established via bank statements, fixed deposits, or loan sanction letters.",
            "Valuation slip and payment of ad valorem court fee on total agreement consideration."
        ],
        checklist_id="sra_sec16c_specific_performance",
        template_id="plaint_specific_performance",
        composite_draft_id="composite_specific_performance",
        court_fee_rule="Ad Valorem on the total consideration stated in the Agreement of Sale under State Court Fees Act.",
        required_documents=[
            "Original / Certified Copy of Agreement of Sale",
            "Receipts / Bank Statements proving earnest deposit payment",
            "Statutory Legal Notice with Postal Receipts and Tracking / Ack Cards",
            "Proof of financial capacity (Bank passbook / IT returns / FD certificates)",
            "Encumbrance Certificate (EC) showing current title"
        ]
    ),

    # 2. Declaration of Title, Possession & Mesne Profits
    LitigationMatter(
        id="declaration_title_possession",
        title="Declaration of Title, Recovery of Possession & Mesne Profits",
        category="Property & Title Dispute",
        forum="Civil Judge / Senior Civil Judge / District Judge (as per valuation)",
        governing_statutes="SRA 1963 (Sections 5, 34 Proviso, 38), CPC 1908 (Sec 26, Order VII, Order XX Rule 12), Limitation Act 1963 (Articles 58 & 65)",
        cause_of_action_rule="Hostile cloud cast on plaintiff's ownership title or unlawful dispossession by defendant claiming adverse possession.",
        limitation_article="Article 58 (Declaration - 3 Years) & Article 65 (Possession on Title - 12 Years)",
        limitation_period_str="3 Years (Declaration) / 12 Years (Possession)",
        limitation_days=None,
        limitation_years=12,
        trigger_event="Article 58: When right to sue first accrues (cloud cast). Article 65: When possession of defendant becomes adverse to plaintiff.",
        fatal_statutory_traps=[
            "Section 34 SRA Proviso Bar (FATAL): An owner who is out of possession CANNOT sue for bare declaration. Failure to seek consequential possession renders suit non-maintainable (Ram Saran v. Ganga Devi; Anathula Sudhakar).",
            "Separate Mesne Profits Enquiry: Failure to specifically invoke Order XX Rule 12 for past and future profits prevents recovery of mesne profits.",
            "Adverse Possession Defense: 12-year continuous, open, hostile, and uninterrupted possession by defendant may extinguish title under Section 27 Limitation Act."
        ],
        mandatory_prayers=[
            "Declaration that Plaintiff is the absolute and lawful owner of the suit schedule property.",
            "Decree directing Defendant to quit and deliver vacant physical possession to Plaintiff (Section 5 SRA & Section 34 Proviso).",
            "Direction for enquiry into mesne profits under Order XX Rule 12 CPC from dispossession until delivery.",
            "Perpetual injunction restraining defendant from interfering or altering property status."
        ],
        statutory_preconditions=[
            "Title deeds establishing uninterrupted chain of title for at least 30 years.",
            "Pleading specific date and manner in which cloud was cast on title.",
            "Specific description of property with 4 boundaries under Order VII Rule 3 CPC."
        ],
        checklist_id="sra_sec34_declaration_proviso",
        template_id="plaint_declaration_title",
        composite_draft_id="composite_declaration_possession",
        court_fee_rule="Ad Valorem on the market value of the property under Section 24/26 of State Court Fees Act.",
        required_documents=[
            "Original Sale Deed / Partition Deed / Gift Deed in favour of Plaintiff",
            "Prior Title Deeds (Parent Documents)",
            "Revenue Records (Pattas, Khata Certificates, RTC extracts)",
            "Tax Paid Receipts for past 12+ years",
            "Survey Sketch / Approved Layout Plan"
        ]
    ),

    # 3. Summary Possessory Suit (Section 6 SRA)
    LitigationMatter(
        id="summary_dispossession",
        title="Summary Possession by Dispossessed Person (Section 6 SRA)",
        category="Possessory Restoration",
        forum="Civil Judge / Senior Civil Judge (Jurisdictional Court)",
        governing_statutes="SRA 1963 (Section 6), CPC 1908 (Sec 26, Order VII Rules 1-3), Limitation Act (Section 6(2)(a) SRA Special 6-Month Bar)",
        cause_of_action_rule="Forceful dispossession of plaintiff without consent otherwise than in due course of law.",
        limitation_article="Section 6(2)(a) Specific Relief Act, 1963",
        limitation_period_str="Strict 6 Months",
        limitation_days=180,
        limitation_years=None,
        trigger_event="Exact date on which plaintiff was physically dispossessed from the property.",
        fatal_statutory_traps=[
            "Strict 6-Month Limitation Bar (Section 6(2)(a)): Suit MUST be filed within 6 months from dispossession. Not a single day can be condoned; Section 5 Limitation Act does NOT apply!",
            "Bar on Suing Government (Section 6(2)(b)): A Section 6 summary suit CANNOT be instituted against the Central or State Government.",
            "Title Defense is Irrelevant: Title cannot be raised or adjudicated under Section 6. Even true owner is liable to restore possession (Lallu Yeshwant Singh).",
            "No Appeal or Review (Section 6(3)): Decrees under Section 6 cannot be appealed or reviewed. Sole remedy is Section 115 Civil Revision before High Court."
        ],
        mandatory_prayers=[
            "Restoration of actual, physical possession of the suit property to plaintiff under Section 6 SRA.",
            "Police protection to execute warrant of possession.",
            "Costs of the suit."
        ],
        statutory_preconditions=[
            "Proof of actual, continuous physical possession immediately prior to dispossession.",
            "Pleading specific date and violent/unlawful manner of dispossession without court decree.",
            "Defendant is a private entity/individual and not Government."
        ],
        checklist_id="sra_sec6_summary_possession",
        template_id="sra_sec6_plaint",
        composite_draft_id="composite_summary_possession",
        court_fee_rule="Half of the ad valorem court fee payable in regular title suits.",
        required_documents=[
            "Utility receipts (Electricity, Water, LPG) showing physical occupancy up to dispossession date",
            "Police complaint / FIR / Endorsement regarding criminal trespass",
            "Photographs / CCTV footage of premises and locks",
            "Affidavits of adjoining neighbours affirming prior possession"
        ]
    ),

    # 4. Commercial Suit under Commercial Courts Act, 2015
    LitigationMatter(
        id="commercial_suit",
        title="Commercial Dispute Recovery (Commercial Courts Act, 2015)",
        category="Commercial Litigation",
        forum="Designated Commercial Court / Commercial Division of High Court",
        governing_statutes="Commercial Courts Act 2015 (Sections 2(1)(c), 12A, 15), CPC 1908 (Order VI Rule 15A, Order XI, Order XIII-A), SRA 1963",
        cause_of_action_rule="Breach of commercial contract, unpaid invoices, or commercial agreement failure.",
        limitation_article="Articles 54 / 55 / 113 Limitation Act (3 Years)",
        limitation_period_str="3 Years",
        limitation_days=None,
        limitation_years=3,
        trigger_event="Date of invoice default, contractual breach, or expiry of credit period.",
        fatal_statutory_traps=[
            "Mandatory Pre-Institution Mediation (Section 12A): Plaint MUST be rejected at threshold if filed without DLSA Non-Starter Report, unless urgent interim relief is genuinely prayed for (Patil Automation v. Rakheja Engineers (2022) 10 SCC 1).",
            "Mandatory Statement of Truth (Order VI Rule 15A): Verification MUST be by Statement of Truth on solemn affirmation. Plain verification is fatal.",
            "Specified Value Threshold: Must exceed Rs. 3,00,000/- as defined under Section 2(1)(i) and Section 12.",
            "Strict Document Disclosure (Order XI): All documents in power, possession or custody must be disclosed with plaint. Late filing requires leave with exemplary costs."
        ],
        mandatory_prayers=[
            "Decree directing defendant to pay principal commercial debt together with interest at contractual/commercial rate (18% p.a.).",
            "Actual legal costs under Section 35 CPC (Commercial amendments).",
            "Summary Judgment under Order XIII-A CPC in absence of real prospect of defense."
        ],
        statutory_preconditions=[
            "Dispute falls strictly within one of the sub-clauses of Section 2(1)(c).",
            "Specified value exceeds Rs. 3 Lakhs.",
            "Production of DLSA Non-Starter Report or urgent interim relief affidavit."
        ],
        checklist_id="commercial_suit_scrutiny",
        template_id="commercial_suit_plaint",
        composite_draft_id="composite_commercial_suit",
        court_fee_rule="Ad Valorem on the Specified Value under State Court Fees Act.",
        required_documents=[
            "DLSA Non-Starter Report under Section 12A",
            "Master Service Agreement / Purchase Order / Commercial Contract",
            "Tax Invoices, Delivery Challans & Transporter Receipts",
            "Ledger Statement with Certificate under Section 65B Indian Evidence Act",
            "Demand Notice and Defendant's Reply"
        ]
    ),

    # 5. Cancellation of Fraudulent Registered Deed
    LitigationMatter(
        id="cancellation_deed",
        title="Cancellation of Void / Fraudulent Registered Sale Deed",
        category="Property & Equity",
        forum="Civil Judge / Senior Civil Judge / District Judge",
        governing_statutes="SRA 1963 (Sections 31, 32, 33), CPC 1908 (Sec 26, Order VII), Limitation Act 1963 (Art. 59), Registration Act 1908",
        cause_of_action_rule="Execution or registration of fraudulent, forged, or voidable instrument creating reasonable apprehension of serious injury.",
        limitation_article="Article 59, Limitation Act 1963",
        limitation_period_str="3 Years",
        limitation_days=None,
        limitation_years=3,
        trigger_event="When the facts entitling the plaintiff to have the instrument cancelled or set aside first become known to him.",
        fatal_statutory_traps=[
            "Executant vs Non-Executant Distinction (Suhrid Singh v. Randhir Singh): An executant MUST seek cancellation and pay ad valorem court fee. A non-executant stranger needs only seek a declaration that the deed is void/non-est and pays fixed court fee.",
            "Reasonable Apprehension of Serious Injury: Must specifically plead why leaving the instrument outstanding causes grave prejudice (Section 31(1) SRA).",
            "Section 31(2) Mandatory Notification: Plaint MUST pray for transmission of copy of decree to Sub-Registrar to note cancellation in Book No. 1."
        ],
        mandatory_prayers=[
            "Decree adjudging the registered Sale Deed dated [ ] as fraudulent, null, void and cancelling the same under Section 31(1) SRA.",
            "Direction under Section 31(2) SRA to transmit copy of decree to Sub-Registrar to endorse cancellation in official registers.",
            "Permanent injunction restraining defendant from asserting rights under the impugned deed."
        ],
        statutory_preconditions=[
            "Certified copy of impugned registered document.",
            "Specific particulars of fraud/forgery pleaded under Order VI Rule 4 CPC.",
            "Pleading exact date of discovery of fraud to anchor Article 59 limitation."
        ],
        checklist_id="sra_sec34_declaration_proviso",
        template_id="plaint_declaration_title",
        composite_draft_id="composite_cancellation_deed",
        court_fee_rule="If plaintiff is executant: Ad valorem on consideration. If non-executant: Fixed declaratory fee (Suhrid Singh).",
        required_documents=[
            "Certified copy of the impugned fraudulent sale deed / document",
            "Genuine title deeds proving plaintiff's ownership",
            "Forensic handwriting / signature comparison report (if forgery)",
            "Police complaint / Encumbrance Certificate showing fraudulent entry"
        ]
    ),

    # 6. Rejection of Plaint Defense (Order VII Rule 11 CPC)
    LitigationMatter(
        id="rejection_plaint_o7r11",
        title="Rejection of Plaint at Threshold (Order VII Rule 11 CPC)",
        category="Defense & Interlocutory",
        forum="Trial Court seized of the Plaint",
        governing_statutes="CPC 1908 (Order VII Rule 11, Section 151), Limitation Act 1963 (Section 3), SRA 1963 (Section 34 Proviso / 41 Bars)",
        cause_of_action_rule="Plaint is barred by limitation, lacks cause of action, is undervalued, or barred by any statutory law.",
        limitation_article="Order VII Rule 11 can be filed at ANY stage prior to conclusion of trial (Saleem Bhai v. State of Maharashtra)",
        limitation_period_str="Any Stage Pre-Trial",
        limitation_days=None,
        limitation_years=None,
        trigger_event="Upon receipt of summons and inspection of plaint averments.",
        fatal_statutory_traps=[
            "Plaint Averments Demurrer Rule: The Court CANNOT look into the Written Statement or defendant's documents. Only the plaint averments and plaint documents can be considered (Dahiben v. Arvindbhai Kalyanji Bhanusali (2020) 7 SCC 366).",
            "No Partial Rejection (Madhav Prasad Aggarwal): A plaint CANNOT be rejected in part and retained in part against some defendants or some reliefs.",
            "Clever Drafting / Illusory Cause of Action: When clever drafting creates an illusory cause of action, court must nip it in the bud under T. Arivandandam."
        ],
        mandatory_prayers=[
            "Order rejecting the Plaint under Order VII Rule 11(a)/(d) CPC as barred by law / disclosing no cause of action.",
            "Exemplary costs under Section 35A CPC for vexatious litigation."
        ],
        statutory_preconditions=[
            "Demonstrate bar directly from four corners of the plaint itself.",
            "Cite specific statutory bar (e.g. Art. 54 Limitation, Section 34 SRA Proviso, Sec 80 CPC, Sec 12A Commercial Courts Act)."
        ],
        checklist_id="o7_r11",
        template_id="ia_o7_r11_rejection",
        composite_draft_id=None,
        court_fee_rule="Fixed interlocutory application court fee.",
        required_documents=[
            "Copy of Plaint and annexed documents served on defendant",
            "Chronological tabular timeline demonstrating limitation bar from plaint dates"
        ]
    ),

    # 7. Temporary Injunction (Order XXXIX Rules 1 & 2)
    LitigationMatter(
        id="temporary_injunction",
        title="Temporary Injunction & Ex-Parte Ad-Interim Protection",
        category="Interlocutory & Emergency Relief",
        forum="Trial Court seized of Suit",
        governing_statutes="CPC 1908 (Order XXXIX Rules 1, 2, 3, 3A, Sec 151), SRA 1963 (Sections 36, 37, 41 Bars, 20A / 41(ha))",
        cause_of_action_rule="Apprehension of waste, damage, alienation, or wrongful dispossession by defendant.",
        limitation_article="Order XXXIX Rule 3A — Endeavour to dispose within 30 days",
        limitation_period_str="30-Day Disposal",
        limitation_days=30,
        limitation_years=None,
        trigger_event="Imminent threat of dispossession, alienation, or construction.",
        fatal_statutory_traps=[
            "Order XXXIX Rule 3 Proviso (MANDATORY): If ex-parte interim injunction is obtained, applicant MUST deliver copy of plaint, application, affidavit and documents to opposite party by registered post on the SAME DAY and file an affidavit of compliance.",
            "Section 41 SRA Prohibitions: Injunction cannot be granted if equally efficacious relief is available (41(h)), to restrain judicial proceedings (41(a)), or against infrastructure projects (41(ha)).",
            "Vacation for Misleading Facts (Rule 4 Proviso): If injunction obtained by knowingly false or misleading statements, it MUST be vacated without exception."
        ],
        mandatory_prayers=[
            "Ad-interim ex-parte order of temporary injunction restraining defendant, agents, and workmen from alienating, encumbering or altering the suit property.",
            "Ad-interim temporary injunction restraining interference with peaceful physical possession."
        ],
        statutory_preconditions=[
            "Prima Facie Case (substantial question to be tried).",
            "Balance of Convenience in applicant's favour.",
            "Irreparable Injury not compensable in monetary damages (Dalpat Kumar v. Prahlad Singh)."
        ],
        checklist_id="o39_r1_2",
        template_id="ia_o39_r1_2_injunction",
        composite_draft_id="composite_temp_injunction",
        court_fee_rule="Fixed interlocutory application court fee.",
        required_documents=[
            "Photographs showing current status of property",
            "Police complaint regarding threatened trespass / demolition",
            "Affidavit in support of Interim Application"
        ]
    ),

    # 8. Condonation of Delay (Section 5 Limitation Act)
    LitigationMatter(
        id="condonation_delay",
        title="Condonation of Delay in Appeal / Application",
        category="Temporal Relief & Restoration",
        forum="Appellate Court / Trial Court",
        governing_statutes="Limitation Act 1963 (Section 5), CPC 1908 (Section 151, Order XLI Rule 3A, Order IX Rule 13, Order XXII Rule 9)",
        cause_of_action_rule="Inability to file appeal or application within the statutory limitation period due to sufficient cause.",
        limitation_article="Section 5 Limitation Act, 1963",
        limitation_period_str="Companion Application",
        limitation_days=None,
        limitation_years=None,
        trigger_event="Expiry of statutory limitation period for companion appeal/application.",
        fatal_statutory_traps=[
            "Section 5 Does NOT Apply to Suits: Section 5 applies ONLY to appeals and applications. It NEVER condones delay in filing an original suit (Section 5 opening words)!",
            "Order XLI Rule 3A Mandatory Procedure: An appeal presented after limitation period MUST be accompanied by an application for condonation of delay with affidavit explaining each day's delay.",
            "Collector Land Acquisition v. Katiji (1987): Substantial justice should prevail over technical considerations, but gross negligence, deliberate inaction, or mala fides will be fatal."
        ],
        mandatory_prayers=[
            "Order condoning the delay of [NUMBER] days in preferring the accompanying Appeal / Application.",
            "Admission of the accompanying proceeding on merits."
        ],
        statutory_preconditions=[
            "Mathematical computation of exact days of delay.",
            "Plausible day-to-day explanation backed by documentary evidence (medical certificates, copy application dates).",
            "Section 12 certified copy exclusion credit computed."
        ],
        checklist_id="o41_r1_5_appeal",
        template_id="condonation_delay_application",
        composite_draft_id="composite_condonation_delay",
        court_fee_rule="Fixed interlocutory application court fee.",
        required_documents=[
            "Certified copies of impugned judgment and decree",
            "Copy Application slips showing dates of application and delivery (Section 12)",
            "Medical records / Hospital discharge summaries (if illness cited)"
        ]
    )
]

MATTER_BY_ID = {m.id: m for m in LITIGATION_MATTERS}


def list_litigation_matters() -> List[LitigationMatter]:
    return LITIGATION_MATTERS


def get_litigation_matter(mid: str) -> Optional[LitigationMatter]:
    return MATTER_BY_ID.get(mid)


def audit_matter_limitation(matter: LitigationMatter, trigger_date: date, excluded_days: int = 0) -> Dict:
    """Compute deadline, elapsed time, and statutory bar status for a matter."""
    from deadlines import add_years
    base_due = None
    if matter.limitation_years:
        base_due = add_years(trigger_date, matter.limitation_years)
    elif matter.limitation_days:
        base_due = trigger_date + timedelta(days=matter.limitation_days)
    else:
        return {
            "has_fixed_deadline": False,
            "message": "Procedural application — to be filed at appropriate stage or companion with proceeding."
        }

    effective_due = base_due + timedelta(days=excluded_days)
    today = date.today()
    days_remaining = (effective_due - today).days
    is_barred = today > effective_due

    return {
        "has_fixed_deadline": True,
        "trigger_date": trigger_date,
        "base_due_date": base_due,
        "excluded_days": excluded_days,
        "effective_due_date": effective_due,
        "days_remaining": days_remaining,
        "is_time_barred": is_barred,
        "status_badge": "TIME-BARRED" if is_barred else ("URGENT" if days_remaining <= 15 else "IN-TIME"),
        "period_str": matter.limitation_period_str
    }
