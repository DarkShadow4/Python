import random

lista = ["cancion1", "cancion2", "cancion3", "cancion4", "cancion5"]
lista2 = []

random.seed()

while len(lista2) < len(lista):
    i = random.randint(0, len(lista)-1)
    if lista[i] in lista2:
        print "i don't append", lista[i], "to lista2 because it was in it before"
    else:
        lista2.append(lista[i])
        print "i append", lista[i], "to lista2 because it wasn't in it before"

#############################################

import random

lista = ["cancion1", "cancion2", "cancion3", "cancion4", "cancion5"]
lista2 = lista

random.seed()

while len(lista2) > 0:
    i = random.randint(0, len(lista)-1)
    print "now playing", lista[i]
    lista2.pop(lista2.index(lista[i]))
