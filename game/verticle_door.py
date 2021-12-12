from game.actor import Actor
from game.point import Point
from game import constants

class VDoor(Actor):
    def __init__(self):
        super().__init__() 
        self.set_width(constants.WALL_SIZE)
        self.set_height(int(constants.MAX_Y / 3))
