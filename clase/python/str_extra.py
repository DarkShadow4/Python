from random import randrange
def ocultar_palabra(palabra):
    palabra_oculta = ""
    for letra in palabra:
        if randrange(0, 100) < 75:
            palabra_oculta += "*"
        else:
            palabra_oculta += letra
    return palabra_oculta
r = "s"
while r == "s":
    solucion = raw_input("La palabra oculta es?: ")
    i = 5
    while i > 0:
        intento = ocultar_palabra(solucion)
        if raw_input(intento) != solucion:
            i -= 1
        else:
            print "Has acertado !! / /inserte emocion"
            i = -1
    if i == 0:
        print "Lo siento, perdiste"
    r = raw_input("Desea jugar de nuevo?(s/n):")
