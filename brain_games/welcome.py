def enter_username():
    name_user = prompt.string('May I have your name? ')
    return name_user


def welcome_user(name):
    print(f'Hello, {name}')
