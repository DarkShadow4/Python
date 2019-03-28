def get_data():
    list = []
    l = input("Introduce la longitud: ")
    for i in range(l):
        list.append(input("Valor " + str(i+1)))
    return list

def find_num(list):
    """Funcion que halla el numero oculto"""
    # para hallar el numero oculto hago una sencilla ecuacion:
    # si bien para hallar el numero oculto hay que restar ese numero x a todos los numeros del array o lista, aplicando las propiedades de las sumas y las multiplicaciones se deduce que:
    # (num1-x) + (num2-x) + (num3-x) = 0        Esto equivale a     (num1+num2+num3) - 3x = 0   por tanto   x = -(num1+num2+num3)/ -3 = (num1+num2+num3)/3
    # aplicando esto al problema en cuestion y su resolucion en pyhton, uso la funcion sum() que devuelve la  suma de todos los elementos de un iterable y lo divido entre lo que devuelve
    # la funcion len(), que devuelve la longitud del objeto iterable que se pase como parametro
    x = sum(list)/len(list)
    return x

def comprobar_numero(list, numero_oculto):
    resultado = 0
    for n in list:
        resultado += n-numero_oculto
    if resultado == 0:
        return numero_oculto
    else:
        return -1


list = get_data()
numero_oculto = find_num(list)
numero_oculto = comprobar_numero(list, numero_oculto)

if numero_oculto != -1:
    print "El numero oculto es", numero_oculto, "porque si le restamos", numero_oculto, "a cada elemento de la lista, su suma seria 0:"
    for n in list:
        print n-numero_oculto, "+",

    print "0 = 0"
else:
    print "No hay un numero oculto válido"
