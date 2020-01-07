#Eric Ayllon Palazon
import random
def construir_tablero():
    """Funcion que construye el tablero"""
    n = input("Introduce n:")
    tablero = []
    for y in range(n): #creo una matriz para el tablero
        fila = []
        for x in range(n):
            fila.append(0)
        tablero.append(fila)
    return tablero, n

def mostrar_tablero(tablero):
    """Funcion que muestra el tablero"""
    for fila in tablero:
        print "",
        for i in range(len(fila)):
            print "-"*3, " ",
        print ""
        for celda in fila:
            print "|",
            if celda == 0:
                print " ",
            elif celda == 1:
                print "X",
            else:
                print "O",
            print "|",
        print ""
    print "",
    for i in range(len(fila)):
        print "-"*3, " ",
    print ""
    # si multiplico un caracter o un string por x, el resultado es x veces el texto multiplicado

def tirar_ficha(tablero, columna, jugador):
    """Funcion para realizar la tirada"""
    col = get_columna(tablero, columna)
    col = col[::-1] #invierto la columna para obtener desde el final el primer hueco libre
    valida = True
    try: #compruebo si se puede tirar en esa columna
        posicion_valida = len(col) - (col.index(0)+1)
    except ValueError: #si no se puede tirar, col.index(0) no devolvera lo que esperamos (un int)
        print "No puedes tirar en esa columna"
        valida = False
    else:
        tablero[posicion_valida][columna] = jugador #modifico el tablero en base a la tirada
    return tablero, valida


def get_columna(tablero, columna):
    """Funcion para obtener la lista columna a partir de la matriz tablero"""
    col = [] #creo una lista
    for fila in tablero:
        col.append(fila[columna]) #anyado el elemento de la especificada columna a la lista de la columna
    return col

def jugada(tablero, njugada, n):
    """Funcion para pedir la jugada"""
    if njugada%2 == 0:
        jugador = 1
        columna = input("Jugador {0} elige columna:".format(jugador))-1
    else:
        jugador = 2
        columna = random.randint(1, n-1)
        print "Jugador {0} elige columna:{1}".format(jugador, columna)

    tablero, valida = tirar_ficha(tablero, columna, jugador)
    mostrar_tablero(tablero)
    return valida

def comprobar_fila(fila):
    """Funcion que comprueba si alguien ha conectado una columna"""
    i = 0
    while i < len(fila):
        if fila[i:i+4:] == [1, 1, 1, 1]: #puesto que fila[i:i+4:] es una lista, la comparo con la lista que debe ser para que haya ganado el jugador
            return "Jugador 1. Has ganado!!"
        elif fila [i:i+4] == [2, 2, 2 ,2]:
            return "Jugador 2. Has ganado!!"
        i += 1
    return "Sigue"

def comprobar_columna(columna):
    """Funcion que comprueba si alguien ha conectado una columna"""
    i = 0
    while i < len(columna):
        if columna[i:i+4:] == [1, 1, 1, 1]:
            return "Jugador 1. Has ganado!!"
        elif columna [i:i+4] == [2, 2, 2 ,2]:
            return "Jugador 2. Has ganado!!"
        i += 1
    return "Sigue"

def comprobar_diagonal(tablero):
    """Funcion que comprueba si alguien ha conectado una diagonal"""
    for y in range(len(tablero)):
        for x in range(len(tablero)):
            if y+3 < len(tablero):
                if x+3 < len(tablero):
                    if [tablero[y][x], tablero[y+1][x+1], tablero[y+2][x+2], tablero[y+3][x+3]] == [1, 1, 1, 1]: #comparo una lista de longitud 4 y valores correspondientes
                                                                                                                # con la diagonal con la lista que debe ser para que haya ganado
                                                                                                                # el jugador
                        return "Jugador 1. Has ganado!!"
                    elif [tablero[y][x], tablero[y+1][x+1], tablero[y+2][x+2], tablero[y+3][x+3]] == [2, 2, 2, 2]:
                        return "Jugador 2. Has ganado!!"
            if y+3 < len(tablero):
                if x-3 >= 0:
                    if [tablero[y][x], tablero[y+1][x-1], tablero[y+2][x-2], tablero[y+3][x-3]] == [1, 1, 1, 1]:
                        return "Jugador 1. Has ganado"
                    elif [tablero[y][x], tablero[y+1][x-1], tablero[y+2][x-2], tablero[y+3][x-3]] == [2, 2, 2, 2]:
                        return "Jugador 2. Has ganado"
    return "Sigue"

def comprobar_estado_partida(tablero):
    """Funcion que comprueba el estado de la partida para ver si ha ganado alguien"""
    for fila in tablero:
        resultado = comprobar_fila(fila)
        if resultado != "Sigue":
            return resultado
    for i in range(len(tablero)):
        columna = get_columna(tablero, i)
        resultado = comprobar_columna(columna)
        if resultado != "Sigue":
            return resultado
    # implementar diagonal
    resultado = comprobar_diagonal(tablero)
    return resultado #devuelve el resultado del analisis del estado de la partida

random.seed()
tablero, n = construir_tablero()
mostrar_tablero(tablero)
njugador = 0
end = False
while end == False:
    valida = jugada(tablero, njugador, n)
    if valida:
        resultado = comprobar_estado_partida(tablero)
        if resultado == "Sigue":
            njugador += 1
        else:
            end = True
print resultado
