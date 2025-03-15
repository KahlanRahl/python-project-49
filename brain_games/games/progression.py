#!/usr/bin/env python3
"""Игра 'Арифметическая прогрессия'."""

import random

from brain_games.game_engine import run_game


def generate_progression(start, step, length):
    """
    Генерирует арифметическую прогрессию.

    Args:
        start (int): Начальное число прогрессии
        step (int): Шаг прогрессии
        length (int): Длина прогрессии

    Returns:
        list: Список чисел прогрессии
    """
    return [start + step * i for i in range(length)]


def generate_question():
    """
    Генерация вопроса и правильного ответа для игры 'Арифметическая прогрессия'.
    """
    # Генерируем параметры прогрессии
    start = random.randint(1, 50)  # Начальное число
    step = random.randint(2, 10)  # Шаг прогрессии
    length = random.randint(5, 10)  # Длина прогрессии

    # Генерируем прогрессию
    progression = generate_progression(start, step, length)

    # Выбираем случайную позицию для скрытия
    hidden_index = random.randint(0, length - 1)

    # Запоминаем правильный ответ
    correct_answer = str(progression[hidden_index])

    # Скрываем элемент
    progression_with_hidden = progression.copy()
    progression_with_hidden[hidden_index] = '..'

    # Формируем вопрос
    question = ' '.join(map(str, progression_with_hidden))

    return question, correct_answer


def play_progression():
    """
    Запуск игры 'Арифметическая прогрессия'.
    """
    run_game(
        "What number is missing in the progression?",
        generate_question
    )


if __name__ == "__main__":
    play_progression()
