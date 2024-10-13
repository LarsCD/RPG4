from assets.classes.Character import Character
from level.menu.classes.View import View


class Enemy(Character):
    def __init__(self, data):
        Character.__init__(self, data, self)
        # CLASS
        self.class_data = {
            'class_tag': data['class_info']['class_tag'],
            'class_name': data['class_info']['class_name']
        }
        self.id = 5  # used for View.py functions

    def view_enemy_stats(self):
        View(self)
