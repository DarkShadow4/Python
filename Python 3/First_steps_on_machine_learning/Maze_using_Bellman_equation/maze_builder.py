import pygame
class Node(object):
    """docstring for Node."""

    def __init__(self, size=None, up=False, down=False, left=False, right=False, price=0, special=None, floor_color=(0, 0, 0), wall_color=(255, 255, 255), position=None):
        super(Node, self).__init__()
        # specials = {
        #     "start":(lambda x: setattr(x, floor_color, (150, 150, 255))),
        #     "end":(lambda x: setattr(x, floor_color, (255, 255, 0))),
        #     "good":(lambda x: setattr(x, floor_color, (150, 255, 150))),
        #     "bad":(lambda x: setattr(x, floor_color, (255, 150, 150)))
        # }
        floor_colors = {
            None:(0, 0, 0),
            "start":(150, 150, 255),
            "end":(255, 255, 0),
            "good":(0, 255, 0),
            "bad":(255, 0, 0)
        }
        self.special = special
        self.size = size
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.floor_color = floor_colors[special]
        self.wall_color = wall_color
        # if special != None:
        #     specials[special](self)
        if position != None:
            self.position = position
