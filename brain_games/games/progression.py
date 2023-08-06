import random

KYSY = 'What number is missing in the progression?'


def generate_progression():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    progression = [start + i * step for i in range(10)]
    return progression

def flow():
    progression = generate_progression()

    last_index = len(progression) - 1
    random_index = random.randint(0, last_index)

    answer = progression[random_index]
    correct_answer = str(answer)

    progression[random_index] = '..'  # type: ignore
    question = ' '.join(map(str, progression))

    return question, correct_answer