#!/usr/bin/env python3

import random


RANGE_START = 1
RANGE_END = 200

rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def get_prime_game():
    number = random.randint(RANGE_START, RANGE_END)
    if is_prime(number):
        result = 'yes'
    else:
        result = 'no'
    question = number
    return question, result
