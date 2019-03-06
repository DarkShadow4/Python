sopa = open("sopa.txt")
m = input("Introduzca numero de filas: ")
n = input("Introduzca numero de columnas: ")
matriz = []
y = 0
while y < m:
    x = 0
    fila = []
    while x < n:
        fila.append(sopa.read((y*n)+x))
        x += 1
    matriz.append(fila)
    y += 1
print matriz
