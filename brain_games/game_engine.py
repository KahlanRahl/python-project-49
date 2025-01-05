#!/usr/bin/env python3

import prompt  # Импорт библиотеки prompt для взаимодействия с пользователем

ROUNDS_COUNT = 3  # Константа: количество раундов игры (одинаково для всех игр)


def run_game(description: str, generate_question_and_answer):
    """
    Запускает игру с общей логикой.

    Параметры:
    - description: Описание игры, выводится в начале.
    - generate_question_and_answer: Функция для генерации вопроса и правильного ответа.
    """
    print("Welcome to the Brain Games!")  # Приветствие игрока
    print(description)  # Вывод описания правил игры
    print()  # Пустая строка для удобства чтения

    name = prompt.string("May I have your name? ")  # Запрос имени игрока
    print(f"Hello, {name}!")  # Приветствие с использованием имени
    print()  # Пустая строка для удобства чтения

    for _ in range(ROUNDS_COUNT):  # Цикл, запускающий три раунда игры
        question, correct_answer = generate_question_and_answer()
        # Генерация вопроса и правильного ответа с использованием переданной функции

        print(f"Question: {question}")  # Вывод вопроса для пользователя
        user_answer = prompt.string("Your answer: ").lower()
        # Получение ответа от пользователя и приведение его к нижнему регистру

        if user_answer != correct_answer:
            # Проверка: совпадает ли ответ пользователя с правильным
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            # Вывод сообщения об ошибке с указанием правильного ответа
            print(f"Let's try again, {name}!")  # Сообщение об окончании игры из-за ошибки
            return  # Завершение игры

        print("Correct!")  # Сообщение о правильном ответе

    print(f"Congratulations, {name}!")  # Поздравление пользователя с успешным завершением игры
