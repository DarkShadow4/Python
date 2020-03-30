import pygame, sys, maze_builder

class Projection(object):
    def __init__(self, width, height):
        super(Projection, self).__init__()
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("TEST MAZE")
        self.background = (0, 0, 0)
        self.nodes = {} # (x, y):maze_builder.Node
        self.displayNodes = True
        self.displayEdges = True
        # self.nodeColour = (0,0,0)
        # self.edgeColour = (125,125,125)
        self.nodeRadius = 4

    def display(self):
        """ Draw the objects on the screen. """
        self.screen.fill(self.background)
        for thing in self.objects.values():
            # if thing.displayEdges:
            #     for edge in thing.edges:
            #         pygame.draw.aaline(self.screen, self.edgeColour, (edge.start.x, edge.start.y), (edge.end.x, edge.end.y), 1)
            for edge in thing.edges:
                    pygame.draw.aaline(self.screen, thing.edge_color, (edge.start.x, edge.start.y), (edge.end.x, edge.end.y), 1)
            # if thing.displayNodes:
            #     for node in thing.nodes:
            #         pygame.draw.circle(self.screen, self.nodeColour, (int(node.x), int(node.y)), self.nodeRadius, 0)
            for node in thing.nodes:
                pygame.draw.circle(self.screen, thing.node_color, (int(node.x), int(node.y)), self.nodeRadius, 0)

    def run(self):
        """Create a pygame screen until it is closed."""
        key_to_function = {
            pygame.K_LEFT:   (lambda x: x.rotateAll('Y', -0.1)),
            pygame.K_RIGHT:   (lambda x: x.rotateAll('Y', 0.1)),
            pygame.K_UP:   (lambda x: x.rotateAll('X', -0.1)),
            pygame.K_DOWN:   (lambda x: x.rotateAll('X', 0.1)),
            pygame.K_q:   (lambda x: x.rotateAll('Z', -0.1)),
            pygame.K_e:   (lambda x: x.rotateAll('Z', 0.1)),
            pygame.K_d:  (lambda x: x.move_all('x',  10)),
            pygame.K_a:   (lambda x: x.move_all('x', -10)),
            pygame.K_s:   (lambda x: x.move_all('y',  10)),
            pygame.K_w:     (lambda x: x.move_all('y', -10)),
            pygame.K_LSHIFT: (lambda x: x.scaleAll(1.25)),
            pygame.K_LCTRL:  (lambda x: x.scaleAll( 0.8))
        }
        done = False
        while not done:
            keys = pygame.key.get_pressed()
            for key in key_to_function.keys():
                if keys[key]:
                    key_to_function[key](self)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    # if event.key in key_to_function.keys():
                    #     key_to_function[event.key](self)

            pygame.time.delay(100)
            self.display()
            pygame.display.flip()
        pygame.quit()
        return done

    def add_node(self, position, node):
        self.objects[position] = node
