x = (1,2,3,2,4,2,3,4,4,3,2,4,1,50,37,42)

def frecuencia_abs(seq) -> dict:
    """
    Funcion que crea un diccionario con las frecuencias
    absolutas de la secuencia proporcionada
    """
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist


fAbs = frecuencia_abs(x)

def ascii_hist(x):
    """
    Draws portrait ascii-like histogram
    """
    fAbs = frecuencia_abs(x)
    for k in sorted(fAbs):
        print("{0:5d} {1}".format(k, "+"*fAbs[k]))

ascii_hist(x)

import random
random.seed(2019)
values = [1,2,3,5,7,8,9,10]
freqs = (random.randint(5,20) for _ in values) # _ means value. we dont assign a variable name because we are not using those values
data = []
for k, v in zip(values, freqs):
    data.extend([k]*v)
data
ascii_hist(data)
