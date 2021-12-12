from game.actor import Actor
from game.point import Point
from game import constants

class HWall(Actor):
    def __init__(self):
        super().__init__() 
        self.set_height(constants.WALL_SIZE)
        self.set_width(constants.MAX_X)
