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
    n = len(route)
    i = 0
    while i < n:

        if route[i:i+2] == ["R", "L"]: # 0 1 || 1 2 || 2 len
            print("R L => S")
            if i == 0:
                route = ["S"] + route[i+2::]
            else:
                route = route[:i+1] + ["S"] + route[i+2::]
            n = len(route) # actualizo la longitud
        print(route[i] != ["R"] and route[i] != ["L"])
        while 0 <= i < n and route[i] != ["R"] and route[i] != ["L"]:
            print("{0} => _".format(route[i]))
            if i == 0:
                route = route[i+1:]
            else:
                route = route[:i] + route[i+1::]
            n = len(route) # actualizo la longitud
        print(route)
        i += 1

    print("\nFINAL route for size: {0}".format(route))
    size = route.count("R")
    return(size)

route = [item for item in sys.argv[1::]]
size = getdims(route)
print (size)
# maze = dibuja_lab(size, route)

# muestra(maze)

# Ruta lab_prueba_dibujo: R L U R R D D L L D D D R L U U U R D D R D R L U L U U R D R D U L U R R D D D R U D L U U U U U R D R D L D R D D R
# ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
