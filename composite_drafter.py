"""
Composite Multi-Statute Pleading Generator & Drafter Engine.
Merges provisions across the Code of Civil Procedure 1908, Specific Relief Act 1963,
The Limitation Act 1963, Transfer of Property Act 1882, Commercial Courts Act 2015,
and State Court Fees Acts into unified, court-tested hybrid legal drafts.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class StatutoryComponent:
    act_name: str
    provisions: str
    role_in_draft: str


@dataclass
class CompositePleading:
    id: str
    title: str
    remedy_type: str
    statutory_header: str
    summary: str
    statutes_merged: List[StatutoryComponent]
    mandatory_clauses: List[Dict[str, str]]
    default_parameters: Dict[str, str]
    template_text: str

    def generate(self, custom_params: Optional[Dict[str, str]] = None) -> str:
        params = dict(self.default_parameters)
        if custom_params:
            params.update({k: v for k, v in custom_params.items() if v})
        text = self.template_text
        for k, v in params.items():
            text = text.replace(f"[{k}]", str(v))
        return text


COMPOSITE_PLEADINGS: List[CompositePleading] = [
    # -------------------------------------------------------------------------
    # 1. SPECIFIC PERFORMANCE COMPOSITE PLAINT
    # -------------------------------------------------------------------------
    CompositePleading(
        id="composite_specific_performance",
        title="Composite Plaint for Specific Performance of Agreement of Sale",
        remedy_type="Substantive Contractual Enforcement & Title Conveyance",
        statutory_header="PLAINT UNDER SECTION 26 AND ORDER VII RULES 1 & 2 OF CPC, 1908 READ WITH SECTIONS 10, 16(c), 20 & 22 OF THE SPECIFIC RELIEF ACT, 1963, SECTION 55(6)(b) OF THE TRANSFER OF PROPERTY ACT, 1882 AND ARTICLE 54 OF THE LIMITATION ACT, 1963",
        summary="Unified composite plaint merging procedural presentation under CPC, post-2018 mandatory enforcement and readiness/willingness under SRA, statutory buyer charge under TPA, and limitation starting point under Article 54.",
        statutes_merged=[
            StatutoryComponent("Code of Civil Procedure, 1908", "Section 26 & Order VII Rules 1 & 2", "Governs institution of suit, plaint format, property schedule, and Order VI Rule 15 verification."),
            StatutoryComponent("The Specific Relief Act, 1963", "Sections 10, 16(c), 20 & 22", "Mandatory right to decree (Sec 10), continuous readiness & willingness plea (Sec 16(c)), substituted performance audit (Sec 20), and MANDATORY prayer for possession & earnest refund (Sec 22)."),
            StatutoryComponent("The Limitation Act, 1963", "Article 54", "Establishes 3-year limitation from date fixed for performance or from date of notice of refusal."),
            StatutoryComponent("Transfer of Property Act, 1882", "Section 55(6)(b)", "Statutory charge on the suit property in favour of purchaser for purchase-money properly paid in anticipation of delivery."),
            StatutoryComponent("State Court Fees Act", "Section 40 / 38 (Ad Valorem)", "Payment of court fee computed on the total agreed consideration stated in the contract.")
        ],
        mandatory_clauses=[
            {"clause": "Post-2018 Mandatory Specific Performance Plea", "requirement": "Averment that under Section 10 SRA (as substituted by Act 18 of 2018), specific performance is a mandatory statutory entitlement."},
            {"clause": "Continuous Readiness & Willingness (Sec 16(c))", "requirement": "Plea of continuous financial capacity and mental willingness from contract date to trial, producing documentary proof of funds."},
            {"clause": "Mandatory Section 22(1)(a) Possession Prayer", "requirement": "FATAL MANDATE: Must explicitly pray for delivery of physical possession; otherwise court cannot decree possession."},
            {"clause": "Mandatory Section 22(1)(b) Earnest Refund Prayer", "requirement": "Alternative prayer for refund of earnest deposit with 18% interest and statutory charge on suit property."},
            {"clause": "Article 54 Limitation Cause of Action Date", "requirement": "Specific averment of date fixed or date when defendant refused execution upon tender of balance money."}
        ],
        default_parameters={
            "COURT_NAME": "COURT OF THE PRINCIPAL SENIOR CIVIL JUDGE AT [CITY/DISTRICT]",
            "SUIT_NO": "O.S. NO. ________ OF 202[ ]",
            "PLAINTIFF_NAME": "[PLAINTIFF FULL NAME], S/o [FATHER NAME], Aged [ ] years, residing at [ADDRESS]",
            "DEFENDANT_NAME": "[DEFENDANT FULL NAME], S/o [FATHER NAME], Aged [ ] years, residing at [ADDRESS]",
            "AGREEMENT_DATE": "[DATE OF AGREEMENT OF SALE]",
            "TOTAL_CONSIDERATION": "Rs. [TOTAL SALE CONSIDERATION]/-",
            "ADVANCE_PAID": "Rs. [ADVANCE EARNEST AMOUNT PAID]/-",
            "BALANCE_PAYABLE": "Rs. [BALANCE CONSIDERATION PAYABLE]/-",
            "TARGET_DATE": "[DATE FIXED FOR EXECUTION IN AGREEMENT]",
            "NOTICE_DATE": "[DATE OF LEGAL DEMAND NOTICE]",
            "REFUSAL_DATE": "[DATE OF DEFENDANT'S REPLY / REFUSAL]",
            "PROPERTY_SCHEDULE": "[FULL PROPERTY DESCRIPTION: SURVEY NO., EXTENT, TOWNSHIP, AND FOUR BOUNDARIES: NORTH, SOUTH, EAST, WEST]",
            "VALUATION_AMOUNT": "[TOTAL SALE CONSIDERATION VALUE]",
            "COURT_FEE_PAID": "Rs. [AD VALOREM COURT FEE AMOUNT]/-"
        },
        template_text="""IN THE [COURT_NAME]
