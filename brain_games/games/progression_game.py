#!/usr/bin/env python3

import random


rule = 'What number is missing in the progression?'


def get_progression(first_number, last_number, step):
    progression = [x for x in range(first_number, last_number, step)]
    return progression


def line_for_game(progression, x_index):
    progression_line = [str(x) for x in progression]
    progression_line[x_index] = '..'
    question_line = ' '.join(progression_line)
    return question_line


def progression_game():
    first_number = random.randint(1, 10)
    last_number = 110
    step = random.randint(2, 10)
    progression = get_progression(first_number, last_number, step)
    x_index = random.randint(0, 9)
    question = line_for_game(progression[0:10], x_index)
    result = int(progression[x_index])
    return question, result
