"""This is programe to Manipulate files."""

from typing import IO, Callable

commands_dictionary: dict = {}

def get_file(file_location: str, mode: str) -> IO[str]:
    try:
        file: IO[str] = open(file_location, mode)
        return file
    except FileExistsError:
        return f"File on the path '{file_location}' is already there."
    except FileNotFoundError:
        return f"File on the path '{file_location}' does not exist."
    except Exception as e:
        return f"An error occurred\nError: {e}"

def file_size(file: IO[str]) -> int:
    size: int = file.tell()
    return size

def command(name: str) -> None:

    def decorator(func: Callable) -> Callable:
        if name in commands_dictionary:
            print(f"The command '{name}' can't be added twice.")
            return
        
        commands_dictionary[name] = func.__name__
        return func

    return decorator

def check_command(command: str) -> bool:
    if not command.lower() in commands_dictionary:
        return False
    return True
    
def execute_command(command: str) -> None:
    if not check_command(command):
        print(f"Command '{command}' does not exist.")
        return
    func_name: str = commands_dictionary[command.lower()]
    try:
        func: Callable = globals()[func_name]
        func()
    except Exception as e:
        print(e)

@command(name="help")
def show_commands() -> None:
    for name in commands_dictionary:
        print(name)

user_command: str = input("> ")
execute_command(user_command)
