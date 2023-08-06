"""General logic for all games"""

import prompt

ROUNDS_MAXIMUM = 3


def play(game):
    """Greet the player and ask his/her name"""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.KYSY)

    for _ in range(ROUNDS_MAXIMUM):
        question, correct_answer = game.flow()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')