#!/usr/bin/env python3
"""
LexOffline — CPC, 1908 & The Limitation Act, 1963 Practice Module
Desktop app (PySide6 + local SQLite). Deterministic only: every screen
reads from the local database or does plain date/text arithmetic.
Nothing here is generated or inferred by a model.
"""
import sys
import os
from datetime import date

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QGuiApplication
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTreeWidget, QTreeWidgetItem, QTextBrowser, QLineEdit, QLabel,
    QSplitter, QTabWidget, QListWidget, QListWidgetItem, QPushButton,
    QDateEdit, QComboBox, QFormLayout, QPlainTextEdit, QMessageBox,
    QSpinBox, QGroupBox, QScrollArea, QCheckBox, QFrame, QDialog,
    QDialogButtonBox, QTableWidget, QTableWidgetItem, QHeaderView
)

from db import ActDatabase
from xref import extract_refs, resolve_refs
from state_amend import KNOWN_STATES, states_present, text_for_state
import deadlines as dl
import limitation_data as ld
import checklists_data as cd
import templates_data as tdata
import execution_data as edata
import case_stages as cs


def html_escape(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class ExplorerTab(QWidget):
    """Tree navigation over CPC 1908 and Limitation Act 1963, with provision
    viewer, deterministic cross-references, limitation linkage, bookmark toggle,
    and a notes box."""

    def __init__(self, db: ActDatabase):
        super().__init__()
        self.db = db
        self.current = None  # ("section"|"rule"|"appendix"|"limitation_section"|"limitation_article", id)
        self._current_body = ""
        self._current_state_blob = ""
        self._is_limitation = False

        layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        # --- left: tree ---
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Acts & Provisions"])
        self.tree.itemClicked.connect(self._on_tree_click)
        splitter.addWidget(self.tree)
        self._populate_tree()

        # --- right: viewer ---
        right = QWidget()
        rlayout = QVBoxLayout(right)
        self.title_label = QLabel("Select a provision")
        self.title_label.setStyleSheet("font-weight: 600; font-size: 13pt; color: #1a365d;")
        self.title_label.setWordWrap(True)
        rlayout.addWidget(self.title_label)

        self.state_row_widget = QWidget()
        state_row = QHBoxLayout(self.state_row_widget)
        state_row.setContentsMargins(0, 0, 0, 0)
        state_row.addWidget(QLabel("View State Amendment:"))
        self.state_combo = QComboBox()
        self.state_combo.addItem("Central Act (default)", None)
        for st in KNOWN_STATES:
            self.state_combo.addItem(st, st)
        self.state_combo.currentIndexChanged.connect(self._render_text)
        state_row.addWidget(self.state_combo, stretch=1)
        rlayout.addWidget(self.state_row_widget)

        self.bookmark_btn = QPushButton("☆ Bookmark")
        self.bookmark_btn.clicked.connect(self._toggle_bookmark)
        rlayout.addWidget(self.bookmark_btn)

        tabs = QTabWidget()
        rlayout.addWidget(tabs, stretch=1)

        self.text_view = QTextBrowser()
        self.text_view.setOpenLinks(False)
        self.text_view.anchorClicked.connect(self._on_anchor_clicked)
        tabs.addTab(self.text_view, "Provision Text")

        self.xref_list = QListWidget()
        self.xref_list.itemDoubleClicked.connect(self._on_xref_activated)
        tabs.addTab(self.xref_list, "Cross-References & Limitation")

        self.notes_box = QPlainTextEdit()
        self.notes_box.textChanged.connect(self._on_notes_changed)
        tabs.addTab(self.notes_box, "Notes")

        splitter.addWidget(right)
        splitter.setSizes([340, 660])

        self._loading_notes = False

    # ---------- tree population ----------
    def _populate_tree(self):
        self.tree.clear()

        # === 1. CODE OF CIVIL PROCEDURE, 1908 ===
        cpc_root = QTreeWidgetItem(["📖 Code of Civil Procedure, 1908"])
        bold_font = QFont()
        bold_font.setBold(True)
        cpc_root.setFont(0, bold_font)
        self.tree.addTopLevelItem(cpc_root)

        sec_root = QTreeWidgetItem(["Sections (1–158)"])
        cpc_root.addChild(sec_root)
        parts = self.db.sections_by_part()
        for part, rows in parts.items():
            part_item = QTreeWidgetItem([f"Part {part}"])
            sec_root.addChild(part_item)
            for r in rows:
                it = QTreeWidgetItem([f"S.{r['section_no']} — {r['title']}"])
                it.setData(0, Qt.UserRole, ("section", r["id"]))
                part_item.addChild(it)

        ord_root = QTreeWidgetItem(["Orders (I–LI)"])
        cpc_root.addChild(ord_root)
        for o in self.db.all_orders():
            o_item = QTreeWidgetItem([f"Order {o['order_no']} — {o['title']}"])
            o_item.setData(0, Qt.UserRole, ("order", o["id"]))
            ord_root.addChild(o_item)
            for r in self.db.rules_for_order(o["id"]):
                rit = QTreeWidgetItem([f"R.{r['rule_no']} — {r['title']}"])
                rit.setData(0, Qt.UserRole, ("rule", r["id"]))
                o_item.addChild(rit)

        app_root = QTreeWidgetItem(["Appendices (A–I)"])
        cpc_root.addChild(app_root)
        for a in self.db.all_appendices():
            it = QTreeWidgetItem([f"Appendix {a['letter']}"])
            it.setData(0, Qt.UserRole, ("appendix", a["id"]))
            app_root.addChild(it)

        # === 2. THE LIMITATION ACT, 1963 ===
        lim_root = QTreeWidgetItem(["⚖️ The Limitation Act, 1963"])
        lim_root.setFont(0, bold_font)
        self.tree.addTopLevelItem(lim_root)

        # Limitation Sections 1-32
        lim_sec_root = QTreeWidgetItem(["Sections (1–32)"])
        lim_root.addChild(lim_sec_root)
        lim_parts = self.db.limitation_sections_by_part()
        for part, rows in lim_parts.items():
            part_item = QTreeWidgetItem([f"Part {part}"])
            lim_sec_root.addChild(part_item)
            for r in rows:
                it = QTreeWidgetItem([f"S.{r['section_no']} — {r['title']}"])
                it.setData(0, Qt.UserRole, ("limitation_section", r["id"]))
                part_item.addChild(it)

        # Limitation Schedule Articles 1-137
        sched_root = QTreeWidgetItem(["The Schedule (Articles 1–137)"])
        lim_root.addChild(sched_root)
        divs = self.db.limitation_articles_by_division()
        for div_name, pmap in divs.items():
            div_item = QTreeWidgetItem([div_name])
            sched_root.addChild(div_item)
            for part_name, arows in pmap.items():
                if part_name != div_name:
                    p_item = QTreeWidgetItem([part_name])
                    div_item.addChild(p_item)
                else:
                    p_item = div_item
                for a in arows:
                    short_desc = a["description"].splitlines()[0]
                    if len(short_desc) > 50:
                        short_desc = short_desc[:47] + "..."
                    it = QTreeWidgetItem([f"Art.{a['article_no']} ({a['period']}) — {short_desc}"])
                    it.setData(0, Qt.UserRole, ("limitation_article", a["id"]))
                    p_item.addChild(it)

        cpc_root.setExpanded(True)

    def _on_tree_click(self, item, _col):
        data = item.data(0, Qt.UserRole)
        if not data:
            return
        kind, ref_id = data
        if kind == "order":
            row = self.db.get_order(ref_id)
            self._show(kind, ref_id, f"Order {row['order_no']} — {row['title']}",
                       f"Order {row['order_no']} — {row['title']}\n\n(Select a Rule under this Order in the left tree for full text.)")
            return
        self._load_and_show(kind, ref_id)

    # ---------- viewer ----------
    def _load_and_show(self, kind, ref_id):
        if kind == "section":
            row = self.db.get_section(ref_id)
            title = f"CPC 1908 — Section {row['section_no']}: {row['title']}"
            body = row["text"]
            state_blob = row["state_amendments"] or ""
            is_limitation = False
        elif kind == "rule":
            row = self.db.get_rule(ref_id)
            order = self.db.get_order(row["order_id"])
            title = f"CPC 1908 — Order {order['order_no']} Rule {row['rule_no']}: {row['title']}"
            body = row["text"]
            state_blob = row["state_amendments"] or ""
            is_limitation = False
        elif kind == "appendix":
            row = self.db.get_appendix(ref_id)
            title = f"CPC 1908 — Appendix {row['letter']}"
            body = row["text"]
            state_blob = ""
            is_limitation = False
        elif kind == "limitation_section":
            row = self.db.get_limitation_section(ref_id)
            title = f"Limitation Act 1963 — Section {row['section_no']}: {row['title']} [{row['part']}]"
            body = row["text"]
            state_blob = ""
            is_limitation = True
        elif kind == "limitation_article":
            row = self.db.get_limitation_article(ref_id)
            title = f"Limitation Act 1963 — Article {row['article_no']} ({row['period']}) [{row['part']}]"
            body = f"<b>Division:</b> {row['division']}<br><b>Part:</b> {row['part']}<br><br>" \
                   f"<b>Description of Suit / Appeal / Application:</b><br>{html_escape(row['description'])}<br><br>" \
                   f"<b>Period of Limitation:</b> {html_escape(row['period'])}<br><br>" \
                   f"<b>Time from which period begins to run:</b><br>{html_escape(row['time_begins'])}<br><br>" \
                   f"<b>Connected CPC Provisions:</b> {html_escape(row['cpc_ref'] or 'None explicitly indexed')}"
            state_blob = ""
            is_limitation = True
        else:
            return
        self._show(kind, ref_id, title, body, state_blob, is_limitation)

    def _show(self, kind, ref_id, title, body, state_blob="", is_limitation=False):
        self.current = (kind, ref_id)
        self._current_body = body
        self._current_state_blob = state_blob
        self._is_limitation = is_limitation
        self.title_label.setText(title)

        self.state_row_widget.setVisible(not is_limitation and bool(state_blob))
        if not is_limitation and state_blob:
            self.state_combo.blockSignals(True)
            self.state_combo.setCurrentIndex(0)
            self.state_combo.blockSignals(False)

        self._render_text()

        self.xref_list.clear()
        if kind in ("section", "rule"):
            self_kind = "section" if kind == "section" else None
            self_ref = None
            search_key = ""
            if kind == "section":
                row = self.db.get_section(ref_id)
                self_ref = row["section_no"]
                search_key = f"Section {row['section_no']}"
            elif kind == "rule":
                row = self.db.get_rule(ref_id)
                order = self.db.get_order(row["order_id"])
                search_key = f"Order {order['order_no']}"

            refs = extract_refs(body, self_kind=self_kind, self_ref=self_ref)
            resolved = resolve_refs(self.db, refs)
            if resolved:
                header = QListWidgetItem("--- In-Text Cross References ---")
                header.setFlags(Qt.NoItemFlags)
                self.xref_list.addItem(header)
                for r in resolved:
                    found = "✓" if r["target"] else "✗ not in local database"
                    li = QListWidgetItem(f"{r['label']}  [{found}]")
                    li.setData(Qt.UserRole, r)
                    self.xref_list.addItem(li)

            lim_matches = self.db.find_articles_for_cpc(search_key)
            if lim_matches:
                header2 = QListWidgetItem("--- Linked Limitation Act 1963 Articles ---")
                header2.setFlags(Qt.NoItemFlags)
                self.xref_list.addItem(header2)
                for a in lim_matches:
                    li = QListWidgetItem(f"⚖️ Article {a['article_no']} ({a['period']}) — {a['description'][:50]}...")
                    li.setData(Qt.UserRole, {"target_kind": "limitation_article", "target": dict(a)})
                    self.xref_list.addItem(li)

            if not resolved and not lim_matches:
                self.xref_list.addItem("(no specific cross-references or limitation articles detected)")

        elif kind == "limitation_article":
            row = self.db.get_limitation_article(ref_id)
            if row["cpc_ref"]:
                header = QListWidgetItem("--- Mentioned / Linked CPC Provisions ---")
                header.setFlags(Qt.NoItemFlags)
                self.xref_list.addItem(header)
                li = QListWidgetItem(f"📖 CPC Provisions: {row['cpc_ref']}")
                li.setFlags(Qt.NoItemFlags)
                self.xref_list.addItem(li)
            else:
                self.xref_list.addItem("(general limitation article)")
        elif kind == "limitation_section":
            self.xref_list.addItem("(The Limitation Act, 1963 substantive section)")
        else:
            self.xref_list.addItem("(cross-references apply to Sections and Rules)")

        bm = self.db.is_bookmarked(kind, ref_id)
        self.bookmark_btn.setText("★ Bookmarked" if bm else "☆ Bookmark")

        self._loading_notes = True
        self.notes_box.setPlainText(self.db.get_note(kind, ref_id))
        self._loading_notes = False

    def _render_text(self):
        selected_state = self.state_combo.currentData()
        if self._is_limitation and "<br>" in self._current_body:
            html = f"<div style='font-family:inherit; line-height:1.6; padding:8px;'>{self._current_body}</div>"
        else:
            html = f"<pre style='white-space:pre-wrap; font-family:inherit; line-height:1.5;'>{html_escape(self._current_body)}</pre>"

        if not self._is_limitation and selected_state:
            available = states_present(self._current_state_blob)
            if selected_state in available:
                state_text = text_for_state(self._current_state_blob, selected_state)
                html += (
                    f"<hr><h3 style='color:#a33;'>State Amendment — {html_escape(selected_state)}</h3>"
                    f"<pre style='white-space:pre-wrap; font-family:inherit;'>{html_escape(state_text)}</pre>"
                )
            elif available:
                others = ", ".join(available)
                html += (
                    f"<hr><p style='color:#888;'><i>No {html_escape(selected_state)} amendment recorded "
                    f"for this provision. State amendments on file here: {html_escape(others)}.</i></p>"
                )
            else:
                html += "<hr><p style='color:#888;'><i>No state amendments recorded for this provision.</i></p>"

        self.text_view.setHtml(html)

    def _on_xref_activated(self, item):
        r = item.data(Qt.UserRole)
        if not r or not r.get("target"):
            return
        t_kind = r.get("target_kind")
        if t_kind == "section":
            self._load_and_show("section", r["target"]["id"])
        elif t_kind == "rule":
            self._load_and_show("rule", r["target"]["id"])
        elif t_kind == "order":
            row = r["target"]
            self._show("order", row["id"], f"Order {row['order_no']} — {row['title']}",
                       f"Order {row['order_no']} — {row['title']}\n\n(Select a Rule under this Order for full text.)")
        elif t_kind == "limitation_article":
            self._load_and_show("limitation_article", r["target"]["id"])
        elif t_kind == "limitation_section":
            self._load_and_show("limitation_section", r["target"]["id"])

    def _on_anchor_clicked(self, url):
        pass

    def _toggle_bookmark(self):
        if not self.current:
            return
        kind, ref_id = self.current
        self.db.toggle_bookmark(kind, ref_id)
        bm = self.db.is_bookmarked(kind, ref_id)
        self.bookmark_btn.setText("★ Bookmarked" if bm else "☆ Bookmark")

    def _on_notes_changed(self):
        if self._loading_notes or not self.current:
            return
        kind, ref_id = self.current
        self.db.save_note(kind, ref_id, self.notes_box.toPlainText())

    def jump_to(self, kind, ref_id):
        self._load_and_show(kind, ref_id)


class SearchTab(QWidget):
    def __init__(self, db: ActDatabase, on_jump):
        super().__init__()
        self.db = db
        self.on_jump = on_jump
        layout = QVBoxLayout(self)

        self.box = QLineEdit()
        self.box.setPlaceholderText("Search by keyword, e.g. injunction, attachment, caveat, Section 80, condonation, adverse possession …")
        self.box.returnPressed.connect(self._run_search)
        layout.addWidget(self.box)

        go = QPushButton("Search")
        go.clicked.connect(self._run_search)
        layout.addWidget(go)

        self.results = QListWidget()
        self.results.itemDoubleClicked.connect(self._on_result_activated)
        layout.addWidget(self.results, stretch=1)

    def _run_search(self):
        q = self.box.text().strip()
        self.results.clear()
        if not q:
            return
        rows = self.db.search(q)
        if not rows:
            self.results.addItem("(no matches found across CPC 1908 or Limitation Act 1963)")
            return
        for r in rows:
            kind_tag = r["kind"].replace("_", " ").title()
            li = QListWidgetItem(f"[{kind_tag}] {r['label']}  —  {r['snip']}")
            li.setData(Qt.UserRole, (r["kind"], r["ref_id"]))
            self.results.addItem(li)

    def _on_result_activated(self, item):
        data = item.data(Qt.UserRole)
        if data:
            self.on_jump(*data)


class DeadlineTrackerTab(QWidget):
    """Deterministic CPC & Limitation Act deadline calculator."""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        form = QFormLayout()

        self.cat_combo = QComboBox()
        self.cat_combo.addItem("All Categories", None)
        for cat in dl.list_categories():
            self.cat_combo.addItem(cat, cat)
        self.cat_combo.addItem(
            "All 137 Limitation Act Articles (comprehensive)",
            "__ALL_LIMITATION_ARTICLES__",
        )
        self.cat_combo.currentIndexChanged.connect(self._on_category_changed)
        form.addRow("Category filter:", self.cat_combo)

        self.rule_combo = QComboBox()
        self._populate_rules()
        form.addRow("Rule / Limitation Article:", self.rule_combo)

        self.trigger_date = QDateEdit(calendarPopup=True)
        self.trigger_date.setDate(date.today())
        form.addRow("Trigger date (e.g. date of decree / death / notice):", self.trigger_date)

        self.exclusion_spin = QSpinBox()
        self.exclusion_spin.setRange(0, 3650)
        self.exclusion_spin.setValue(0)
        self.exclusion_spin.setSuffix(" days")
        self.exclusion_spin.setToolTip("Days excluded under Section 12 of Limitation Act (time taken for obtaining certified copy)")
        form.addRow("Section 12 Copy Exclusion (optional):", self.exclusion_spin)

        layout.addLayout(form)

        calc_btn = QPushButton("Calculate Statutory Deadline")
        calc_btn.setStyleSheet("font-weight: 600; padding: 6px;")
        calc_btn.clicked.connect(self._calculate)
        layout.addWidget(calc_btn)

        self.result_box = QGroupBox("Computation Result")
        res_layout = QVBoxLayout(self.result_box)
        self.result_label = QLabel("Select a rule and click Calculate.")
        self.result_label.setStyleSheet("font-size: 12pt; font-weight: 600; color: #1a365d; padding: 6px;")
        self.result_label.setWordWrap(True)
        res_layout.addWidget(self.result_label)

        self.detail_label = QLabel("")
        self.detail_label.setStyleSheet("color: #4a5568; padding: 4px;")
        self.detail_label.setWordWrap(True)
        res_layout.addWidget(self.detail_label)
        layout.addWidget(self.result_box)

        warn = QLabel(
            "Note: These computations apply Central Act timelines and Limitation Act 1963 Articles. "
            "Under Section 4, if the due date falls on a court holiday, filing on the re-opening day is permitted. "
            "Under Section 5, condonation of delay applies to appeals and applications (except Order XXI execution petitions)."
        )
        warn.setWordWrap(True)
        warn.setStyleSheet("color: #a33; padding: 8px; font-size: 9pt;")
        layout.addWidget(warn)
        layout.addStretch(1)

    def _populate_rules(self):
        self.rule_combo.clear()
        selected_cat = self.cat_combo.currentData()
        if selected_cat == "__ALL_LIMITATION_ARTICLES__":
            for a in ld.LIMITATION_ARTICLES:
                desc = a["description"].split("\n")[0][:70]
                label = f"Art. {a['article_no']} — {desc} ({a['period'].splitlines()[0]}{'...' if len(a['period'].splitlines()) > 1 else ''})"
                self.rule_combo.addItem(label, f"LIMART:{a['article_no']}")
            return
        rules = dl.list_rules(category=selected_cat)
        for r in rules:
            self.rule_combo.addItem(f"{r.label}  [{r.provision}]", r.key)

    def _on_category_changed(self):
        self._populate_rules()

    def _calculate(self):
        key = self.rule_combo.currentData()
        if not key:
            return
        qd = self.trigger_date.date()
        trigger = date(qd.year(), qd.month(), qd.day())
        excluded = self.exclusion_spin.value()

        if isinstance(key, str) and key.startswith("LIMART:"):
            article_no = key.split(":", 1)[1]
            article = next((a for a in ld.LIMITATION_ARTICLES if a["article_no"] == article_no), None)
            if not article:
                return
            result = dl.compute_limitation_article(trigger, article, excluded_days=excluded)
            ex_note = f" (including +{excluded} days excluded u/s 12)" if excluded > 0 else ""
            options = result["options"]
            if len(options) == 1:
                opt = options[0]
                self.result_label.setText(
                    f"Statutory Due Date: {opt['due_date'].strftime('%d %B %Y')}{ex_note}"
                )
            else:
                lines = "<br>".join(
                    f"{opt['label']} {opt['amount']} {opt['unit']} — <b>{opt['due_date'].strftime('%d %B %Y')}</b>"
                    for opt in options
                )
                self.result_label.setText(
                    f"This Article prescribes alternative periods depending on which "
                    f"sub-clause applies to the facts of the case{ex_note}:<br>{lines}"
                )
            self.detail_label.setText(
                f"<b>Article {article['article_no']}</b> ({article['division']}, {article['part']})<br>"
                f"<b>Description:</b> {article['description']}<br>"
                f"<b>Time begins:</b> {article['time_begins']}<br>"
                f"<b>CPC cross-reference:</b> {article.get('cpc_ref') or '—'}"
            )
            return

        result = dl.compute(trigger, key, excluded_days=excluded)
        due = result["due_date"]
        rule = result["rule"]

        ex_note = f" (including +{excluded} days excluded u/s 12)" if excluded > 0 else ""
        self.result_label.setText(
            f"Statutory Due Date: {due.strftime('%d %B %Y')}{ex_note}"
        )
        self.detail_label.setText(
            f"<b>Provision:</b> {rule.provision}<br>"
            f"<b>Period:</b> {result['period_str']} from trigger date {trigger.strftime('%d %B %Y')}<br>"
            f"<b>Starting Event:</b> {rule.note or 'As prescribed by the provision'}"
        )


class ChecklistsTab(QWidget):
    """Interactive courtroom practice checklists & statutory compliance tests."""

    def __init__(self, db: ActDatabase, on_jump):
        super().__init__()
        self.db = db
        self.on_jump = on_jump

        layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)

        self.cat_combo = QComboBox()
        self.cat_combo.addItem("All Categories", None)
        for cat in cd.list_checklist_categories():
            self.cat_combo.addItem(cat, cat)
        self.cat_combo.currentIndexChanged.connect(self._populate_list)
        left_layout.addWidget(self.cat_combo)

        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self._on_item_clicked)
        left_layout.addWidget(self.list_widget, stretch=1)
        splitter.addWidget(left)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.viewer = QWidget()
        self.vlayout = QVBoxLayout(self.viewer)
        self.vlayout.setAlignment(Qt.AlignTop)
        self.scroll.setWidget(self.viewer)
        splitter.addWidget(self.scroll)

        splitter.setSizes([320, 680])
        self._populate_list()

        if self.list_widget.count() > 0:
            self.list_widget.setCurrentRow(0)
            self._on_item_clicked(self.list_widget.item(0))

    def _populate_list(self):
        self.list_widget.clear()
        selected_cat = self.cat_combo.currentData()
        items = cd.list_checklists(category=selected_cat)
        for c in items:
            it = QListWidgetItem(f"{c.title}\n[{c.provision}]")
            it.setData(Qt.UserRole, c.id)
            self.list_widget.addItem(it)

    def _on_item_clicked(self, item):
        cid = item.data(Qt.UserRole)
        c = cd.get_checklist(cid)
        if not c:
            return

        while self.vlayout.count():
            child = self.vlayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        header = QLabel(f"<h2>{c.title}</h2><p style='color:#4a5568;'><b>Provision:</b> {c.provision} &nbsp;|&nbsp; <b>Category:</b> {c.category}</p><p style='font-size:10pt; line-height:1.4;'>{c.summary}</p>")
        header.setWordWrap(True)
        self.vlayout.addWidget(header)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.vlayout.addWidget(line)

        sg_box = QGroupBox("📋 Statutory Grounds & Threshold Tests")
        sg_layout = QVBoxLayout(sg_box)
        for g in c.statutory_grounds:
            g_label = QLabel(f"<b>{g['clause']}: {g['ground']}</b><br><span style='color:#4a5568;'>{g['detail']}</span>")
            g_label.setWordWrap(True)
            sg_layout.addWidget(g_label)
        self.vlayout.addWidget(sg_box)

        jp_box = QGroupBox("⚖️ Settled Judicial Principles (Landmark Precedents)")
        jp_layout = QVBoxLayout(jp_box)
        for p in c.judicial_principles:
            p_label = QLabel(f"<b>{p['principle']}</b><br><i style='color:#2b6cb0;'>{p['citation']}</i><br><span style='color:#4a5568;'>{p['detail']}</span>")
            p_label.setWordWrap(True)
            jp_layout.addWidget(p_label)
        self.vlayout.addWidget(jp_box)

        steps_box = QGroupBox("☑️ Actionable Courtroom Checklist (Check off while preparing)")
        steps_layout = QVBoxLayout(steps_box)
        for s in c.steps:
            cb = QCheckBox(f"<b>{s.label}</b> [{s.statutory_ref}]")
            desc = QLabel(f"<span style='color:#4a5568; margin-left:22px;'>{s.description}</span>")
            desc.setWordWrap(True)
            steps_layout.addWidget(cb)
            steps_layout.addWidget(desc)
        self.vlayout.addWidget(steps_box)

        pit_box = QGroupBox("⚠️ Common Pitfalls & Fatal Traps")
        pit_box.setStyleSheet("QGroupBox { font-weight: bold; color: #c53030; }")
        pit_layout = QVBoxLayout(pit_box)
        for pit in c.common_pitfalls:
            pit_label = QLabel(f"• {pit}")
            pit_label.setWordWrap(True)
            pit_label.setStyleSheet("color: #9b2c2c;")
            pit_layout.addWidget(pit_label)
        self.vlayout.addWidget(pit_box)

        conn_box = QGroupBox("🔗 Connected Provisions (Click to Jump)")
        conn_layout = QHBoxLayout(conn_box)
        for cp in c.connected_provisions:
            btn = QPushButton(f"{cp['ref']}")
            btn.setToolTip(cp.get("title", ""))
            btn.clicked.connect(lambda checked=False, target=cp: self._jump_to_provision(target))
            conn_layout.addWidget(btn)
        conn_layout.addStretch(1)
        self.vlayout.addWidget(conn_box)

    def _jump_to_provision(self, cp):
        ref_text = cp["ref"]
        if "Section" in ref_text:
            s_no = ref_text.replace("Section", "").strip().split()[0]
            if cp.get("kind") == "limitation_section":
                row = self.db.get_limitation_section_by_no(s_no)
                if row:
                    self.on_jump("limitation_section", row["id"])
                    return
            else:
                row = self.db.get_section_by_no(s_no)
                if row:
                    self.on_jump("section", row["id"])
                    return
        elif "Article" in ref_text:
            a_no = ref_text.replace("Article", "").strip().split("(")[0].strip()
            row = self.db.find_article_by_no(a_no)
            if row:
                self.on_jump("limitation_article", row["id"])
                return
        elif "Order" in ref_text and "Rule" in ref_text:
            parts = ref_text.replace("Order", "").split("Rule")
            o_no = parts[0].strip()
            r_no = parts[1].strip().split("(")[0].strip()
            row = self.db.find_rule_in_order(o_no, r_no)
            if row:
                self.on_jump("rule", row["id"])
                return
        elif "Order" in ref_text:
            o_no = ref_text.replace("Order", "").strip()
            row = self.db.find_order_by_no(o_no)
            if row:
                self.on_jump("order", row["id"])
                return


