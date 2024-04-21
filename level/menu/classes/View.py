# from assets.classes.Item import Item
from utilities.GUT_2 import GUT, Color
from data.config.config_settings import GAME_SETTINGS


class View:
    def __init__(self, object_class):
        self.game_settings = GAME_SETTINGS
        self.Gut = GUT()
        self.Clr = Color()
        self.object_class = object_class
        self.display_manager()

    def display_manager(self):
        if self.object_class.id == 1:
            self.print_item_display()

    @staticmethod
    def format_description(description):
        formatted_description = "{:<40}".format(description[:40])
        return formatted_description

    def print_item_display(self):
        display_string = self.return_return_display()
        return display_string

    def return_return_display(self):
        return_string = """"""
        # colors
        r = self.Clr.hex('#ff0000')
        b = self.Clr.hex('#00aaff')
        y = self.Clr.hex('#ffd900')
        g = self.Clr.hex('#03fc13')
        it = self.Clr.italicize()
        rst = self.Clr.rst()
        # item display
        item = self.object_class
        char = '█'
        colored_line = f"{self.Clr.hex(item.tier_hex_color)}{str(char) * int(self.game_settings['game_resolution'][1])}{rst}"
        return_string += f"""{colored_line}\n\n [{self.Clr.hex(item.tier_hex_color)}{item.name}{rst} - {self.Clr.italicize()}{item.tier_name}{rst}]
 {self.Clr.italicize()}{str(item.type).capitalize()}{rst}\n\n   {it}"{item.description}"{rst}
        
"""
        for specific in item.specifics:
            return_string += str(
                f"    {g}{item.specifics[specific]}{rst} {str(specific).replace('_', ' ').capitalize()}")

        return_string += f"""\n
    Amount: x{item.quantity}
    Value: {y}{item.value}{rst} gold
"""
        return return_string
