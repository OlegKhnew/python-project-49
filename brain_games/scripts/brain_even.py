#!/usr/bin/env python3

from brain_games.even import welcome_user
from brain_games.even import is_even_number


def main():
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


if __name__ == '__main__':
    main()