class DraftingTemplatesTab(QWidget):
    """Court-ready drafting templates & fillable form library."""

    def __init__(self, db: ActDatabase, on_jump):
        super().__init__()
        self.db = db
        self.on_jump = on_jump

        layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)

        from collections import Counter
        all_templates = tdata.list_templates()
        cat_counts = Counter(t.category for t in all_templates)

        self.cat_combo = QComboBox()
        self.cat_combo.addItem(f"All Formats ({len(all_templates)})", None)
        for cat in tdata.list_template_categories():
            count = cat_counts.get(cat, 0)
            self.cat_combo.addItem(f"{cat} ({count})", cat)
        self.cat_combo.currentIndexChanged.connect(self._populate_list)
        left_layout.addWidget(self.cat_combo)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Filter templates...")
        self.search_input.textChanged.connect(self._populate_list)
        left_layout.addWidget(self.search_input)

        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self._on_item_clicked)
        left_layout.addWidget(self.list_widget, stretch=1)
        splitter.addWidget(left)

        right = QWidget()
        rlayout = QVBoxLayout(right)

        top_bar = QHBoxLayout()
        self.title_label = QLabel("Select a template")
        self.title_label.setStyleSheet("font-weight: 600; font-size: 13pt; color: #1a365d;")
        self.title_label.setWordWrap(True)
        top_bar.addWidget(self.title_label, stretch=1)

        self.copy_btn = QPushButton("📋 Copy to Clipboard")
        self.copy_btn.setStyleSheet("font-weight: bold; padding: 6px 14px; background: #2b6cb0; color: white;")
        self.copy_btn.clicked.connect(self._copy_to_clipboard)
        top_bar.addWidget(self.copy_btn)
        rlayout.addLayout(top_bar)

        self.notes_label = QLabel("")
        self.notes_label.setStyleSheet("color: #4a5568; background: #f7fafc; border-left: 3px solid #3182ce; padding: 6px;")
        self.notes_label.setWordWrap(True)
        rlayout.addWidget(self.notes_label)

        self.editor = QPlainTextEdit()
        font = QFont("Courier New", 10)
        self.editor.setFont(font)
        rlayout.addWidget(self.editor, stretch=1)

        self.conn_row = QHBoxLayout()
        self.conn_widget = QWidget()
        self.conn_widget.setLayout(self.conn_row)
        rlayout.addWidget(self.conn_widget)

        splitter.addWidget(right)
        splitter.setSizes([320, 680])
        self._populate_list()

        if self.list_widget.count() > 0:
            self.list_widget.setCurrentRow(0)
            self._on_item_clicked(self.list_widget.item(0))

    def _populate_list(self):
        self.list_widget.clear()
        selected_cat = self.cat_combo.currentData()
        q = self.search_input.text().lower().strip() if hasattr(self, 'search_input') else ""
        items = tdata.list_templates(category=selected_cat)
        for t in items:
            if q and (q not in t.title.lower() and q not in t.provision.lower() and q not in t.summary.lower()):
                continue
            it = QListWidgetItem(f"{t.title}\n[{t.provision}]")
            it.setData(Qt.UserRole, t.id)
            self.list_widget.addItem(it)

    def _on_item_clicked(self, item):
        tid = item.data(Qt.UserRole)
        t = tdata.get_template(tid)
        if not t:
            return

        self.title_label.setText(f"{t.title} [{t.provision}]")
        self.notes_label.setText(f"<b>Summary:</b> {t.summary}<br><b>Practice Note:</b> {t.practice_notes}")
        self.editor.setPlainText(t.template_text)

        while self.conn_row.count():
            child = self.conn_row.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.conn_row.addWidget(QLabel("<b>Connected:</b>"))
        for cp in t.connected_provisions:
            btn = QPushButton(cp["ref"])
            btn.setToolTip(cp.get("title", ""))
            btn.clicked.connect(lambda checked=False, target=cp: self._jump_to_provision(target))
            self.conn_row.addWidget(btn)
        self.conn_row.addStretch(1)

    def _copy_to_clipboard(self):
        text = self.editor.toPlainText()
        if text:
            QGuiApplication.clipboard().setText(text)
            orig_text = self.copy_btn.text()
            self.copy_btn.setText("✓ Copied to Clipboard!")
            QTimer.singleShot(2000, lambda: self.copy_btn.setText(orig_text))

    def _jump_to_provision(self, cp):
        ref_text = cp["ref"]
        if "Section" in ref_text:
            s_no = ref_text.replace("Section", "").strip().split()[0]
            if cp.get("kind") == "limitation_section":
                row = self.db.get_limitation_section_by_no(s_no)
                if row:
                    self.on_jump("limitation_section", row["id"])
                    return
            else:
                row = self.db.get_section_by_no(s_no)
                if row:
                    self.on_jump("section", row["id"])
                    return
        elif "Article" in ref_text:
            a_no = ref_text.replace("Article", "").strip().split("(")[0].strip()
            row = self.db.find_article_by_no(a_no)
            if row:
                self.on_jump("limitation_article", row["id"])
                return
        elif "Order" in ref_text and "Rule" in ref_text:
            parts = ref_text.replace("Order", "").split("Rule")
            o_no = parts[0].strip()
            r_no = parts[1].strip().split("(")[0].strip()
            row = self.db.find_rule_in_order(o_no, r_no)
            if row:
                self.on_jump("rule", row["id"])
                return
        elif "Order" in ref_text:
            o_no = ref_text.replace("Order", "").strip()
            row = self.db.find_order_by_no(o_no)
            if row:
                self.on_jump("order", row["id"])
                return


