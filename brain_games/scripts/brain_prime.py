import prompt
from random import randint
from brain_games.printing_templates import print_ok, print_unwin, congratulate
from brain_games.welcome import enter_username, welcome_user


def check_number_prime(number):
    temp_number = 2
    while temp_number < number:
        if number % temp_number == 0:
            return False
        temp_number += 1
    return True


def is_number_prime(number):
    return check_number_prime(number) and 'yes' or 'no'


def main():
    print('Welcome to the Brain Games!')
    name_user = enter_username()
    welcome_user(name_user)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    attempt_counter = 3
    game_status = True
    while attempt_counter > 0 and game_status:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        computer_answer = is_number_prime(random_number)
        user_answer = prompt.string('Your answer: ').lower().strip()
        if user_answer == computer_answer:
            print_ok()
        else:
            print_unwin(user_answer, computer_answer, name_user)
            game_status = False
        attempt_counter -= 1

    if game_status:
        congratulate(name_user)


if __name__ == '__main__':
    main()
