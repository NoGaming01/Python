"""This is programe to Manipulate files."""

from typing import IO, Callable, Optional

commands_dictionary = {}

def command(name: str) -> Callable:

    def decorator(func: Callable) -> Callable:

        if name in commands_dictionary:
            print(f"The command '{name}' can't be added twice.")
            return
        
        commands_dictionary[name] = func.__name__

        return func
    
    return decorator

def check_command(command: str) -> bool:
    return command.lower() in commands_dictionary

def execute_command(command: str, *args: list[str]) -> None:
    if not check_command(command):
        print(f"Command '{command}' not found.")
        return
    
    func_name: str = commands_dictionary[command.lower()]

    try:
        func = globals()[func_name]
        func(*args)
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

@command(name="help")
def help_menu() -> None:
    for commands in commands_dictionary:
        print(commands)

def get_file(file_location: str) -> IO[str]:
    file: IO[str] = open(file_location, "r")
    return file

@command(name="open")
def open_file(file_location: str) -> None:
    file: IO[str] = get_file(file_location)
    print(file)

while True:

    def get_command_from_user() -> str:
        command_input: str = input("Enter Command > ")
        return command_input

    command_from_user = get_command_from_user()

    if command_from_user == 'exit':
        break

    execute_command(*command_from_user.split())
