#!/usr/bin/env python3


import prompt
import random
from random import randint
from operator import add, sub, mul


# функция приветствия пользователя
def main():
  print("Welcome to the Brain Games!")
  name = prompt.string("May I have your name? ")
  print('Hello, ' + name + "!")

  operators = {"+": add, "-": sub, "*": mul}  # создаем словарь
  tries = 3  # переменная на количество попыток
  print('What is the result of the expression?')

  keys = list(operators)  # ключи к словарю

  for i in range(3):
    random_num1 = random.randint(1, 30)
    random_num2 = random.randint(1, 30)
    operator = random.choice(keys)
    counting = str(random_num1) + str(operator) + str(random_num2)
    print("Question: " + counting)
    result = operators[operator](random_num1, random_num2)
    answer = int(input('Your answer:'))
    if answer == result:
      print('Correct!')
      tries += 1
    else:
      print(answer, "is wrong answer ;(. Correct answer was", result)
      print('Let\'s try again, ' + name + '!')
      break
  if tries >= 3:
    print('Congratulations!')


if __name__ == '__main__':
  main()