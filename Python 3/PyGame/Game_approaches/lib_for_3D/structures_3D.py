import pygame, math

class Node(object):
    def __init__(self, x, y, z):
        super(Node, self).__init__()
        self.x = x
        self.y = y
        self.z = z

class Edge(object):
    def __init__(self, node1, node2):
        super(Edge, self).__init__()
        self.start = node1
        self.end = node2

class Plane(object):
    """docstring for Plane."""

    def __init__(self, **definition): # {"points":[None, None, None], "normal":None, "ecuation":None}
        super(Plane, self).__init__()
        if definition["equation"] != None:
            self.equation = definition["equation"]
            x, y, z, d = self.equation.split()
            # x
            if x == "x":
                x = 1
            elif x == "-x":
                x = -1
            else:
                x = x[:-1]
                if x[0] == "+":
                    x = int(x[1::])
                else:
                    x = int(x)
            # y
            if y == "+y":
                y = 1
            elif y == "-y":
                y = -1
            else:
                y = y[:-1]
                if y[0] == "+":
                    y = int(y[1::])
                else:
                    y = int(y)
            # z
            if z == "+z":
                z = 1
            elif z == "-z":
                z = -1
            else:
                z = z[:-1]
                if z[0] == "+":
                    z = int(z[1::])
                else:
                    z = int(z)
            # d
            if d[0] == "+":
                d = int(d[1::])
            else:
                d = int(d)
            self.d = d
            self.normal = Vector(x, y, z)
        elif definition["points"][0] != None and definition["normal"] != None:
            self.points = [point for point in definition["points"] if point != None]
            self.normal = definition["normal"]
            self.equation = self.find_equation(1)
        elif None not in definition["points"][:2]:
            self.points = [point for point in definition["points"] if point != None]
            self.find_equation(0)
        else:
            print("Not enough arguments")

    def find_equation(self, type):
        if type == 0:
            d1 = vec_A_to_B(self.points[0], self.points[1])
            d2 = vec_A_to_B(self.points[0], self.points[2])
            self.normal = vec_v1xv2(d1, d2)

        d = -self.normal.x*self.points[0].x-self.normal.y*self.points[0].y-self.normal.z*self.points[0].z

        equation = "{0}".format(self.normal.x)

        if self.normal.y > 0:
            equation += " +{0}".format(self.normal.y)
        elif self.normal.y < 0:
            equation += " {0}".format(self.normal.y)
        else:
            equation += " +0"


        if self.normal.z > 0:
            equation += " +{0}".format(self.normal.z)
        elif self.normal.z < 0:
            equation += " {0}".format(self.normal.z)
        else:
            equation += " +0"

        if d > 0:
            equation += " +{0}".format(d)
        elif d < 0:
            equation += " {0}".format(d)
        else:
            equation += " +{0}"

        self.equation = equation



class Vector(object):
    """Objeto que son vectores"""

    def __init__(self, x, y, z):
        super(Vector, self).__init__()
        self.x = x
        self.y = y
        self.z = z
        self.actualizar_modulo()

    def actualizar_modulo(self):
        if self.x == self.y == self.z == 0:
            self.modulo = 0
            self.ux = 0
            self.uy = 0
            self.uz = 0
        else:
            self.modulo = ((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
            self.ux = 20*(self.x/self.modulo)
            self.uy = 20*(self.y/self.modulo)
            self.uz = 20*(self.z/self.modulo)

class Object(object):
    def __init__(self, nodes=[], edges=[], node_color=(0,0,0), edge_color=(125,125,125), containter_center=None):
        self.nodes = nodes
        self.edges = edges
        self.node_color = node_color
        self.edge_color = edge_color
        self.containter_center = containter_center

    def add_nodes(self, nodes):
        for node in nodes:
            if node not in self.nodes:
                self.nodes.append(node)
    def add_edges(self, edges):
        for edge in edges:
            if edge not in self.edges:
                self.edges.append(edge)
    def remove_node(self, node):
        if node in self.nodes:
            del self.nodes[self.nodes.index(node)]
    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges[self.edges.index(edge)]
    def Show_components(self):
        if len(self.nodes) > 0:
            for i, node in enumerate(self.nodes):
                print("Node {0} in ({1}, {2}, {3})".format(i, node.x, node.y, node.z))
        else:
            print("No nodes in this object")
        if len(self.edges) > 0:
            for i, edge in enumerate(self.edges):
                print("Edge {0} goes from ({1}, {2}, {3}) to ({4}, {5}, {6})".format(i, edge.start.x, edge.start.y, edge.start.z, edge.end.x, edge.end.y, edge.end.z))
        else:
            print("No edges in this object")
    def move(self, axis, d):
        if axis in ["x", "y", "z"]:
            for node in self.nodes:
                z = node.z
                setattr(node, axis, getattr(node, axis) + d)
                z -= node.z
                if z == 0 and axis == "z":
                    node.z += d
    def scale(self, centre, scale):
        """ Scale the wireframe from the centre of the screen. """
        centre_x, centre_y = centre
        for node in self.nodes:
            node.x = centre_x + scale * (node.x - centre_x)
            node.y = centre_y + scale * (node.y - centre_y)
            node.z *= scale

    def get_centre(self):
        """Returns the centre of the object"""
        n_nodes = len(self.nodes)
        centre_x = int(sum(node.x for node in self.nodes)/n_nodes)
        centre_y = int(sum(node.y for node in self.nodes)/n_nodes)
        centre_z = int(sum(node.z for node in self.nodes)/n_nodes)
        return(centre_x, centre_y, centre_z)

    def rotateX(self, centre, radians):
        centre_x, centre_y, centre_z = centre
        for node in self.nodes:
            y = node.y-centre_y
            z = node.z-centre_z
            d = math.hypot(y, z)
            theta = math.atan2(y, z) + radians
            node.y = centre_y + d*math.sin(theta)
            node.z = centre_z + d*math.cos(theta)

    def rotateY(self, centre, radians):
        centre_x, centre_y, centre_z = centre
        for node in self.nodes:
            x = node.x-centre_x
            z = node.z-centre_z
            d = math.hypot(x, z)
            theta = math.atan2(x, z) + radians
            node.x = centre_x + d*math.sin(theta)
            node.z = centre_z + d*math.cos(theta)

    def rotateZ(self, centre, radians):
        centre_x, centre_y, centre_z = centre
        for node in self.nodes:
            x = node.x-centre_x
            y = node.y-centre_y
            d = math.hypot(y, x)
            theta = math.atan2(y, x) + radians
            node.x = centre_x + d*math.cos(theta)
            node.y = centre_y + d*math.sin(theta)

def vec_A_to_B(node1, node2):
    return(Vector(node2.x - node1.x, node2.y - node1.y, node2.z - node1.z))

def vec_v1xv2(v1, v2):
    """
    |   i    j    k| x = ((v1.y*v2.z)-(v1.z*v2.y))
    |v1.x v1.y v1.z| y = -((v1.x*v2.z)-(v1.z*v2.x))
    |v2.x v2.y v2.z| z = ((v1.x*v2.y)-(v1.y*v2.x))
    """
    x = ((v1.y*v2.z)-(v1.z*v2.y))
    y = -((v1.x*v2.z)-(v1.z*v2.x))
    z = ((v1.x*v2.y)-(v1.y*v2.x))
    resultado = Vector(x, y, z)
    return(resultado)
