#!/usr/bin/env python3

import random


even_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_game():
    number = random.randint(1, 100)
    question = 'Question: ' + str(number)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return question, result
