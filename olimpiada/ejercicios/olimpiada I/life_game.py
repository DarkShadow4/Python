celda = {
    "viva": "#",
    "vacia": "-"
}

def generar_tablero():
    """Genera un tablero vacio"""
    n = input("introduce numero de filas: ")
    m = input("introduce numero de columnas: ")
    tablero = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(celda["vacia"])
        tablero.append(fila)
    return tablero, n, m

def mostrar_tablero(tablero):
    """Muestra el tablero"""
    for fila in tablero:
        for celda in fila:
            print celda,
        print ""

def dar_vida(tablero):
    """Introduce las celulas en el tablero"""
    x, y = 0, 0
    while y >= 0 and x >= 0:
        y, x = raw_input("introduce coordenadas").split()
        y = int(y)-1
        x = int(x)-1
        if y >= len(tablero) or x >= len(tablero[0]):
            print "coordenada erronea"
        else:

            if y >= 0 and x >= 0:
                tablero[y][x] = celda["viva"]

# def comprobar_vecindario(tablero, y, x, vecinas_para_sobrevivir, vecinas_para_nacer):
#     """Comprueba el numero de celulas vecinas"""
#     merece_vivir = False
#     cv = 0
#     y = y
#     x = x
#     pre_y = y-1
#     pre_x = x-1
#     if y <= len(tablero)-2:
#         post_y = y+1
#     else:
#         post_y = 0
#     if x <= len(tablero[y])-2:
#         post_x = x+1
#     else:
#         post_x = 0
#     if tablero[pre_y][pre_x] == celda["viva"]:
#         cv += 1
#     if tablero[pre_y][x] == celda["viva"]:
#         cv += 1
#
#     if tablero[pre_y][post_x] == celda["viva"]:
#         cv += 1
#     if tablero[y][pre_x] == celda["viva"]:
#         cv += 1
#
#     if tablero[y][post_x] == celda["viva"]:
#         cv += 1
#
#     if tablero[post_y][pre_x] == celda["viva"]:
#         cv += 1
#
#     if tablero[post_y][x] == celda["viva"]:
#         cv += 1
#
#     if tablero[post_y][post_x] == celda["viva"]:
#         cv += 1
#     cell = tablero[y][x]
#     tablero[y][x] = "·"
#     mostrar_tablero(tablero)
#     tablero[y][x] = cell
#     if tablero[y][x] == celda["viva"]:
#         print "vecinas_para_sobrevivir:", vecinas_para_sobrevivir
#         for vps in vecinas_para_sobrevivir:
#             if cv == vps:
#                 merece_vivir = True
#             print "vps", vps, "cv", cv, "cv == vps", cv == vps, "merece_vivir", merece_vivir
#         if merece_vivir == False:
#             tablero[y][x] = celda["vacia"]
#     else:
#         print "vecinas_para_nacer:", vecinas_para_nacer
#         if tablero[y][x] == celda["vacia"]:
#             for vpn in vecinas_para_nacer:
#                 if cv == vpn:
#                     merece_vivir = True
#                 print "vpn", vpn, "cv", cv, "cv == vpn", cv == vpn, "merece_vivir", merece_vivir
#             if merece_vivir == True:
#                 tablero[y][x] = celda["viva"]

def comprobar_vecindario(tablero, y, x, vecinas_para_sobrevivir, vecinas_para_nacer):
    """Comprueba el numero de celulas vecinas"""
    merece_vivir = False
    cv = 0
    pre_y = y
    pre_x = x
    post_x = None
    post_y = None
    if y <= len(tablero)-2:
        post_y = y+1
    # else:
        # post_y = 0
    if x <= len(tablero[y])-2:
        post_x = x+1
    # else:
        # post_x = 0
    if tablero[pre_y][pre_x] == celda["viva"]:
        cv += 1
    if tablero[pre_y][x] == celda["viva"]:
        cv += 1
    if tablero[y][pre_x] == celda["viva"]:
        cv += 1
    if (post_x is None) and (post_y is None):
        pass
    else:
        if post_x is None:
            if tablero[post_y][pre_x] == celda["viva"]:
                cv += 1
            if tablero[post_y][x] == celda["viva"]:
                cv += 1
        if post_y is None:
            if tablero[pre_y][post_x] == celda["viva"]:
                cv += 1
            if tablero[y][post_x] == celda["viva"]:
                cv += 1
        if (post_x is not None) and (post_y is not None):
            if tablero[post_y][post_x] == celda["viva"]:
                cv += 1

    cell = tablero[y][x]
    tablero[y][x] = "·"
    mostrar_tablero(tablero)
    tablero[y][x] = cell
    print cv
    if tablero[y][x] == celda["viva"]:
        print "vecinas_para_sobrevivir:", vecinas_para_sobrevivir
        for vps in vecinas_para_sobrevivir:
            if cv == vps:
                merece_vivir = True
            print "vps", vps, "cv", cv, "cv == vps", cv == vps, "merece_vivir", merece_vivir
        if merece_vivir == False:
            tablero[y][x] = celda["vacia"]
    else:
        print "vecinas_para_nacer:", vecinas_para_nacer
        if tablero[y][x] == celda["vacia"]:
            for vpn in vecinas_para_nacer:
                if cv == vpn:
                    merece_vivir = True
                print "vpn", vpn, "cv", cv, "cv == vpn", cv == vpn, "merece_vivir", merece_vivir
            if merece_vivir == True:
                tablero[y][x] = celda["viva"]

