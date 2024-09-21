from assets.classes.Character import Character
from level.menu.classes.View import View


class Player(Character):
    def __init__(self, data):
        Character.__init__(self, data, self)
        # CLASS
        self.class_data = {
            'class_tag': data['class_info']['class_tag'],
            'class_name': data['class_info']['class_name']
        }
        self.id = 3

    def view(self):
        View(self)



