def buscar_palabra_h(palabra, sopa, m, n):
    f = False
    for row in sopa:
        x = 0
        while x < n:
            if m-x >= len(palabra):
                if row[x:(x+len(palabra))] == palabra:
                    print y, x
                    f = True
                    x = n
                    y = m
            x += 1
        if f == False:
            for reversed(row) in sopa:
                x = 0
                while x < n:
                    if m-x >= len(palabra):
                        if row[x:(x+len(palabra))] == palabra:
                            print y, x
                            f = True
                            x = n
                            y = m
                    x += 1
    return f

# def buscar_palabra_v(palabra, sopa, m, n):
#     f = False
#     y = 0
#     while y < m:
#         x = 0
#         while x < n:
#             if m-x >= len(palabra):
#                 if sopa[y:(y+len(palabra))][x] == palabra:
#                     print y, x
#                     f = True
#                     x = n
#                     y = m
#             x += 1
#         y += 1
#         if f == False:
#             while y > 0:
#                 x = n
#                 while x > 0:
#                     if x-len(palabra) >= 0:
#                         if sopa[y:y-len(palabra)][x] == palabra[::-1]:
#                             print y, x
#                             f = True
#                             x = n
#                             y = m
#                     x += 1
#                 y += 1
#     return f
m = input("Introduzca numero de filas: ")
n = input("Introduzca numero de columnas: ")
matriz = []
y = 0
while y < m:
    x = 0
    fila = []
    while x < n:
        fila.append(raw_input())
        x += 1
    matriz.append(fila)
    y += 1
x = input("numero de palabras")
y = 0
palabras = []
while y < x:
    palabras.append(raw_input("introduce palabra"))
    y += 1
for palabra in palabras:
    p = buscar_palabra_h(palabra, sopa, m, n)
    if p == False:
        buscar_palabra_v(palabra, sopa, m, n)
