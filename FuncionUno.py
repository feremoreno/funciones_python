def invertir_cadena(cadena):
    cadena_invertida = ""
    # Iterar sobre la cadena desde el último carácter hasta el primero
    for i in range(len(cadena) - 1, -1, -1):
        cadena_invertida += cadena[i]  # Agregar cada carácter al resultado
    return cadena_invertida

# Solicitar que se ingrese una cadena
entrada = input("Introduce una cadena: ")
# Llamar a la función e imprimir el resultado
resultado = invertir_cadena(entrada)
print("Cadena invertida:", resultado)