class ExecutionNavigatorTab(QWidget):
    """Order XXI Execution Roadmap & Navigator."""

    def __init__(self, db: ActDatabase, on_jump):
        super().__init__()
        self.db = db
        self.on_jump = on_jump

        layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)

        left_layout.addWidget(QLabel("<b>Execution Roadmaps:</b>"))
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self._on_item_clicked)
        left_layout.addWidget(self.list_widget, stretch=1)
        splitter.addWidget(left)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.viewer = QWidget()
        self.vlayout = QVBoxLayout(self.viewer)
        self.vlayout.setAlignment(Qt.AlignTop)
        self.scroll.setWidget(self.viewer)
        splitter.addWidget(self.scroll)

        splitter.setSizes([320, 680])
        self._populate_list()

        if self.list_widget.count() > 0:
            self.list_widget.setCurrentRow(0)
            self._on_item_clicked(self.list_widget.item(0))

    def _populate_list(self):
        self.list_widget.clear()
        for w in edata.list_execution_workflows():
            it = QListWidgetItem(f"{w.title}\n({len(w.stages)} stages)")
            it.setData(Qt.UserRole, w.id)
            self.list_widget.addItem(it)

    def _on_item_clicked(self, item):
        wid = item.data(Qt.UserRole)
        w = edata.get_execution_workflow(wid)
        if not w:
            return

        while self.vlayout.count():
            child = self.vlayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        header = QLabel(f"<h2>{w.title}</h2><p style='color:#2b6cb0; font-weight:bold;'>{w.decree_type}</p><p style='font-size:10pt; line-height:1.4; color:#4a5568;'>{w.summary}</p>")
        header.setWordWrap(True)
        self.vlayout.addWidget(header)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.vlayout.addWidget(line)

        for stage in w.stages:
            stage_box = QGroupBox(f"Stage {stage.stage_number}: {stage.title}")
            stage_box.setStyleSheet("QGroupBox { font-weight: bold; color: #1a365d; font-size: 10.5pt; }")
            s_layout = QVBoxLayout(stage_box)

            meta = QLabel(f"<span style='background:#edf2f7; color:#2d3748; padding:3px 8px; border-radius:4px; font-weight:bold;'>Rules: {stage.governing_rules}</span> &nbsp; "
                          f"<span style='background:#feebc8; color:#7b341e; padding:3px 8px; border-radius:4px; font-weight:bold;'>Limitation: {stage.limitation_period}</span>")
            meta.setWordWrap(True)
            s_layout.addWidget(meta)

            act_header = QLabel("<b>Actions Required:</b>")
            s_layout.addWidget(act_header)
            for act in stage.actions_required:
                a_label = QLabel(f"  • {act}")
                a_label.setWordWrap(True)
                s_layout.addWidget(a_label)

            if stage.statutory_provisos:
                prov_box = QLabel("<b>Statutory Provisos & Caveats:</b><br>" + "<br>".join(f"  ⚠️ {p}" for p in stage.statutory_provisos))
                prov_box.setWordWrap(True)
                prov_box.setStyleSheet("color: #742a2a; background: #fff5f5; padding: 6px; border-left: 3px solid #e53e3e;")
                s_layout.addWidget(prov_box)

            tact_box = QLabel(f"<b>💡 Advocate Tactic:</b> {stage.advocate_tactics}")
            tact_box.setWordWrap(True)
            tact_box.setStyleSheet("color: #2c5282; background: #ebf8ff; padding: 6px; border-left: 3px solid #3182ce;")
            s_layout.addWidget(tact_box)

            self.vlayout.addWidget(stage_box)

        conn_box = QGroupBox("🔗 Connected Order XXI Rules & Limitation Articles")
        conn_layout = QHBoxLayout(conn_box)
        for cp in w.connected_provisions:
            btn = QPushButton(cp["ref"])
            btn.setToolTip(cp.get("title", ""))
            btn.clicked.connect(lambda checked=False, target=cp: self._jump_to_provision(target))
            conn_layout.addWidget(btn)
        conn_layout.addStretch(1)
        self.vlayout.addWidget(conn_box)

    def _jump_to_provision(self, cp):
        ref_text = cp["ref"]
        if "Section" in ref_text:
            s_no = ref_text.replace("Section", "").strip().split()[0]
            if cp.get("kind") == "limitation_section":
                row = self.db.get_limitation_section_by_no(s_no)
                if row:
                    self.on_jump("limitation_section", row["id"])
                    return
            else:
                row = self.db.get_section_by_no(s_no)
                if row:
                    self.on_jump("section", row["id"])
                    return
        elif "Article" in ref_text:
            a_no = ref_text.replace("Article", "").strip().split("(")[0].strip()
            row = self.db.find_article_by_no(a_no)
            if row:
                self.on_jump("limitation_article", row["id"])
                return
        elif "Order" in ref_text and "Rule" in ref_text:
            parts = ref_text.replace("Order", "").split("Rule")
            o_no = parts[0].strip()
            r_no = parts[1].strip().split("(")[0].strip()
            row = self.db.find_rule_in_order(o_no, r_no)
            if row:
                self.on_jump("rule", row["id"])
                return
        elif "Order" in ref_text:
            o_no = ref_text.replace("Order", "").strip()
            row = self.db.find_order_by_no(o_no)
            if row:
                self.on_jump("order", row["id"])
                return


