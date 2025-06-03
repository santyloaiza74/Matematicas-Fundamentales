### Ejercicio 1 ###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
continente_poblacion = df.groupby('continent')['pop'].sum()
plt.figure(figsize=(10, 6))
continente_poblacion.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Población por Continente')
plt.ylabel('')
plt.show()


### Ejercicio 2 ###

esperanza_vida_promedio = df.groupby('continent')['lifeExp'].mean()
plt.figure(figsize=(10, 6))
esperanza_vida_promedio.plot(kind='bar', color='skyblue')
plt.title('Esperanza de Vida Promedio por Continente')
plt.xlabel('Continente')
plt.ylabel('Esperanza de Vida (años)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.show()