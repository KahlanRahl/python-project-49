#!/usr/bin/env python3
import io
import sys


def welcome_user():
    """
    Запрос имени пользователя и приветствие.
    """
    print("Welcome to the Brain Games!")

    # Перенастройка stdin для корректной обработки UTF-8
    sys.stdin = io.TextIOWrapper(
        sys.stdin.buffer,
        encoding='utf-8',
        errors='replace'
    )

    try:
        name = input('May I have your name? ')
    except UnicodeDecodeError:
        print("Error reading input. Using default name.")
        name = "Player"

    print(f'Hello, {name}!')
    return name
