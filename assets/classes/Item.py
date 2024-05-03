import logging

# from level.menu.view_item import View_Item
from utilities.GUT_2 import Color
from utilities.logger.dev_logger import DevLogger
from level.menu.classes.View import View


class Item:
    def __init__(self, item_data, parent):
        self.log = DevLogger(Item).log

        self.Tier = Tier()
        self.Clr = Color()

        self.parent = parent

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
        self.tier_hex_color = self.Tier.get_tier_hex_color(self.tier)
        self.id = 1  # indicates what kind of object it is, is used for View class, 1 means item

        # default flags
        self.is_stackable = item_data['is_stackable']
        self.is_equipped = False
        self.options = item_data['options']
        self.item_view_options = item_data['item_view_options']

    def use_consumable(self):
        self.log(logging.INFO, f'consuming \'{self.tag}\' ({self.parent})')
        if 'use_consumable' in self.options:
            self.remove_quantity(1)
            return self.specifics['health']

    def use_weapon(self):
        """
        Returns attack damage and removes durability from the users weapon
        :return: attack value
        """
        self.log(logging.INFO, f'using weapon \'{self.tag}\' ({self.parent})')
        if 'use_weapon' in self.options:
            self.remove_durability()
            return None
        else:
            return self.specifics['damage'], self.specifics

    def remove_durability(self):
        self.log(logging.INFO, f'removing durability \'{self.tag}\' ({self.parent})')
        if 'remove_durability' in self.options:
            self.specifics['durability'] -= 1
            if self.specifics['durability'] <= 0:
                self.destroy()  # Removes item if item has no durability left

    def sell(self):
        self.log(logging.INFO, f'selling item \'{self.tag}\' ({self.parent})')
        if 'sell' in self.options:
            # sell the item
            pass

    def view(self):
        View(self)

    def update_quantity(self):
        if not self.is_stackable:
            if self.quantity > 1:
                self.log(logging.WARNING, f'\'{self.tag}\' ({self}) is not stackable, setting quantity to 1')
                self.quantity = 1
        if self.quantity < 0:
            self.quantity = 0
        if self.quantity == 0:
            self.destroy()

    def add_quantity(self, quantity):
        self.quantity += quantity
        self.update_quantity()

    def remove_quantity(self, quantity):
        self.quantity -= quantity
        self.update_quantity()

    def set_quantity(self, quantity):
        self.quantity = quantity
        self.update_quantity()

    def destroy(self):
        self.log(logging.INFO, f'DESTROYING \'{self.tag}\' ({self})')
        del self


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
