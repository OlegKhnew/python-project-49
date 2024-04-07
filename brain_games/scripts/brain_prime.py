#!/usr/bin/env python3

import brain_games.games.prime_game as prime_game
from brain_games.game_logic import game_logic


def main():
    game_logic(prime_game.rule, prime_game.prime_game)


if __name__ == '__main__':
    main()