[SUIT_NO]

IN THE MATTER OF:
[PLAINTIFF_NAME]                                                          ... PLAINTIFF
VERSUS
[DEFENDANT_NAME]                                                          ... DEFENDANT

COMPOSITE PLAINT FOR SPECIFIC PERFORMANCE OF CONTRACT, POSSESSION AND REFUND
(FILED UNDER SECTION 26 AND ORDER VII RULES 1 & 2 OF CPC, 1908 READ WITH SECTIONS 10, 16(c), 20 & 22 OF THE SPECIFIC RELIEF ACT, 1963, SECTION 55(6)(b) OF THE TRANSFER OF PROPERTY ACT, 1882 AND ARTICLE 54 OF THE LIMITATION ACT, 1963)

The Plaintiff above-named respectfully submits as follows:

1. DESCRIPTION AND CAPACITY OF PARTIES:
That the Plaintiff is a law-abiding citizen residing at the address set forth in the cause title. The Defendant is the absolute owner of the immovable property more fully described in the Schedule hereunder (hereinafter referred to as the "Suit Property").

2. THE CONTRACT (SUBSTANTIVE RIGHT UNDER SECTION 10 SRA):
That on [AGREEMENT_DATE], the Defendant entered into an Agreement of Sale in writing with the Plaintiff, agreeing to sell and convey the Suit Property absolutely and free from all encumbrances for a total consideration of [TOTAL_CONSIDERATION]. On the same date, the Plaintiff paid and the Defendant acknowledged receipt of [ADVANCE_PAID] as earnest money deposit. The balance consideration of [BALANCE_PAYABLE] was agreed to be paid on or before [TARGET_DATE] against execution and registration of the sale deed.

3. CONTINUOUS READINESS AND WILLINGNESS (SECTION 16(c) SRA COMPLIANCE):
That the Plaintiff has performed and has always been ready and willing to perform all essential terms of the contract on his part. The Plaintiff has continuously possessed the financial capacity and liquid funds to pay the balance consideration of [BALANCE_PAYABLE], as evidenced by his bank account statements / deposit certificates produced herewith. The Plaintiff has also been continuously willing and eager to have the sale deed registered in his favour.

4. BREACH BY DEFENDANT AND NOTICE:
That before the target date of [TARGET_DATE], the Plaintiff called upon the Defendant to receive the balance sale price and execute the deed. The Plaintiff caused a statutory Legal Notice dated [NOTICE_DATE] to be served upon the Defendant by Registered Post AD, tendering the balance amount. However, the Defendant, vide reply dated [REFUSAL_DATE] / by conduct, failed, refused, and neglected to execute the sale deed, thereby committing breach of the agreement.

5. STATUTORY REMEDY UNDER POST-2018 SRA:
That under Section 10 of the Specific Relief Act, 1963 (as substituted by Act 18 of 2018), specific performance of a contract is a mandatory statutory entitlement and the Court shall enforce the same. The contract does not fall under any of the barred categories in Section 14 or Section 16, nor does it relate to any infrastructure project in the Schedule under Section 20A.

