#!/usr/bin/env python3

import random

from brain_games.game_engine import run_game  # Импортируем общую логику игры


def is_even(number):
    """
    Проверяет, является ли число четным.
    """
    return number % 2 == 0


def generate_question():
    """
    Генерация вопроса и правильного ответа для игры "Проверка на четность".
    """
    number = random.randint(1, 100)  # Генерация случайного числа
    # Определение правильного ответа
    correct_answer = "yes" if is_even(number) else "no"
    question = f"{number}"  # Вопрос — это само число
    return question, correct_answer  # Возвращаем вопрос и правильный ответ


def play_even():
    """
    Запуск игры "Проверка на четность".
    """
    run_game(
        "Answer 'yes' if the number is even, otherwise answer 'no'.",
        generate_question
    )


if __name__ == "__main__":
    play_even()  # Запуск игры
