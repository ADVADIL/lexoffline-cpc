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


if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    for t in tests:
        t()
        print(f'  OK  {t.__name__}')
    print(f'\n>>> ALL {len(tests)} WEB TESTS PASSED! <<<')




