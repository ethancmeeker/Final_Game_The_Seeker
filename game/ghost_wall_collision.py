from game import constants, physics_service
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
from game.room_attributes import RoomAttributes
import sys
import time
import random

class GhostWallCollisions(Action):
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
        ghosts = cast["ghost"][0]
        walls = cast["walls"]
        direction = ghosts.get_velocity()
        vx = direction.get_x()
        vy = direction.get_y()
        x_possible = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        y_possible = [35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15]
        for wall in walls:
            if self._physics_service.is_collision(ghosts, wall):
                x_pick = random.choice(x_possible)
                x_spot = x_possible.index(x_pick)
                y_pick = y_possible[x_spot]
                if vx > 0 and vy > 0:
                    ghosts.set_velocity(Point(x_pick * -1, y_pick))
                if vx < 0 and vy > 0:
                    ghosts.set_velocity(Point(x_pick * -1, y_pick * -1))
                if vx < 0 and vy < 0:
                    ghosts.set_velocity(Point(x_pick, y_pick * -1))
                if vx > 0 and vy < 0:
                    ghosts.set_velocity(Point(x_pick, y_pick))

            '''
            This is what I did to make my code my unique. The game would play out exactly
            the same if I didn't do this every single time (unless you lost). This changes
            the direction it bounces off the paddle making things different.'''