import prompt


def welcome_user():
    print('Welcome to the brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def check_answer(answer, exp_answer, name):
    if answer == exp_answer:
        print('Correct!')
        return 1
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{exp_answer}'.")
    print(f"Let's try again, {name}!")
    return 0


def run_game(game_question, make_question):
    name = welcome_user()
    print(game_question)
    index = 0
    max_rounds = 3
    while index < max_rounds:
        question, expected_answer = make_question()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if check_answer(answer, expected_answer, name):
            index += 1
        else:
            break
    if index == max_rounds:
        print(f'Congratulations, {name}!')
