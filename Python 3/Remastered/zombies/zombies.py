import random

def crear_mapa(w, h):
    mapa = []
    for y in range(h):
        fila = []
        for x in range(w):
            fila.append(0)
        mapa.append(fila)
    return mapa

def mostrar_mapa(mapa):
    for fila in mapa:
        for celda in fila:
            if celda == 0:
                print("O", end = " ")
            elif celda == 1:
                print("X", end = " ")
            elif celda == 2:
                print("#", end = " ")
        print()

def spawnear_jugador(mapa):
    jx = random.randint(0, len(mapa[0])-1)
    jy = random.randint(0, len(mapa)-1)
    mapa[jy][jx] = 2
    return mapa

def generar_partida():
    # Pido las dimensiones del mapa y las convierto en int
    h, w = map(int, input().split())
    # Creo el mapa
    mapa = crear_mapa(w, h)
    mapa = spawnear_jugador(mapa)

# Establezco la semilla random con su valor por defecto, es decir, el tiempo del sistema
random.seed()

generar_partida()

mostrar_mapa(mapa)
