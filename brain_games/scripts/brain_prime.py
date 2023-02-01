#!/usr/bin/env python3

import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime,otherwise answer "no".')
    for i in range(3):
        number = random.randint(1, 100)
        if is_prime(number):
            answer = "yes"
        else:
            answer = "no"
        print(f"Question: {number}")
        user_answer = input().strip()
        if user_answer == answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
