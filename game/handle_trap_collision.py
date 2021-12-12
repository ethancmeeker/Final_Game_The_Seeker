import random
from game import constants
from game.action import Action
from game.point import Point
from game.spikes import Spikes
from game.audio_service import AudioService

class HandleTrapCollisions(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._active = False

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        audio_service = AudioService()
        hero = cast["hero"][0] # there's only one
        trap = cast["trap"][0]
        spikes = []
        if self._physics_service.is_collision(hero, trap):
            trap.set_position(Point(900, 900))
            audio_service.play_sound(constants.SOUND_TRAP)
            for n in range(constants.SPIKES_IN_ROOM):
                x = random.randint(50, constants.MAX_X - 90)
                y = random.randint(50, constants.MAX_Y - 90)
                spike = Spikes()
                spike.set_position(Point(x, y))
                spikes.append(spike)
            cast["spikes"] = spikes
