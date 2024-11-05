def palabra_mas_larga(oracion):
    # Dividir la oración en palabras
    palabras = oracion.split()
    
    # Inicializar la variable para la palabra más larga
    max_palabra = ""
    
    # Iterar sobre cada palabra en la lista
    for palabra in palabras:
        # Verificar si la longitud de la palabra actual es mayor que la de max_palabra
        if len(palabra) > len(max_palabra):
            max_palabra = palabra  # Actualizar max_palabra

    return max_palabra

# Solicitar al usuario que ingrese una oración
entrada = input("Introduce una oración: ")
# Llamar a la función e imprimir el resultado
resultado = palabra_mas_larga(entrada)
print("La palabra más larga en la oración es:", resultado)