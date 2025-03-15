#!/usr/bin/env python3
"""Игра 'Наибольший общий делитель (НОД)'."""

import math
import random

from brain_games.game_engine import run_game


def generate_question():
    """
    Генерация вопроса и правильного ответа для игры 'НОД'.
    """
    # Генерируем два случайных числа от 1 до 100
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # Вычисляем НОД с помощью встроенной функции math.gcd
    correct_answer = str(math.gcd(num1, num2))

    # Формируем вопрос в виде "num1 num2"
    question = f"{num1} {num2}"

    return question, correct_answer


def play_gcd():
    """
    Запуск игры 'НОД'.
    """
    run_game(
        "Find the greatest common divisor of given numbers.",
        generate_question
    )


if __name__ == "__main__":
    play_gcd()
