from os import system

import colorama as col
from data.config.config_settings import DEFAULT_GUT_SETTINGS


class GUT:
    def __init__(self, SETTINGS=DEFAULT_GUT_SETTINGS):
        self.settings = SETTINGS
        self.hl_color = col.Fore.GREEN
        self.bar_fg_color = col.Fore.BLACK
        self.bar_bg_color = col.Back.LIGHTBLACK_EX
        self.rst = col.Style.RESET_ALL

        self.standard_bar_text = "[Type \'/\' for commands, \'/h\' or \'/help\' for list of commands]"

    def clear_screen(self):
        system('cls' if self.settings.get('os', 'windows') == 'windows' else 'clear')

    def draw_line(self, char=None):
        if char is None:
            print('' * self.settings['default_line_size'])
        else:
            print(str(char) * self.settings['default_line_size'])

    def draw_title(self, title):
        print(f"[{title}]")

    def draw_text(self, text):
        print(f"{text}")

    def draw_warning(self, text):
        print(f"{col.Fore.LIGHTYELLOW_EX} > [WARNING]: {text}{self.rst}")

    def draw_error(self, text):
        print(f"{col.Fore.RED} > [ERROR]: {text}{self.rst}")

    def click_text(self, text=""):
        self.draw_text(text)
        input()

    def click_error(self, text):
        self.draw_error(text)
        input()

    def input_entry(self, text=""):
        input_entry = input(f" {text}> ")
        return input_entry

    def draw_bar_text(self, text=""):
        if text == "":
            text = self.standard_bar_text

        print(f'{self.bar_bg_color} {self.bar_fg_color} {text}{self.rst}')

    def draw_box(self, width, height):
        for _ in range(height):
            self.draw_line()

    @staticmethod
    def align_text(text, width, alignment='left'):
        if alignment == 'l':
            return text.ljust(width)
        elif alignment == 'r':
            return text.rjust(width)
        elif alignment == 'c':
            return text.center(width)
        else:
            return f"{text}"

    def menu_select(self, options, title=None, text=None, bar_text="", error_text: list = [],
                    clear_screen=False, draw_line=False):
        if title is not None:
            self.clear_screen()
        if clear_screen is True:
            self.draw_line(char="")
        if draw_line is True:
            self.draw_title(title)
        if text:
            self.draw_text(text)
        for key, value in options.items():
            print(f' [{self.hl_color}{key.capitalize()}{self.rst}]: {value}')

        for line in error_text:
            print(f"{col.Fore.RED}> [ERROR]: {line}{self.rst}")

        if bar_text != "":
            self.draw_bar_text(bar_text)
        user_input = input(f"> ")
        return user_input

    def display_text(self, title, text, options=None, bar_text="", error_text: list = []):

        self.clear_screen()
        self.draw_line()
        self.draw_title(title)

        if isinstance(text, str):
            text = text.split('\n')  # Split the text into paragraphs based on newline characters

        for paragraph in text:
            lines = paragraph.split('\n')  # Split each paragraph into lines
            for line in lines:
                print(f"{line}")  # Print each line prefixed with the desired character

        if options:
            for key, value in options.items():
                print(f'[{self.hl_color}{key.capitalize()}{self.rst}]: {value}')

        for line in error_text:
            print(f"{col.Fore.RED}> [ERROR]: {line}{self.rst}")

        self.draw_bar_text(bar_text)
        user_input = input(f"> ")
        return user_input


class Color:
    def __init__(self):
        pass

    @staticmethod
    def rst():
        return col.Style.RESET_ALL

    @staticmethod
    def bold():
        return '\x1b[1m'

    @staticmethod
    def italicize():
        return '\x1b[3m'

    @staticmethod
    def hex(hex_color, bold=False, italicize=False):
        # Remove '#' if present
        hex_color = hex_color.lstrip('#')

        # Convert hex to RGB
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        # ANSI escape sequence for colorizing text
        ansi_code = f'\x1b[38;2;{r};{g};{b}m'

        # Add ANSI escape sequences for bold and italicized text if requested
        if bold:
            ansi_code += '\x1b[1m'  # Bold
        if italicize:
            ansi_code += '\x1b[3m'  # Italicize

        return ansi_code


# Example usage:
if __name__ == "__main__":
    settings = {
        'os': 'windows',
        'char': '█',
        'default_line_size': 80
    }
    gut = GUT(settings)
    gut.clear_screen()
    gut.draw_line()
    gut.draw_title('Sample Title')
    gut.draw_text('This is a sample text.')
    # gut.draw_box(20, 5)
    options = {'a': 'Option A', 'b': 'Option B', 'c': 'Option C'}
    user_input = gut.menu_select(options, title='Menu', text='Please select an option:',
                                 error_text=["File \'homework.COS\' could not be saved correctly"])
    gut.display_text('TITLE', '''Wow, look at me!
Is this working

I think so!''', options=options)
    gut.click_error("Command could not be completed successfully")
    options2 = {'1': 'START COREOS', '2': 'SETTINGS', '3': 'EXIT'}
    gut.menu_select(options2, title='COREOS GAMMA STARTUP', bar_text="[For advanced config type: \'/config\']")
