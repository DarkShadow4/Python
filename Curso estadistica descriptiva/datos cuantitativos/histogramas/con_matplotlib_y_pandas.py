import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
np.random.seed(2019)
np.set_printoptions(precision = 3)
x = np.random.laplace(loc=10, scale=3, size = 1000)

n, bins, patches = plt.hist(x = x, bins = "auto", color = "#00ff00", alpha = 0.80, rwidth=0.7)
plt.grid(axis="y", alpha=0.6)
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("IDK they are just random")

# Pandas

size, scale = 1000, 10
data = pd.Series(np.random.gamma(scale, size = size))
data.plot.hist(grid = True, bins = 20, rwidth = 0.8, color = "#f0f000")
plt.title("Distribución gamma")
