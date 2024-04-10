#!/usr/bin/env python3

import random
import operator


RANGE_START = 1
RANGE_END = 50

rule = 'What is the result of the expression?'


def get_calc_game():
    x = random.randint(RANGE_START, RANGE_END)
    y = random.randint(RANGE_START, RANGE_END)
    op = random.choice(['+', '-', '*'])
    question = 'Question: ' + str(x) + ' ' + op + ' ' + str(y)
    if op == '+':
        result = operator.add(x, y)
    elif op == '-':
        result = operator.sub(x, y)
    elif op == '*':
        result = operator.mul(x, y)
    return question, result
