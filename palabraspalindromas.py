def palindroma(string):
    # Eliminar los espacios en blanco de la cadena
    string_sin_espacios = string.replace(" " , " , ")
    return string_sin_espacios == string_sin_espacios[::-1]
usuario = input("Por favor, ingresa una palabra o una oración para verificar si es palíndroma: ")
if palindroma(usuario):
    print(f"{usuario} es palíndroma.")
else:
    print(f"{usuario} no es palíndroma.")

