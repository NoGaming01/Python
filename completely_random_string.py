"""Completely Random String is here."""

import random
import string


def random_string_v1(length: int) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))


while True:
    print(random_string_v1(6))
