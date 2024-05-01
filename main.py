"""
###############################################################
RPG4 (Working Title)
By: LarsCD(2002)

File: Main file to run tests


###############################################################
"""
from level.menu.main_menu_test import Main_Menu
from utilities.game_window_tools import GameWindowTools
from utilities.dataloader import Dataloader
from assets.classes.Inventory import Inventory
from assets.classes.Character import Character

GameWindowTools().run_setup()

Inventory = Inventory('Player')
item_data = Dataloader().load_item_data()

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

print(item_data)

Inventory.add_all_items(item_data, 1)
Inventory.view()



# Main_Menu().main_loop()
# Template_Menu().main_loop()
