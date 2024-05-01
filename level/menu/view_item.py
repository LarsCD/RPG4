from level.menu.classes.Menu import Menu
# from level.menu.classes.View import View
from utilities.GUT_2 import Color, GUT
from ascii_art_tester import ascii_animator


class View_Item(Menu):
    def __init__(self, item_class, menu_art):
        # imports
        self.Gut = GUT()
        self.Clr = Color()
        self.animator = ascii_animator()
        self.current_item = item_class
        self.menu_art = menu_art

        # menu settings
        self.menu_options = {}
        self.generate_menu_options()
        self.menu_settings = {
            'menu_art': self.menu_art,
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
        highest_index = 0
        for i, option in enumerate(self.current_item.item_view_options):
            self.menu_options[f"{i+1}"] = str(option).replace('_', ' ').capitalize()
            highest_index = i
        self.menu_options[f"e"] = f'{self.Clr.hex("#ff0000")}Exit{self.Clr.rst()}'

    def user_input_manager(self, user_input):
        match user_input:
            case '1':
                pass
            case '2':
                # inventory
                pass
            case '3':
                # disengage
                pass
            case 'e':
                self.in_menu = False

    def run_loop(self):
        while self.in_menu:
            super().print_full_menu_UI(no_top_bar=True)
            user_input = self.Gut.menu_select(self.menu_settings['menu_options'], self.menu_settings['menu_title'])
            self.user_input_manager(user_input)
