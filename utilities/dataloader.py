import logging
import os
from os.path import dirname, abspath
import json

from data.config.config_settings import DATALOADER_SETTINGS
from utilities.logger.dev_logger import DevLogger


class Dataloader:
    def __init__(self):
        self.log = DevLogger(Dataloader).log

        self.cwd = dirname(dirname(abspath(__file__)))
        self.item_dir_path = {
            'item_dir': DATALOADER_SETTINGS['item_dir_path'],
            'player_class_dir': DATALOADER_SETTINGS['player_class_dir_path'],
            'enemy_class_dir': DATALOADER_SETTINGS['enemy_class_dir_path']
        }

    def load_item_data(self):
        data_list = []
        self.log(logging.INFO, 'loading items data')
        full_path = f"{self.cwd}{self.item_dir_path['item_dir']}"

        for filename in os.listdir(full_path):
            if filename.endswith(".json"):
                file_path = os.path.join(full_path, filename)
                self.log(logging.INFO, f'loading \'{filename}\'')
                with open(file_path, "r") as file:
                    loaded_data = json.load(file)
                    data_list.append(loaded_data)
        return data_list[0]

    def load_player_class_data(self):
        data_list = []
        self.log(logging.INFO, 'loading player_class data')
        full_path = f"{self.cwd}{self.item_dir_path['player_class_dir']}"

        for filename in os.listdir(full_path):
            if filename.endswith(".json"):
                file_path = os.path.join(full_path, filename)
                self.log(logging.INFO, f'loading \'{filename}\'')
                with open(file_path, "r") as file:
                    loaded_data = json.load(file)
                    data_list.append(loaded_data)
        return data_list[0]

    def load_enemy_class_data(self):
        data_list = []
        self.log(logging.INFO, 'loading enemy_class data')
        full_path = f"{self.cwd}{self.item_dir_path['enemy_class_dir']}"

        for filename in os.listdir(full_path):
            if filename.endswith(".json"):
                file_path = os.path.join(full_path, filename)
                self.log(logging.INFO, f'loading \'{filename}\'')
                with open(file_path, "r") as file:
                    loaded_data = json.load(file)
                    data_list.append(loaded_data)
        return data_list[0]


if __name__ == '__main__':
    data = Dataloader().load_item_data()
    print(data)
