import logging

from utilities.logger.dev_logger import DevLogger


class Game_rules:
    def __init__(self):
        self.log = DevLogger(Game_rules).log
        self.status_multipliers = {
            'poisoned': {
                'strength': 0.75,
                'defense': 0.8,
                'speed': 0.9,
                'agility': 0.6,
            }
        }
        self.attribute_index = [
            'strength',
            'defense',
            'speed',
            'agility',
            'intelligence',
            'stealth',
            'sorcery'
        ]
