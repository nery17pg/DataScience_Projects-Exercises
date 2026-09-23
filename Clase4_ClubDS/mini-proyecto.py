import numpy as np

# Creamos matriz del problema
calificaciones = np.array([
    [9, 8, 10],
    [7, 9, 8],
    [10, 9, 9],
    [8, 7, 8],
    [9, 10, 9]
])

print("Matriz de calificaciones:")
print(calificaciones)

# Calcular el promedio de calificaciones por alumno
# Nota: axis=1 nos ayuda a calcular el promedio a lo largo de las filas (vectores o por alumno)
promedio_alumnos = np.mean(calificaciones, axis=1)
print("\nPromedio de calificaciones por alumno:")
print(promedio_alumnos)

# Calcular el promedio de calificaciones por asignatura
# Nota: axis=0 nos ayuda a calcular el promedio a lo largo de las columnas (variables o por asignatura)
promedio_asignatura = np.mean(calificaciones, axis=0)
print("\nPromedio de calificaciones por asignatura:")
print(promedio_asignatura)

# Identificar el alumno con el mayor promedio
top_alumno = np.argmax(promedio_alumnos)
print("\nAlumno con mayor promedio:")
print(top_alumno)

# Identificar el alumno con el menor promedio
bajito_alumno = np.argmin(promedio_alumnos)
print("\nAlumno con menor promedio:")
print(bajito_alumno)

# Identificar la asignatura con mayor promedio
top_asignatura = np.argmax(promedio_asignatura)

materias = ["Matemáticas", "Programación", "Estadística"]

print("\nAsignatura con mayor promedio:")
print(top_asignatura)
print(materias[top_asignatura])
print(promedio_asignatura)
print(promedio_asignatura[top_asignatura])