import random
import os
import sys
import time
from game import constants
from game import control_actors
from game.director import Director
from game.move_actors_action import MoveActorsAction
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.control_actors import ControlActorsAction
from game.hero import Hero


# TODO: Add imports similar to the following when you create these classes
# from game.brick import Brick
# from game.ball import Ball
# from game.paddle import Paddle
# from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction
# from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 100)
    position = Point(x, y)
    hero = Hero()
    hero.set_position(position)
    cast["hero"] = [hero]

    # TODO: Create a paddle here and add it to the list


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors = MoveActorsAction()

    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)


    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Seeker")  #There was a semi-colon here not sure if I accidently added it or not.
    audio_service.start_audio()
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()



if __name__ == "__main__":
    main()
