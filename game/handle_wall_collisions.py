from game import constants, physics_service
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
import sys
import time
import random

class HandleWallCollisions(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        audio_service = AudioService()
        hero = cast["hero"][0]
        walls = cast["walls"]
        locked_door = cast["locked_door"]
        collide = hero.get_position()
        direction = hero.get_velocity()
        px = collide.get_x()
        py = collide.get_y()
        vx = direction.get_x()
        vy = direction.get_y()
        '''
        This is what I did to make my code my unique. The game would play out exactly
        the same if I didn't do this every single time (unless you lost). This changes
        the direction it bounces off the paddle making things different.'''
        for wall in walls:
            if self._physics_service.is_collision(hero, wall):
                if vx > 0 and vy == 0:
                    hero.set_position(Point(px - 40, py))
                if vx < 0 and vy == 0:
                    hero.set_position(Point(px + 40, py))
                if vy > 0 and vx == 0:
                    hero.set_position(Point(px, py - 40))
                if vy < 0 and vx == 0:
                    hero.set_position(Point(px, py + 40))  
                if vx > 0 and vy > 0:
                    hero.set_position(Point(px - 40, py - 40))
                if vx > 0 and vy < 0:
                    hero.set_position(Point(px - 40, py + 40))
                if vx < 0 and vy > 0:
                    hero.set_position(Point(px + 40, py - 40))
                if vx < 0 and vy < 0:
                    hero.set_position(Point(px + 40, py + 40))
            for door in locked_door:
                if self._physics_service.is_collision(hero, door):
                    if vx > 0 and vy == 0:
                        hero.set_position(Point(px - 40, py))
                    if vx < 0 and vy == 0:
                        hero.set_position(Point(px + 40, py))
                    if vy > 0 and vx == 0:
                        hero.set_position(Point(px, py - 40))
                    if vy < 0 and vx == 0:
                        hero.set_position(Point(px, py + 40))  
                    if vx > 0 and vy > 0:
                        hero.set_position(Point(px - 40, py - 40))
                    if vx > 0 and vy < 0:
                        hero.set_position(Point(px - 40, py + 40))
                    if vx < 0 and vy > 0:
                        hero.set_position(Point(px + 40, py - 40))
                    if vx < 0 and vy < 0:
                        hero.set_position(Point(px + 40, py + 40))