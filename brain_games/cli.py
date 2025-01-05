#!/usr/bin/env python3

def welcome_user():
    """
    Приветствие пользователя и запрос имени.
    """
    print("Welcome to the Brain Games!")  # Приветствие
    name = input("May I have your name? ")  # Запрос имени
    print(f"Hello, {name}!")  # Приветствие с именем
    return name  # Возвращаем имя пользователя