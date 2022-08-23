import prompt
from brain_games.printing_templates import print_ok, print_unwin, congratulate
from brain_games.welcome import enter_username, welcome_user
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
            print_ok()
        else:
            print_unwin(user_answer, computer_answer, name_user)
            game_status = False
        attempt_counter -= 1

    if game_status:
        congratulate(name_user)


if __name__ == '__main__':
    main()
