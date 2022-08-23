import prompt
from brain_games.welcome import *
from random import randint


def check_even(number):
    return number % 2 == 0 and 'yes' or 'no'


def enter_answer():
    return prompt.string('Your answer: ').lower().strip()


def main():
    print('Welcome to the Brain Games!')
    name_user = enter_username()
    welcome_user(name_user)
    attempt_counter = 3
    game_status = True
    random_number = None
    while attempt_counter > 0 and game_status:
        random_number = randint(0, 100)
        print(f'Question: {random_number}')
        user_answer = enter_answer()
        computer_answer = check_even(random_number)
        if computer_answer == user_answer:
            print('Correct!')
        else:
            first_part_string = f"'{user_answer}' is wrong answer ;("
            second_part_string = f"Correct answer was '{computer_answer}'"
            print(f'{first_part_string} {second_part_string}')
            print(f"Let's try again, {name_user}")
            game_status = False
        attempt_counter -= 1

    if game_status:
        print(f'Congratulations, {name_user}!')


if __name__ == '__main__':
    main()
