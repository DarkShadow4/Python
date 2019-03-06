palabra = raw_input("Introduce palabra:")
M = 0
m = 0
for letra in palabra:
    if letra.isupper():
        M += 1
    else:
        m += 1
print "Letras mayusculas:", M
print "Letras minusculas:", m
