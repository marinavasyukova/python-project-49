#!/usr/bin/env python3
# from brain_games.cli import welcome_user

from random import randint
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def check_even(num):
    if num % 2:
        return 'no'
    return 'yes'


def main():
    print('Welcome to the brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        rand_number = randint(1, 100)
        expected_answer = check_even(rand_number)
        print(f'Question: {rand_number}')
        answer = input('Your answer: ')
        if answer == expected_answer:
            print('Correct!')
            continue
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
