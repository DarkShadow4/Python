import random

opciones = ["tijera", "papel", "piedra"]

jo = random.randint(0, 2)
jj = input("Escoje tu jugada (Tijera = 1, Papel = 2, Piedra = 3): ")
jj -= 1

if jj == jo-1:
    print "Has elegido:", opciones[jj]
    print "El ordenador ha elegido:", opciones[jo]
    print "Has ganado"
else:
    if jo == jj-1:
        print "Has elegido:", opciones[jj]
        print "El ordenador ha elegido:", opciones[jo]
        print "Has perdido"
    else:
        print "Has elegido:", opciones[jj]
        print "El ordenador ha elegido:", opciones[jo]
        print "Habeis quedado empate"
