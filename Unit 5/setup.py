import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS student (
    rollno TEXT PRIMARY KEY,
    name TEXT,
    gender TEXT,
    age INTEGER,
    email TEXT,
    mobile TEXT,
    city TEXT
)
''')

conn.commit()
conn.close()
