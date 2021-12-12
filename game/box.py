from game.actor import Actor
from game import constants

class Box(Actor):
    """
    Defines an artifact in the game. Inherits from Actor, and adds a description.
    """
    def __init__(self):
        super().__init__()
        self.set_width(constants.BOX_WIDTH)
        self.set_height(constants.BOX_HEIGHT)
        self.set_description('NO KEY HERE')
        self.set_image(constants.BOX_IMAGE)

