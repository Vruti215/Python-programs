# open file in read mode
file = open("students.txt", "r")

for line in file:
    data = line.strip().split(",")
    
    rollno = data[0]
    name = data[1]
    m1 = int(data[2])
    m2 = int(data[3])
    m3 = int(data[4])
    m4 = int(data[5])
    
    total = m1 + m2 + m3 + m4
    percentage = total / 4

    # grade calculation
    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

    print("Roll No:", rollno)
    print("Name:", name)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("----------------------")

file.close()
