import random

KYSY = 'Answer "yes" if the number is even, otherwise answer "no".'


def flow():
    question = random.randint(0, 100)

    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer