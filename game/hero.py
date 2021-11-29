from game.actor import Actor
from game import constants

class Hero(Actor):
    def __init__(self):
        super().__init__()

        self.set_width(constants.HERO_WIDTH)
        self.set_height(constants.HERO_HEIGHT)