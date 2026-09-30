import pandas as pd

# Dataset a utilizar
datos = {
    "horas_estudio": [1, 2, 2, 3, 4, 5, 5, 6, 7, 8],
    "calificaciones": [55, 58, 62, 65, 70, 75, 78, 82, 88, 92]
}

df = pd.DataFrame(datos)

print(df)

# Calculamos matriz de correlación :)
correlaciones = df.corr()

print("\nMatriz de correlación:")
print(correlaciones)