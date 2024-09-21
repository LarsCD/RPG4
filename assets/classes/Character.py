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
                'current': data['stats']['hp_max'],
                'max': data['stats']['hp_max']
            },
            'xp': {
                'current': 0,
                'total': 0,
                'max': data['stats']['xp_max']
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
        # =========================== LOADOUT ===========================
        self.flags = {
            'is_dead': False
        }

    # =========================== LOADOUT FUNCTIONALITY ===========================
    def attack_weapon(self, weapon_slot_index=1):
        if weapon_slot_index < 0 or weapon_slot_index > 1:
            self.log(logging.WARNING,
                     f'can not attack: weapon_slot_index={weapon_slot_index} ({self.parent.character["tag"]}:{self.parent})')
        else:
            loadout_index = self.get_loadout_index_list()[weapon_slot_index]
            if self.loadout[loadout_index] is not None:
                #  User has weapon equipped and can now attack.
                current_weapon: Item = self.loadout[loadout_index]
                damage, damage_type_list = current_weapon.use_weapon()
                if damage is None:
                    self.log(logging.WARNING,
                             f'\'{self.parent.character["tag"]}\' can not attack with \'{current_weapon.tag}\': Item is not a weapon ({self.parent.character["tag"]}:{self.parent})')
                else:
                    self.log(logging.INFO,
                             f'\'{self.parent.character["tag"]}\' is attacking with \'{current_weapon.tag}\' {damage} dmg, ({damage_type_list}) ({self.parent.character["tag"]}:{self.parent})')
                return damage, damage_type_list
            else:
                self.log(logging.WARNING,
                         f'can not attack: weapon_slot_index_{weapon_slot_index + 1} is empty ({self.parent.character["tag"]}:{self.parent})')

    def get_loadout_index_list(self):
        return_list = []
        for slot_index in self.loadout:
            return_list.append(slot_index)
        return return_list

    def equip_weapon(self, weapon_class: Item, weapon_slot_index):
        if weapon_slot_index < 0 or weapon_slot_index > 1:
            self.log(logging.WARNING, f'can not equip \'{weapon_class.tag}\' to weapon slot: weapon_slot_index: '
                                      f'{weapon_slot_index} ({self.parent.character["tag"]}:{self.parent})')
        else:
            self.loadout[f'weapon_slot_{weapon_slot_index + 1}'] = weapon_class
            weapon_class.is_equipped = True
            self.log(logging.INFO,
                     f'equipped \'{weapon_class.tag}\' to weapon slot weapon_slot_index_{weapon_slot_index + 1} ({self.parent.character["tag"]}:{self})')

    def un_equip_weapon(self, weapon_class: Item, weapon_slot_index):
        if weapon_slot_index < 0 or weapon_slot_index > 1:
            self.log(logging.WARNING, f'can not unequip \'{weapon_class.tag}\' from weapon slot: weapon_slot_index: '
                                      f'{weapon_slot_index} ({self.parent.character["tag"]}:{self.parent})')
        else:
            index = f'weapon_slot_{weapon_slot_index + 1}'
            if weapon_class == self.loadout[index]:
                self.loadout[f'weapon_slot_{weapon_slot_index + 1}'] = None
                weapon_class.is_equipped = True
                self.log(logging.INFO,
                         f'unequipped \'{weapon_class.tag}\' from weapon slot ({self.parent.character["tag"]}:{self.parent})')
            else:
                self.log(logging.WARNING, f'can not unequip \'{weapon_class.tag}\' from weapon slot: weapon_slot_index: '
                                          f'{weapon_slot_index} ({self.parent.character["tag"]}:{self.parent})')

    def take_damage(self, damage):
        self.log(logging.INFO,
                 f'\'{self.parent.character["tag"]}\' takes -{damage} dmg ({self.parent.character["tag"]}:{self.parent})')
        self.stats['hp']['current'] -= damage
        if self.stats['hp']['current'] < 0:
            self.die()

    def die(self):
        self.log(logging.INFO,
                 f'\'{self.parent.character["tag"]}\' dies ({self.parent.character["tag"]}:{self.parent})')
        self.stats['hp']['current'] = 0
        self.flags['is_dead'] = True

    def heal(self, health):
        self.log(logging.INFO,
                 f'healing \'{self.parent.character["tag"]}\' +{health} hp ({self.parent.character["tag"]}:{self.parent})')
        self.stats['hp']['current'] += health
        if self.stats['hp']['current'] > self.stats['hp']['max']:
            self.stats['hp']['current'] = self.stats['hp']['max']

    def heal_full(self):
        self.log(logging.INFO,
                 f'fully healing \'{self.parent.character["tag"]}\' ({self.parent.character["tag"]}:{self.parent})')
        self.stats['hp']['current'] = self.stats['hp']['max']

    def give_xp(self, xp):
        self.log(logging.INFO,
                 f'giving \'{self.parent.character["tag"]}\' +{xp} xp ({self.parent.character["tag"]}:{self.parent})')
        self.stats['xp']['current'] += xp
        self.stats['xp']['total'] += xp
        self.check_level_up()

    def level_up(self):
        self.log(logging.INFO,
                 f'\'{self.parent.character["tag"]}\' level up {self.level["current"]} > {self.level["current"] + 1} ({self.parent.character["tag"]}:{self.parent})')
        self.stats['xp']['current'] -= self.stats['xp']['max']
        self.stats['xp']['max'] = round(self.stats['xp']['max'] * self.multiplier['xp'])
        self.level['current'] += 1
        if self.level['current'] > self.level['max']:
            self.level['current'] = self.level['max']
        self.check_level_up()

    def check_level_up(self):
        # Automatically level up if current XP exceeds max XP for the current level
        while self.stats['xp']['current'] >= self.stats['xp']['max']:
            self.stats['xp']['current'] -= self.stats['xp']['max']  # Carry over any extra XP to the next level
            self.level_up()

    def level_up_character(self):
        # Increase the level by 1
        self.set_level(self.level['current'] + 1)

    def set_level(self, level):
        # Set the current level
        self.level['current'] = level

        # Calculate the new max XP needed for the current level
        self.stats['xp']['max'] = self.stats['xp']['max'] * (self.multiplier['xp'] * level)

        # Update the total XP gained
        self.stats['xp']['total'] += self.stats['xp']['current']  # Add current XP to total before resetting current

        # Reset current XP (any excess XP is handled in check_level_up)
        self.stats['xp']['current'] = 0

