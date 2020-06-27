import inspect, sys, math
import lib_for_3D
pygame = lib_for_3D.projections3D.pygame

class Props(lib_for_3D.structures_3D.Object):
    def __init__(self, nodes=[], edges=[], node_color=(0,0,0), edge_color=(125,125,125), containter_center=None):
        super(Props, self).__init__(nodes, edges, node_color, edge_color, containter_center)

    def add_nodes(self, nodes):
        super(Props, self).add_nodes(nodes)

    def add_edges(self, edges):
        super(Props, self).add_edges(edges)

    def remove_node(self, node):
        super(Props, self).remove_node(node)

    def remove_edge(self, edge):
        super(Props, self).remove_edge(edge)

    def Show_components(self):
        super(Props, self).Show_components()

    def move(self, axis, d):
        super(Props, self).move(axis, d)

    def scale(self, centre, scale):
        """ Scale the wireframe from the centre of the screen. """
        super(Props, self).scale(centre, scale)

    def get_centre(self):
        """Returns the centre of the object"""
        super(Props, self).get_centre()

    def rotateX(self, centre, radians, sightline):
        centre_x, centre_y, centre_z = centre
        for node in self.nodes:
            y = node.y-centre_y
            z = node.z-centre_z
            d = math.hypot(y, z)
            theta = math.atan2(y, z) + radians
            node.y = centre_y + d*math.sin(theta)
            node.z = centre_z + d*math.cos(theta)

    def rotateY(self, centre, radians, sightline):
        centre_x, centre_y, centre_z = centre
        if sightline[1] != 0:
            self.rotateX(centre, -sightline[1], sightline)
        for node in self.nodes:
            x = node.x-centre_x
            z = node.z-centre_z
            d = math.hypot(x, z)
            theta = math.atan2(x, z) + radians
            node.x = centre_x + d*math.sin(theta)
            node.z = centre_z + d*math.cos(theta)
        if sightline[1] != 0:
            self.rotateX(centre, sightline[1], sightline)

    def rotateZ(self, centre, radians, sightline):
        centre_x, centre_y, centre_z = centre
        for node in self.nodes:
            x = node.x-centre_x
            y = node.y-centre_y
            d = math.hypot(y, x)
            theta = math.atan2(y, x) + radians
            node.x = centre_x + d*math.cos(theta)
            node.y = centre_y + d*math.sin(theta)

cubes = []
#cube 0 (Up Left)
vertexs = [lib_for_3D.structures_3D.Node(x, y, z) for x in (0, 50) for y in (0, 50) for z in (0, 50)]
edges = [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+4]) for n in range(0,4)] + [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+1]) for n in range(0,8,2)] + [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+2]) for n in (0,1,4,5)]
cubes.append(Props(nodes=vertexs, edges=edges))
#cube 1 (Up Right)
vertexs = [lib_for_3D.structures_3D.Node(x, y, z) for x in (450, 500) for y in (0, 50) for z in (0, 50)]
edges = [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+4]) for n in range(0,4)] + [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+1]) for n in range(0,8,2)] + [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+2]) for n in (0,1,4,5)]
cubes.append(Props(nodes=vertexs, edges=edges))
#cube 2 (Bottom Left)
vertexs = [lib_for_3D.structures_3D.Node(x, y, z) for x in (0, 50) for y in (450, 500) for z in (0, 50)]
edges = [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+4]) for n in range(0,4)] + [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+1]) for n in range(0,8,2)] + [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+2]) for n in (0,1,4,5)]
cubes.append(Props(nodes=vertexs, edges=edges))
#cube 3 (Bottom Right)
vertexs = [lib_for_3D.structures_3D.Node(x, y, z) for x in (450, 500) for y in (450, 500) for z in (0, 50)]
edges = [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+4]) for n in range(0,4)] + [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+1]) for n in range(0,8,2)] + [lib_for_3D.structures_3D.Edge(vertexs[n],vertexs[n+2]) for n in (0,1,4,5)]
cubes.append(Props(nodes=vertexs, edges=edges))


# print(inspect.getsource(lib_for_3D.projections3D.structures_3D.Object.rotateY))


# print(inspect.getsource(lib_for_3D.projections3D.structures_3D.Object))


