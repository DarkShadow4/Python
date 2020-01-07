import pandas as pd

df = pd.read_csv("../../../../r-basic/data/run.csv")
len(df)
df


len(df.loc[df.genero == "H"])
len(df.loc[df.genero == "M"])

df['pulso.variacion'] = ((df['pulso.despues'] - df['pulso.antes'])/df['pulso.despues'])*100
df.groupby('hace.deporte').aggregate('pulso.variacion').mean()
