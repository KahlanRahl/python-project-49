#!/usr/bin/env python3
"""Игра 'Простое ли число?'."""

import random

from brain_games.game_engine import run_game

# Минимальное простое число
MIN_PRIME = 2


def is_prime(n):
    """
    Проверяет, является ли число простым.

    Args:
        n (int): Проверяемое число

    Returns:
        bool: True, если число простое, иначе False
    """
    # Числа меньше MIN_PRIME не являются простыми
    if n < MIN_PRIME:
        return False

    # Оптимизированная проверка простоты числа
    return all(n % i != 0 for i in range(MIN_PRIME, int(n ** 0.5) + 1))


def generate_question():
    """
    Генерация вопроса и правильного ответа для игры 'Простое ли число?'.
    """
    # Генерируем случайное число от 1 до 100
    number = random.randint(1, 100)

    # Определяем, простое ли оно
    correct_answer = "yes" if is_prime(number) else "no"

    # Вопрос - это само число
    question = str(number)

    return question, correct_answer


def play_prime():
    """
    Запуск игры 'Простое ли число?'.
    """
    run_game(
        "Answer \"yes\" if given number is prime. Otherwise answer \"no\".",
        generate_question
    )


if __name__ == "__main__":
    play_prime()
