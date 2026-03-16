import zipfile

# create zip file
with zipfile.ZipFile("myfiles.zip", "w") as z:
    z.write("file1.txt")
    z.write("file2.txt")

print("Files zipped successfully")

with zipfile.ZipFile("myfiles.zip", "r") as z:
    z.extractall()

print("Files unzipped successfully")
