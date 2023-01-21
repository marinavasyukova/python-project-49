from random import randint

game_question = 'What number is missing in the progression?'


def make_question():
    start_num = randint(1, 20)
    step = randint(2, 5)
    progression = list(range(start_num, start_num + step * 11, step))
    index = randint(0, 9)
    expected_answer = progression[index]
    progression[index] = '..'
    progression = [str(i) for i in progression]
    question = ' '.join(progression)
    return question, str(expected_answer)
