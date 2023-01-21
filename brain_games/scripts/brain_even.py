#!/usr/bin/env python3

from brain_games.games.even import game_question, make_question
from brain_games.engine import run_game


def main():
    run_game(game_question, make_question)


if __name__ == '__main__':
    main()
