# Programa de Búsqueda en una Matriz Bidimensional

def buscar_valor(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                return fila, columna
    return None

# Definir la matriz bidimensional
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Solicitar al usuario el valor a buscar
valor_a_buscar = int(input("Introduce el valor que deseas buscar: "))

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion} (fila {posicion[0]}, columna {posicion[1]}).")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
