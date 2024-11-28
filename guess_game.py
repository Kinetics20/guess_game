import random


def convert_user_input(user_input: str) -> int:
    return int(user_input)


def get_user_range() -> tuple[int, int]:
    min_range_txt: str = input(f'Enter min range:\n')
    max_range_txt: str = input(f'Enter max range:\n')

    try:
        min_range: int = convert_user_input(min_range_txt)
        max_range: int = convert_user_input(max_range_txt)
    except ValueError:
        print('Please enter a valid numbers')
        raise ValueError('Invalid numbers.')

    if min_range > max_range:
        raise ValueError('Range max has to be greater than range min.')

    if max_range == min_range:
        raise ValueError('Range min and max have to not be equal')

    return min_range, max_range


def draw_number(min_number: int, max_number: int) -> int:
    return random.randint(min_number, max_number)


def guess_number(min_number: int, max_number: int, drawn_number: int) -> None:
    print(f'Guess number from range: {min_number} to {max_number}. Good Luck!')

    counter: int = 0

    while True:
        try:
            user_digit: int = convert_user_input(input('Enter valid number: \n'))
        except ValueError:
            continue

        counter += 1

        if user_digit > drawn_number:
            print(f'Too high')
        elif user_digit < drawn_number:
            print(f'Too low')
        else:
            print(f'You won! Your numbers of guesses: {counter}')
            break




