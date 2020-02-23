import pygame, math

class Punto(object):
    """docstring for Punto."""

    def __init__(self, x, y, z):
        super(Punto, self).__init__()
        self.x = x
        self.y = y
        self.z = z

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
            self.ux = 5*x/self.modulo
            self.uy = 5*y/self.modulo
            self.uz = 5*z/self.modulo


class Linea_de_campo(object):
    """docstring for Linea_de_campo."""

    def __init__(self, p1, p2):
        super(Linea_de_campo, self).__init__()
        self.p1 = p1
        self.p2 = p2

class Particula(object):
    """docstring for particula."""

    def __init__(self, carga, posicion, velocidad):
        super(Particula, self).__init__()
        self.carga = carga
        self.posicion = posicion
        self.velocidad = velocidad

    def dibujar(self):
        pygame.draw.circle(canvas, (0, 0, 255), (posicion.x, posicion.y), 10, 1)

def v1xv2(v1, v2):
    """
    |   i    j    k| x = ((v1.y*v2.z)-(v1.z*v2.y))
    |v1.x v1.y v1.z| y = -((v1.x*v2.z)-(v1.z*v2.x))
    |v2.x v2.y v2.z| z = ((v1.x*v2.y)-(v1.y*v2.x))
    """
    x = ((v1.y*v2.z)-(v1.z*v2.y))
    y = -((v1.x*v2.z)-(v1.z*v2.x))
    z = ((v1.x*v2.y)-(v1.y*v2.x))
    resultado = (x, y, z)
    return(resultado)

def Vec_A2B(A, B, unit=False):
    vector = Vector((B.x-A.x), (B.y-A.y), (B.z-A.z))
    return(vector)

def dibujar_vector(P_aplicacion, vector, color=(255, 255, 255)):
    if vector.z == 0:
        pygame.draw.line(canvas, color, (P_aplicacion.x, P_aplicacion.y), (P_aplicacion.x+vector.ux, P_aplicacion.y+vector.uy))
    else:
        if vector.z > 0:
            pygame.draw.circle(canvas, color, (P_aplicacion.x, P_aplicacion.y), 2, 1)
            pygame.draw.circle(canvas, color, (P_aplicacion.x, P_aplicacion.y), 3, 1)
        else:
            pygame.draw.circle(canvas, color, (P_aplicacion.x, P_aplicacion.y), 3, 1)
            pygame.draw.line(canvas, color, (P_aplicacion.x-1, P_aplicacion.y-1), (P_aplicacion.x+1, P_aplicacion.y+1))
            pygame.draw.line(canvas, color, (P_aplicacion.x+1, P_aplicacion.y-1), (P_aplicacion.x-1, P_aplicacion.y+1))


colores = {
    "B":(0, 255, 0),
    "E":(0, 255, 255),
    "velocidad":(255, 0, 0)
}


size = 1000
pygame.init()
canvas = pygame.display.set_mode([size, size])


posicion = Punto(100, 500, 0)
# posicion = Punto(math.ceil(size/2), math.ceil(size/2), 0)
carga=-1.6*(10**-19)
particula = Particula(carga, posicion, Vector(0, 0, 0))
# puntos_B = []
puntos_E = []
for x in range(1, size):
    for y in range(1, size):
        if x%150==0 and y%150==0:
            puntos_E.append(Punto(x, y, 0))
#         if (x-5)%10 == 0 and (y-5)%10 == 0:
#             puntos_E.append(Punto(x-5, y-5, 0))
#
# lineas_de_campo = []
# Del campo electrico
# for p in puntos_E:
#     lineas_de_campo.append(Linea_de_campo(p, particula.posicion))


done = False
while not done:
    particula.dibujar()
    for p in puntos_E:
        dibujar_vector(p, Vec_A2B(p, particula.posicion, True), colores["E"])
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
    pygame.display.flip()
