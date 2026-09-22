import statistics

calificaciones = [6, 7, 7, 8, 8, 8, 9, 10]

media = statistics.mean(calificaciones)
mediana = statistics.median(calificaciones)
moda = statistics.mode(calificaciones)
varianza = statistics.pvariance(calificaciones)
desviacion = statistics.pstdev(calificaciones)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion)