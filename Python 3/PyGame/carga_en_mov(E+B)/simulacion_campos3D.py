import pygame, math, projections3D, structures_3D
class Space(projections3D.Projection):
    def __init__(self, width, height):
        super(Space, self).__init__(width, height)

    def move_all(self, axis, d):
        if axis in ["x", "y", "x"]:
            pos_particula = self.objects["particula"].posicion
            for thing_name, thing in self.objects.keys(), self.objects.values():
                if "particula" != thing_name:
                    thing.move(axis, d, pos_particula)
                    thing.update(pos_particula)

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
            self.ux = 5*(x/self.modulo)
            self.uy = 5*(y/self.modulo)
            self.uz = 5*(z/self.modulo)

class E(structures_3D.Object):
    """Electrostatic field"""
    def __init__(self, nodes=[], edges=[]):
        super(E, self).__init__()
        # self.nodes = nodes
        # self.edges = edges

    def generate_nodes(self, size):
        for x in range(10, size, int(size/5)):
            for y in range(10, size, int(size/5)):
                for z in range(10, size, int(size/5)):
                    self.nodes.append(structures_3D.Node(x, y, z))

    def generate_edges(self, vect_end):
        pass
        # for node in self.nodes:
        #     vector = Vec_A2B(node, vect_end)
        #     self.edges.append(structures_3D.Edge(node, structures_3D.Node(node.x+vector.ux, node.y+vector.uy, node.z+vector.uz)))

    def move(self, axis, d, pos_particula):
        super(E, self).move(axis, d)
        self.update(pos_particula)

    def update(self, vect_end):
        self.edges =[]
        for node in self.nodes:
            vector = Vec_A2B(node, vect_end)
            self.edges.append(structures_3D.Edge(node, structures_3D.Node(node.x+vector.ux, node.y+vector.uy, node.z+vector.uz)))

class Linea_de_campo(object):
    """docstring for Linea_de_campo."""

    def __init__(self, p1, p2):
        super(Linea_de_campo, self).__init__()
        self.p1 = p1
        self.p2 = p2

class Particula(structures_3D.Object):
    """docstring for particula."""

    def __init__(self, carga, posicion, velocidad):
        super(Particula, self).__init__()
        self.carga = carga
        self.posicion = posicion
        self.velocidad = velocidad

    def dibujar(self):
        pygame.draw.circle(canvas, (0, 0, 255), (self.posicion.x, self.posicion.y), 10, 1)

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
    "B":(0, 255, 0),
    "E":(0, 255, 255),
    "velocidad":(255, 0, 0)
}


pygame.init()
size = 1000
espacio = Space(size, size)
# canvas = pygame.display.set_mode([size, size])

# particula
posicion = structures_3D.Node(500, 500, 500)

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

campo_E = E()
campo_E.generate_nodes(size)
campo_E.generate_edges(particula.posicion)
espacio.add_object("particula", particula)
espacio.add_object("E", campo_E)

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
