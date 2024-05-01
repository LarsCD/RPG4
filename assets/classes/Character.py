from assets.classes.Inventory import Inventory
from assets.classes.Item import Item


class Character(Inventory):
    def __init__(self, data, parent):
        # =========================== CLASS INHERITANCE ===========================
        self.Inventory = super().__init__(parent)
        # =========================== GENERAL ===========================
        self.tag = data['tag']
        self.name = data['name']
        # CLASS
        self.class_tag = data['class_info']['class_tag']
        self.class_name = data['class_info']['class_name']
        # LEVEL
        self.level = {
            'current': 1,
            'max': data['level_max']
        }
        # =========================== STATS ===========================
        self.hp = {
            'current': data['hp_max'],
            'max': data['hp_max']
        }
        self.xp = {
            'current': data['xp_max'],
            'multiplier': data['xp_multiplier']
        }
        self.ep = {
            'current': data['ep_max'],
            'max': data['ep_max']
        }
        self.mp = {
            'current': data['mp_max'],
            'max': data['mp_max']
        }
        self.multiplier = {
            'hp': data['multiplier']['hp'],
            'ep': data['multiplier']['ep'],
            'mp': data['multiplier']['mp']
        }
        # =========================== ATTRIBUTES ===========================
        self.attributes = {
            'current': {
                'strength': data['strength'],
                'speed': data['speed'],
                'agility': data['agility'],
                'intelligence': data['intelligence'],
                'stealth': data['stealth'],
                'sorcery': data['sorcery']
            },
            'default': {
                'strength': data['strength'],
                'speed': data['speed'],
                'agility': data['agility'],
                'intelligence': data['intelligence'],
                'stealth': data['stealth'],
                'sorcery': data['sorcery']
            }
        }
        # =========================== STATUS EFFECTS ===========================
        self.status_effects = {
            'poisoned': False,
            'stunned': False
        }
        self.status_multipliers = {
            'poisoned': {
                'strength': 0.7,
                'speed': 0.8,
                'agility': 0.8
            }
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
            damage = current_weapon.use_weapon()

    def get_loadout_index_list(self):
        return_list = []
        for slot_index in self.loadout:
            return_list.append(slot_index)
        return return_list


