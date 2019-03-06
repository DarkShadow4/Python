m = input("Introduzca el valor m")
print "Numeros primos:",
n = 2
while n <= m:
    i = 2
    p = True
    while i < n:
        if n%i == 0:
            p = False
        i += 1
    if p:
        print n,
    n += 1
