#!/usr/bin/env python3

import random


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_evem(x):
    if x % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even_game():
    number = random.randint(1, 100)
    question = str(number)
    result = is_evem(number)
    return question, result
