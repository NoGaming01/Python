"""This is programe to Manipulate files."""

from typing import IO

def get_file(file_location: str) -> IO[str]:
    file: IO[str] = open(file_location, "r")
    return file

def file_size(file: IO[str]) -> int:
    size: int = file.tell()
    return size

read_file: IO[str] = get_file("FileManipulator/readfile.txt")

print(read_file.read())
print(f"{file_size(read_file)} Bytes")

read_file.close()
