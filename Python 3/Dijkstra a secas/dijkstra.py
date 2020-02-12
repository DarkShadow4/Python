def minimo(D):
    minimo = 1e+100
    min = 0
    for i in range(len(D)):
        if D[i] < minimo:
            minimo = D[i]
            min = i
    return (min)


def  dijkstra(n,c,v0):
    # D[v]:  coste  del  camino  especial  optimo a v
    # D = [c[(v0 ,v)] if v!=v0 else 0 for v in  range(n)]
    D = c[v0] # D son los pesos de v0 a cada vértice
    # P[v]:  vertice  anterior  en el  camino  especial  optimo a v
    # como desde v0 a cada vértice hay camino, sin optimizar,
    # el camino a cada vértice es el camino directo independientemente del peso
    P = [v0 for v in range(n)]
    C = [v if v!=v0 for v in range(n)] # C es el vector de vértices sin optimizar
    while len(C) > 0:
        min = minimo(D)
        C.remove(min)
        for v in C: # actualizacion  de D y P # # TODO:  cambiar
            if (w,v) in c and D[w] + c[(w,v)] < D[v]:
                D[v] = D[w] + c[(w,v)]
                P[v] = w
    return D,P

tabla = [
    [0, 10, 50, 100, 30],
    [10, 0, 1e+100, 10, 1e+100],
    [50, 1e+100, 0, 20, 5],
    [100, 10, 20, 0, 50],
    [30, 1e+100, 5, 50, 0]
]
