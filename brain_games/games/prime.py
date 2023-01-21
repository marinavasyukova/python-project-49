from random import randint

game_question = 'Answer "yes" if the number is prime, otherwise answer "no".'


def is_prime(num):
    for diviser in range(2, num // 2 + 1):
        if num % diviser == 0:
            return 'no'
    return 'yes'


def make_question():
    rand_number = randint(1, 100)
    expected_answer = is_prime(rand_number)
    return rand_number, expected_answer
