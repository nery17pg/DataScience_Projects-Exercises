import numpy as np

# Creación de matrices
matriz_a = np.array([[3, 1], [4, 2]])
matriz_b = np.array([[2, 0], [1, 5]])

# Suma
suma = matriz_a + matriz_b
print("\nSuma de matrices:")
print(suma)

# Producto de matrices
producto = np.dot(matriz_a, matriz_b)
print("\nProducto de matrices:")
print(producto)