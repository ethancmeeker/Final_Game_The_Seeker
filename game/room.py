from game import constants
from game.actor import Actor
from game.point import Point
from game.horizontal_wall import HWall
from game.horizontal_door import HDoor
from game.verticle_door import VDoor
from game.verticle_wall import VWall
from game.locked_door import LockedDoor

class Rooms(Actor): 
    def __init__(self):
        super().__init__()  
        self._roomnumber = 0
        self._leftwall = 0
        self._rightwall = 0
        self._topwall = 0
        self._bottemwall = 0
        """
        With these numbers, 1 means a normal wall, 2 means a door, 3 means a locked door
        """
    def get_roomnumber(self):
        return self._roomnumber
    def set_roomnumber(self, roomnumber):
        self._roomnumber = roomnumber
    def get_topwall(self):
        return self._topwall
    def set_topwall(self, topwall):
        self._topwall = topwall
    def get_bottemwall(self):
        return self._bottemwall
    def set_bottemwall(self, bottemwall):
        self._bottemwall = bottemwall
    def get_leftwall(self):
        return self._leftwall
    def set_leftwall(self, leftwall):
        self._leftwall = leftwall
    def get_rightwall(self):
        return self._rightwall
    def set_rightwall(self, rightwall):
        self._rightwall = rightwall
    def layout(self):
        if self._leftwall == 1:
            wall_left = VWall()
            wall_left.set_position(Point(0, 0))
        if self._leftwall == 2:
            door_b_left = VDoor()
            door_t_left = VDoor()
            door_b_left.set_position(Point(0, int(constants.MAX_Y / 3 * 2)))
            door_t_left.set_position(Point(0, 0))
        if self._rightwall == 1:
            wall_right = VWall()
            wall_right.set_position(Point(constants.MAX_X - 40, 0))
        if self._rightwall == 2:
            door_b_right = VDoor()
            door_t_right = VDoor()
            door_b_right.set_position(Point(constants.MAX_X - 40, int(constants.MAX_Y / 3 * 2)))
            door_t_right.set_position(Point(constants.MAX_X - 40, 0))
        if self._topwall == 1:
            wall_top = HWall()
            wall_top.set_position(Point(0, 0))
        if self._topwall == 2:
            door_b_top = HDoor()
            door_t_top = HDoor()
            door_b_top.set_position(Point(0, 0))
            door_t_top.set_position(Point(int(constants.MAX_X / 3 * 2), 0))
        if self._bottemwall == 1:
            wall_bottem = HWall()
            wall_bottem.set_position(Point(0, constants.MAX_Y - 40))
        if self._bottemwall == 2:
            door_b_bottem = HDoor()
            door_t_bottem = HDoor()
            door_b_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_t_bottem.set_position(Point(int(constants.MAX_X / 3 * 2), constants.MAX_Y - 40))
        if self._bottemwall == 3:
            door_b_bottem = HDoor()
            door_t_bottem = HDoor()
            door_locked = LockedDoor()
            door_b_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_t_bottem.set_position(Point(int(constants.MAX_X / 3 * 2), constants.MAX_Y - 40))
            door_locked.set_position(Point(0, constants.MAX_Y - 20))

