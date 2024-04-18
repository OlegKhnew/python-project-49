#!/usr/bin/env python3

import brain_games.games.even_game as even_game
from brain_games.engine import run_game


def main():
    run_game(even_game.rule, even_game.get_round_of_even_game)


if __name__ == '__main__':
    main()
