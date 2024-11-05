def frecuencia_caracteres(cadena):
    # Inicializar un diccionario para almacenar la frecuencia
    frecuencia = {}
    
    # Iterar sobre cada carácter en la cadena
    for caracter in cadena:
        # Si el carácter ya está en el diccionario, incrementar su conteo
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            # Si no está, inicializarlo en 1
            frecuencia[caracter] = 1
    
    return frecuencia

# Solicitar al usuario que ingrese una cadena
entrada = input("Introduce una cadena: ")
# Llamar a la función e imprimir el resultado
resultado = frecuencia_caracteres(entrada)
print("Frecuencia de cada carácter:", resultado)