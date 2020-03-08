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

class Object(object):
    def __init__(self, node_color=(0,0,0), edge_color=(125,125,125), nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        self.node_color = node_color
        self.edge_color = edge_color

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
                setattr(node, axis, getattr(node, axis) + d)
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

# nodes = [
#     Node(10, 10, 10),
#     Node(20, 10, 10),
#     Node(10, 20, 10),
#     Node(20, 20, 10),
#     Node(10, 10, 20),
#     Node(20, 10, 20),
#     Node(10, 20, 20),
#     Node(20, 20, 20)
# ]
#
# edges = [
#     Edge(nodes[0], nodes[1]),
#     Edge(nodes[0], nodes[2]),
#     Edge(nodes[3], nodes[1]),
#     Edge(nodes[3], nodes[2]),
#
#     Edge(nodes[4], nodes[5]),
#     Edge(nodes[4], nodes[6]),
#     Edge(nodes[7], nodes[5]),
#     Edge(nodes[7], nodes[6]),
#
#     Edge(nodes[4], nodes[0]),
#     Edge(nodes[5], nodes[1]),
#     Edge(nodes[6], nodes[2]),
#     Edge(nodes[7], nodes[3])
#
# ]
#
# cube = Object(nodes, edges)

#cube
# cube_nodes = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
# cube_edges = [(n,n+4) for n in range(0,4)] + [(n,n+1) for n in range(0,8,2)] + [(n,n+2) for n in (0,1,4,5)]

# cube2 = Object(cube_nodes, cube_edges)
