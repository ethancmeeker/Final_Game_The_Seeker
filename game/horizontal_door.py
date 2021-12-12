from game.actor import Actor
from game.point import Point
from game import constants

class HDoor(Actor):
    def __init__(self):
        super().__init__() 
        self.set_height(constants.WALL_SIZE)
        self.set_width(int(constants.MAX_X / 3))
