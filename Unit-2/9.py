import os

filename = "students.txt"

while True:
    print("\n--- Student Menu ---")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Update Student")
    print("e) Delete Student")
    print("f) Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == 'a':
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")

        file = open(filename, "a")
        file.write(str(roll) + "," + name + "\n")
        file.close()

        print("Student added successfully")

    # Search Student
    elif choice == 'b':
        roll = int(input("Enter Roll No to search: "))
        file = open(filename, "r")

        found = False
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll:
                print("Roll No:", data[0], "Name:", data[1])
                found = True

        if not found:
            print("Student not found")

        file.close()

    # List All Students
    elif choice == 'c':
        file = open(filename, "r")

        for line in file:
            data = line.strip().split(",")
            print("Roll No:", data[0], "Name:", data[1])

        file.close()

    # Update Student
    elif choice == 'd':
        roll = int(input("Enter Roll No to update: "))
        newname = input("Enter new name: ")

        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        file = open(filename, "w")

        for line in lines:
            data = line.strip().split(",")
            if data[0] == roll:
                file.write(roll + "," + newname + "\n")
            else:
                file.write(line)

        file.close()
        print("Student updated")

    # Delete Student
    elif choice == 'e':
        roll = int(input("Enter Roll No to delete: "))

        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        file = open(filename, "w")

        for line in lines:
            data = line.strip().split(",")
            if data[0] != roll:
                file.write(line)

        file.close()
        print("Student deleted")

    # Exit
    elif choice == 'f':
        print("Program exited")
        break

    else:
        print("Invalid choice")
