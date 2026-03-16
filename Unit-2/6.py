#Write a program to read a file which contains only numbers. Display total of all numbers with maximum and minimum number.

# Open the file
file = open("numbers.txt", "r")

numbers = []

# Read numbers from file
for line in file:
    line = line.strip()
    if line != "":
        numbers.append(int(line))
file.close()

# Calculate total, maximum and minimum
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Display results
print("Total =", total)
print("Maximum number =", maximum)
print("Minimum number =", minimum)
