import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Show all tables in the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())

conn.close()