def simular_evolucion(n_generaciones, tablero, vecinas_para_sobrevivir, vecinas_para_nacer):
    for i in range(n_generaciones):
        print "generacion", i+1
        y = 0
        for fila in tablero:
            x = 0
            for celda in fila:
                comprobar_vecindario(tablero, y, x, vecinas_para_sobrevivir, vecinas_para_nacer)
                x += 1
            y += 1

        mostrar_tablero(tablero)

tablero, n, m = generar_tablero()
dar_vida(tablero)
mostrar_tablero(tablero)

vecinas_para_sobrevivir = []
for x in raw_input("Numero de celulas vecinas para sobrevivir: ").split():
    if x not in vecinas_para_sobrevivir:
        vecinas_para_sobrevivir.append(int(x))

vecinas_para_nacer = []
for x in raw_input("Numero de celulas vecinas para nacer: ").split():
    if x not in vecinas_para_nacer:
        vecinas_para_nacer.append(int(x))
n_generaciones = input("Introduce numero de generaciones a simular:")
simular_evolucion(n_generaciones, tablero, vecinas_para_sobrevivir, vecinas_para_nacer)


# def comprobar_vecindario(tablero, y, x, vecinas_para_sobrevivir, vecinas_para_nacer):
#     """Comprueba el numero de celulas vecinas"""
#     merece_vivir = False
#     cv = 0
#     y = y-1
#     x = x-1
#     pre_y = y-1
#     pre_x = x-1
#     if y <= len(tablero)-1:
#         post_y = y+1
#     # else:
#         # post_y = 0
#     if x <= len(tablero[y])-1:
#         post_x = x+1
#     # else:
#         # post_x = 0
#     if tablero[pre_y][pre_x] == celda["viva"]:
#         cv += 1
#     if tablero[pre_y][x] == celda["viva"]:
#         cv += 1
#
#     if tablero[pre_y][post_x] == celda["viva"]:
#         cv += 1
#     if tablero[y][pre_x] == celda["viva"]:
#         cv += 1
#
#     if tablero[y][post_x] == celda["viva"]:
#         cv += 1
#
#     if tablero[post_y][pre_x] == celda["viva"]:
#         cv += 1
#
#     if tablero[post_y][x] == celda["viva"]:
#         cv += 1
#
#     if tablero[post_y][post_x] == celda["viva"]:
#         cv += 1
#     cell = tablero[y][x]
#     tablero[y][x] = "·"
#     mostrar_tablero(tablero)
#     tablero[y][x] = cell
#     if tablero[y][x] == celda["viva"]:
#         print "vecinas_para_sobrevivir:", vecinas_para_sobrevivir
#         for vps in vecinas_para_sobrevivir:
#             if cv == vps:
#                 merece_vivir = True
#             print "vps", vps, "cv", cv, "cv == vps", cv == vps, "merece_vivir", merece_vivir
#         if merece_vivir == False:
#             tablero[y][x] = celda["vacia"]
#     else:
#         print "vecinas_para_nacer:", vecinas_para_nacer
#         if tablero[y][x] == celda["vacia"]:
#             for vpn in vecinas_para_nacer:
#                 if cv == vpn:
#                     merece_vivir = True
#                 print "vpn", vpn, "cv", cv, "cv == vpn", cv == vpn, "merece_vivir", merece_vivir
#             if merece_vivir == True:
#                 tablero[y][x] = celda["viva"]
