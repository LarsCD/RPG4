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


GameWindowTools().run_setup()
Template_Menu().main_loop()
# Main_Menu().main_loop()
