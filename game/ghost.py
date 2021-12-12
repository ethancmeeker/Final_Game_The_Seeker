from game.actor import Actor
from game import constants
import pyray

class Ghost(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(constants.GHOST_WIDTH)
        self.set_height(constants.GHOST_HEIGHT)
        self.set_image(constants.GHOST_IMAGE)
