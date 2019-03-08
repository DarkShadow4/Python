def get_total_bebidas(pueblos):
    bebidas = [0, 0, 0, 0, 0, 0, 0, 0]
    for drinks in pueblos:
        for drink in range(8):
            bebidas[drink] += drinks[drink]
    return bebidas

def get_bebida_alcoholica_mas_consumida(bebidas, alcohol):
    tipos = [1, 2, 3, 4, 5, 6, 7, 8]
    assigned = list(sorted(zip(tipos, bebidas, alcohol), key=lambda x:x[1], reverse=True))
    max = False
    for i in assigned:
        if i[2] and max == False:
            max = True
            return i[0]

def get_pueblo_mayor_consumo(pueblos, alchol):
    num_pueblo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    alcohol_por_pueblo = []
    for pueblo in pueblos:
        alcohol_pueblo = 0
        for bebida in range(8):
            if alcohol[bebida]:
                alcohol_pueblo += pueblo[bebida]
        alcohol_por_pueblo.append(alcohol_pueblo)
    comparacion = list(sorted(zip(num_pueblo, alcohol_por_pueblo), key=lambda i:i[1], reverse = True))
    return comparacion[0][0]

pueblos = [[0, 0, 0, 0, 0, 150, 20, 30], [0, 0, 0, 0, 0, 120, 0, 10], [0, 0, 0, 6000, 0, 150, 20, 30], [0, 0, 4000, 0, 0, 6150, 20, 30], [0, 20, 4000, 2000, 0, 6150, 20, 30]]
# for n_pueblo in range(1):
#     data = ""
#     print "Pueblo", n_pueblo+1
#     bebidas = [0, 0, 0, 0, 0, 0, 0, 0]
#     while data != "FIN":
#         data = raw_input()
#         if data != "FIN":
#             tipo_bebida, litros = data.split(" ")
#             tipo_bebida = int(tipo_bebida)
#             litros = int(litros)
#             bebidas[tipo_bebida-1] += litros
#     pueblos.append(bebidas)

alcohol = [True, True, True, True, True, False, True, True]
# data = ""
# while data != "FIN":
#     data = raw_input()
#     if data != "FIN":
#         if alcohol[data] not True:
#             alcohol.append(int(data)-1)

bebidas = get_total_bebidas(pueblos)

print "El tipo de bebida mas bebida es la:", bebidas.index(max(bebidas))+1
print "El tipo de bebida con alcohol mas consumida es la:", get_bebida_alcoholica_mas_consumida(bebidas, alcohol)
print "El pueblo que consume mas bebidas alcoholicas es el:", get_pueblo_mayor_consumo(pueblos, alcohol)