class GAMR(lib_for_3D.projections3D.Projection):
    """docstring for GAMR."""

    def __init__(self, width, height, sensibility):
        self.objects = {}
        super(GAMR, self).__init__(width, height)
        self.center = (self.width//2, self.height//2, 0)
        self.sensibility = sensibility
        self.sightline = [0, 0]

    def display(self):
        """ Draw the objects on the screen. """
        self.screen.fill(self.background)
        for name, thing in self.objects.items():
            if "surface_" in name:
                pygame.draw.polygon(self.screen, (255, 255, 255), [(node.x, node.y) for node in thing.nodes])
            else:
                for edge in thing.edges:
                    pygame.draw.aaline(self.screen, thing.edge_color, (edge.start.x, edge.start.y), (edge.end.x, edge.end.y), 1)
                for node in thing.nodes:
                    pygame.draw.circle(self.screen, thing.node_color, (int(node.x), int(node.y)), self.nodeRadius, 0)




    def run(self):
        """Create a pygame screen until it is closed."""
        pygame.mouse.set_visible(False)
        key_to_function = {
            pygame.K_LEFT:   (lambda x: x.rotateAll('Y', -0.1)),
            pygame.K_RIGHT:   (lambda x: x.rotateAll('Y', 0.1)),
            pygame.K_UP:   (lambda x: x.rotateAll('X', -0.1)),
            pygame.K_DOWN:   (lambda x: x.rotateAll('X', 0.1)),
            pygame.K_q:   (lambda x: x.rotateAll('Z', -0.1)),
            pygame.K_e:   (lambda x: x.rotateAll('Z', 0.1)),
            pygame.K_d:  (lambda x: x.move_all('x', -10)),
            pygame.K_a:   (lambda x: x.move_all('x', 10)),
            pygame.K_s:   (lambda x: x.move_all('z', 10)),
            pygame.K_w:     (lambda x: x.move_all('z', -10)),
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
                        # pygame.event.get()

            self.track_mouse()
            self.move_camera()
            pygame.time.delay(100)
            self.display()
            pygame.display.flip()
        return done

    def add_object(self, name, thing):
        thing.containter_center = self.center
        self.objects[name] = thing

    def add_surface(self, name, thing):
        thing.containter_center = self.center
        self.objects["surface_" + name] = thing

    def move_all(self, axis, d):
        super(GAMR, self).move_all(axis, d)

    def scaleAll(self, scale):
        super(GAMR, self).scaleAll(scale)

    def rotateAll(self, axis, theta):
        """ Rotate all thing about their centre, along a given axis by a given angle. """
        rotateFunction = 'rotate' + axis
        for thing in self.objects.values():
            centre = thing.get_centre() if thing.containter_center == None else thing.containter_center
            getattr(thing, rotateFunction)(centre, theta, self.sightline)



    def track_mouse(self):
        self.rel_mouse_pos = (0, 0)
        if pygame.mouse.get_focused():
            mouse_pos = pygame.mouse.get_pos()
            self.rel_mouse_pos = (mouse_pos[0]-self.center[0], mouse_pos[1]-self.center[1])
            pygame.mouse.set_pos(self.center[0], self.center[1])

    def move_camera(self):
        angle = [-self.sensibility*2*self.rel_mouse_pos[0]/self.width, -self.sensibility*2*self.rel_mouse_pos[1]/self.height]
        self.sightline[0] += angle[0]

        if -1.5 < self.sightline[1]+angle[1] < 1.5:
            self.sightline[1] += angle[1]
        else:
            angle[1] = 0


        for axis, theta in zip(["Y", "X"], angle):
            self.rotateAll(axis, theta)

sensibility = 0.5
game = GAMR(500, 500, sensibility)

test_surface = Props(nodes = [])
test_surface.add_nodes([lib_for_3D.structures_3D.Node(0, 0, 0), lib_for_3D.structures_3D.Node(500, 0, 0), lib_for_3D.structures_3D.Node(500, 500, 0), lib_for_3D.structures_3D.Node(0, 500, 0)])

game.add_object("cube0", cubes[0])
game.add_object("cube1", cubes[1])
game.add_object("cube2", cubes[2])
game.add_object("cube3", cubes[3])
game.add_surface("test", test_surface)
# print(inspect.getsource(lib_for_3D.projections3D.Projection))
game.run()
pygame.quit()
