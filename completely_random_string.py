"""Completely Random String is here."""

import random
import string
from sys import getsizeof


def random_string_v1(length: int) -> str:
    characters: str = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=length))


tokens: list = []
used_tokens: list = []


def random_string_v2(length: int) -> str:
    characters: str = string.ascii_letters + string.digits

    token = "".join(random.choices(characters, k=length))

    while True:
        if token in tokens:
            continue
        tokens.append(token)
        return token


def user_response() -> str:
    user_input: str = input("Token: ")

    if user_input in used_tokens:
        return "Sorry the token has been used"
    elif user_input in tokens:
        used_tokens.append(user_input)
        return "Login Successfull"
    return "Invalid Token"


for i in range(10):
    print(random_string_v2(6))

print(getsizeof(tokens))

while True:
    print(user_response())
