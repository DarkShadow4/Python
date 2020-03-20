dividendo, divisor = input("Introduce la división con el formato Dividendo/divisor: ").split("/")

i = 0
resto = ""
cociente = ""
steps = []
while i < len(dividendo):
    resto += dividendo[i]
    steps.append("{0}{1}".format(" "*(i-1), resto)+" "*len(dividendo[i:]))
    cociente += str(int(resto)//int(divisor))
    resto = str(int(resto)%int(divisor))
    i += 1
steps.append("{0}{1}".format(" "*(i-1), resto)+" "*len(dividendo[i:])) # para mostrar el resto final

print("{0}  |{1}".format(dividendo, divisor)) # Dividendo y divisor
print("{0}  -{1}".format(" "*len(dividendo), "-"*len(divisor))) # Formato (omisible)
print(steps[0]+cociente) # primer cálculo y cociente
for i in range(1, len(steps)): # Los demás de cálculos y el resto final
    print(steps[i])

print("Done: Cociente={0} Resto={1}".format(int(cociente), int(resto))) # Solución de la división
