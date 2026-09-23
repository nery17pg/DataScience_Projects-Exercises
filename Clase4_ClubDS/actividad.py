import numpy as np

# Crear la matriz del problema
calificaciones = np.array([
    [9, 8, 10],
    [7, 9, 8],
    [10, 9, 9],
    [8, 7, 8],
    [9, 10, 9]
])

print("Matriz de calificaciones:")
print(calificaciones)

print("\nCalificación del primer alumno en la materia de Programación:")
print(calificaciones[0, 1])

print("\nCalificaciones de Yatziri:")
print(calificaciones[1])

print("\nCalificaciones de Estadística:")
print(calificaciones[:, 2])

# Obtener dimensiones de la matriz
print("\nDimensiones de la matriz:")
print(calificaciones.shape) # Método utilizado para ello