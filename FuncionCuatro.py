def convertir_a_titulo(cadena):
    # Utilizar la función title() para convertir la cadena al formato título
    return cadena.title()

# Solicitar que ingrese una cadena
entrada = input("Introduce una cadena: ")
# Llamar a la función e imprimir el resultado
resultado = convertir_a_titulo(entrada)
print("Cadena en formato título:", resultado)