import random

from consolet import Console
from colorama import Fore

from .utils import get_input_from_user, get_range_of_numbers, user_number_check


def start(console: Console):
    console.write_line('About: In this game, the number is selected by computer. Guess the number.', count=2,
                       fore_color=Fore.LIGHTBLUE_EX)

    from_number, to_number = get_range_of_numbers(console)

    console.write_line('Guess the selected number ^_^')
    console.write_line(f'It\'s start from {from_number} to {to_number}', count=3)

    console.sleep_(1)
    random_number = random.randint(from_number, to_number)

    guess_count = 1
    while True:
        guess_number = get_input_from_user(console, guess_count)

        if user_number_check(console, guess_number, random_number, guess_count):
            break

        guess_count += 1

    console.write('Please wait for 3 seconds, then redirect to home page ^_~')
    console.sleep_(3)
