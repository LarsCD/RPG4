import logging

from assets.classes.Inventory import Inventory
from assets.classes.Item import Item
from utilities.logger.dev_logger import DevLogger


class Character:
    def __init__(self, data, parent):
        # =========================== GENERAL ===========================
        self.log = DevLogger(Character).log
        self.parent = parent
        # =========================== CLASS INHERITANCE ===========================
        self.Inventory = Inventory(parent)
        # =========================== GENERAL ===========================
        self.character = {
            'tag': data['character']['tag'],
            'name': data['character']['name']
        }
        # LEVEL
        self.level = {
            'current': data['level']['level'],
            'max': data['level']['level_max']
        }
        # =========================== STATS ===========================
        self.stats = {
            'hp': {
                'current': data['stats']['xp_max'],
                'max': data['stats']['xp_max']
            },
            'xp': {
                'current': data['stats']['ep_max'],
                'max': data['stats']['ep_max']
            },
            'ep': {
                'current': data['stats']['ep_max'],
                'max': data['stats']['ep_max']
            },
            'mp': {
                'current': data['stats']['mp_max'],
                'max': data['stats']['mp_max']
            }
        }
        self.multiplier = {
            'hp': data['multiplier']['hp'],
            'xp': data['multiplier']['xp'],
            'ep': data['multiplier']['ep'],
            'mp': data['multiplier']['mp']
        }
        # =========================== ATTRIBUTES ===========================
        self.attributes = {
            'current': {
                'strength': data['attributes']['strength'],
                'speed': data['attributes']['speed'],
                'agility': data['attributes']['agility'],
                'intelligence': data['attributes']['intelligence'],
                'stealth': data['attributes']['stealth'],
                'sorcery': data['attributes']['sorcery']
            },
            'default': {
                'strength': data['attributes']['strength'],
                'speed': data['attributes']['speed'],
                'agility': data['attributes']['agility'],
                'intelligence': data['attributes']['intelligence'],
                'stealth': data['attributes']['stealth'],
                'sorcery': data['attributes']['sorcery']
            }
        }
        # =========================== STATUS EFFECTS ===========================
        self.status_effects = {
            'poisoned': False,
            'stunned': False
        }
        # =========================== LOADOUT ===========================
        self.loadout = {
            'weapon_slot_1': None,
            'weapon_slot_2': None,
            'accessory_slot_1': None,
            'accessory_slot_2': None,
            'accessory_slot_3': None,
            'armor_slot': None,
            'shield_slot': None
        }

    # =========================== LOADOUT FUNCTIONALITY ===========================
    def attack_weapon(self, weapon_slot_index=1):
        loadout_index = self.get_loadout_index_list()[weapon_slot_index-1]
        if self.loadout[loadout_index] is not None:
            #  User has weapon equipped and can now attack.
            current_weapon: Item = self.loadout[loadout_index]
            damage, damage_type_list = current_weapon.use_weapon()
            self.log(logging.INFO, f'\'{self.parent.tag}\' is attacking with \'{current_weapon.tag}\'')
            return damage, damage_type_list

    def get_loadout_index_list(self):
        return_list = []
        for slot_index in self.loadout:
            return_list.append(slot_index)
        return return_list

    def equip_weapon(self, weapon_class: Item, weapon_slot_index):
        if weapon_slot_index < 0 or weapon_slot_index > 1:
            self.log(logging.WARNING, f'can not equip \'{weapon_class.tag}\' to weapon slot > weapon_slot_index: '
                                      f'{weapon_slot_index} ({self.parent.character["tag"]}:{self.parent})')
        else:
            self.loadout[f'weapon_slot_{weapon_slot_index+1}'] = weapon_class
            weapon_class.is_equipped = True
            self.log(logging.INFO, f'equipped \'{weapon_class.tag}\' to weapon slot ({self.parent.character["tag"]}:{self})')

    def un_equip_weapon(self, weapon_class: Item, weapon_slot_index):
        if weapon_slot_index < 0 or weapon_slot_index > 1:
            self.log(logging.WARNING, f'can not unequip \'{weapon_class.tag}\' to weapon slot > weapon_slot_index: '
                                      f'{weapon_slot_index} ({self.parent.character["tag"]}:{self.parent})')
        else:
            self.loadout[f'weapon_slot_{weapon_slot_index + 1}'] = None
            weapon_class.is_equipped = True
            self.log(logging.INFO, f'unequipped \'{weapon_class.tag}\' to weapon slot ({self.parent.character["tag"]}:{self.parent})')

