import pygame, math, projections3D, structures_3D
# import dill

class Space(projections3D.Projection):
    def __init__(self, width, height, profundity):
        super(Space, self).__init__(width, height)
        self.profundity = profundity

    def find_common_centre(self):
        centres = []
        for thing in self.objects.values():
            centres.append(thing.get_centre())
        centre_x = sum(centres[0])/len(centres[0])
        centre_y = sum(centres[1])/len(centres[1])
        centre_z = sum(centres[2])/len(centres[2])
        return(centre_x, centre_y, centre_z)

    def move_all(self, axis, d):
        if axis in ["x", "y", "x"]:
            for thing_name in self.objects.keys():
                self.objects[thing_name].move(axis, d)

    def move_particle(self, axis, d):
        self.objects["particula"].move(axis, d)
        # if axis in ["x", "y", "x"]:
        #     self.objects["particula"].move(axis, d)

    def rotateAll(self, axis, theta):
        """ Rotate all thing about their centre, along a given axis by a given angle. """
        rotateFunction = 'rotate' + axis
        for thing in self.objects.values():
            # centre = self.find_common_centre()
            centre = (self.width/2, self.height/2, self.profundity/2)
            getattr(thing, rotateFunction)(centre, theta)

    def update_lines(self):
        pos_particula = self.objects["particula"].posicion
        for thing in self.objects.values():
            if "update" in dir(thing):
                thing.update(pos_particula, self.objects["particula"])

    def invert_particle_charge(self):
         self.objects["particula"].carga = -self.objects["particula"].carga

    def print_all_centres(self):
        for thing in self.objects.values():
            centre = thing.get_centre()
            print("({0}, {1}, {2})".format(centre[0], centre[1], centre[2]))
        print()


    def run(self):
        """Create a pygame screen until it is closed."""
        key_to_function = {
            # Keymap for the field rotations:
            pygame.K_KP8:   (lambda x: x.rotateAll('X', 0.1)),                  # numpad 8: rotate x wise clockwise (right)
            pygame.K_KP4:   (lambda x: x.rotateAll('Y', 0.1)),                  # numpad 4: rotate y wise clockwise (left)
            pygame.K_KP2:   (lambda x: x.rotateAll('X', -0.1)),                 # numpad 2: rotate x wise anti-clockwise (down)
            pygame.K_KP6:   (lambda x: x.rotateAll('Y', -0.1)),                 # numpad 6: rotate y wise anti-clockwise (right)
            pygame.K_KP7:   (lambda x: x.rotateAll('Z', -0.1)),                 # numpad 7: rotate z wise anti-clockwise (left)
            pygame.K_KP9:   (lambda x: x.rotateAll('Z', 0.1)),                  # numpad 9: rotate z wise clockwise (right)

            # Zooming
            pygame.K_RSHIFT:   (lambda x: x.scaleAll(1.25)),               # right shift: zoom +
            pygame.K_RCTRL:   (lambda x: x.scaleAll(0.8)),                # right ctrl: zoom -

            # Keymap for the field translations:
            pygame.K_LEFT:   (lambda x: x.move_all('x', -10)),
            pygame.K_RIGHT: (lambda x: x.move_all('x',  10)),
            pygame.K_UP:   (lambda x: x.move_all('y', -10)),
            pygame.K_DOWN:   (lambda x: x.move_all('y', 10)),

            # Keymap for the particle translations:
            # pygame.K_q:   (lambda x: x.rotateAll('Z', -0.1)),
            # pygame.K_e:   (lambda x: x.rotateAll('Z', 0.1)),
            pygame.K_d:  (lambda x: x.move_particle('x',  10)),      # change to move only the particle
            pygame.K_a:   (lambda x: x.move_particle('x', -10)),     # change to move only the particle
            pygame.K_s:   (lambda x: x.move_particle('y',  10)),     # change to move only the particle
            pygame.K_w:     (lambda x: x.move_particle('y', -10)),   # change to move only the particle
            pygame.K_LSHIFT: (lambda x: x.move_particle('z', 10)),      # change to move only the particle
            pygame.K_LCTRL:  (lambda x: x.move_particle('z', -10)),       # change to move only the particle

            pygame.K_SPACE:  (lambda x: x.print_all_centres())       # change to move only the particle
        }
        done = False
        while not done:
            keys = pygame.key.get_pressed()
            self.objects["particula"].velocidad = Vector(10*keys[pygame.K_d]-10*keys[pygame.K_a], 10*keys[pygame.K_s]-10*keys[pygame.K_w], 10*keys[pygame.K_LSHIFT]-10*keys[pygame.K_LCTRL])
            for key in key_to_function.keys():
                if keys[key]:
                    key_to_function[key](self)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    if event.key == pygame.K_TAB:
                        self.invert_particle_charge()

            pygame.time.delay(100)
            self.update_lines()
            self.display()
            pygame.display.flip()
        return done




