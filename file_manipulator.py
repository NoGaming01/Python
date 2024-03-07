"""This is programe to Manipulate files."""

from typing import IO, Callable
import time

commands_dictionary: dict = {}

def get_file(file_location: str, mode: str) -> IO[str]:
    try:
        file: IO[str] = open(file_location, mode)
        return file
    except FileExistsError:
        return f"File on the path '{file_location}' is already there."
    except FileNotFoundError:
        return f"File on the path '{file_location}' does not exists."
    except Exception as e:
        return f"An error occured\nError: {e}"

def file_size(file: IO[str]) -> int:
    size: int = file.tell()
    return size

def command(name: str) -> None:

    def decorator(func: Callable) -> Callable:
        if name in commands_dictionary:
            print(f"The command '{name}' can't be added twice.")
            return
        
        commands_dictionary[name] = func.__name__

    return decorator

print("Welcome to File Manipulator Programe.")
print("*" * 100)

print("Please enter the location of the file.")
file_location: str = input("> ")

file_mode: str = input("> ")

file: IO[str] = get_file(file_location, file_mode)

print("We are processing the things wait...")
time.sleep(5)

print("We have the information of the file.")
print("Giving the information...")
time.sleep(3)

print(f"The name of the file is {file.name}")
time.sleep(3)

print(f"The size of the file is {file_size(file)} bytes.")

file.close()
