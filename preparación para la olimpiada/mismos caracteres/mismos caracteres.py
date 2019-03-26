c1 = raw_input("Introduce cadena 1:")
c2 = raw_input("Introduce cadena 2:")

cc = ""
for c in c1:
    if c in c2:
        cc += c
print cc
