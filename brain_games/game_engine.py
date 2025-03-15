#!/usr/bin/env python3

import prompt  # Импортируем необходимые модули

from brain_games.cli import welcome_user  # Импортируем функцию welcome_user

ROUNDS_COUNT = 3  # Общее количество раундов для всех игр


def run_game(description: str, generate_question_and_answer):
    """
    Запускает игру с общей логикой.

    Параметры:
    - description (str): Описание игры.
    - generate_question_and_answer (Callable): Функция для генерации
      вопроса и ответа.
    """
    name = welcome_user()  # Приветствие и запрос имени
    print(description)  # Описание игры
    print()

    for _ in range(ROUNDS_COUNT):
        # Генерация вопроса и ответа
        question, correct_answer = generate_question_and_answer()
        print(f"Question: {question}")  # Вывод вопроса
        # Приводим ответ к нижнему регистру
        user_answer = prompt.string("Your answer: ").strip().lower()

        if user_answer != correct_answer:
            # Неправильный ответ
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")  # Сообщение о неудаче
            return

        print("Correct!")  # Если ответ правильный

    print(f"Congratulations, {name}!")  # Поздравление с победой
