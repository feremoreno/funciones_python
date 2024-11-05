def es_palindromo(cadena):
    # Limpiar la cadena: eliminar espacios y convertir a minúsculas
    cadena_limpia = ''.join(cadena.split()).lower()
    
    # Inicializar dos punteros
    izquierda = 0
    derecha = len(cadena_limpia) - 1

    # Comparar caracteres desde los extremos hacia el centro
    while izquierda < derecha:
        if cadena_limpia[izquierda] != cadena_limpia[derecha]:
            return False  # No es un palíndromo
        izquierda += 1
        derecha -= 1
    
    return True  # Es un palíndromo

# Solicitar que ingrese una cadena
entrada = input("Introduce una cadena: ")
# Llamar a la función e imprimir el resultado
if es_palindromo(entrada):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")