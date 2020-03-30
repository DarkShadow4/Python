import pygame
class Node(object):
    """docstring for Node."""

    def __init__(self, size, up=False, down=False, left=False, right=False, price=0, end=False, floor_color=(0, 0, 0), wall_color=(255, 255, 255), position=None):
        super(Node, self).__init__()
        self.size = size
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.floor_color = floor_color
        self.wall_color = wall_color
        if position != None:
            self.position = position
