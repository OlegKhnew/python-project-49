#!/usr/bin/env python3

import random
import prompt


def gcd_game():
    x = random.randint(1,100)
    y = random.randint(1,100)
    print('Question: ' + str(x) + ' ' + str(y))
    answer = prompt.integer('Your answer: ')
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    result = x
    return answer, result
