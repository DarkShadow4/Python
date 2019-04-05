from __future__ import print_function #python2
import random
import getch

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

def generar_partida():
    # Pido las dimensiones del mapa y las convierto en int
    h, w = map(int, raw_input().split()) #python2
    # h, w = map(int, input().split()) #python3
    # Creo el mapa
    mapa = crear_mapa(w, h)
    spawnear_jugador(mapa)
    return mapa

def pedir_movimiento():
    movimiento = getch.getch()
    return movimiento

def mover_zombies(mapa):
    pass

def mover(mapa):
    movimiento = "n"
    pedir = any(movimiento == "w", movimiento == "W")
    while pedir:
    movimiento = pedir_movimiento()



# Establezco la semilla random con su valor por defecto, es decir, el tiempo del sistema
random.seed()

mapa = generar_partida()

mostrar_mapa(mapa)
