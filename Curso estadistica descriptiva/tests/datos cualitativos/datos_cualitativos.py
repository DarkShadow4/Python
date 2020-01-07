import pandas as pd


Falumnos = pd.crosstab(index=alumnos, columns="count")

FRedades = pd.crosstab(index=edades, columns="count") / pd.crosstab(index=edades, columns="count").sum()


altura = range(10)
peso = range(11, 21)

Faltura_peso = pd.crosstab(index=altura, columns=peso)

Faltura_peso = pd.crosstab(index=altura, columns=peso)/pd.crosstab(index=altura, columns=peso).sum()
Faltura_peso
