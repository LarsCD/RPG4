import sys
from data.config.config_settings import GAME_SETTINGS


class GameWindowTools:
    def __init__(self):
        pass

    def run_setup(self):
        self.set_window_resolution()

    @staticmethod
    def set_window_resolution():
        cols, rows = GAME_SETTINGS['game_resolution']
        sys.stdout.write(f"\x1b[8;{rows};{cols}t")
