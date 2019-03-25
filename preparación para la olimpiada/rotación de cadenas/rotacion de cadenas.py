def comprobar_rotaciones(p1, p2):
    """Funcion que comprueba si una palabra es rotacion de otra"""
    for i in range(len(p1)):
        if p1[i:]+p1[:i] == p2: #si los caracteres de la palabra desde i hasta el final mas el primero hasta el i es igual a la palabra 2 significa que la palabra 2 es una rotación
            return True
    return False

p1 = raw_input("Introduzca palabra 1").lower()
p2 = raw_input("Introduzca palabra 2").lower()
r = comprobar_rotaciones(p1, p2)

if r:
    print p2, "es una rotacion de", p1
else:
    print p2, "no es una rotacion de", p1