class Vector(object):
    """Objeto que son vectores"""

    def __init__(self, x, y, z):
        super(Vector, self).__init__()
        self.x = x
        self.y = y
        self.z = z
        if x == y == z == 0:
            self.modulo = 0
            self.ux = 0
            self.uy = 0
            self.uz = 0
        else:
            self.modulo = ((x**2)+(y**2)+(z**2))**(1/2)
            self.ux = 20*(x/self.modulo)
            self.uy = 20*(y/self.modulo)
            self.uz = 20*(z/self.modulo)

class E(structures_3D.Object):
    """Electrostatic field"""
    def __init__(self, node_color = (0, 100, 150), edge_color = (0, 255, 255), nodes=[], edges=[]):
        super(E, self).__init__(nodes, edges, node_color, edge_color)
        # self.nodes = nodes
        # self.edges = edges

    def generate_nodes(self, size):
        for x in range(200, size, int(size/5)):
            for y in range(200, size, int(size/5)):
                for z in range(200, size, int(size/5)):
                    self.nodes.append(structures_3D.Node(x, y, z)) # -(size/2)

    def move(self, axis, d):
        super(E, self).move(axis, d)

    def update(self, vect_end, particle):
        self.edges =[]
        for node in self.nodes:
            vector = Vec_A2B(node, vect_end)
            vector.x, vector.y, vector.z = vector.x*(particle.carga/((particle.carga**2)**1/2)), vector.y*(particle.carga/((particle.carga**2)**1/2)), vector.z*(particle.carga/((particle.carga**2)**1/2))
            start = structures_3D.Node(node.x, node.y, node.z)
            end = structures_3D.Node(start.x+vector.ux, start.y+vector.uy, start.z+vector.uz)
            edge = structures_3D.Edge(start, end)
            self.edges.append(edge)
        # print("de ({0}, {1}, {2}) a ({3}, {4}, {5})".format(start.x, start.y, start.z, end.x, end.y, end.z))
        # print("vector ({0}, {1}, {2}) vector unitario ({3}, {4}, {5})".format(vector.x, vector.y, vector.z, vector.ux, vector.uy, vector.uz))

class B(structures_3D.Object):
    """Magnetic field"""
    def __init__(self, node_color = (0, 100, 0), edge_color = (0, 255, 0), nodes=[], edges=[]):
        super(B, self).__init__(nodes, edges, node_color, edge_color)
        # self.nodes = nodes
        # self.edges = edges

    def generate_nodes(self, size):
        for x in range(200, size, int(size/5)):
            for y in range(200, size, int(size/5)):
                for z in range(200, size, int(size/5)):
                    self.nodes.append(structures_3D.Node(x, y, z)) # -(size/2)

    def move(self, axis, d):
        super(B, self).move(axis, d)

    def update(self, vect_end, particle):
        self.edges =[]
        carga = particle.carga
        velocidad = particle.velocidad
        for node in self.nodes:
            radio = Vec_A2B(node, vect_end)
            start = structures_3D.Node(node.x, node.y, node.z)
            vector = q__v1xv2(radio, velocidad, carga)
            end = structures_3D.Node(start.x+vector.ux, start.y+vector.uy, start.z+vector.uz)
            edge = structures_3D.Edge(start, end)
            self.edges.append(edge)


class Linea_de_campo(object):
    """docstring for Linea_de_campo."""

    def __init__(self, p1, p2):
        super(Linea_de_campo, self).__init__(node_color = (10, 255, 255), edge_color = (0, 255, 255))
        self.p1 = p1
        self.p2 = p2

class Particula(structures_3D.Object):
    """docstring for particula."""

    def __init__(self, carga, posicion, velocidad):
        super(Particula, self).__init__(node_color=(0, 0, 255), edge_color=(200, 200, 200))
        self.carga = carga
        self.posicion = posicion
        self.nodes = [posicion] # El segundo nodo es la punta del vector velocidad, como empieza en reposo no tiene velocidad
        self.velocidad = velocidad

    def update(self, vect_end, particle):
        self.edges = [structures_3D.Edge(self.posicion, structures_3D.Node(self.posicion.x+self.velocidad.ux, self.posicion.y+self.velocidad.uy, self.posicion.z+self.velocidad.uz))]
        if self.carga > 0:
            self.node_color = (0, 0, 255)
        else:
            self.node_color = (255, 0, 0)

    def move(self, axis="", d=0):
        print("antes: ({0}, {1}, {2})".format(self.posicion.x, self.posicion.y, self.posicion.z))
        if axis in ["x", "y", "z"]:
            super(Particula, self).move(axis, d)
            # for node in self.nodes:
            #     setattr(node, axis, getattr(node, axis) + d)
        elif axis == "":
            for axis in ["x", "y", "z"]:
                for node in self.nodes:
                    setattr(node, axis, getattr(node, axis) + getattr(velocidad, axis))
        print("despues: ({0}, {1}, {2})".format(self.posicion.x, self.posicion.y, self.posicion.z))
    # def dibujar(self):
    #     if self.carga > 0:
    #         self.color = (0, 0, 255)
    #     else:
    #         self.color = (255, 0, 0)
    #     pygame.draw.circle(canvas, color, (self.posicion.x, self.posicion.y), 10, 1)

