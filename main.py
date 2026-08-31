#!/usr/bin/env python3
"""
LexOffline — CPC, 1908 Practice Module
Desktop app (PySide6 + local SQLite). Deterministic only: every screen
reads from the local database or does plain date/text arithmetic.
Nothing here is generated or inferred by a model.
"""
import sys
from datetime import date

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTreeWidget, QTreeWidgetItem, QTextBrowser, QLineEdit, QLabel,
    QSplitter, QTabWidget, QListWidget, QListWidgetItem, QPushButton,
    QDateEdit, QComboBox, QFormLayout, QPlainTextEdit, QMessageBox,
)

from db import ActDatabase
from xref import extract_refs, resolve_refs
import deadlines as dl


def html_escape(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class ExplorerTab(QWidget):
    """Tree navigation over Sections / Orders+Rules / Appendices, with a
    provision viewer, deterministic cross-references, bookmark toggle,
    and a notes box."""

    def __init__(self, db: ActDatabase):
        super().__init__()
        self.db = db
        self.current = None  # ("section", id) or ("rule", id) or ("appendix", id)

        layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Horizontal)
        layout.addWidget(splitter)

        # --- left: tree ---
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Provision"])
        self.tree.itemClicked.connect(self._on_tree_click)
        splitter.addWidget(self.tree)
        self._populate_tree()

        # --- right: viewer ---
        right = QWidget()
        rlayout = QVBoxLayout(right)
        self.title_label = QLabel("Select a provision")
        self.title_label.setStyleSheet("font-weight: 600; font-size: 14pt;")
        rlayout.addWidget(self.title_label)

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
        tabs.addTab(self.xref_list, "Cross-References")

        self.notes_box = QPlainTextEdit()
        self.notes_box.textChanged.connect(self._on_notes_changed)
        tabs.addTab(self.notes_box, "Notes")

        rlayout.addWidget(right) if False else None
        splitter.addWidget(right)
        splitter.setSizes([320, 680])

        self._loading_notes = False

    # ---------- tree population ----------
    def _populate_tree(self):
        self.tree.clear()

        sec_root = QTreeWidgetItem(["Sections (1–158)"])
        self.tree.addTopLevelItem(sec_root)
        parts = self.db.sections_by_part()
        for part, rows in parts.items():
            part_item = QTreeWidgetItem([f"Part {part}"])
            sec_root.addChild(part_item)
            for r in rows:
                it = QTreeWidgetItem([f"S.{r['section_no']} — {r['title']}"])
                it.setData(0, Qt.UserRole, ("section", r["id"]))
                part_item.addChild(it)

        ord_root = QTreeWidgetItem(["Orders (I–LI)"])
        self.tree.addTopLevelItem(ord_root)
        for o in self.db.all_orders():
            o_item = QTreeWidgetItem([f"Order {o['order_no']} — {o['title']}"])
            o_item.setData(0, Qt.UserRole, ("order", o["id"]))
            ord_root.addChild(o_item)
            for r in self.db.rules_for_order(o["id"]):
                rit = QTreeWidgetItem([f"R.{r['rule_no']} — {r['title']}"])
                rit.setData(0, Qt.UserRole, ("rule", r["id"]))
                o_item.addChild(rit)

        app_root = QTreeWidgetItem(["Appendices (A–I)"])
        self.tree.addTopLevelItem(app_root)
        for a in self.db.all_appendices():
            it = QTreeWidgetItem([f"Appendix {a['letter']}"])
            it.setData(0, Qt.UserRole, ("appendix", a["id"]))
            app_root.addChild(it)

    def _on_tree_click(self, item, _col):
        data = item.data(0, Qt.UserRole)
        if not data:
            return
        kind, ref_id = data
        if kind == "order":
            row = self.db.get_order(ref_id)
            self._show(kind, ref_id, row["title"], f"Order {row['order_no']} — {row['title']}\n\n(Select a Rule under this Order for full text.)")
            return
        self._load_and_show(kind, ref_id)

    # ---------- viewer ----------
    def _load_and_show(self, kind, ref_id):
        if kind == "section":
            row = self.db.get_section(ref_id)
            title = f"Section {row['section_no']} — {row['title']}"
            body = row["text"]
            if row["state_amendments"]:
                body += "\n\n--- STATE AMENDMENTS ---\n" + row["state_amendments"]
        elif kind == "rule":
            row = self.db.get_rule(ref_id)
            order = self.db.get_order(row["order_id"])
            title = f"Order {order['order_no']} Rule {row['rule_no']} — {row['title']}"
            body = row["text"]
            if row["state_amendments"]:
                body += "\n\n--- STATE AMENDMENTS ---\n" + row["state_amendments"]
        elif kind == "appendix":
            row = self.db.get_appendix(ref_id)
            title = f"Appendix {row['letter']}"
            body = row["text"]
        else:
            return
        self._show(kind, ref_id, title, body)

    def _show(self, kind, ref_id, title, body):
        self.current = (kind, ref_id)
        self.title_label.setText(title)
        self.text_view.setHtml(f"<pre style='white-space:pre-wrap; font-family:inherit;'>{html_escape(body)}</pre>")

        # cross-references (deterministic regex, resolved locally)
        self.xref_list.clear()
        if kind in ("section", "rule"):
            self_kind = "section" if kind == "section" else None
            self_ref = None
            if kind == "section":
                row = self.db.get_section(ref_id)
                self_ref = row["section_no"]
            refs = extract_refs(body, self_kind=self_kind, self_ref=self_ref)
            resolved = resolve_refs(self.db, refs)
            if not resolved:
                self.xref_list.addItem("(no cross-references detected in this text)")
            for r in resolved:
                found = "✓" if r["target"] else "✗ not in local database"
                li = QListWidgetItem(f"{r['label']}  [{found}]")
                li.setData(Qt.UserRole, r)
                self.xref_list.addItem(li)
        else:
            self.xref_list.addItem("(cross-references apply to Sections and Rules)")

        # bookmark state
        bm = self.db.is_bookmarked(kind, ref_id)
        self.bookmark_btn.setText("★ Bookmarked" if bm else "☆ Bookmark")

        # notes
        self._loading_notes = True
        self.notes_box.setPlainText(self.db.get_note(kind, ref_id))
        self._loading_notes = False

    def _on_xref_activated(self, item):
        r = item.data(Qt.UserRole)
        if not r or not r.get("target"):
            return
        if r["target_kind"] == "section":
            self._load_and_show("section", r["target"]["id"])
        elif r["target_kind"] == "rule":
            self._load_and_show("rule", r["target"]["id"])
        elif r["target_kind"] == "order":
            row = r["target"]
            self._show("order", row["id"], f"Order {row['order_no']} — {row['title']}",
                        f"Order {row['order_no']} — {row['title']}\n\n(Select a Rule under this Order for full text.)")

    def _on_anchor_clicked(self, url):
        pass  # reserved for future inline-link jumps

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
        self.box.setPlaceholderText("Search by keyword, e.g. injunction, attachment, caveat, Section 80 …")
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
            self.results.addItem("(no matches)")
            return
        for r in rows:
            li = QListWidgetItem(f"[{r['kind']}] {r['label']}  —  {r['snip']}")
            li.setData(Qt.UserRole, (r["kind"], r["ref_id"]))
            self.results.addItem(li)

    def _on_result_activated(self, item):
        data = item.data(Qt.UserRole)
        if data:
            self.on_jump(*data)


