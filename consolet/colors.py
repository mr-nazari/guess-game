import os

WINDOWS_COLOR_SET = {
    'black': '0',
    'blue': '1',
    'green': '2',
    'aqua': '3',
    'red': '4',
    'purple': '5',
    'yellow': '6',
    'white': '7',
    'gray': '8',
    'light_blue': '9',
    'light_green': 'A',
    'light_aqua': 'B',
    'light_red': 'C',
    'light_purple': 'D',
    'light_yellow': 'E',
    'bright_white': 'F',
}


class WindowsColorSet:
    # Standard Colors
    BLACK = '0'
    BLUE = '1'
    GREEN = '2'
    AQUA = '3'
    RED = '4'
    PURPLE = '5'
    YELLOW = '6'
    WHITE = '7'
    GRAY = '8'
    # Light Colors
    LIGHT_BLUE = '9'
    LIGHT_GREEN = 'A'
    LIGHT_AQUA = 'B'
    LIGHT_RED = 'C'
    LIGHT_PURPLE = 'D'
    LIGHT_YELLOW = 'E'
    LIGHT_WHITE = 'F'


class ColorSet:
    # Standard Colors
    BLACK = 'black'
    BLUE = 'blue'
    GREEN = 'green'
    AQUA = 'aqua'
    RED = 'red'
    PURPLE = 'purple'
    YELLOW = 'yellow'
    WHITE = 'white'
    GRAY = 'gray'
    # Light Colors
    LIGHT_BLUE = 'light_blue'
    LIGHT_GREEN = 'light_green'
    LIGHT_AQUA = 'light_aqua'
    LIGHT_RED = 'light_red'
    LIGHT_PURPLE = 'light_purple'
    LIGHT_YELLOW = 'light_yellow'
    LIGHT_WHITE = 'light_white'


class Color:

    def __init__(self, background_color='black', default_foreground_color='white', is_colorized=True, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.background_color = background_color
        self.default_foreground_color = default_foreground_color
        if is_colorized:
            self.colorize(self.background_color, self.default_foreground_color)

    def set_background_color(self, back_code):
        self.colorize(back_code, self.default_foreground_color)

    def set_foreground_color(self, fore_code):
        self.colorize(self.background_color, fore_code)

    @staticmethod
    def colorize(back_code, fore_code):
        # See : https://ss64.com/nt/color.html

        if back_code is not None:
            back_code = back_code.lower().replace(' ', '_')
        if fore_code is not None:
            fore_code = fore_code.lower().replace(' ', '_')

        if os.name == 'nt':
            if back_code is not None:
                back_code = WINDOWS_COLOR_SET.get(back_code, WINDOWS_COLOR_SET.get('black'))
            if fore_code is not None:
                fore_code = WINDOWS_COLOR_SET.get(fore_code, WINDOWS_COLOR_SET.get('white'))
            os.system(f'color {back_code}{fore_code}')
        else:
            pass
