import random

KYSY = 'What is the result of the expression?'

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


def flow():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)

    operators = ['+', '-', '*']
    operation = random.choice(operators)

    question = f"{num1} {operation} {num2}"

    answer = 0

    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    correct_answer = str(answer)

    return question, correct_answer
