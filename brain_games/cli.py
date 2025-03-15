#!/usr/bin/env python3
import prompt


def welcome_user():
    """
    Запрос имени пользователя и приветствие.
    """
    print("Welcome to the Brain Games!")  # Добавляем приветствие
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
