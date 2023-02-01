#!/usr/bin/env python3

import prompt
import random


def calculate_expression(num1, num2, operation):
    """
    Function to perform the calculation for a given expression
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    for i in range(3):
        # Generate two random numbers and a random operation
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        operation = random.choice(["+", "-", "*"])
        question = f"{num1} {operation} {num2}"
        correct_answer = calculate_expression(num1, num2, operation)

        print(f"Question: {question}")
        answer = input("Your answer: ").strip()
        try:
            answer = int(answer)
        except ValueError:
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}")
            print(f"Let's try again, {name}!")
            return

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
