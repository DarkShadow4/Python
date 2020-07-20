import sys, os
sys.path.append(os.getcwd())
import entities
import pygame
import numpy as np

class Button(object):
    """docstring for Button."""

    def __init__(self, id=None, background_color=(255, 255, 255), text_color=(0, 0, 0), top_left=None, text="", font_size= 10):
        super(Button, self).__init__()
        self.top_left = top_left
        pygame.font.init()
        font = pygame.font.Font("freesansbold.ttf", font_size)
        self.text = font.render(text, True, text_color, background_color)
        self.name = text
        self.button_rect = self.text.get_rect()
        self.button_rect.topleft = top_left

    def clicked_in(self, mouse_pos):
        # print(self.button_rect.left < mouse_pos[0] < self.button_rect.right and self.button_rect.top < mouse_pos[1] < self.button_rect.bottom)
        return ((self.button_rect.left < mouse_pos[0] < self.button_rect.right) and (self.button_rect.top < mouse_pos[1] < self.button_rect.bottom))

# font_size = 20
# i = 0
# test_button = Button(id=i, background_color=(147, 255, 0), text_color=(255, 0, 247), top_left = (0, i*(font_size+2)), text="test", font_size = font_size)
# test_button.name

class Viewer(object):
    """docstring for Viewer."""

    def __init__(self, width, height, background_color=(0, 0, 0)):
        super(Viewer, self).__init__()
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width, height))
        pygame.init()
        self.objects = {}
        self.buttons = {}
        self.object_focus = "context"

    def addObjects(self, objects):
        for obj in objects:
            self.objects[obj.name] = obj

    def run(self):
        KtF = {
            pygame.K_w: (lambda x: x.translateFocus([0, -10, 0])),
            pygame.K_a: (lambda x: x.translateFocus([-10, 0, 0])),
            pygame.K_s: (lambda x: x.translateFocus([0, 10, 0])),
            pygame.K_d: (lambda x: x.translateFocus([10, 0, 0])),
            pygame.K_INSERT: (lambda x: x.scaleFocus(1.25)),
            pygame.K_DELETE: (lambda x: x.scaleFocus(0.8)),
            pygame.K_q: (lambda x: x.rotateFocus(0.1, "z")), # counterclockwise
            pygame.K_e: (lambda x: x.rotateFocus(-0.1, "z")), # clockwise
            pygame.K_LEFT: (lambda x: x.rotateFocus(-0.1, "y")), # clockwise
            pygame.K_RIGHT: (lambda x: x.rotateFocus(0.1, "y")), # counterclockwise
            pygame.K_UP: (lambda x: x.rotateFocus(-0.1, "x")), # forward
            pygame.K_DOWN: (lambda x: x.rotateFocus(0.1, "x")) # backward
        }
        running = True
        while running:
            pressed_keys = pygame.key.get_pressed()
            for key in KtF.keys():
                if pressed_keys[key]:
                    KtF[key](self)
            mouse_pressed = pygame.mouse.get_pressed()

            running = not pressed_keys[pygame.K_ESCAPE]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if mouse_pressed[pygame.BUTTON_LEFT-1]:
                    for button in self.buttons.values():
                        if button.clicked_in(pygame.mouse.get_pos()):
                            self.object_focus = button.name


            self.display()
            self.display_buttons()
            pygame.display.flip()
            pygame.time.delay(100)

        pygame.quit()

    def display(self):
        self.screen.fill(self.background_color)
        pygame.display.flip()
        for obj in self.objects.values():
            for node in obj.nodes:
                pygame.draw.circle(self.screen, obj.node_color, (int(node[0]+self.width/2), int(node[1]+self.height/2)), int(obj.node_radius/2), 0)
            for start, end in obj.edges:
                pygame.draw.line(self.screen, obj.edge_color, (obj.nodes[start][0]+self.width/2, obj.nodes[start][1]+self.height/2), (obj.nodes[end][0]+self.width/2, obj.nodes[end][1]+self.height/2), 1)

    def display_buttons(self):
        for button in self.buttons.values():
            self.screen.blit(button.text, button.button_rect)
            # self.screen.update(button.button_rect)
    # def display(self):
    #     self.screen.fill(self.background_color)
    #     pygame.display.flip()
    #     for obj in self.objects.values():
    #         i = 0
    #         color = (0, 255, 0)
    #         while i < 4:
    #
    #             pygame.draw.circle(self.screen, (0, 255, 0), (int(obj.nodes[i][0]+self.width/2), int(obj.nodes[i][1]+self.height/2)), obj.node_radius, 0)
    #             i += 1
    #
    #         color = (255, 255, 255)
    #         while i < len(obj.nodes):
    #             pygame.draw.circle(self.screen, color, (int(obj.nodes[i][0]+self.width/2), int(obj.nodes[i][1]+self.height/2)), int(obj.node_radius/2), 0)
    #             i += 1
    #
    #         for start, end in obj.edges:
    #             pygame.draw.line(self.screen, obj.edge_color, (obj.nodes[start][0]+self.width/2, obj.nodes[start][1]+self.height/2), (obj.nodes[end][0]+self.width/2, obj.nodes[end][1]+self.height/2), 1)

    def translateAll(self, movement):
        matrix = entities.translationMatrix(*movement)
        for obj in self.objects.values():
            obj.transform(matrix, "T")

    def scaleAll(self, scalar):
        matrix = entities.scalingMatrix(scalar, scalar, scalar)
        for obj in self.objects.values():
            obj.transform(matrix, "S")

    def rotate(self, radians, axis):
        rotateMatrix = "rotate"+axis.title()+"matrix"
        matrix = getattr(entities, rotateMatrix)(radians)
        for obj in self.objects.values():
            obj.transform(matrix, "R"+axis.title())

    def addButtons(self, buttons):
        for button in buttons:
            type(button)
            self.buttons[button.text] = button

    def translateFocus(self, movement):
        if self.object_focus == "context":
            self.translateAll(movement)
        else:
            matrix = entities.translationMatrix(*movement)
            self.objects[self.object_focus].transform(matrix, "T")

    def scaleFocus(self, scalar):
        if self.object_focus == "context":
            self.scaleAll(scalar)
        else:
            matrix = entities.scalingMatrix(scalar, scalar, scalar)
            self.objects[self.object_focus].transform(matrix, "S")

    def rotateFocus(self, radians, axis):
        if self.object_focus == "context":
            self.rotate(radians, axis)
        else:
            rotateMatrix = "rotate"+axis.title()+"matrix"
            matrix = getattr(entities, rotateMatrix)(radians)
            self.objects[self.object_focus].transform(matrix, "R"+axis.title())
