# -*- coding: utf-8 -*-

elementos={
    0:" ",
    1:"o",
    2:"x"
}
tipos={
    "nogana":0,
    "gana1":1,
    "gana2":2,
    "colnovalida":3,
    "empate":4,
    "back":5,
    "salidavoluntaria":6
}

def getConfig():
    """Pide las características del juego: dimensión del tablero y nº de jugadores (1/2)"""
    n = int(input('Introduce el tamaño del tablero'))
    j = int(input("Introduce número de jugadores (1/2)(si se Introduce 1 jugará contra el ordenador, que no es muy bueno):"))
    return(n, j)

def generar_tablero(n):
    """Genera un tablero vacío de nxn dado el parámetro n"""
    tablero=[]
    for j in range(n):
        columna = []
        for i in  range(n):
            columna.append(0)
        tablero.append(columna)
    return(tablero)

def mostrar_tablero(tablero):
    """Muestra el tablero con el formato correcto"""
    colsep="\n "+(" "+"-"*3)*len(tablero)+"\n"
    print(colsep, end="")
    for fila in tablero:
        for elemento in fila:
            print(" | ", end=elementos[elemento])
        print(" |", end=colsep)

def pedir_columna(turno):
    """Pide la columna en la que se quiere tirar la ficha"""
    col = int(input("Jugador {0}. Elige columna: ".format(turno)))-1
    return(col)

def comprobar_tirada(tablero, jugador, columna):
    """Comprueba la validez de la tirada y si es una jugada ganadora"""
    if not (0 in tablero[0]):     # Si no hay huecos vacíos en la fila superior
        return(tipos["empate"])
                                # entonces no quedan movimientos válidos
                                # porque forzosamente las filas inferiores no
                                # pueden contener huecos vacíos

    if columna == -1:
        return(tipos["salidavoluntaria"])
    elif not 0 <= columna < n:
        return(tipos["colnovalida"])

    #comprueba si es empate
    return (tipos["nogana"])

def getYpos(tablero, columna):
    """Devuelve la columna que se pide"""
    col = []
    for fila in tablero:
        col.append(fila[columna])
    col = col[::-1]                         # Lo obtengo y le doy la vuelta
                                            # para hallar el hueco disponible

    if not 0 in col:                        # Si hay hueco en la columna
        return(-1)                          # situa la ficha en la primera
                                            # fila que se pueda empezando
    return ((n-1)-col.index(0))             # desde abajo. Si no, devuelve -1

def ganaono(tablero, jugador, tirada):
    """Comprueba si la jugada da la victoria al jugador actual"""
    n = len(tablero)

    # Comprobaciones no diagonales:

    # Horizontal izquierda
    if tirada[0] >= 3 and tablero[tirada[0]][tirada[1]] == tablero[tirada[0]-1][tirada[1]] == tablero[tirada[0]-2][tirada[1]] == tablero[tirada[0]-3][tirada[1]] == jugador:
        return(tipos["gana{0}".format(jugador)])

    # Horizontal derecha
    if tirada[0] <= (n-1)-3 and tablero[tirada[0]][tirada[1]] == tablero[tirada[0]+1][tirada[1]] == tablero[tirada[0]+2][tirada[1]] == tablero[tirada[0]+3][tirada[1]] == jugador:
        return(tipos["gana{0}".format(jugador)])

    # Vertical arriba
    if tirada[1] >= 3 and tablero[tirada[0]][tirada[1]] == tablero[tirada[0]][tirada[1]-1] == tablero[tirada[0]][tirada[1]-2] == tablero[tirada[0]][tirada[1]-3] == jugador:
        return(tipos["gana{0}".format(jugador)])

    # Vertical abajo
    if tirada[1] <= (n-1)-3 and tablero[tirada[0]][tirada[1]] == tablero[tirada[0]][tirada[1]+1] == tablero[tirada[0]][tirada[1]+2] == tablero[tirada[0]][tirada[1]+3] == jugador:
        return(tipos["gana{0}".format(jugador)])

    # Comprobaciones diagonales:

    # Abajo derecha
    if (tirada[0] >= 3 and tirada[1] >= 3) and tablero[tirada[0]][tirada[1]] == tablero[tirada[0]-1][tirada[1]-1] == tablero[tirada[0]-2][tirada[1]-2] == tablero[tirada[0]-3][tirada[1]-3] == jugador:
        return(tipos["gana{0}".format(jugador)])

    # Abajo izquierda
    if (tirada[0] <= (n-1)-3 and tirada[1] >= 3) and tablero[tirada[0]][tirada[1]] == tablero[tirada[0]+1][tirada[1]-1] == tablero[tirada[0]+2][tirada[1]-2] == tablero[tirada[0]+3][tirada[1]-3] == jugador:
        return(tipos["gana{0}".format(jugador)])

    # Arriba izquierda
    if (tirada[0] <= (n-1)-3 and tirada[1] <= (n-1)-3) and tablero[tirada[0]][tirada[1]] == tablero[tirada[0]+1][tirada[1]+1] == tablero[tirada[0]+2][tirada[1]+2] == tablero[tirada[0]+3][tirada[1]+3] == jugador:
        return(tipos["gana{0}".format(jugador)])

    # Arriba derecha
    if (tirada[0] >= 3 and tirada[1] <= (n-1)-3) and tablero[tirada[0]][tirada[1]] == tablero[tirada[0]-1][tirada[1]+1] == tablero[tirada[0]-2][tirada[1]+2] == tablero[tirada[0]-3][tirada[1]+3] == jugador:
        return(tipos["gana{0}".format(jugador)])

    return(tipos["nogana"])

