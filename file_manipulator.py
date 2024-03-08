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
        print(f"Vakue Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def get_command_from_user() -> str:
    command_input: str = input("Enter Command > ")
    return command_input

command_from_user = get_command_from_user()

execute_command(*command_from_user.split())