class DeadlineTrackerTab(QWidget):
    """Deterministic deadline calculator — Part 6, Screen 2 of the spec."""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        form = QFormLayout()
        self.trigger_date = QDateEdit(calendarPopup=True)
        self.trigger_date.setDate(date.today())
        form.addRow("Trigger date (e.g. date of service):", self.trigger_date)

        self.rule_combo = QComboBox()
        for r in dl.list_rules():
            self.rule_combo.addItem(f"{r.label}  [{r.provision}]", r.key)
        form.addRow("Deadline type:", self.rule_combo)

        layout.addLayout(form)

        calc_btn = QPushButton("Calculate")
        calc_btn.clicked.connect(self._calculate)
        layout.addWidget(calc_btn)

        self.result_label = QLabel("")
        self.result_label.setStyleSheet("font-size: 13pt; font-weight: 600; padding: 12px;")
        layout.addWidget(self.result_label)

        warn = QLabel(
            "Note: these are the general Central Act timelines. Always verify "
            "against the section text and applicable state amendment — some "
            "periods (e.g. Order VIII Rule 1) vary by state or by whether the "
            "suit is a commercial suit."
        )
        warn.setWordWrap(True)
        warn.setStyleSheet("color: #a33; padding: 8px;")
        layout.addWidget(warn)
        layout.addStretch(1)

    def _calculate(self):
        key = self.rule_combo.currentData()
        qd = self.trigger_date.date()
        trigger = date(qd.year(), qd.month(), qd.day())
        result = dl.compute(trigger, key)
        due = result["due_date"]
        self.result_label.setText(
            f"Due date: {due.strftime('%d %B %Y')}  "
            f"({result['days']} days from {trigger.strftime('%d %B %Y')}, {result['rule'].provision})"
        )


class BookmarksTab(QWidget):
    def __init__(self, db: ActDatabase, on_jump):
        super().__init__()
        self.db = db
        self.on_jump = on_jump
        layout = QVBoxLayout(self)
        refresh = QPushButton("Refresh")
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
            return f"[Section] S.{row['section_no']} — {row['title']}" if row else "[Section] (missing)"
        if kind == "rule":
            row = self.db.get_rule(ref_id)
            if not row:
                return "[Rule] (missing)"
            order = self.db.get_order(row["order_id"])
            return f"[Rule] O.{order['order_no']} R.{row['rule_no']} — {row['title']}"
        if kind == "appendix":
            row = self.db.get_appendix(ref_id)
            return f"[Appendix] {row['letter']}" if row else "[Appendix] (missing)"
        return kind

    def _on_activated(self, item):
        data = item.data(Qt.UserRole)
        if data:
            self.on_jump(*data)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LexOffline — CPC, 1908")
        self.resize(1200, 800)

        self.db = ActDatabase()

        tabs = QTabWidget()
        self.setCentralWidget(tabs)

        self.explorer = ExplorerTab(self.db)
        tabs.addTab(self.explorer, "Act Explorer")

        self.search_tab = SearchTab(self.db, self._jump)
        tabs.addTab(self.search_tab, "Search")

        self.bookmarks_tab = BookmarksTab(self.db, self._jump)
        tabs.addTab(self.bookmarks_tab, "Bookmarks")

        self.deadline_tab = DeadlineTrackerTab()
        tabs.addTab(self.deadline_tab, "Deadline Tracker")

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
