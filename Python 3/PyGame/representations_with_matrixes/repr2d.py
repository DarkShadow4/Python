import pygame

class Transformation(object):
    """docstring for Transformation."""

    def __init__(self, matrix):
        super(Transformation, self).__init__()
        self.matrix = []
        for row in matrix:
            r = []
            for item in row:
                r.append(item)
            self.matrix.append(r)


    def print_T(self, det=False):
        for row in range(len(self.matrix)):
            if det == False:
                if row == 0:
                    print("/", end = " ")
                elif row == len(self.matrix)-1:
                    print("\\", end = " ")
                else:
                    print("|", end = " ")
            else:
                print("|", end = " ")

            for column in range(len(self.matrix[row])):
                print(self.matrix[row][column], end=" ")

            if det == False:
                if row == 0:
                    print("\\")
                elif row == len(self.matrix)-1:
                    print("/")
                else:
                    print("|")
            else:
                print("|")

    def transform(self, vectors, right = False):
        for vector in vectors:
            print(vector)
            if len(vector) == len(self.matrix):
                new_vector = [item for item in vector]
                for i in range(len(vector)):
                    new_vector[i] = sum([vector[row]*self.matrix[i][row] for row in range(len(vector))])
                print(new_vector)
        return(new_vector)

Base = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
B = Transformation(Base)
Grid = [] # a list with the vectors or positions
size = 1000
step = int(size/10)
Base_grid = [[x, y] for x in range(0, size, step) for y in range(0, size, step)]

class Projection(object):
    def __init__(self, width, height, point_color=(0,0,0), line_color=(255, 255, 255), grid_color=(125,125,125)):
        super(Projection, self).__init__()
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Object display")
        self.background = (0, 0, 0)
        self.vectors = []
        self.displayPoints = True
        self.displayGridLines = True
        self.displayLines = True
        self.point_color = point_color
        self.line_color = line_color
        self.grid_line_color = grid_color
        self.nodeRadius = 2
        self.center = (int(self.width/2), int(self.height/2))

    def set_grid(self, grid):
        self.grid = grid

    def display(self):
        """ Draw the objects on the screen. """
        self.screen.fill(self.background)
        #display the grid
        if self.displayGridLines:
            for i in range(len(self.grid)):
                pygame.draw.aaline(self.screen, self.grid_line_color, (self.grid[i][0], self.grid[i][1]), (self.grid[i][0]+int(self.width/10), self.grid[i][1]), 1)
                pygame.draw.aaline(self.screen, self.grid_line_color, (self.grid[i][0], self.grid[i][1]), (self.grid[i][0], self.grid[i][1]+int(self.height/10)), 1)

        if self.displayLines:
            for vector in self.vectors:
                pygame.draw.aaline(self.screen, self.line_color, self.center, (self.center[0]+vector[0]*20, self.center[1]+vector[1]*20), 1)

        # for thing in self.objects.values():
        #     # if thing.displayEdges:
        #     #     for edge in thing.edges:
        #     #         pygame.draw.aaline(self.screen, self.line_color, (edge.start.x, edge.start.y), (edge.end.x, edge.end.y), 1)
        #     for edge in thing.edges:
        #             pygame.draw.aaline(self.screen, thing.edge_color, (edge.start.x, edge.start.y), (edge.end.x, edge.end.y), 1)
        #     # if thing.displayNodes:
        #     #     for node in thing.nodes:
        #     #         pygame.draw.circle(self.screen, self.point_color, (int(node.x), int(node.y)), self.nodeRadius, 0)
        #     for node in thing.nodes:
        #         pygame.draw.circle(self.screen, thing.node_color, (int(node.x), int(node.y)), self.nodeRadius, 0)

    def run(self):
        """Create a pygame screen until it is closed."""
        # key_to_function = {
        #     pygame.K_LEFT:   (lambda x: x.rotateAll('Y', -0.1)),
        #     pygame.K_RIGHT:   (lambda x: x.rotateAll('Y', 0.1)),
        #     pygame.K_UP:   (lambda x: x.rotateAll('X', -0.1)),
        #     pygame.K_DOWN:   (lambda x: x.rotateAll('X', 0.1)),
        #     pygame.K_q:   (lambda x: x.rotateAll('Z', -0.1)),
        #     pygame.K_e:   (lambda x: x.rotateAll('Z', 0.1)),
        #     pygame.K_d:  (lambda x: x.move_all('x',  10)),
        #     pygame.K_a:   (lambda x: x.move_all('x', -10)),
        #     pygame.K_s:   (lambda x: x.move_all('y',  10)),
        #     pygame.K_w:     (lambda x: x.move_all('y', -10)),
        #     pygame.K_LSHIFT: (lambda x: x.scaleAll(1.25)),
        #     pygame.K_LCTRL:  (lambda x: x.scaleAll( 0.8))
        # }
        done = False
        while not done:
            # keys = pygame.key.get_pressed()
            # for key in key_to_function.keys():
            #     if keys[key]:
            #         key_to_function[key](self)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
            pygame.time.delay(100)
            self.display()
            pygame.display.flip()
        return done

    def transform(self, matrix):
        type(self.vectors)
        vectors = matrix.transform(self.vectors, False)

    def add_vector(self, vector):
        self.vectors.append(vector)

M = [[1, 2, 3], [3, 7, 2], [4, 3, 5]]
T = Transformation(M)
v = [1, 2, 5]
# T.print_T()
# v = T.transform(v, False)
test = Projection(size, size)
test.set_grid(Base_grid)
test.add_vector(v)
test.transform(T)
test.run()
