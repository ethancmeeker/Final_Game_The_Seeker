from game.actor import Actor
from game import constants
import pyray

class Trap(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(constants.TRAP_SIZE)
        self.set_height(constants.TRAP_SIZE)
        self.set_image(constants.TRAP_IMAGE)