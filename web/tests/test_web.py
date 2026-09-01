"""
Web application route tests for LexOffline.
Uses Flask's built-in test client — no server needed.
"""
import sys
import os

# Ensure project root is on path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from app import app


def _client():
    app.config['TESTING'] = True
    return app.test_client()


def test_home():
    resp = _client().get('/')
    assert resp.status_code == 200
    assert b'LexOffline' in resp.data


def test_cpc_sections():
    resp = _client().get('/cpc/sections')
    assert resp.status_code == 200
    assert b'Section' in resp.data


def test_cpc_section_detail():
    resp = _client().get('/cpc/section/1')
    assert resp.status_code == 200
    assert b'Section 1' in resp.data


def test_cpc_section_with_state_amendment():
    resp = _client().get('/cpc/section/50?state=Kerala')
    assert resp.status_code == 200


def test_cpc_orders():
    resp = _client().get('/cpc/orders')
    assert resp.status_code == 200
    assert b'Order' in resp.data


def test_cpc_rule_detail():
    resp = _client().get('/cpc/rule/1')
    assert resp.status_code == 200


def test_cpc_appendix():
    resp = _client().get('/cpc/appendix/1')
    assert resp.status_code == 200
    assert b'Appendix' in resp.data


def test_limitation_sections():
    resp = _client().get('/limitation/sections')
    assert resp.status_code == 200
    assert b'Limitation' in resp.data or b'Section' in resp.data


def test_limitation_section_detail():
    resp = _client().get('/limitation/section/1')
    assert resp.status_code == 200


def test_limitation_articles():
    resp = _client().get('/limitation/articles')
    assert resp.status_code == 200
    assert b'Article' in resp.data


def test_limitation_article_detail():
    resp = _client().get('/limitation/article/1')
    assert resp.status_code == 200


def test_search_injunction():
    resp = _client().get('/search?q=injunction')
    assert resp.status_code == 200
    assert b'injunction' in resp.data.lower()


def test_search_condonation():
    resp = _client().get('/search?q=condonation')
    assert resp.status_code == 200


def test_search_empty():
    resp = _client().get('/search')
    assert resp.status_code == 200


def test_deadline_form():
    resp = _client().get('/deadline')
    assert resp.status_code == 200
    assert b'Calculate' in resp.data


def test_deadline_compute():
    resp = _client().get('/deadline?rule_key=lim_art_123&trigger_date=2026-03-01&excluded_days=0')
    assert resp.status_code == 200
    assert b'31 March 2026' in resp.data


def test_deadline_with_exclusion():
    resp = _client().get('/deadline?rule_key=lim_art_116_a&trigger_date=2026-01-01&excluded_days=14')
    assert resp.status_code == 200
    assert b'15 April 2026' in resp.data


def test_deadline_compute_limitation_article_single():
    resp = _client().get('/deadline?rule_key=LIMART:54&trigger_date=2026-05-10&excluded_days=0')
    assert resp.status_code == 200
    assert b'10 May 2029' in resp.data
    assert b'Article 54' in resp.data


def test_deadline_compute_limitation_article_compound():
    resp = _client().get('/deadline?rule_key=LIMART:61&trigger_date=2026-01-01&excluded_days=0')
    assert resp.status_code == 200
    assert b'Article 61' in resp.data
    assert b'alternative periods' in resp.data
    assert b'30 years' in resp.data or b'Twelve years' in resp.data or b'12 years' in resp.data


def test_404_missing_section():
    resp = _client().get('/cpc/section/9999')
    assert resp.status_code == 404


def test_checklists_index():
    resp = _client().get('/checklists')
    assert resp.status_code == 200
    assert b'Courtroom Practice Checklists' in resp.data
    assert b'Order VII Rule 11' in resp.data


def test_checklists_category_filter():
    resp = _client().get('/checklists?category=Trial+Court+Practice+%26+Pleadings')
    assert resp.status_code == 200
    assert b'Rejection of Plaint' in resp.data


def test_checklist_detail_o7_r11():
    resp = _client().get('/checklist/o7_r11')
    assert resp.status_code == 200
    assert b'Rejection of Plaint' in resp.data
    assert b'Dahiben' in resp.data
    assert b'Saleem Bhai' in resp.data
    assert b'/cpc/section/' in resp.data


def test_checklist_detail_o39():
    resp = _client().get('/checklist/o39_r1_2')
    assert resp.status_code == 200
    assert b'Temporary Injunction' in resp.data
    assert b'Dalpat Kumar' in resp.data


