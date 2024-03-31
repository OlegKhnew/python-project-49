#!/usr/bin/env python3

from brain_games.games.calc_game import calc_game
from brain_games.games.calc_game import calc_rule
from brain_games.game_logic import game_logic


def main():
    game_logic(calc_rule, calc_game)


if __name__ == '__main__':
    main()
