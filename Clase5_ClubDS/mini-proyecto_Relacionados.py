import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = {
    "horas_estudio": [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9],
    "calificaciones": [55, 58, 62, 65, 70, 75, 78, 82, 88, 92, 40]
}

df = pd.DataFrame(datos)

print(df)

# Covarianza
covarianza = np.cov(df["horas_estudio"], df["calificaciones"])[0, 1]
print("\nCovarianza: ", covarianza)

# Correlación de Pearson
correlacion = np.corrcoef(df["horas_estudio"], df["calificaciones"])[0, 1]
print("\nCorrelación: ", correlacion)

# Matriz de correlación
print("\nMatriz de correlación:")
print(df.corr()) # Muestra la matriz de correlación de todas las columnas

# Visualización con outlier
plt.scatter(df["horas_estudio"], df["calificaciones"])

plt.title("Relación entre horas de estudio y calificaciones")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificaciones")

plt.grid(True)
plt.show()

# QUITEMOS EL OUTLIER :P
df_sin_outlier = df[df["calificaciones"] != 40] 

# Covarianza sin outlier
covarianza_sin_outlier = np.cov(df_sin_outlier["horas_estudio"], df_sin_outlier["calificaciones"])[0, 1]
print("\nCovarianza sin outlier: ", covarianza_sin_outlier)

# Correlación sin outlier
correlacion_sin_outlier = np.corrcoef(df_sin_outlier["horas_estudio"], df_sin_outlier["calificaciones"])[0, 1]

# Visualización sin outlier
print("\nCorrelación sin outlier: ", correlacion_sin_outlier)

plt.scatter(df_sin_outlier["horas_estudio"], df_sin_outlier["calificaciones"])

plt.title("Relación entre horas de estudio y calificaciones")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificaciones")

plt.grid(True)
plt.show()