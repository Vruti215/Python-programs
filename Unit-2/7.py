# open source file in read mode
f1 = open("source.txt", "r")

# open destination file in write mode
f2 = open("destination.txt", "w")

# read content from source and write to destination
for line in f1:
    f2.write(line)

# close both files
f1.close()
f2.close()

print("File copied successfully")
