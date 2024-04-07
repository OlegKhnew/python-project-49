#!/usr/bin/env python3

import prompt


def game_logic(rule, function):
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(rule)
    count = 0
    while count < 3:
        question, result = function()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            count += 1
            continue
        else:
            answer = f"'{answer}' is wrong answer ;(. "\
                     f"Correct answer was '{result}'."
            print(answer)
# print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():
    game_logic()


if __name__ == '__main__':
    main()
