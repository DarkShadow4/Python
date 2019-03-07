def get_bebida_alcoholica_mas_consumida(bebidas, alcohol):
    tipos = [1, 2, 3, 4, 5, 6, 7, 8]
    assigned = list(sorted(zip(tipos, bebidas, alcohol), key=lambda x:x[1], reverse=True))
    max = False
    for i in assigned:
        if i[2] and max == False:
            max = True
            return i[0]

# def get_pueblo_mayor_consumo(assigned):
#     alcohol_total =
#     for i in assigned:


bebidas = [0, 0, 0, 0, 0, 0, 0, 10]
# for n_pueblo in range(1):
#     data = ""
#     print "Pueblo", n_pueblo+1
#     while data != "FIN":
#         data = raw_input()
#         if data != "FIN":
#             tipo_bebida, litros = data.split(" ")
#             tipo_bebida = int(tipo_bebida)
#             litros = int(litros)
#             bebidas[tipo_bebida-1] += litros


alcohol = [True, True, True, True, True, True, True, True]
# data = ""
# while data != "FIN":
#     data = raw_input()
#     if data != "FIN":
#         if alcohol[data] not True:
#             alcohol.append(int(data)-1)



print "El tipo de bebida mas bebida es la:", bebidas.index(max(bebidas))+1
print "El tipo de bebida con alcohol mas consumida es la:", get_bebida_alcoholica_mas_consumida(bebidas, alcohol)
