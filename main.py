#!/usr/bin/env python3
"""
LexOffline — CPC, 1908 & The Limitation Act, 1963 Practice Module
Desktop app (PySide6 + local SQLite). Deterministic only: every screen
reads from the local database or does plain date/text arithmetic.
Nothing here is generated or inferred by a model.
"""
import sys
from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTreeWidget, QTreeWidgetItem, QTextBrowser, QLineEdit, QLabel,
    QSplitter, QTabWidget, QListWidget, QListWidgetItem, QPushButton,
    QDateEdit, QComboBox, QFormLayout, QPlainTextEdit, QMessageBox,
    QSpinBox, QGroupBox,
)

from db import ActDatabase
from xref import extract_refs, resolve_refs
from state_amend import KNOWN_STATES, states_present, text_for_state
import deadlines as dl


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

        # Toggle state amendment dropdown visibility
        self.state_row_widget.setVisible(not is_limitation and bool(state_blob))
        if not is_limitation and state_blob:
            self.state_combo.blockSignals(True)
            self.state_combo.setCurrentIndex(0)
            self.state_combo.blockSignals(False)

        self._render_text()

        # cross-references and limitation linkage
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

            # 1. In-text CPC xrefs
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

            # 2. Linked Limitation Act Articles
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

        # bookmark state
        bm = self.db.is_bookmarked(kind, ref_id)
        self.bookmark_btn.setText("★ Bookmarked" if bm else "☆ Bookmark")

        # notes
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

        # Category filter
        self.cat_combo = QComboBox()
        self.cat_combo.addItem("All Categories", None)
        for cat in dl.list_categories():
            self.cat_combo.addItem(cat, cat)
        self.cat_combo.currentIndexChanged.connect(self._on_category_changed)
        form.addRow("Category filter:", self.cat_combo)

        # Deadline Rule
        self.rule_combo = QComboBox()
        self._populate_rules()
        form.addRow("Rule / Limitation Article:", self.rule_combo)

        # Trigger date
        self.trigger_date = QDateEdit(calendarPopup=True)
        self.trigger_date.setDate(date.today())
        form.addRow("Trigger date (e.g. date of decree / death / notice):", self.trigger_date)

        # Section 12 Certified Copy Exclusion
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
