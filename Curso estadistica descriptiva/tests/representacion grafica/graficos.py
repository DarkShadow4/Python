import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

# Ejercicio 1

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)
plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.plot(X, Y - 1, color='blue', alpha=1.00)
plt.fill_between(X, Y + 1, 1, color = "blue", alpha=0.3)
plt.fill_between(X, Y - 1, -1, where=Y - 1>-1.0, color = "blue", alpha=0.3)
plt.fill_between(X, Y - 1, -1, where=Y - 1<-1.0, color = "red", alpha=0.3)
plt.xticks(())
plt.yticks(())

# Ejercicio 2

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

plt.scatter(X,Y, c=np.arctan2(Y,X), alpha=0.5)
plt.xlim=(-2.5, 2.5)
plt.xticks(())
plt.ylim=(-2.5, 2.5)
plt.yticks(())
plt.show()

# Ejercicio 3

plt.figure(figsize=(10, 8))
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')
for x, y in zip(X, Y2):
        plt.text(x, -y - 0.1, '%.2f' % y, ha='center', va='bottom')
plt.ylim=(-2, + 2)
plt.xticks(())
plt.yticks(())
plt.show()

# Ejercicio 4

n = 20
Z = np.ones(n)
Z[-1] *= 2
plt.axes([0.025, 0.025, 0.95, 0.95])
plt.pie(Z, explode=Z*.05, colors = ['%f' % (i/float(n)) for i in range(n)])
plt.axis('equal')
plt.xticks(())
plt.yticks()
plt.show()
