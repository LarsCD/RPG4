import logging

from utilities.GUT_2 import Color
from utilities.logger.dev_logger import DevLogger


class Item:
    def __init__(self, item_data):
        self.log = DevLogger(Item).log

        self.Tier = Tier()
        self.Clr = Color()

        # indexing info
        self.tag = item_data['tag']
        self.name = item_data['name']
        self.type = item_data['type']
        self.description = item_data['description']

        # general items data
        self.value = item_data['value']
        self.quantity = 1

        # specifics items data
        self.specifics = item_data['specifics']  # specifics data that's different per items like damage, health etc.

        # tier items data
        self.tier = item_data['tier']
        self.tier_tag = self.Tier.get_tier_tag(self.tier)
        self.tier_name = self.Tier.get_tier_name(self.tier)
        self.tier_hex_color = self.Clr.rgb_to_hex(*self.Tier.get_tier_hex_color(self.tier))
        self.id = 0  # don't know what to do with this

        # default flags
        self.is_stackable = item_data['is_stackable']
        self.is_equipped = False

    def check_for_stackable(self):
        if not self.is_stackable:
            if self.quantity > 1:
                self.log(logging.WARNING, f'\'{self.tag}\' ({self}) is not stackable, setting quantity to 1')
                self.quantity = 1

    def add_quantity(self, quantity):
        self.quantity += quantity
        self.check_for_stackable()

    def remove_quantity(self, quantity):
        self.quantity -= quantity
        if self.quantity < 0:
            self.quantity = 0
        self.check_for_stackable()

    def set_quantity(self, quantity):
        self.quantity = quantity
        self.check_for_stackable()


class Tier:
    def __init__(self):
        self.tier_tag_index = {
            1: 'common',
            2: 'uncommon',
            3: 'rare',
            4: 'super_rare',
            5: 'ultra_rare',
            6: 'legendary'
        }
        self.tier_name_index = {
            1: 'Common',
            2: 'Uncommon',
            3: 'Rare',
            4: 'Super Rare',
            5: 'Exotic',
            6: 'Legendary'
        }
        self.tier_rgb_color = {
            1: (166, 166, 166),
            2: (143, 222, 93),
            3: (77, 166, 255),
            4: (171, 0, 255),
            5: (188, 0, 0),
            6: (255, 187, 0)
        }

    def get_tier_tag(self, tier_nr):
        return self.tier_tag_index[tier_nr]

    def get_tier_name(self, tier_nr):
        return self.tier_name_index[tier_nr]

    def get_tier_hex_color(self, tier_nr):
        return self.rgb_to_hex(*self.tier_rgb_color[tier_nr])

    @staticmethod
    def rgb_to_hex(r, g, b):
        """
        Convert RGB color values to hexadecimal color representation.

        Args:
            r (int): Red value (0-255).
            g (int): Green value (0-255).
            b (int): Blue value (0-255).

        Returns:
            str: Hexadecimal color representation.
        """
        return "#{:02x}{:02x}{:02x}".format(r, g, b)
