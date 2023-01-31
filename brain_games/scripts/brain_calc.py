#!/usr/bin/env python3


import prompt
import random
from operator import add, sub, mul

name = ''


# функция приветствия пользователя
def main():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print('Hello, ' + name + "!")


main()


operators = {"+": add, "-": sub, "*": mul}  # создаем словарь
tries = 0  # переменная для количества попыток
print('What is the result of the expression?')

keys = list(operators)  # Keys to the dictionary


for i in range(3):
    random_num1 = random.randint(1, 30)
    random_num2 = random.randint(1, 30)
    operator = random.choice(keys)
    print("Question: " + str(random_num1) + str(operator) + str(random_num2))
    result = operators[operator](random_num1, random_num2)
    answer = int(input('Your answer:'))
    if answer == result:
        print('Correct!')
        tries += 1
    else:
        print(answer, "is wrong answer ;(. Correct answer was", result)
        print('Let\'s try again, ' + name + '!')
        break
if tries == 3:
    print('Congratulations!')
