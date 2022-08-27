import prompt
from random import randint
from brain_games.printing_templates import print_ok, print_unwin, congratulate
from brain_games.welcome import enter_username, welcome_user


def generate_data_progession():
    len_progession = randint(5, 10)
    step_progression = randint(1, 5)
    return (len_progession, step_progression)


def generate_progession():
    length, step = generate_data_progession()

    first_num_progression = randint(1, 100)
    progression = (first_num_progression,)
    next_num_progression = first_num_progression

    iteration = 0
    while iteration < length - 1:
        next_num_progression += step
        progression = progression + (next_num_progression, )
        iteration += 1

    return progression


def print_progression(progression):
    for element in progression:
        print(element, end='')


def make_secret_progression(progression):
    random_index = randint(0, len(progression) - 1)

    progression_with_secret = ''
    for element in progression:
        insert_num = element
        if progression[random_index] == element:
            insert_num = '..'
        progression_with_secret = f'{progression_with_secret} {insert_num}'
    return progression_with_secret, progression[random_index]


def main():
    print('Welcome to the Brain Games!')
    name_user = enter_username()
    welcome_user(name_user)
    print('What number is missing in the progression?')

    attempt_counter = 3
    game_status = True
    while attempt_counter > 0 and game_status:
        progression = generate_progession()
        sec_progression, right_answer = make_secret_progression(progression)
        print(f'Question: {sec_progression}')
        user_answer = prompt.integer('Your answer: ')
        if user_answer == right_answer:
            print_ok()
        else:
            print_unwin(user_answer, right_answer, name_user)
            game_status = False
        attempt_counter -= 1

    if game_status:
        congratulate(name_user)


if __name__ == '__main__':
    main()
