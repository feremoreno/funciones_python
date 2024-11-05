def contar_vocales(cadena):
    # Definir las vocales en una lista
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    contador = 0
    
    # Iterar sobre cada carácter en la cadena
    for caracter in cadena:
        if caracter in vocales:
            contador += 1  # Incrementar el contador si es una vocal
    
    return contador

# Solicitar que ingrese una cadena
entrada = input("Introduce una cadena: ")
# Llamar a la función e imprimir el resultado
resultado = contar_vocales(entrada)
print("Número de vocales en la cadena:", resultado)