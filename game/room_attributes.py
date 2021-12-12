from game import constants, physics_service
from game.action import Action
from game.point import Point
from game.room import Rooms
from game.audio_service import AudioService
from game.actor import Actor
from game.point import Point
from game.ghost import Ghost
from game.horizontal_wall import HWall
from game.horizontal_door import HDoor
from game.verticle_door import VDoor
from game.verticle_wall import VWall
from game.locked_door import LockedDoor
from game.box import Box
from game.trap import Trap
from game.spikes import Spikes
import sys
import time
import random

class RoomAttributes(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._roomnumber = 2
        self._key_location = random.randint(1, 8)
        self._key = False
        self._physics_service = physics_service

    def set_key(self, key):
        self._key == key
    def get_key(self):
        return self._key
    def get_roomnumber(self):
        return self._roomnumber
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        hero = cast["hero"][0]
        room = Rooms()
        location = hero.get_position()
        hero_location_x = location.get_x()
        hero_location_y = location.get_y()

        '''
        This is what I did to make my code my unique. The game would play out exactly
        the same if I didn't do this every single time (unless you lost). This changes
        the direction it bounces off the paddle making things different.'''
        #Room 1
        ghost = Ghost()
        trap = Trap()
        box1 = Box()
        box2 = Box()
        if (hero_location_x <= 5 and self._roomnumber == 2) or (hero_location_y >= constants.MAX_Y - 65 and self._roomnumber == 4):
            if self._roomnumber == 2:
                hero.set_position(Point(constants.MAX_X - 80, int(constants.MAX_Y / 2)))
            elif self._roomnumber == 4:
                hero.set_position(Point(int(constants.MAX_X / 2), 40))
            walls = []
            boxes = []
            spikes = []
            locked_door = []
            self._roomnumber = 1
            ghost.set_position(Point(900, 900))
            ghost.set_velocity(Point(0, 0))
            box1.set_position(Point(100, 120))
            box2.set_position(Point(900, 900))
            if self._key_location == 1:
                box1.set_description('KEY FOUND')
            lockeddoor = LockedDoor()
            lockeddoor.set_position(Point(900, 900))
            wall_left = VWall()
            wall_left.set_position(Point(0, 0))
            door_b_right = VDoor()
            door_t_right = VDoor()
            door_b_right.set_position(Point(constants.MAX_X - 40, int(constants.MAX_Y / 3 * 2)))
            door_t_right.set_position(Point(constants.MAX_X - 40, 0))
            wall_bottem = HWall()
            wall_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_b_top = HDoor()
            door_t_top = HDoor()
            door_b_top.set_position(Point(0, 0))
            door_t_top.set_position(Point(int(constants.MAX_X / 3 * 2), 0)) 
            locked_door.append(lockeddoor)
            walls.append(door_b_top)  
            walls.append(door_t_top) 
            walls.append(door_t_right)  
            walls.append(door_b_right)
            walls.append(wall_left)
            walls.append(wall_bottem) 
            boxes.append(box1)
            boxes.append(box2)
            cast["walls"] = walls
            cast["spikes"] = spikes
            cast["locked_door"] = locked_door
            cast["boxes"] = boxes
            cast["ghost"] = [ghost]
            cast["trap"] = [trap]
        #Room 2
        if (hero_location_x >= constants.MAX_X - 45 and self._roomnumber == 1) or (hero_location_x <= 5 and self._roomnumber == 3) or (hero_location_y >= constants.MAX_Y - 45 and self._roomnumber == 5):
            if self._roomnumber == 1:
                hero.set_position(Point(40, int(constants.MAX_Y / 2)))
            elif self._roomnumber == 3: 
                hero.set_position(Point(constants.MAX_X - 80, int(constants.MAX_Y / 2)))
            elif self._roomnumber == 5:
                hero.set_position(Point(int(constants.MAX_X / 2), 40))
            self._roomnumber = 2
            marquee = cast["marquee"][0]
            phrase = marquee.get_text()                
            walls = []
            spikes = []
            boxes = []
            locked_door = []
            ghost.set_position(Point(900, 900))
            ghost.set_velocity(Point(0, 0))
            door_b_bottem = HDoor()
            door_t_bottem = HDoor()
            lockeddoor = LockedDoor()
            if phrase == 'KEY FOUND':
                lockeddoor.set_position(Point(900, 900))
            door_b_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_t_bottem.set_position(Point(int(constants.MAX_X / 3 * 2), constants.MAX_Y - 40))
            door_b_top = HDoor()
            door_t_top = HDoor()
            door_b_top.set_position(Point(0, 0))
            door_t_top.set_position(Point(int(constants.MAX_X / 3 * 2), 0))
            door_b_right = VDoor()
            door_t_right = VDoor()
            door_b_right.set_position(Point(constants.MAX_X - 40, int(constants.MAX_Y / 3 * 2)))
            door_t_right.set_position(Point(constants.MAX_X - 40, 0)) 
            door_b_left = VDoor()
            door_t_left = VDoor()
            door_b_left.set_position(Point(0, int(constants.MAX_Y / 3 * 2)))
            door_t_left.set_position(Point(0, 0))
            locked_door.append(lockeddoor)
            walls.append(door_b_left) 
            walls.append(door_t_left)
            walls.append(door_b_right)
            walls.append(door_t_right)
            walls.append(door_b_top)
            walls.append(door_t_top)
            walls.append(door_b_bottem)
            walls.append(door_t_bottem)
            boxes.append(box1)
            boxes.append(box2)
            locked_door.append(lockeddoor)
            cast["walls"] = walls
            cast["locked_door"] = locked_door
            cast["trap"] = [trap]
            cast["ghost"] = [ghost]
            cast["boxes"] = boxes
            cast["spikes"] = spikes
        #Room 3
        if (hero_location_x >= constants.MAX_X - 35 and self._roomnumber == 2) or (hero_location_y >= constants.MAX_Y - 40 and self._roomnumber == 6):
            if self._roomnumber == 2:
                hero.set_position(Point(40, int(constants.MAX_Y / 2)))
            elif self._roomnumber == 6:
                hero.set_position(Point(int(constants.MAX_X / 2), 45))
            walls = []
            boxes = []
            locked_door = []
            spikes = []
            self._roomnumber = 3
            ghost.set_position(Point(900, 900))
            ghost.set_velocity(Point(0, 0))
            trap.set_position(Point(120, int(constants.MAX_Y / 2)))
            box1.set_position(Point(300, 300))
            if self._key_location == 2:
                box1.set_description('KEY FOUND')
            lockeddoor = LockedDoor()
            lockeddoor.set_position(Point(900, 900))
            wall_bottem = HWall()
            wall_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_b_top = HDoor()
            door_t_top = HDoor()
            door_b_top.set_position(Point(0, 0))
            door_t_top.set_position(Point(int(constants.MAX_X / 3 * 2), 0))
            wall_right = VWall()
            wall_right.set_position(Point(constants.MAX_X - 40, 0)) 
            door_b_left = VDoor()
            door_t_left = VDoor()
            door_b_left.set_position(Point(0, int(constants.MAX_Y / 3 * 2)))
            door_t_left.set_position(Point(0, 0))
            locked_door.append(lockeddoor)
            walls.append(door_b_left) 
            walls.append(door_t_left)
            walls.append(wall_right)
            walls.append(door_b_top)
            walls.append(door_t_top)
            walls.append(wall_bottem)
            boxes.append(box1)
            boxes.append(box2)
            cast["trap"] = [trap]
            cast["ghost"] = [ghost]
            cast["walls"] = walls
            cast["boxes"] = boxes
            cast["locked_door"] = locked_door
        #Room 4
        if (hero_location_x <= 5 and self._roomnumber == 5) or (hero_location_y <= 20 and self._roomnumber == 1) or (hero_location_y >= constants.MAX_Y - 45 and self._roomnumber == 7):
            if self._roomnumber == 7:
                hero.set_position(Point(int(constants.MAX_X / 2), 45))
            elif self._roomnumber == 1:
                hero.set_position(Point(int(constants.MAX_X / 2), constants.MAX_Y - 85))
            elif self._roomnumber == 5:
                hero.set_position(Point(constants.MAX_X - 80, int(constants.MAX_Y / 2)))
            walls = []
            locked_door = []
            boxes = []
            spikes = []
            self._roomnumber = 4
            ghost.set_position(Point(900, 900))
            ghost.set_velocity(Point(0, 0))
            trap.set_position(Point(450, 200))
            box1.set_position(Point(460, 110))
            if self._key_location == 3:
                box1.set_description('KEY FOUND')
            lockeddoor = LockedDoor()
            lockeddoor.set_position(Point(900, 900))
            wall_left = VWall()
            wall_left.set_position(Point(0, 0))
            door_b_right = VDoor()
            door_t_right = VDoor()
            door_b_right.set_position(Point(constants.MAX_X - 40, int(constants.MAX_Y / 3 * 2)))
            door_t_right.set_position(Point(constants.MAX_X - 40, 0))
            door_b_bottem = HDoor()
            door_t_bottem = HDoor()
            door_b_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_t_bottem.set_position(Point(int(constants.MAX_X / 3 * 2), constants.MAX_Y - 40))
            door_b_top = HDoor()
            door_t_top = HDoor()
            door_b_top.set_position(Point(0, 0))
            door_t_top.set_position(Point(int(constants.MAX_X / 3 * 2), 0))   
            locked_door.append(lockeddoor)
            walls.append(door_b_top)  
            walls.append(door_t_top) 
            walls.append(door_t_right)  
            walls.append(door_b_right)
            walls.append(wall_left)
            walls.append(door_b_bottem)
            walls.append(door_t_bottem) 
            boxes.append(box1)
            boxes.append(box2)
            cast["walls"] = walls
            cast["ghost"] = [ghost]
            cast["boxes"] = boxes
            cast["trap"] = [trap]
            cast["spikes"] = spikes
        #Room 5
        if (hero_location_x >= constants.MAX_X - 75 and self._roomnumber == 4) or (hero_location_x <= 5 and self._roomnumber == 6) or (hero_location_y <= 20 and self._roomnumber == 2) or (hero_location_y >= constants.MAX_Y - 20 and self._roomnumber == 8):
            if self._roomnumber == 4:
                hero.set_position(Point(40, int(constants.MAX_Y / 2)))
            elif self._roomnumber == 6: 
                hero.set_position(Point(constants.MAX_X - 80, int(constants.MAX_Y / 2)))
            elif self._roomnumber == 8:
                hero.set_position(Point(int(constants.MAX_X / 2), 40))
            elif self._roomnumber == 2:
                hero.set_position(Point(int(constants.MAX_X / 2), constants.MAX_Y - 80))
            self._roomnumber = 5
            walls = []
            spikes = []
            locked_door = []
            boxes = []
            locked_door = []
            ghost.set_position(Point(int(constants.MAX_X / 3), int(constants.MAX_Y / 2)))
            ghost.set_velocity(Point(25, 25))
            lockeddoor = LockedDoor()
            lockeddoor.set_position(Point(900, 900))
            door_b_bottem = HDoor()
            door_t_bottem = HDoor()
            door_b_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_t_bottem.set_position(Point(int(constants.MAX_X / 3 * 2), constants.MAX_Y - 40))
            door_b_top = HDoor()
            door_t_top = HDoor()
            door_b_top.set_position(Point(0, 0))
            door_t_top.set_position(Point(int(constants.MAX_X / 3 * 2), 0))
            door_b_right = VDoor()
            door_t_right = VDoor()
            door_b_right.set_position(Point(constants.MAX_X - 40, int(constants.MAX_Y / 3 * 2)))
            door_t_right.set_position(Point(constants.MAX_X - 40, 0)) 
            door_b_left = VDoor()
            door_t_left = VDoor()
            door_b_left.set_position(Point(0, int(constants.MAX_Y / 3 * 2)))
            door_t_left.set_position(Point(0, 0))
            locked_door.append(lockeddoor)
            walls.append(door_b_left) 
            walls.append(door_t_left)
            walls.append(door_b_right)
            walls.append(door_t_right)
            walls.append(door_b_top)
            walls.append(door_t_top)
            walls.append(door_b_bottem)
            walls.append(door_t_bottem)
            boxes.append(box1)
            boxes.append(box2)
            cast["walls"] = walls
            cast["locked_door"] = locked_door
            cast["ghost"] = [ghost]
            cast["trap"] = [trap]
            cast["spikes"] = spikes
            cast["boxes"] = boxes
        #Room 6
        if (hero_location_x >= constants.MAX_X - 45 and self._roomnumber == 5) or (hero_location_y >= constants.MAX_Y - 45 and self._roomnumber == 9) or (hero_location_y <= 40 and self._roomnumber == 3):
            if self._roomnumber == 9:
                hero.set_position(Point(int(constants.MAX_X / 2), 45))
            elif self._roomnumber == 3:
                hero.set_position(Point(int(constants.MAX_X / 2), constants.MAX_Y - 105))   
            elif self._roomnumber == 5:
                hero.set_position(Point(10, int(constants.MAX_Y / 2)))
            walls = []
            locked_door = []
            spikes = []
            boxes = []
            self._roomnumber = 6
            ghost.set_position(Point(900, 900))
            ghost.set_velocity(Point(0, 0))
            trap.set_position(Point(900, 900))
            box1.set_position(Point(100, 180))
            box2.set_position(Point(470, 420))
            if self._key_location == 4:
                box1.set_description('KEY FOUND')
            if self._key_location == 5:
                box2.set_description('KEY FOUND')
            lockeddoor = LockedDoor()
            lockeddoor.set_position(Point(900, 900))
            wall_right = VWall()
            wall_right.set_position(Point(constants.MAX_X - 40, 0))
            door_b_left = VDoor()
            door_t_left = VDoor()
            door_b_left.set_position(Point(0, int(constants.MAX_Y / 3 * 2)))
            door_t_left.set_position(Point(0, 0))
            door_b_bottem = HDoor()
            door_t_bottem = HDoor()
            door_b_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_t_bottem.set_position(Point(int(constants.MAX_X / 3 * 2), constants.MAX_Y - 40))
            door_b_top = HDoor()
            door_t_top = HDoor()
            door_b_top.set_position(Point(0, 0))
            door_t_top.set_position(Point(int(constants.MAX_X / 3 * 2), 0))   
            locked_door.append(lockeddoor)
            walls.append(door_b_top)  
            walls.append(door_t_top) 
            walls.append(door_t_left)  
            walls.append(door_b_left)
            walls.append(wall_right)
            walls.append(door_b_bottem)
            walls.append(door_t_bottem)
            boxes.append(box1)
            boxes.append(box2) 
            cast["trap"] = [trap]
            cast["boxes"] = boxes
            cast["walls"] = walls
            cast["spikes"] = spikes
            cast["ghost"] = [ghost]
            cast["spikes"] = spikes
        #Room 7
        if (hero_location_x <= 5 and self._roomnumber == 8) or (hero_location_y <= 15 and self._roomnumber == 4):
            if self._roomnumber == 4:
                hero.set_position(Point(int(constants.MAX_X / 2), constants.MAX_Y - 85))
            elif self._roomnumber == 8:
                hero.set_position(Point(constants.MAX_X - 80, int(constants.MAX_Y / 2)))
            walls = []
            locked_door = []
            boxes = []
            spikes = []
            self._roomnumber = 7
            ghost.set_position(Point(int(constants.MAX_X / 3), int(constants.MAX_Y / 2)))
            ghost.set_velocity(Point(25, 25))
            trap.set_position(Point(520, int(constants.MAX_Y / 2)))
            box1.set_position(Point(300, 300))
            if self._key_location == 6:
                box1.set_description('KEY FOUND')
            lockeddoor = LockedDoor()
            lockeddoor.set_position(Point(900, 900))
            wall_left = VWall()
            wall_left.set_position(Point(0, 0))
            door_b_right = VDoor()
            door_t_right = VDoor()
            door_b_right.set_position(Point(constants.MAX_X - 40, int(constants.MAX_Y / 3 * 2)))
            door_t_right.set_position(Point(constants.MAX_X - 40, 0))
            door_b_bottem = HDoor()
            door_t_bottem = HDoor()
            door_b_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_t_bottem.set_position(Point(int(constants.MAX_X / 3 * 2), constants.MAX_Y - 40))
            wall_top = HWall()
            wall_top.set_position(Point(0, 0))
            locked_door.append(lockeddoor)
            walls.append(wall_top) 
            walls.append(door_t_right)  
            walls.append(door_b_right)
            walls.append(wall_left)
            walls.append(door_b_bottem)
            walls.append(door_t_bottem)
            boxes.append(box1)
            boxes.append(box2) 
            cast["walls"] = walls
            cast["ghost"] = [ghost]
            cast["boxes"] = boxes
            cast["trap"] = [trap]
            cast["spikes"] = spikes
        #Room 8
        if (hero_location_x >= constants.MAX_X - 75 and self._roomnumber == 7) or (hero_location_x <= 5 and self._roomnumber == 9) or (hero_location_y <= 10 and self._roomnumber == 5):
            if self._roomnumber == 7:
                hero.set_position(Point(40, int(constants.MAX_Y / 2)))
            elif self._roomnumber == 9: 
                hero.set_position(Point(constants.MAX_X - 80, int(constants.MAX_Y / 2)))
            elif self._roomnumber == 5:
                hero.set_position(Point(int(constants.MAX_X / 2), constants.MAX_Y - 80))
            self._roomnumber = 8
            walls = []
            locked_door = []
            boxes = []
            spikes = []
            ghost.set_position(Point(900, 900))
            ghost.set_velocity(Point(0, 0))
            trap.set_position(Point(120, int(constants.MAX_Y / 2)))
            box1.set_position(Point(300, 100))
            if self._key_location == 7:
                box1.set_description('KEY FOUND')
            lockeddoor = LockedDoor()
            lockeddoor.set_position(Point(900, 900))
            door_b_bottem = HDoor()
            door_t_bottem = HDoor()
            door_b_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_t_bottem.set_position(Point(int(constants.MAX_X / 3 * 2), constants.MAX_Y - 40))
            wall_top = HWall()
            wall_top.set_position(Point(0, 0))
            door_b_right = VDoor()
            door_t_right = VDoor()
            door_b_right.set_position(Point(constants.MAX_X - 40, int(constants.MAX_Y / 3 * 2)))
            door_t_right.set_position(Point(constants.MAX_X - 40, 0)) 
            door_b_left = VDoor()
            door_t_left = VDoor()
            door_b_left.set_position(Point(0, int(constants.MAX_Y / 3 * 2)))
            door_t_left.set_position(Point(0, 0))
            locked_door.append(lockeddoor)
            walls.append(door_b_left) 
            walls.append(door_t_left)
            walls.append(door_b_right)
            walls.append(door_t_right)
            walls.append(wall_top)
            walls.append(door_b_bottem)
            walls.append(door_t_bottem)
            boxes.append(box1)
            boxes.append(box2)
            cast["walls"] = walls
            cast["trap"] = [trap]
            cast["boxes"] = boxes
            cast["ghost"] = [ghost]
            cast["spikes"] = spikes
        #Room 9
        if (hero_location_x >= constants.MAX_X - 45 and self._roomnumber == 8) or (hero_location_y <= 20 and self._roomnumber == 6):
            if self._roomnumber == 6:
                hero.set_position(Point(int(constants.MAX_X / 2), constants.MAX_Y - 85))
            elif self._roomnumber == 8:
                hero.set_position(Point(40, int(constants.MAX_Y / 2)))
            walls = []
            spikes = []
            boxes = []
            locked_door = []
            self._roomnumber = 9
            ghost.set_position(Point(int(constants.MAX_X / 3), int(constants.MAX_Y / 2)))
            ghost.set_velocity(Point(25, 25))
            box1.set_position(Point(460, 75))
            if self._key_location == 8:
                box1.set_description('KEY FOUND')
            lockeddoor = LockedDoor()
            lockeddoor.set_position(Point(900, 900))
            wall_right = VWall()
            wall_right.set_position(Point(constants.MAX_Y - 40, 0))
            door_b_left = VDoor()
            door_t_left = VDoor()
            door_b_left.set_position(Point(0, int(constants.MAX_Y / 3 * 2)))
            door_t_left.set_position(Point(0, 0))
            door_b_bottem = HDoor()
            door_t_bottem = HDoor()
            door_b_bottem.set_position(Point(0, constants.MAX_Y - 40))
            door_t_bottem.set_position(Point(int(constants.MAX_X / 3 * 2), constants.MAX_Y - 40))
            wall_top = HWall()
            wall_top.set_position(Point(0, 0))
            locked_door.append(lockeddoor)
            walls.append(wall_top) 
            walls.append(door_t_left)  
            walls.append(door_b_left)
            walls.append(wall_right)
            walls.append(door_b_bottem)
            walls.append(door_t_bottem) 
            boxes.append(box1)
            boxes.append(box2)
            cast["walls"] = walls
            cast["ghost"] = [ghost]
            cast["trap"] = [trap]
            cast["boxes"] = boxes
            cast["spikes"] = spikes
        #exit
        if hero_location_y >= constants.MAX_Y - 35 and self._roomnumber == 2:
            win_text = Actor()
            win_text.set_position(Point(int(constants.MAX_X / 2), int(constants.MAX_Y / 2)))
            win_text.set_height(constants.WIN_SIZE)
            win_text.set_width(constants.WIN_SIZE)
            win_text.set_text('YOU WIN')
            cast["win"] = [win_text]
            audio_service = AudioService()
            audio_service.play_sound(constants.SOUND_WIN)
            time.sleep(4)
            sys.exit()


