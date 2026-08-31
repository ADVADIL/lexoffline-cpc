"""
Procedural Stages & Statutory Deadline Suggester for Civil Litigation.
Maps standard Indian civil court litigation stages to deterministic statutory
deadlines under the Code of Civil Procedure, 1908 and The Limitation Act, 1963.
"""
from dataclasses import dataclass
from datetime import date, timedelta
from typing import List, Dict, Optional


@dataclass
class StageDeadlineAdvice:
    stage: str
    statutory_rule: str
    period_str: str
    statutory_due_date: Optional[date]
    advice: str
    warning: str = ""


CIVIL_STAGES: List[str] = [
    "Plaint / Petition Filed (Awaiting Summons)",
    "Service of Summons (Awaiting Written Statement)",
    "Written Statement Filed (Awaiting Issues)",
    "Framing of Issues (Order XIV)",
    "Interlocutory Applications / Injunction (Order XXXIX)",
    "Plaintiff Evidence (PW-1 Cross-Examination)",
    "Defendant Evidence (DW-1 Cross-Examination)",
    "Final Arguments",
    "Pronouncement of Judgment / Decree (Order XX)",
    "Execution Proceedings (Order XXI)",
    "Caveat Lodged (Section 148A)",
    "Death of Party Reported (Order XXII)",
    "Civil Appeal Filed (Section 96 / 100)"
]


def suggest_statutory_deadline(stage: str, trigger_date: Optional[date] = None) -> StageDeadlineAdvice:
    """
    Given a litigation stage and an optional trigger date (e.g. date of summons service,
    death, or decree), computes the exact statutory due date and returns actionable
    statutory advice.
    """
    base_date = trigger_date or date.today()

    if stage == "Service of Summons (Awaiting Written Statement)":
        due_30 = base_date + timedelta(days=30)
        due_90 = base_date + timedelta(days=90)
        return StageDeadlineAdvice(
            stage=stage,
            statutory_rule="Order VIII Rule 1 CPC",
            period_str="30 Days (extendable up to 90 days)",
            statutory_due_date=due_30,
            advice=f"Defendant must file Written Statement within 30 days from summons service (by {due_30.strftime('%d %B %Y')}). If extension is sought, maximum outer limit is 90 days (by {due_90.strftime('%d %B %Y')}) with recorded reasons.",
            warning="Under commercial court provisions, the 120-day outer limit is mandatory and non-extendable."
        )

    elif stage == "Caveat Lodged (Section 148A)":
        due = base_date + timedelta(days=90)
        return StageDeadlineAdvice(
            stage=stage,
            statutory_rule="Section 148A(5) CPC",
            period_str="90 Days",
            statutory_due_date=due,
            advice=f"Caveat protection remains in force for exactly 90 days (expires on {due.strftime('%d %B %Y')}). If no suit/application has been instituted by then, lodge a fresh caveat on the 91st day.",
            warning="Opposite parties often deliberately wait for the 91st day to move an ex-parte injunction application."
        )

    elif stage == "Death of Party Reported (Order XXII)":
        due_lr = base_date + timedelta(days=90)
        due_abate = base_date + timedelta(days=150)
        return StageDeadlineAdvice(
            stage=stage,
            statutory_rule="Order XXII Rules 3 & 4 CPC r/w Article 120 Limitation Act",
            period_str="90 Days for LR Substitution",
            statutory_due_date=due_lr,
            advice=f"Application to bring Legal Representatives on record must be filed within 90 days from the date of death (by {due_lr.strftime('%d %B %Y')}). On day 91, the suit automatically abates.",
            warning=f"If abated, an application under Order XXII Rule 9 to set aside abatement must be made within 60 days of abatement (by {due_abate.strftime('%d %B %Y')} under Article 121)."
        )

    elif stage == "Interlocutory Applications / Injunction (Order XXXIX)":
        due_30 = base_date + timedelta(days=30)
        return StageDeadlineAdvice(
            stage=stage,
            statutory_rule="Order XXXIX Rule 3 Proviso & Rule 3A CPC",
            period_str="Same-day compliance & 30-day disposal",
            statutory_due_date=due_30,
            advice=f"If an ex-parte ad-interim injunction was granted, plaintiff must dispatch copies by registered post on the same day or next day and file an affidavit of compliance. Under Rule 3A, the court shall endeavour to dispose of the injunction application within 30 days (by {due_30.strftime('%d %B %Y')}).",
            warning="Failure to file the Rule 3 compliance affidavit entitles the defendant to seek vacation of injunction on this ground alone."
        )

    elif stage == "Pronouncement of Judgment / Decree (Order XX)":
        due_30 = base_date + timedelta(days=30)
        due_90 = base_date + timedelta(days=90)
        return StageDeadlineAdvice(
            stage=stage,
            statutory_rule="Section 96 CPC r/w Articles 116(a)/(b) Limitation Act",
            period_str="30 Days (District Court) / 90 Days (High Court)",
            statutory_due_date=due_30,
            advice=f"First Appeal to District Court must be filed within 30 days (by {due_30.strftime('%d %B %Y')}). Appeal to High Court within 90 days (by {due_90.strftime('%d %B %Y')}). Apply immediately for certified copies of judgment and decree.",
            warning="Under Section 12 of the Limitation Act, the time taken for obtaining certified copies is excluded from the calculation of the limitation period."
        )

    elif stage == "Framing of Issues (Order XIV)":
        due_15 = base_date + timedelta(days=15)
        return StageDeadlineAdvice(
            stage=stage,
            statutory_rule="Order XVI Rule 1 CPC",
            period_str="15 Days for List of Witnesses",
            statutory_due_date=due_15,
            advice=f"Parties must file a list of witnesses they propose to call within 15 days of the settlement of issues (by {due_15.strftime('%d %B %Y')}).",
            warning="Witnesses not on the list require leave of the court under Order XVI Rule 1(3)."
        )

    elif stage == "Execution Proceedings (Order XXI)":
        return StageDeadlineAdvice(
            stage=stage,
            statutory_rule="Order XXI Rule 11 & 22 CPC r/w Article 136 Limitation Act",
            period_str="12 Years",
            statutory_due_date=None,
            advice="Execution petition is maintainable for up to 12 years from the date decree became enforceable. If filed more than 2 years from decree date, mandatory notice under Rule 22 must be issued.",
            warning="Objections to execution under Section 47 must be determined by executing court, not by a separate suit."
        )

    else:
        return StageDeadlineAdvice(
            stage=stage,
            statutory_rule="Code of Civil Procedure, 1908",
            period_str="As fixed by Court",
            statutory_due_date=None,
            advice=f"Current stage: {stage}. Ensure all procedural filings, witness affidavits (Order XVIII Rule 4), or documentary evidence are filed before the next hearing date.",
            warning="Adjournments under Order XVII Rule 1 are restricted to a maximum of 3 times during the hearing of the suit."
        )
