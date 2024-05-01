import logging

from assets.classes.Item import Item
from level.menu.classes.View import View
from utilities.logger.dev_logger import DevLogger


class Inventory:
    def __init__(self, parent):
        self.log = DevLogger(Inventory).log

        self.parent = parent
        self.content_list = {}
        self.id = 2  # indicates what kind of object it is, is used for View class, 2 means inventory

    def get_contents(self) -> dict:
        """
        Returns the full data list of the contents of the inventory
        :return: list
        """
        self.update_inventory()
        return self.content_list

    def get_index_list(self) -> list:
        """
        Returns a list of all item keys/tags
        :return: list
        """
        index_list = []
        for item_index in self.content_list:
            index_list.append(item_index)
        return index_list

    def add_all_items(self, item_data, quantity):
        for item_index in item_data:
            self.add_item(item_data[item_index], quantity)
            self.sort_inventory()

    def view(self):
        View(self)

    def update_inventory(self):
        self.remove_empty_items()
        # self.sort_inventory()

    def equip_item(self, item_tag='', item_index=0, equip_slot=0):
        pass

    def add_item(self, item_data, quantity):
        item_exists_in_inventory = item_data["tag"] in self.content_list
        if item_exists_in_inventory:
            item_can_stack = item_data["is_stackable"]
            if not item_can_stack:
                # do not add, items exists but not stackable
                self.log(logging.WARNING, f'could not add item \'{item_data["tag"]}\' ({self.parent}:{self}): cannot stack item')
                return
            else:
                # add, items exists and stackable
                self.log(logging.INFO, f'adding item \'{item_data["tag"]}\' x{quantity} ({self.parent}:{self})')
                self.content_list[item_data["tag"]].add_quantity(quantity)
        else:
            item_can_stack = item_data["is_stackable"]
            if not item_can_stack:
                # add only one new, is not stackable
                self.log(logging.INFO, f'adding item \'{item_data["tag"]}\' x{quantity} ({self.parent}:{self})')
                self.content_list[item_data["tag"]] = Item(item_data, self.parent)
                self.content_list[item_data["tag"]].set_quantity(quantity)
            else:
                # add new
                self.log(logging.INFO, f'adding item \'{item_data["tag"]}\' x{quantity} ({self.parent}:{self})')
                self.content_list[item_data["tag"]] = Item(item_data, self.parent)
                self.content_list[item_data["tag"]].set_quantity(quantity)
        self.update_inventory()

    def remove_item(self, item_data, quantity):
        self.update_inventory()
        item_exists_in_inventory = item_data["tag"] in self.content_list
        if not item_exists_in_inventory:
            self.log(logging.WARNING, f'could not remove item \'{item_data["tag"]}\' ({self.parent}:{self}): item not in inventory')
            return
        else:
            if quantity > self.content_list[item_data["tag"]].quantity:
                self.log(logging.WARNING, f'could not remove item \'{item_data["tag"]}\' ({self.parent}:{self}): only x{self.content_list[item_data["tag"]].quantity} in inventory (want to remove x{quantity})')
                return
            else:
                self.log(logging.INFO, f'removing item \'{item_data["tag"]}\' x{quantity} ({self.parent}:{self})')
                self.content_list[item_data["tag"]].remove_quantity(quantity)

    def add_item_as_list(self, list_with_items, quantity_list=None):
        self.update_inventory()
        self.log(logging.INFO, f'adding items in list ({self.parent}:{self})')
        if quantity_list is None:
            quantity_list = []
            for _ in list_with_items:
                quantity_list.append(1)
        for i, item in enumerate(list_with_items):
            self.add_item(item, quantity_list[i])

    def remove_item_as_list(self, list_with_items, quantity_list=None):
        self.update_inventory()
        self.log(logging.INFO, f'removing items in list ({self.parent}:{self})')
        if quantity_list is None:
            quantity_list = []
            for _ in list_with_items:
                quantity_list.append(1)
        for i, item in enumerate(list_with_items):
            self.remove_item(item, quantity_list[i])

    def remove_empty_items(self):
        remove_items_list = []
        for item in self.content_list:
            item_class = self.content_list[item]
            if item_class.quantity == 0:
                remove_items_list.append(item)
        for removal_item in remove_items_list:
            self.content_list.pop(removal_item)

    def sort_inventory(self):
        # TODO: Hmmmmmmmmmm yummy shit code that doesnt work, fix please! :D
        # Convert the dictionary to a list of (key, value) tuples for sorting
        content_list_items = list(self.content_list.items())

        # Sort the list first by 'type' and then by 'tier'
        for _ in self.content_list:
            content_list_items = list(self.content_list.items())
            sorted_content_list = sorted(
                content_list_items,
                key=lambda item: (item[1].type, item[1].tier)
            )

            self.content_list = dict(sorted_content_list)

        # Convert the sorted list back into a dictionary
