# This is the main python script for running game.

# Console Manger for game
from consolet import Console, init_colorama

from colorama import Fore, Style

from gameplay import *
from gameplay.utils import get_console_position


def choice_type(console: Console):
    while True:
        try:
            # Select a type for game. if this isn't valid (not a number or etc), try again.

            console.new_line()
            console.write_line('Type 1:', text_style=Style.DIM)
            console.write_line('# In this game, the number is selected by computer. Guess the number.',
                               fore_color=Fore.BLUE)
            console.new_line()
            console.write_line('Type 2:', text_style=Style.DIM)
            console.write_line('# Play with computer.', fore_color=Fore.BLUE)
            console.new_line()
            console.write_line('Type 3:', text_style=Style.DIM)
            console.write_line('# Two-player game. Playing two people together.', fore_color=Fore.BLUE)
            console.new_line(2)

            type_id = console.get_input("Enter Number Of Type: ", int, exit_code='exit')
        except Exception:
            console.clear_console()
            console.write_line("Please enter a valid number", count=2, fore_color=Fore.RED)
        else:
            break
    return type_id


def run_gameplay(type_id: int, console: Console):
    # In this function by selected game type ID, run gameplay start function.
    while True:
        console.clear_console()
        game_plays = {
            1: gstart_1,
            2: gstart_2,
            3: gstart_3,
        }
        gp = game_plays.get(type_id)  # get start function of gameplay with type_id.
        if gp is None:  # If type_id is not valid show a message and try again.
            console.clear_console()
            console.write_line("Please enter a valid type ID (1 or 2 or 3)...", count=2, fore_color=Fore.RED)

            # Choice Type of game
            type_id = choice_type(console)
        else:
            break
    gp(console)  # calling start function


def main():
    """
    For dynamic things on console
    (like a console editor for example vim [It's just an example for using dynamic] ) you have to create this yourself
    in this time ... .
    """

    init_colorama()  # Init colorama for coloring texts in console

    # Define console
    console = Console()
    console.title = "Guess Game ಠ_ಠ"  # Change terminal title.
    console.change_terminal_size(80, 30)  # Change terminal size to 80 columns and 30 lines.
    console_position = get_console_position(console)
    console.rect.move_to(*console_position)  # centered console

    # Game loop
    while True:
        # Welcome section
        console.clear_console()
        console.write_line("Welcome to GuessGame V1 :)", fore_color=Fore.YELLOW)
        console.write_line("Enter 'exit' to exit the game", count=2, fore_color=Fore.YELLOW)

        # Choice Type of game
        type_id = choice_type(console)

        run_gameplay(type_id, console)  # start a new game play


if __name__ == '__main__':
    main()
