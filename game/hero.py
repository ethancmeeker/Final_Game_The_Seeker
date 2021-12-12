from game.actor import Actor
from game import constants
import pyray

class Hero(Actor):
    def __init__(self):
        super().__init__()
        self._new_room = False
        self.set_width(constants.HERO_WIDTH)
        self.set_height(constants.HERO_HEIGHT)
        self.set_image(constants.HERO_IMAGE)
