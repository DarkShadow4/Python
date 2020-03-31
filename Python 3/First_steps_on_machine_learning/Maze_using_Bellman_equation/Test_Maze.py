import pygame, sys, maze_builder

class Maze(object):
    def __init__(self, width, height, grid_length): # width and height of the window and the grid size (x, y) so there would be a maximum number of nodes which would be x*y
        super(Maze, self).__init__()
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("TEST MAZE")
        self.background = (0, 0, 0)
        self.nodes = {} # (x, y):maze_builder.Node
        self.nodeRadius = 4
        self.grid_length = grid_length
        self.node_width = width/grid_length[0]
        self.node_height = height/grid_length[1]


    def display(self):
        """ Draw the objects on the screen. """
        self.screen.fill(self.background)
        for position, node in self.nodes.items():
            # i get the square for the node
            pygame.draw.rect(self.screen, node.floor_color, (int(node.position[0])*self.node_width, int(node.position[1])*self.node_height, self.node_width, self.node_height), 0) # this is the floor
            # now lets draw the walls
            pygame.draw.rect(self.screen, node.wall_color, (int(node.position[0])*self.node_width, int(node.position[1])*self.node_height, self.node_width*0.1, self.node_height*0.1), 0) # top left corner
            pygame.draw.rect(self.screen, node.wall_color, (int(node.position[0])*self.node_width+self.node_width*0.9, int(node.position[1])*self.node_height, self.node_width*0.1, self.node_height*0.1), 0) # top right corner
            pygame.draw.rect(self.screen, node.wall_color, (int(node.position[0])*self.node_width+self.node_width*0.9, int(node.position[1])*self.node_height+self.node_height*0.9, self.node_width*0.1, self.node_height*0.1), 0) # bottom right corner
            pygame.draw.rect(self.screen, node.wall_color, (int(node.position[0])*self.node_width, int(node.position[1])*self.node_height+self.node_height*0.9, self.node_width*0.1, self.node_height*0.1), 0) # bottom left corner
            # taking wall width equal to 10% of the node size
            if not node.up: # top wall
                pygame.draw.rect(self.screen, node.wall_color, (int(node.position[0])*self.node_width+self.node_width*0.09, int(node.position[1])*self.node_height, self.node_width*0.82, self.node_height*0.1), 0)
            if not node.right: # right wall
                pygame.draw.rect(self.screen, node.wall_color, (int(node.position[0])*self.node_width+self.node_width*0.9, int(node.position[1])*self.node_height+self.node_height*0.09, self.node_width*0.1, self.node_height*0.82), 0)
            if not node.down: # bottom wall
                pygame.draw.rect(self.screen, node.wall_color, (int(node.position[0])*self.node_width+self.node_width*0.09, int(node.position[1])*self.node_height+self.node_height*0.9, self.node_width*0.82, self.node_height*0.1), 0)
            if not node.left: # left wall
                pygame.draw.rect(self.screen, node.wall_color, (int(node.position[0])*self.node_width, int(node.position[1])*self.node_height+self.node_height*0.09, self.node_width*0.1, self.node_height*0.82), 0)

        pygame.draw.rect(self.screen, self.runner.color, (self.runner.position[0]*self.node_width+(self.node_width/2-self.runner.width/2), self.runner.position[1]*self.node_height+(self.node_height/2-self.runner.height/2), self.runner.width, self.runner.height), 0)

    def move_runner(self, direction):
        if getattr(self.nodes[self.runner.position], direction):
            if direction == "up":
                self.runner.position = (self.runner.position[0], self.runner.position[1]-1)
            if direction == "down":
                self.runner.position = (self.runner.position[0], self.runner.position[1]+1)
            if direction == "right":
                self.runner.position = (self.runner.position[0]+1, self.runner.position[1])
            if direction == "left":
                self.runner.position = (self.runner.position[0]-1, self.runner.position[1])

    def run(self):
        """Create a pygame screen until it is closed."""
        key_to_function = {
            pygame.K_LEFT:   (lambda x: x.move_runner("left")),
            pygame.K_RIGHT:   (lambda x: x.move_runner("right")),
            pygame.K_UP:   (lambda x: x.move_runner("up")),
            pygame.K_DOWN:   (lambda x: x.move_runner("down"))
            # pygame.K_q:   (lambda x: x.rotateAll('Z', -0.1)),
            # pygame.K_e:   (lambda x: x.rotateAll('Z', 0.1)),
            # pygame.K_d:  (lambda x: x.move_all('x',  10)),
            # pygame.K_a:   (lambda x: x.move_all('x', -10)),
            # pygame.K_s:   (lambda x: x.move_all('y',  10)),
            # pygame.K_w:     (lambda x: x.move_all('y', -10)),
            # pygame.K_LSHIFT: (lambda x: x.scaleAll(1.25)),
            # pygame.K_LCTRL:  (lambda x: x.scaleAll( 0.8))
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

            pygame.time.delay(100)
            self.display()
            pygame.display.flip()
        pygame.quit()
        return done

    def add_node(self, node):
        type = node.special
        if type == "start":
            self.start = node.position
        if type == "end":
            self.end = node.position
        self.nodes[node.position] = node

    def add_runner(self, runner):
        if runner.width == "relative":
            runner.width = self.node_width*0.4
        if runner.height == "relative":
            runner.height = self.node_height*0.4
        if runner.position == None:
            runner.position = self.start

        self.runner = runner

class Maze_runner(object):
    """docstring for Maze_runner."""

    def __init__(self, position=None, color=(255, 255, 255), width="relative", height="relative"):
        super(Maze_runner, position).__init__()
        self.position = position
        self.color = color
        self.width = width
        self.height = height


runner = Maze_runner()

# x x
#   x x
# x x
maze = Maze( 1000, 1000, (3, 3))
test_node_00 = maze_builder.Node(position=(0, 0), right = True, special="start")
test_node_10 = maze_builder.Node(position=(1, 0), left = True, down = True, right = True)
test_node_20 = maze_builder.Node(position=(2, 0), down = True, left = True)
test_node_11 = maze_builder.Node(position=(1, 1), down = True, up = True, right = True, special="bad")
test_node_21 = maze_builder.Node(position=(2, 1), left = True, up=True, down=True, special="good")
test_node_22 = maze_builder.Node(position=(2, 2), up = True, left = True)
test_node_12 = maze_builder.Node(position=(1, 2), up = True, left = True, right = True)
test_node_02 = maze_builder.Node(position=(0, 2), right = True, special="end")
maze.add_node(test_node_00)
maze.add_node(test_node_20)
maze.add_node(test_node_10)
maze.add_node(test_node_11)
maze.add_node(test_node_21)
maze.add_node(test_node_22)
maze.add_node(test_node_12)
maze.add_node(test_node_02)
maze.add_runner(runner)
maze.run()

# x x
# x x

# maze = Maze( 1000, 1000, (2, 2))
# test_node_00 = maze_builder.Node(position=(0, 0), right = True, up = True, special="start")
# test_node_10 = maze_builder.Node(position=(1, 0), left = True, down = True)
# test_node_11 = maze_builder.Node(position=(1, 1), up = True, left = True)
# test_node_01 = maze_builder.Node(position=(0, 1), right = True, down = True, special="end")
# maze.add_node(test_node_00)
# maze.add_node(test_node_10)
# maze.add_node(test_node_11)
# maze.add_node(test_node_01)
# maze.add_runner(runner)
# maze.run()
