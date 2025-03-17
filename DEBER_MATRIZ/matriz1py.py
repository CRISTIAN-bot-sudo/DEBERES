# Programa de Ordenación en una Matriz Bidimensional

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

def ordenar_fila_matriz(matriz, fila_indice):
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    matriz[fila_indice] = bubble_sort(matriz[fila_indice])

    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)

# Definir la matriz bidimensional
matriz = [
    [34, 12, 25],
    [88, 56, 43],
    [90, 11, 67]
]

# Solicitar al usuario la fila a ordenar
fila_a_ordenar = int(input("Introduce el número de la fila que deseas ordenar (0-2): "))

# Verificar que el índice esté dentro del rango
if 0 <= fila_a_ordenar < len(matriz):
    ordenar_fila_matriz(matriz, fila_a_ordenar)
else:
    print("El índice de la fila está fuera del rango permitido.")