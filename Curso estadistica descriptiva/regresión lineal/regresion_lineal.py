import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()
type(diabetes)
type(diabetes.data)
diabetes.data.shape
x = diabetes.data[:, np.newaxis, 2]
y = diabetes.target

modelo = linear_model.LinearRegression()
modelo.fit(x, y)
modelo.coef_
modelo.intercept_

plt.scatter(x, y, color = "black")
plt.plot(x, modelo.predict(x), color = "cyan", linewidth = 3)
mean_squared_error(y, modelo.predict(x))
r2_score(y, modelo.predict(x))


# Entrenamiento y validacion

x_train = x[:-60]
x_test = x[-60:]

y_train = y[:-60]
y_test = y[-60:]

## Entrenamiento

modelo = linear_model.LinearRegression
modelo.fit(x_train, y_train)
modelo.coef_
modelo.intercept_

plt.scatter(x_train, y_train, color = "black")
plt.plot(x_train, modelo.predict(x_train), color = "cyan", linewidth = 3)
mean_squared_error(y_train, modelo.predict(x_train))
r2_score(y_train, modelo.predict(x_train))

## Validacion

y_pred = modelo.predict(x_test)
mean_squared_error(y_test, y_pred)
r2_score(y_test, y_pred)
