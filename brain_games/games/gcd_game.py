#!/usr/bin/env python3

import random


RANGE_START = 1
RANGE_END = 100

rule = 'Find the greatest common divisor of given numbers.'


def get_gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


def get_round_of_gcd_game():
    x = random.randint(RANGE_START, RANGE_END)
    y = random.randint(RANGE_START, RANGE_END)
    question = 'Question: ' + str(x) + ' ' + str(y)
    result = get_gcd(x, y)
    return question, result
