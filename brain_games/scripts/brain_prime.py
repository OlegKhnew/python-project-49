#!/usr/bin/env python3

import brain_games.games.prime_game as prime_game
from brain_games.engine import run_game


def main():
    run_game(prime_game.rule, prime_game.get_prime_game)


if __name__ == '__main__':
    main()
