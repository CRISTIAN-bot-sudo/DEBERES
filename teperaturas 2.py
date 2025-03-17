def calcular_promedio_temperaturas(datos):
    """
    Calcula el promedio de temperatura de cada ciudad.

    Parámetros:
    - datos (list[list[float]]): Matriz donde cada fila representa una ciudad y
      cada columna representa la temperatura promedio de una semana.

    Retorna:
    - list[float]: Lista con el promedio de temperatura de cada ciudad.
    """
    promedios = [sum(ciudad) / len(ciudad) for ciudad in datos]
    return promedios


# Ejemplo de datos: 3 ciudades con 4 semanas de temperaturas
datos_temperaturas = [
    [20.5, 22.0, 19.8, 21.2],  # Ciudad 1
    [25.3, 26.1, 24.7, 27.0],  # Ciudad 2
    [18.9, 19.5, 20.0, 17.8]  # Ciudad 3
]

# Cálculo de promedios
promedios = calcular_promedio_temperaturas(datos_temperaturas)

# Mostrar resultados
for i, promedio in enumerate(promedios, start=1):
    print(f"Ciudad {i}: {promedio:.2f}°C")
