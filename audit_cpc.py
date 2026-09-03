import sqlite3

con = sqlite3.connect('cpc_1908.db')
cur = con.cursor()

tables = [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
print("Tables in DB:", tables)

print("\n--- BARE ACT STATS ---")
print("CPC Sections in DB:", cur.execute("SELECT count(*) FROM sections").fetchone()[0])
print("CPC Orders in DB:", cur.execute("SELECT count(*) FROM orders").fetchone()[0])
print("CPC Rules in DB:", cur.execute("SELECT count(*) FROM rules").fetchone()[0])
print("Limitation Sections:", cur.execute("SELECT count(*) FROM limitation_sections").fetchone()[0])
print("Limitation Articles:", cur.execute("SELECT count(*) FROM limitation_articles").fetchone()[0])
print("SRA Sections:", cur.execute("SELECT count(*) FROM sra_sections").fetchone()[0])

print("\n--- APPENDICES IN DB ---")
appendices = cur.execute("SELECT letter, title, length(text) FROM appendices").fetchall()
for a in appendices:
    print(f"Appendix {a[0]}: {a[1]} ({a[2]} chars)")

# Check missing sections from 1 to 158
section_nos = set([r[0] for r in cur.execute("SELECT section_no FROM sections").fetchall()])
missing_sections = []
for i in range(1, 159):
    if str(i) not in section_nos and f"{i}A" not in section_nos and f"{i}B" not in section_nos:
        missing_sections.append(i)
print("\nSections 1-158 missing check:", missing_sections)

# Check orders from 1 to 51
order_nos = set([r[0] for r in cur.execute("SELECT order_no FROM orders").fetchall()])
print("Orders present:", sorted(list(order_nos)))
missing_orders = []
roman_orders = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", 
                "XI", "XII", "XIII", "XIII-A", "XIV", "XV", "XV-A", "XVI", "XVI-A", "XVII", 
                "XVIII", "XIX", "XX", "XXA", "XXI", "XXII", "XXIII", "XXIV", "XXV", 
                "XXVI", "XXVII", "XXVII-A", "XXVIII", "XXIX", "XXX", "XXXI", "XXXII", 
                "XXXIIA", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", 
                "XL", "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L", "LI"]
for ro in roman_orders:
    if ro not in order_nos:
        missing_orders.append(ro)
print("Missing Orders from list:", missing_orders)
