def es_palindromo(palabra):
    # Convertir la palabra a minúsculas y eliminar espacios
    palabra_limpia = ''.join(palabra.lower().split())
    # Comparar la palabra con su inversa
    return palabra_limpia == palabra_limpia[::-1]

# Solicitar una palabra al usuario
palabra = input("Ingresa una palabra para verificar si es un palíndromo: ")

# Verificar si es un palíndromo y mostrar el resultado
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo. ')
else:
    print(f'"{palabra}" no es un palíndromo. ')
