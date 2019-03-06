modo = raw_input("Cifrar(c) o descifrar(d)?: ")
cesar = input("Numero cesar: ")
cad = raw_input("Introduce cadena:")

def accion(modo, cadena, cesar):
    """Realiza el cifrado o descifrado de la cadena segun la eleccion del usuario"""
    cifrado = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if modo == "c":
        # Paso por parametro la cadena de cifrado al reves ya que lo que quiero es aprovechar la capacidad de python para manejar indices negativos
        cifrado = ",".join(reversed(cifrado))
        cifrado = cifrado.split(",")
        cadena_cifrada = cifrar(cadena, cesar, reversed(cifrado))
    else:
        if modo == "d":
            cadena_cifrada = descifrar(cadena, cesar, cifrado)
    return cadena_cifrada

def descifrar(cadena, cesar, cifrado):
    """Descifra la cadena introducida"""
    cadena_cifrada = [] # Creo una lista en la que voy añadiendo los caracteres segun los cifro
    for letra in cadena:
        index = cifrado.index(letra) # Obtengo el indice del caracter en la cadena de cifrado
        cadena_cifrada.append(cifrado[index-cesar]) # Le resto el numero cesar sin comprovar si daria un indice negativo puesto que quiero aprovechar esta caracteristica de python
    return "".join(cadena_cifrada) # Convierto la lista cifrada en una cadena y hago que la funcion la devuelva

def cifrar(cadena, cesar, cifrado):
    """Cifra la cadena introducida"""
    cadena_cifrada = [] # Creo una lista en la que voy añadiendo los caracteres segun los descifro
    for letra in cadena:
        indice = cifrado.index(letra) # Obtengo el indice del caracter en la cadena de cifrado
        cadena_cifrada.append(cifrado[indice-cesar]) # Le resto el numero cesar sin comprovar si daria un indice negativo puesto que quiero aprovechar esta caracteristica de python
    return "".join(cadena_cifrada) # Convierto la lista cifrada en una cadena y hago que la funcion la devuelva

accion(modo, cad, cesar)
print cadena