class AddCaseDialog(QDialog):
    """Dialog to add a new litigation matter into the Case Diary."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Case to Chamber Diary")
        self.resize(500, 480)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.case_no = QLineEdit()
        self.case_no.setPlaceholderText("e.g. O.S. No. 124 of 2025")
        form.addRow("Case Number*:", self.case_no)

        self.court_name = QLineEdit()
        self.court_name.setPlaceholderText("e.g. Court of Principal Senior Civil Judge, Bangalore")
        form.addRow("Court Name*:", self.court_name)

        self.client_name = QLineEdit()
        self.client_name.setPlaceholderText("e.g. Ramesh Kumar")
        form.addRow("Client Name*:", self.client_name)

        self.client_role = QComboBox()
        self.client_role.addItems(["Plaintiff", "Defendant", "Appellant", "Respondent", "Decree Holder", "Judgment Debtor"])
        form.addRow("Client Role:", self.client_role)

        self.opposite_party = QLineEdit()
        self.opposite_party.setPlaceholderText("e.g. Suresh Patel")
        form.addRow("Opposite Party:", self.opposite_party)

        self.opposite_counsel = QLineEdit()
        self.opposite_counsel.setPlaceholderText("e.g. Adv. R.K. Sharma")
        form.addRow("Opposite Counsel:", self.opposite_counsel)

        self.stage = QComboBox()
        self.stage.addItems(cs.CIVIL_STAGES)
        form.addRow("Current Stage:", self.stage)

        self.next_date = QDateEdit(calendarPopup=True)
        self.next_date.setDate(date.today())
        form.addRow("Next Hearing Date:", self.next_date)

        self.notes = QPlainTextEdit()
        self.notes.setPlaceholderText("Brief facts, claim value, interlocutory applications, etc.")
        self.notes.setMaximumHeight(80)
        form.addRow("Brief Notes:", self.notes)

        layout.addLayout(form)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self._validate_and_accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _validate_and_accept(self):
        if not self.case_no.text().strip() or not self.court_name.text().strip() or not self.client_name.text().strip():
            QMessageBox.warning(self, "Required Fields", "Please enter Case Number, Court Name, and Client Name.")
            return
        self.accept()

    def get_data(self):
        qd = self.next_date.date()
        return {
            "case_no": self.case_no.text().strip(),
            "court_name": self.court_name.text().strip(),
            "client_name": self.client_name.text().strip(),
            "client_role": self.client_role.currentText(),
            "opposite_party": self.opposite_party.text().strip(),
            "opposite_counsel": self.opposite_counsel.text().strip(),
            "stage": self.stage.currentText(),
            "next_date": f"{qd.year():04d}-{qd.month():02d}-{qd.day():02d}",
            "notes": self.notes.toPlainText().strip()
        }


class AddHearingDialog(QDialog):
    """Dialog to record court proceedings and set next hearing date."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Record Court Hearing / Daily Order")
        self.resize(450, 320)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.hearing_date = QDateEdit(calendarPopup=True)
        self.hearing_date.setDate(date.today())
        form.addRow("Hearing Date:", self.hearing_date)

        self.business_done = QPlainTextEdit()
        self.business_done.setPlaceholderText("e.g. Issues framed. PW-1 affidavit filed. Adjourned for cross-examination.")
        self.business_done.setMaximumHeight(80)
        form.addRow("Daily Order / Business Done:", self.business_done)

        self.next_date = QDateEdit(calendarPopup=True)
        self.next_date.setDate(date.today())
        form.addRow("Next Hearing Date:", self.next_date)

        self.next_purpose = QLineEdit()
        self.next_purpose.setPlaceholderText("e.g. For Cross-examination of PW-1")
        form.addRow("Next Stage / Purpose:", self.next_purpose)

        layout.addLayout(form)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_data(self):
        hd = self.hearing_date.date()
        nd = self.next_date.date()
        return {
            "hearing_date": f"{hd.year():04d}-{hd.month():02d}-{hd.day():02d}",
            "business_done": self.business_done.toPlainText().strip(),
            "next_date": f"{nd.year():04d}-{nd.month():02d}-{nd.day():02d}",
            "next_purpose": self.next_purpose.text().strip()
        }


