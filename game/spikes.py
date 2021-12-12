from game.actor import Actor
from game import constants
import pyray

class Spikes(Actor):
    def __init__(self):
        super().__init__()
        self.set_width(constants.SPIKE_SIZE)
        self.set_height(constants.SPIKE_SIZE)
        self.set_image(constants.SPIKE_IMAGE)