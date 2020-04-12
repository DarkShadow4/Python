import pygame

class Node(object):
    """docstring for Node."""

    def __init__(self, size=None, up=False, down=False, left=False, right=False, price=0, special=None, floor_color=(0, 0, 0), wall_color=(255, 255, 255), position=None):
        super(Node, self).__init__()
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
        self.actions = ""
        if right:
            self.actions += "r"
        if down:
            self.actions += "d"
        if left:
            self.actions += "l"
        if up:
            self.actions += "u"

        self.floor_color = floor_colors[special]
        self.reward = 0
        self.value = 0
        if special == "end":
            self.reward = 1
        if special == "good":
            self.reward = 0.5
        if special == "bad":
            self.reward = -0.5

        self.wall_color = wall_color
        if position != None:
            self.position = position
