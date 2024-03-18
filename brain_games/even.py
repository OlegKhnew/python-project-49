import prompt
import random

def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def is_even_number():
    number = random.randint(1, 100)
    print('Question: ' + str(number))
    answer = prompt.string('Your answer: ')
    if number % 2 == 0:
        correct = 'yes'
    else:
        correct = 'no'

    if answer == correct:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        return False


def is_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        if is_even_number():
            count += 1
            continue
        else:
            break
    if count == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
