#!/usr/bin/env python3

import prompt
import random
import operator


def calc_game():
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    op = random.choice(['+', '-', '*'])
    print('Question: ' + str(x) + ' ' + op + ' ' + str(y))
    answer = prompt.integer('Your answer: ')
    if op == '+':
        result = operator.add(x, y)
    elif op == '-':
        result = operator.sub(x, y)
    elif op == '*':
        result = operator.mul(x, y)
    return answer, result
