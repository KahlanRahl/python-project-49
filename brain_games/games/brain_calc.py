#!/usr/bin/env python3

import random

from brain_games.game_engine import run_game  # Импортируем общую логику игры


def generate_question():
    """
    Генерация вопроса и правильного ответа для игры "Калькулятор".
    """
    num1 = random.randint(1, 100)  # Первое случайное число
    num2 = random.randint(1, 100)  # Второе случайное число
    # Операция (сложение, вычитание или умножение)
    operation = random.choice(['+', '-', '*'])

    result = None  # Инициализация переменной result, чтобы избежать ошибки

    # Применяем оператор match для выбора операции
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2

    # Если result остался равным None, то нужно выбросить исключение
    if result is None:
        raise ValueError(f"Unsupported operation: {operation}")

    question = f"{num1} {operation} {num2}"  # Формируем вопрос
    return question, str(result)  # Возвращаем вопрос и правильный ответ


def play_calc():
    """
    Запуск игры "Калькулятор".
    """
    run_game(
        "What is the result of the expression?",  # Описание игры
        generate_question,  # Функция для генерации вопроса и ответа
    )


if __name__ == "__main__":
    play_calc()  # Запуск игры
