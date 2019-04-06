# from __future__ import print_function #python2
import random
import getch
from statistics import mean

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
    return jx, jy

def spawnear_zombies(mapa, zombies):
    i = 0
    while i < zombies:
        zx = random.randint(0, len(mapa[0])-1)
        zy = random.randint(0, len(mapa)-1)
        if mapa[zy][zx] == 0:
            mapa[zy][zx] = 1
            i += 1

def generar_partida():
    # Pido las dimensiones del mapa y las convierto en int
    # h, w = map(int, raw_input().split()) #python2
    h, w = map(int, input().split()) #python3
    # Creo el mapa
    mapa = crear_mapa(w, h)
    #spawneo el spawnear_jugador
    jx, jy = spawnear_jugador(mapa)
    #spawneo los zombies
    spawnear_zombies(mapa, mean([h, w]))
    return mapa, jx, jy

def pedir_movimiento():
    pedir = True
    while pedir:
        movimiento = (getch.getch()).decode("utf-8")
        print ("movimiento: " + movimiento)
        #movimiento = input()
        pedir = not any([movimiento == "w", movimiento == "W", movimiento == "a", movimiento == "A", movimiento == "s", movimiento == "S", movimiento == "d", movimiento == "D"])
    return movimiento

def comprobar_movimiento(mapa, jx, jy, movimiento, avance):
    valido = True
    # jx = jx
    # jy = jy
    if movimiento.lower() == "w":
        if jy-avance < 0:
            valido = False
        elif mapa[jy-avance][jx] == 1:
            return "muere", 0, 0
        else:
            mapa[jy][jx] = 0
            mapa[jy-avance][jx] = 2
            jy -= avance
    elif movimiento.lower() == "a":
        if jx-avance < 0:
            valido = False
        elif mapa[jy][jx-avance] == 1:
            return "muere", 0, 0
        else:
            mapa[jy][jx] = 0
            mapa[jy][jx-avance] = 2
            jx -= avance
    elif movimiento.lower() == "s":
        if jy+avance >= len(mapa):
            valido = False
        elif mapa[jy+avance][jx] == 1:
            return "muere", 0, 0
        else:
            mapa[jy][jx] = 0
            mapa[jy+avance][jx] = 2
            jy += avance
    elif movimiento.lower() == "d":
        if jx+avance >= len(mapa[0]):
            valido = False
        elif mapa[jy][jx+avance] == 1:
            return "muere", 0, 0
        else:
            print("muevo hacia la izquierda")
            mapa[jy][jx] = 0
            mapa[jy][jx+avance] = 2
            jx += avance
    return valido, jx, jy


def mover_zombies(mapa, jx, jy):
    pass

def mover(mapa, jx, jy):
    #pido movimiento
    movimiento = pedir_movimiento()
    #si se pulsa mayus, el avance es el doble
    if movimiento.isupper():
        avance = 2
    else:
        avance = 1
    #compruebo si el movimiento es valido o no
    move, jx, jy = comprobar_movimiento(mapa, jx, jy, movimiento, avance)
    if move != "muere":
        if move:
            mover_zombies(mapa, jx, jy)
            return True, jx, jy
        else:
            return True, jx, jy
    else:
        return False, jx, jy



# Establezco la semilla random con su valor por defecto, es decir, el tiempo del sistema
random.seed()
continuar = True
mapa, jx, jy = generar_partida()
while continuar:
    mostrar_mapa(mapa)
    continuar, jx, jy = mover(mapa, jx, jy)
