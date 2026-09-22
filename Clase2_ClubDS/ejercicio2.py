import numpy as np

calificaciones = np.array([6, 7, 7, 8, 8, 8, 9, 10])

print("Media:", np.mean(calificaciones))
print("Mediana:", np.median(calificaciones))
print("Varianza:", np.var(calificaciones))
print("Desviación estándar:", np.std(calificaciones))