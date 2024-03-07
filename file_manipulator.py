"""This is programe to Manipulate files."""

from typing import IO
import time

def get_file(file_location: str) -> IO[str]:
    file: IO[str] = open(file_location, "r")
    return file

def file_size(file: IO[str]) -> int:
    size: int = file.tell()
    return size

print("Welcome to File Manipulator Programe.")
print("*" * 100)

print("Please enter the location of the file.")
file_location: str = input("> ")

file: IO[str] = get_file(file_location)

print("We are processing the things wait...")
time.sleep(5)

print("We have the information of the file.")
print("Giving the information...")
time.sleep(3)

print(f"The name of the file is {file.name}")
time.sleep(3)

print(f"The size of the file is {file_size(file)} bytes.")

file.close()
