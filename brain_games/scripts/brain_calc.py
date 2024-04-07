#!/usr/bin/env python3

import brain_games.games.calc_game as calc_game
from brain_games.game_logic import game_logic


def main():
    game_logic(calc_game.rule, calc_game.calc_game)


if __name__ == '__main__':
    main()
