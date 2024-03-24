#!/usr/bin/env python3

import random
import prompt


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def prime_game():
    n = random.randint(1, 200)
    if is_prime(n):
        result = 'yes'
    else:
        result = 'no'
    print(f'Question: {n}')
    answer = prompt.string('Your answer: ')
    return answer, result
