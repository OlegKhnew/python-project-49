#!/usr/bin/env python3

import random
import prompt


def progression_game():
    first_number = random.randint(1, 10)
    step = random.randint(2, 10)
    progression_line = [str(x) for x in range(first_number, 110, step)][0:10]
    x_index = random.randint(0, 9)
    result = int(progression_line[x_index])
    progression_line[x_index] = '..'
    question_line = ' '.join(progression_line)
    print(f'Question: {question_line}')
    answer = prompt.integer('Your answer: ')
    return answer, result
