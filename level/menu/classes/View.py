from level.menu.view_player_stats import View_Player_Stats
from level.menu.view_inventory import View_Inventory
from level.menu.view_item import View_Item
from level.menu.player_menu import Player_Menu
from logic.Game_rules import Game_rules

from utilities.GUT_2 import GUT, Color
from data.config.config_settings import GAME_SETTINGS


class View:
    def __init__(self, object_class, id=None):
        self.game_settings = GAME_SETTINGS
        self.Gut = GUT()
        self.Clr = Color()
        self.object_class = object_class
        self.display_manager(id=id)

    def display_manager(self, id=None):
        # check if object_class is given a special id
        if id is not None:
            if id == 4:
                View_Player_Stats(self.object_class, self.return_player_stats_display()).run_loop()
        # check for normal object_class id's
        else:
            if self.object_class.id == 1:
                View_Item(self.object_class, self.return_item_display()).run_loop()
            if self.object_class.id == 2:
                View_Inventory(self.object_class, self.return_inventory_display()).run_loop()
            if self.object_class.id == 3:
                # View_Player_Stats(self.object_class, self.return_player_stats_display()).run_loop()
                Player_Menu(self.object_class, self.return_player_menu_display()).run_loop()


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

    {self.Clr.hex(item.tier_hex_color)}{item.name}{rst} | {self.Clr.italicize()}{str(item.type).capitalize()}{rst} ({item.quantity}x)
    {self.Clr.italicize()}{item.tier_name}{rst}

    {it}"{item.description}"{rst}

