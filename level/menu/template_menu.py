from level.menu.classes.Menu import Menu
from utilities.GUT_2 import Color, GUT
from ascii_art_tester import ascii_animator

from art.characters.enemies.frog_sprite_art import frog_sprite_art
from art.animations.slash_1 import frames as animation_slash_1


class Template_Menu(Menu):
    def __init__(self):
        # imports
        self.Gut = GUT()
        self.Clr = Color()
        self.animator = ascii_animator()

        # settings
        menu_options = {
            '1': 'Attack',
            '2': 'Inventory',
            '3': f'{self.Clr.hex("#ff0000", bold=True)}Disengage{self.Clr.rst()}',
        }
        self.menu_settings = {
            'menu_art': frog_sprite_art,
            'menu_char': '+',
            'menu_text': '[TEXT]',
            'menu_title': '[TITLE]',
            'menu_options': menu_options,
            'menu_line_char': '=',
            'menu_art_default_color': '##c90000'
        }
        super().__init__(self.menu_settings)
        # vars
        self.in_menu = True

    def user_input_manager(self, user_input):
        match user_input:
            case '1':
                # attack
                self.animator.animate(animation_slash_1, loop=1)
            case '2':
                # inventory
                pass
            case '3':
                # disengage
                pass

    def main_loop(self):
        while self.in_menu:
            super().print_full_menu_UI()
            user_input = self.Gut.menu_select(self.menu_settings['menu_options'], self.menu_settings['menu_title'])
            self.user_input_manager(user_input)
