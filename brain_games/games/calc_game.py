#!/usr/bin/env python3

import random
import operator


rule = 'What is the result of the expression?'


def calc_game():
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    op = random.choice(['+', '-', '*'])
    question = 'Question: ' + str(x) + ' ' + op + ' ' + str(y)
    if op == '+':
        result = operator.add(x, y)
    elif op == '-':
        result = operator.sub(x, y)
    elif op == '*':
        result = operator.mul(x, y)
    return question, result
