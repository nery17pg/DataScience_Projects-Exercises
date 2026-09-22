import statistics

grupo_A = [7, 7, 8, 8, 8, 8, 9, 9, 8, 8]
grupo_B = [5, 6, 7, 8, 8, 8, 9, 10, 10, 9]

for nombre, grupo in [("Grupo A", grupo_A), ("Grupo B", grupo_B)]:
    print("\n", nombre)
    print("Media:", statistics.mean(grupo))
    print("Mediana:", statistics.median(grupo))
    print("Moda:", statistics.mode(grupo))
    print("Rango:", max(grupo) - min(grupo))
    print("Varianza:", statistics.pvariance(grupo))
    print("Desviación estándar:", statistics.pstdev(grupo))
