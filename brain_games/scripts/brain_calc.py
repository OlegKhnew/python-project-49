#!/usr/bin/env python3

import brain_games.games.calc_game as calc_game
from brain_games.engine import run_game


def main():
    run_game(calc_game.rule, calc_game.get_round_of_calc_game)


if __name__ == '__main__':
    main()
