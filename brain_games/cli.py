#!/usr/bin/env python3


def welcome_user():
    """
    Запрос имени пользователя и приветствие.
    """
    print("Welcome to the Brain Games!")
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name