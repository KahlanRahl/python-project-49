#!/usr/bin/env python3


import prompt
import random
from random import randint


# функция определения четности числа
def even_or_odd(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


# функция приветствия пользователя + задача игры
def main():
    global name # для доступности переменной в других частях кодах, используем глобальность
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print('Hello, ' + name + "!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

main()  # вызываем основную функцию

guess_left = 3  # вводим переменную с количеством оставшихся попыток
while guess_left > 0:  # приступаем к циклу while
    random_number = random.randint(1, 20) #генерируем случайное число
    print("Question: " + str(random_number))
    answer = input('Your answer:')
    result = even_or_odd(random_number)
    if result == answer:   # сверяем ответ пользователя и результат программы
        print('Correct!')
        guess_left -= 1  # подсчитываем сколько осталось попыток
    else:
        print(answer, "is wrong answer ;(. Correct answer was", result)
        print('Let\'s try again, ' + name + '!')
        break

if guess_left == 0:
    print('Congratulations, ' + name + '!')


if name == 'main':
    main()
