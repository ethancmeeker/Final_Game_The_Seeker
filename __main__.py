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
from game.room_attributes import RoomAttributes
from game.handle_wall_collisions import HandleWallCollisions
from game.ghost_wall_collision import GhostWallCollisions
from game.ghost_hero_collision import GhostHeroCollision
from game.handle_box_collisions import HandleBoxCollisions
from game.handle_trap_collision import HandleTrapCollisions
from game.audio_service import AudioService
from game.room import Rooms
from game.control_actors import ControlActorsAction
from game.hero import Hero
from game.ghost import Ghost
from game.box import Box
from game.trap import Trap
from game.spikes import Spikes
from game.verticle_door import VDoor
from game.verticle_wall import VWall
from game.horizontal_wall import HWall
from game.horizontal_door import HDoor
from game.locked_door import LockedDoor



def main():

    # create the cast {key: tag, value: list}
    cast = {}
    current = 1
    walls = []
    locked_door = []
    door_b_bottem = HDoor()
    door_t_bottem = HDoor()
    door_locked = LockedDoor()
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
    walls.append(door_b_left) 
    walls.append(door_t_left)
    walls.append(door_b_right)
    walls.append(door_t_right)
    walls.append(door_b_top)
    walls.append(door_t_top)
    walls.append(door_b_bottem)
    walls.append(door_t_bottem)
    locked_door.append(door_locked)
    cast["walls"] = walls
    cast["locked_door"] = locked_door

    marquee = Actor()
    marquee.set_text('')
    marquee.set_position(Point(1, 0))
    cast["marquee"] = [marquee]

    trap = Trap()
    cast["trap"] = [trap]

    spikes = []
    spike = Spikes()
    spikes.append(spike)
    cast["spikes"] = spikes

    boxes = []
    box1 = Box()
    boxes.append(box1)
    cast["boxes"] = boxes

    ghost = Ghost()
    cast["ghost"] = [ghost]

    x = int(constants.MAX_X / 2 - 20)
    y = int(constants.MAX_Y - 100)
    position = Point(x, y)
    hero = Hero()
    hero.set_position(position)
    cast["hero"] = [hero]

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors = MoveActorsAction()

    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)
    room_attributes = RoomAttributes(physics_service)
    handle_wall_collisions = HandleWallCollisions(physics_service)
    ghost_wall_collisions = GhostWallCollisions(physics_service)
    ghost_hero_collisions = GhostHeroCollision(physics_service)
    box_collisions = HandleBoxCollisions(physics_service)
    trap_collisions = HandleTrapCollisions(physics_service)



    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors, room_attributes, handle_wall_collisions, ghost_wall_collisions, ghost_hero_collisions, box_collisions, trap_collisions]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Seeker")  #There was a semi-colon here not sure if I accidently added it or not.
    audio_service.start_audio()
    
    director = Director(cast, script)
    director.start_game()
    audio_service.stop_audio()



if __name__ == "__main__":
    main()
