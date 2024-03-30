from utilities.GUT_2 import GUT, Color
from assets.art.menu_art import MENU_ART_1
from data.config.config_settings import GAME_DEFAULTS


class Main_Menu:
    def __init__(self):
        self.Gut = GUT()
        self.Clr = Color()

        self.MENU_ART = MENU_ART_1
        self.game_name = GAME_DEFAULTS['game_name']
        self.game_version = GAME_DEFAULTS['game_version']
        self.menu_options = {'1': 'Start Game',
                             '2': 'Load Game',
                             '3': f'{self.Clr.hex("#0088ff", bold=True)}Exit Game{self.Clr.rst()}'}

    def print_menu_art(self):
        print(self.MENU_ART)

    def menu_text(self):
        blue = self.Clr.hex("#0088ff", bold=True)
        purple = self.Clr.hex("#ae00ff", bold=True)
        orange = self.Clr.hex("#ff9100", bold=True)
        red = self.Clr.hex("#ff0000", bold=True)
        rst = self.Clr.rst()

        string = f"""
Welcome to {blue}{self.game_name}{rst} ({orange}{self.game_version}{rst}). This is a rogue-like, text based 
dungeon crawler. Fight {red}monsters{rst}, find {purple}loot{rst} and get to the end??? Enjoy

By: {self.Clr.bold()}LarsCD{rst}
"""
        return string

    def main_loop(self):
        in_menu = True
        while in_menu:
            self.Gut.clear_screen()
            self.Gut.draw_line(char='█')
            self.print_menu_art()
            self.Gut.draw_line(char='+')
            menu_text_string = self.menu_text()
            user_input = self.Gut.menu_select(self.menu_options, text=menu_text_string)


if __name__ == '__main__':
    Main_Menu().main_loop()

