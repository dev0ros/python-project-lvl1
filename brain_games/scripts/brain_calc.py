import prompt
from random import choice
from random import randint
from brain_games.printing_templates import print_ok, print_unwin, congratulate
from brain_games.welcome import enter_username, welcome_user


def choice_operator():
    operations = '+*-'
    return choice(operations)


def make_expression():
    first_num = randint(0, 100)
    second_num = randint(0, 100)
    operation_with_nums = choice_operator()
    return f'{first_num} {operation_with_nums} {second_num}'


def calculate_expression(expression):
    return eval(expression)


def is_equal(first_num, second_num):
    return first_num == second_num


def main():
    print('Welcome to the Brain Games!')
    name_user = enter_username()
    welcome_user(name_user)
    print('What is the result of the expression?')
    attempt_counter = 3
    game_status = True
    while attempt_counter > 0 and game_status:
        our_expression = make_expression()
        computer_answer = calculate_expression(our_expression)
        print(f'Question: {our_expression}')
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
