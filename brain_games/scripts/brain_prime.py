#!/usr/bin/env python3

from brain_games.games.prime_game import prime_game
from brain_games.games.prime_game import prime_rule
from brain_games.game_logic import game_logic


def main():
    game_logic(prime_rule, prime_game)


if __name__ == '__main__':
    main()
