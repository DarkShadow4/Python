import sys

movements={
    "U":"""
    j += 1
    """,
    "D":"""
    j -= 1
    """,
    "L":"""
    i -= 1
    """,
    "R":"""
    i += 1
    """,
}

args = [item for item in sys.argv[1::]]
print(args)
if len(args) != 1:
    for step in args:
        print(step)

def dibuja_lab(size, route):
    maze = [["o"]*size]*size
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

muestra(dibuja_lab(7, "lll"))
