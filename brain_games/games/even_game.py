#!/usr/bin/env python3

import random
import prompt


def even_game():
    number = random.randint(1,100)
    print('Question: ' + str(number))
    answer = prompt.string('Your answer: ')
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return answer, result

