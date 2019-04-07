# from __future__ import print_function #python2
import random, getch, subprocess, platform
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
    spawnear_zombies(mapa, mean([h, w])/2)
    return mapa, jx, jy

def pedir_movimiento():
    pedir = True
    while pedir:
        movimiento = (getch.getch()).decode("utf-8")
        #print ("movimiento: " + movimiento)
        #movimiento = input()
        pedir = not any([movimiento == "w", movimiento == "W", movimiento == "a", movimiento == "A", movimiento == "s", movimiento == "S", movimiento == "d", movimiento == "D"])
    return movimiento

def comprobar_movimiento(mapa, jx, jy, movimiento, avance):
    valido = True
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
            print("muevo hacia la derecha")
            mapa[jy][jx] = 0
            mapa[jy][jx+avance] = 2
            jx += avance
    return valido, jx, jy

def mover_hacia_jugador(mapa, jx, jy, zx, zy):
    # Quito el zombie para moverlo
    mapa[zy][zx] = 0
    # Se mueve horizontalmente
    if jx > zx:
        zx += 1
    elif jx < zx:
        zx -= 1
    # Se mueve vertialmente
    if jy > zy:
        zy += 1
    elif jy < zy:
        zy -= 1
    # Vuelvo a poner el zombie pero en el lugar correcto
    mapa[zy][zx] = 1
    print("movido un zombie")
    mostrar_mapa(mapa)
    if zx == jx and zy == jy:
        return "muere"
    return ""

def mover_zombies(mapa, jx, jy):
    for zy in range(len(mapa)):
        for zx in range(len(mapa[zy])):
            if mapa[zy][zx] == 1:
                resultado = mover_hacia_jugador(mapa, jx, jy, zx, zy)
    return resultado

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
            resultado = mover_zombies(mapa, jx, jy)
            if resultado:
                return False, jx, jy
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
    # if platform.system() == 'Windows':
    #     subprocess.call("cls", shell=True)
    # elif platform.system() == 'Linux':
    #     subprocess.call("clear")
    mostrar_mapa(mapa)
    continuar, jx, jy = mover(mapa, jx, jy)
print("Lo siento pero has muerto")
