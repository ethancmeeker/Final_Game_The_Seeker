from game import constants, physics_service
from game.action import Action
from game.point import Point
from game.audio_service import AudioService
from game.room_attributes import RoomAttributes
from game.director import Director
import sys
import pyray
import time
import random

class GhostHeroCollision(Action):
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
        hero = cast["hero"][0]
        spikes = cast["spikes"]
        audio_service = AudioService()
        if self._physics_service.is_collision(ghosts, hero):
            audio_service.play_sound(constants.SOUND_GAME_OVER)
            time.sleep(3)
            sys.exit()
        for spike in spikes:
            if self._physics_service.is_collision(spike, hero):
                audio_service.play_sound(constants.SOUND_GAME_OVER)
                time.sleep(3)
                sys.exit()