def q__v1xv2(v1, v2, carga):
    """
    |   i    j    k| x = ((v1.y*v2.z)-(v1.z*v2.y))
    |v1.x v1.y v1.z| y = -((v1.x*v2.z)-(v1.z*v2.x))
    |v2.x v2.y v2.z| z = ((v1.x*v2.y)-(v1.y*v2.x))
    """
    x = ((v1.y*v2.z)-(v1.z*v2.y))*(carga/abs(carga))
    y = -((v1.x*v2.z)-(v1.z*v2.x))*(carga/abs(carga))
    z = ((v1.x*v2.y)-(v1.y*v2.x))*(carga/abs(carga))
    resultado = Vector(x, y, z)
    return(resultado)

def Vec_A2B(A, B):
    vector = Vector((B.x-A.x), (B.y-A.y), (B.z-A.z))
    return(vector)

def dibujar_vector(P_aplicacion, vector, color=(255, 255, 255)):
    if vector.z == 0:
        pygame.draw.line(canvas, color, (P_aplicacion.x, P_aplicacion.y), (P_aplicacion.x+vector.ux, P_aplicacion.y+vector.uy))
    else:
        if vector.z > 0:
            pygame.draw.circle(canvas, color, (P_aplicacion.x, P_aplicacion.y), 2, 1)
            pygame.draw.circle(canvas, color, (P_aplicacion.x, P_aplicacion.y), 10, 1)
        else:
            pygame.draw.circle(canvas, color, (P_aplicacion.x, P_aplicacion.y), 10, 1)
            pygame.draw.line(canvas, color, (P_aplicacion.x-7, P_aplicacion.y-7), (P_aplicacion.x+7, P_aplicacion.y+7))
            pygame.draw.line(canvas, color, (P_aplicacion.x+7, P_aplicacion.y-7), (P_aplicacion.x-7, P_aplicacion.y+7))

colores = {
    "B_edges":(0, 255, 0),
    "B_nodes":(0, 100, 150),
    "E_edges":(0, 255, 255),
    "E_nodes":(150, 150, 255),
    "velocidad":(200, 200, 200)
}


pygame.init()
size = 1000
espacio = Space(size, size, size)
# canvas = pygame.display.set_mode([size, size])

# particula
posicion = structures_3D.Node(size/2, size/2, size/2)

carga=1.6*(10**-19)
particula = Particula(carga, posicion, Vector(0, 0, 0))
#

puntos_B = []
puntos_E = []
for x in range(1, size):
    for y in range(1, size):
        if x%100==0 and y%100==0:
            puntos_E.append(structures_3D.Node(x, y, 0))
        # if (x-50)%100 == 0 and (y-50)%100 == 0:
        #     puntos_B.append(structures_3D.Node(x-5, y-5, 0))

campo_E = E(colores["E_nodes"], colores["E_edges"])
campo_E.generate_nodes(size)
campo_B = B(colores["B_nodes"], colores["B_edges"])
campo_B.generate_nodes(size)

espacio.add_object("particula", particula)
espacio.add_object("E", campo_E)
espacio.add_object("B", campo_B)

espacio.run()
#
# done = False
# while not done:
#     pressed = pygame.key.get_pressed()
#     particula.velocidad = Vector((pressed[pygame.K_d]*5-pressed[pygame.K_a]*5), (pressed[pygame.K_s]*5-pressed[pygame.K_w]*5), pressed[pygame.K_LSHIFT]*5-pressed[pygame.K_LCTRL]*5)
#     if particula.velocidad.modulo > 0:
#         particula.posicion = structures_3D.Node(particula.posicion.x + particula.velocidad.x, particula.posicion.y + particula.velocidad.y, particula.posicion.z + (particula.velocidad.z)*0)
#     particula.dibujar()
#     # for p in puntos_E:
#     #     dibujar_vector(p, Vec_A2B(p, particula.posicion, True), colores["E"])
#     E.
#     for p in puntos_B:
#         if particula.velocidad.modulo > 0:
#             dibujar_vector(p, q__v1xv2(Vec_A2B(p, particula.posicion, True), particula.velocidad, particula.carga), colores["B"])
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_q:
#                 done = True
#             if event.key == pygame.K_TAB:
#                 particula.carga = -particula.carga
#
#
#
#     pygame.display.flip()
#     pygame.time.delay(100)
#     canvas.fill((0, 0, 0))
#     pygame.display.flip()
