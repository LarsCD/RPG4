import random
from data.config.gameplay_config_settings import GAMEPLAY_SETTINGS


class Calculations:
    def __init__(self):
        pass

    @staticmethod
    def damage(player_level, weapon_power, strength, target_armor, critical):
        random_value = random.uniform(*GAMEPLAY_SETTINGS['damage_calculation_variance_values'])
        damage = (((((2 * player_level) / 5) + 2) * weapon_power * (
                (strength * 10) / target_armor / 10) / 50) * critical + 2) * random_value
        return damage

    @staticmethod
    def XP(enemy_level, player_level, enemy_difficulty, game_difficulty):
        xp_value = ((enemy_level / player_level) / (game_difficulty * 3.5)) * enemy_difficulty * 1100
        return xp_value
