import prompt
import brain_games.games.calc
import brain_games.games.even
import brain_games.games.gcd


def welcome_user():
    print('Welcome to the brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def run_game(game_question):
    name = welcome_user()
    print(game_question)
    index = 0
    max_rounds = 3
    while index < max_rounds:
        if brain_games.games.calc.game_question == game_question:
            question, expected_answer = brain_games.games.calc.make_question()
        elif brain_games.games.even.game_question == game_question:
            question, expected_answer = brain_games.games.even.make_question()
        elif brain_games.games.gcd.game_question == game_question:
            question, expected_answer = brain_games.games.gcd.make_question()
        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer == expected_answer:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if index == 3:
        print(f'Congratulations, {name}!')
