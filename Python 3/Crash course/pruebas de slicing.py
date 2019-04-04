# creo el string
letters = "abcdefghij"
numbers = "0123456789"
# La sintáxis del slicing es la siguiente string[start:end:step]
# start = start || start es el indice en el que empieza el slice
# end = end-1 || end es el elemento en el que termina el slice
# step = step || step es el avance del slice (por defecto es 1, es decir, si no se introduce, es como si se introdujese un 1)
# Un slice es como un bucle (pero no es un bucle) que se usa solo para obtener fragmentos de objetos iterables. Al igual que en los bucles convencionales que usan un contador
# y su condición de salida es el valor maximo que debe tomar el contador
# Para hacer una correcta comparación con un bucle convencional voy a hacer un bucle con un estructura parecida a la que tendria un slice si fuera realmente un bucle:
iterador = start = 0
end = 5
step = 2
while iterador < end:
    # do something
    print("iterador: " + str(iterador))#yo imprimo el iterador para mostrar el funcionamiento con el step distinto a 1, pero el objetivo de un splice no es imprimir el slice,
    # sino devolverlo para poder usarlo
    print("letra: " + letters[iterador])#en el caso del slice de las letras
    print("numero: " + numbers[iterador])#en el caso del slice de los numeros
    iterador += step
#imprimo del primero al 5
print(string[0:5]) # imprime del indice 0 al quinto elemento (indice 4)
print(string[1:5]) # imprime del indice 1 al quinto elemento (indice 4)
print(string[5:]) # imprime del indice 5 hasta el final
print(numbers[0:5]) # imprime del indice 0 al quinto elemento (indice 4)
print(numbers[1:5]) # imprime del indice 1 al quinto elemento (indice 4)
print(numbers[5:]) # imprime del indice 5 hasta el final
# Viendo el output genedado decuzco que al hacer un slice, el primer indice indica el indice donde empieza el slice, mientras que el segundo indice indica el elemento donde acaba
# Esto seria lo mismo que decir que el primer indice introducido lo trata tal cuál se introduce, sin embargo, al segundo indice se le resta una unidad

# Para copiar una lista sin que se vinculen la nueva y la copiada se copia usando un slice de toda la lista
lista1 = list(range(10))
lista2 = lista1[:] #no hace falta poner el step
lista1.append(10)
print(lista1)
print(lista2)
