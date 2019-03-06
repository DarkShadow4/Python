def imprimir_tablero(tablero):
    print "-------------"
    for fila in tablero:
        for celda in fila:
            print "|", celda,
        print "|"
        print "-------------"

def comprobar_jugada(tablero, y, x, turno):
    """Comprueba si la jugada que se acaba de realizar es la correcta"""
    if tablero[y][x] == tablero[y][x-1] == tablero[y][x-2] == turno:
        print "Ha ganado", turno
        imprimir_tablero(tablero)
        return False
    else:
        if tablero[y][x] == tablero[y-1][x] == tablero[y-2][x] == turno:
            print "Ha ganado", turno
            imprimir_tablero(tablero)
            return False
        else:
            if (x+y)%2 == 0:
                if tablero[y][x] == tablero[y-1][x-1] == tablero[y-2][x-2] == turno:
                    print "Ha ganado", turno
                    imprimir_tablero(tablero)
                    return False
                else:
                    if tablero[y][x] == tablero[y-1][x-2] == tablero[y-2][x-4] == turno:
                        print "Ha ganado", turno
                        imprimir_tablero(tablero)
                        return False
            return True


tablero = []
for x in range(3):
    fila = []
    for y in range(3):
        fila.append(" ")
    tablero.append(fila)

c = True
jugador = 1
while c == True:
    imprimir_tablero(tablero)
    if jugador%2 == 0:
        turno = "x"
    else:
        turno = "o"
    print "Turno de", turno
    i = True
    while i == True:
        y = input("Introduce fila: ")
        x = input("introduce columna:")
        if tablero[y][x] != " ":
            print "Movimiento incorrecto"
        else:
            tablero[y][x] = turno
            i = False
    c = comprobar_jugada(tablero, y, x, turno)
    jugador += 1
