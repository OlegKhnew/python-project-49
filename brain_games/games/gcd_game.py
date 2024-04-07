#!/usr/bin/env python3

import random


rule = 'Find the greatest common divisor of given numbers.'


def is_gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


def gcd_game():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    question = 'Question: ' + str(x) + ' ' + str(y)
    result = is_gcd(x, y)
    return question, result
