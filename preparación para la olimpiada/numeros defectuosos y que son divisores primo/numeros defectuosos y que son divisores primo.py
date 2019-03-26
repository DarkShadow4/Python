def get_divisores(num):
    """Funcion para obtener los divisores del numero dado"""
    divisores = [] #uso una lista para guardar los divisores
    for i in range(1, num):
        if num%i == 0:
            divisores.append(i)
    return divisores

def comprobar_primo(num):
    """Funcion para comprobar si un numero es primo o no"""
    primo = True
    for i in range(2, num):
        if num%i == 0:
            primo = False
    return primo

n = -1
while n <= 0:
    n = input("Introduzca numero mayor que 0: ")
    if n <= 0:
        print "Error: numero incorrecto. Vuelva a intentarlo"
i = 0
num = 0
defectuosos = []
while i < n:
    num += 1
    if sum(get_divisores(num)) > num: # la funcion sum() devuelve la suma de los elementos de un objeto iterable
        defectuosos.append(num)
        i += 1

for defectuoso in defectuosos:
    num_divisores = len(get_divisores(defectuoso)) #la longitud de la lista de divisores es el numero de divisores que tiene
    print "D"+str(defectuosos.index(defectuoso)+1), "=", defectuoso, "y tiene", num_divisores, "divisores.",
    if comprobar_primo(num_divisores):
        print "El numero de divisores es primo"
    else:
        print ""
