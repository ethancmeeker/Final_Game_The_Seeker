from game.actor import Actor
from game.point import Point
from game import constants

class VWall(Actor):
    def __init__(self):
        super().__init__() 
        self.set_width(constants.WALL_SIZE)
        self.set_height(constants.MAX_Y)
