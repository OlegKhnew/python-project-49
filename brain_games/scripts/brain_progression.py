#!/usr/bin/env python3

import brain_games.games.progression_game as progression_game
from brain_games.engine import run_game


def main():
    run_game(progression_game.rule,
             progression_game.get_round_of_progression_game)


if __name__ == '__main__':
    main()
