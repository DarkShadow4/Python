# Shadows
import pygame, projections3D, structures_3D

size = 1000
class World(projections3D.Projection):
    """docstring for World."""

    def __init__(self, width, height, background=(255, 255, 255), floor=None):
        super(World, self).__init__(width, height)
        self.background = background
        self.floor = floor

    def project_all_shadows(self):
        for thing in self.objects.values():
            if thing.shadow:
                thing.shadow.project_on_surface(self.floor)

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

            if self.floor != None:
                self.project_all_shadows()

            pygame.time.delay(100)
            self.display()
            pygame.display.flip()
        pygame.quit()
        return done

    def display(self):
        """ Draw the objects on the screen. """
        self.screen.fill(self.background)
        for thing in self.objects.values():
            for edge in thing.edges:
                    pygame.draw.aaline(self.screen, thing.edge_color, (edge.start.x, edge.start.y), (edge.end.x, edge.end.y), 1)
            for node in thing.nodes:
                pygame.draw.circle(self.screen, thing.node_color, (int(node.x), int(node.y)), self.nodeRadius, 0)

            for node in thing.shadow.nodes:
                pygame.draw.circle(self.screen, thing.shadow.color, (int(node.x), int(node.y)), self.nodeRadius, 0)


class Mat_object(structures_3D.Object):
    """docstring for Mat_object."""

    def __init__(self, nodes=[], edges=[], node_color=(0,0,0), edge_color=(125,125,125), shadow=True):
        super(Mat_object, self).__init__(nodes, edges, node_color=(0,0,0), edge_color=(125,125,125))
        if shadow:
            shadow_color = (0, 0, 0)
            self.shadow = Shadow(self, shadow_color)



class Shadow(object):
    """docstring for Shadow."""

    def __init__(self, thing, shadow_color=(0, 0, 0)):
        """Given the object initializes its shadow"""
        # First i will have the second object being a static flat floor
        super(Shadow, self).__init__()
        self.thing = thing
        self.color = shadow_color
        self.shadow = structures_3D.Object([], [], shadow_color)
        self.nodes = []

    def project_on_surface(self, surface, plain=True):
        """Given a surface"""
        self.nodes = []
        if plain:
            for node in self.thing.nodes:
                # hallo el punto node' en superficie surface con la ecuación de la recta (x, y, z) = (node.x, node.y, node.z) + lambda(n.x, n.y, n.z)
                l = (- surface.normal.x*node.x - surface.normal.y*node.y - surface.normal.z*node.z - surface.d)/(surface.normal.x**2 + surface.normal.y**2 + surface.normal.z**2)
                self.nodes.append(structures_3D.Node(node.x+surface.normal.x*l, node.y+surface.normal.y*l, node.z+surface.normal.z*l))



world = World(size, size, (255, 255, 255), structures_3D.Plane(equation="0x +y +z -100")) # structures_3D.Plane(equation="x+0+z=0")
cube_nodes = [structures_3D.Node(x, y, z) for x in (0, 50) for y in (0, 50) for z in (0, 50)]

# for node in cube_nodes:
#     print("x: {0} y: {1} z: {2}".format(node.x, node.y, node.z))

edges = [(cube_nodes[n],cube_nodes[n+4]) for n in range(0,4)] + [(cube_nodes[n],cube_nodes[n+1]) for n in range(0,8,2)] + [(cube_nodes[n],cube_nodes[n+2]) for n in (0,1,4,5)]
cube_edges = []
for edge in edges:
    cube_edges.append(structures_3D.Edge(edge[0], edge[1]))

cube = Mat_object(cube_nodes, cube_edges)
world.add_object("cube", cube)
world.run()
