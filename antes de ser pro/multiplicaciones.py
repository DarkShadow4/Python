multiplicando = raw_input("Introduce el multiplicando (3 cifras):")
multiplicador = raw_input("Introduce el multiplicador (3 cifras):")
print "El producto de la multiplicación es:", int(multiplicando)*int(multiplicador)
print "El proceso es:"
print "   ", multiplicando
print " x ", multiplicador
print "--------"
print "   ", int(multiplicando)*int(multiplicador[0])
print " ", int(multiplicando)*int(multiplicador[1]), "x"
print "", int(multiplicando)*int(multiplicador[2]), "xx"
print "--------"
print int(multiplicando)*int(multiplicador)
