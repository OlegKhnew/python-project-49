#!/usr/bin/env python3

from brain_games.games.even_game import even_game
from brain_games.games.even_game import even_rule
from brain_games.game_logic import game_logic


def main():
    game_logic(even_rule, even_game)


if __name__ == '__main__':
    main()