def test_checklist_detail_plaint_scrutiny():
    resp = _client().get('/checklist/plaint_scrutiny_o7')
    assert resp.status_code == 200
    assert b'Plaint Institution' in resp.data
    assert b'Order VII' in resp.data


def test_checklist_detail_commercial_suit():
    resp = _client().get('/checklist/commercial_suit_cca')
    assert resp.status_code == 200
    assert b'Commercial Courts Act' in resp.data
    assert b'Patil Automation' in resp.data


def test_provision_link_resolver_routes_sra_sections_correctly():
    # Section 14A of the SRA must resolve to the SRA's own section, not
    # silently to a CPC section (CPC has no Section 14A, but this guards
    # against the routing bug regressing for a number CPC does have).
    import app as a
    with a.app.app_context():
        db = a.get_db()
        result = a.resolve_provision_link(
            {'kind': 'sra_section', 'ref': 'Section 14A', 'title': 'x'}, db)
        assert result['url'] == '/sra/section/15'


def test_provision_link_resolver_strips_subclause_suffix():
    # 'Section 2(11)' must link to the parent CPC Section 2, not fail to
    # resolve because '2(11)' isn't a stored section number.
    import app as a
    with a.app.app_context():
        db = a.get_db()
        result = a.resolve_provision_link(
            {'kind': 'section', 'ref': 'Section 2(11)', 'title': 'x'}, db)
        assert result['url'] is not None
        assert '/cpc/section/' in result['url']


def test_provision_link_resolver_leaves_out_of_corpus_refs_unresolved():
    # References to Acts this app doesn't ingest (Commercial Courts Act,
    # Evidence Act) must correctly stay unresolved rather than being
    # force-matched to an unrelated provision.
    import app as a
    with a.app.app_context():
        db = a.get_db()
        result = a.resolve_provision_link(
            {'kind': 'section', 'ref': 'Section 65B', 'title': 'x'}, db)
        assert result['url'] is None


def test_no_limitation_act_references_mistagged_as_plain_cpc_section():
    # CPC, the Limitation Act, and the SRA all have their own differently-
    # worded Section 3, Section 5, Section 12, etc. A connected_provisions
    # entry whose title is plainly about the Limitation Act (e.g.
    # 'Extension of prescribed period', 'Bar of limitation', 'Exclusion of
    # time') but tagged kind='section' would silently resolve to CPC's
    # unrelated section of the same number instead of failing safely —
    # confirmed live for Section 5 (CPC: revenue courts jurisdiction,
    # Limitation Act: condonation of delay) and Section 3 (CPC: court
    # subordination, Limitation Act: bar of limitation). Guards against
    # this class of source-data mistagging recurring across checklists,
    # templates, and execution workflows.
    import checklists_data as cd
    import templates_data as td
    import execution_data as edata
    import app as a

    with a.app.app_context():
        db = a.get_db()
        lim_titles = {}
        for row in db.conn.execute('SELECT section_no, title FROM limitation_sections'):
            lim_titles[row['section_no']] = row['title'].lower()

        mistagged = []
        for items in (cd.list_checklists(), td.list_templates(), edata.list_execution_workflows()):
            for item in items:
                for cp in item.connected_provisions:
                    if cp.get('kind') == 'section' and 'Section' in cp.get('ref', ''):
                        s_no = cp['ref'].replace('Section', '').strip().split()[0].split('(')[0]
                        title_lower = cp.get('title', '').lower()
                        lim_title = lim_titles.get(s_no, '')
                        if lim_title and any(w in title_lower for w in lim_title.split() if len(w) > 5):
                            mistagged.append((item.id, cp['ref'], cp['title']))
        assert mistagged == [], f"Found Limitation Act references mistagged as plain CPC sections: {mistagged}"


def test_checklist_404_invalid():
    resp = _client().get('/checklist/non_existent_checklist')
    assert resp.status_code == 404


def test_templates_index():
    resp = _client().get('/templates')
    assert resp.status_code == 200
    assert b'Court-Ready Drafting Templates' in resp.data
    assert b'Caveat Petition' in resp.data


def test_templates_category_filter():
    resp = _client().get('/templates?category=Execution+Proceedings')
    assert resp.status_code == 200
    assert b'Tabular Execution Petition' in resp.data


