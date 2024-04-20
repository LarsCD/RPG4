import logging

from assets.classes.Item import Item
from utilities.logger.dev_logger import DevLogger


class Inventory:
    def __init__(self, parent):
        self.log = DevLogger(Inventory).log

        self.parent = parent
        self.content_list = {}

    def add_item(self, item_data, quantity):
        item_exists_in_inventory = item_data["tag"] in self.content_list
        if item_exists_in_inventory:
            item_can_stack = item_data["is_stackable"]
            if not item_can_stack:
                # do not add, items exists but not stackable
                self.log(logging.WARNING, f'could not add item \'{item_data["tag"]}\' to {self.parent}: cannot stack item')
                return
            else:
                # add, items exists and stackable
                self.log(logging.INFO, f'adding item \'{item_data["tag"]}\' x{quantity} to {self.parent}')
                self.content_list[item_data["tag"]] = self.content_list[item_data["tag"]].add_quantity(quantity)
        else:
            item_can_stack = item_data["is_stackable"]
            if not item_can_stack:
                # add only one new, is not stackable
                self.log(logging.INFO, f'adding item \'{item_data["tag"]}\' x{quantity} to {self.parent}')
                self.content_list[item_data["tag"]] = Item(item_data)
                self.content_list[item_data["tag"]].set_quantity(quantity)
            else:
                # add new
                self.log(logging.INFO, f'adding item \'{item_data["tag"]}\' x{quantity} to {self.parent}')
                self.content_list[item_data["tag"]] = Item(item_data)
                self.content_list[item_data["tag"]].set_quantity(quantity)

    def remove_item(self, item_data, quantity):
        item_exists_in_inventory = item_data["tag"] in self.content_list
        if not item_exists_in_inventory:
            self.log(logging.WARNING, f'could not remove item \'{item_data["tag"]}\' from {self.parent}: item not in inventory')
            return
        else:
            if quantity > self.content_list[item_data["tag"]].quantity:
                self.log(logging.WARNING, f'could not remove item \'{item_data["tag"]}\' from {self.parent}: only x{self.content_list[item_data["tag"]].quantity} in inventory (want to remove x{quantity})')
                return
            else:
                self.log(logging.INFO, f'removing item \'{item_data["tag"]}\' x{quantity} to {self.parent}')
                self.content_list[item_data["tag"]].remove_quantity(quantity)

    def add_item_as_list(self, list_with_items, quantity_list=None):
        self.log(logging.INFO, f'adding items in list to {self}')
        if quantity_list is None:
            quantity_list = []
            for _ in list_with_items:
                quantity_list.append(1)
        for i, item in enumerate(list_with_items):
            self.add_item(item, quantity_list[i])

    def remove_item_as_list(self, list_with_items, quantity_list=None):
        self.log(logging.INFO, f'removing items in list to {self}')
        if quantity_list is None:
            quantity_list = []
            for _ in list_with_items:
                quantity_list.append(1)
        for i, item in enumerate(list_with_items):
            self.remove_item(item, quantity_list[i])

    def sort_inventory(self):
        # TODO: change so that this works for this inventory system
        # sets order of items from low to high tier (with fuckin magic...)
        for category in self.inventory:
            new_categorized_inventory = sorted(self.inventory[category], key=lambda x: x.tier, reverse=False)
            self.inventory[category] = new_categorized_inventory
