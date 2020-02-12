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
    D = [c[(v0 ,v)] if v!=v0 else 0 for v in  range(n)]
    # P[v]:  vertice  anterior  en el  camino  especial  optimo a v
    P = [v0 for v in range(n)]
    C = [v for v in range(n) if v!=v0]
    while  len(C) > 0:
        minimo = 1e+100 # infinito
        for v in C:
            if D[v] < minimo:
                minimo = D[v]
                w=v
                C.remove(w)
        for v in C: # actualizacion  de D y P
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
