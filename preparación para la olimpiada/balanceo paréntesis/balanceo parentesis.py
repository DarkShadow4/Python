# -*- coding: utf-8 -*-
def get_frase():
    frase = raw_input("é")
    return frase

def comprobar_parentesis(frase):
    parentesis_sin_cerrar = 0
    for c in frase:
        if c == "(":
            parentesis_sin_cerrar += 1
        elif c== ")":
            parentesis_sin_cerrar -= 1
    if parentesis_sin_cerrar != 0:
        return False
    else:
        return True

frase = get_frase()
parentesis_correcto = comprobar_parentesis(frase)
if parentesis_correcto:
    print u"los paréntesis estan bien balanceados"
else:
    print u"los paréntesis no estan correctamente balanceados"
