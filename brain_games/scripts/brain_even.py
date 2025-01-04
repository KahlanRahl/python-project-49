#!/usr/bin/env python3

import random  # Импортируем модуль для генерации случайных чисел


def is_even(number):
    """Проверяет, является ли число чётным."""
    return number % 2 == 0  # Возвращает True, если число чётное, иначе False


def play_even_game():
    """Запускает игру «Проверка на чётность»."""
    # Приветствуем пользователя
    print("Welcome to the Brain Games!")
    # Запрашиваем имя пользователя
    name = input("May I have your name? ")
    # Приветствуем пользователя по имени
    print(f"Hello, {name}!")
    # Объясняем правила игры
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0  # Счётчик правильных ответов

    # Игровой цикл: продолжается, пока не будет 3 правильных ответа
    while correct_answers < 3:
        # Генерируем случайное число от 1 до 100
        number = random.randint(1, 100)
        # Показываем число пользователю
        print(f"Question: {number}")
        # Запрашиваем ответ пользователя и очищаем его от пробелов
        user_answer = input("Your answer: ").strip().lower()

        # Используем оператор match для обработки ответа
        match user_answer:
            case "yes" if is_even(number):  # Если ответ "yes" и число чётное
                print("Correct!")
                correct_answers += 1  # Увеличиваем счётчик правильных ответов
            case "no" if not is_even(number):  # Если ответ "no" и число нечётное
                print("Correct!")
                correct_answers += 1  # Увеличиваем счётчик правильных ответов
            case _:  # Любой другой ответ (неправильный или некорректный)
                # Определяем правильный ответ
                correct_answer = "yes" if is_even(number) else "no"
                # Сообщаем об ошибке
                print(
                    f"'{user_answer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_answer}'."
                )
                # Прощаемся с игроком
                print(f"Let's try again, {name}!")
                return  # Завершаем игру

    # Поздравляем пользователя с победой
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_even_game()  # Запуск игры