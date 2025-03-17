# Programa para calcular el promedio de temperaturas en una matriz 3D
import random

# Definir las dimensiones de la matriz (3 ciudades, 7 días, 4 semanas)
ciudades = ["Barcelona", "Paris", "Italia"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Crear la matriz 3D con valores aleatorios de temperatura entre 15 y 35 grados
matriz_temperaturas = [[[random.randint(15, 35) for _ in dias] for _ in range(semanas)] for _ in ciudades]

# Mostrar la matriz de temperaturas
def mostrar_temperaturas():
    for i, ciudad in enumerate(ciudades):
        print(f"\nTemperaturas en {ciudad}:")
        for semana in range(semanas):
            print(f"  Semana {semana + 1}: {matriz_temperaturas[i][semana]}")

# Calcular el promedio de temperaturas por ciudad y por semana
def calcular_promedios():
    print("\nPromedio de temperaturas por ciudad y semana:")
    for i, ciudad in enumerate(ciudades):
        for semana in range(semanas):
            promedio = sum(matriz_temperaturas[i][semana]) / len(dias)
            print(f"{ciudad} - Semana {semana + 1}: {promedio:.2f} °C")

# Mostrar resultados
mostrar_temperaturas()
calcular_promedios()
