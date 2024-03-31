#!/usr/bin/env python3

from brain_games.games.gcd_game import gcd_game
from brain_games.games.gcd_game import gcd_rule
from brain_games.game_logic import game_logic


def main():
    game_logic(gcd_rule, gcd_game)


if __name__ == '__main__':
    main()
