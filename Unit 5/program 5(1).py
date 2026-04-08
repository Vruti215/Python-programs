import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Ask user for roll number
roll = input("Enter Roll No to update: ")

# Collect new details
new_name   = input("Enter new name: ")
new_gender = input("Enter new gender: ")
new_age    = int(input("Enter new age: "))
new_email  = input("Enter new email: ")
new_mobile = input("Enter new mobile: ")
new_city   = input("Enter new city: ")

# Update all fields
cur.execute("""
UPDATE student
SET name = ?, gender = ?, age = ?, email = ?, mobile = ?, city = ?
WHERE rollno = ?
""", (new_name, new_gender, new_age, new_email, new_mobile, new_city, roll))

conn.commit()
conn.close()

print("Student details updated successfully.")
