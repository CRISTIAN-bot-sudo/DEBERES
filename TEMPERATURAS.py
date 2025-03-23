def calcular_promedio_temperaturas(datos):
    """
    Calcula la temperatura promedio de cada ciudad.

    Parámetros:
    - datos (list): Lista de listas donde cada sublista representa las temperaturas semanales de una ciudad.

    Retorna:
    - dict: Un diccionario con el nombre de la ciudad como clave y su temperatura promedio como valor.
    """
    promedios = {}
    for ciudad, temperaturas in datos.items():
        promedio = sum(sum(semana) for semana in temperaturas) / sum(len(semana) for semana in temperaturas)
        promedios[ciudad] = round(promedio, 2)
    return promedios


# Datos de ejemplo: temperaturas en 3 ciudades durante 4 semanas
datos_temperaturas = {
    "Ciudad_Alemania": [[30, 32, 31, 29], [28, 27, 26, 25], [29, 30, 31, 32], [33, 34, 35, 36]],
    "Ciudad_Portugal": [[20, 21, 22, 23], [24, 25, 26, 27], [28, 29, 30, 31], [32, 33, 34, 35]],
    "Ciudad_Suiza": [[15, 16, 17, 18], [19, 20, 21, 22], [23, 24, 25, 26], [27, 28, 29, 30]]
}

# Prueba de la función
resultado = calcular_promedio_temperaturas(datos_temperaturas)
print("Temperaturas promedio por ciudad:", resultado)

