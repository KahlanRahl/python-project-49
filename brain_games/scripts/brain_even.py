#!/usr/bin/env python3

import random
from random import randint


# функция для определения четности числа
def even_or_odd(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


# функция - цикл 
# у пользователя есть три попытки ответить
def sequence():
    guess_left = 0
    while guess_left <= 3:
# переменная - генерация случайного числа
        random_number = random.randint(1, 20)
# программа задает вопрос пользователю со случайным числом
        print("Question: " + str(random_number))
        answer = input('Your answer:')
        result = even_or_odd(random_number)
        if result == answer:
            print('Correct!')
            guess_left += 1
        else:
            print(answer, "is wrong answer ;(. Correct answer was", result)
            print('Let\'s try again', + name + '!')
        break
    if guess_left >= 3:
        print('Congratulations!')
sequence()