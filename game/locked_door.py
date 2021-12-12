from game.actor import Actor
from game.point import Point
from game import constants

class LockedDoor(Actor):
    def __init__(self):
        super().__init__() 
        self.set_height(40)
        self.set_width(constants.MAX_X)
        self.set_position(Point(0, constants.MAX_Y - 40))
        self.set_image(constants.LOCKED_DOOR_IMAGE)