def test_template_detail_caveat():
    resp = _client().get('/template/caveat_sec_148a')
    assert resp.status_code == 200
    assert b'Caveat Petition' in resp.data
    assert b'SECTION 148A' in resp.data
    assert b'VERIFICATION AFFIDAVIT' in resp.data


def test_template_detail_execution_tabular():
    resp = _client().get('/template/execution_o21_tabular')
    assert resp.status_code == 200
    assert b'COLUMN NO.' in resp.data
    assert b'Order XXI Rule 11' in resp.data


def test_template_detail_amendment():
    resp = _client().get('/template/amendment_o6_r17')
    assert resp.status_code == 200
    assert b'Order VI Rule 17' in resp.data
    assert b'Amendment of Pleadings' in resp.data


def test_template_detail_commissioner():
    resp = _client().get('/template/commissioner_o26_r9')
    assert resp.status_code == 200
    assert b'Order XXVI Rule 9' in resp.data
    assert b'Court Commissioner' in resp.data


def test_template_detail_specific_performance():
    resp = _client().get('/template/plaint_specific_performance')
    assert resp.status_code == 200
    assert b'Specific Performance' in resp.data
    assert b'Article 54' in resp.data


def test_template_detail_impleadment():
    resp = _client().get('/template/impleadment_o1_r10')
    assert resp.status_code == 200
    assert b'Order I Rule 10' in resp.data
    assert b'Impleadment' in resp.data


def test_template_detail_chief_affidavit():
    resp = _client().get('/template/chief_affidavit_o18_r4')
    assert resp.status_code == 200
    assert b'Order XVIII Rule 4' in resp.data
    assert b'Evidence' in resp.data


def test_template_detail_commercial_suit():
    resp = _client().get('/template/plaint_commercial_suit')
    assert resp.status_code == 200
    assert b'Commercial Courts Act' in resp.data
    assert b'STATEMENT OF TRUTH' in resp.data


def test_template_detail_rsa():
    resp = _client().get('/template/regular_second_appeal_sec100')
    assert resp.status_code == 200
    assert b'Section 100' in resp.data
    assert b'SUBSTANTIAL QUESTIONS OF LAW' in resp.data


def test_template_404_invalid():
    resp = _client().get('/template/non_existent_template')
    assert resp.status_code == 404


def test_execution_index():
    resp = _client().get('/execution')
    assert resp.status_code == 200
    assert b'Order XXI Execution Roadmap' in resp.data
    assert b'Money Decrees' in resp.data


def test_execution_detail_money_decree():
    resp = _client().get('/execution/money_decree')
    assert resp.status_code == 200
    assert b'Money Decrees' in resp.data
    assert b'Attachment of Judgment Debtor' in resp.data
    assert b'Order XXI Rule 54' in resp.data


def test_execution_detail_possession():
    resp = _client().get('/execution/immovable_possession')
    assert resp.status_code == 200
    assert b'Delivery of Immovable Property' in resp.data
    assert b'Rule 35' in resp.data
    assert b'Rule 97' in resp.data


def test_execution_404_invalid():
    resp = _client().get('/execution/non_existent_workflow')
    assert resp.status_code == 404


def test_diary_index():
    resp = _client().get('/diary')
    assert resp.status_code == 200
    assert b'Advocate Case Diary' in resp.data


def test_diary_new_get():
    resp = _client().get('/diary/new')
    assert resp.status_code == 200
    assert b'Add New Case to Chamber Diary' in resp.data


def test_diary_full_lifecycle():
    c = _client()
    # 1. Create case via POST
    post_resp = c.post('/diary/new', data={
        'case_no': 'WEB/OS/555/2026',
        'court_name': 'Civil Court, Alipore',
        'client_name': 'Debashis Roy',
        'client_role': 'Plaintiff',
        'opposite_party': 'Subhash Bose',
        'opposite_counsel': 'Adv. Mukherjee',
        'stage': 'Service of Summons (Awaiting Written Statement)',
        'next_date': '2026-07-15',
        'notes': 'Partition suit'
    }, follow_redirects=True)
    assert post_resp.status_code == 200
    assert b'WEB/OS/555/2026' in post_resp.data
    assert b'Debashis Roy' in post_resp.data
    assert b'Order VIII Rule 1' in post_resp.data

    # Extract case ID from URL or page
    import re
    m = re.search(r'/diary/case/(\d+)/hearing', post_resp.data.decode('utf-8'))
    assert m is not None
    cid = m.group(1)

    # 2. Add hearing via POST
    h_resp = c.post(f'/diary/case/{cid}/hearing', data={
        'hearing_date': '2026-06-15',
        'business_done': 'Summons served on Defendant. WS awaited.',
        'next_date': '2026-07-15',
        'next_purpose': 'For filing of Written Statement',
        'new_stage': 'Service of Summons (Awaiting Written Statement)'
    }, follow_redirects=True)
    assert h_resp.status_code == 200
    assert b'Hearing on 2026-06-15' in h_resp.data

    # 3. Delete case via POST
    del_resp = c.post(f'/diary/case/{cid}/delete', follow_redirects=True)
    assert del_resp.status_code == 200
    assert b'WEB/OS/555/2026' not in del_resp.data


