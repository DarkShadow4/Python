import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mu = 10, 20
sigma = 5, 2
dist = pd.DataFrame(np.random.normal(loc = mu, scale = sigma, size = (1000, 2)), columns=["x1", "x2"])
dist
dist.agg(["min", "max", "mean", "std"])

# Densidad y función de probabilidad

fig, ax = plt.subplots()
dist.plot.kde(ax = ax, legend = False, title = "Histograma de dos normales") # kde stands for kernel density estimator
dist.plot.hist(density = True, ax = ax)
ax.set_ylabel("probabilidad")
ax.grid(axis = "y", alpha = 0.75)
ax.set_facecolor("#d5d5d5")


from scipy import stats
dist = stats.norm() # Distribución normal teórica N(0,1) -exp(-x**2/2)/sqrt(2*pi)
sample = dist.rvs(size = 1000)
x = np.linspace(start = stats.norm.ppf(0.1), stop = stats.norm.ppf(0.99), num = 250)
gkde = stats.gaussian_kde(dataset = sample)

fig, ax = plt.subplots()
ax.plot(x, dist.pdf(x), linestyle = "solid", c = "green", lw = 4, alpha = 0.9, label = "Distribución normal teórica") #pdf stands for probability density function
ax.plot(x, gkde.evaluate(x), linestyle = "dotted", c = "red", lw=3, label="PDF estimada con KDE")
ax.legend(loc="best", frameon=False)
ax.set_title("Normal analítica vs estimada")
ax.text(0,0.10, r"$f(x) = \frac{e^{-x^2/2}}{\sqrt{2\pi}}$", fontsize = 20)
