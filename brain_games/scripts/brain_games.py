#!/usr/bin/env python3

# Импортируем функцию welcome_user из модуля cli
from brain_games.cli import welcome_user


def main():
    """
    Основная функция программы.
    """
    # Выводим приветственное сообщение
    print("Welcome to the Brain Games!")

    # Вызываем функцию welcome_user
    welcome_user()


# Проверяем, запущен ли файл напрямую
if __name__ == "__main__":
    # Если да, то вызываем функцию main
    main()
