#!/usr/bin/env python3

import random


gcd_rule = 'Find the greatest common divisor of given numbers.'


def gcd_game():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    question = 'Question: ' + str(x) + ' ' + str(y)
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    result = x
    return question, result
