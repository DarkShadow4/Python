def get_bebida_alcoholica_mas_consumida(bebidas, alcohol):
    bebidas1 = bebidas
    bebidas1.sort(reverse = True)
    max = False
    print bebidas.index(bebidas1[0])
    # for i in bebidas1:
    #     print bebidas.index(i)
    #     if (bebidas.index(i)+1 in alcohol) and max == False:
    #         # print bebidas.index(i)
    #         pass

bebidas = [0, 0, 0, 0, 0, 0, 0, 0]
for n_pueblo in range(5):
    data = ""
    while data != "FIN":
        data = raw_input()
        if data != "FIN":
            tipo_bebida, litros = data.split(" ")
            tipo_bebida = int(tipo_bebida)
            litros = int(litros)
            bebidas[tipo_bebida-1] += litros
alcohol = []
data = ""
while data != "FIN":
    data = raw_input()
    if data not in alcohol:
        alcohol.append(data)
print "El tipo de bebida mas bebida es la:", bebidas.index(max(bebidas))+1

print "El tipo de bebida con alcohol mas consumida es la:", get_bebida_alcoholica_mas_consumida(bebidas, alcohol)
