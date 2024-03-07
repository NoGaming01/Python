"""This is a File Manipulator programme"""

def divider(n = 100):
    print("-" * n)

try:
    file = open("FileManipulator/readfile.txt", "x")
    print("Read file has been made.")
    divider()
    file.close()
except FileExistsError:
    print("File already Exists. Skipping this ;)")
    divider()

try:
    file = open("FileManipulator/readfile.txt", "r")
    print(file.read())
    divider()
    file.close()
except FileNotFoundError:
    print("You forgot to make the file my boy :) or you typed the name wrong ;)")
    divider()

try:
    file = open("FileManipulator/writefile.txt", "w")
    text = "Hello I am Skele.\nAnd I am writing few things in the file.\nI guess You will like this.\n:) ;) :-) idk ...\nHello and Bye."

    file.write(text)
    print("File has been written.")
    divider()
    file.close()
except Exception as e:
    print(f"An error occured.\n{e}")
    divider()

try:
    file = open("FileManipulator/writefile.txt", "r")
    print(file.read())
    divider()
    file.close()
except FileNotFoundError:
    print("You forgot to make the file my boy :) or you typed the name wrong ;)")
    divider()
