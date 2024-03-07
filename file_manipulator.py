"""This is a File Manipulator programme"""

try:
    file = open("FileManipulator/readfile.txt", "x")
    print("Read file has been made.")
    file.close()
except FileExistsError:
    print("File already Exists. Skipping this ;)")
    print("-" * 100)

file = open("FileManipulator/readfile.txt", "r")
print(file.read())
file.close()
