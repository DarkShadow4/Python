ISBN = raw_input("Introduzca ISBN")
n=10
numero=0
md = 0
for digito in ISBN:
    if digito == 'X' or digito == 'x':
        numero += 10
    elif digito == '?':
        md = n
    else:
        numero = numero+(int(digito)*n)
    n -= 1
if numero%11 == 0 and md== 0:
    print "El ISBN es valido"
elif md == 0:
    print "El ISBN no es valido"
else:
    i = 0
    while md != 0:
        if (numero+(i*md))%11 == 0:
            print "El digito que falta es", i
            md = 0
        else:
            i += 1
# 15?881111x
