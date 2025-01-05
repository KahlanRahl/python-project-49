#!/usr/bin/env python3

from brain_games.games.game_engine import run_game
import random


def is_even(number):
    """
    Проверяет, является ли число чётным.

    Параметры:
    - number: Число для проверки.

    Возвращает:
    - True, если число чётное, иначе False.
    """
    return number % 2 == 0


def generate_question():
    """
    Генерирует вопрос и правильный ответ для игры «Проверка на чётность».

    Возвращает:
    - question: Вопрос (случайное число).
    - correct_answer: Правильный ответ ("yes" или "no").
    """
    number = random.randint(1, 100)  # Генерация случайного числа
    correct_answer = "yes" if is_even(number) else "no"  # Определение правильного ответа
    question = f"{number}"  # Формирование вопроса
    return question, correct_answer


def play_even():
    """
    Запускает игру «Проверка на чётность».
    """
    run_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        generate_question,
    )


if __name__ == "__main__":
    play_even()  # Запуск игры
