#!/usr/bin/env python3

import random


def generate_question():
    """
    Генерирует случайное математическое выражение и вычисляет правильный ответ.
    Возвращает кортеж (вопрос, правильный ответ).
    """
    num1 = random.randint(1, 100)  # Генерация первого числа
    num2 = random.randint(1, 100)  # Генерация второго числа
    operation = random.choice(['+', '-', '*'])  # Выбор случайной операции

    # Инициализируем переменную result
    result = 0  # Значение по умолчанию

    # Используем оператор match для вычисления результата
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2

    question = f"{num1} {operation} {num2}"  # Формируем вопрос
    return question, result


def play_calc():
    """
    Основная функция игры «Калькулятор».
    Управляет процессом игры: приветствие, вопросы, проверка ответов.
    """
    print("Welcome to the Brain Games!")
    player_name = input("May I have your name? ")  # Запрос имени пользователя
    print(f"Hello, {player_name}!")
    print("What is the result of the expression?")

    # Основной цикл игры (3 раунда)
    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        # Проверка ответа пользователя
        if int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            return  # Завершение игры при неправильном ответе

    # Поздравление при успешном завершении
    print(f"Congratulations, {player_name}!")


def main():
    """
    Точка входа в программу. Запускает игру «Калькулятор».
    """
    play_calc()


if __name__ == "__main__":
    main()  # Запуск игры при прямом выполнении скрипта
