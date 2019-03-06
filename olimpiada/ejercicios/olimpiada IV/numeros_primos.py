m = input("Introduce un numero: ")
print "Numeros primos: ",
for i in range(2, m+1):
    primo = True
    for x in range(2, i):
        if i%x == 0:
            primo = False
    if primo == True:
        print i,
