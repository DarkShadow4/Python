import numpy as np

def translationMatrix(dx=0, dy=0, dz=0):
    return np.array([[1,  0,  0,  0],
                     [0,  1,  0,  0],
                     [0,  0,  1,  0],
                     [dx, dy, dz, 1]])

def scalingMatrix(sx=1, sy=1, sz=1):
    return np.array([[sx, 0,  0, 0],
                     [0, sy,  0, 0],
                     [0,  0, sz, 0],
                     [0,  0,  0, 1]])

def rotateXmatrix(radians):
    c = np.cos(radians)
    s = np.sin(radians)
    return np.array([[1, 0,  0, 0],
                     [0, c, -s, 0],
                     [0, s,  c, 0],
                     [0, 0,  0, 1]])

def rotateYmatrix(radians):
    c = np.cos(radians)
    s = np.sin(radians)
    return np.array([[ c, 0, s, 0],
                     [ 0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [ 0, 0, 0, 1]])

def rotateZmatrix(radians):
    c = np.cos(radians)
    s = np.sin(radians)
    return np.array([[c, -s, 0 ,0],
                     [s,  c, 0, 0],
                     [0,  0, 1, 0],
                     [0,  0, 0, 0]])


class Entity(object):
    """docstring for Entity."""

    def __init__(self, name="", type="", node_color=(0, 0, 0), edge_color=(255, 255, 255), node_radius=4):
        super(Entity, self).__init__()
        self.name = name
        self.type = type
        self.nodes = np.zeros((0, 4))
        self.node_color = node_color
        self.edge_color = edge_color
        self.node_radius = node_radius
        # self.nodes = np.zeros((0, 4))
        self.edges = []
####
        self.initial_nodes = np.zeros((0, 4))
        print("self.initial_nodes is self.nodes: {0}".format(self.initial_nodes is self.nodes))
        self.totalTransformations = {
        "T":[   [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]    ],

        "RX":[  [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]    ],

        "RY":[  [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]    ],

        "RZ":[  [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]    ],

        "S":[   [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]    ]
        }
####
    def addNodes(self, nodes):
        ones = np.ones((len(nodes), 1))
        nodes = np.hstack((nodes, ones))
####
        self.initial_nodes = np.vstack((self.initial_nodes, nodes))
        self.nodes = np.dot(self.initial_nodes, self.totalTransformations["RY"])
        # self.nodes = np.dot(self.nodes, self.totalTransformations["RY"])
        self.nodes = np.dot(self.nodes, self.totalTransformations["RX"])
        self.nodes = np.dot(self.nodes, self.totalTransformations["RZ"])
        self.nodes = np.dot(self.nodes, self.totalTransformations["T"])
        self.nodes = np.dot(self.nodes, self.totalTransformations["S"])

        # print("self.initial_nodes[0] is self.nodes[0]: {0}".format(self.initial_nodes[0] is self.nodes[0]))
####
        # self.nodes = np.vstack((self.nodes, nodes))


    def addEdges(self, edges):
        self.edges += edges

    def transform(self, matrix, type):
        self.totalTransformations[type] = np.dot(self.totalTransformations[type], matrix)
        self.nodes = np.dot(self.initial_nodes, self.totalTransformations["RY"])
        # self.nodes = np.dot(self.nodes, self.totalTransformations["RY"])
        self.nodes = np.dot(self.nodes, self.totalTransformations["RX"])
        self.nodes = np.dot(self.nodes, self.totalTransformations["RZ"])
        self.nodes = np.dot(self.nodes, self.totalTransformations["T"])
        self.nodes = np.dot(self.nodes, self.totalTransformations["S"])
