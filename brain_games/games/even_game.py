#!/usr/bin/env python3

import random


RANGE_START = 1
RANGE_END = 100

rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(x):
    return x % 2 == 0


def get_round_of_even_game():
    number = random.randint(RANGE_START, RANGE_END)
    question = str(number)
    if is_even(number):
        result = 'yes'
    else:
        result = 'no'
    return question, result