def tirar(tablero, jugador, columna):
    """Realiza la tirada si es válida"""
    tipo=comprobar_tirada(tablero, jugador, columna)
    if not (tipo == tipos["salidavoluntaria"] or tipo == tipos["colnovalida"]):
        fila = getYpos(tablero, columna)
        if fila != -1:
            tablero[fila][columna] = jugador
        else:                                   # Si no es válida porque está
                                                # llena
            tipo=tipos["colnovalida"]

    if tipo == tipos["nogana"]:
        tirada = (fila, columna)
        tipo = ganaono(tablero, jugador, tirada)
    return(tablero, tipo)

#### IA

# TODO: Implementar rangos de predicción 5, 10, ...

def value(tablero):
    """
    Función que valora lo favorable que es el tablero para la IA
    """
    # Primero cuento el número de veces que el j1 o j2 tiene 3 fichas seguidas que no estén bloqueadas
    j12_3_f = {
        1:0,
        2:0
    }

    # three_free4j1 = [1, 1, 1, 0]
    # three_free4j2 = [2, 2, 2, 0]

    n = range(len(tablero))
    for fila in n:
        for columna in n:

            if columna+3 < n-3: # Horizontal [i, i, i, 0]
                if 0 != tablero[fila][columna] == tablero[fila][columna+1] == tablero[fila][columna+2] and tablero[fila][columna+3] == 0:
                    j12[tablero[fila][columna]] += 1

            if fila+3 < n-3: # Vertical [i, i, i, 0]
                if 0 != tablero[fila][columna] == tablero[fila+1][columna] == tablero[fila+2][columna] and tablero[fila+3][columna] == 0:
                    j12[tablero[fila][columna]] += 1

            if columna-3 > 0: # Horizontal [0, i, i, i]
                if 0 != tablero[fila][columna] == tablero[fila][columna-1] == tablero[fila][columna-2] and tablero[fila][columna-3] == 0:
                    j12[tablero[fila][columna]] += 1

            if fila-3 > 0: # Vertical [0, i, i, i]
                if 0 != tablero[fila][columna] == tablero[fila-1][columna] == tablero[fila-2][columna] and tablero[fila-3][columna] == 0:
                    j12[tablero[fila][columna]] += 1

            #### Diagonal
            ### Arriba
            ## Izquierda
            # [i, i, i, 0]
            if columna-3 > 0 and fila-3 >0:
                if 0 != tablero[fila-3][columna-3] == tablero[fila-2][columna-2] == tablero[fila-1][columna-1] and tablero[fila][columna] == 0:
                    j12[tablero[fila][columna]] += 1
            # # [0, i, i, i]
            #     if 0 != tablero[fila][columna] == tablero[fila-1][columna-1] == tablero[fila-2][columna-2] and tablero[fila-3][columna-3] == 0:
            #         j12[tablero[fila][columna]] += 1
            ## Derecha
            # [i, i, i, 0]
            if columna-3 > 0 and fila-3 >0:
                if 0 != tablero[fila-3][columna-3] == tablero[fila-2][columna-2] == tablero[fila-1][columna-1] and tablero[fila][columna] == 0:
                    j12[tablero[fila][columna]] += 1
            # # [0, i, i, i]
            #     if 0 != tablero[fila][columna] == tablero[fila-1][columna-1] == tablero[fila-2][columna-2] and tablero[fila-3][columna-3] == 0:
            #         j12[tablero[fila][columna]] += 1
            # [0, i, i, i]

            ### Abajo
            ## Derecha
            # [i, i, i, 0]

            # [0, i, i, i]

            ## Izquierda
            # [i, i, i, 0]

            # [0, i, i, i]

    pass

 # ·---·---·---·---·
 # |   |   |   |   |
 # ·---·---·---·---·
 # |   |   |   |   |
 # ·---·---·---·---·
 # |   |   |   |   |
 # ·---·---·---·---·
 # |   |   |   |   |
 # ·---·---·---·---·


