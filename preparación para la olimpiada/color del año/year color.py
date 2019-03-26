# -*- coding: utf-8 -*-

def get_color(colores, par = 0, impar = 0):
    """Funcion para obtener el color en funcion de los datos sacados del year"""
    if par == impar:
        colores[0] += 1
        return "rojo"
    elif par < impar:
        colores[1] += 1
        return "verde"
    elif par > impar:
        colores[2] += 1
        return "azul"


def analize_year(colores, intentos, year):
    intentos[0] += 1
    if int(year) >= 1900 and int(year) <= 2016:
        intentos[1] += 1
        par = 0
        impar = 0
        for cifra in year:
            cifra = int(cifra)
            if cifra%2 == 0:
                par += cifra
            else:
                impar += cifra
        return "Tu color es el " + get_color(colores, par, impar)
    else:
        return "No es un año valido"

def mostrar_informe(colores, intentos):
    print "Intentos totales:", intentos[0]
    print "Intentos validos:", intentos[1]
    print "Numero de rojos:", colores[0]
    print "Numero de verdes:", colores[1]
    print "Numero de azules:", colores[2]

intentos = [0, 0] # guardo los intentos totales y validos en una lista
colores = [0, 0 ,0] #guardo las veces que aparece cada color en una lista
c = "s"
while c == "s":
    year = raw_input("Introduce año de nacimiento: ")
    ans = analize_year(colores, intentos, year)
    print ans
    if ans != "No es un año valido":
        char = True
    while char:
        c = raw_input("Quieres continuar(S/n)? ").lower()
        if c != "s" and c != "n":
            char = True
        else:
            char = False
            if c == "n":
                mostrar_informe(colores, intentos)
