#!/usr/bin/env python3

import random


INITIAL_RANGE_START = 1
INITIAL_RANGE_END = 10
COMMON_DIFFERENCE_RANGE_START = 2
COMMON_DIFFERENCE_RANGE_END = 10
X_INDEX_RANGE_START = 0
X_INDEX_RANGE_END = 9
PROGRESSION_LENGTH = 10

rule = 'What number is missing in the progression?'


def get_progression(initial_term, common_difference):
    progression = []
    i = 0
    n = initial_term
    while i < PROGRESSION_LENGTH:
        progression.append(n)
        n += common_difference
        i += 1
    return progression


def create_question_line(progression, x_index):
    progression_line = [str(x) for x in progression]
    progression_line[x_index] = '..'
    question_line = ' '.join(progression_line)
    return question_line


def get_progression_game():
    initial_term = random.randint(INITIAL_RANGE_START, INITIAL_RANGE_END)
    common_difference = random.randint(2, 10)
    progression = get_progression(initial_term, common_difference)
    x_index = random.randint(X_INDEX_RANGE_START, X_INDEX_RANGE_END)
    question = create_question_line(progression, x_index)
    result = int(progression[x_index])
    return question, result