6. MANDATORY PRAYERS UNDER SECTION 22 SRA & TPA CHARGE:
That in strict compliance with Section 22(1)(a) & (2) of the Specific Relief Act, 1963, the Plaintiff specifically claims the relief of delivery of physical possession of the Suit Property. Furthermore, under Section 22(1)(b) SRA and Section 55(6)(b) of the Transfer of Property Act, 1882, the Plaintiff is entitled in the alternative to refund of the earnest money paid with interest at 18% per annum with a statutory charge on the Suit Property.

7. LIMITATION PARAGRAPH (ARTICLE 54 LIMITATION ACT):
That the suit is instituted on [DATE], which is well within 3 years from [TARGET_DATE] (the date fixed for performance) and from [REFUSAL_DATE] (the date when performance was refused), fully satisfying Article 54 of the Limitation Act, 1963.

8. VALUATION AND COURT FEES:
The suit is valued for purpose of court fees and jurisdiction at [VALUATION_AMOUNT], being the total agreed sale consideration, and an ad valorem court fee of [COURT_FEE_PAID] is paid under the State Court Fees and Suits Valuation Act.

PRAYER:
Wherefore the Plaintiff respectfully prays that this Hon'ble Court may be pleased to pass a judgment and decree:
(a) Directing the Defendant to execute and register a proper Deed of Sale conveying the Suit Schedule Property in favour of the Plaintiff after receiving the balance sale consideration of [BALANCE_PAYABLE], within a timeframe fixed by this Hon'ble Court, failing which this Hon'ble Court may appoint an officer of the Court to execute and register the sale deed on behalf of the Defendant under Order XXI Rule 34 CPC;
(b) Directing the Defendant to deliver actual, physical, and vacant possession of the Suit Schedule Property to the Plaintiff under Section 22(1)(a) of the Specific Relief Act, 1963;
(c) IN THE ALTERNATIVE: in the event this Hon'ble Court refuses specific performance, passing a decree under Section 22(1)(b) SRA directing the Defendant to refund the earnest deposit of [ADVANCE_PAID] together with interest at 18% per annum from date of payment until realisation, creating a statutory charge on the Suit Schedule Property under Section 55(6)(b) of the Transfer of Property Act, 1882;
(d) Awarding compensation/damages under Section 21 of the Specific Relief Act, 1963 for delayed performance;
(e) Awarding full costs of this suit; and
(f) Granting such further and other reliefs as this Hon'ble Court deems fit and proper.

SCHEDULE OF IMMOVABLE PROPERTY
[PROPERTY_SCHEDULE]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF

