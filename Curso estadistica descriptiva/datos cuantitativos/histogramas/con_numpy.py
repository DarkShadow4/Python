import numpy as np
np.random.seed(2019)
np.set_printoptions(precision = 3)
x = np.random.laplace(loc=10, scale=3, size = 1000)
x[:10]
hist, bin_edges = np.histogram(x)
hist
bin_edges

# Lo que np.histogram hace para crear los intervalos

min_edge = min(x)
max_edge = x.max()

n_bins = 10
bin_edges = np.linspace(start=min_edge, stop=max_edge, num=n_bins+1, endpoint = True)
bin_edges

####

np.bincount() # Cuenta las frecuencias absolutas de números enteros (creo, porque no le veo sentido al vector que devuelve)
