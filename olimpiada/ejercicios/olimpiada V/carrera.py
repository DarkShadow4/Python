posicion1 = input("Posición inicial canguro 1:")
longitud1 = input("Longitud de salto canguro 1:")
posicion2 = input("Posición inicial canguro 2:")
longitud2 = input("Longitud de salto canguro 2:")

# pf1 = pi1 + l1*t
# pf2 = pi2 + l2*t

# pf1 = pf2

# pf1 = pi1 + l1*t    pi1   l1
# ---------------- =  --- + -- = 1
# pf2 = pi2 + l2*t    pi2   l2



if (posicion1/posicion2) + (longitud1/longitud2) == 1:
    print "si"
else:
    print "no"