VERIFICATION
I, [PLAINTIFF NAME], do hereby declare and verify that the contents of paragraphs 1 to 8 are true to my knowledge and paragraphs 9 to 10 are based on legal advice believed to be true.
Verified at [CITY] on this [DATE].

                                                        PLAINTIFF"""
    ),

    # -------------------------------------------------------------------------
    # 2. DECLARATION, POSSESSION & MESNE PROFITS COMPOSITE PLAINT
    # -------------------------------------------------------------------------
    CompositePleading(
        id="composite_declaration_possession",
        title="Composite Plaint for Declaration of Title, Possession & Mesne Profits",
        remedy_type="Proprietary Declaration & Ejectment with Mesne Inquest",
        statutory_header="PLAINT UNDER SECTION 26 AND ORDER VII RULES 1 & 2 OF CPC, 1908 READ WITH SECTIONS 5, 34 & 38 OF THE SPECIFIC RELIEF ACT, 1963, ORDER XX RULE 12 OF CPC, AND ARTICLES 58 & 65 OF THE LIMITATION ACT, 1963",
        summary="Composite plaint harmonizing declaration of title under Section 34 SRA, consequential recovery of possession under Section 5 SRA (complying strictly with Section 34 Proviso to prevent dismissal), mesne profits enquiry under Order XX Rule 12 CPC, and 12-year title limitation under Article 65.",
        statutes_merged=[
            StatutoryComponent("Code of Civil Procedure, 1908", "Section 26 & Order VII Rules 1-2, Order XX Rule 12", "Governs plaint presentation, boundaries under Order VII Rule 3, and mandatory procedure for inquiry into past and future mesne profits under Order XX Rule 12."),
            StatutoryComponent("The Specific Relief Act, 1963", "Sections 5, 34 (Proviso) & 38", "Declaration of title (Sec 34), recovery of possession according to CPC (Sec 5), compliance with Section 34 Proviso (omitting possession bars suit under Ram Saran v. Ganga Devi), and perpetual injunction (Sec 38)."),
            StatutoryComponent("The Limitation Act, 1963", "Articles 58 & 65, Section 27", "Article 58 (3 years for declaration from right to sue accrual) and Article 65 (12 years for possession based on proprietary title). Extinguishment of title under Section 27."),
            StatutoryComponent("State Court Fees Act", "Section 25(a) / (b)", "Court fee computed on market value of property for composite relief of declaration and possession.")
        ],
        mandatory_clauses=[
            {"clause": "Legal Character / Title Chain", "requirement": "Establish absolute ownership through registered title deeds, parent documents, revenue patta/khata, and inheritance genealogy."},
            {"clause": "Hostile Overt Act & Denial Date", "requirement": "Plead the exact date when defendant set up a hostile title, encroached, or denied plaintiff's title."},
            {"clause": "Consequential Possession Prayer (Sec 34 Proviso)", "requirement": "FATAL PROVISO BAR: Must pray for recovery of physical possession to prevent threshold dismissal under Ram Saran v. Ganga Devi."},
            {"clause": "Order XX Rule 12 Mesne Profits Prayer", "requirement": "Explicit prayer directing inquiry into profits earned by defendant from illegal occupation."}
        ],
        default_parameters={
            "COURT_NAME": "COURT OF THE PRINCIPAL SENIOR CIVIL JUDGE / DISTRICT JUDGE AT [CITY]",
            "SUIT_NO": "O.S. NO. ________ OF 202[ ]",
            "PLAINTIFF_NAME": "[PLAINTIFF FULL NAME], S/o [FATHER NAME], residing at [ADDRESS]",
            "DEFENDANT_NAME": "[DEFENDANT FULL NAME], S/o [FATHER NAME], residing at [ADDRESS]",
            "TITLE_DEED_DETAILS": "Registered Sale Deed Doc. No. [ ] of [YEAR] registered at SRO [ ]",
            "ENCROACHMENT_DATE": "[DATE DEFENDANT ILLEGALLY ENCROACHED / DENIED TITLE]",
            "MARKET_VALUE": "Rs. [MARKET VALUE OF PROPERTY]/-",
            "MESNE_PROFITS_RATE": "Rs. [ESTIMATED MONTHLY RENTAL/MESNE PROFIT]/- per month",
            "PROPERTY_SCHEDULE": "[FULL PROPERTY DETAILS: SURVEY NO., REVENUE EXTENT, BOUNDARIES NORTH, SOUTH, EAST, WEST]",
            "COURT_FEE_PAID": "Rs. [COURT FEE AMOUNT]/-"
        },
        template_text="""IN THE [COURT_NAME]
[SUIT_NO]

IN THE MATTER OF:
[PLAINTIFF_NAME]                                                          ... PLAINTIFF
VERSUS
[DEFENDANT_NAME]                                                          ... DEFENDANT

COMPOSITE PLAINT FOR DECLARATION OF TITLE, RECOVERY OF POSSESSION, MESNE PROFITS AND PERPETUAL INJUNCTION
(UNDER SECTION 26 & ORDER VII RULES 1 & 2 CPC READ WITH SECTIONS 5, 34 & 38 OF SPECIFIC RELIEF ACT, 1963, ORDER XX RULE 12 CPC, AND ARTICLES 58 & 65 OF THE LIMITATION ACT, 1963)

The Plaintiff above-named respectfully submits as follows:

1. ABSOLUTE TITLE OF PLAINTIFF:
That the Plaintiff is the absolute, sole, and exclusive owner of the immovable property more fully described in the Schedule hereunder (hereinafter referred to as the "Suit Property"). The Plaintiff acquired valid and marketable title under [TITLE_DEED_DETAILS] for valuable consideration. Ever since the purchase, revenue records (Patta / Khata / Tax Receipts) have stood mutated in the Plaintiff's name.

2. HOSTILE DENIAL AND ILLEGAL DISPOSSESSION BY DEFENDANT:
That the Defendant, who has no right, title, or interest whatsoever in the Suit Property, cast a cloud on Plaintiff's ownership by creating false revenue representations. Furthermore, on [ENCROACHMENT_DATE], taking unlawful advantage of Plaintiff's temporary absence, the Defendant unlawfully and high-handedly trespassed into the Suit Property, erected a temporary fence, and dispossessed the Plaintiff without due process of law.

