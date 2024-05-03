"""
###############################################################
RPG4 (Working Title)
By: LarsCD(2002)

File: Main file to run tests


###############################################################
"""
import time

from level.menu.main_menu_test import Main_Menu
from utilities.game_window_tools import GameWindowTools
from utilities.dataloader import Dataloader
from assets.classes.Inventory import Inventory
from assets.classes.Character import Character
from assets.player.Player import Player

GameWindowTools().run_setup()

# Inventory = Inventory('Player')
DATALOADER = Dataloader()
item_data = DATALOADER.load_item_data()
player_class_data = DATALOADER.load_player_class_data()

"""------------------------------------ Zombie code here :3 ------------------------------------"""
# Inventory.add_item(item_data['placeholder_apple'], 5)
# Inventory.add_item(item_data['orkian_battle_axe'], 1)
# Inventory.remove_item(item_data[0]['placeholder_apple'], 3)
# Inventory.add_item(item_data['placeholder_weapon'], 1)
# Inventory.remove_item(item_data[0]['placeholder_apple'], 1)
# Inventory.add_item(item_data['throwable_apple'], 2)

# Inventory.get_contents()['placeholder_apple'].item_view_menu()
# Inventory.get_contents()['placeholder_weapon'].item_view_menu()
# Inventory.get_contents()['throwable_apple'].item_view_menu()
# Inventory.get_contents()['orkian_battle_axe'].item_view_menu()

# Inventory.get_contents()['placeholder_apple'].use_consumable()
# Inventory.get_contents()['placeholder_apple'].destroy()
# Inventory.get_contents()['placeholder_apple'].use_weapon()
# Inventory.get_contents()['throwable_apple'].use_weapon()
# Inventory.get_contents()['orkian_battle_axe'].use_weapon()
"""------------------------------------ Zombie code here :3 ------------------------------------"""


# print(item_data)
# print(player_class_data)

PLAYER = Player(player_class_data)
PLAYER.Inventory.add_all_items(item_data, 1)
# PLAYER.Inventory.view()
ITEM_1 = PLAYER.Inventory.content_list[PLAYER.Inventory.get_index_list()[13]]
PLAYER.equip_weapon(ITEM_1, -1)
print(PLAYER.loadout)
# Inventory.add_all_items(item_data, 1)
# Inventory.view()


# Main_Menu().main_loop()
# Template_Menu().main_loop()
