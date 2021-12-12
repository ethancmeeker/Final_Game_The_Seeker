import random
import time
import sys
from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor

class HandleBoxCollisions(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._key_value = ''
        self._x = 0 
        self._y = constants.MAX_Y - 20
    
    def set_key_value(self, key):
        self._key_value = key

    def get_key_value(self):
        return self._key_value 

    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        marquee = cast["marquee"][0] # there's only one
        hero = cast["hero"][0] # there's only one
        boxes = cast["boxes"]
        locked_door = cast["locked_door"]
        marquee.set_text(self._key_value)
        hero_spot = hero.get_position()
        hero_y = hero_spot.get_y()
        for box in boxes:
            if self._physics_service.is_collision(hero, box):
                description = box.get_description()
                marquee.set_text(description)
        if marquee.get_text() == 'KEY FOUND':
            self.set_key_value('KEY FOUND') 
        