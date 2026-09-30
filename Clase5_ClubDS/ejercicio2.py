import numpy as np
import matplotlib.pyplot as plt

horas_estudio = np.array([1, 2, 2, 3, 4, 5, 5, 6, 7, 8]),
calificaciones = np.array([55, 58, 62, 65, 70, 75, 78, 82, 88, 92])

# Covarianza
covarianza = np.cov(horas_estudio, calificaciones)[0, 1] # Fila 0 (1) y columna 1 (2)

# Coeficiente de correlación
correlacion = np.corrcoef(horas_estudio, calificaciones)[0, 1]

print("Covarianza: ", covarianza)
print("\nCorrelación de Pearson: ", correlacion)

# Visualización (scatter plot)
plt.scatter(horas_estudio, calificaciones) # scatter genera el gráfico

plt.title("Relación entre horas de estudio y calificaciones")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificaciones")

plt.grid(True)
plt.show()