def relleno(char, filas, columnas):
    """Imprime el rectangulo con el relleno"""
    for i in range(filas):
        for j in range(columnas):
            print char,
        print ""

def contorno(char, filas, columnas):
    """Imprime el contorno del rectangulo"""
    for i in range(columnas):
        print char,
    print ""
    for i in range(filas-2):
        print char,
        for j in range(columnas-2):
            print " ",
        print char
    for i in range(columnas):
        print char,

char = raw_input("Introduzca caracter: ")
filas = input("introduzca numero de filas: ")
columnas = input("introduzca numero de columnas: ")
forma = raw_input("Contorno(c) o relleno(r): ")

if forma == "c":
    contorno(char, filas, columnas)
else:
    relleno(char, filas, columnas)
