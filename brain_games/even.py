

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

