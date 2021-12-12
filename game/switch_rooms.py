from game import constants
from game.action import Action
from game.point import Point
from game.horizontal_wall import HWall
from game.horizontal_door import HDoor
from game.verticle_door import VDoor
from game.verticle_wall import VWall
from game.locked_door import LockedDoor
from game.room import Rooms

class SwitchRooms(Action):
    def __init__(self):
        super().__init__()
        self._walls = []

    def execute(self, cast):
        rooms = Rooms()
        ["layout"] = [rooms]
        

