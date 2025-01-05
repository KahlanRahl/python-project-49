#!/usr/bin/env python3

from brain_games.game_engine import run_game  # Импортируем общую логику игры
import random


def is_even(number):
    """
    Функция для проверки, является ли число чётным.
    """
    return number % 2 == 0


def generate_question():
    """
    Генерация вопроса и правильного ответа для игры "Чётное ли число?".
    """
    number = random.randint(1, 100)  # Генерация случайного числа
    correct_answer = "yes" if is_even(number) else "no"  # Определение правильного ответа
    question = f"{number}"  # Вопрос — это само число
    return question, correct_answer  # Возвращаем вопрос и правильный ответ


def play_even():
    """
    Запуск игры для проверки чётности числа.
    """
    run_game(
        'Answer "yes" if the number is even, otherwise answer "no".',  # Описание игры
        generate_question,  # Функция для генерации вопроса и ответа
    )


if __name__ == "__main__":
    play_even()  # Запуск игры
