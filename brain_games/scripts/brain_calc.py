#!/usr/bin/env python3


import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    # Loop to repeat the game 3 times
    for i in range(3):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        # List of possible operations
        operations = ["+", "-", "*"]
        # Choosing a random operation from the list
        operation = random.choice(operations)
        # Forming the question string
        question = f"{num1} {operation} {num2}"
        # Variable to store the correct answer
        correct_answer = None
        # Checking which operation was chosen and performing the calculation
        if operation == "+":
            correct_answer = num1 + num2
        elif operation == "-":
            correct_answer = num1 - num2
        elif operation == "*":
            correct_answer = num1 * num2
        print(f"Question: {question}")
        answer = input("Your answer: ").strip()
        # Converting the user's answer to an integer
        try:
            answer = int(answer)
        except ValueError:
            # If the answer is not a number, it is considered an error
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}")
            print(f"Let's try again, {name}!")
            return
        # Checking if the user's answer is correct
        if answer == correct_answer:
            print("Correct!")
        else:
            # If the answer is incorrect, the game ends
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
