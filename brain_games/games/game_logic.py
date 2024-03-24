#!/usr/bin/env python3

import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def goodbye_user(count, name):
    if count == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def question(function):
    if 'even' in str(function):
        print('Answer "yes" if the number is even, otherwise answer "no".')
    if 'calc' in str(function):
        print('What is the result of the expression?')
    if 'gcd' in str(function):
        print('Find the greatest common divisor of given numbers.')


def check_result(answer, result):
    if answer == result:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        return False


def game_logic(function):
    name = welcome_user()
    question(function)
    count = 0
    while count < 3:
        answer, result = function()
        if check_result(answer, result):
            count += 1
            continue
        else:
            break
    goodbye_user(count, name)


def main():
    game_logic()


if __name__ == '__main__':
    main()
