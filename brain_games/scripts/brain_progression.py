#!/usr/bin/env python3

from brain_games.games.progression_game import progression_game
from brain_games.games.progression_game import progression_rule
from brain_games.game_logic import game_logic


def main():
    game_logic(progression_rule, progression_game)


if __name__ == '__main__':
    main()
