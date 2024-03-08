"""A game for fun. Name is Guess the Number"""

import random


guess: int = 0
number: int = random.randint(1, 100)


def guess_or_guesses(guess: int) -> str:
    if guess == 1:
        return "guess"
    return "guesses"


print("I am guessing a number between 1 to 100.")
print("Try to guess the number.")


while True:
    user_guess = int(input("> "))

    if user_guess < number:
        print("Too low.")
        guess += 1
    elif user_guess > number:
        print("Too high.")
        guess += 1
    else:
        guess += 1
        print(f"You guessed it in {guess} {guess_or_guesses(guess)}.")
        print(f"The number was {number}.")
        break
