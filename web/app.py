"""
LexOffline — Web companion to the desktop app.
Flask application serving CPC 1908 & Limitation Act 1963 as read-only
server-rendered HTML. Reuses the same db.py / xref.py / state_amend.py /
deadlines.py modules as the desktop app — no code duplication.
"""
import sys
import os
from datetime import date, datetime

from flask import Flask, render_template, request, g, abort, redirect

# Add project root to path so we can import shared modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from db import ActDatabase
from xref import extract_refs, resolve_refs
from state_amend import KNOWN_STATES, states_present, text_for_state
import deadlines as dl

app = Flask(__name__)

DATABASE = os.path.join(os.path.dirname(__file__), '..', 'cpc_1908.db')


# ---------- DB lifecycle ----------

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = ActDatabase(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def row_to_dict(row):
    """Convert a sqlite3.Row to a plain dict (Jinja2 can't index Row objects)."""
    return dict(row) if row else None


def rows_to_dicts(rows):
    return [dict(r) for r in rows] if rows else []


# ---------- Routes ----------

@app.route('/')
def home():
    return render_template('home.html')


# --- CPC 1908 ---

@app.route('/cpc/sections')
def cpc_sections():
    db = get_db()
    parts_raw = db.sections_by_part()
    parts = {part: rows_to_dicts(sections) for part, sections in parts_raw.items()}
    return render_template('cpc_sections.html', parts=parts)


@app.route('/cpc/section/<int:id>')
def cpc_section(id):
    db = get_db()
    row = db.get_section(id)
    if not row:
        abort(404)

    section = row_to_dict(row)
    text = section['text']

    # Cross-references
    refs = extract_refs(text, self_kind='section', self_ref=section['section_no'])
    xrefs = resolve_refs(db, refs)

    # Linked Limitation articles
    limitation_links = rows_to_dicts(
        db.find_articles_for_cpc(f"Section {section['section_no']}")
    )

    # State amendments
    sa_blob = section.get('state_amendments') or ''
    available_states = states_present(sa_blob)
    selected_state = request.args.get('state')
    state_text = text_for_state(sa_blob, selected_state) if selected_state else ''

    title = f"CPC 1908 — Section {section['section_no']}: {section['title']}"

    return render_template('provision.html',
                           title=title,
                           body=text,
                           kind='section',
                           ref_id=id,
                           available_states=available_states,
                           selected_state=selected_state,
                           state_text=state_text,
                           xrefs=xrefs,
                           limitation_links=limitation_links)


@app.route('/cpc/orders')
def cpc_orders():
    db = get_db()
    orders = []
    for o in db.all_orders():
        od = row_to_dict(o)
        od['rules'] = rows_to_dicts(db.rules_for_order(od['id']))
        orders.append(od)
    return render_template('cpc_orders.html', orders=orders)


@app.route('/cpc/rule/<int:id>')
def cpc_rule(id):
    db = get_db()
    row = db.get_rule(id)
    if not row:
        abort(404)

    rule = row_to_dict(row)
    order = row_to_dict(db.get_order(rule['order_id']))
    text = rule['text']

    refs = extract_refs(text)
    xrefs = resolve_refs(db, refs)

    # Try both "Order XXI" and "Order XXI, Rule 54" patterns
    limitation_links = rows_to_dicts(
        db.find_articles_for_cpc(f"Order {order['order_no']}")
    )

    sa_blob = rule.get('state_amendments') or ''
    available_states = states_present(sa_blob)
    selected_state = request.args.get('state')
    state_text = text_for_state(sa_blob, selected_state) if selected_state else ''

    title = f"CPC 1908 — Order {order['order_no']} Rule {rule['rule_no']}: {rule['title']}"

    return render_template('provision.html',
                           title=title,
                           body=text,
                           kind='rule',
                           ref_id=id,
                           available_states=available_states,
                           selected_state=selected_state,
                           state_text=state_text,
                           xrefs=xrefs,
                           limitation_links=limitation_links)


@app.route('/cpc/appendix/<int:id>')
def cpc_appendix(id):
    db = get_db()
    row = db.get_appendix(id)
    if not row:
        abort(404)

    appendix = row_to_dict(row)
    title = f"CPC 1908 — Appendix {appendix['letter']}"

    return render_template('provision.html',
                           title=title,
                           body=appendix['text'],
                           kind='appendix',
                           ref_id=id,
                           available_states=[],
                           selected_state=None,
                           state_text='',
                           xrefs=[],
                           limitation_links=[])


# --- Limitation Act 1963 ---

@app.route('/limitation/sections')
def limitation_sections():
    db = get_db()
    parts_raw = db.limitation_sections_by_part()
    parts = {part: rows_to_dicts(rows) for part, rows in parts_raw.items()}
    return render_template('limitation_sections.html', parts=parts)


@app.route('/limitation/section/<int:id>')
def limitation_section(id):
    db = get_db()
    row = db.get_limitation_section(id)
    if not row:
        abort(404)

    section = row_to_dict(row)
    title = f"Limitation Act 1963 — Section {section['section_no']}: {section['title']}"

    return render_template('limitation_detail.html',
                           title=title,
                           kind='limitation_section',
                           body=section['text'],
                           article_data=None)


@app.route('/limitation/articles')
def limitation_articles():
    db = get_db()
    divs_raw = db.limitation_articles_by_division()
    # divs_raw is {division: {part: [Row, ...]}} — convert all Rows to dicts
    divisions = {}
    for div_name, part_map in divs_raw.items():
        divisions[div_name] = {}
        for part_name, articles in part_map.items():
            divisions[div_name][part_name] = rows_to_dicts(articles)
    return render_template('limitation_articles.html', divisions=divisions)


@app.route('/limitation/article/<int:id>')
def limitation_article(id):
    db = get_db()
    row = db.get_limitation_article(id)
    if not row:
        abort(404)

    article = row_to_dict(row)
    title = f"Limitation Act 1963 — Article {article['article_no']} ({article['period']})"

    article_data = {
        'division': article['division'],
        'part': article['part'],
        'description': article['description'],
        'period': article['period'],
        'time_begins': article['time_begins'],
        'cpc_ref': article.get('cpc_ref') or '',
    }

    return render_template('limitation_detail.html',
                           title=title,
                           kind='limitation_article',
                           body=None,
                           article_data=article_data)


# --- The Specific Relief Act, 1963 ---

@app.route('/sra/sections')
def sra_sections():
    db = get_db()
    parts_raw = db.sra_sections_by_part()
    parts = {}
    for part_name, secs in parts_raw.items():
        parts[part_name] = rows_to_dicts(secs)
    return render_template('sra_sections.html', parts=parts)


@app.route('/sra/section/<int:id>')
def sra_section(id):
    db = get_db()
    row = db.get_sra_section(id)
    if not row:
        abort(404)

    sec = row_to_dict(row)
    sec_no = sec['section_no']
    title = f"Specific Relief Act 1963 — Section {sec_no}: {sec['title']}"

    # Map connected provisions
    connected_links = []
    if sec_no in ('5', '6'):
        connected_links.extend([
            {"ref": "Order XXI", "title": "Execution of Decrees for Possession", "url": "/cpc/orders"},
            {"ref": "Article 64", "title": "Suit based on previous possession (12 years)", "url": "/limitation/articles"},
            {"ref": "Article 65", "title": "Suit for possession of immovable property based on title (12 years)", "url": "/limitation/articles"}
        ])
    elif sec_no in ('10', '14', '14A', '16', '20', '20A', '20B', '20C', '21', '22'):
        connected_links.extend([
            {"ref": "Article 54", "title": "Suit for specific performance of a contract (3 years)", "url": "/limitation/articles"},
            {"ref": "Template: Specific Performance Plaint", "title": "Standard Plaint for Specific Performance", "url": "/template/plaint_specific_performance"}
        ])
    elif sec_no in ('31', '32', '33'):
        connected_links.extend([
            {"ref": "Article 59", "title": "To cancel or set aside an instrument (3 years)", "url": "/limitation/articles"},
            {"ref": "Template: Cancellation of Deed", "title": "Plaint for Cancellation of Voidable Sale Deed", "url": "/template/plaint_cancellation_deed"}
        ])
    elif sec_no in ('34', '35'):
        connected_links.extend([
            {"ref": "Article 58", "title": "To obtain any other declaration (3 years)", "url": "/limitation/articles"},
            {"ref": "Template: Declaration of Title", "title": "Plaint for Declaration of Title & Possession", "url": "/template/plaint_declaration_possession"}
        ])
    elif sec_no in ('36', '37', '38', '39', '40', '41', '42'):
        connected_links.extend([
            {"ref": "Order XXXIX Rules 1 & 2", "title": "Temporary Injunctions", "url": "/cpc/orders"},
            {"ref": "Checklist: Order XXXIX", "title": "Temporary Injunction 3-Prong Statutory Test", "url": "/checklist/o39_r1_2"},
            {"ref": "Template: Temporary Injunction", "title": "Order XXXIX Application & Affidavit", "url": "/template/injunction_o39_r1_2"}
        ])

    return render_template('sra_detail.html',
                           section=sec,
                           title=title,
                           connected_links=connected_links)


import sra_navigator as sn

@app.route('/sra/analyzer')
def sra_analyzer():
    pathways = sn.list_sra_pathways()
    return render_template('sra_analyzer_index.html', pathways=pathways)


@app.route('/sra/analyzer/<pathway_id>')
def sra_analyzer_detail(pathway_id):
    pathway = sn.get_sra_pathway(pathway_id)
    if not pathway:
        abort(404)
    return render_template('sra_analyzer_detail.html', pathway=pathway)


# --- Multi-Statute Composite Drafter ---

import composite_drafter as cdraft

@app.route('/drafter')
def drafter_index():
    pleadings = cdraft.list_composite_pleadings()
    return render_template('drafter_index.html', pleadings=pleadings)


@app.route('/drafter/<draft_id>', methods=['GET', 'POST'])
def drafter_builder(draft_id):
    pleading = cdraft.get_composite_pleading(draft_id)
    if not pleading:
        abort(404)
    current_params = dict(pleading.default_parameters)
    source = request.form if request.method == 'POST' else request.args
    for k in current_params.keys():
        if k in source and source.get(k):
            current_params[k] = source.get(k)
    generated_text = pleading.generate(current_params)
    return render_template('drafter_builder.html',
                           pleading=pleading,
                           current_params=current_params,
                           generated_text=generated_text)


# --- Search ---

@app.route('/search')
def search():
    q = request.args.get('q', '').strip()
    results = []
    if q:
        db = get_db()
        results = rows_to_dicts(db.search(q))
    return render_template('search_results.html', query=q, results=results)


import checklists_data as cd

# --- Practice Checklists ---

@app.route('/checklists')
def checklists():
    selected_cat = request.args.get('category', '').strip()
    all_items = cd.list_checklists()
    from collections import Counter
    cat_counts = Counter(c.category for c in all_items)
    categories = cd.list_checklist_categories()
    category_list = [{"name": cat, "count": cat_counts.get(cat, 0)} for cat in categories]
    items = cd.list_checklists(category=selected_cat if selected_cat else None)
    return render_template('checklists_index.html',
                           categories=categories,
                           category_list=category_list,
                           total_count=len(all_items),
                           selected_category=selected_cat,
                           checklists=items)


@app.route('/checklist/<checklist_id>')
def checklist_detail(checklist_id):
    c = cd.get_checklist(checklist_id)
    if not c:
        abort(404)
    db = get_db()

    # Resolve connected provisions to web URLs
    resolved_links = []
    for cp in c.connected_provisions:
        ref_text = cp["ref"]
        url = None
        if "Section" in ref_text:
            s_no = ref_text.replace("Section", "").strip().split()[0]
            if cp.get("kind") == "limitation_section":
                row = db.get_limitation_section_by_no(s_no)
                if row:
                    url = f"/limitation/section/{row['id']}"
            else:
                row = db.get_section_by_no(s_no)
                if row:
                    url = f"/cpc/section/{row['id']}"
        elif "Article" in ref_text:
            a_no = ref_text.replace("Article", "").strip().split("(")[0].strip()
            row = db.find_article_by_no(a_no)
            if row:
                url = f"/limitation/article/{row['id']}"
        elif "Order" in ref_text and "Rule" in ref_text:
            parts = ref_text.replace("Order", "").split("Rule")
            o_no = parts[0].strip()
            r_no = parts[1].strip().split("(")[0].strip()
            row = db.find_rule_in_order(o_no, r_no)
            if row:
                url = f"/cpc/rule/{row['id']}"
        elif "Order" in ref_text:
            url = "/cpc/orders"

        resolved_links.append({
            "ref": cp["ref"],
            "title": cp.get("title", ""),
            "url": url
        })

    return render_template('checklist_detail.html',
                           checklist=c,
                           connected_links=resolved_links)


import templates_data as tdata

# --- Drafting Templates ---

@app.route('/templates')
def drafting_templates():
    selected_cat = request.args.get('category', '').strip()
    all_items = tdata.list_templates()
    from collections import Counter
    cat_counts = Counter(t.category for t in all_items)
    categories = tdata.list_template_categories()
    category_list = [{"name": cat, "count": cat_counts.get(cat, 0)} for cat in categories]
    items = tdata.list_templates(category=selected_cat if selected_cat else None)
    return render_template('templates_index.html',
                           categories=categories,
                           category_list=category_list,
                           total_count=len(all_items),
                           selected_category=selected_cat,
                           templates=items)


@app.route('/template/<template_id>')
def template_detail(template_id):
    t = tdata.get_template(template_id)
    if not t:
        abort(404)
    db = get_db()

    # Resolve connected provisions to web URLs
    resolved_links = []
    for cp in t.connected_provisions:
        ref_text = cp["ref"]
        url = None
        if "Section" in ref_text:
            s_no = ref_text.replace("Section", "").strip().split()[0]
            if cp.get("kind") == "limitation_section":
                row = db.get_limitation_section_by_no(s_no)
                if row:
                    url = f"/limitation/section/{row['id']}"
            else:
                row = db.get_section_by_no(s_no)
                if row:
                    url = f"/cpc/section/{row['id']}"
        elif "Article" in ref_text:
            a_no = ref_text.replace("Article", "").strip().split("(")[0].strip()
            row = db.find_article_by_no(a_no)
            if row:
                url = f"/limitation/article/{row['id']}"
        elif "Order" in ref_text and "Rule" in ref_text:
            parts = ref_text.replace("Order", "").split("Rule")
            o_no = parts[0].strip()
            r_no = parts[1].strip().split("(")[0].strip()
            row = db.find_rule_in_order(o_no, r_no)
            if row:
                url = f"/cpc/rule/{row['id']}"
        elif "Order" in ref_text:
            url = "/cpc/orders"

        resolved_links.append({
            "ref": cp["ref"],
            "title": cp.get("title", ""),
            "url": url
        })

    return render_template('template_detail.html',
                           template=t,
                           connected_links=resolved_links)


import execution_data as edata

# --- Order XXI Execution Navigator ---

@app.route('/execution')
def execution_index():
    workflows = edata.list_execution_workflows()
    return render_template('execution_index.html', workflows=workflows)


@app.route('/execution/<workflow_id>')
def execution_detail(workflow_id):
    w = edata.get_execution_workflow(workflow_id)
    if not w:
        abort(404)
    db = get_db()

    # Resolve connected provisions to web URLs
    resolved_links = []
    for cp in w.connected_provisions:
        ref_text = cp["ref"]
        url = None
        if "Section" in ref_text:
            s_no = ref_text.replace("Section", "").strip().split()[0]
            if cp.get("kind") == "limitation_section":
                row = db.get_limitation_section_by_no(s_no)
                if row:
                    url = f"/limitation/section/{row['id']}"
            else:
                row = db.get_section_by_no(s_no)
                if row:
                    url = f"/cpc/section/{row['id']}"
        elif "Article" in ref_text:
            a_no = ref_text.replace("Article", "").strip().split("(")[0].strip()
            row = db.find_article_by_no(a_no)
            if row:
                url = f"/limitation/article/{row['id']}"
        elif "Order" in ref_text and "Rule" in ref_text:
            parts = ref_text.replace("Order", "").split("Rule")
            o_no = parts[0].strip()
            r_no = parts[1].strip().split("(")[0].strip()
            row = db.find_rule_in_order(o_no, r_no)
            if row:
                url = f"/cpc/rule/{row['id']}"
        elif "Order" in ref_text:
            url = "/cpc/orders"

        resolved_links.append({
            "ref": cp["ref"],
            "title": cp.get("title", ""),
            "url": url
        })

    return render_template('execution_detail.html',
                           workflow=w,
                           connected_links=resolved_links)


import case_stages as cs

# --- Case Diary & Hearing Timeline Tracker ---

@app.route('/diary')
def diary_index():
    db = get_db()
    selected_stage = request.args.get('stage', '')
    cases_rows = db.all_cases(stage=selected_stage if selected_stage else None)
    cases = [dict(r) for r in cases_rows]
    upcoming_rows = db.upcoming_cases()
    upcoming = [dict(r) for r in upcoming_rows]
    return render_template('diary_index.html',
                           cases=cases,
                           upcoming=upcoming,
                           stages=cs.CIVIL_STAGES,
                           selected_stage=selected_stage)


@app.route('/diary/new', methods=['GET', 'POST'])
def diary_new():
    if request.method == 'POST':
        db = get_db()
        case_no = request.form.get('case_no', '').strip()
        court_name = request.form.get('court_name', '').strip()
        client_name = request.form.get('client_name', '').strip()
        client_role = request.form.get('client_role', 'Plaintiff').strip()
        opposite_party = request.form.get('opposite_party', '').strip()
        opposite_counsel = request.form.get('opposite_counsel', '').strip()
        stage = request.form.get('stage', cs.CIVIL_STAGES[0]).strip()
        next_date = request.form.get('next_date', '').strip()
        notes = request.form.get('notes', '').strip()

        if case_no and court_name and client_name:
            cid = db.add_case(case_no, court_name, client_name, client_role,
                              opposite_party, opposite_counsel, stage, next_date, notes)
            return redirect(f'/diary/case/{cid}')

    return render_template('diary_form.html', stages=cs.CIVIL_STAGES)


@app.route('/diary/case/<int:case_id>')
def diary_detail(case_id):
    db = get_db()
    c = db.get_case(case_id)
    if not c:
        abort(404)
    case_dict = dict(c)
    hearings_rows = db.hearings_for_case(case_id)
    hearings = [dict(h) for h in hearings_rows]
    advice = cs.suggest_statutory_deadline(case_dict['stage'])
    return render_template('diary_detail.html',
                           case=case_dict,
                           hearings=hearings,
                           advice=advice,
                           stages=cs.CIVIL_STAGES)


@app.route('/diary/case/<int:case_id>/hearing', methods=['POST'])
def diary_add_hearing(case_id):
    db = get_db()
    c = db.get_case(case_id)
    if not c:
        abort(404)
    hearing_date = request.form.get('hearing_date', '').strip()
    business_done = request.form.get('business_done', '').strip()
    next_date = request.form.get('next_date', '').strip()
    next_purpose = request.form.get('next_purpose', '').strip()
    new_stage = request.form.get('new_stage', '').strip()

    if hearing_date:
        db.add_hearing(case_id, hearing_date, business_done, next_date, next_purpose)
        if new_stage:
            db.update_case(case_id, c['case_no'], c['court_name'], c['client_name'],
                           c['client_role'], c['opposite_party'], c['opposite_counsel'],
                           new_stage, next_date or c['next_date'], c['notes'])

    return redirect(f'/diary/case/{case_id}')


@app.route('/diary/case/<int:case_id>/delete', methods=['POST'])
def diary_delete_case(case_id):
    db = get_db()
    db.delete_case(case_id)
    return redirect('/diary')



import limitation_data as ld




# --- Deadline Calculator ---

@app.route('/deadline')
def deadline():
    categories = dl.list_categories() + ["All 137 Limitation Act Articles"]
    all_rules = dl.list_rules()
    # Convert DeadlineRule dataclass instances to dicts for Jinja / JS
    rules_data = [
        {'key': r.key, 'label': r.label, 'provision': r.provision,
         'category': r.category, 'note': r.note or ''}
        for r in all_rules
    ]
    for a in ld.LIMITATION_ARTICLES:
        desc = a["description"].split("\n")[0][:70]
        label = f"Art. {a['article_no']} — {desc} ({a['period'].splitlines()[0]}{'...' if len(a['period'].splitlines()) > 1 else ''})"
        rules_data.append({
            'key': f"LIMART:{a['article_no']}",
            'label': label,
            'provision': f"Article {a['article_no']}",
            'category': "All 137 Limitation Act Articles",
            'note': a['time_begins']
        })

    result = None
    selected_rule = request.args.get('rule_key', '')
    trigger_date_str = request.args.get('trigger_date', '')
    excluded_days_str = request.args.get('excluded_days', '0')
    selected_category = request.args.get('category', '')
    court_holidays_str = request.args.get('court_holidays', '').strip()

    # Optional known court-closure dates beyond Sunday (state/High Court
    # specific — e.g. Pongal, Deepavali as observed by that jurisdiction).
    # Sunday is applied automatically regardless of this field; nothing
    # else is assumed closed unless the advocate states it.
    court_holidays = []
    holiday_parse_error = False
    if court_holidays_str:
        for tok in court_holidays_str.split(","):
            tok = tok.strip()
            if not tok:
                continue
            try:
                court_holidays.append(datetime.strptime(tok, '%Y-%m-%d').date())
            except ValueError:
                holiday_parse_error = True

    if selected_rule and trigger_date_str:
        try:
            trigger = datetime.strptime(trigger_date_str, '%Y-%m-%d').date()
            excluded = int(excluded_days_str) if excluded_days_str else 0
            if selected_rule.startswith("LIMART:"):
                art_no = selected_rule.split(":", 1)[1]
                article = next((a for a in ld.LIMITATION_ARTICLES if a["article_no"] == art_no), None)
                if article:
                    raw_art = dl.compute_limitation_article(trigger, article, excluded_days=excluded,
                                                             court_holidays=court_holidays)
                    options = raw_art["options"]
                    result = {
                        'is_limitation_article': True,
                        'article_no': article['article_no'],
                        'division': article['division'],
                        'part': article['part'],
                        'description': article['description'],
                        'time_begins': article['time_begins'],
                        'cpc_ref': article.get('cpc_ref') or '—',
                        'excluded_days': excluded,
                        'trigger_date': trigger.strftime('%d %B %Y'),
                        'options': [
                            {
                                'label': opt['label'],
                                'amount': opt['amount'],
                                'unit': opt['unit'],
                                'due_date': opt['due_date'].strftime('%d %B %Y (%A)'),
                                'section4_applied': opt['section4_applied'],
                                'pre_section4_due_date': opt['pre_section4_due_date'].strftime('%d %B %Y (%A)'),
                            }
                            for opt in options
                        ]
                    }
            else:
                raw = dl.compute(trigger, selected_rule, excluded_days=excluded,
                                 court_holidays=court_holidays)
                result = {
                    'is_limitation_article': False,
                    'due_date': raw['due_date'].strftime('%d %B %Y (%A)'),
                    'trigger_date': raw['trigger_date'].strftime('%d %B %Y'),
                    'period_str': raw['period_str'],
                    'excluded_days': raw['excluded_days'],
                    'provision': raw['rule'].provision,
                    'note': raw['rule'].note or '',
                    'days': raw['days'],
                    'section4_applied': raw['section4_applied'],
                    'pre_section4_due_date': raw['pre_section4_due_date'].strftime('%d %B %Y (%A)'),
                }
        except (ValueError, KeyError):
            result = None

    return render_template('deadline.html',
                           categories=categories,
                           rules=rules_data,
                           result=result,
                           selected_category=selected_category,
                           selected_rule=selected_rule,
                           trigger_date=trigger_date_str,
                           excluded_days=excluded_days_str,
                           court_holidays=court_holidays_str,
                           holiday_parse_error=holiday_parse_error)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
