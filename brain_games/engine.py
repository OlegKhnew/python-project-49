#!/usr/bin/env python3

import prompt


ROUNDS = 3


def run_game(rule, get_question_and_result):
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(rule)
    count = 0
    while count < ROUNDS:
        question, result = get_question_and_result()
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
            break
    if count == ROUNDS:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def main():
    run_game()


if __name__ == '__main__':
    main()
