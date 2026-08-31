"""
Specific Relief Act (SRA) 1963 — Practical Litigation Navigator & Relief Decision Engine.
Provides civil litigators with actionable strategic pathways, mandatory prayer audits,
proviso bars, fatal traps, limitation rules, and landmark Supreme Court precedents.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class SRAStrategyPathway:
    id: str
    title: str
    statutory_relief: str
    sra_provisions: str
    cpc_limitation_ref: str
    summary: str
    statutory_prerequisites: List[str]
    mandatory_prayers: List[Dict[str, str]]
    fatal_statutory_traps: List[Dict[str, str]]
    landmark_authorities: List[Dict[str, str]]
    defense_counter_tactics: List[str]
    court_fee_rules: str
    connected_provisions: List[Dict[str, str]]


SRA_PATHWAYS: List[SRAStrategyPathway] = [
    # -------------------------------------------------------------------------
    # PATHWAY 1: SPECIFIC PERFORMANCE OF CONTRACT
    # -------------------------------------------------------------------------
    SRAStrategyPathway(
        id="specific_performance_sec10",
        title="Specific Performance of Agreement of Sale (Sections 10, 16(c), 20 & 22)",
        statutory_relief="Specific Performance of Immovable Property Contract",
        sra_provisions="Sections 10, 14, 16(c), 20, 20A, 21, 22 SRA 1963",
        cpc_limitation_ref="Article 54 Limitation Act (3 Years); Order VII Rule 1 & Order VIII CPC",
        summary="Post-2018 mandatory statutory enforcement of contracts. Requires continuous proof of readiness and willingness, mandatory Section 22 prayers for possession and earnest refund, and compliance with Section 20 substituted performance notice.",
        statutory_prerequisites=[
            "Valid, subsisting written agreement with consensus ad idem on property identity, consideration, and completion terms.",
            "Continuous readiness (financial capacity) and willingness (mental eagerness) from the date of agreement up to the date of decree (Section 16(c)).",
            "Issuance of statutory notice calling upon the vendor to execute the sale deed upon tender of balance consideration within the stipulated date.",
            "Suit instituted within 3 years under Article 54 from date fixed for performance, or from date of refusal if no fixed date.",
            "Absence of substituted performance through third party under Section 20, and subject matter not an infrastructure project under Section 20A."
        ],
        mandatory_prayers=[
            {
                "prayer": "Decree for Specific Performance (Section 10)",
                "audit": "Directing defendant to execute and register proper sale deed upon receiving balance consideration, failing which court officer executes under Order XXI Rule 34."
            },
            {
                "prayer": "Delivery of Possession / Partition (Section 22(1)(a) MANDATORY)",
                "audit": "FATAL STATUTORY RULE: Under Section 22(2), no possession or partition relief shall be granted UNLESS SPECIFICALLY CLAIMED in the plaint. Must not be omitted!"
            },
            {
                "prayer": "Alternative Refund of Earnest Money & Charge (Section 22(1)(b) MANDATORY)",
                "audit": "In the alternative, decree for refund of earnest deposit with 18% p.a. interest, creating a statutory charge on suit property under Section 55(6)(b) Transfer of Property Act."
            },
            {
                "prayer": "Damages in Addition to Specific Performance (Section 21)",
                "audit": "Compensation for delay, loss of rental income, or escalation in construction costs incurred due to vendor's default."
            }
        ],
        fatal_statutory_traps=[
            {
                "trap": "Failure to Plead & Prove Financial Capacity (Section 16(c))",
                "explanation": "Pleading readiness without producing documentary proof of funds (bank statements, fixed deposits, loan sanction) on the crucial dates is fatal. SC in Sughar Singh (2021) and N.P. Thirugnanam (1995) held readiness is capacity to pay."
            },
            {
                "trap": "Omitting Section 22 Prayer for Possession",
                "explanation": "If plaintiff only asks for execution of sale deed without praying for possession, defendant in execution can object that decree did not grant possession. Requires an amendment under Section 22 proviso."
            },
            {
                "trap": "Determinable Contracts under Section 14(d)",
                "explanation": "Contracts containing a unilateral termination without cause clause are 'in their nature determinable' and cannot be specifically enforced under Section 14(d)."
            },
            {
                "trap": "Ignoring Section 20 Substituted Performance 30-Day Notice",
                "explanation": "If plaintiff engages a third contractor to complete work without giving 30 days prior written notice to defendant under Section 20(2), plaintiff loses right to recover costs and loses specific performance."
            }
        ],
        landmark_authorities=[
            {
                "case": "Sughar Singh v. Hari Singh (2021) 18 SCC 493 (SC)",
                "principle": "Post-2018 Amendment, Specific Performance is a mandatory statutory right and not a discretionary equitable relief. Court cannot deny relief on arbitrary grounds."
            },
            {
                "case": "N.P. Thirugnanam v. Dr. R. Jagan Mohan Rao (1995) 5 SCC 115 (SC)",
                "principle": "Readiness means continuous financial capacity to pay balance sale price; willingness means conduct showing intention to perform. Both must subsist through trial."
            },
            {
                "case": "Man Kaur v. Hartar Singh Sangha (2010) 10 SCC 512 (SC)",
                "principle": "Plaintiff must enter witness box personally to testify to readiness and willingness. Power of Attorney cannot testify to personal facts unknown to him."
            },
            {
                "case": "Babu Lal v. Hazari Lal Kishori Lal (1982) 1 SCC 525 (SC)",
                "principle": "Section 22 proviso is an enabling provision allowing plaintiff to amend plaint even at the execution stage to incorporate relief of possession."
            }
        ],
        defense_counter_tactics=[
            "Challenge Section 16(c) financial capacity: Serve Notice to Produce bank statements / passbooks for the relevant contract period.",
            "Set up Section 14(b) continuous supervision bar: If contract involves ongoing building development.",
            "Invoke Section 28 post-decree rescission: If plaintiff succeeds in decree but fails to deposit balance money within the court-stipulated window, vendor applies to rescind contract.",
            "Establish time was of essence: Prove market volatility, notices demanding completion, and buyer's deliberate procrastination."
        ],
        court_fee_rules="Computed under State Court Fees Act based on the agreed total consideration stated in the agreement of sale (ad valorem).",
        connected_provisions=[
            {"kind": "sra_section", "ref": "Section 10", "title": "Mandatory specific performance"},
            {"kind": "sra_section", "ref": "Section 16(c)", "title": "Proving readiness & willingness"},
            {"kind": "sra_section", "ref": "Section 22", "title": "Mandatory possession & refund prayers"},
            {"kind": "limitation_article", "ref": "Article 54", "title": "3-Year limitation period"},
            {"kind": "template", "ref": "plaint_specific_performance", "title": "Plaint for Specific Performance"}
        ]
    ),

    # -------------------------------------------------------------------------
    # PATHWAY 2: DECLARATION OF TITLE & STATUS
    # -------------------------------------------------------------------------
    SRAStrategyPathway(
        id="declaration_sec34",
        title="Declaratory Suits & The Section 34 Proviso Bar (Sections 34 & 35)",
        statutory_relief="Declaration of Legal Character or Proprietary Title",
        sra_provisions="Sections 34 & 35 SRA 1963",
        cpc_limitation_ref="Article 58 Limitation Act (3 Years); Section 9 & Order VII CPC",
        summary="Discretionary declaration of legal status or property ownership. Subject to the fatal Section 34 Proviso bar: a suit for mere declaration WITHOUT seeking consequential possession is liable to immediate dismissal.",
        statutory_prerequisites=[
            "Plaintiff must possess a present, existing legal character or right to specific property.",
            "Defendant must have explicitly denied or be interested in denying plaintiff's title/character.",
            "Plaintiff MUST seek further/consequential relief (possession, injunction, partition) if able to do so (Section 34 Proviso).",
            "Suit must be instituted within 3 years under Article 58 from when right to sue first accrued."
        ],
        mandatory_prayers=[
            {
                "prayer": "Declaration of Title (Section 34)",
                "audit": "Decree declaring plaintiff absolute and exclusive owner of the suit property."
            },
            {
                "prayer": "Consequential Recovery of Possession (Section 34 PROVISO COMPLIANCE)",
                "audit": "FATAL PROVISO MANDATE: If plaintiff is out of possession, plaintiff MUST seek recovery of possession. A pure declaration is barred by Section 34 Proviso!"
            },
            {
                "prayer": "Consequential Perpetual Injunction (Section 38)",
                "audit": "If plaintiff is in possession, consequential injunction restraining defendant from interfering with peaceful possession."
            },
            {
                "prayer": "Mesne Profits & Account (Order XX Rule 12 CPC)",
                "audit": "Determination of past and future mesne profits from defendant's illegal occupation."
            }
        ],
        fatal_statutory_traps=[
            {
                "trap": "The Section 34 Proviso Fatal Bar",
                "explanation": "Where defendant is in actual physical possession and plaintiff sues only for declaration of title without praying for possession, the suit is incompetent and barred by law. (Ram Saran v. Ganga Devi, SC)."
            },
            {
                "trap": "Suit Against Non-Interested Parties",
                "explanation": "Declaration cannot be claimed against a person who has never denied or had interest to deny title; plaint must aver hostile overt act."
            },
            {
                "trap": "Negative Declarations Bar",
                "explanation": "Courts will not grant purely negative declarations that defendant is NOT the owner or has no title, unless plaintiff establishes his own positive title."
            }
        ],
        landmark_authorities=[
            {
                "case": "Ram Saran v. Ganga Devi (1973) 2 SCC 60 (SC - 3 Judge Bench)",
                "principle": "Where defendant was in possession of some of the suit properties and plaintiff was in a position to claim possession but omitted to do so, suit for mere declaration of title is barred by Section 34 Proviso."
            },
            {
                "case": "Venkataraja v. Vidyane Doureradjaperumal (2014) 14 SCC 502 (SC)",
                "principle": "The purpose of Section 34 Proviso is to prevent multiplicity of proceedings by forcing plaintiff to claim all reliefs flowing from the title in a single suit."
            },
            {
                "case": "Anathula Sudhakar v. P. Buchi Reddy (2008) 4 SCC 594 (SC)",
                "principle": "Where title is cloud-free and plaintiff is in lawful possession, simple injunction suit lies. But where title is disputed and plaintiff is not in de facto possession, suit must be for Declaration and Possession."
            }
        ],
        defense_counter_tactics=[
            "Plead Section 34 Proviso Bar: Demonstrate defendant is in physical possession and plaintiff failed to pray for possession.",
            "Plead Article 58 Limitation Bar: Prove cloud on title was cast more than 3 years before institution (e.g. through earlier mutation or registered deed).",
            "Plead Adverse Possession: Establish open, hostile, continuous possession for 12+ years extinguishing plaintiff's title under Section 27 Limitation Act."
        ],
        court_fee_rules="If seeking declaration and possession, court fee is payable on market value under Section 25(a) / (b) of State Court Fees Act; if seeking pure declaration with injunction, under Section 25(d).",
        connected_provisions=[
            {"kind": "sra_section", "ref": "Section 34", "title": "Declaratory decrees"},
            {"kind": "sra_section", "ref": "Section 35", "title": "Effect of declaration"},
            {"kind": "limitation_article", "ref": "Article 58", "title": "3-Year limitation period"},
            {"kind": "template", "ref": "plaint_declaration_possession", "title": "Plaint for Declaration & Possession"}
        ]
    ),

    # -------------------------------------------------------------------------
    # PATHWAY 3: CANCELLATION OF INSTRUMENTS
    # -------------------------------------------------------------------------
    SRAStrategyPathway(
        id="cancellation_sec31",
        title="Cancellation of Void & Voidable Instruments (Sections 31, 32 & 33)",
        statutory_relief="Adjudging Instrument Void/Voidable & Delivery for Cancellation",
        sra_provisions="Sections 31, 32, 33 SRA 1963",
        cpc_limitation_ref="Article 59 Limitation Act (3 Years); Order VII CPC",
        summary="Equitable cancellation of deeds, contracts, and registered instruments. Distinguishes executants (must seek cancellation under Sec 31) from non-executants (need only seek declaration that deed is void).",
        statutory_prerequisites=[
            "Written instrument is void ab initio or voidable at plaintiff's option.",
            "Reasonable apprehension that if the instrument is left outstanding, it may cause plaintiff serious injury.",
            "Suit filed within 3 years under Article 59 from date facts entitling cancellation first became known.",
            "Plaintiff must be ready to restore any benefits received under the instrument under Section 33."
        ],
        mandatory_prayers=[
            {
                "prayer": "Cancellation of Instrument (Section 31(1))",
                "audit": "Decree adjudging sale deed / gift deed / release deed void or voidable and ordering it to be delivered up and cancelled."
            },
            {
                "prayer": "Intimation to Sub-Registrar (Section 31(2) MANDATORY FOR REGISTERED DEEDS)",
                "audit": "Mandatory statutory direction to court to send copy of decree to Sub-Registrar to record cancellation on book registers under Section 31(2)."
            },
            {
                "prayer": "Consequential Possession / Injunction",
                "audit": "Restoration of possession if defendant took possession under the impugned instrument."
            },
            {
                "prayer": "Partial Cancellation (Section 32)",
                "audit": "If instrument covers multiple rights/properties, praying for partial cancellation preserving valid portions."
            }
        ],
        fatal_statutory_traps=[
            {
                "trap": "The Suhrid Singh Court Fee & Prayer Trap",
                "explanation": "Executant of deed MUST seek cancellation under Sec 31 and pay ad valorem court fees on sale consideration. Non-executant need only seek declaration under Sec 34 paying fixed court fee (Suhrid Singh v. Randhir Singh)."
            },
            {
                "trap": "Section 33 Restitution of Benefits",
                "explanation": "Plaintiff who received advance/consideration under voidable contract cannot obtain cancellation without restoring benefit to opposite party."
            },
            {
                "trap": "Article 59 Limitation Starting Point",
                "explanation": "Clock starts from the date of knowledge of fraudulent instrument, not the date of execution; plaint must explicitly plead date of discovery."
            }
        ],
        landmark_authorities=[
            {
                "case": "Suhrid Singh @ Sardool Singh v. Randhir Singh (2010) 5 SCC 357 (SC)",
                "principle": "Executant of deed must seek cancellation under Section 31 SRA with ad valorem court fees. Non-executant seeking to establish deed is void/inoperative against his share needs only declaration under Section 34 with fixed court fees."
            },
            {
                "case": "Dahiben v. Arvindbhai Kalyanji Bhanusali (2020) 7 SCC 366 (SC)",
                "principle": "Non-payment of balance sale price does NOT render a registered sale deed void or voidable under Section 31; unpaid price is only a statutory charge under Sec 55(4)(b) TPA."
            },
            {
                "case": "Prem Singh v. Birbal (2006) 5 SCC 353 (SC)",
                "principle": "When a document is void ab initio, a decree for setting aside is not necessary, but Article 59 applies when cancellation is sought."
            }
        ],
        defense_counter_tactics=[
            "Invoke Dahiben rule: If cancellation sought for bounce of cheque or non-payment of balance price, move Order VII Rule 11 rejection as non-payment is not a ground for deed cancellation.",
            "Plead bona fide purchaser for value without notice: Third-party purchaser protected under Section 19(b) and Section 33.",
            "Plead Article 59 limitation bar: Establish plaintiff was present at registration or had constructive notice via public encumbrance certificate."
        ],
        court_fee_rules="If plaintiff is executant, ad valorem court fee on value stated in deed under Section 40 / 38 State Act; if non-executant, fixed court fee under Section 25(d).",
        connected_provisions=[
            {"kind": "sra_section", "ref": "Section 31", "title": "When cancellation may be ordered"},
            {"kind": "sra_section", "ref": "Section 33", "title": "Restoration of benefit"},
            {"kind": "limitation_article", "ref": "Article 59", "title": "3-Year limitation from knowledge"},
            {"kind": "template", "ref": "plaint_cancellation_deed", "title": "Plaint for Cancellation of Sale Deed"}
        ]
    ),

    # -------------------------------------------------------------------------
    # PATHWAY 4: SUMMARY DISPOSSESSION SUIT (SECTION 6)
    # -------------------------------------------------------------------------
    SRAStrategyPathway(
        id="summary_dispossession_sec6",
        title="Summary Possessory Suit within 6 Months (Section 6 SRA vs Section 5)",
        statutory_relief="Restoration of Dispossessed Possession without Proving Title",
        sra_provisions="Section 6 SRA 1963 (and Section 5 comparison)",
        cpc_limitation_ref="Section 6(2)(a) SRA (Strict 6 Months); Section 6(3) Bar on Appeals",
        summary="Swift summary possessory remedy for persons unlawfully dispossessed. Title is completely irrelevant; defendant cannot set up title in defense. No appeal or review lies. Strict 6-month limitation bar and cannot be brought against Government.",
        statutory_prerequisites=[
            "Plaintiff was in actual, peaceful, juridical physical possession of immovable property.",
            "Plaintiff was dispossessed WITHOUT consent otherwise than in due course of law.",
            "Suit instituted strictly within SIX MONTHS from the date of dispossession (Section 6(2)(a)).",
            "Dispossession was NOT caused by the Government (Section 6(2)(b))."
        ],
        mandatory_prayers=[
            {
                "prayer": "Summary Restoration of Possession (Section 6(1))",
                "audit": "Decree directing defendant to restore physical possession of suit property to plaintiff on basis of prior peaceful possession."
            },
            {
                "prayer": "Removal of Encroachments / Locks",
                "audit": "Mandatory direction to remove trespassing structures, locks, or padlocks placed during unlawful dispossession."
            },
            {
                "prayer": "Police Assistance for Possession",
                "audit": "Direction to jurisdictional police authorities to aid in execution of possession decree."
            }
        ],
        fatal_statutory_traps=[
            {
                "trap": "Filing After 6 Months Expiry",
                "explanation": "Section 6(2)(a) creates an absolute jurisdictional bar. Day 181 is fatal. After 6 months, suit can only be filed under regular civil law (Section 5 SRA & Article 64/65 Limitation Act)."
            },
            {
                "trap": "Suing the Government",
                "explanation": "Section 6(2)(b) expressly prohibits summary dispossession suits against Government / State authorities."
            },
            {
                "trap": "Attempting Appeals or Review",
                "explanation": "Under Section 6(3), NO appeal and NO review lies from an order or decree under Section 6. Only a Civil Revision Petition under Section 115 CPC is maintainable."
            },
            {
                "trap": "Mixing Title Pleas in Section 6 Plaint",
                "explanation": "Pleas of proprietary title confuse the trial court. Section 6 is strictly confined to possession and dispossession."
            }
        ],
        landmark_authorities=[
            {
                "case": "Lallu Yeshwant Singh v. Rao Jagdish Singh (1968) 2 SCR 203 (SC)",
                "principle": "Law respects possession even of a trespasser against everyone except the true owner. Even the true owner cannot dispossess by force; he must take recourse to due process of law."
            },
            {
                "case": "East India Hotels Ltd v. Syndicate Bank (1992) Supp (2) SCC 29 (SC)",
                "principle": "A person in juridical possession dispossessed without consent is entitled to summary restoration under Section 6 irrespective of any defect in his title."
            },
            {
                "case": "Sanjay Kumar Pandey v. Gulbahar Sheikh (2004) 4 SCC 664 (SC)",
                "principle": "Court in Section 6 suit will not adjudicate upon title. Decree under Section 6 does not bar unsuccessful party from subsequently establishing title under Section 6(4)."
            }
        ],
        defense_counter_tactics=[
            "Plead 6-month bar: Produce electricity bills, police FIRs, or photos showing dispossession occurred beyond 6 months.",
            "Establish voluntary surrender: Show tenant/occupant handed over keys voluntarily without force.",
            "File comprehensive Title Suit under Section 6(4): Section 6(4) specifically provides that Section 6 does not bar any person from suing to establish title.",
            "Establish suit is against Government: Move rejection under Section 6(2)(b) if municipality or state agency is impleaded."
        ],
        court_fee_rules="Payable at half the ad valorem rate prescribed for regular recovery of possession suits under State Court Fees Act.",
        connected_provisions=[
            {"kind": "sra_section", "ref": "Section 6", "title": "Summary suit by dispossessed person"},
            {"kind": "sra_section", "ref": "Section 5", "title": "Recovery based on title"},
            {"kind": "limitation_article", "ref": "Article 64", "title": "12-Year limitation for possession on previous possession"},
            {"kind": "section", "ref": "Section 115", "title": "Civil Revision (sole remedy against Sec 6 decree)"}
        ]
    ),

    # -------------------------------------------------------------------------
    # PATHWAY 5: PERPETUAL & MANDATORY INJUNCTIONS (SECTIONS 38, 39, 41)
    # -------------------------------------------------------------------------
    SRAStrategyPathway(
        id="injunctions_sec38_41",
        title="Perpetual & Mandatory Injunctions & Section 41 Statutory Bars",
        statutory_relief="Perpetual & Mandatory Injunctions against Breach of Obligation",
        sra_provisions="Sections 36, 37, 38, 39, 40, 41, 42 SRA 1963",
        cpc_limitation_ref="Article 113 Limitation Act (3 Years); Order XXXIX CPC",
        summary="Preventive and coercive equitable remedies. Subject to the 10 exhaustive statutory bars under Section 41 (restraining judicial proceedings, criminal matters, determinable contracts, equally efficacious remedies, infrastructure projects under 41(ha)).",
        statutory_prerequisites=[
            "Breach or threatened invasion of an obligation existing in plaintiff's favour (express or implied).",
            "No standard for ascertaining actual damage, or money compensation inadequate, or necessary to prevent multiplicity of proceedings (Section 38(3)).",
            "Absence of any of the 10 statutory prohibitions under Section 41.",
            "Plaintiff must come with clean hands and without personal disentitling conduct (Section 41(i))."
        ],
        mandatory_prayers=[
            {
                "prayer": "Perpetual Injunction (Section 38)",
                "audit": "Decree perpetually restraining defendant, their agents, and henchmen from interfering with peaceful possession and enjoyment."
            },
            {
                "prayer": "Mandatory Injunction (Section 39)",
                "audit": "Decree compelling defendant to demolish unauthorized encroachment or restore status quo ante."
            },
            {
                "prayer": "Damages in Addition to Injunction (Section 40 MANDATORY PRAYER)",
                "audit": "FATAL RULE: Under Section 40(2), no damages in lieu or in addition to injunction shall be granted UNLESS SPECIFICALLY CLAIMED in plaint."
            }
        ],
        fatal_statutory_traps=[
            {
                "trap": "The Section 41(h) Equally Efficacious Relief Bar",
                "explanation": "If plaintiff is out of possession or title is seriously clouded, an injunction suit is barred under Section 41(h) because 'equally efficacious relief' (Suit for Declaration and Possession) is available."
            },
            {
                "trap": "The Section 41(ha) Infrastructure Bar (2018 Amendment)",
                "explanation": "No court can grant an injunction impeding, delaying, or interfering with any infrastructure project specified in The Schedule (Roads, Metro, Airports, Power, Telecom, Affordable Housing)."
            },
            {
                "trap": "Section 41(a) & (b) Judicial Restraint Bar",
                "explanation": "Court cannot grant an injunction restraining a person from prosecuting a pending judicial proceeding or proceeding in a court not subordinate to it."
            },
            {
                "trap": "Section 41(i) Disentitling Conduct & Clean Hands",
                "explanation": "Plaintiff who suppresses material facts, encroaches on public land, or breaches terms is barred from injunction by virtue of Section 41(i)."
            }
        ],
        landmark_authorities=[
            {
                "case": "Anathula Sudhakar v. P. Buchi Reddy (2008) 4 SCC 594 (SC)",
                "principle": "Where defendant establishes cloud on plaintiff's title or disputes identity/boundaries, simple suit for permanent injunction is not maintainable. Plaintiff must sue for Declaration."
            },
            {
                "case": "Shiv Kumar Chadha v. Municipal Corporation of Delhi (1993) 3 SCC 161 (SC)",
                "principle": "Injunction is an equitable relief; person seeking it must come with clean hands. Suppression of notice or construction deviation disentitles injunction under Section 41(i)."
            },
            {
                "case": "Gujarat Bottling Co. Ltd v. Coca Cola Co. (1995) 5 SCC 545 (SC)",
                "principle": "Doctrine of clean hands: Court will examine whether plaintiff's conduct is fair, honest, and unblemished before granting equitable relief."
            }
        ],
        defense_counter_tactics=[
            "Plead Section 41(h): Demonstrate plaintiff is not in actual possession; suit for bare injunction is barred by Anathula Sudhakar.",
            "Invoke Section 41(ha): If dispute touches construction of highways, bridges, power lines, or telecom, move dismissal under Section 20A & 41(ha).",
            "Expose Section 41(i) clean hands violation: Show plaintiff suppressed earlier litigation, municipal show cause notices, or boundary violations.",
            "Invoke Section 41(e): If injunction seeks to enforce contract that cannot be specifically enforced under Section 14."
        ],
        court_fee_rules="Fixed court fee or ad valorem under Section 27 / 26 of State Court Fees Act depending on whether relief relates to immovable property.",
        connected_provisions=[
            {"kind": "sra_section", "ref": "Section 38", "title": "Perpetual injunction when granted"},
            {"kind": "sra_section", "ref": "Section 39", "title": "Mandatory injunctions"},
            {"kind": "sra_section", "ref": "Section 41", "title": "10-Clause statutory bars on injunction"},
            {"kind": "rule", "ref": "Order XXXIX Rule 1", "title": "Temporary injunctions regulated by CPC"},
            {"kind": "template", "ref": "injunction_o39_r1_2", "title": "Injunction Application & Affidavit"}
        ]
    )
]


def get_sra_pathway(pathway_id: str) -> Optional[SRAStrategyPathway]:
    for p in SRA_PATHWAYS:
        if p.id == pathway_id:
            return p
    return None


def list_sra_pathways() -> List[SRAStrategyPathway]:
    return SRA_PATHWAYS