3. STRICT COMPLIANCE WITH SECTION 34 PROVISO OF SRA:
That the Plaintiff is aware of the mandatory statutory proviso to Section 34 of the Specific Relief Act, 1963 and the law laid down by the Hon'ble Supreme Court in Ram Saran v. Ganga Devi (1973) 2 SCC 60 and Anathula Sudhakar v. P. Buchi Reddy (2008) 4 SCC 594. Since the Defendant is in wrongful physical possession, the Plaintiff is seeking not merely a declaration of title, but ALSO the consequential substantive relief of recovery of possession under Section 5 SRA and Order XXI CPC, thereby completely avoiding the statutory bar of Section 34 Proviso.

4. CLAIM FOR MESNE PROFITS (ORDER XX RULE 12 CPC):
That the Defendant's possession from [ENCROACHMENT_DATE] is that of a rank trespasser. The Suit Property is capable of fetching [MESNE_PROFITS_RATE]. The Plaintiff is entitled to an inquiry into past and future mesne profits under Order XX Rule 12 CPC from the date of illegal occupation until restoration of actual possession.

5. LIMITATION (ARTICLES 58 & 65 LIMITATION ACT):
That the suit for declaration is within 3 years from [ENCROACHMENT_DATE] under Article 58, and the relief of possession based on proprietary title is well within 12 years under Article 65 of the Limitation Act, 1963. The Defendant has not perfected title by adverse possession.

6. VALUATION AND COURT FEES:
The Suit Property is valued for declaration and possession on the market value at [MARKET_VALUE] and court fee of [COURT_FEE_PAID] is paid under Section 25 of the State Court Fees Act.

PRAYER:
Wherefore the Plaintiff respectfully prays for a judgment and decree:
(a) Declaring that the Plaintiff is the absolute, sole, and exclusive owner of the Suit Schedule Property under Section 34 of the Specific Relief Act, 1963;
(b) Directing the Defendant to quit, vacate, and deliver actual, vacant, and physical possession of the Suit Schedule Property to the Plaintiff under Section 5 SRA and Order XXI Rule 35 CPC;
(c) Directing an inquiry into past and future mesne profits under Order XX Rule 12 CPC and passing a final decree against the Defendant for the sum found due with interest;
(d) Granting a perpetual injunction under Section 38 SRA restraining the Defendant from altering the nature of the property or creating third-party encumbrances;
(e) Awarding full costs of this suit; and
(f) Granting such other reliefs as deemed fit and proper.

SCHEDULE OF IMMOVABLE PROPERTY
[PROPERTY_SCHEDULE]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF

