import random
from winsound import Beep

from consolet import Console
from colorama import Fore, Back

from .utils import get_input_from_user, get_range_of_numbers, user_number_check


def start(console: Console):
    console.write_line(
        "About: In this game, A random number selected for you and\n"
        "another random number selected for computer.\n"
        "Whoever responds faster wins (*^-^*)",
        count=2,
        fore_color=Fore.LIGHTBLUE_EX,
    )

    from_number, to_number = get_range_of_numbers(console)

    # TODO: Add computer level (Like Easy, Middle, Hard, etc.) with many different algorithms.

    console.write_line("Guess the selected number ^_^")
    console.write_line(f"It's start from {from_number} to {to_number}", count=3)

    console.sleep_(1)
    random_number_user = random.randint(from_number, to_number)
    random_number_computer = random.randint(from_number, to_number)

    guess_count = 1
    x, y = from_number, to_number
    while True:
        guess_number_user = get_input_from_user(console, guess_count)

        if user_number_check(
            console, guess_number_user, random_number_user, guess_count
        ):
            break

        guess_number_computer = (x + y) // 2
        console.write_line(40 * " " + f"Guess the computer is: {guess_number_computer}")
        if random_number_computer == guess_number_computer:
            console.write(40 * " ")
            console.write_line("Computer win `(*>﹏<*)′", count=3, back_color=Back.RED)
            for i in range(700, 200, -20):
                Beep(i, 100)
            break
        elif random_number_computer < guess_number_computer:
            y = guess_number_computer
        else:
            x = guess_number_computer

        guess_count += 1

    console.write("Please wait for 3 seconds, then redirect to home page ^_~")
    console.sleep_(3)
