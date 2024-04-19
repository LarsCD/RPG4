"""
###############################################################
RPG4 (Working Title)
By: LarsCD(2002)

File: Main file to run tests


###############################################################
"""
from level.menu.main_menu_test import Main_Menu
from level.menu.template_menu import Template_Menu
from utilities.game_window_tools import GameWindowTools
from utilities.dataloader import Dataloader
from classes.Item import Item
from classes.Inventory import Inventory

GameWindowTools().run_setup()

Inventory = Inventory('Player')
item_data = Dataloader().load_item_data()

Inventory.add_item(item_data[0]['placeholder_apple'], 2)
Inventory.remove_item(item_data[0]['placeholder_apple'], 3)
Inventory.add_item(item_data[0]['placeholder_weapon'], 1)
Inventory.remove_item(item_data[0]['placeholder_apple'], 1)
Inventory.add_item(item_data[0]['throwable_apple'], 2)
print(Inventory.content_list)

# Template_Menu().main_loop()
Main_Menu().main_loop()