VERIFICATION
I, [PLAINTIFF NAME], verify that the contents of paragraphs 1 to 6 are true to my knowledge and paragraphs 7 to 8 are based on legal advice.
Verified at [CITY] on this [DATE].

                                                        PLAINTIFF"""
    ),

    # -------------------------------------------------------------------------
    # 3. CANCELLATION OF DEED COMPOSITE PLAINT
    # -------------------------------------------------------------------------
    CompositePleading(
        id="composite_cancellation_deed",
        title="Composite Plaint for Cancellation of Fraudulent Sale Deed",
        remedy_type="Annulment of Registered Instruments & Register Correction",
        statutory_header="PLAINT UNDER SECTION 26 AND ORDER VII RULES 1 & 2 OF CPC, 1908 READ WITH SECTIONS 31 & 33 OF THE SPECIFIC RELIEF ACT, 1963, SECTION 31(2) SRA FOR SUB-REGISTRAR INTIMATION, AND ARTICLE 59 OF THE LIMITATION ACT, 1963",
        summary="Composite plaint harmonizing instrument cancellation under Section 31 SRA, the Suhrid Singh executant court fee rules, mandatory decree transmission to Sub-Registrar under Section 31(2) SRA, and limitation from discovery of fraud under Article 59.",
        statutes_merged=[
            StatutoryComponent("Code of Civil Procedure, 1908", "Section 26 & Order VII Rules 1 & 2", "Regulates plaint presentation and cause of action averments."),
            StatutoryComponent("The Specific Relief Act, 1963", "Sections 31, 32 & 33", "Adjudging deed void/voidable, delivering up for cancellation (Sec 31(1)), mandatory statutory transmission of decree copy to Sub-Registrar (Sec 31(2)), and restitution of benefits (Sec 33)."),
            StatutoryComponent("The Limitation Act, 1963", "Article 59", "3-year limitation commencing strictly from when the facts entitling the plaintiff to have the instrument cancelled FIRST BECAME KNOWN to him."),
            StatutoryComponent("Indian Registration Act, 1908", "Section 17 & Book No. 1 Records", "Sub-Registrar's duty upon receiving Section 31(2) decree to endorse cancellation in official registration books.")
        ],
        mandatory_clauses=[
            {"clause": "The Suhrid Singh Executant Rule", "requirement": "Distinguish executant (must seek cancellation under Sec 31 with ad valorem fee) from non-executant (seeking declaration under Sec 34)."},
            {"clause": "Reasonable Apprehension of Serious Injury (Sec 31(1))", "requirement": "Specific averment that if the fraudulent instrument is left outstanding, it will cause serious cloud and injury to plaintiff's title."},
            {"clause": "Article 59 Discovery of Fraud Date", "requirement": "Specific averment stating the exact date of obtaining Encumbrance Certificate or knowledge of fraudulent deed."},
            {"clause": "Mandatory Section 31(2) Intimation Prayer", "requirement": "Prayer directing court to transmit decree copy to the registering Sub-Registrar to record cancellation in Book No. 1."}
        ],
        default_parameters={
            "COURT_NAME": "COURT OF THE PRINCIPAL SENIOR CIVIL JUDGE AT [CITY]",
            "SUIT_NO": "O.S. NO. ________ OF 202[ ]",
            "PLAINTIFF_NAME": "[PLAINTIFF FULL NAME], S/o [FATHER NAME], residing at [ADDRESS]",
            "DEFENDANT_NAME": "[DEFENDANT FULL NAME / PURCHASER & IMPOSTOR], residing at [ADDRESS]",
            "IMPUGNED_DEED_DETAILS": "Registered Sale Deed bearing Document No. [ ] of [YEAR] registered at SRO [ ]",
            "FRAUD_DESCRIPTION": "[BRIEFLY DESCRIBE FRAUD: E.G. IMPERSONATION / FORGED POWER OF ATTORNEY / FRAUDULENT MISREPRESENTATION]",
            "DATE_OF_KNOWLEDGE": "[DATE OF KNOWLEDGE VIA ENCUMBRANCE CERTIFICATE / POLICE COMPLAINT]",
            "PROPERTY_SCHEDULE": "[FULL PROPERTY DETAILS AND BOUNDARIES]",
            "DEED_VALUE": "Rs. [CONSIDERATION MENTIONED IN IMPUGNED DEED]/-",
            "COURT_FEE_PAID": "Rs. [COURT FEE AMOUNT]/-"
        },
        template_text="""IN THE [COURT_NAME]
[SUIT_NO]

IN THE MATTER OF:
[PLAINTIFF_NAME]                                                          ... PLAINTIFF
VERSUS
[DEFENDANT_NAME]                                                          ... DEFENDANT

COMPOSITE PLAINT FOR CANCELLATION OF REGISTERED SALE DEED, CORRECTION OF REGISTERS AND PERPETUAL INJUNCTION
(UNDER SECTION 26 & ORDER VII RULES 1 & 2 CPC READ WITH SECTIONS 31 & 33 OF THE SPECIFIC RELIEF ACT, 1963, SECTION 31(2) SRA AND ARTICLE 59 OF THE LIMITATION ACT, 1963)

The Plaintiff above-named respectfully submits as follows:

1. PLAINTIFF'S UNDISPUTED TITLE:
That the Plaintiff is the absolute owner in physical possession of the immovable property described in the Schedule hereunder (the "Suit Property"), having acquired it under valid registered instruments.

2. FRAUDULENT CREATION OF IMPUGNED INSTRUMENT:
That the Defendant, acting fraudulently and in collusion with impostors, created and registered [IMPUGNED_DEED_DETAILS], purporting to convey the Suit Property. The said instrument is vitiated by [FRAUD_DESCRIPTION]. The Plaintiff never executed the said instrument, never received any consideration, and never authorized any person to execute the same.

3. REASONABLE APPREHENSION OF SERIOUS INJURY (SECTION 31(1) SRA):
That the impugned Sale Deed is void ab initio, illegal, and fraudulent. If the said deed is left outstanding, there is reasonable and imminent apprehension that the Defendant will use it to alienate the property to third parties or create encumbrances, causing irreparable loss and serious injury to the Plaintiff's lawful title.

4. COMPLIANCE WITH SUHRID SINGH RULING:
That as settled by the Hon'ble Supreme Court in Suhrid Singh v. Randhir Singh (2010) 5 SCC 357, the Plaintiff is seeking cancellation of the deed under Section 31 of the Specific Relief Act, 1963 and has valued the relief and paid court fees accordingly.