"""
        for specific in item.specifics:
            plus_sign = ''
            value = item.specifics[specific]
            # check for plus sigh with attributes
            if isinstance(value, int):
                if str(specific).lower() in Game_rules().attribute_index:
                    if value > 0:
                        plus_sign = '+'
            if isinstance(value, list):
                value = ""
                for i, specific_list_index in enumerate(item.specifics[specific]):
                    if i > 0:
                        value += ', '
                    value += f"{str(specific_list_index).replace('_', ' ').title()}"

            return_string += str(
                f"    |    {g}{plus_sign}{value}{rst} {str(specific).replace('_', ' ').title()}")

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
        o = self.Clr.hex('#ff9500')
        it = self.Clr.italicize()
        rst = self.Clr.rst()
        # item display
        inventory = self.object_class
        char = '█'
        colored_line = f"{rst}{str(char) * int(self.game_settings['game_resolution'][1])}{rst}"
        format_buffer_size = {
            'name': 21,
            'tier': 10,
            'type': 12,
            'amount': 6,
            'value': 6,
        }

        return_string += f"""{colored_line}

    {it}Inventory{rst} | [{o}S{rst}] Sort: {it}{o}Tier{rst}

    [XX]   Item{" " * int(format_buffer_size['name'] - 4)}  |  Tier{" " * int(format_buffer_size['tier'] - 4)}  |  Type{" " * int(format_buffer_size['type'] - 4)}  |  Amount{" " * int(format_buffer_size['amount'] - 6)}   |  Value{" " * int(format_buffer_size['value'] - 5)}  |"""

        current_item_type = None
        for i, item_name in enumerate(inventory.get_contents()):
            item_class = inventory.get_contents()[item_name]

            # formatting
            name_str_buffer = (" " * int(format_buffer_size['name'] - len(f"{item_class.name}")))
            tier_str_buffer = (" " * int(format_buffer_size['tier'] - len(f"{item_class.tier_name}")))
            type_str_buffer = (" " * int(format_buffer_size['type'] - len(f"{item_class.type}")))
            amount_str_buffer = (" " * int(format_buffer_size['amount'] - len(f"{item_class.quantity}")))
            value_str_buffer = (" " * int(format_buffer_size['value'] - len(f"{item_class.value}")))

            if item_class.type != current_item_type:
                return_string += f"\n    -- {it}{str(item_class.type).replace('_', ' ').title()}{rst} --"
                current_item_type = item_class.type

            return_string += f"\n    [{o}{i + 1:02}{rst}]   {self.Clr.hex(item_class.tier_hex_color)}{item_class.name}{rst}{name_str_buffer}  |  {self.Clr.hex(item_class.tier_hex_color)}{str(item_class.tier_name).title()}{rst}{tier_str_buffer}  |  {it}{str(item_class.type).replace('_', ' ').title()}{rst}{type_str_buffer}  |  {item_class.quantity}x{amount_str_buffer}  |  {y}{item_class.value}{rst} g{value_str_buffer}|"
        return return_string

    def return_player_stats_display(self):
        return_string = """"""
        # colors
        self.Gut = GUT()
        r = self.Clr.hex('#ff0000')
        b = self.Clr.hex('#00aaff')
        y = self.Clr.hex('#ffd900')
        g = self.Clr.hex('#03fc13')
        o = self.Clr.hex('#ff9500')
        it = self.Clr.italicize()
        rst = self.Clr.rst()
        bld = self.Clr.bold()
        player = self.object_class
        char = '█'
        colored_line = f"{rst}{str(char) * int(self.game_settings['game_resolution'][1])}{rst}"
        return_string += f"""{colored_line}
        
    [{it}{bld}{player.character['name']}{rst}]      Class: {bld}{player.class_info['class_name']}{rst}
    \\\\ Level {bld}{player.level['current']}{rst}
    
    STATUS
    {self.Gut.stat_bar("Health", player.stats['hp']['current']-10, player.stats['hp']['max'], 30, "/", '#ffffff', '#ff0000')}
    {self.Gut.stat_bar("XP    ", player.stats['xp']['current']+20, player.stats['xp']['max'], 20, "|", '#ffffff', '#ffffff')}

    {self.Gut.stat_bar("Energy", player.stats['ep']['current'], player.stats['ep']['max'], 30, "/", '#ffffff', '#ff9500')}
    {self.Gut.stat_bar("Mana  ", player.stats['mp']['current'], player.stats['mp']['max'], 30, "/", '#ffffff', '#00aaff')}

    ATTRIBUTES
    STR     : {it}{g}{player.attributes['current']['strength']}{rst}
    SPD     : {it}{g}{player.attributes['current']['speed']}{rst}
    AGI     : {it}{g}{player.attributes['current']['agility']}{rst}
    INT     : {it}{g}{player.attributes['current']['intelligence']}{rst}
    STL     : {it}{g}{player.attributes['current']['stealth']}{rst}
    SOR     : {it}{g}{player.attributes['current']['sorcery']}{rst}

"""
        return return_string

    def return_player_menu_display(self):
        return_string = """"""
        # colors
        self.Gut = GUT()
        r = self.Clr.hex('#ff0000')
        b = self.Clr.hex('#00aaff')
        y = self.Clr.hex('#ffd900')
        g = self.Clr.hex('#03fc13')
        o = self.Clr.hex('#ff9500')
        it = self.Clr.italicize()
        rst = self.Clr.rst()
        bld = self.Clr.bold()
        player = self.object_class
        char = '█'
        colored_line = f"{rst}{str(char) * int(self.game_settings['game_resolution'][1])}{rst}"
        return_string += f"""{colored_line}
    PLAYER MENU
    
    [{it}{bld}{player.character['name']}{rst}]      Class: {bld}{player.class_info['class_name']}{rst}
    \\\\ Level {bld}{player.level['current']}{rst}
    
       
    STATUS
    {self.Gut.stat_bar("Health", player.stats['hp']['current']-10, player.stats['hp']['max'], 30, "/", '#ffffff', '#ff0000')}
    {self.Gut.stat_bar("XP    ", player.stats['xp']['current']+20, player.stats['xp']['max'], 20, "|", '#ffffff', '#ffffff')}
"""
        return return_string


