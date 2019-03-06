def mostrar_palabra(word):
    npalabra = ""
    for letra in word:
        if letra.isupper():
            npalabra += letra.lower()
        else:
            npalabra += letra.upper()
    print len(npalabra)
    print npalabra
palabras = []
i = 0
while i < 5:
    palabra = raw_input("Introduce palabra:")
    palabras.append(palabra)
    i += 1
while i > 0:
    mostrar_palabra(palabras[i])
    i += 1