def test_diary_case_404():
    resp = _client().get('/diary/case/999999')
    assert resp.status_code == 404


def test_sra_sections():
    resp = _client().get('/sra/sections')
    assert resp.status_code == 200
    assert b'The Specific Relief Act, 1963' in resp.data
    assert b'PART II' in resp.data
    assert b'Section 10' in resp.data


def test_sra_section_detail_sec10():
    resp = _client().get('/sra/section/10')
    assert resp.status_code == 200
    assert b'Specific performance in respect of contracts' in resp.data
    assert b'shall be enforced by the court' in resp.data
    assert b'Article 54' in resp.data


def test_sra_section_detail_sec20a():
    resp = _client().get('/sra/section/22')
    assert resp.status_code == 200
    assert b'infrastructure project' in resp.data


def test_sra_section_404():
    resp = _client().get('/sra/section/9999')
    assert resp.status_code == 404


def test_search_sra_provisions():
    resp = _client().get('/search?q=substituted+performance')
    assert resp.status_code == 200
    assert b'SRA Section 20' in resp.data
    assert b'/sra/section/' in resp.data


def test_sra_analyzer_index():
    resp = _client().get('/sra/analyzer')
    assert resp.status_code == 200
    assert b'SRA Strategic Navigator' in resp.data
    assert b'Specific Performance of Agreement of Sale' in resp.data
    assert b'Declaratory Suits' in resp.data


def test_sra_analyzer_detail_sec10():
    resp = _client().get('/sra/analyzer/specific_performance_sec10')
    assert resp.status_code == 200
    assert b'Mandatory Plaint Prayers Checklist' in resp.data
    assert b'Section 22(1)(a)' in resp.data
    assert b'Sughar Singh' in resp.data


def test_sra_analyzer_detail_sec34():
    resp = _client().get('/sra/analyzer/declaration_sec34')
    assert resp.status_code == 200
    assert b'Section 34 Proviso' in resp.data
    assert b'Ram Saran v. Ganga Devi' in resp.data


def test_template_sra_sec20_notice():
    resp = _client().get('/template/sra_sec20_notice')
    assert resp.status_code == 200
    assert b'STATUTORY NOTICE UNDER SECTION 20(2)' in resp.data
    assert b'THIRTY (30) DAYS' in resp.data


def test_checklist_sra_sec16c():
    resp = _client().get('/checklist/sra_sec16c_specific_performance')
    assert resp.status_code == 200
    assert b'Specific Performance Trial Checklist' in resp.data
    assert b'Section 16(c)' in resp.data


def test_drafter_index():
    resp = _client().get('/drafter')
    assert resp.status_code == 200
    assert b'Multi-Statute Composite Draft Builder' in resp.data
    assert b'Composite Plaint for Specific Performance' in resp.data
    assert b'Statutory Provisions Merged' in resp.data


def test_drafter_builder_sp():
    resp = _client().get('/drafter/composite_specific_performance')
    assert resp.status_code == 200
    assert b'Statutory Harmonization Matrix' in resp.data
    assert b'Section 22(1)(a)' in resp.data
    assert b'ORDER VII' in resp.data
    assert b'COMPOSITE PLAINT FOR SPECIFIC PERFORMANCE' in resp.data


def test_drafter_builder_custom_param():
    resp = _client().get('/drafter/composite_specific_performance?PLAINTIFF_NAME=Advocate+Kiran+Verma')
    assert resp.status_code == 200
    assert b'Advocate Kiran Verma' in resp.data


if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    for t in tests:
        t()
        print(f'  OK  {t.__name__}')
    print(f'\n>>> ALL {len(tests)} WEB TESTS PASSED! <<<')




