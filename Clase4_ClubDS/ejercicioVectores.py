import numpy as np

# Creación de vectores
vector_a = np.array([4, 2, 8])
vector_b = np.array([1, 5, 2])

# Suma
suma = vector_a + vector_b
print("Suma de vectores:")
print(suma)

# Producto escalar
producto_escalar = 3 * vector_a
print("\nProducto escalar de vector A por 3:")
print(producto_escalar)

# Producto punto
producto_punto = np.dot(vector_a, vector_b)
print("\nProducto punto de vectores:")
print(producto_punto)