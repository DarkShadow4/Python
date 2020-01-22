import sys

movements={
    "U":"j -= 1",
    "D":"j += 1",
    "L":"i -= 1",
    "R":"i += 1"
}


def dibuja_lab(size, route):
    maze = [["o" for i in range(size)] for i in range(size)]
    global i
    global j
    i = 1
    j = 1
    maze[j][i] = "x"
    for step in route:
        exec(movements[step], globals())
        maze[j][i] = "x"
    return(maze)

def muestra(maze):
    for fila in maze:
        for item in fila:
            print(item, end=" ")
        print("\n", end="")

def getdims(route):
    for i in range(len(route)):
        if route[i:i+2] == ["R", "L"]: # 0 1 || 1 2 || 2 len
            if i == 0:
                route = ["S"] + route[i+2::]
            else:
                route = route[:i+1] + ["S"] + route[i+2::]
        print(route)
    print("\nFINAL route for size: {0}".format(route))
    size = route.count("R")
    return(size)

route = [item for item in sys.argv[1::]]
size = getdims(route)
print (size)
# maze = dibuja_lab(size, route)

# muestra(maze)

# Ruta lab_prueba_dibujo: R L U R R D D L L D D D R L U U U R D D R D R L U L U U R D R D U L U R R D D D R U D L U U U U U R D R D L D R D D R
