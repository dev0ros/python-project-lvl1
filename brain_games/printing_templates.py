def print_ok():
    print('Correct!')


def print_unwin(user_answer, computer_answer, name_user):
    first_part_string = f"'{user_answer}' is wrong answer ;("
    second_part_string = f"Correct answer was '{computer_answer}'"
    print(f'{first_part_string} {second_part_string}')
    print(f"Let's try again, {name_user}")


def congratulate(name_user):
    print(f'Congratulations, {name_user}!')