class CaseDiaryTab(QWidget):
    """Advocate Case Diary & Hearing Timeline Tracker."""

    def __init__(self, db: ActDatabase):
        super().__init__()
        self.db = db
        self.current_case_id = None

        layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        # Left panel: Add button, filter, case list
        left = QWidget()
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)

        add_btn = QPushButton("➕ Add New Case")
        add_btn.setStyleSheet("font-weight: bold; background: #2b6cb0; color: white; padding: 6px;")
        add_btn.clicked.connect(self._add_case)
        left_layout.addWidget(add_btn)

        self.stage_filter = QComboBox()
        self.stage_filter.addItem("All Stages", None)
        for st in cs.CIVIL_STAGES:
            self.stage_filter.addItem(st, st)
        self.stage_filter.currentIndexChanged.connect(self._refresh_list)
        left_layout.addWidget(self.stage_filter)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search by Case No / Client Name...")
        self.search_box.textChanged.connect(self._refresh_list)
        left_layout.addWidget(self.search_box)

        self.case_list = QListWidget()
        self.case_list.itemClicked.connect(self._on_case_selected)
        left_layout.addWidget(self.case_list, stretch=1)
        splitter.addWidget(left)

        # Right panel: Case details, deadline advice, hearing log
        right = QWidget()
        rlayout = QVBoxLayout(right)

        # Case title bar
        self.title_label = QLabel("Select a case from the list or click 'Add New Case'")
        self.title_label.setStyleSheet("font-weight: 600; font-size: 13pt; color: #1a365d;")
        self.title_label.setWordWrap(True)
        rlayout.addWidget(self.title_label)

        self.meta_label = QLabel("")
        self.meta_label.setStyleSheet("color: #4a5568; font-size: 9.5pt;")
        self.meta_label.setWordWrap(True)
        rlayout.addWidget(self.meta_label)

        # Statutory Deadline Advice Box
        self.advice_box = QGroupBox("⚖️ Statutory Next-Step & Deadline Alert")
        self.advice_box.setStyleSheet("QGroupBox { font-weight: bold; color: #2b6cb0; }")
        adv_layout = QVBoxLayout(self.advice_box)
        self.advice_label = QLabel("Automatic statutory deadline advice appears here based on the case stage.")
        self.advice_label.setWordWrap(True)
        self.advice_label.setStyleSheet("color: #2d3748; line-height: 1.4;")
        adv_layout.addWidget(self.advice_label)
        rlayout.addWidget(self.advice_box)

        # Toolbar
        tbar = QHBoxLayout()
        self.record_hearing_btn = QPushButton("➕ Record Court Hearing")
        self.record_hearing_btn.setStyleSheet("font-weight: bold; padding: 5px 10px;")
        self.record_hearing_btn.clicked.connect(self._record_hearing)
        tbar.addWidget(self.record_hearing_btn)

        self.delete_btn = QPushButton("🗑️ Delete Case")
        self.delete_btn.setStyleSheet("color: #c53030; padding: 5px 10px;")
        self.delete_btn.clicked.connect(self._delete_case)
        tbar.addWidget(self.delete_btn)
        tbar.addStretch(1)
        rlayout.addLayout(tbar)

        # Hearings history table
        h_label = QLabel("<b>Court Hearings & Daily Orders History:</b>")
        rlayout.addWidget(h_label)

        self.hearings_table = QTableWidget(0, 4)
        self.hearings_table.setHorizontalHeaderLabels(["Hearing Date", "Proceedings / Business Done", "Next Date", "Next Purpose"])
        self.hearings_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        rlayout.addWidget(self.hearings_table, stretch=1)

        splitter.addWidget(right)
        splitter.setSizes([320, 680])

        self._refresh_list()
        if self.case_list.count() > 0:
            self.case_list.setCurrentRow(0)
            self._on_case_selected(self.case_list.item(0))

    def _refresh_list(self):
        self.case_list.clear()
        stage = self.stage_filter.currentData()
        q = self.search_box.text().strip().lower()
        rows = self.db.all_cases(stage=stage)
        for r in rows:
            if q and q not in r["case_no"].lower() and q not in r["client_name"].lower() and q not in r["opposite_party"].lower():
                continue
            posting = f"Posting: {r['next_date']}" if r["next_date"] else "No date"
            it = QListWidgetItem(f"{r['case_no']}  [{posting}]\n{r['client_name']} ({r['client_role']}) vs {r['opposite_party'] or 'Opposite'}\nStage: {r['stage']}")
            it.setData(Qt.UserRole, r["id"])
            self.case_list.addItem(it)

    def _on_case_selected(self, item):
        cid = item.data(Qt.UserRole)
        self.current_case_id = cid
        c = self.db.get_case(cid)
        if not c:
            return

        self.title_label.setText(f"{c['case_no']} &mdash; {c['court_name']}")
        self.meta_label.setText(
            f"<b>Client:</b> {c['client_name']} (<b>{c['client_role']}</b>) &nbsp;|&nbsp; "
            f"<b>Opposite Party:</b> {c['opposite_party'] or '—'} &nbsp;|&nbsp; "
            f"<b>Opposite Counsel:</b> {c['opposite_counsel'] or '—'}<br>"
            f"<b>Current Stage:</b> {c['stage']} &nbsp;|&nbsp; <b>Next Hearing:</b> {c['next_date'] or 'Not fixed'}"
        )

        # Statutory deadline computation
        adv = cs.suggest_statutory_deadline(c["stage"])
        warn_html = f"<br><span style='color:#c53030;'>⚠️ <b>Warning:</b> {adv.warning}</span>" if adv.warning else ""
        self.advice_label.setText(
            f"<b>Governing Rule:</b> {adv.statutory_rule} &nbsp; ({adv.period_str})<br>"
            f"{adv.advice}{warn_html}"
        )

        # Load hearings
        hearings = self.db.hearings_for_case(cid)
        self.hearings_table.setRowCount(len(hearings))
        for i, h in enumerate(hearings):
            self.hearings_table.setItem(i, 0, QTableWidgetItem(h["hearing_date"]))
            self.hearings_table.setItem(i, 1, QTableWidgetItem(h["business_done"]))
            self.hearings_table.setItem(i, 2, QTableWidgetItem(h["next_date"]))
            self.hearings_table.setItem(i, 3, QTableWidgetItem(h["next_purpose"]))

    def _add_case(self):
        dlg = AddCaseDialog(self)
        if dlg.exec() == QDialog.Accepted:
            data = dlg.get_data()
            cid = self.db.add_case(**data)
            self._refresh_list()
            # Select new case
            for i in range(self.case_list.count()):
                if self.case_list.item(i).data(Qt.UserRole) == cid:
                    self.case_list.setCurrentRow(i)
                    self._on_case_selected(self.case_list.item(i))
                    break

    def _record_hearing(self):
        if not self.current_case_id:
            QMessageBox.information(self, "No Case Selected", "Please select a case to record a hearing.")
            return
        dlg = AddHearingDialog(self)
        if dlg.exec() == QDialog.Accepted:
            data = dlg.get_data()
            self.db.add_hearing(self.current_case_id, **data)
            self._refresh_list()
            # Re-select current case
            for i in range(self.case_list.count()):
                if self.case_list.item(i).data(Qt.UserRole) == self.current_case_id:
                    self.case_list.setCurrentRow(i)
                    self._on_case_selected(self.case_list.item(i))
                    break

    def _delete_case(self):
        if not self.current_case_id:
            return
        ret = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this case and its hearing history?")
        if ret == QMessageBox.Yes:
            self.db.delete_case(self.current_case_id)
            self.current_case_id = None
            self._refresh_list()
            if self.case_list.count() > 0:
                self.case_list.setCurrentRow(0)
                self._on_case_selected(self.case_list.item(0))
            else:
                self.title_label.setText("No cases in diary.")
                self.meta_label.setText("")
                self.advice_label.setText("")
                self.hearings_table.setRowCount(0)


