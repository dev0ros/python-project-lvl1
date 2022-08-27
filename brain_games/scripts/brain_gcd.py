import prompt
from random import randint
from math import gcd
from brain_games.printing_templates import print_ok, print_unwin, congratulate
from brain_games.welcome import enter_username, welcome_user


def is_equal(first_num, second_num):
    return first_num == second_num


def main():
    print('Welcome to the Brain Games!')
    name_user = enter_username()
    welcome_user(name_user)
    print('Find the greatest common divisor of given numbers?')
    attempt_counter = 3
    game_status = True
    while attempt_counter > 0 and game_status:
        first_num = randint(1, 100)
        second_num = randint(1, 100)
        print(f'Question: {first_num} {second_num}')
        computer_answer = gcd(first_num, second_num)
        user_answer = prompt.integer('Your answer: ')
        if is_equal(computer_answer, user_answer):
            print_ok()
        else:
            print_unwin(user_answer, computer_answer, name_user)
            game_status = False
        attempt_counter -= 1

    if game_status:
        congratulate(name_user)


if __name__ == '__main__':
    main()
