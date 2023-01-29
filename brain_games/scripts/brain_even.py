#!/usr/bin/env python3


import prompt
import random
from random import randint


# функция определения четности нечетности числа
def even_or_odd(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


# функция приветствия пользователя
def main():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print('Hello, ' + name + "!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
main()


# описание логики игры
guess_left = 0
while guess_left < 3:
    random_number = random.randint(1, 20)
    print("Question: " + str(random_number))
    answer = input('Your answer:')
    result = even_or_odd(random_number)
    if result == answer:
        print('Correct!')
        guess_left += 1
    else:
        print(answer, "is wrong answer ;(. Correct answer was", result)
        print('Let\'s try again, ' + name + '!')
        break

if guess_left == 3:
    print('Congratulations, ' + name + '!')


if name == 'main':
    main()
