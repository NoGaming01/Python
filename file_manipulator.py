"""This is a File Manipulator programme"""

try:
    file = open("FileManipulator/readfile.txt", "x")
    print("Read file has been made.")
    file.close()
except FileExistsError:
    print("File already Exists. Skipping this ;)")
    print("-" * 100)

try:
    file = open("FileManipulator/filerad.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("You forgot to make the file my boy :) or you typed the name wrong ;)")
