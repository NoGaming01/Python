"""Completely Random String is here."""

import random
import string
from sys import getsizeof


def random_string_v1(length: int) -> str:
    characters: str = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))


generated_tokens: list = []


def random_string_v2(length: int) -> str:
    characters: str = string.ascii_letters + string.digits

    token = "".join(random.choices(characters, k=length))

    while True:
        if token in generated_tokens:
            continue
        generated_tokens.append(token)
        return token
        

for i in range(10 ** 5):
    print(random_string_v2(121))

print(getsizeof(generated_tokens))
