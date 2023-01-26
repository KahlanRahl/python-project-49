#!/usr/bin/env python3


import prompt
import random
from random import randint
from operator import add, sub, mul

# глобальная функция приветствия и запроса имени
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print('Hello, ' + name + "!")

main()

operators = {"+": add, "-": sub, "*": mul}
tries = 3 # количество попыток пользователя
print('What is the result of the expression?')


# создаем список/list ключей к словарю для передачи к random.choice
keys = list(operators)


# используем функцию range()
for i in range(3):
  random_num1 = random.randint(1, 30)
  random_num2 = random.randint(1, 30)
  operator = random.choice(keys)
  print("Question: " + str(random_num1) + str(operator) + str(random_num2))
  result = str(random_num1) + str(operator) + str(random_num2)
  answer = input('Your answer:')
  if answer == (operators[operator](random_num1, random_num2)):
    print('Correct!')
    tries += 1
  else:
    print(answer, "is wrong answer ;(. Correct answer was", result)
    print('Let\'s try again, ' + name + '!')
  break
if tries >= 3:
  print('Congratulations!')


#if __name__ == '__main__':
#main() 