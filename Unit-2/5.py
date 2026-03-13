'''Write a program to read a file and display its contents. At the end it shall
also display no. of words available in file.'''
# open the file in read mode
file = open("sample.txt", "r")

# read the content of the file
content = file.read()

# display file content
print("File Content:\n")
print(content)

# count words
words = content.split()
word_count = len(words)

# display number of words
print("\nTotal number of words in file:", word_count)

# close the file
file.close()
