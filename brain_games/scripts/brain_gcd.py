#!/usr/bin/env python3

import brain_games.games.gcd_game as gcd_game
from brain_games.engine import run_game


def main():
    run_game(gcd_game.rule, gcd_game.get_round_of_gcd_game)


if __name__ == '__main__':
    main()
