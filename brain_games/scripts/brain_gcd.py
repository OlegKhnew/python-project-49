#!/usr/bin/env python3

import brain_games.games.gcd_game as gcd_game
from brain_games.game_logic import game_logic


def main():
    game_logic(gcd_game.rule, gcd_game.gcd_game)


if __name__ == '__main__':
    main()
