#!/usr/bin/env python3

import prompt
import random
from random import randint


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def play_game(name):
    print(f"Hello, {name}!\nFind the greatest common divisor of given numbers.")
    attempts = 3
    while attempts > 0:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        print(f"Question: {num1} {num2}")
        answer = int(input("Your answer: "))
        if gcd(num1, num2) == answer:
            print("Correct!")
            break
        else:
            attempts -= 1
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{gcd(num1, num2)}'.")
            if attempts == 0:
                print(f"Let's try again, {name}!")
                break
            print(f"Let's try again, {name}!")

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    play_game(name)

if __name__ == "__main__":
    main()