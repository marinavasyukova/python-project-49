from random import randint

game_question = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    while min(num1, num2) > 1:
        mod = max(num1, num2) % min(num1, num2)
        if mod:
            num1, num2 = mod, min(num1, num2)
        else:
            return min(num1, num2)
    return 1


def make_question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = f'{num1} {num2}'
    expected_answer = find_gcd(num1, num2)
    return question, str(expected_answer)