5. MANDATORY DIRECTION TO SUB-REGISTRAR UNDER SECTION 31(2) SRA:
That under Section 31(2) of the Specific Relief Act, 1963, it is the statutory duty of this Hon'ble Court upon passing a decree of cancellation to send an official copy of its decree to the Sub-Registrar in whose office the instrument was registered, so that the fact of cancellation may be entered in Book No. 1.

6. LIMITATION (ARTICLE 59 LIMITATION ACT):
That the Plaintiff first obtained knowledge of the fraudulent registration on [DATE_OF_KNOWLEDGE] when applying for an Encumbrance Certificate. The suit is filed on [DATE], which is well within 3 years from the date of knowledge, strictly in accordance with Article 59 of the Limitation Act, 1963.

7. VALUATION AND COURT FEES:
Valued at [DEED_VALUE] and court fee of [COURT_FEE_PAID] is paid under the State Court Fees Act.

PRAYER:
Wherefore the Plaintiff prays for a judgment and decree:
(a) Adjudging that the Sale Deed dated [DATE] bearing Document No. [ ] registered at SRO [ ] is void ab initio, fraudulent, and ordering the same to be delivered up and cancelled under Section 31(1) of the Specific Relief Act, 1963;
(b) Directing this Hon'ble Court under Section 31(2) of the Specific Relief Act, 1963 to send a certified copy of the decree to the Sub-Registrar, [NAME OF SRO], with a direction to note the fact of cancellation in Book No. 1 and relevant register indexes;
(c) Granting a perpetual injunction under Section 38 SRA restraining the Defendant from asserting any rights under the impugned deed;
(d) Awarding full costs of this suit; and
(e) Granting such other reliefs as deemed fit and proper.

SCHEDULE OF IMMOVABLE PROPERTY
[PROPERTY_SCHEDULE]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR PLAINTIFF

VERIFICATION
I, [PLAINTIFF NAME], verify that the contents of paragraphs 1 to 7 are true to my knowledge and paragraphs 8 to 9 are based on legal advice.
Verified at [CITY] on this [DATE].

                                                        PLAINTIFF"""
    ),

    # -------------------------------------------------------------------------
    # 4. TEMPORARY INJUNCTION COMPOSITE APPLICATION
    # -------------------------------------------------------------------------
    CompositePleading(
        id="composite_temp_injunction",
        title="Composite Application for Temporary Injunction & Urgency Affidavit",
        remedy_type="Interlocutory Protective Order with Section 41 SRA Audit",
        statutory_header="APPLICATION UNDER ORDER XXXIX RULES 1 & 2 READ WITH SECTION 151 OF CPC, 1908 READ WITH SECTIONS 36, 37 & 38 OF THE SPECIFIC RELIEF ACT, 1963",
        summary="Composite interlocutory application harmonizing CPC Order XXXIX procedure, Section 37 SRA statutory mandate, 3-prong test (Dalpat Kumar), clean hands doctrine (Sec 41(i)), infrastructure non-interference audit (Sec 20A / 41(ha)), and Order XXXIX Rule 3 Proviso urgency affidavit.",
        statutes_merged=[
            StatutoryComponent("Code of Civil Procedure, 1908", "Order XXXIX Rules 1 & 2, Section 151", "Governs interlocutory injunction orders, restraining wasting/damaging of property, and Order XXXIX Rule 3A 30-day disposal mandate."),
            StatutoryComponent("The Specific Relief Act, 1963", "Sections 36, 37, 38, 41 & 20A", "Section 37 statutorily confirms temporary injunctions are regulated by CPC. Section 41 ensures absence of 10 statutory prohibitions. Section 20A / 41(ha) verifies dispute does not impede infrastructure projects."),
            StatutoryComponent("The Limitation Act, 1963", "N/A (Interlocutory)", "Interlocutory application during pendency of suit.")
        ],
        mandatory_clauses=[
            {"clause": "Prima Facie Case Demonstration", "requirement": "Detailed averment of lawful title / possession backed by documentary exhibits."},
            {"clause": "Irreparable Injury & Balance of Convenience", "requirement": "Pleading that monetary compensation is inadequate and greater hardship will result if relief is refused."},
            {"clause": "Section 41 Statutory Bar Audit", "requirement": "Averment that applicant has clean hands (41(i)), no equally efficacious remedy (41(h)), and no infrastructure delay (41(ha))."},
            {"clause": "Order XXXIX Rule 3 Proviso Urgency", "requirement": "Special urgency averment showing delay in giving notice would defeat the very purpose of injunction."}
        ],
        default_parameters={
            "COURT_NAME": "COURT OF THE [SENIOR CIVIL JUDGE / DISTRICT JUDGE] AT [CITY]",
            "SUIT_NO": "I.A. NO. _____ OF 202[ ] IN O.S. NO. _____ OF 202[ ]",
            "APPLICANT_NAME": "[APPLICANT / PLAINTIFF FULL NAME]",
            "RESPONDENT_NAME": "[RESPONDENT / DEFENDANT FULL NAME]",
            "ACTS_RESTRAINED": "[SPECIFIC ACTS TO BE RESTRAINED: E.G. INTERFERING WITH POSSESSION / ALIENATING / DEMOLISHING]",
            "IMMEDIATE_THREAT_DATE": "[DATE OF RECENT THREAT / ENCROACHMENT ATTEMPT]",
            "PROPERTY_SCHEDULE": "[FULL PROPERTY DETAILS AND BOUNDARIES]"
        },
        template_text="""IN THE [COURT_NAME]