class BookmarksTab(QWidget):
    def __init__(self, db: ActDatabase, on_jump):
        super().__init__()
        self.db = db
        self.on_jump = on_jump
        layout = QVBoxLayout(self)
        refresh = QPushButton("Refresh Bookmarks")
        refresh.clicked.connect(self._refresh)
        layout.addWidget(refresh)
        self.list = QListWidget()
        self.list.itemDoubleClicked.connect(self._on_activated)
        layout.addWidget(self.list, stretch=1)
        self._refresh()

    def _refresh(self):
        self.list.clear()
        for bm in self.db.all_bookmarks():
            kind, ref_id = bm["kind"], bm["ref_id"]
            label = self._label_for(kind, ref_id)
            li = QListWidgetItem(label)
            li.setData(Qt.UserRole, (kind, ref_id))
            self.list.addItem(li)

    def _label_for(self, kind, ref_id):
        if kind == "section":
            row = self.db.get_section(ref_id)
            return f"[CPC Section] S.{row['section_no']} — {row['title']}" if row else "[Section] (missing)"
        if kind == "rule":
            row = self.db.get_rule(ref_id)
            if not row:
                return "[Rule] (missing)"
            order = self.db.get_order(row["order_id"])
            return f"[CPC Rule] O.{order['order_no']} R.{row['rule_no']} — {row['title']}"
        if kind == "appendix":
            row = self.db.get_appendix(ref_id)
            return f"[CPC Appendix] {row['letter']}" if row else "[Appendix] (missing)"
        if kind == "limitation_section":
            row = self.db.get_limitation_section(ref_id)
            return f"[Limitation S.] S.{row['section_no']} — {row['title']}" if row else "[Limitation Section] (missing)"
        if kind == "limitation_article":
            row = self.db.get_limitation_article(ref_id)
            return f"[Limitation Art.] Art.{row['article_no']} ({row['period']})" if row else "[Limitation Article] (missing)"
        return kind

    def _on_activated(self, item):
        data = item.data(Qt.UserRole)
        if data:
            self.on_jump(*data)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LexOffline — CPC 1908 & Limitation Act 1963 Practice Module")
        self.resize(1200, 800)

        self.db = ActDatabase()

        tabs = QTabWidget()
        self.setCentralWidget(tabs)

        self.explorer = ExplorerTab(self.db)
        tabs.addTab(self.explorer, "Act Explorer (CPC & Limitation)")

        self.diary_tab = CaseDiaryTab(self.db)
        tabs.addTab(self.diary_tab, "Case Diary")

        self.checklists_tab = ChecklistsTab(self.db, self._jump)
        tabs.addTab(self.checklists_tab, "Practice Checklists")

        self.templates_tab = DraftingTemplatesTab(self.db, self._jump)
        tabs.addTab(self.templates_tab, "Drafting Templates")

        self.execution_tab = ExecutionNavigatorTab(self.db, self._jump)
        tabs.addTab(self.execution_tab, "Execution Navigator")

        self.search_tab = SearchTab(self.db, self._jump)
        tabs.addTab(self.search_tab, "Search")

        self.bookmarks_tab = BookmarksTab(self.db, self._jump)
        tabs.addTab(self.bookmarks_tab, "Bookmarks")

        self.deadline_tab = DeadlineTrackerTab()
        tabs.addTab(self.deadline_tab, "Deadline & Limitation Tracker")

        self.tabs = tabs

    def _jump(self, kind, ref_id):
        self.tabs.setCurrentWidget(self.explorer)
        self.explorer.jump_to(kind, ref_id)

    def closeEvent(self, event):
        self.db.close()
        super().closeEvent(event)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("LexOffline")
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
