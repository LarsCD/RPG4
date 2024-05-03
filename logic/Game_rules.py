import logging

from utilities.logger.dev_logger import DevLogger


class Game_rules:
    def __init__(self):
        self.log = DevLogger(Game_rules).log
        self.status_multipliers = {
            'poisoned': {
                'strength': 0.7,
                'speed': 0.8,
                'agility': 0.8
            }
        }
        self.attribute_index = [
            'strength',
            'speed',
            'agility',
            'intelligence',
            'stealth',
            'sorcery'
        ]