def IA1(tablero):
    """
    Función que simula un segundo jugador y en combinación con IA2 elabora
    razonamientos con los que puede anteponerse a las jugadas del jugador
    """
    # print("IA1(simj2)")
    n = len(tablero)
    c = -1
    tablero_original=simular(tablero)
    tipo = tipos["nogana"]
    while c+1 < n and tipo == tipos["nogana"]:
        c += 1
        t_prueba, tipo = tirar(simular(tablero), 2, c)
        # print("Si j2 tira en col: {0}, es una tirada: {1} y quedaria el tablero así:".format(c, tipo))
        # mostrar_tablero(t_prueba)
        if not (tipo == tipos["empate"] or tipo == tipos["colnovalida"]):
            if tipo == tipos["gana2"]:
                return(t_prueba, tipo, c)
            tablero, tipo, null = IA2(tirar(simular(tablero), 2, c)[0])
            # print("tipo: {0}".format(tipo))
            if not(tipo == tipos["empate"] or tipo == tipos["colnovalida"]):
                # if tipo == tipos["gana2"]:
                    # return(tablero, tipo, c)
                if tipo == tipos["gana1"]:
                    tablero = simular(tablero_original)
                    # print("Como ganaría el j1, vuelve para atrás")
                    return(tablero, tipos["back"], c)

            # tablero = simular(tablero_original)

        if tipo == tipos["empate"] or tipo == tipos["colnovalida"] or tipo == tipos["back"]:
            tipo = tipos["nogana"]

        tablero = simular(tablero_original)

    tablero, tipo = tirar(tablero_original, 2, c)
    return(tablero, tipo, c)




def IA2(tablero):
    """
    Función que simula el primer jugador para que la IA1 pueda anteponerse a
    las posibles tiradas del jugador
    """
    # print("IA2(simj1)")
    n = len(tablero)
    c = -1
    tipo = tipos["nogana"]
    tablero_original=simular(tablero)
    while c+1 < n and tipo == tipos["nogana"]:
        c += 1
        t_prueba, tipo = tirar(simular(tablero), 1, c)
        # print("Si j1 tira en col: {0}, es una tirada: {1} y quedaria el tablero así:".format(c, tipo))
        # mostrar_tablero(t_prueba)
        if not ((tipo == tipos["empate"]) or (tipo == tipos["colnovalida"])):
            if tipo == tipos["gana1"]:
                return(t_prueba, tipo, c)
            tablero, tipo, null = IA1(tirar(simular(tablero), 1, c)[0])
            # print("tipo: {0}".format(tipo))
            if tipo == tipos["back"]:
                # print("Vuelve otra vez")
                return(tablero_original, tipo, c)
            # if not (tipo == tipos["empate"] or tipo == tipos["colnovalida"]):
                # if tipo == tipos["gana1"]:
                    # return(tablero, tipo, c)


            # tablero = simular(tablero_original)

        if tipo == tipos["colnovalida"] or tipo == tipos["empate"]:# or tipo == tipos["reback"]:
            tipo = tipos["nogana"]

        tablero = simular(tablero_original)

    tablero, tipo = tirar(tablero_original, 1, c)
    return(tablero, tipo, c)



####

def simular(tablero):
    sim = []
    for fila in tablero:
        f = []
        for elemento in fila:
            f.append(elemento)
        sim.append(f)
    return(sim)

n, nj = getConfig()
tablero = generar_tablero(n)
mostrar_tablero(tablero)
tipo = tipos["nogana"]
turno = 0

while tipo == tipos["nogana"]:
    jugador = (turno%2)+1
    if nj == 1 and jugador == 2:
        null, tipo, tirada = IA1(simular(tablero))
        tablero, tipo = tirar(tablero, 2, tirada)
        print("El jugador 2 ha decidido tirar en la columna {0}".format(tirada))
    else:
        tirada = pedir_columna(jugador)
        tablero, tipo = tirar(tablero, jugador, tirada)

    mostrar_tablero(tablero)
    if tipo == tipos["nogana"]:
        turno += 1
    elif tipo == tipos["colnovalida"]:
        print("Introduce una columna válida")
        tipo = tipos["nogana"]

    if tipo == tipos["nogana"] and turno == n*n:
        tipo = tipos["empate"]

if tipo == tipos["empate"]:
    print("Empate, nadie gana y nadie pierde. Se podría decir que la partida está en un estado cuántico")
elif tipo == tipos["salidavoluntaria"]:
    print("Has salido voluntariamente")
else:
    print("Ha ganado el Jugador {0}".format(jugador))
