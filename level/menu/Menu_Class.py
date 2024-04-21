from utilities.GUT_2 import GUT, Color
from data.config.config_settings import GAME_DEFAULTS


class Menu_Class:
    def __init__(self, menu_settings, game_defaults=GAME_DEFAULTS):
        # imports
        self.Gut = GUT()
        self.Clr = Color()

        # game preferences
        self.game_name = game_defaults['game_name']
        self.game_version = game_defaults['game_version']

        # menu preferences
        self.menu_art = menu_settings['menu_art']
        self.menu_char = menu_settings['menu_char']
        self.menu_text = menu_settings['menu_text']
        self.menu_title = menu_settings['menu_title']
        self.menu_options = menu_settings['menu_options']
        self.menu_line_char = menu_settings['menu_line_char']
        self.menu_art_default_color = menu_settings['menu_art_default_color']

    def print_menu_art(self):
        print(self.menu_art)

    def print_full_menu_UI(self, no_top_bar=False):
        self.Gut.clear_screen()
        if not no_top_bar:
            self.Gut.draw_line(char=self.menu_char)
        print(self.Clr.hex(self.menu_art_default_color))
        self.print_menu_art()
        print(self.Clr.rst())
        self.Gut.draw_line(char=self.menu_line_char)
        menu_text_string = self.menu_text
        return menu_text_string
