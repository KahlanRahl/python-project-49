# Импортируем библиотеку prompt
import prompt

def welcome_user():
    """
    Функция запрашивает имя пользователя и приветствует его.
    """
    # Используем функцию prompt.string для запроса имени пользователя
    # Она сама выведет текст "May I have your name? " и будет ждать ввода
    name = prompt.string('May I have your name? ')

    # Приветствуем пользователя по имени
    print(f"Hello, {name}!")