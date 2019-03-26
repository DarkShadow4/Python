import random

random.seed()
r = True
while r:
    n1 = input("Introduce el dia de nacimiento: ")
    n2 = input("Introduce el mes de tu nacimiento: ")
    n3 = input("Introduce tu numero de zapato: ")
    if n1 >= 1 and n1 <= 31:
        if n2 >= 1 and n2 <= 12:
            if n3 >= 35 and n3 <= 45:
                r = False
puntuacion = float(0)
r = "s"
intentos = 5
while r == "s" and intentos > 0:
    coincidencias = 0
    r1 = random.randint(1, 31)
    r2 = random.randint(1, 12)
    r3 = random.randint(35, 45)
    print "Los numeros eran:", r1, r2, r3
    if r1 == n1:
        coincidencias += 1
    if r2 == n2:
        coincidencias += 1
    if r3 == n3:
        coincidencias += 1

    if coincidencias == 0:
        print "No hay coincidencias. Ganas 0 puntos"
        puntuacion /= 2 #divido entre dos la puntuacion
    elif coincidencias == 1:
        print "1 coincidencia.Ganas 5 puntos"
        puntuacion += 5
    elif coincidencias == 2:
        print "2 coincidencia.Ganas 15 puntos"
        puntuacion += 15
    elif coincidencias == 3:
        print "3 coincidencia.Ganas 50 puntos"
        puntuacion += 50
    print "Llevas", puntuacion, "puntos"
    intentos -= 1
    if intentos > 0:
        r = raw_input("Quieres seguir jugando?").lower()
print "Fin de partida. Has ganado", puntuacion, "puntos"
