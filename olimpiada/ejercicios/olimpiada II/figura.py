filas = input("introduzca numero de filas: ")
for i in range(filas):
    for space in range((filas-(i+1))):
        print " ",
    for j in range(i+1):
        print "*",
        if j < i:
            print "o",
    print ""
    
