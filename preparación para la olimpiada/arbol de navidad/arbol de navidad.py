import random #importo la librería de aleatorios
from __future__ import print_function # importo la funcion print de Python 3


random.seed() #establezco la random seed con la por defecto
n = input("Numero de bloques: ")
h = input("Altura del primer bloque: ")
anterior = 0

for nbloque in range(n):
    for fila in range(anterior, h+anterior):
        row = ""
        for i in range(fila):
            row += str(random.randint(0, 1))
        row += str(random.randint(0, 1))
        for i in range(fila):
            row += str(random.randint(0, 1))
        print (row.center((n+1)*(h+1)))
    anterior = fila-1
