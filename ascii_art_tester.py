import time

from utilities.GUT_2 import GUT
from assets.art.animations.slash_1 import frames as animation_slash_1


class ascii_animator:
    def __init__(self):
        self.Gut = GUT()
        self.animation_speed = 0.08

    def animate(self, animation_list, loop=15):
        for _ in range(loop):
            for frame in animation_list:
                self.Gut.clear_screen()
                print(frame)
                time.sleep(self.animation_speed)


# ascii_animator().animate(animation_slash_1)
