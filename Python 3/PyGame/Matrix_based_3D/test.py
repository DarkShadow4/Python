import sys, os
sys.path.append(os.getcwd())
import entities, viewer
import numpy as np
cube = entities.Entity(node_color=(255, 255, 255))
cube_nodes = [(x, y, z) for x in (-75, 75) for y in (-75, 75) for z in (-75, 75)]
cube.addNodes(np.array(cube_nodes))
cube.addEdges([(n, n + 4) for n in range(0, 4)])
cube.addEdges([(n, n + 1) for n in range(0, 8, 2)])
cube.addEdges([(n, n + 2) for n in (0, 1, 4, 5)])

plain = entities.Entity(node_color=(255, 255, 255))
plain_nodes = [(x, y, z) for x in (0, 150) for y in (0, 150) for z in (0,)]
plain_edges = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
plain.addNodes(np.array(plain_nodes))
plain.addEdges(plain_edges)

yes = viewer.Viewer(500, 500)
yes.addObjects([cube])
# yes.addObjects([plain])
yes.run()
