#!/usr/bin/env python3


import prompt
import random
from random import randint


print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")


# глобальная функция приветствия
def main():
    print('Hello, ' + name + "!")
    print('Find the greatest common divisor of given numbers')

main()


random_num1 = random.randint(1, 1000)
random_num2 = random.randint(1, 1000)


# функция нахождения gcd
def find_gcd(random_num1, random_num2):
    value_of_remainder = random_num1%random_num2
    while value_of_remainder:
        random_num1=random_num2
        random_num2=value_of_remainder
        value_of_remainder=random_num1%random_num2
    return random_num2


# программа задает вопрос
guesses_left = 0
while guesses_left <=3:
    print("Question: " + str(random_num1) + ' ' + str(random_num2))
    answer = input('Your answer:')
    result = find_gcd(value_of_remainder)
    if result == answer:
        print('Correct!')
        guesses_left += 1
    else:
        print(answer, "is wrong answer ;(. Correct answer was", result)
        print('Let\'s try again, ' + name + '!')
    break
if guesses_left >= 3:
    print('Congratulations!')


