import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np
%matplotlib inline

y = [1,2,3,4,10]
x = [1,2,3,4,10]

line, = plt.plot(x, y, "-", linewidth=5.0) # linewidth means the width of the line
line.set_antialiased(False) # this removes the blur

plt.plot(x, y, "ro") # r means red o means o which makes the plot represent points instead of a line
plt.axis([0, 6, 0, 20])

sequence = np.arange(0.0, 10.0, 0.2)
plt.plot(x, y, "r--", sequence, sequence**2, "gs") # represents two functions in one plot; r-- means red and dashed; gs means green and squares

plt.plot(x, y, "r--", sequence, sequence**2, "gs", sequence, sequence**3, "b^") # represents two functions in one plot; r-- means red and dashed; gs means green and squares;
# b^ means blue and with triangles

lines = plt.plot(sequence, sequence, sequence, sequence**2)
plt.setp(lines, color="r", linewidth=2.0)
plt.show()

lines = plt.plot(sequence, sequence, sequence, sequence**2)
plt.setp(lines, "color", "r", "linewidth", 2.0)
plt.show()

plt.plot(sequence, sequence, "r.", sequence, sequence**2, "g:", marker="+", animated=True)
plt.setp(lines) #shows all parameters
plt.show()


# Representing functions

def f(x):
    return np.exp(-x)*np.cos(2*np.pi*x)

x1 = np.arange(0.0, 5.0, 0.1)
x2 = np.arange(0.0, 5.0, 0.2)

plt.figure(1)
plt.subplot(211) # length:height ratio for plot 1 by default is 111 the numbers actually mean 2 rows and 1 column. The third one represents the figure whose data
# is just going to be introduced
plt.plot(x1, f(x1), "ro", x2, f(x2))

plt.subplot(212) # length:height ratio for plot 2
plt.plot(x1, f(x1), "go")

# Once you have passed one figure, you can still go back to a certain plot in a given figure

plt.figure(1)
plt.subplot(211) # length:height ratio for plot 1 by default is 111 the numbers actually mean 2 rows and 1 column. The third one represents the figure whose data
# is just going to be introduced
plt.plot(x1, f(x1), "ro", x2, f(x2))

plt.subplot(212) # length:height ratio for plot 2
plt.plot(x1, f(x1), "go")

plt.figure(2)
plt.plot([1,5,10])

plt.figure(1)
plt.subplot(211)
plt.title("This is a plot")
plt.close()

# plt.hold() erases the function represented in the last plot it is still the focus (haven't stated another one or closed the last one) and then the next function will
# be represented in the same plot

# Adding text to a plot

mu = 100
sigma = 20

x = mu+sigma*np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, normed=1, facecolor="g", alpha=0.6)
plt.xlabel("numeros aleatorios $N(\mu,\sigma)$", fontsize=15, color="green")
plt.ylabel("probabilidad de que al generarlos aleatoriamente se genere dicho numero")
plt.title("simplemente numeros aleatorios, literalmente. No, te lo digo de verdad, son aleatorios")
plt.text(40, 0.015, "$\mu=100,\ \sigma=20$")
plt.ylim(0, 0.03)
plt.grid(True)
plt.annotate("Maximo", xy=(105,0.02), xytext=(110, 0.025), arrowprops = dict(facecolor = "blue", shrink = 0.05))
plt.show()
plt.close()


# Changing the scale
mu = 0.5
sd = 0.3

y = mu+ sd*np.random.randn(1000)
y = y[(y>0)&(y<1)]
y.sort()
x = np.arange(len(y))

plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.plot(x, y)
plt.yscale("linear")
plt.xscale("linear")
plt.title("Escala lineal")
plt.grid(True)

plt.subplot(222)
plt.plot(x, y)
plt.xscale("log")
plt.title("Escala logaritmica")
plt.grid(True)

plt.subplot(223)
plt.plot(x, y-y.mean())
plt.yscale("symlog", linthreshy=0.01)
plt.title("Escala logaritmica simetrica")
plt.grid(True)

plt.subplot(224)
plt.plot(x, y)
plt.yscale("logit")
plt.title("Escala logistica")
plt.gca().yaxis.set_minor_formatter(NullFormatter())
plt.grid(True)

plt.subplots_adjust(top = 0.92, bottom = 0.08, left = 0.10, right = 0.95, hspace = 0.45, wspace = 0.4)


# More configuration parameters for plots
plt.figure(figsize=(10,8))
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
S, C = np.sin(x), np.cos(x)
plt.plot(x, S, color = "green", linestyle = "-", label = "Sin")
plt.plot(x, C, color = "blue", linestyle = "--", label = "Cos")
plt.xlim(-4,4)
plt.ylim(S.min()*1.2, S.max()*1.2)
plt.xticks(np.linspace(-4, 4, 9, endpoint = True))
plt.yticks( [-1, 1], ["-1", "+1"])
ax = plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data", 0))
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data", 0))
plt.legend(loc = "upper left")

# making changes in axis labels

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.3))

plt.show()
