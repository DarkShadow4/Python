posicion1 = input("Posición inicial canguro 1:")
longitud1 = input("Longitud de salto canguro 1:")
posicion2 = input("Posición inicial canguro 2:")
longitud2 = input("Longitud de salto canguro 2:")
if (posicion1 > posicion2 and longitud1 > longitud2) or (posicion1 < posicion2 and longitud1 < longitud2):
    respuesta = "no"
else:
print "Alcanza?", respuesta
