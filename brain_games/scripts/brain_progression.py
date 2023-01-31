#!/usr/bin/env python3


import prompt
import random


# Основная функция
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")
    for j in range(3):  # описываем правила с тремя попытками
        progression = generate_progression()  # получаем прогрессию чисел
# случайная позиция для недостающего числа
        missing_number_index = random.randint(0, len(progression) - 1)
# копируем список progression
        prog = progression[:]
# заменяем отсутствующее число в списке-копии выше точками
        prog[missing_number_index] = ".."
# соединяем элементы списка-копии `prog`
# в виде строки с пробелом между каждым элементом
        question = " ".join(map(str, prog))
        vacancy = str(progression[missing_number_index])   # правильный ответ
        print(f"Question: {question}")
        user_answer = input()
# проверяем совпадает ли ответ пользователя с правильным ответом
        if user_answer == vacancy:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{vacancy}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


# функция для генерации прогрессии чисел
def generate_progression():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    progression = [start + i * step for i in range(10)]
    return progression


if __name__ == "__main__":
    main()
