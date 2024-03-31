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


def check_result(answer, result):
    if answer == str(result):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        return False


def game_logic(rule, function):
    name = welcome_user()
    print(rule)
    count = 0
    while count < 3:
        question, result = function()
        print(question)
        answer = prompt.string('Your answer: ')
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
