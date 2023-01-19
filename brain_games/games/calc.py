from random import randint, choice

game_question = 'What is the result of the expression?'


def make_question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = choice('+-*')
    question = f'{num1} {operator} {num2}'
    if operator == '+':
        expected_answer = num1 + num2
    elif operator == '-':
        expected_answer = num1 - num2
    else:
        expected_answer = num1 * num2
    return question, str(expected_answer)
