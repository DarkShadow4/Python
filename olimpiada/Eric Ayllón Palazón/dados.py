# Eric Ayllon Palazon
def get_dado():
    dado = raw_input().split() # cojo como una cadena de texto los numeros y lo divido en los numeros
    i = 0
    while i < 6:
        dado[i] = int(dado[i]) #convierto los elementos/numeros del dado en numeros
        i += 1
    return dado #devuelvo el dado
def get_dados():
    """Funcion para introducir los dados"""
    j1 = []
    j2 = []
    # pido el primer dado del j1
    j1.append(get_dado())
    #Pido el 2o dado del j1
    j1.append(get_dado())
    #Pido el 2o dado del j2
    j2.append(get_dado())
    #Pido el 2o dado del j2
    j2.append(get_dado())
    return j1, j2

def comprobar_dados(j1, j2):
    posibilidades_j1 = {} # uso diccionarios para las posibilidades de suma que estan entre 2 y 16 aunque tambien pongo la posibilidad de que sumen 1 por poder inicializar
    # los diccionarios automaticamente
    posibilidades_j2 = {}
    for i in range(16):
        posibilidades_j1[i+1] = 0
        posibilidades_j2[i+1] = 0
    for n1 in j1[0]:
        for n2 in j1[1]:
            posibilidades_j1[n1+n2] += 1 # realizo todas las posibles sumas
    for n1 in j2[0]:
        for n2 in j2[1]:
            posibilidades_j2[n1+n2] += 1
    if posibilidades_j1 == posibilidades_j2: #si son iguales los diccionarios de posibilidades es que el juego es justo
        print "Juego justo"
    else:
        print "Juego injusto"

j1, j2 = get_dados()
comprobar_dados(j1, j2)
