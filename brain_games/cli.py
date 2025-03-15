#!/usr/bin/env python3
import prompt


def welcome_user():
    """
    Запрос имени пользователя и приветствие с использованием
    библиотеки prompt для лучшей обработки кодировки.
    """
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name