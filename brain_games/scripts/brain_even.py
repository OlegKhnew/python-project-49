#!/usr/bin/env python3

import brain_games.games.even_game as even_game
from brain_games.game_logic import game_logic


def main():
    game_logic(even_game.rule, even_game.even_game)


if __name__ == '__main__':
    main()
