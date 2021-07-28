import random

from consolet import Console
from colorama import Fore

from .utils import (
    get_input_from_user,
    get_range_of_numbers,
    user_number_check,
    get_console_position,
)


def start(console: Console):
    console.write_line(
        "About: In this game, A random number selected for player1 and\n"
        "another random number selected for player2.\n"
        "Whoever responds faster wins (*^-^*)",
        count=2,
        fore_color=Fore.LIGHTBLUE_EX,
    )

    from_number, to_number = get_range_of_numbers(console)

    console.terminal_columns += 15
    console_position = get_console_position(console)
    console.rect.move_to(*console_position)  # centered console

    console.write_line("Guess the selected number ^_^")
    console.write_line(f"It's start from {from_number} to {to_number}", count=3)

    console.sleep_(1)
    random_number_player1 = random.randint(from_number, to_number)
    random_number_player2 = random.randint(from_number, to_number)

    guess_count = 1
    while True:
        guess_number_player1 = get_input_from_user(
            console, "Player1 | " + str(guess_count)
        )
        if user_number_check(
            console, guess_number_player1, random_number_player1, guess_count
        ):
            break
        guess_number_player2 = get_input_from_user(
            console, "Player2 | " + str(guess_count), space=40
        )
        if user_number_check(
            console, guess_number_player2, random_number_player2, guess_count, space=40
        ):
            break

        guess_count += 1

    console.write("Please wait for 3 seconds, then redirect to home page ^_~")
    console.sleep_(3)
