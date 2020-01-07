import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19990519)

dist1 = 100*np.random.rand(50)
dist2 = 50*np.random.rand(25)
dist3 = 100+100*np.random.rand(10)
dist4 = -100*np.random.rand(10)

data = np.concatenate((dist1, dist2, dist3, dist4))

plt.boxplot(data)

plt.boxplot(data, notch=True)

# Boxplot con los outliers personalizados
greendiamonds = dict(markerfacecolor = "g", marker="D")
plt.boxplot(data, notch = True, flierprops = greendiamonds)

# Boxplot sin outliers

plt.boxplot(data, showfliers = False)

# Boxplot en horizontal

plt.boxplot(data, vert = False)

# Boxplot con bigotes de tamaño distinto al por defecto

plt.boxplot(data, whis=0.75)
plt.boxplot(data, whis=3) # Si se pide que los bigotes tengan una longitud mayor a la necesaria para eliminar los outliers, se aplica la normade que los bigotes van hasta el valor minimo y maximo
plt.boxplot(data, whis=0)
