import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Ask user for table name
table_name = input("Enter table name: ")

# Show columns
cur.execute(f"PRAGMA table_info({table_name})")
columns = cur.fetchall()
print("\nColumns:")
for col in columns:
    print(f"{col[1]} ({col[2]})")

# Show rows
cur.execute(f"SELECT * FROM {table_name}")
rows = cur.fetchall()

print("\nRows:")
for row in rows:
    print(row)

conn.close()
