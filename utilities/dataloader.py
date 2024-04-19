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
            'item_dir': DATALOADER_SETTINGS['item_dir_path']
        }
        self.log(logging.INFO, '[online]')

    def load_item_data(self):
        data_list = []
        self.log(logging.INFO, 'loading items data')
        full_path = f"{self.cwd}{self.item_dir_path['item_dir']}"

        for filename in os.listdir(full_path):
            if filename.endswith(".json"):
                file_path = os.path.join(full_path, filename)
                with open(file_path, "r") as file:
                    loaded_data = json.load(file)
                    data_list.append(loaded_data)
        return data_list


if __name__ == '__main__':
    data = Dataloader().load_item_data()
    print(data)
