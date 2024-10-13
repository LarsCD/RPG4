from level.menu.classes.Menu import Menu
from level.menu.view_player_stats import View_Player_Stats
# from assets.player.Player import Player
from utilities.GUT_2 import Color, GUT
from ascii_art_tester import ascii_animator


class Player_Menu(Menu):
    def __init__(self, player_class, menu_art):
        # imports
        self.Gut = GUT()
        self.Clr = Color()
        self.animator = ascii_animator()
        self.player_class = player_class
        self.menu_art = menu_art

        # menu settings
        self.menu_options = {}
        self.generate_menu_options()
        self.menu_settings = {
            'menu_art': menu_art,
            'menu_char': '',
            'menu_text': '',
            'menu_title': '',
            'menu_options': self.menu_options,
            'menu_line_char': '+',
            'menu_art_default_color': '#ffffff'
        }
        super().__init__(self.menu_settings)
        # vars
        self.in_menu = True

    def generate_menu_options(self):
        self.menu_options[f"1"] = f'Inventory'
        self.menu_options[f"2"] = f'Equipment'
        self.menu_options[f"3"] = f'Stats'
        self.menu_options[f"e"] = f'{self.Clr.hex("#ff0000")}Exit{self.Clr.rst()}'

    def user_input_manager(self, user_input):
        try:
            user_input = int(user_input)
        except:
            pass
        if isinstance(user_input, int):
            if user_input == 1:
                self.player_class.Inventory.view()
            if user_input == 2:
                print('#player_equipment_menu')
            if user_input == 3:
                self.player_class.view_player_stats()
        if user_input == 'e':
            self.in_menu = False
        else:
            pass

    def run_loop(self):
        while self.in_menu:
            super().print_full_menu_UI(no_top_bar=True)
            user_input = self.Gut.menu_select(self.menu_settings['menu_options'], self.menu_settings['menu_title'])
            self.user_input_manager(user_input)
