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
            self.return_item_display()
        if self.object_class.id == 2:
            self.return_inventory_display()

    @staticmethod
    def format_description(description):
        formatted_description = "{:<40}".format(description[:40])
        return formatted_description

    def return_item_display(self):
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
        return_string += f"""{colored_line}

    {self.Clr.hex(item.tier_hex_color)}{item.name}{rst} - {self.Clr.italicize()}{str(item.type).capitalize()}{rst} ({item.quantity}x)
    {self.Clr.italicize()}{item.tier_name}{rst}
 
    {it}"{item.description}"{rst}

        
"""
        for specific in item.specifics:
            return_string += str(
                f"    {g}{item.specifics[specific]}{rst} {str(specific).replace('_', ' ').capitalize()}")

        return_string += f"""\n
    Worth {y}{item.value}{rst} Gold"""
        return return_string

    def return_inventory_display(self):
        return_string = """"""
        # colors
        r = self.Clr.hex('#ff0000')
        b = self.Clr.hex('#00aaff')
        y = self.Clr.hex('#ffd900')
        g = self.Clr.hex('#03fc13')
        it = self.Clr.italicize()
        rst = self.Clr.rst()
        # item display
        inventory = self.object_class
        char = '█'
        colored_line = f"{rst}{str(char) * int(self.game_settings['game_resolution'][1])}{rst}"
        return_string += f"""{colored_line}
    {it}Inventory{rst}
"""     
        for item_name in inventory.get_contents():
            item_class = inventory.get_contents()[item_name]
            print(f"> {self.Clr.hex(item_class.tier_hex_color)}{item_class.name}{rst} ({item_class.quantity}x)")

