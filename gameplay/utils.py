from winsound import Beep

from consolet.utils import get_system_metrics

from colorama import Fore


def get_input_from_user(console, guess_count, space=0):
    while True:
        is_value_None = False
        try:
            guess_number = console.get_input(space * ' ' + f"[{guess_count}] Enter your guess: ", int, exit_code='exit',
                                             commands={'clear': console.clear_console})
            if guess_number is None:
                is_value_None = True
                raise
        except Exception:
            if not is_value_None:
                console.write_line(space * ' ' + 'You must enter a number :|', fore_color=Fore.CYAN, count=2)
        else:
            break
    return guess_number


def get_range_of_numbers(console):
    while True:
        try:
            console.fore_color = Fore.MAGENTA
            console.write_line('Please enter range of number (from | to)')
            from_number = console.get_input("From: ", int, exit_code='exit')
            to_number = console.get_input("To: ", int, exit_code='exit')
            console.fore_color = Fore.RESET
        except Exception:
            console.write_line('Wrong range. Inputs must be numbers...', fore_color=Fore.RED, count=2)
        else:
            console.clear_console()
            break
    return from_number, to_number


def user_number_check(console, guess_number, random_number, guess_count, space=0):
    if random_number == guess_number:
        for i in range(300, 800, 20):
            Beep(i, 100)
        console.write_line(space * ' ' + f'You win! In {guess_count} moves...', count=2, fore_color=Fore.LIGHTGREEN_EX)
        return True
    elif random_number < guess_number:
        Beep(467, 430)
        console.write_line(space * ' ' + '> Enter a smaller number', count=2, fore_color=Fore.LIGHTRED_EX)
    else:
        Beep(467, 430)
        console.write_line(space * ' ' + '> Enter a larger number', count=2, fore_color=Fore.LIGHTRED_EX)
    return False


def get_console_position(console):
    monitor_width, monitor_height = get_system_metrics()
    _, _, console_width, console_height = console.rect.refresh()
    return (monitor_width - console_width) // 2, (monitor_height - console_height) // 2