[SUIT_NO]

IN THE MATTER OF:
[APPLICANT_NAME]                                                          ... APPLICANT / PLAINTIFF
VERSUS
[RESPONDENT_NAME]                                                         ... RESPONDENT / DEFENDANT

COMPOSITE APPLICATION FOR AD-INTERIM EX-PARTE TEMPORARY INJUNCTION
(UNDER ORDER XXXIX RULES 1 & 2 READ WITH SECTION 151 OF CPC, 1908 READ WITH SECTIONS 36, 37 & 38 OF THE SPECIFIC RELIEF ACT, 1963)

The Applicant / Plaintiff above-named respectfully submits as follows:

1. PENDENCY OF MAIN SUIT:
That the Applicant has instituted the above Original Suit for substantive reliefs in respect of the immovable property described in the Schedule hereunder (the "Suit Property"). The averments made in the accompanying Plaint may be read as part and parcel of this Application.

2. PRIMA FACIE CASE:
That the Applicant is the lawful owner in peaceful physical possession of the Suit Property. The registered title documents, tax assessment receipts, and photos demonstrate an overwhelming and unimpeachable prima facie case in favour of the Applicant.

3. BALANCE OF CONVENIENCE:
That the balance of convenience lies entirely in favour of granting an ad-interim injunction. The Applicant has been in long-standing enjoyment, whereas the Respondent has no right, title, or interest. If the status quo is altered, the Applicant will suffer catastrophic prejudice.

4. IRREPARABLE INJURY (SECTION 38(3) SRA TEST):
That on [IMMEDIATE_THREAT_DATE], the Respondent along with henchmen attempted to forcefully enter the property and threatened to [ACTS_RESTRAINED]. If an ad-interim injunction is not granted, the Respondent will succeed in creating third-party rights or changing the physical nature of the property, causing irreparable injury which cannot be compensated in money.

5. AUDIT OF STATUTORY BARS UNDER SECTION 41 & 20A SRA:
That this application strictly satisfies the statutory parameters of the Specific Relief Act, 1963:
(a) The Applicant has approached this Hon'ble Court with utmost clean hands without suppression of any facts, fully complying with Section 41(i) SRA;
(b) The subject matter does NOT involve any infrastructure project specified in the Schedule under Sections 20A & 41(ha) of the SRA;
(c) There is no equally efficacious alternative relief available under Section 41(h) SRA.

6. URGENCY UNDER ORDER XXXIX RULE 3 PROVISO:
That the object of granting the injunction would be completely defeated by the delay of issuing prior notice. The Respondent has openly proclaimed that he will execute encumbrances before summons can be served. The Applicant undertakes to comply strictly with the proviso to Order XXXIX Rule 3 CPC by delivering copies on the very same day.

PRAYER:
Wherefore the Applicant respectfully prays that this Hon'ble Court may be pleased to:
(a) Grant an ad-interim ex-parte temporary injunction restraining the Respondent, their agents, and henchmen from [ACTS_RESTRAINED] pending disposal of the suit;
(b) Grant police protection under Section 151 CPC to enforce the injunction; and
(c) Pass such further orders as this Hon'ble Court deems fit and proper.

SCHEDULE OF IMMOVABLE PROPERTY
[PROPERTY_SCHEDULE]

Place: [CITY]
Date: [DATE]
                                                        ADVOCATE FOR APPLICANT"""
    )
]


def list_composite_pleadings() -> List[CompositePleading]:
    return COMPOSITE_PLEADINGS


def get_composite_pleading(pleading_id: str) -> Optional[CompositePleading]:
    for p in COMPOSITE_PLEADINGS:
        if p.id == pleading_id:
            return p
    return None
