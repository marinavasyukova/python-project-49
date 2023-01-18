from random import randint

game_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_even(num):
    if num % 2:
        return 'no'
    return 'yes'


def make_question():
    rand_number = randint(1, 100)
    expected_answer = check_even(rand_number)
    return rand_number, expected_answer
    