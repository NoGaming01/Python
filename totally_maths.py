"""This is totally Mathematics"""

import random
import signal
import sys
from typing import get_type_hints


def generate_problems() -> tuple[int, int]:
    number1: int = random.randint(100, 1000)
    number2: int = random.randint(100, 1000)

    return number1, number2


def exit_shell(signal, frame) -> None:
    print("\nExiting the shell.")
    sys.exit(0)


signal.signal(signal.SIGINT, exit_shell)


while True:
    number1, number2 = generate_problems()

    result = number1 + number2

    print(f"{number1} + {number2}")

    user_input: int = int(input("> "))

    if user_input == result:
        print(f"You got it, {result=}")
    else:
        print(f"No, {result=}")
